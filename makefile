ACT ?= act
WORKFLOW_FILE := .github/workflows/validate-ics.yml
JOB_NAME := validate-ics

ACT_PLATFORM ?= ubuntu-latest=ghcr.io/catthehacker/ubuntu:act-22.04

.PHONY: help validate validate-ics

help:
	@echo "Available targets:"
	@echo "  make validate       - Run ICS validation workflow locally via act"
	@echo "  make validate-ics   - Same as 'validate' (explicit name)"
	@echo ""
	@echo "Requirements:"
	@echo "  - Docker running"
	@echo "  - act installed (https://github.com/nektos/act)"

validate: validate-ics

validate-ics:
	@echo "▶ Running GitHub Actions workflow locally: $(WORKFLOW_FILE) (job: $(JOB_NAME))"
	@$(ACT) -P $(ACT_PLATFORM) -W $(WORKFLOW_FILE) -j $(JOB_NAME)
