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
4. Run `make validate` to check links, anchors, paths, and CTF flag consistency
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
- **File Naming**: follow the neighbours in the folder you are editing. The numbered program series uses `NN_Title_Case` filenames such as `07_CTF_Worksheets.md`; `docs/` uses `lower_snake_case` such as `ctf_scoring_rubric.md`. Do not rename files without updating every reference — `make validate` checks this.

## 🧪 Testing & Validation

Run the validator before you commit. It exits non-zero on failure, so it works in CI:
```bash
python3 scripts/validate_repo.py   # conflict markers, BOMs, links and anchors, CTF flags
make validate                      # the same check, wrapped for make users
```
It checks that no merge-conflict marker survived, no file carries a UTF-8 BOM, every relative link and heading anchor resolves, and every CTF flag matches both its format rule and the scoring rubric.

## ❓ Questions?
Open a [Discussion](https://github.com/RobChaykoski/K12_Digital_Self_Defense_Framework/discussions) or tag `@RobChaykoski` in issues.

Thank you for helping students become digital defenders! 🛡️
