# Changelog

All notable changes to this repository are recorded here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) for the curriculum
release as a whole.

**Why a curriculum needs semantic versions:** a version number here means "the
material changed in a way a board needs to notice." A patch release is a typo or
a broken link. A minor release adds or reorders lessons. A major release changes
what students are taught to *do* — and therefore what the assessment, the parent
toolkit, and the teacher training must say.

---

## [Unreleased]

### Fixed

- **Remaining v3.0 consistency gaps.** The phase plans still had students write
  real passwords or passphrases (Phases 1–2), set up MFA on personal accounts
  (Phases 3–4), and record family voices (Phase 3). Those activities now use
  invented credentials, demo or school-managed accounts, and synthetic or
  licensed audio.
- **Provenance-first media checks completed.** Phases 2–4, the Program 1
  AI Art Detective worksheet, the Program 3 evidence brief, and the Program 2–3
  Lens persona still led with visual tells. They now use source → reverse image
  search → corroboration → clues, and the Program 1 flag changed from
  `flag{ai_detected}` to `flag{check_the_source}` (rubric updated).
- **Resource and reporting-route corrections.** NeedHelpNow.ca is no longer
  described as a 24/7 line; C3P is no longer credited with restorative-practice
  programmes; reporting routes now distinguish Cybertip.ca (online sexual
  exploitation of children) from police and the Canadian Anti-Fraud Centre
  (adult image and fraud cases).
- **Worksheet and mapping corrections.** Program 1 worksheets now match their
  lesson counts (6 emails, 8 cards, 6 AI items, 5 links, 10 scavenger cards),
  and the "Link Lab Sorting" worksheet was renamed to match its Track A
  session.
- **Build and documentation fixes.** `make pdf-export` no longer overwrites each
  program's handout PDF; the QR output path is consistent across the script,
  `.gitignore`, Makefile, and assets README; stale "Agent Nova" and `flag{3}`
  examples were corrected; the phase plans carry the v3.0 version label.

---

## [3.0.0] — 2026-10-25

This release is a correctness and safety pass over the whole repository. The
curriculum structure is unchanged: four phases, three programs, the same session
counts, the same personas. What changed is what the material tells students to
believe and to do.

**Read this release if you have already trained staff on the previous version.**
Two protocols changed, and three factual claims were withdrawn.

### Changed

- **Sextortion response is now one protocol: 3 Do Nots + Tell.** Don't pay,
  don't reply, don't delete, tell a trusted adult. The repository previously
  taught "Stop, Screenshot, Block, Report" in Phase 3, Phase 4, and the Program 2
  worksheet, while Programs 2 and 3, the parent toolkits, and the framework's
  protocol list taught the 3 Do Nots. A student met one mnemonic in Grade 7 and a
  different one in Grade 9. "Stop" is also not advice a frightened student can
  act on, and the retired mnemonic had no answer for financial sextortion — now
  the dominant form. Screenshotting and reporting survive inside "don't delete"
  and "tell".
- **Synthetic media is taught provenance-first.** The order of checks is now
  source → reverse image search → corroboration → forensic artefacts. Visual and
  audio "tells" are described as clues, not proof, because current generators
  make fewer errors every year and the same artefacts appear in compressed real
  photographs. The assessment outcome changed from "spot the deepfake" to
  "state what the evidence does and does not prove."
- **The same standard now runs through every program.** Phase 4 already used it,
  but Programs 1–3 still taught perception first: Program 1's "tell list",
  Program 2's Session 4 objective ("spot visual deepfakes using at least 3
  tells"), Program 3's Session 5 objective ("detect synthetic audio … using
  waveform analysis"), both programs' CTF worksheets, and Phase 4's graduation
  handout ("AI detection checklist"). All now teach source → reverse search →
  corroboration → clues, and every assessment requires a statement of what the
  evidence cannot prove.
- **Voice-clone instruction corrected.** Removed the claim that 3-5 seconds of
  speech is enough to clone a voice (vendor marketing; a convincing clone needs
  closer to 30 seconds of clear speech, sometimes less), removed Fakespot (a
  review-authenticity tool, never an audio or video detector, now discontinued),
  and reframed the exercise so students learn that their ears are not a security
  control. The defence taught is procedural: a pre-agreed safe word, then a
  call-back on a number you already have.
- **AI policy alignment rebuilt.** The ISED alignment document now uses the
  published six-pillar *AI for All* strategy and states explicitly which pillars
  this framework does not serve. The framework is not an ISED resource and has no
  ISED funding or endorsement.
- **ECNO alignment rebuilt** against the 2026 four-theme campaign: Digital Me,
  Digital Us, Digital Families, Digital Minds. "ECNO" is the Educational
  Collaborative Network of Ontario; the previous document treated the campaign
  as a set of pillars it does not have.
- **Metadata is no longer evidence.** EXIF and the "Software" field are taught as
  things that are usually stripped, not as proof of origin.
- **Repository structure and documentation** now match reality: no references to
  a missing LMS-integration guide, a nonexistent `assets/templates/` directory,
  or `exports/pdf/` as if it were tracked.

### Fixed

- **Criminal Code citation.** Ten occurrences across seven files cited **s.276**
  for publication of intimate images. s.276 is an evidence rule about a
  complainant's sexual history. The offence is **s.162.1**. The legal section now
  also cites s.162.1(1.1) (threats to publish) and s.162.1(2)(b), which expressly
  covers AI-generated depictions, and names s.346 (extortion), s.380 (fraud), and
  ss.402.2/403 (identity theft and fraud).
- **The Stop & Think context checklists.** The sextortion checklist asked "Can I
  afford it?" and "Did I send the original photo publicly or privately?" — the
  first treats payment as a live option, the second puts the student's behaviour
  on trial. It is now the four moves. The deepfake checklist led with visual
  artefacts; it now leads with source and corroboration.
- **Resource details.** Cybertip.ca is **1-866-658-9022**, operated by the
  Canadian Centre for Child Protection, staffed Monday–Friday 8:30–16:00 Central
  Time. It is not a 24/7 line; the material now says so and routes emergencies to
  9-1-1, Kids Help Phone (1-800-668-6868), and 9-8-8.
- **Forty merge-conflict markers** that had been committed and published were
  resolved. All kept the incoming side; 39 had an empty other side.
- **CTF worksheets.** Program 3's worksheet ended mid-table at a corrupt
  fragment; rebuilt. Program 2's Caesar texts decoded to nonsense; replaced with
  real shifts and a stated space convention. Two flags were unvalidatable
  placeholders (`flag{green_count}`, `flag{happy_count}`).
- **Session mappings.** Program 2's Wi-Fi Whisperer was mapped to a visual
  deepfake session; Program 3's Privilege Climb to the final simulation and its
  mood audit to the sextortion session. Program 1's mood tracker was labelled
  Session 6, which is Review & Celebration. All three lesson-plan tables and
  every worksheet anchor now resolve to the session that actually teaches the
  material.
- **The scoring rubric** was regenerated from the worksheets. It previously
  listed five sessions per program, matched none of the flags, and was dated
  September 2024. All 18 flags now match, and the validation regex is one the
  flags actually satisfy.
- **Framework version metadata** disagreed with itself: the header said 2.0, the
  footer said 3.0, and the draft beside it said nothing. One version, one place,
  and a version history.

### Removed

- Claims that do not survive checking: **AIDA** as current law (it did not
  proceed), **"Canada.AI"** and a **G7 Canada.AI** programme (no such
  programmes), **CPTPP AI guidelines for Indigenous data sovereignty** (no such
  instrument), and a five- or seven-pillar AI strategy (the strategy has six
  pillars with different names).

### Safety and privacy

- **Phase 4 no longer asks students to write down real passwords.** The exercise
  maps account *names* only, and practises detection on a teacher-supplied dump
  of fictional credentials.
- **No student records their own or a family member's voice** for a cloning
  exercise. Synthetic samples or licensed clips are used.
- **No classmate's image, name, or account** is used in a forensic or OSINT
  exercise.
- **Deepfake creation is not an activity** in this curriculum. Analysis is.
- Safeguarding requirements are now written down in the framework: counsellor
  presence for sensitive topics, a named response protocol, board
  mandatory-reporting procedures, an opt-out that requires no explanation,
  crisis routes posted in the room, and no requirement to disclose personal
  experience.
- Non-curriculum material — including the OpenCyberRange product, which targets
  K-2 with `ping`, `nmap`, and `curl` — moved to `_archive/` with a written
  rationale rather than being deleted.

### Added

- `scripts/validate_repo.py` — a standard-library validator that fails on merge
  conflict markers, UTF-8 BOMs, broken relative links and heading anchors,
  inline paths to files that do not exist, and CTF flags that violate their own
  format rule or disagree with the rubric.
- `.github/workflows/validate.yml` — runs the validator on push and pull request.
- `CHANGELOG.md` — this file.
- `Digital_Self_Defense_Foundation.md` — the five competency arcs that the
  framework delivers, linked from the framework and the README.
- `.gitattributes` and an expanded `.gitignore`, so line endings and generated
  artefacts stop producing noise in diffs.
- Framework sections that existed only in an unmerged draft: the four-stage
  architecture with exit competencies, the 9-10 and 11-12 topic tables,
  authentication guidance, the legal framework, safety guidelines, the
  autonomy ladder, transfer-based assessment, accessibility, professional
  development, and references.

### Known limitations

- The CTF answer keys are teacher-facing text in the worksheets. There is no
  automated grader; flags are checked with the rubric and a regex, not a server.
- QR codes are generated per deployment and are git-ignored, so a printed
  worksheet's QR target is a local decision, not a repository artefact.
- The repository has no unit tests. The validator is structural, not semantic:
  it cannot tell you that a lesson is pedagogically sound, only that it is
  internally consistent.
- English only. The framework recommends bilingual materials; none are included.

---

## [2.0.0] — 2026-10

The AI literacy release, reflected in the framework document's own change log.
No tag was created at the time; this entry is reconstructed from the document.

### Added

- ISED Canada's National AI Strategy — *AI for All* as an integrated resource
- Canadian AI innovator spotlights (Mila, Vector, Amii)
- National AI Policy Debate and AI for All Challenge capstone projects
- AI Literacy For All curriculum integration across all phases

---

## [1.0.0] — 2026-09

### Added

- Initial K-12 framework
- Phase plans for K-2, 3-5, 6-8, and 9-12
- Program 1 (K-5), Program 2 (6-8), and Program 3 (9-12) guides, lesson plans,
  student handouts, parent toolkits, assessments, persona casts, and CTF
  worksheets
- ECNO and ISED alignment documents
- `Stop_Think_Reinforcement.md`, issue and pull-request templates, MIT licence

---

[Unreleased]: https://github.com/RobChaykoski/K12_Digital_Self_Defense_Framework/compare/v3.0.0...HEAD
[3.0.0]: https://github.com/RobChaykoski/K12_Digital_Self_Defense_Framework/releases/tag/v3.0.0
[2.0.0]: https://github.com/RobChaykoski/K12_Digital_Self_Defense_Framework/commits/main
[1.0.0]: https://github.com/RobChaykoski/K12_Digital_Self_Defense_Framework/commits/main
