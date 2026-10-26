# 🛡️ K12 Digital Self-Defense Framework

A complete, age-appropriate cybersecurity and AI-literacy curriculum for Kindergarten through Grade 12. It ships as three sequential programs, four phase plans, parent toolkits, assessments, and hands-on Capture-the-Flag (CTF) scenarios mapped to the [Capture-the-Flag Cheat Sheet](https://uppusaikiran.github.io/hacking/Capture-the-Flag-CheatSheet/).

**Version 3.0** — see [CHANGELOG.md](CHANGELOG.md) for what changed and why. If you have already trained staff on 2.x, read the v3.0.0 entry before your next session.

---

## 🎯 What this is

| Component | Description |
|-----------|-------------|
| **Program 1** (K–5) | Foundations & digital literacy — two tracks: Little Guardians (K–2, 6 sessions) and Digital Detectives (3–5, 8 sessions). Visual CTF, safe-linking, early AI concepts |
| **Program 2** (6–8) | Social dynamics & web safety — 10 sessions. Social engineering, MFA, voice cloning, sextortion response, ciphers, unencrypted traffic |
| **Program 3** (9–12) | Legal, AI & system security — 12 sessions. Credential audits, passkeys, media provenance, sextortion economics, crypto scams, Canadian law |

Everything is plain Markdown so it can be read on GitHub, printed, pasted into an LMS, or exported to PDF. There is no build step required to teach from it.

---

## 📂 Repository layout

```
.
├── .github/
│   ├── ISSUE_TEMPLATE/          # bug report, feature request, lesson feedback
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/validate.yml   # runs the structural validator on every PR
├── _archive/                    # material kept for reference, not part of the curriculum
│   └── README.md                # why each item is here
├── assets/
│   └── README.md                # where logos and templates go when they exist
├── docs/
│   ├── README.md
│   ├── ctf_scoring_rubric.md    # grading + flag validation
│   ├── implementation_guide.md  # LMS setup and district rollout
│   └── teacher_onboarding.md
├── Phase_Plans/
│   ├── GECDSB_Monthly_Calendar_Integration.md
│   ├── Phase_1_K_Grade2_Ages5-8.md
│   ├── Phase_2_Grades3-5_Ages8-11.md
│   ├── Phase_3_Grades6-8_Ages11-14.md
│   └── Phase_4_Grades9-12_Ages14-18.md
├── Programs/
│   ├── Program_1_Foundations_K-5/
│   ├── Program_2_Social_Dynamics_Grades6-8/
│   └── Program_3_Legal_AI_Grades9-12/
│       └── 01_Program_Guide.md … 07_CTF_Worksheets.md
├── scripts/
│   ├── generate_qr.py           # QR codes for worksheets (output is git-ignored)
│   └── validate_repo.py         # structural validation; exits 1 on failure
├── CHANGELOG.md
├── CONTRIBUTING.md
├── Digital_Self_Defense_Foundation.md  # the five competency arcs
├── ECNO_Alignment_Guide.md             # 2026 four-theme campaign crosswalk
├── ISED_AI_for_All_Alignment.md        # national AI strategy crosswalk + what is not claimed
├── K12_Cyber_Safety_Framework.md       # master framework
├── LICENSE                              # MIT
├── Makefile                             # validate / lint / qr-generate / pdf-export / clean
├── README.md
└── Stop_Think_Reinforcement.md          # the cross-phase pause habit
```

Each program folder follows the same seven-file pattern: program guide, lesson plans, student handouts, parent toolkit, assessments and materials, persona cast, and CTF worksheets. The persona cast is the continuity device — the same characters return across programs, so a Grade 10 student recognises the tool they met in Grade 4.

---

## 🚀 Where to start

**If you are a teacher about to deliver a session**
1. Read the program guide (`01_Program_Guide.md`) for your grade band
2. Read the lesson plan for the session you are teaching (`02_Lesson_Plans.md`)
3. Check the materials list in `05_Assessments_and_Materials.md`
4. Print the session's worksheet from `07_CTF_Worksheets.md`, or make a QR code with `scripts/generate_qr.py`

**If you are a curriculum lead or administrator**
1. Read [K12_Cyber_Safety_Framework.md](K12_Cyber_Safety_Framework.md) — start with *Safety Guidelines* and *Canadian Legal Framework*
2. Read [docs/implementation_guide.md](docs/implementation_guide.md)
3. Read the alignment guides ([ECNO](ECNO_Alignment_Guide.md), [ISED](ISED_AI_for_All_Alignment.md)) — the ISED document is explicit about what this framework does *not* claim
4. Read the *Known limitations* section of [CHANGELOG.md](CHANGELOG.md)

**If you are contributing**
1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Run the validator before you commit: `python3 scripts/validate_repo.py`
3. Read [Digital_Self_Defense_Foundation.md](Digital_Self_Defense_Foundation.md) — every new session should map to one competency arc, one persona, and one age band

---

## ✅ Validation

The repository ships a dependency-free structural validator. It checks for merge-conflict markers, UTF-8 BOMs, relative links and heading anchors that do not resolve, inline paths to files that do not exist, and CTF flags that violate their own format rule or disagree with the scoring rubric.

```bash
python3 scripts/validate_repo.py   # no dependencies; exits 1 on failure
make validate                      # the same check, for make users
make lint                          # optional; requires markdownlint-cli
```

It runs in CI on every pull request via `.github/workflows/validate.yml`. It checks structure, not pedagogy — it cannot tell you whether a lesson is good, only that it is internally consistent.

---

## 📚 Documentation

- [Master framework](K12_Cyber_Safety_Framework.md) — phases, protocols, legal framework, assessment
- [Competency arcs](Digital_Self_Defense_Foundation.md) — the five threads and the spiral model
- [Implementation guide](docs/implementation_guide.md) — LMS setup and district rollout
- [Teacher onboarding](docs/teacher_onboarding.md) — training materials
- [CTF scoring rubric](docs/ctf_scoring_rubric.md) — grading and flag validation
- [ECNO alignment](ECNO_Alignment_Guide.md) — Digital Me, Digital Us, Digital Families, Digital Minds
- [ISED alignment](ISED_AI_for_All_Alignment.md) — six-pillar *AI for All* crosswalk
- [Stop and Think](Stop_Think_Reinforcement.md) — the habit that runs through every session
- [Changelog](CHANGELOG.md) — every material change, and what it means for trained staff

---

## ⚠️ Before you teach this

- **Sensitive content.** Programs 2 and 3 cover sextortion and image-based abuse. Read the *Safety Guidelines* section of the framework first; it sets out counsellor presence, opt-out, mandatory reporting, and crisis routes.
- **One protocol, everywhere.** The sextortion response taught here is **3 Do Nots + Tell** — don't pay, don't reply, don't delete, tell. If your board uses different wording, change it everywhere (worksheets, parent toolkit, assessment) rather than in one place.
- **No real personal data.** Every activity is designed to run on fictional personas, demo accounts, and sample material. If a student's screenshot of a completed worksheet would harm someone, the activity is wrong.
- **Not legal advice.** The legal section summarises the Criminal Code for teaching. Have board counsel review offence descriptions before delivery.

---

## 🤝 Contributing

Lesson feedback, worksheet corrections, and new CTF scenarios are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📄 Licence

MIT — see [LICENSE](LICENSE).
