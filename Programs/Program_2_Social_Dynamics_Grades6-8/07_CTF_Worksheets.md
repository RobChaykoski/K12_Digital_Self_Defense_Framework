# 🚩 Program 2 — CTF Worksheets & Scenarios (Grades 6–8)
*Aligned with `02_Lesson_Plans.md` and the Cheat Sheet (uppusaikiran.github.io/hacking/Capture-the-Flag-CheatSheet/)*

---

## Discord Drop (Session 1)
**Mapped CTF:** *Discord Drop* | **Category:** Web Hacking (URL Inspection)

**Instructions:** A bot message says: "🎁 FREE ROBUX! Click here to claim!" The link points to `roblox-login-secure.com`.

| Check Item | Present? (Y/N) | Notes |
|------------|:--------------:|-------|
| Suspicious domain suffix | [ ] | _________________________ |
| Asks for account info | [ ] | _________________________ |
| Urgency language | [ ] | _________________________ |

**🏆 CTF Challenge:**  
Inspect the URL. The flag is hidden in the discrepancy: `flag{spot_the_fake_link}`.

---

## Voice of the Family (Session 3)
**Mapped CTF:** *Voice of the Family* | **Category:** Crypto (Audio/Cipher)

**Instructions:** Listen to two audio clips. One is real, one is AI-cloned. Use the "Family Safe Word" list to verify.

> ⚠️ **Do not score yourself on whether you could hear the difference.** Current voice cloning is often indistinguishable by ear. That is exactly why the rule is *verify through another channel* — not *listen harder*.

| Clip ID | Real or AI? | Safe Word Used? | Tell Found |
|---------|:-----------:|:---------------:|------------|
| A       | [ ] Real [ ] AI | [ ] Yes [ ] No | _________________________ |
| B       | [ ] Real [ ] AI | [ ] Yes [ ] No | _________________________ |

**🏆 CTF Challenge:**  
The correct audio file's waveform visualization contains a QR code. Scan it for: `flag{safe_word_verified}`.

---

## Sextortion Station (Session 6)
**Mapped CTF:** *Sextortion Station* | **Category:** File Hacking (Logic)

**Instructions:** A scammer sent you a photo and said: "Send $10 or I'll post this on Instagram." Fill in the protocol steps below. Order them correctly (1-4).

| Step | Action | Check When Done |
|:----:|--------|:---------------:|
| **1** | 🚫 **DON'T PAY** (Paying proves you will pay again) | [ ] |
| **2** | 🚫 **DON'T REPLY** (Any reply feeds them; silence is power) | [ ] |
| **3** | 🚫 **DON'T DELETE** (Screenshots = evidence for police/take-down) | [ ] |
| **4** | ✅ **TELL** a trusted adult & Report to Cybertip.ca / Take It Down | [ ] |

**🏆 CTF Challenge:**  
Write the four moves in order, lowercase, joined by underscores: `flag{dont_pay_dont_reply_dont_delete_tell}`.

---

## Wi-Fi Whisperer (Session 2)
**Mapped CTF:** *Wi-Fi Whisperer* | **Category:** Forensics (Packet Sniffing)

**Instructions:** Analyze the provided `.pcap` hex dump or use a web-based Wireshark demo. Look for unencrypted HTTP traffic containing login details. This is why "look for the padlock" matters: on an unencrypted connection, a password is readable by anyone on the same network.

| Packet # | Protocol | Payload Preview | Flag Found? |
|----------|:--------:|-----------------|:-----------:|
| 1        | TCP      | `GET /index.html` | [ ] |
| 2        | HTTP     | `username=admin&pass=1234` | [ ] |
| 3        | UDP      | DNS Query       | [ ] |

**🏆 CTF Challenge:**  
The plaintext password in the packet reveals: `flag{unencrypted_found}`.

---

## The Encrypted DM (Session 9)
**Mapped CTF:** *The Encrypted DM* | **Category:** Crypto (Caesar/Base64)

**Instructions:** A "message from IT" is received in Base64 or Caesar Shift. Decode it using the cheat sheet's one-liners.

| Cipher Type | Encoded String | Decoded Result |
|:----------:|----------------|----------------|
| Base64     | `ZmxhZ3tteV9zZWNyZXRfaXNfc2F0ZX0=` | _________________________ |
| Caesar (Shift 3, `#` stands for a space) | `#nhhs#lw#vhfuhw` | _________________________ |

**🏆 CTF Challenge:**  
Decoded text reveals: `flag{my_secret_is_safe}`.

---

## Cyberbullying Cipher Decode (Digital Wellness extension)
**Mapped CTF:** *The Cyberbullying Cipher Decode* | **Category:** Digital Wellness (Mental Health & Coping)

**Student Name:** ____________________  
**Date:** ______________  

**Instructions:** ECNO's Digital Wellness theme covers coping with cyberbullying. A classmate posts an unkind comment, encrypted with a Caesar cipher: each letter was shifted **forward 3** in the alphabet (A→D, B→E, …). Shift each letter **back 3** to read it.

Ciphertext: `xqnlg zrugv kxuw`

| Encoded | Decoded |
|---------|--------|
| xqnlg | ___ |
| zrugv | ___ |
| kxuw | ___ |

**🏆 CTF Challenge:**  
Write the decoded message on your worksheet. Submit: `flag{unkind_words_hurt}`

> 💡 *ECNO Alignment:* Addresses the **Digital Minds / Digital Me** themes by practising a decoding skill on a message about online cruelty — a 10-minute advisory or homeroom activity, not tied to a numbered session. The response protocol attached to bullying is the same **3 Do Nots + Tell** used in Session 6, minus the payment step: don't reply, don't delete, tell an adult, and report through the school's pathway.
