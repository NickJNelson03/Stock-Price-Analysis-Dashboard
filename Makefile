VENV = venv

run:
@echo "Running fetch_data.py..."
$(VENV)/bin/python fetch_data.py
@echo "Script execution completed."
