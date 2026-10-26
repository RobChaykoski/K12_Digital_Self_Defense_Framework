# Archive

This directory holds material that was previously mixed into the curriculum tree but is **not part of the K-12 Digital Self-Defense Framework**. It is retained rather than deleted so the history and the reasoning stay available.

Nothing here is part of the published deliverable. If you are looking for the curriculum, start at the repository root `README.md`.

---

## `k5_opencyberrange/`

`K-5_Enhanced_Exercise.md`, `K-5_Scenario_Template.md`, `K-5_Student_Guide.md`, `K-5_Teacher_Guide.md`, and `K-5_Cyber_Engagement_Package/`.

These belong to a **different product** — the OpenCyberRange platform — not to this framework. Evidence:

- They teach `ping`, `nmap`, and `curl` to **Grades K–2**.
- They assume a lab environment launched from `lab.yaml` with Docker.
- They use the `OCR{...}` flag convention, not this framework's `flag{...}` convention.
- They reference an "Admin Panel → Exercises → Tracks & Levels" UI that does not exist here.

They were never referenced by any file in the canonical tree. Keeping them would have left a teacher able to mistake a grade-inappropriate network-scanning lab for part of the K–5 curriculum, which is both an age-appropriateness problem and a safeguarding one.

The canonical K–5 content lives in `Programs/Program_1_Foundations_K-5/`.

## `superseded_copies/`

- `Corrected_ECNO_Alignment_Guide.md` — byte-identical (MD5) to `ECNO_Alignment_Guide.md`. The "Corrected" prefix is misleading; it contains the same defects as its source.
- `Corrected_Lesson_Plans.md` — byte-identical to `Programs/Program_3_Legal_AI_Grades9-12/02_Lesson_Plans.md`, including the same unresolved merge-conflict markers. It also carried the incorrect Criminal Code citation.
- `Framework_Updates_Summary.md` and `Final_Framework_Updates_Changelog.md` — both describe corrections (the s.276 → s.162.1 fix, conflict-marker resolution, AI-detection changes) that were **not** present in the canonical framework at the time of archiving. They are superseded by the real `CHANGELOG.md` at the repository root.
- `Framework_Review_Summary.md` — a historical review artifact. Its claim that AI literacy begins in Grade 3 contradicts the framework's existing K–2 AI content.
- `_temp_tree.txt` — a generated directory listing, retained only as an artifact.

## `unused_diagrams/`

`growth_diagram.svg`, `k12_growth_diagram.svg`, `k12_growth_diagram_2.svg`.

None were referenced by any document in the repository. `k12_growth_diagram.svg` and `k12_growth_diagram_2.svg` are byte-identical. `growth_diagram.svg` declares a `0 0 1400 900` viewBox while placing High School content at y=700–1060, so that content renders clipped.

If a progression diagram is wanted, it should be authored fresh against the four-phase structure and referenced from the README.
