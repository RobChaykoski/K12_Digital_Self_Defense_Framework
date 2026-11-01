# 🚩 Program 1 — CTF Worksheets & Scenarios (K–5)
*Aligned with `02_Lesson_Plans.md` and the Cheat Sheet (uppusaikiran.github.io/hacking/Capture-the-Flag-CheatSheet/)*

---

## Clicking Safely — Green vs. Red Links (Track A, Session 3)
**Mapped CTF:** *Red Light, Green Light Links* | **Category:** Web Hacking (Visual)

**Student Name:** ____________________  
**Date:** ______________  

**Instructions:** Read each message or button description. Draw a ✅ next to the **GREEN (Safe)** link and an ❌ next to the **RED (Risky)** link. Circle your final answer for the CTF flag!

| # | Message / Button Description | Green (✅) | Red (❌) | Reason (Why?) |
|---|------------------------------|:----------:|:--------:|---------------|
| 1 | "Click here to claim your FREE Robux!" | [ ] | [ ] | _________________________ |
| 2 | "Mom shows you how to video call Grandma." | [ ] | [ ] | _________________________ |
| 3 | "URGENT! Your account will be deleted in 1 hour. Click NOW." | [ ] | [ ] | _________________________ |
| 4 | "Your teacher posts the class pet's puppy-training video in the school app." | [ ] | [ ] | _________________________ |
| 5 | "Stranger DM: 'Add me on Snapchat for a secret game!'" | [ ] | [ ] | _________________________ |

**🏆 CTF Challenge:**  
Count the **Green (Safe)** links you identified. Two of the five messages are safe.  
*Flag Format:* `flag{2}`

---

## The Password Lockbox (Track A, Session 2)
**Mapped CTF:** *The Password Lockbox* | **Category:** File Hacking (Basics)

**Instructions:** Decorate your paper padlock. Write your "key rule" inside: **Only my family knows my key.** Hide a slip of paper with a **pretend** 4-digit PIN inside the box — never a real bank card, phone, or door code.

**🏆 CTF Challenge:**  
The teacher scans the QR code on the back of your lock. The correct PIN unlocks `flag{my_key_works}`.

---

## AI Art Detective (Track B, Session 4)
**Mapped CTF:** *AI Art Detective* | **Category:** Forensics (Visual)

**Instructions:** Look at the two images provided by your teacher. For each one, write down:
- **Source:** who made or published it, and where did you find it?
- **Corroboration:** does an independent source show the same thing?
- **Clues:** hands/teeth/jewellery, eyes/reflections, hair edges, lighting, garbled text.

> ⚠️ **Clues, not proof.** These mistakes are getting rarer every year, and compressed real photos can show the same artefacts.

**🏆 CTF Challenge:**  
Check the file's metadata: right-click → Properties → Details. Many AI tools leave a **Software** field, but most apps strip it. A missing field proves nothing; a present field is only a clue about the tool, not proof of what the image claims.

*Flag Format:* `flag{check_the_source}`

> Write down what the metadata and clues do and do not prove.

> 💡 *ECNO Alignment:* Addresses **Digital Minds** (safe and responsible AI use) by introducing the idea that an image can be *made*, not just *taken*. For Grades 3–5 the goal is the concept, not a reliable detector.

---

## Digital Footprint Trail (Track A, Session 5)
**Mapped CTF:** *The Digital Footprint Trail* | **Category:** File Hacking (Steganography)

**Instructions:** Create a chain of footprints on your paper strip. On each footprint, draw something you WOULD post online. Attach a QR code to the final footprint.

**🏆 CTF Challenge:**  
Scanning the final QR code reveals `flag{my_footprints_stay}`.

---

## Social Media Mood Tracker (Track A, Session 4 — Screen Time Boundaries)
**Mapped CTF:** *The Social Media Mood Tracker* | **Category:** Digital Wellness (Journaling)

**Student Name:** ____________________  
**Date:** ______________  

**Instructions:** ECNO's Digital Families theme teaches us that screen time affects our mood. Track how different apps make you feel:
- 😊 Happy / Calm
- 😐 Neutral / Bored
- 😟 Anxious / Frustrated

| App / Game | Time Spent | Mood Emoji | Why? |
|------------|-----------|------------|------|
| TikTok | 20 min | 😊 | Funny cat videos |
| Roblox | 45 min | 😐 | Waiting for friends |
| YouTube Kids | 15 min | 😟 | Scary monster video |

**🏆 CTF Challenge:**  
There is no fixed number of "happy" apps — the answer is yours. Finish the tracker, then scan the station QR code to reveal: `flag{mood_tracked}`

> 💡 *ECNO Alignment:* Extends the **Digital Families** theme (managing screen time and digital wellbeing together). The completed tracker goes home so a family can compare notes — the conversation, not the count, is the point.

---

## The Phishing Post Office (Track B, Session 1)
**Mapped CTF:** *The Phishing Post Office* | **Category:** Web Hacking (Source Code)

**Instructions:** You receive a printed "school newsletter" email with 3 links. Two are fake (`schoo1-news.com`), one is real (`schoolboard.ca`). Hover over them before clicking.

**🏆 CTF Challenge:**  
The correct URL contains a hidden comment: `<!-- flag{real_email_found} -->`. Write it on your worksheet to submit.
