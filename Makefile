SOURCE_DIR=src
CORE_DIR=$(SOURCE_DIR)/core
ARGS ?=

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


.PHONY: runserver
runserver:
	@echo "Migrating database..."
	@python manage.py migrate
	@echo "Database migrated."

	@echo "Collecting static files..."
	@python manage.py collectstatic --noinput
	@echo "Static files collected."

	@echo "Starting server..."
	@python manage.py runserver 0.0.0.0:8000
