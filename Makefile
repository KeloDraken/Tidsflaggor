SOURCE_DIR=src
CORE_DIR=$(SOURCE_DIR)/core
ARGS ?=

.PHONY: project_setup
project_setup:
	@echo "Setting up project..."
	@echo "Installing dependencies..."
	@pip install -r requirements.txt
	@echo "Project setup complete."

.PHONY: startapp
startapp:
	@cd $(CORE_DIR) && python ../manage.py startapp $(ARGS)

.PHONY: migrate
migrate:
	@cd $(SOURCE_DIR) && python manage.py migrate $(ARGS)