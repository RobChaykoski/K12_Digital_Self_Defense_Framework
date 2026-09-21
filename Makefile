.PHONY: validate qr-generate pdf-export help

help:
	@echo "📚 K12 Digital Self-Defense Framework - Build Helpers"
	@echo ""
	@echo "  make validate     - Check markdown syntax & formatting"
	@echo "  make qr-generate  - Generate QR codes for CTF worksheets"
	@echo "  make pdf-export   - Compile handouts to PDF (requires pandoc)"
	@echo "  make clean        - Remove generated assets"
	@echo "  make help         - Show this message"

validate:
	@echo "🔍 Validating markdown files..."
	@find . -name "*.md" ! -path "./.git/*" -exec markdownlint {} \; 2>/dev/null || echo "⚠️ markdownlint not installed. Install with: npm install -g markdownlint-cli"
	@echo "✅ Validation complete. Check output above."

qr-generate:
	@echo "📱 Generating QR codes for CTF worksheets..."
	@python3 scripts/generate_qr.py "https://your-landing-page.com/submit-flag" "master_flag_submission.png"
	@echo "💡 Edit scripts/generate_qr.py to add worksheet-specific URLs."

pdf-export:
	@echo "📄 Exporting handouts to PDF..."
	@mkdir -p exports/pdf
	@for f in Programs/*/03_Student_Handouts.md; do \
		pandoc "$$f" -o "exports/pdf/$$(basename $${f%.md}).pdf" --standalone --section-divs 2>/dev/null || echo "⚠️ Pandoc failed for $$f"; \
	done
	@echo "✅ PDFs saved to exports/pdf/"

clean:
	@echo "🧹 Cleaning generated assets..."
	@rm -rf assets/qr_codes/*.png exports/
	@echo "✅ Cleanup complete."
