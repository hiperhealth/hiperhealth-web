import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

export default function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      await login(email, password);
      navigate("/");
    } catch (err) {
      setError(err.message || "Login failed. Please try again.");
    } finally {
      setLoading(false);
    }
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
          Physician Portal
        </h1>
        <p style={{ color: "#94a3b8", marginBottom: "32px" }}>
          Sign in to your account
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
          <label style={{ display: "block", marginBottom: "16px" }}>
            <span
              style={{
                color: "#cbd5e1",
                fontSize: "0.875rem",
                display: "block",
                marginBottom: "6px",
              }}
            >
              Email or Username
            </span>
            <input
              id="login-email"
              type="text"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              style={{
                width: "100%",
                padding: "10px 14px",
                borderRadius: "8px",
                border: "1px solid rgba(255,255,255,0.15)",
                background: "rgba(255,255,255,0.07)",
                color: "#fff",
                fontSize: "1rem",
                boxSizing: "border-box",
              }}
            />
          </label>

          <label style={{ display: "block", marginBottom: "24px" }}>
            <span
              style={{
                color: "#cbd5e1",
                fontSize: "0.875rem",
                display: "block",
                marginBottom: "6px",
              }}
            >
              Password
            </span>
            <input
              id="login-password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              style={{
                width: "100%",
                padding: "10px 14px",
                borderRadius: "8px",
                border: "1px solid rgba(255,255,255,0.15)",
                background: "rgba(255,255,255,0.07)",
                color: "#fff",
                fontSize: "1rem",
                boxSizing: "border-box",
              }}
            />
          </label>

          <button
            id="login-submit"
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
              transition: "opacity 0.2s",
            }}
          >
            {loading ? "Signing in…" : "Sign in"}
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
          No account?{" "}
          <Link to="/register" style={{ color: "#818cf8" }}>
            Register here
          </Link>
        </p>
      </div>
    </div>
  );
}
