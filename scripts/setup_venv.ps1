# PowerShell script for Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Write-Output "Virtual environment created at .venv and requirements installed."