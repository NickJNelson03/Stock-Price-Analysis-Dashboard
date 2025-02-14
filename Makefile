PYTHON = python3  
VENV = venv 
REQS = requirements.txt

setup:
	@echo "📦 Setting up virtual environment..."
	$(PYTHON) -m venv $(VENV)
	@echo "✅ Virtual environment created."

install:
	@echo "📦 Installing dependencies..."
	$(VENV)/bin/pip install -r $(REQS)
	@echo "✅ Dependencies installed."

run:
	@echo "🚀 Running fetch_data.py..."
	$(VENV)/bin/python fetch_data.py
	@echo "✅ Script execution completed."

full-setup: setup install
	@echo "🚀 Full setup completed."

clean:
	@echo "🧹 Removing virtual environment..."
	rm -rf $(VENV)
	@echo "✅ Cleanup complete."

push:
	git status
	@for file in $$(git status --porcelain | awk '{print $$2}'); do \
		read -p "Enter commit message for $$file: " msg; \
		git add $$file; \
		git commit -m "$$msg"; \
	done; \
	git push origin main

.PHONY: setup install run full-setup push
