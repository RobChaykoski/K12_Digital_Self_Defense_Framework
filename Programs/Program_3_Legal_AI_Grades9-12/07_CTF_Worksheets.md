# 🚩 Program 3 — CTF Worksheets & Scenarios (Grades 9–12)
*Aligned with `02_Lesson_Plans.md` and the Cheat Sheet (uppusaikiran.github.io/hacking/Capture-the-Flag-CheatSheet/)*

---

## MFA Mayhem (Session 2)
**Mapped CTF:** *MFA Mayhem* | **Category:** Web Hacking (Auth)

**Instructions:** Complete the authenticator app setup and backup code recovery plan.

| Step | Task | Completed? |
|:----:|------|:----------:|
| 1 | Install approved authenticator app | [ ] |
| 2 | Enroll TOTP on two services | [ ] |
| 3 | Generate and securely save backup codes | [ ] |
| 4 | Simulate "lost phone" recovery | [ ] |

**🏆 CTF Challenge:**  
Correct completion reveals: `flag{multi_layer_active}`.

---

## Deepfake Detectives (Session 4)
**Mapped CTF:** *Deepfake Detectives* | **Category:** Forensics (EXIF/Hash)

**Instructions:** Analyze the two provided images. Work in the order of evidence strength, then decide which image the available evidence supports calling AI — and state what the evidence does **not** prove.

| Check (in order) | Image A | Image B | Evidence / limit |
|------------------|---------|---------|------------------|
| **1. Source** — who published it first, and is that account verifiable? | _____________ | _____________ | _________________________ |
| **2. Reverse image search** — earlier appearance elsewhere? | _____________ | _____________ | _________________________ |
| **3. Corroboration** — independent report of the same thing? | _____________ | _____________ | _________________________ |
| **4. Clues** — hands/teeth glitches, eyes/reflections, hair edges, lighting, garbled text | [ ] Real [ ] AI | [ ] Real [ ] AI | _________________________ |

**🏆 CTF Challenge:**  
Run a reverse image search and check the file's metadata (right-click → Properties → Details). **Neither check is conclusive:** most platforms strip EXIF, and a real photo can be re-uploaded without it. Submit the flag once you can name the AI image *and* the evidence that supports your call, plus one line on what the evidence cannot prove: `flag{truth_detected}`

> ⚠️ **The clues are not proof.** They are getting rarer every year. The durable skills are source tracing, reverse search, and corroboration — decide what the image *claims* and whether anything independent supports it.

---

## Crypto Rush & Rug Pulls (Session 8)
**Mapped CTF:** *Crypto Rush & Rug Pulls* | **Category:** Crypto (Smart Contracts)

**Instructions:** Analyze the provided token offer (`$MILK`). Apply the red-flag framework.

| Scam Menu Item | Present in Offer? (Y/N) | Why it's a Red Flag |
|----------------|:----------------------:|---------------------|
| 💰 Guaranteed Returns | [ ] Yes [ ] No | _________________________ |
| ⏱️ Urgency / Scarcity Timer | [ ] Yes [ ] No | _________________________ |
| 👛 Wallet Connection for "Prize" | [ ] Yes [ ] No | _________________________ |
| 🕵️ Anonymous Team | [ ] Yes [ ] No | _________________________ |

**🏆 CTF Challenge:**  
Identify the drained wallet address in the simulated dashboard: `flag{rug_pull_survived}`.

---

## The School Server (Session 1)
**Mapped CTF:** *The School Server* | **Category:** System (Boot2Root)

**Instructions:** Run a guided audit. Count accounts, flag reused passwords, identify "crown jewels".

| Account Type | Unique Passphrase? | Flagged for Change? |
|:-----------:|:------------------:|:-------------------:|
| Email (Master Key) | [ ] Yes [ ] No | [ ] |
| School Portal | [ ] Yes [ ] No | [ ] |
| Gaming/Social | [ ] Yes [ ] No | [ ] |

**🏆 CTF Challenge:**  
The breach simulation flowchart leads to a simulated VM login. Root access reveals: `flag{server_rooted}`.

---

## Privilege Climb (extension — follows The School Server)
**Mapped CTF:** *Privilege Climb* | **Category:** PrivEsc (Linux Permissions)

**Instructions:** After getting a "user" shell, look for misconfigured permissions or SUID binaries to become `root`.

| File/Command | Permission/SUID Bit | Escalation Path? |
|:-----------:|:-------------------:|:----------------:|
| `/usr/bin/find` | `-rwsr-xr-x` | [ ] Yes [ ] No |
| `/home/student/data.txt` | `-rw-r--r--` | [ ] Yes [ ] No |
| `sudo -l` | `NOPASSWD` | [ ] Yes [ ] No |

**🏆 CTF Challenge:**  
Escalating privileges reveals the admin flag: `flag{priv_escalated_success}`.

---

## Algorithmic Mood Audit (Session 9 — Social Media Algorithms)
**Mapped CTF:** *The Algorithmic Mood Audit* | **Category:** Digital Wellness (Mental Health & Social Comparison)

**Student Name:** ____________________  
**Date:** ______________  

**Instructions:** The Digital Minds theme covers how feeds are built to hold attention. Track your own feed for 15 minutes (or use the teacher's screenshot pack):
- Note 3 posts that made you feel **inferior**
- Note 3 posts that made you feel **inspired**
- Identify the **engagement bait** pattern in each

| Post Type | Mood Impact | Engagement Bait? |
|-----------|-------------|------------------|
| Influencer outfit | 😟 Inferior | Yes (likes/comments) |
| Friend graduation | 😊 Inspired | No |
| "You won't believe #4" | 😟 Anxious | Yes (curiosity gap) |
| Study-tips carousel | 😊 Inspired | No |

**🏆 CTF Challenge:**  
The goal is not a "correct" mood — it is spotting the mechanism. Write one sentence naming the pattern the feed used on you, then submit: `flag{feed_pattern_found}`

> 💡 *ECNO Alignment:* Extends the **Digital Minds** theme (safe and responsible AI use, protecting privacy) and the **Digital Me** theme (recognising risk) into algorithmic literacy — a Phase 4 module the theme-level material does not reach. Run alongside Session 9.
