import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const Navbar = () => {
  const [patients, setPatients] = useState([]);
  const [selected, setSelected] = useState("");
  const navigate = useNavigate();

  // Fetch patients
  useEffect(() => {
    fetch("http://localhost:8000/api/patients")
      .then((res) => res.json())
      .then((data) => setPatients(data))
      .catch((err) => console.error("Error:", err));
  }, []);

  // Handle patient switch
  const handleChange = (e) => {
    const id = e.target.value;
    setSelected(id);
    if (id) navigate(`/patient/${id}`);
  };

  // Resume consultation
  const handleResume = async () => {
    if (!selected) return;

    const res = await fetch(
      `http://localhost:8000/api/consultations/${selected}/status`
    );
    const data = await res.json();

    const step = data.current_step || "demographics";

    // map backend step → frontend route
    const routeMap = {
      demographics: "/demographics",
      lifestyle: "/lifestyle",
      symptoms: "/symptoms",
      mental: "/mental",
      reports: "/reports",
      wearable: "/wearable",
      diagnosis: "/diagnosis",
      exams: "/exams",
    };

    navigate(`/consult/${selected}${routeMap[step]}`);
  };

  return (
    <nav style={styles.nav}>
      <h3>Patient Dashboard</h3>

      <select value={selected} onChange={handleChange}>
        <option value="">Select Patient</option>
        {patients.map((p) => (
          <option key={p.id} value={p.id}>
            {p.name || `Patient ${p.id}`}
          </option>
        ))}
      </select>

      <button onClick={handleResume}>Resume</button>
    </nav>
  );
};

const styles = {
  nav: {
    display: "flex",
    gap: "10px",
    padding: "10px",
    background: "#f5f5f5",
  },
};

export default Navbar;