# CarryBot — MMAR 2026 Contacts

Public contact page for the CarryBot poster presented at the 30th International Conference on Methods and Models in Automation and Robotics ([MMAR 2026](https://mmar.pl/)), Międzyzdroje, Poland.

This repo exists on its own, separate from the main project repo, because that one has to stay private until our paper clears the IEEE publication process. This one only holds the contact page and QR assets, so it's safe to keep public in the meantime.

## What's in the poster

The CarryBot poster carries two QR codes:

| QR code          | Target                                    |
|-------------------|--------------------------------------------|
| `demo_qr.png`      | Demo video (Google Drive)                   |
| `contact_qr.png`   | `contact.html` — team photos, names, emails |

## Files

- `contact.html` — the team contact page, served via GitHub Pages.
- `photos/`, `University_logo.png` — headshots and logo referenced by `contact.html`.
- `generate_qr_codes.py` — regenerates `contact_qr.png` and `demo_qr.png`                from the team roster and target URLs.

## Regenerating the QR codes

```bash
pip install qrcode[pil]
python generate_qr_codes.py
```

## Related

Main project repo (private until the paper is published on IEEE):
`Autonomous_Airport_Assistant_Robot-CarryBot`
