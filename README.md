````markdown
# OctoFit Tracker App (skeleton)

This branch contains a minimal OctoFit Tracker application skeleton and helper scripts to create a Python virtual environment and install dependencies.

Quick start (UNIX / macOS):

1. Ensure you have Python 3.8+ installed.
2. Run the setup script to create a virtual environment and install requirements:

```bash
chmod +x scripts/setup_venv.sh
./scripts/setup_venv.sh
```

3. Activate the virtual environment:

```bash
source .venv/bin/activate
```

4. Run the app:

```bash
python -m octofit
```

Quick start (Windows PowerShell):

```powershell
.\scripts\setup_venv.ps1
.\.venv\Scripts\Activate.ps1
python -m octofit
```

Files added:
- octofit/ (package)
  - __init__.py
  - app.py
  - __main__.py
- requirements.txt
- scripts/setup_venv.sh
- scripts/setup_venv.ps1
- .gitignore

````