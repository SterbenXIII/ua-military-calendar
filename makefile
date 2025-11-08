POETRY ?= poetry
ACT ?= act

WORKFLOW_FILE := .github/workflows/validate-ics.yml
JOB_NAME := validate-ics
ACT_PLATFORM ?= ubuntu-latest=ghcr.io/catthehacker/ubuntu:act-22.04

.PHONY: help install lint lint-ics validate validate-ics

help:
	@echo "Available targets:"
	@echo "  make install        - Install Python dependencies via Poetry"
	@echo "  make lint           - Lint all .ics files (alias for lint-ics)"
	@echo "  make lint-ics       - Run ICS linter with Poetry (scripts/lint_ics.py)"
	@echo "  make validate       - Run GitHub Actions workflow locally via act"
	@echo "  make validate-ics   - Same as 'make validate'"

install:
	@echo "▶ Installing dependencies with Poetry"
	@$(POETRY) install

lint: lint-ics

lint-ics:
	@echo "▶ Linting ICS files via Poetry"
	@$(POETRY) run python scripts/lint_ics.py

validate: validate-ics

validate-ics:
	@echo "▶ Running GitHub Actions workflow locally with act"
	@$(ACT) -P $(ACT_PLATFORM) -W $(WORKFLOW_FILE) -j $(JOB_NAME)
