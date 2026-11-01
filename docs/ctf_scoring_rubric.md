# 📊 CTF Scoring Rubric & Flag Validation Guide

This rubric standardises grading for all Capture-the-Flag challenges across Programs 1, 2, and 3. It is generated from the three `07_CTF_Worksheets.md` files — those are the source of truth for flags. Use it alongside `05_Assessments_and_Materials.md`.

**Framework version:** 3.0
**Last synchronised with the worksheets:** October 2026

---

## 📋 Table of Contents
- [1. Scoring Overview](#scoring-overview)
- [2. Flag Validation Rules](#flag-validation-rules)
- [3. Session-by-Session Rubric](#session-by-session-rubric)
- [4. Partial Credit Guidelines](#partial-credit-guidelines)
- [5. Leaderboard & Badges](#leaderboard--badges)
- [6. Submission Templates](#submission-templates)

---

## Scoring Overview

Each CTF challenge is worth **10 points**:

| Criteria | Max Points | Description |
|----------|------------|-------------|
| **Flag Accuracy** | 4 pts | Correct `flag{}` string submitted |
| **Worksheet Completion** | 2 pts | All tables, checkboxes, and reasoning fields filled |
| **Collaboration** | 2 pts | Peer assistance, role rotation, group problem-solving |
| **Effort / Participation** | 2 pts | On-task behaviour, time management, initiative |

### Grade Band Adjustments
- **K–5:** Effort and participation carry 4 pts; flag accuracy is visual matching, awarded for the right answer even if typed imperfectly by an adult helper.
- **6–8:** Collaboration carries 3 pts; flags are typed by the student.
- **9–12:** Flag accuracy and the written reasoning carry 5 pts — a correct flag with no explanation earns 2.

### CTFs that are not auto-gradable
Some challenges have a personal answer with no fixed flag (`flag{mood_tracked}`, `flag{feed_pattern_found}`). These are **completion flags**: the student earns the flag by finishing the activity, and the assessed work is the reflection, not the string.

---

## Flag Validation Rules

All flags conform to:

```
flag{exact_string_here}
```

### Validation Checklist
- [ ] Starts with `flag{` and ends with `}`
- [ ] Lowercase letters, digits, and underscores only — no spaces
- [ ] No space before `{` or after `}`
- [ ] Matches the flag printed in the corresponding `07_CTF_Worksheets.md`

Validate with: `^flag\{[a-z0-9_]+\}$`

### Common Errors & Corrections
| Student Submission | Correct Flag | Issue |
|--------------------|--------------|-------|
| `Flag{my_key_works}` | `flag{my_key_works}` | Uppercase F |
| `flag{ my_footprints_stay }` | `flag{my_footprints_stay}` | Extra spaces |
| `flag{real_email_found` | `flag{real_email_found}` | Missing closing brace |
| `flag{don't pay}` | `flag{dont_pay_dont_reply_dont_delete_tell}` | Spaced prose instead of the flag string |

> ⚠️ **Rule:** Flags are case-sensitive unless the worksheet says otherwise.

---

## Session-by-Session Rubric

### Program 1 (K–5) — Foundations

Program 1 runs two tracks, so session numbers alone are ambiguous. Both are given.

| Track / Session | Challenge | Expected Flag | Points |
|-----------------|-----------|---------------|--------|
| Track B, S1 | The Phishing Post Office | `flag{real_email_found}` | 4 |
| Track A, S2 | The Password Lockbox | `flag{my_key_works}` | 4 |
| Track A, S3 | Clicking Safely (Red Light, Green Light Links) | `flag{2}` | 4 |
| Track A, S4 | The Social Media Mood Tracker | `flag{mood_tracked}` (completion) | 4 |
| Track B, S4 | AI Art Detective | `flag{check_the_source}` | 4 |
| Track A, S5 | The Digital Footprint Trail | `flag{my_footprints_stay}` | 4 |

### Program 2 (6–8) — Social Dynamics

| Session | Challenge | Expected Flag | Points |
|---------|-----------|---------------|--------|
| S1 | Discord Drop | `flag{spot_the_fake_link}` | 4 |
| S2 | Wi-Fi Whisperer | `flag{unencrypted_found}` | 4 |
| S3 | Voice of the Family | `flag{safe_word_verified}` | 4 |
| S6 | Sextortion Station | `flag{dont_pay_dont_reply_dont_delete_tell}` | 4 |
| S9 | The Encrypted DM | `flag{my_secret_is_safe}` | 4 |
| Advisory | The Cyberbullying Cipher Decode | `flag{unkind_words_hurt}` | 4 |

### Program 3 (9–12) — Legal / AI

| Session | Challenge | Expected Flag | Points |
|---------|-----------|---------------|--------|
| S1 | The School Server | `flag{server_rooted}` | 4 |
| S2 | MFA Mayhem | `flag{multi_layer_active}` | 4 |
| S4 | Deepfake Detectives | `flag{truth_detected}` | 4 |
| S8 | Crypto Rush & Rug Pulls | `flag{rug_pull_survived}` | 4 |
| S9 | The Algorithmic Mood Audit | `flag{feed_pattern_found}` (completion) | 4 |
| Extension | Privilege Climb | `flag{priv_escalated_success}` | 4 |

---

## Partial Credit Guidelines

| Scenario | Points Awarded | Rationale |
|----------|----------------|-----------|
| Flag submitted with a minor typo (missing brace, wrong case) | 3 pts | Recognises understanding; deduct 1 for precision |
| Worksheet partially filled (≥75%) | 2 pts | Evidence of effort despite incomplete solution |
| Collaboration observed but individual flag incorrect | 1 pt | Group problem-solving demonstrated |
| Late submission (>48 hrs) | 3 pts | Accept with deduction; document in the gradebook |
| Correct flag, no reasoning (9–12 only) | 2 pts | The reasoning is the assessed skill at this level |

---

## Leaderboard & Badges

### Monthly Leaderboard Template
| Rank | Student Name | Flags Earned | Program | Badge |
|------|--------------|--------------|---------|-------|
| 1 | Alex M. | 5/6 | Prog 2 | 🔐 Cipher Master |
| 2 | Jordan K. | 4/6 | Prog 3 | 🛡️ Firewall Guardian |

### Achievement Badges
| Badge | Requirement | Description |
|-------|-------------|-------------|
| 🔐 **Cipher Master** | Complete all cipher challenges in Program 2 | Decodes hidden messages |
| 🛡️ **Firewall Guardian** | Pass the MFA and auth challenges in Program 3 | Secures digital identity |
| 👁️ **Source Tracer** | Complete both media-forensics challenges (P1 AI Art Detective, P3 Deepfake Detectives) | Traces where media came from instead of guessing at "tells" |
| 🦶 **Footprint Finder** | Complete the digital trail in Program 1 | Tracks online presence |
| 🤝 **Upstander** | Complete the Cyberbullying Cipher and the 3 Do Nots + Tell station | Knows what to do, and who to tell |

> 🏆 Award badges via printable certificates or LMS digital badges.

---

## Submission Templates

### Google Form / Microsoft Form Structure
```
Question 1: Student Name (Short answer)
Question 2: Program and Session (Short answer, e.g. "Program 2, Session 6")
Question 3: Flag Submission (Short answer — validate with regex: ^flag\{[a-z0-9_]+\}$)
Question 4: Reasoning / Notes (Paragraph)
```

### LMS Assignment Rubric (Canvas Example)
```json
{
  "criteria": [
    {"name": "Flag Accuracy", "points": 4, "description": "Exact flag{string} match"},
    {"name": "Worksheet Completion", "points": 2, "description": "All fields filled"},
    {"name": "Collaboration", "points": 2, "description": "Peer assistance observed"},
    {"name": "Effort", "points": 2, "description": "On-task and timely"}
  ]
}
```

---

## 📞 Support & Updates
- Report rubric discrepancies: [Feature Request](https://github.com/RobChaykoski/K12_Digital_Self_Defense_Framework/issues/new?template=feature_request.md)
- Email: `rob.chaykoski@live.ca`
- Last Updated: October 2026
