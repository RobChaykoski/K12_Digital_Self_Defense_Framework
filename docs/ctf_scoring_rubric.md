# 📊 CTF Scoring Rubric & Flag Validation Guide

This rubric standardizes grading for all Capture-the-Flag challenges across Programs 1, 2, and 3. Use it alongside `05_Assessments_and_Materials.md` for consistent evaluation.

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

Each CTF session is worth **10 points**, distributed as follows:

| Criteria | Max Points | Description |
|----------|------------|-------------|
| **Flag Accuracy** | 4 pts | Correct `flag{}` string submitted |
| **Worksheet Completion** | 2 pts | All tables, checkboxes, and reasoning fields filled |
| **Collaboration** | 2 pts | Peer assistance, role rotation, group problem-solving |
| **Effort / Participation** | 2 pts | On-task behavior, time management, initiative |

### Grade Band Adjustments
- **K–5:** Focus on effort & participation (4 pts). Flag accuracy simplified to visual matching.
- **6–8:** Add collaboration weighting (3 pts for teamwork).
- **9–12:** Emphasize flag accuracy & reasoning (5 pts for technical explanation).

---

## Flag Validation Rules

All flags must conform to:
```
flag{exact_string_here}
```

### Validation Checklist
- [ ] Starts with `flag{` and ends with `}`
- [ ] Lowercase letters, numbers, underscores only (unless specified)
- [ ] No extra spaces before `{` or after `}`
- [ ] Matches the answer key in `07_CTF_Worksheets.md`

### Common Errors & Corrections
| Student Submission | Correct Flag | Issue |
|--------------------|--------------|-------|
| `Flag{my_key_works}` | `flag{my_key_works}` | Uppercase F |
| `flag{ my_footprints_stay }` | `flag{my_footprints_stay}` | Extra spaces |
| `flag{real_email_found}` (missing braces) | `flag{real_email_found}` | Missing closing brace |

> ⚠️ **Rule:** Flags are case-sensitive unless noted in the worksheet.

---

## Session-by-Session Rubric

### Program 1 (K–5) — Foundations
| Session | Challenge | Expected Flag | Points |
|---------|-----------|---------------|--------|
| 1 | Phishing Post Office | `flag{real_email_found}` | 4 |
| 2 | Password Lockbox | `flag{my_key_works}` | 4 |
| 3 | Link Lab Sorting | `flag{green_count}` | 4 |
| 4 | AI Art Detective | `flag{ai_detected}` | 4 |
| 5 | Digital Footprint Trail | `flag{my_footprints_stay}` | 4 |

### Program 2 (6–8) — Social Dynamics
| Session | Challenge | Expected Flag | Points |
|---------|-----------|---------------|--------|
| 1 | URL Inspector | `flag{safe_link_found}` | 4 |
| 2 | Caesar Cipher Decode | `flag{message_decoded}` | 4 |
| 3 | Packet Sniffer Lite | `flag{packet_captured}` | 4 |
| 4 | Voice of the Family | `flag{voice_verified}` | 4 |
| 5 | Discord Drop | `flag{file_extracted}` | 4 |

### Program 3 (9–12) — Legal/AI
| Session | Challenge | Expected Flag | Points |
|---------|-----------|---------------|--------|
| 1 | Boot2Root Intro | `flag{system_booted}` | 4 |
| 2 | MFA Enrollment | `flag{mfa_enabled}` | 4 |
| 3 | Deepfake Detective | `flag{deepfake_found}` | 4 |
| 4 | Auth Token Analysis | `flag{token_valid}` | 4 |
| 5 | School Server | `flag{server_accessed}` | 4 |

---

## Partial Credit Guidelines

| Scenario | Points Awarded | Rationale |
|----------|----------------|-----------|
| Flag submitted with minor typo (e.g., missing brace) | 3 pts | Recognizes understanding; deduct 1 for precision |
| Worksheet partially filled out (≥75%) | 2 pts | Evidence of effort despite incomplete solution |
| Collaboration observed but individual flag incorrect | 1 pt | Group problem-solving demonstrated |
| Late submission (>48 hrs) | 3 pts | Accept with deduction; document in gradebook |

---

## Leaderboard & Badges

### Monthly Leaderboard Template
| Rank | Student Name | Flags Earned | Program | Badge |
|------|--------------|--------------|---------|-------|
| 1 | Alex M. | 5/5 | Prog 2 | 🔐 Cipher Master |
| 2 | Jordan K. | 4/5 | Prog 3 | 🛡️ Firewall Guardian |

### Achievement Badges
| Badge | Requirement | Description |
|-------|-------------|-------------|
| 🔐 **Cipher Master** | Complete all ciphers in Program 2 | Decodes hidden messages |
| 🛡️ **Firewall Guardian** | Pass MFA & Auth challenges in Program 3 | Secures digital identity |
| 👁️ **AI Eye** | Identify all AI tells in Program 1/3 | Detects synthetic media |
| 🦶 **Footprint Finder** | Complete digital trail in Program 1 | Tracks online presence |

> 🏆 Award badges via printable certificates or LMS digital badges.

---

## Submission Templates

### Google Form / Microsoft Form Structure
```
Question 1: Student Name (Short answer)
Question 2: Session Number (Multiple choice: 1–5)
Question 3: Flag Submission (Short answer — validate with regex: ^flag\{.*\}$)
Question 4: Reasoning / Notes (Paragraph)
```

### LMS Assignment Rubric (Canvas Example)
```json
{
  "criteria": [
    {"name": "Flag Accuracy", "points": 4, "description": "Exact flag{string} match"},
    {"name": "Worksheet Completion", "points": 2, "description": "All fields filled"},
    {"name": "Collaboration", "points": 2, "description": "Peer assistance observed"},
    {"name": "Effort", "points": 2, "description": "On-task & timely"}
  ]
}
```

---

## 📞 Support & Updates
- Report rubric discrepancies: [Feature Request](https://github.com/RobChaykoski/K12_Digital_Self_Defense_Framework/issues/new?template=feature_request.md)
- Email: `rob.chaykoski@live.ca`
- Last Updated: September 2024
