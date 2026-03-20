import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

export default function Register() {
  const { register } = useAuth();
  const navigate = useNavigate();
  const [form, setForm] = useState({
    username: "",
    email: "",
    password: "",
    confirm: "",
  });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handle = (field) => (e) =>
    setForm((f) => ({ ...f, [field]: e.target.value }));

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    if (form.password !== form.confirm) {
      setError("Passwords do not match.");
      return;
    }
    setLoading(true);
    try {
      await register(form.username, form.email, form.password);
      navigate("/login");
    } catch (err) {
      setError(err.message || "Registration failed.");
    } finally {
      setLoading(false);
    }
  };

  const inputStyle = {
    width: "100%",
    padding: "10px 14px",
    borderRadius: "8px",
    border: "1px solid rgba(255,255,255,0.15)",
    background: "rgba(255,255,255,0.07)",
    color: "#fff",
    fontSize: "1rem",
    boxSizing: "border-box",
  };

  const labelSpanStyle = {
    color: "#cbd5e1",
    fontSize: "0.875rem",
    display: "block",
    marginBottom: "6px",
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        background: "linear-gradient(135deg, #0f172a 0%, #1e3a5f 100%)",
      }}
    >
      <div
        style={{
          background: "rgba(255,255,255,0.05)",
          backdropFilter: "blur(12px)",
          border: "1px solid rgba(255,255,255,0.12)",
          borderRadius: "16px",
          padding: "48px",
          width: "100%",
          maxWidth: "420px",
          boxShadow: "0 24px 64px rgba(0,0,0,0.4)",
        }}
      >
        <h1
          style={{
            color: "#fff",
            fontSize: "1.75rem",
            fontWeight: 700,
            marginBottom: "8px",
          }}
        >
          Create Account
        </h1>
        <p style={{ color: "#94a3b8", marginBottom: "32px" }}>
          Register to access the Physician Portal
        </p>

        {error && (
          <div
            style={{
              background: "rgba(239,68,68,0.15)",
              border: "1px solid rgba(239,68,68,0.4)",
              borderRadius: "8px",
              padding: "12px",
              color: "#fca5a5",
              marginBottom: "16px",
              fontSize: "0.875rem",
            }}
          >
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          {[
            { field: "username", label: "Username", type: "text", id: "reg-username" },
            { field: "email", label: "Email", type: "email", id: "reg-email" },
            { field: "password", label: "Password", type: "password", id: "reg-password" },
            { field: "confirm", label: "Confirm Password", type: "password", id: "reg-confirm" },
          ].map(({ field, label, type, id }) => (
            <label key={field} style={{ display: "block", marginBottom: "16px" }}>
              <span style={labelSpanStyle}>{label}</span>
              <input
                id={id}
                type={type}
                value={form[field]}
                onChange={handle(field)}
                required
                style={inputStyle}
              />
            </label>
          ))}

          <button
            id="register-submit"
            type="submit"
            disabled={loading}
            style={{
              width: "100%",
              padding: "12px",
              borderRadius: "8px",
              border: "none",
              background: loading
                ? "rgba(99,102,241,0.5)"
                : "linear-gradient(90deg, #6366f1, #8b5cf6)",
              color: "#fff",
              fontSize: "1rem",
              fontWeight: 600,
              cursor: loading ? "not-allowed" : "pointer",
              marginTop: "8px",
            }}
          >
            {loading ? "Creating account…" : "Create account"}
          </button>
        </form>

        <p
          style={{
            textAlign: "center",
            marginTop: "24px",
            color: "#94a3b8",
            fontSize: "0.875rem",
          }}
        >
          Already have an account?{" "}
          <Link to="/login" style={{ color: "#818cf8" }}>
            Sign in
          </Link>
        </p>
      </div>
    </div>
  );
}
