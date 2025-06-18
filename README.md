# SomatigoX
Model for Auto-generate MongoDB query 

# Versions
Python: 3.10.11 

# Troubleshoot
 - For any dependencies issue, using python 3.10.11

# Quick Start
1. Create & activate a virtualenv
python -m venv .venv
source .venv/bin/activate   # PowerShell: .venv\Scripts\Activate.ps1
2. Install dev dependencies
pip install -e ".[dev]"     # pulls pytest + pyyaml
3. Run the unit tests
pytest                       # green ✅
4. Launch the sample app
python -m app.main
→ log lines in console and logs/app.log
