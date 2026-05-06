/* eslint-disable react-refresh/only-export-components */
import React, { createContext, useContext, useReducer, useEffect } from 'react';
import { initialState, consultationReducer, consultationActions } from './ConsultationReducer';

//Context Creation
const ConsultationContext = createContext(initialState);

//Helper to get localStorage key scoped to patient
const getStorageKey= (patientId)=>
  patientId?`consultationState_${patientId}`:'consultationState_temp';


//Provider Component
export function ConsultationProvider({ children }) {
  const [state, dispatch] = useReducer(
    consultationReducer,
    initialState,
    (initial) => {
      try {
        const tempSaved = localStorage.getItem('consultationState_temp');
        if (tempSaved) {
          const parsed = JSON.parse(tempSaved);
          let loadedState = parsed;
          if (parsed.patientId) {
            const patientSaved = localStorage.getItem(getStorageKey(parsed.patientId));
            if (patientSaved) {
                loadedState = JSON.parse(patientSaved);
            }
          }
          // Merge loaded state with initial state to ensure all nested properties exist
          return {
            ...initial,
            ...loadedState,
            formData: {
                ...initial.formData,
                ...(loadedState.formData || {})
            }
          };
        }
        return initial;
      } catch (e) {
        console.error('Failed to load state:', e);
        return initial;
      }
    }
  );

  useEffect(() => {
    if(!state.patientId){
      localStorage.removeItem('consultationState_temp');
      return;
    }
    const key=getStorageKey(state.patientId);
    const stateToSave={
      patientId: state.patientId,
      language: state.language,
      currentStep: state.currentStep,
      formData: state.formData,
    };
    localStorage.setItem(key,JSON.stringify(stateToSave));
    localStorage.setItem('consultationState_temp',JSON.stringify(stateToSave));
  }, [state]);

  const value = { state, dispatch };

  return (
    <ConsultationContext.Provider value={value}>
      {children}
    </ConsultationContext.Provider>
  );
}


//Custom Hook
export function useConsultation() {
  const context = useContext(ConsultationContext);
  if (!context) {
    throw new Error(
      'useConsultation must be used within a ConsultationProvider. ' +
        'Make sure your App is wrapped with <ConsultationProvider> in main.jsx'
    );
  }
  return context;
}

export { consultationActions };
export default ConsultationContext;
