# 📚 Program 3 — Lesson Plans (Grades 9–12)

Condensed from the Phase 4 plan. S6–7 require the guidance counsellor present.

---

## Session 1: "The Password Audit" — Credential Stuffing & Reuse (50 min)
<<<<<<< HEAD
=======
**In this session:** Patch leads; Ghost, Cipher.
>>>>>>> 723954f (first commit)
**Objective:** Explain credential stuffing; complete a personal password-hygiene audit.

| Time | Activity |
|------|----------|
| 5 min | Hook: "A list of 12 million email/password pairs was just published. Which of YOUR passwords are on it?" (They're probably not — but here's why that's luck, not skill.) |
| 10 min | Teach: breach databases • **credential stuffing** = stolen combos tried automatically against every major site • why one reused password is a house key to everything • passphrases vs. passwords (length beats complexity) • what a password manager actually does. |
| 20 min | **The Audit Lab:** students run a guided audit worksheet — count their accounts, flag reused passwords (without writing them down), identify the "crown jewels" (email = the master key), pick which get unique passphrases first. Optional: have them check one email at a breach checker (e.g., Have I Been Pwned) with parent/IT awareness. |
| 5 min | The rule stack: unique passphrase per crown-jewel account • manager for the rest • email account is account #1 to protect. |
| 10 min | **Breach simulation:** teacher plays out a live credential-stuffing story (breach → stuffing → email takeover → bank/social cascade). Students mark on a flowchart where they'd intervene. Exit ticket: *My crown-jewel accounts are ___ and my plan is ___.* |

**Materials:** audit worksheet (D1), breach flowchart, optional breach-checker access.

## Session 2: "MFA Mastery" — App-Based Authentication & Backups (50 min)
<<<<<<< HEAD
=======
**In this session:** Patch leads; Cipher.
>>>>>>> 723954f (first commit)
**Objective:** Implement authenticator-app MFA; build a recovery plan.

| Time | Activity |
|------|----------|
| 5 min | Hook: "SMS codes can be stolen in 30 seconds with a phone call to your carrier. Watch." (SIM-swap demo video.) |
| 10 min | Teach the MFA hierarchy: SMS (weakest — interceptable) • **authenticator apps** (TOTP, offline, better) • hardware keys (strongest). Then the part everyone skips: **recovery architecture** — backup codes stored safely, recovery email that's ALSO protected, knowing which adult/family member holds your backup. |
| 25 min | **Lab:** on school/demo accounts: install an authenticator app → enroll TOTP on two services → generate and securely save backup codes → simulate a "lost phone" recovery using only the backup codes. Checklist as they go (D2). No-device version: guided screenshot walkthrough + home mission with a parent. |
| 5 min | The lost-phone protocol: what to do in hour one (revoke sessions, MFA off/on, alert family) — written on their Quickie Card update. |
| 5 min | Exit ticket: *Rank the three MFA methods and say why.* + recovery plan check-in. |

**Materials:** lab accounts/devices, authenticator app pre-approved by IT, checklist D2.

## Session 3: "The Clone Wars" — Voice Cloning (50 min)
<<<<<<< HEAD
=======
**In this session:** Echo leads; Static (safe word, multi-generational).
>>>>>>> 723954f (first commit)
**Objective:** Explain how voice cloning works; apply the family verification protocol at adult level.

| Time | Activity |
|------|----------|
| 5 min | Hook: play two clips of the same public figure — one real, one cloned saying something they never said. Which is which? Why does it matter that you can't tell easily? |
| 10 min | Teach: how TTS/voice-cloning models work (minutes of source audio) • the **elder-fraud pipeline** (cloned grandparent → urgency → wire/gift cards/crypto) • why "it sounds exactly right" is now the LEAST reliable signal • consent and identity: cloning someone's voice to defraud is a criminal act in Canada. |
| 15 min | **Verification protocol workshop:** groups design the family protocol for urgent money requests — safe word • callback to a known number (not the number that called) • delay rule ("real emergencies survive a 10-minute verification") • who verifies what. Compare protocols; class adopts the strongest elements. |
| 10 min | **Defence drill:** teacher role-plays a cloned-voice scenario live (pre-recorded clip + follow-up texts); students run the protocol in real time and report where it held / broke. |
| 5 min | Exit ticket: *The three checks before any money moves based on a voice or message.* |

**Materials:** labelled clips, protocol template (D3), drill script.

## Session 4: "Deepfake Detection Lab" — Visual Forensics (50 min)
<<<<<<< HEAD
=======
**In this session:** Lens leads; Ghost.
>>>>>>> 723954f (first commit)
**Objective:** Dismantle deepfakes using ≥4 technical tells and free tools.

| Time | Activity |
|------|----------|
| 5 min | Hook: a labelled celebrity deepfake video played twice — first at normal speed, then paused frame-by-frame. "Now find it." |
| 10 min | Teach the forensic stack: Program 2's tell list + **tools** — reverse image search (where did this originate?) • metadata/EXIF basics • free detection tools & browser extensions (demo 1–2) • the provenance question (original source, uploader history, timing vs. events). |
| 20 min | **Lab:** 4 labelled samples (video + stills, public material). Teams run the full pipeline: tells → reverse search → metadata → verdict with confidence level + written evidence brief. Reveal ground truth; compare which method caught what. *(Never use classmates' images. AI-CSAEM is discussed at pattern level only — never shown.)* |
| 5 min | The legal lens: non-consensual deepfakes of real people — intimate ones are criminal in Canada (publication of intimate images); even non-intimate ones carry defamation/identity-theft exposure. |
| 5 min | Exit ticket: *Name 4 tells AND 2 tools you'd use on an unknown video.* |

**Materials:** labelled sample set, tool accounts/devices, evidence brief template (D4).

## Session 5: "Audio Forensics" — Cloned Voice & Lip-Sync Errors (50 min)
<<<<<<< HEAD
=======
**In this session:** Echo leads; Lens.
>>>>>>> 723954f (first commit)
**Objective:** Detect synthetic audio and lip-sync failures using waveform/visual analysis.

| Time | Activity |
|------|----------|
| 5 min | Hook: same sentence, three versions (human, cloned, TTS) — blind vote. Reveal. "You just did the hard part: your ear can't be trusted alone." |
| 10 min | Teach audio tells: missing breaths/micro-pauses • robotic cadence on emphasis • background noise too uniform • **lip-sync:** mouth shape vs. phoneme mismatches, jaw timing, frame interpolation smearing. Intro to waveform visualization (free online tool) — synthetic speech has telltale silence patterns. |
| 20 min | **Forensics lab:** 6 audio/video clips (labelled set). Teams assign roles (ear-tester, waveform analyst, lip-sync watcher, provenance researcher) and file a joint verdict with the strongest single piece of evidence. Debrief: which tell was most reliable? |
| 10 min | **Identity-theft connection:** cloned voice + deepfake face = full identity attack — fake "CEO" wire requests, fake family emergencies, synthetic alibis. Tie to S1/S2: your verification protocol is the defence at human scale. |
| 5 min | Exit ticket: *One audio tell, one visual tell, and the one question that beats both.* (Who benefits if I believe this?) |

**Materials:** labelled clip set, waveform tool access, role cards.

## Session 6: "Sextortion Syndicates" — The Business Behind the Scam 🛑 (50 min)
<<<<<<< HEAD
=======
**In this session:** Vault + Clause lead; Ledger (payment rails), Static.
>>>>>>> 723954f (first commit)
**Objective:** Analyze sextortion as an organized business model; identify Canadian law that applies. *(Counsellor present.)*

| Time | Activity |
|------|----------|
| 10 min | Ground rules (Program 2 protocol). Frame: this is a **business analysis**, like dissecting any criminal enterprise — because that's what it is. |
| 15 min | Teach the model: sourcing targets (gaming/social platforms) • grooming scripts • image acquisition (trick, or *deepfake fabrication* — no real photo needed anymore) • escalation & payment rails (gift cards → crypto, because untraceable and irreversible) • distribution threats as leverage. Scale: Cybertip.ca averages multiple sextortion reports **per day** nationally. |
| 15 min | **The law panel:** what's actually criminal in Canada — extortion (Criminal Code s.346) • publication of intimate images without consent (s.276) • fraud & identity theft • child exploitation material offences. Key point for victims: *the crime is committed by the threatener, every single time.* Victim rights: reporting to police (it IS a reportable offence), Cybertip.ca, Take It Down, Project Arachnid for CSAEM. Informational only — not legal advice. |
| 5 min | Anonymous question slips; counsellor closes with support resources (NeedHelpNow.ca). |

**Materials:** business-model diagram (D5), law summary sheet (D6), slips.

## Session 7: "The 3 Do Nots Deep Dive" — Protocols in Action 🛑 (50 min)
<<<<<<< HEAD
=======
**In this session:** Vault + Clause lead; Static (reporting map).
>>>>>>> 723954f (first commit)
**Objective:** Execute the full victim protocol including evidence preservation and reporting decisions. *(Counsellor present.)*

| Time | Activity |
|------|----------|
| 10 min | Recap the 3 Do Nots at adult depth: why paying funds escalation • why replying re-establishes contact • why deletion destroys the evidence chain police need. Add the fourth move: **contain** — change passwords on exposed accounts, lock socials, warn close friends in advance so a leak doesn't also become a phishing event. |
| 20 min | **Protocol gauntlet:** 3 full scenarios run end-to-end (demand → escalation → fake authority → attempted re-contact weeks later). Teams produce the complete response file: timeline log, evidence screenshots list, exact report text for Cybertip.ca/police, containment checklist. Teacher + counsellor audit each file against a rubric. |
| 10 min | **The reporting decision tree:** when to call police vs. report online (images of minors → always reportable; threats against safety → police now; everything else → Cybertip first). Who can report: the victim, a parent, or anyone with evidence — anonymity options explained. |
| 5 min | Silent reflection + slips. Counsellor availability signalled clearly for the rest of the week. |

**Materials:** gauntlet scenario files (D7), decision tree poster, audit rubric.

## Session 8: "Crypto Scam Basics" — Rug Pulls, Airdrops & Pump-and-Dump (50 min)
<<<<<<< HEAD
=======
**In this session:** Ledger leads; Cipher, Patch guests.
>>>>>>> 723954f (first commit)
**Objective:** Apply a red-flag framework to crypto/finance scams. *(Defensive education only — no platforms, no wallets, no token promotion.)*

| Time | Activity |
|------|----------|
| 5 min | Hook: "An influencer with 2M followers told his followers to buy this coin. It went to zero in 48 hours and he cashed out at the top. That's not bad luck — that's the product." |
| 15 min | Teach the scam menu: **rug pulls** (developers vanish with liquidity) • **fake airdrops** ("free tokens" = wallet-drain phishing — connecting your wallet to the fake site IS the theft) • **pump-and-dump** (coordinated shill → retail buys the top) • **influencer shilling** (paid promotion disguised as opinion) • **recovery-agent scams** (the second layer: "we can hack your money back" — they'll steal what's left). Underlying psychology: FOMO, scarcity timers, authority, and why crypto's irreversibility makes it the scammer's favourite rail. |
| 15 min | **Scam autopsy lab:** 3 real, publicly documented cases (labelled printouts). Teams build the anatomy: hook → trust builders → the ask → exit → who profited. Then apply the class-built **red-flag framework** to 4 fresh "offers" and vote INVEST / AVOID / REPORT with reasons. |
| 5 min | The framework on one card (D8): guaranteed returns? urgency? wallet connection for a "prize"? anonymous team? influencer-only credibility? unregulated promises? Any two = walk. |
| 10 min | Consumer-protection reality check: most crypto has NO Canadian investor protection if it goes wrong — the only real defence is not entering. Tie to S6: why syndicates moved sextortion payments to crypto. Exit ticket. |

**Materials:** case printouts, framework card D8, voting slips.

## Session 9: "Social Media Algorithms" — Echo Chambers & Engagement Bait (50 min)
<<<<<<< HEAD
=======
**In this session:** Signal leads; Ghost (paid amplification).
>>>>>>> 723954f (first commit)
**Objective:** Explain algorithmic manipulation; audit and deliberately reshape one personal feed.

| Time | Activity |
|------|----------|
| 5 min | Hook: two students, same platform, same topic — completely opposite feeds. "Who hacked one of you?" (Answer: the algorithm, separately.) |
| 10 min | Teach: engagement as the product • outrage/curiosity weighting • **echo chambers & radicalization gradients** (how feeds drift) • engagement bait ("share if you agree") as data harvesting • recommendation systems in AI era (auto-generated content flooding feeds). |
| 20 min | **Feed audit lab:** students screenshot their own feed (or a provided sample), categorize the top 10 items by intent (inform/entertain/provoke/sell), identify the one pattern they didn't choose, then actively reshape: unfollow/mute 3 sources, follow 2 deliberate ones, use platform controls ("not interested", timeline reset). Written before/after plan. |
| 5 min | The media diet concept: you can curate your information environment like any other environment — the algorithm optimizes for time, not truth. |
| 5 min | Exit ticket: *One thing my feed optimized for that I didn't ask for, and one control I'll use this week.* |

**Materials:** audit worksheet (D9), sample feeds for no-device version.

## Session 10: "The Wild West Simulation" — Multi-Platform Scenario (50 min)
<<<<<<< HEAD
=======
**In this session:** Cipher leads (IC); all specialists score domains, Signal runs the feed.
>>>>>>> 723954f (first commit)
**Objective:** Execute integrated incident response across simultaneous threats.

| Time | Activity |
|------|----------|
| 5 min | Briefing: you are the **Incident Response Team**. Over the next 40 minutes, your "client" (a scripted persona) receives escalating multi-front attacks. Teams of 4–5 take rotating roles: Comms (handles incoming messages), Forensics (analyses media/links), Protocol (runs victim protocols), Legal (decides reporting). |
| 35 min | **The Simulation** (Appendix packet): Wave 1 — phishing link in a "school" email. Wave 2 — cloned-voice urgent money request from the client's parent. Wave 3 — deepfake video of the client circulating. Wave 4 — sextortion demand referencing an old photo. Wave 5 — "recovery agent" DM offering to fix everything for a crypto fee. Teams log every decision with timestamp, rationale, and reporting target. Teacher injects complications (evidence "deleted", peer pressure to stay quiet). |
| 10 min | Debrief: where did teams break down? Which wave was hardest and why? The meta-lesson: **multi-front attacks are designed so you can only handle one at a time — the protocol is what lets you triage.** |

**Materials:** simulation packet (D10), role cards, decision log sheets, timers.

## Session 11: "Guest Speaker Panel" — Real-World Cyber Experts (50 min)
<<<<<<< HEAD
=======
**In this session:** Clause briefs panel; Static moderates.
>>>>>>> 723954f (first commit)
**Objective:** Hear directly from practitioners; connect curriculum to real careers and cases.

| Time | Activity |
|------|----------|
| 5 min | Intro + panelist bios. Suggested mix: **RCMP/Cyber Crime unit officer** (what actually gets reported, what helps investigations) • **IT forensics/detection professional** (how deepfakes are really caught) • **youth advocate or lawyer** (victim rights, the law in plain language). Alternates: bank fraud unit, platform trust-and-safety rep. |
| 30 min | Panel Q&A — students submit questions anonymously beforehand (slips or form); teacher curates ~8. Guaranteed questions: *What's the most common mistake victims make?* • *What evidence actually helps police?* • *What do you wish schools taught earlier?* |
| 10 min | Careers corner: what these jobs actually are, paths in, and the honest part (grinding, gravity, why it's still worth it). |
| 5 min | Thank-yous; panelists stay for optional 1:1 chats. Exit ticket: *One thing I'll do differently after today.* |

**Materials:** question slips pre-collected, bios printed, A/V check.

## Session 12: "Review & Certification" — Digital Self-Defense Champion Graduation 🎉 (50 min)
<<<<<<< HEAD
=======
**In this session:** Cipher leads; Static sign-off, full cast on stage.
>>>>>>> 723954f (first commit)
**Objective:** Demonstrate mastery; certify; transition to ambassador role.

| Time | Activity |
|------|----------|
| 20 min | **Champion Challenge:** 8-station circuit covering all blocks (audit quiz, MFA rank + recovery plan, clone-or-real audio, deepfake brief, protocol file audit, crypto red-flags vote, feed-audit reflection, simulation mini-wave). Teams rotate; scored out of 32. |
| 10 min | **Ambassador pledge:** graduates sign up as peer ambassadors — running Program 2 sessions for Grades 6–8 next year (they become the "older kid who knows"), or leading a classroom demo for their school. This is how the framework compounds. |
| 15 min | **Graduation:** certificates ("Digital Self-Defense Champion"), Quickie Card v3 issued, family guests welcome, panelist video message if recorded. |
| 5 min | Final reflection: *The single strongest defence I now have is ___ — and the person I'd call first is ___.* Collected privately. |

**Materials:** station circuit setups, certificates, ambassador pledge forms.

---

## 🚩 CTF Integration & Worksheets
*Capture The Flag scenarios mapped to the Cheat Sheet (uppusaikiran.github.io/hacking/Capture-the-Flag-CheatSheet/)*

| Session | CTF Scenario | Cheat Sheet Category | Worksheet Reference |
|---------|--------------|---------------------|-------------------|
| S1 | The School Server | System (Boot2Root) | `07_CTF_Worksheets.md#school-server` |
| S2 | MFA Mayhem | Web Hacking (Auth) | `07_CTF_Worksheets.md#mfa-mayhem` |
| S4 | Deepfake Detectives | Forensics (EXIF/Hash) | `07_CTF_Worksheets.md#deepfake-detectives` |
| S8 | Crypto Rush & Rug Pulls | Crypto (Smart Contracts) | `07_CTF_Worksheets.md#crypto-scam-autopsy` |
| S10 | Privilege Climb | PrivEsc (Linux Permissions) | `07_CTF_Worksheets.md#priv-escalation` |

**Implementation Notes:**
- Flags follow the format `flag{answer}`.
- QR codes link to a local verification server or GitHub Pages.
- Real VMs (TryHackMe/Docker) and cheat sheet one-liners (`nmap`, `strings`) are used for 9-12.
- Full worksheet templates are in `07_CTF_Worksheets.md`.

---

## Appendix: Simulation Scenario Packet (Session 10)
Each wave card: **TIMESTAMP** • **INCOMING ITEM** (message/clip/link description) • **TEAM LOG** (decision, rationale, reporting target). Teacher script includes the complication injections and the ground-truth reveal for each wave (e.g., Wave 3 video = deepfake of a teacher; Wave 5 recovery agent = second-layer scam — correct play is to ignore AND report it). Full answer key in the Assessments file.
