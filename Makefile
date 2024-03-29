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
	@echo "Creating app..."
	@cd $(CORE_DIR) && python ../manage.py startapp $(ARGS)
	@echo "App created."

.PHONY: migrate
migrate:
	@echo "Migrating database..."
	@cd $(SOURCE_DIR) && python manage.py migrate $(ARGS)
	@echo "Database migrated."