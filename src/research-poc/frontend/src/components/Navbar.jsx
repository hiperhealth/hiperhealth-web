import React, { useEffect, useMemo, useState } from "react";
import { Link, NavLink, useLocation } from "react-router-dom";
import { FiBell, FiChevronDown, FiMenu, FiSearch, FiX } from "react-icons/fi";
import "./Navbar.css";

const NAV_ITEMS = [
  { label: "Dashboard", to: "/", end: true },
  { label: "Patients", to: "/patients" },
  { label: "Records", to: "/medical-reports" },
  { label: "Analytics", to: "/analytics" },
];

export default function Navbar({
  appName = "Health Dashboard",
  addPatientTo = "/demographics",
  showSearch = true,
  showNotifications = true,
}) {
  const location = useLocation();
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [isProfileOpen, setIsProfileOpen] = useState(false);

  useEffect(() => {
    setIsMobileMenuOpen(false);
    setIsProfileOpen(false);
  }, [location.pathname]);

  const userInitials = useMemo(() => "SD", []);

  return (
    <nav className="app-navbar" aria-label="Main navigation">
      <div className="app-navbar__container">
        <div className="app-navbar__left">
          <Link to="/" className="app-navbar__brand" aria-label={`${appName} home`}>
            {appName}
          </Link>
        </div>

        <div className="app-navbar__center" aria-label="Primary links">
          {NAV_ITEMS.map((item) => (
            <NavLink
              key={item.label}
              to={item.to}
              end={item.end}
              className={({ isActive }) =>
                `app-navbar__link ${isActive ? "app-navbar__link--active" : ""}`
              }
            >
              {item.label}
            </NavLink>
          ))}
        </div>

        <div className="app-navbar__right">
          {showSearch ? (
            <form className="app-navbar__search" role="search" onSubmit={(event) => event.preventDefault()}>
              <FiSearch aria-hidden="true" />
              <input
                type="search"
                placeholder="Search patients..."
                aria-label="Search patients"
              />
            </form>
          ) : null}

          {showNotifications ? (
            <button
              type="button"
              className="app-navbar__icon-btn"
              aria-label="Notifications"
            >
              <FiBell aria-hidden="true" />
            </button>
          ) : null}

          <Link to={addPatientTo} className="app-navbar__cta" aria-label="Add patient">
            Add Patient
          </Link>

          <div className="app-navbar__profile-wrap">
            <button
              type="button"
              className="app-navbar__profile-btn"
              aria-label="Open profile menu"
              aria-expanded={isProfileOpen}
              onClick={() => setIsProfileOpen((prev) => !prev)}
            >
              <span className="app-navbar__avatar">{userInitials}</span>
              <FiChevronDown aria-hidden="true" />
            </button>

            {isProfileOpen ? (
              <div className="app-navbar__dropdown" role="menu" aria-label="Profile menu">
                <button type="button" role="menuitem">
                  Profile
                </button>
                <button type="button" role="menuitem">
                  Settings
                </button>
                <button type="button" role="menuitem">
                  Sign out
                </button>
              </div>
            ) : null}
          </div>

          <button
            type="button"
            className="app-navbar__menu-btn"
            aria-label={isMobileMenuOpen ? "Close menu" : "Open menu"}
            aria-expanded={isMobileMenuOpen}
            onClick={() => setIsMobileMenuOpen((prev) => !prev)}
          >
            {isMobileMenuOpen ? <FiX aria-hidden="true" /> : <FiMenu aria-hidden="true" />}
          </button>
        </div>
      </div>

      {isMobileMenuOpen ? (
        <div className="app-navbar__mobile-panel" aria-label="Mobile menu">
          {showSearch ? (
            <form className="app-navbar__search app-navbar__search--mobile" role="search" onSubmit={(event) => event.preventDefault()}>
              <FiSearch aria-hidden="true" />
              <input type="search" placeholder="Search patients..." aria-label="Search patients" />
            </form>
          ) : null}

          <div className="app-navbar__mobile-links">
            {NAV_ITEMS.map((item) => (
              <NavLink
                key={`mobile-${item.label}`}
                to={item.to}
                end={item.end}
                className={({ isActive }) =>
                  `app-navbar__mobile-link ${isActive ? "app-navbar__mobile-link--active" : ""}`
                }
              >
                {item.label}
              </NavLink>
            ))}
          </div>

          <Link to={addPatientTo} className="app-navbar__cta app-navbar__cta--mobile">
            Add Patient
          </Link>
        </div>
      ) : null}
    </nav>
  );
}
