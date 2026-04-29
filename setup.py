"""Setup script with frontend build integration."""

import subprocess

from pathlib import Path

from setuptools import setup
from setuptools.command.build_py import build_py
from setuptools.command.develop import develop
from setuptools.command.install import install


def install_frontend_dependencies():
    """Install npm dependencies for the frontend."""
    frontend_dir = Path(__file__).parent / "src" / "research" / "frontend"

    if not frontend_dir.exists():
        print("Frontend directory not found, skipping npm install.")
        return

    package_json = frontend_dir / "package.json"
    if not package_json.exists():
        print("package.json not found, skipping npm install.")
        return

    # Check if npm is available
    try:
        subprocess.run(
            ["npm", "--version"],
            check=True,
            capture_output=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(
            "Warning: npm not found - skipping frontend"
            " dependency installation."
        )
        return

    print("Installing frontend dependencies...")
    lock_file = frontend_dir / "package-lock.json"

    npm_cmd = (
        ["npm", "ci", "--no-audit", "--no-fund"]
        if lock_file.exists()
        else ["npm", "install", "--no-audit", "--no-fund"]
    )

    result = subprocess.run(
        npm_cmd,
        cwd=frontend_dir,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Warning: npm install failed: {result.stderr}")
    else:
        print("Frontend dependencies installed successfully.")


def build_frontend():
    """Build the frontend for production."""
    frontend_dir = Path(__file__).parent / "src" / "research" / "frontend"

    if not frontend_dir.exists():
        return

    node_modules = frontend_dir / "node_modules"
    if not node_modules.exists():
        print("node_modules not found, running npm install first...")
        install_frontend_dependencies()

    print("Building frontend...")
    result = subprocess.run(
        ["npm", "run", "build"],
        cwd=frontend_dir,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Warning: Frontend build failed: {result.stderr}")
    else:
        print("Frontend built successfully.")


class CustomBuildPy(build_py):
    """Custom build_py command that installs and builds frontend."""

    def run(self):
        """Install frontend deps and build, then run default build."""
        install_frontend_dependencies()
        build_frontend()
        super().run()


class CustomDevelop(develop):
    """Custom develop command that installs frontend dependencies."""

    def run(self):
        """Install frontend deps, then run default develop install."""
        install_frontend_dependencies()
        super().run()


class CustomInstall(install):
    """Custom install command that installs frontend dependencies."""

    def run(self):
        """Install frontend deps, then run default install."""
        install_frontend_dependencies()
        super().run()


setup(
    cmdclass={
        "build_py": CustomBuildPy,
        "develop": CustomDevelop,
        "install": CustomInstall,
    },
)
