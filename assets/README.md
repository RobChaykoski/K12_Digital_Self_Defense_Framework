# 🖼️ Assets Directory

This folder is for images, logos, and downloadable resources that ship with the framework.

It currently contains only this README. The directories described below are created on demand as material is added — they are not checked in empty.

## 📁 Intended structure
```
assets/
├── logos/          # School / program branding
├── templates/      # Editable handout templates (DOCX/PPTX)
└── screenshots/    # LMS preview images
```

Generated QR codes are written to `assets/qr_codes/` by `scripts/generate_qr.py` and are git-ignored, because they encode deployment-specific URLs.

## 📝 Notes
- Keep files under 2 MB where possible
- Use PNG for transparency, JPG for photographs
- QR codes should point at HTTPS endpoints, never at a personal device or file path
- Add an entry to this README when you add a new subdirectory, so the next person can find it
