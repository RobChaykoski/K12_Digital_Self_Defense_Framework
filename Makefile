# Build helpers for the K-12 Digital Self-Defense Framework.
#
# None of these are required to read or teach the material; they exist for
# contributors. On Windows, run them from Git Bash or WSL, or invoke the Python
# scripts directly.
#
# `make validate` is a real gate: it exits non-zero when anything fails. The
# previous version ended in `|| echo ...`, which meant it printed a warning and
# returned success no matter what it found.

.PHONY: validate lint qr-generate pdf-export clean help

PYTHON ?= python3
PANDOC ?= pandoc

help:
	@echo "K12 Digital Self-Defense Framework - build helpers"
	@echo ""
	@echo "  make validate     - Conflict markers, BOMs, links/anchors, CTF flags"
	@echo "  make lint         - Markdown style check (needs markdownlint-cli)"
	@echo "  make qr-generate  - Generate a QR code for CTF worksheets"
	@echo "  make pdf-export   - Compile handouts to PDF (needs pandoc)"
	@echo "  make clean        - Remove generated artifacts"
	@echo "  make help         - Show this message"

validate:
	@$(PYTHON) scripts/validate_repo.py

lint:
	@command -v markdownlint >/dev/null 2>&1 || { \
		echo "markdownlint not installed. Install with: npm install -g markdownlint-cli"; \
		exit 1; \
	}
	@markdownlint "**/*.md" --ignore "_archive/**" --ignore "node_modules/**"

qr-generate:
	@echo "Generating QR code..."
	@$(PYTHON) scripts/generate_qr.py "https://your-landing-page.com/submit-flag" "master_flag_submission.png"
	@echo "Generated assets/qr_*.png files are git-ignored; edit scripts/generate_qr.py for worksheet-specific URLs."

pdf-export:
	@command -v $(PANDOC) >/dev/null 2>&1 || { \
		echo "pandoc not installed. See https://pandoc.org/installing.html"; \
		exit 1; \
	}
	@mkdir -p exports/pdf
	@for f in Programs/*/03_Student_Handouts.md; do \
		$(PANDOC) "$$f" -o "exports/pdf/$$(basename "$${f%.md}").pdf" --standalone --section-divs; \
	done
	@echo "PDFs written to exports/pdf/ (git-ignored)."

clean:
	@rm -rf exports assets/qr_*.png
	@echo "Removed generated artifacts."
