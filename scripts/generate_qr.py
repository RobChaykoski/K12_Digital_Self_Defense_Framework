#!/usr/bin/env python3
"""
QR Code Generator for K12 Digital Self-Defense CTF Worksheets
Generates QR codes that link to a flag submission endpoint or local validation page.
"""
import os
import sys
from pathlib import Path

try:
    import qrcode
except ImportError:
    print("❌ Missing dependency: qrcode")
    print("Install with: pip install qrcode[pil]")
    sys.exit(1)


def generate_qr(url: str, output_name: str, folder: str = "assets/qr_codes") -> None:
    """Generate a QR code for the given URL and save it."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    output_path = Path(folder) / output_name
    os.makedirs(folder, exist_ok=True)
    img.save(output_path)
    print(f"✅ Generated: {output_path}")


def main():
    # Example usage patterns:
    # python scripts/generate_qr.py "https://your-site.com/submit-flag" "worksheet_01.png"
    # python scripts/generate_qr.py "https://your-site.com/ctf/k5/session3" "k5_s3_qr.png"

    if len(sys.argv) < 3:
        print("Usage: python generate_qr.py <URL> <OUTPUT_FILENAME>")
        print("Example: python generate_qr.py 'https://example.com/flag' 'session1_qr.png'")
        sys.exit(1)

    url = sys.argv[1]
    filename = sys.argv[2]
    generate_qr(url, filename)


if __name__ == "__main__":
    main()
