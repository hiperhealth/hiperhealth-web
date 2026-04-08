import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Dashboard from "./components/dashboard/Dashboard";
import PatientView from "./components/dashboard/PatientView";
import LanguageSelection from "./components/consultation/LanguageSelection";
import "./i18";
import Demographics from "./components/consultation/Demographics";
import Lifestyle from "./components/consultation/Lifestyle";
import Symptoms from "./components/consultation/Symptoms";
import Mental from "./components/consultation/Mental";
import MedicalReport from "./components/consultation/MedicalReport";
import Wearable from "./components/consultation/Wearable";
import Diagnosis from "./components/consultation/Diagnosis";
import Exam from "./components/consultation/Exam";
import Confirmation from "./components/consultation/Confirmation";
import { AuthProvider } from "./context/AuthContext";
import Login from "./components/auth/Login";
import Register from "./components/auth/Register";
import PrivateRoute from "./components/auth/PrivateRoute";

export default function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          {/* Public routes */}
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />

          {/* Protected routes */}
          <Route
            path="/"
            element={
              <PrivateRoute>
                <Dashboard />
              </PrivateRoute>
            }
          />
          <Route
            path="/patients/:id"
            element={
              <PrivateRoute>
                <PatientView />
              </PrivateRoute>
            }
          />
          <Route
            path="/language"
            element={
              <PrivateRoute>
                <LanguageSelection />
              </PrivateRoute>
            }
          />
          <Route
            path="/demographics"
            element={
              <PrivateRoute>
                <Demographics />
              </PrivateRoute>
            }
          />
          <Route
            path="/lifestyle"
            element={
              <PrivateRoute>
                <Lifestyle />
              </PrivateRoute>
            }
          />
          <Route
            path="/symptoms"
            element={
              <PrivateRoute>
                <Symptoms />
              </PrivateRoute>
            }
          />
          <Route
            path="/mental"
            element={
              <PrivateRoute>
                <Mental />
              </PrivateRoute>
            }
          />
          <Route
            path="/medical-reports"
            element={
              <PrivateRoute>
                <MedicalReport />
              </PrivateRoute>
            }
          />
          <Route
            path="/wearable-data"
            element={
              <PrivateRoute>
                <Wearable />
              </PrivateRoute>
            }
          />
          <Route
            path="/diagnosis"
            element={
              <PrivateRoute>
                <Diagnosis />
              </PrivateRoute>
            }
          />
          <Route
            path="/exams"
            element={
              <PrivateRoute>
                <Exam />
              </PrivateRoute>
            }
          />
          <Route
            path="/confirmation"
            element={
              <PrivateRoute>
                <Confirmation />
              </PrivateRoute>
            }
          />
          <Route
            path="*"
            element={
              <PrivateRoute>
                <Dashboard />
              </PrivateRoute>
            }
          />
        </Routes>
      </Router>
    </AuthProvider>
  );
}
