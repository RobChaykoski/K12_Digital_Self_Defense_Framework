# 📘 Implementation Guide: K12 Digital Self-Defense Framework

This guide provides step-by-step instructions for deploying the curriculum in school districts, integrating with Learning Management Systems (LMS), and rolling out to teachers.

---

## 📋 Table of Contents
- [1. Prerequisites](#prerequisites)
- [2. LMS Integration](#lms-integration)
- [3. District Rollout Strategy](#district-rollout-strategy)
- [4. Teacher Preparation](#teacher-preparation)
- [5. Student Onboarding](#student-onboarding)
- [6. Troubleshooting](#troubleshooting)

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| **Device Access** | 1:1 tablets, Chromebooks, or computer lab access |
| **Internet** | Required for CTF web challenges and QR scanning |
| **LMS Account** | Canvas, Google Classroom, Schoology, or Microsoft Teams |
| **Teacher Training** | Complete `docs/teacher_onboarding.md` before first session |
| **QR Scanner App** | Pre-installed on student devices (or use built-in camera) |

---

## LMS Integration

### Canvas
1. Navigate to your course → **Settings** → **Import Course Content**
2. Select `GitHub Repository` or upload PDF handouts from `exports/pdf/`
3. Create a module per session and attach:
   - `02_Lesson_Plans.md` (as Rich Text)
   - `07_CTF_Worksheets.md` (as File Upload or Page)
4. Enable **Student Analytics** to track worksheet submissions

### Google Classroom
1. Create a new class → **Classwork** → **Material**
2. Upload `Programs/*/03_Student_Handouts.pdf` as a resource
3. Create an assignment for each CTF session using the flag format:
   ```
   Submit your answer here: flag{your_answer}
   ```
4. Use **Question** type for quick checks before CTF challenges

### Schoology / Microsoft Teams
- Upload PDF handouts to **Resources** or **Files** tabs
- Embed QR codes as images linking to submission forms
- Use **Quizzes** for flag validation and auto-grading

---

## District Rollout Strategy

| Phase | Timeline | Activities |
|-------|----------|------------|
| **Phase 1: Pilot** | Weeks 1–2 | Select 2–3 teachers, run Program 1 (K–5), gather feedback via `.github/ISSUE_TEMPLATE/lesson_feedback.md` |
| **Phase 2: Expansion** | Weeks 3–6 | Roll out to all K–8 schools, host virtual Q&A sessions |
| **Phase 3: Full Deployment** | Weeks 7–10 | Integrate Program 3 (9–12), launch inter-school CTF competition |
| **Phase 4: Review & Iterate** | Ongoing | Compile teacher feedback, update worksheets, publish v2.0 |

### ECNO Alignment Verification Checklist
- [ ] All sessions map to at least one ECNO category (Cyber Safety Basics, Digital Wellness, AI, Social Media/Gaming)
- [ ] Ontario-specific resources referenced: Cybertip.ca, NeedHelpNow.ca, Take It Down, Kids Help Phone
- [ ] French-language resources available for bilingual schools (Mois de la Cybersensibilisation)
- [ ] October Cyber Awareness Month campaign dates synced with framework rollout
- [ ] ECNO "Cyber Heroes Unite" activity packs integrated into K–5 sessions

### Rollout Checklist
- [ ] Print QR codes and attach to physical worksheets
- [ ] Distribute `Programs/*/04_Parent_Toolkit.md` via parent portal
- [ ] Schedule 30-min teacher sync before first CTF session
- [ ] Configure LMS grading rubrics (see `docs/ctf_scoring_rubric.md`)
- [ ] Test QR code scanning on district-issued devices

---

## Teacher Preparation

1. **Review Lesson Plans** (`02_Lesson_Plans.md`) 48 hours before delivery
2. **Print Worksheets** → `exports/pdf/` or copy-paste into LMS
3. **Generate QR Codes** → Run `python scripts/generate_qr.py "URL" "filename.png"`
4. **Set Up Flag Submission** → Create a Google Form, Microsoft Form, or custom landing page
5. **Run a Dry-Run** → Complete the CTF challenge yourself to verify flag formats

---

## Student Onboarding

### First Session Script (K–5)
> "Welcome, Digital Defenders! Today we're going on a treasure hunt. Each worksheet has a QR code that leads to a secret flag. When you solve the puzzle correctly, you'll unlock `flag{your_answer}`. Let's see who can find all the hidden links!"

### First Session Script (6–8)
> "You've joined the Cyber Squad. Your mission: inspect URLs, decode ciphers, and sniff out fake packets. Each session ends with a CTF challenge. Submit your flags to earn points and climb the leaderboard."

### First Session Script (9–12)
> "Welcome to Digital Self-Defense 101. You'll explore web forensics, AI deepfake detection, and system boot sequences. Flags follow `flag{description}` format. Submit via LMS or our competition portal."

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| QR code won't scan | Ensure image is saved as `.png` (not `.jpg`) and resolution ≥ 300 DPI |
| Flag rejected by LMS | Verify exact casing: `flag{lowercase_description}` |
| Worksheet formatting broken | Use `make validate` to check markdown syntax |
| Student lacks device access | Pair students; use printed handouts with teacher-provided QR codes |
| CTF challenge too easy/hard | Adjust flag difficulty in `07_CTF_Worksheets.md` or add hint steps |

---

## 📞 Support & Feedback
- Open a [Lesson Feedback Issue](https://github.com/RobChaykoski/K12_Digital_Self_Defense_Framework/issues/new?template=lesson_feedback.md)
- Email: `rob.chaykoski@live.ca`
- Community Discussions: [GitHub Discussions](https://github.com/RobChaykoski/K12_Digital_Self_Defense_Framework/discussions)
