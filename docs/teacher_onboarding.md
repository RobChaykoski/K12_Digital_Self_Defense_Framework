# 👩‍🏫 Teacher Onboarding Guide: K12 Digital Self-Defense Framework

Welcome, educator! This guide prepares you to deliver engaging, hands-on cybersecurity lessons aligned with developmental stages. No prior coding experience is required.

---

## 📋 Table of Contents
- [1. Curriculum Overview](#curriculum-overview)
- [2. Program Structure](#program-structure)
- [3. CTF Challenge Format](#ctf-challenge-format)
- [4. Classroom Management Tips](#classroom-management-tips)
- [5. Assessment & Grading](#assessment--grading)
- [6. Common Questions](#common-questions)

---

## Curriculum Overview

The framework is divided into **three programs**, each targeting a specific developmental stage:

| Program | Grades | Focus | CTF Style |
|---------|--------|-------|-----------|
| **Program 1** | K–5 | Digital literacy, safe links, basic passwords | Visual sorting, QR decoding, physical lockboxes |
| **Program 2** | 6–8 | Social media safety, URL inspection, ciphers | Caesar cipher decryption, packet sniffing concepts |
| **Program 3** | 9–12 | AI forensics, MFA workflows, system boot | Boot2Root simulations, auth token analysis |

---

## Program Structure

Each program contains **7 standardized files**:

| File | Purpose | Teacher Use |
|------|---------|-------------|
| `01_Program_Guide.md` | Curriculum map & objectives | Planning overview |
| `02_Lesson_Plans.md` | Session-by-session instructions | Deliver lessons |
| `03_Student_Handouts.md` | Printable worksheets | Distribute to students |
| `04_Parent_Toolkit.md` | At-home reinforcement | Share via parent portal |
| `05_Assessments_and_Materials.md` | Rubrics & grading keys | Grade CTF submissions |
| `06_Persona_Cast.md` | Roleplay characters | Frame scenarios (e.g., "Agent Nova") |
| `07_CTF_Worksheets.md` | Capture-the-Flag challenges | Primary student activity |

> 💡 **Tip:** Read `02_Lesson_Plans.md` fully before teaching. Each lesson includes timing estimates and tech requirements.

---

## CTF Challenge Format

All challenges follow the standard flag format:
```
flag{your_answer_here}
```

### Example Flow (Program 1)
1. Student receives worksheet with link-sorting table
2. Scans QR code → lands on submission page
3. Enters `flag{3}` (if 3 safe links found)
4. System validates → displays ✅ or ❌

### Flag Validation
- Flags are **case-sensitive**
- Spaces and special characters must match exactly
- Use the rubric in `docs/ctf_scoring_rubric.md` for partial credit

---

## Classroom Management Tips

| Strategy | Implementation |
|----------|----------------|
| **Group Work** | Pair students for CTF challenges; rotate roles (scanner, decoder, recorder) |
| **Time Boxing** | Use a visible timer; allocate 15 min per challenge + 5 min debrief |
| **Leaderboard** | Create a simple whiteboard tracker: `Student | Flags Earned` |
| **Tech Troubleshooting** | Pre-test all QR codes; keep printed backups |
| **Differentiation** | Provide hint cards for struggling students; advanced extensions for fast finishers |

### Sample Lesson Flow (60-Minute Block)
```
0–10 min  → Introduction & persona briefing (06_Persona_Cast.md)
10–25 min → Guided worksheet completion (03_Student_Handouts.md)
25–45 min → CTF challenge execution (07_CTF_Worksheets.md)
45–55 min → Flag submission & validation
55–60 min → Debrief & preview next session
```

---

## Assessment & Grading

### Grading Rubric Overview
| Criteria | Points | Description |
|----------|--------|-------------|
| **Flag Accuracy** | 4 pts | Correct `flag{}` submission |
| **Reasoning Shown** | 2 pts | Worksheet explanations filled out |
| **Collaboration** | 2 pts | Peer assistance & role rotation |
| **Effort / Participation** | 2 pts | On-task behavior, time management |
| **Total** | **10 pts** | Per session |

> 📎 Full rubric: `docs/ctf_scoring_rubric.md`

### Progress Tracking
- Use the LMS gradebook to log weekly CTF scores
- Compile monthly reports for admin review
- Highlight "Digital Defender" achievements (5+ flags in a month)

---

## Common Questions

**Q: Do students need laptops/tablets?**  
A: Programs 1–2 work with printed worksheets + QR scanners. Program 3 benefits from computer lab access but can be adapted for paper-based metadata inspection.

**Q: How do I handle missing flags?**  
A: Allow resubmission within 48 hours. Deduct 1 point per late attempt. Document in `05_Assessments_and_Materials.md`.

**Q: Can I skip sessions?**  
A: Sessions build cumulatively. At minimum, teach Session 1 (Phishing/Link Sorting) before CTF challenges.

**Q: How do I report bugs or typos?**  
A: Open a [Bug Report Issue](https://github.com/RobChaykoski/K12_Digital_Self_Defense_Framework/issues/new?template=bug_report.md). Include file path and screenshot.

**Q: Is there a certification for students?**  
A: Yes! Upon completing all 7 sessions in a program, award the "Digital Self-Defense Certificate" (template provided in `assets/templates/`).

---

## 📞 Support
- **Email:** `rob.chaykoski@live.ca`
- **GitHub Issues:** [Lesson Feedback](https://github.com/RobChaykoski/K12_Digital_Self_Defense_Framework/issues/new?template=lesson_feedback.md)
- **Quick Start Video:** [Link to Loom walkthrough] *(add when recorded)*
