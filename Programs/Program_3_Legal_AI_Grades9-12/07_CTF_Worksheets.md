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

**Instructions:** Analyze the two provided images. Use the forensic stack to determine which is REAL and which is AI/Deepfake.

| Forensic Check | Image A (Real/AI?) | Image B (Real/AI?) | Evidence / Tells Found |
|----------------|:------------------:|:------------------:|------------------------|
| ✋ Hands / Teeth / Jewelry Glitches | [ ] Real [ ] AI | [ ] Real [ ] AI | _________________________ |
| 👁️ Eyes (Blinking, Reflections) | [ ] Real [ ] AI | [ ] Real [ ] AI | _________________________ |
| 🪞 Hair Edges & Lighting Mismatches | [ ] Real [ ] AI | [ ] Real [ ] AI | _________________________ |
| 📝 Text / Logos Garbled | [ ] Real [ ] AI | [ ] Real [ ] AI | _________________________ |

**🏆 CTF Challenge:**  
Run a reverse image search. The metadata/EXIF data contains the flag hash: `flag{truth_detected}`.

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

## Privilege Climb (Session 10)
**Mapped CTF:** *Privilege Climb* | **Category:** PrivEsc (Linux Permissions)

**Instructions:** After getting a "user" shell, look for misconfigured permissions or SUID binaries to become `root`.

| File/Command | Permission/SUID Bit | Escalation Path? |
|:-----------:|:-------------------:|:----------------:|
| `/usr/bin/find` | `-rwsr-xr-x` | [ ] Yes [ ] No |
| `/home/student/data.txt` | `-rw-r--r--` | [ ] Yes [ ] No |
| `sudo -l` | `NOPASSWD` | [ ] Yes [ ] No |

**🏆 CTF Challenge:**  
Escalating privileges reveals the admin flag: `flag{priv_escalated_success}`.
