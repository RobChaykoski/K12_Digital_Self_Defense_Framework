# 🛡️ K12 Digital Self-Defense Framework

A comprehensive, age-appropriate cybersecurity and digital literacy curriculum for Kindergarten through Grade 12. Includes lesson plans, student handouts, parent toolkits, assessments, and hands-on Capture-the-Flag (CTF) scenarios aligned with the [Capture-the-Flag Cheat Sheet](https://uppusaikiran.github.io/hacking/Capture-the-Flag-CheatSheet/).

---

## 📖 Overview

| Component | Description |
|-----------|-------------|
| **Program 1** (K–5) | Foundations & Digital Literacy – Visual CTF, QR decoding, basic metadata |
| **Program 2** (6–8) | Social Dynamics & Web Safety – URL inspection, ciphers, packet sniffing concepts |
| **Program 3** (9–12) | Legal/AI & System Security – Boot2Root simulations, MFA workflows, deepfake forensics |

---

## 📂 Repository Structure

```
K12_Digital_Self_Defense_Framework/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── lesson_feedback.md
│   └── PULL_REQUEST_TEMPLATE.md
├── assets/
│   └── README.md
├── docs/
│   ├── README.md
│   ├── ctf_scoring_rubric.md
│   ├── implementation_guide.md
│   └── teacher_onboarding.md
├── scripts/
│   └── generate_qr.py
├── Phase_Plans/
│   ├── GECDSB_Monthly_Calendar_Integration.md
│   ├── Phase_1_K_Grade2_Ages5-8.md
│   ├── Phase_2_Grades3-5_Ages8-11.md
│   ├── Phase_3_Grades6-8_Ages11-14.md
│   └── Phase_4_Grades9-12_Ages14-18.md
├── Programs/
│   ├── Program_1_Foundations_K-5/
│   │   ├── 01_Program_Guide.md
│   │   ├── 02_Lesson_Plans.md
│   │   ├── 03_Student_Handouts.md
│   │   ├── 04_Parent_Toolkit.md
│   │   ├── 05_Assessments_and_Materials.md
│   │   ├── 06_Persona_Cast.md
│   │   └── 07_CTF_Worksheets.md
│   ├── Program_2_Social_Dynamics_Grades6-8/
│   │   ├── 01_Program_Guide.md
│   │   ├── 02_Lesson_Plans.md
│   │   ├── 03_Student_Handouts.md
│   │   ├── 04_Parent_Toolkit.md
│   │   ├── 05_Assessments_and_Materials.md
│   │   ├── 06_Persona_Cast.md
│   │   └── 07_CTF_Worksheets.md
│   └── Program_3_Legal_AI_Grades9-12/
│       ├── 01_Program_Guide.md
│       ├── 02_Lesson_Plans.md
│       ├── 03_Student_Handouts.md
│       ├── 04_Parent_Toolkit.md
│       ├── 05_Assessments_and_Materials.md
│       ├── 06_Persona_Cast.md
│       └── 07_CTF_Worksheets.md
├── CONTRIBUTING.md           # How to contribute
├── ECNO_Alignment_Guide.md   # Curriculum mapping to ECNO Digital Wellness standards
├── ISED_AI_for_All_Alignment.md  # ISED AI Literacy & AI for All alignment
├── K12_Cyber_Safety_Framework.md   # Master framework document
├── LICENSE                   # MIT License
├── Makefile                  # Build & validation helpers
├── README.md                 # This file
├── Stop_Think_Reinforcement.md   # Cross-phase Stop, Think, Ask, Break principle
└── _temp_tree.txt                # (auto-generated tree listing)
```

### File Purpose Summary

| Category | Description |
|----------|-------------|
| **Master Framework** | `K12_Cyber_Safety_Framework.md` — Full curriculum overview with ISED AI integration |
| **Phase Plans** | Age-band pacing documents (K-2, 3-5, 6-8, 9-12) with monthly integration |
| **Programs (×3)** | Core modules: Foundations (K-5), Social Dynamics (6-8), Legal/AI (9-12) |
| **Each Program Contains** | Program Guide, Lesson Plans, Student Handouts, Parent Toolkit, Assessments, Persona Cast, CTF Worksheets |
| **Supporting Docs** | `Stop_Think_Reinforcement.md`, `ISED_AI_for_All_Alignment.md`, `ECNO_Alignment_Guide.md` |
| **Implementation** | `docs/` — Onboarding, implementation guide, CTF scoring rubric |
| **Automation** | `scripts/` — QR code generation |
| **Templates** | `.github/` — Issue & PR templates for community feedback |

---

## 🚀 Quick Start

### 1. Clone & Explore
```bash
git clone https://github.com/RobChaykoski/K12_Digital_Self_Defense_Framework.git
cd K12_Digital_Self_Defense_Framework
```

### 2. Validate Markdown
```bash
make validate
```

### 3. Generate QR Codes for Worksheets
```bash
python scripts/generate_qr.py "https://your-landing.com/flag" "worksheet_qr.png"
```

### 4. Export Handouts to PDF
```bash
make pdf-export
```

---

## 📚 Documentation & Guides

- [Implementation Guide](docs/implementation_guide.md) – LMS setup & district rollout
- [Teacher Onboarding](docs/teacher_onboarding.md) – Training materials for instructors
- [CTF Scoring Rubric](docs/ctf_scoring_rubric.md) – Grading & flag validation
- [ECNO Alignment Guide](ECNO_Alignment_Guide.md) – Curriculum mapping to standards

---

## 🤝 Contributing
We welcome lesson feedback, worksheet improvements, and new CTF scenarios. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
