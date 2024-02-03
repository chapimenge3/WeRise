# Makefile for Alembic commands

# Define variables
PYTHON = python
ALEMBIC = alembic
DATE = $(shell date +"%Y%m%d%H%M%S")

# Set default target
.DEFAULT_GOAL := help

# Help message
help:
	@echo "Available targets:"
	@echo "  make run-db          - Run docker database"
	@echo "  make migrate         - Run database migrations"
	@echo "  make upgrade         - Upgrade the database to the latest revision"
	@echo "  make downgrade       - Downgrade the database by one revision"
	@echo "  make revision        - Create a new migration revision"
	@echo "    Usage: make revision [message='Your migration message here']"


# Run docker database
run-db:
	docker compose up -d

# Run database migrations
migrate:
	$(ALEMBIC) upgrade head

# Upgrade the database to the latest revision
upgrade:
	$(ALEMBIC) upgrade head

# Downgrade the database by one revision
downgrade:
	$(ALEMBIC) downgrade -1

# Create a new migration revision
revision:
	$(eval message ?= "Automatic migration on $(shell date +'%Y-%m-%d %H:%M:%S')")
	@echo "Creating migration revision: $(message)"
	$(ALEMBIC) revision --autogenerate -m "$(message)"
