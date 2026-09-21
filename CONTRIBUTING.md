# Contributing to K12 Digital Self-Defense Framework

Thank you for your interest in contributing! This framework is designed for educators, instructional designers, and cybersecurity professionals to deliver age-appropriate digital literacy and CTF-based learning.

## 📋 How to Contribute

### 1. Report Issues / Feedback
Use the [Issue Templates](.github/ISSUE_TEMPLATE/) to submit:
- **Lesson Feedback** – Classroom implementation notes, student engagement observations
- **Bug Reports** – Typos, broken links, formatting issues in worksheets
- **Feature Requests** – New CTF scenarios, additional handouts, LMS integration ideas

### 2. Submit Pull Requests
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Run `make validate` to check markdown formatting
5. Submit a PR with the template filled out

### 3. Code of Conduct
- Be respectful and inclusive
- Provide constructive feedback
- Test worksheets before submitting

## 📝 Style Guidelines

- **Markdown**: Use H2 (`##`) for section headers, H3 (`###`) for subsections
- **CTF Flags**: Format as `flag{description}`
- **Tables**: Align columns for readability
- **Images/Assets**: Place in `/assets/` and reference with relative paths
- **File Naming**: Use snake_case (e.g., `07_ctf_worksheets.md`)

## 🧪 Testing & Validation

Run the included scripts to validate your changes:
```bash
make validate    # Check markdown syntax
make qr-generate # Generate QR codes for worksheets
make pdf-export  # Compile handouts to PDF (requires pandoc)
```

## ❓ Questions?
Open a [Discussion](https://github.com/RobChaykoski/K12_Digital_Self_Defense_Framework/discussions) or tag `@RobChaykoski` in issues.

Thank you for helping students become digital defenders! 🛡️
