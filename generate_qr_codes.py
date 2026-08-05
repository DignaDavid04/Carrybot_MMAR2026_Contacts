"""
Generates the CarryBot poster contact page and its two QR codes.

The poster carries two QR codes:
    QR 1  demo_qr.png     -> Google Drive demo video (opens straight into the player)
    QR 2  contact_qr.png  -> contact.html (team photos, names, emails)

Setup (once):
    pip install qrcode[pil]

Run (from this folder):
    python generate_qr_codes.py
"""

from pathlib import Path

import qrcode

HERE = Path(__file__).resolve().parent

# Opens directly in Google Drive's video player.
DEMO_VIDEO_URL = "https://drive.google.com/file/d/1vwK6EDCWHPQNqCMkmaF2zhuxJl4Q6nLp/view?usp=drive_link"

CONTACT_PAGE_URL = "https://dignadavid04.github.io/Carrybot_MMAR2026_Contacts/contact.html"

AFFILIATIONS = {
    1: "Dept. of Intelligent Interactive Systems",
    2: "Dept. of Decision Systems and Robotics",
}

TEAM = [
    {
        "name": "Zdzisław Kowalczuk",
        "affil": 1,
        "email": "kova@pg.edu.pl",
        "photo": "zdzislaw_kowalczuk.webp",
    },
    {
        "name": "Digna David",
        "affil": 2,
        "email": "s206959@student.pg.edu.pl",
        "photo": "digna_david.jpg",
    },
    {
        "name": "Dilbrin Mustafa",
        "affil": 2,
        "email": "s201872@student.pg.edu.pl",
        "photo": "dilbrin_mustafa.png",
    },
    {
        "name": "Zhangirkhan Baurzhanov",
        "affil": 2,
        "email": "s207317@student.pg.edu.pl",
        "photo": "zhangirkhan_baurzhanov.png",
    },
]


def initials(name: str) -> str:
    parts = [p for p in name.split() if p]
    return "".join(p[0] for p in parts[:2]).upper()


CSS = """
  :root{
    --navy:   #002147;
    --blue:   #0057A8;
    --light:  #E5F0FD;
    --mid:    #B4D4F8;
    --gold:   #FFB400;
    --ink:    #14171c;
    --paper:  #ffffff;
    --line:   #d7e4f7;
    --radius: 14px;
  }
  *{ box-sizing:border-box; }
  html, body{ height:100%; margin:0; }
  body{
    display:flex; flex-direction:column;
    min-height:100vh; min-height:100dvh;
    background:var(--paper); color:var(--ink);
    font-family:"IBM Plex Sans", -apple-system, "Segoe UI", Arial, sans-serif;
    line-height:1.35;
  }
  .mono{ font-family:"IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace; letter-spacing:.04em; }
  a{ color:inherit; }

  header{
    flex:0 0 auto;
    background:linear-gradient(180deg, var(--navy) 0%, #001836 100%);
    color:#fff; text-align:center;
    padding:clamp(12px,3vh,26px) clamp(14px,4vw,24px) clamp(10px,2vh,18px);
  }
  .logo{
    width:clamp(36px,8vw,64px); margin:0 auto clamp(8px,1.6vh,14px); display:block;
  }
  .logo img{ width:100%; height:auto; display:block; }
  h1{
    margin:0; font-weight:700; letter-spacing:-.005em; line-height:1.25;
    font-size:clamp(14px, 3.4vw, 22px);
  }
  h1 .accent{ color:var(--gold); }
  .subtitle{
    margin:clamp(4px,1vh,8px) 0 0; color:#c9dbf5; font-weight:500;
    font-size:clamp(9.5px, 2vw, 12.5px);
  }

  main{
    flex:1 1 auto; min-height:0;
    display:flex; flex-direction:column; justify-content:center;
    max-width:820px; width:100%; margin:0 auto;
    padding:clamp(8px,2vh,20px) clamp(12px,4vw,20px);
  }
  .section-label{
    font-size:11px; font-weight:600; text-transform:uppercase;
    letter-spacing:.08em; color:var(--blue); text-align:center;
    margin:0 0 clamp(8px,1.6vh,14px);
  }

  .team{
    display:grid;
    grid-template-columns:repeat(2, 1fr);
    gap:clamp(10px,1.8vw,22px);
  }
  .member{
    display:flex; flex-direction:column; align-items:center; text-align:center;
    gap:6px;
    background:#fff; border:1px solid var(--line); border-radius:var(--radius);
    padding:clamp(10px,2.4vh,24px) clamp(10px,2.4vw,22px);
    min-width:0;
  }
  .avatar-wrap{
    position:relative; flex:none;
    width:clamp(38px,9vw,72px); height:clamp(38px,9vw,72px);
    border-radius:50%; overflow:hidden; background:var(--blue);
  }
  .avatar-wrap img{
    width:100%; height:100%; object-fit:cover; display:block;
  }
  .avatar-wrap .fallback{
    position:absolute; inset:0; display:none; align-items:center; justify-content:center;
    color:#fff; font-weight:600; font-size:clamp(12px,3vw,20px); background:var(--blue);
  }
  .member h4{ margin:0; font-weight:600; font-size:clamp(11.5px,2.6vw,19px); }
  .member .role{ margin:0; color:#5a6472; font-size:clamp(9px,2vw,14px); }
  .member a.email{
    color:var(--blue); text-decoration:none; word-break:break-all;
    font-size:clamp(8.5px,1.9vw,13.5px);
  }
  .member a.email:hover{ text-decoration:underline; }
  .affil-legend{
    margin-top:clamp(8px,1.6vh,14px); text-align:center;
    color:#8592a3; font-size:clamp(8.5px,1.8vw,11px);
  }

  footer{
    flex:0 0 auto;
    background:var(--light); text-align:center;
    color:var(--navy); font-weight:600;
    padding:clamp(10px,2vh,20px) clamp(14px,4vw,20px);
    font-size:clamp(9.5px,2vw,12.5px);
  }
  footer .conf{ display:block; margin-top:4px; font-weight:500; color:#4a5568; font-size:.95em; }
"""


def render_member(m: dict) -> str:
    dept = AFFILIATIONS[m["affil"]]
    return f"""        <div class="member">
          <div class="avatar-wrap">
            <img src="photos/{m['photo']}" alt="{m['name']}"
                 onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
            <div class="fallback">{initials(m['name'])}</div>
          </div>
          <h4>{m['name']}<sup>{m['affil']}</sup></h4>
          <p class="role">{dept}</p>
          <a class="email mono" href="mailto:{m['email']}">{m['email']}</a>
        </div>"""


def render_html() -> str:
    members_html = "\n".join(render_member(m) for m in TEAM)
    affil_legend = "  &nbsp;&nbsp;·&nbsp;&nbsp; ".join(
        f"<sup>{k}</sup>{v}" for k, v in AFFILIATIONS.items()
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CarryBot — Contacts</title>
<meta name="description" content="Project team and contact details for CarryBot, presented at MMAR 2026.">
<meta property="og:title" content="CarryBot — Project Team">
<meta property="og:description" content="Project team and contact details for CarryBot, presented at MMAR 2026.">
<meta property="og:image" content="University_logo.png">
<link rel="icon" href="University_logo.png">
<style>{CSS}</style>
</head>
<body>

  <header>
    <div class="logo"><img src="University_logo.png" alt="Gdańsk University of Technology"></div>
    <h1>Interactivity of a Mobile Robot: A Case Study of the
        Autonomous Airport Assistant <span class="accent">CarryBot</span></h1>
    <p class="subtitle">30th International Conference on Methods and Models
       in Automation and Robotics (MMAR 2026) · Miedzyzdroje, Poland</p>
  </header>

  <main>
    <p class="section-label">Contacts</p>
    <div class="team">
{members_html}
    </div>
    <p class="affil-legend">{affil_legend}</p>
  </main>

  <footer>
    Department of Intelligent Interactive Systems &amp; Department of Decision Systems and Robotics
    <span class="conf">Faculty of Electronics, Telecommunications and Informatics, Gdańsk University of Technology, Gdańsk, Poland</span>
  </footer>

</body>
</html>
"""


def write_contact_html():
    (HERE / "contact.html").write_text(render_html(), encoding="utf-8")
    print("  wrote contact.html")


def make_qr(data, filename):
    img = qrcode.make(data, error_correction=qrcode.constants.ERROR_CORRECT_M)
    img.save(HERE / filename)
    print(f"  wrote {filename}  ->  {data}")


def main():
    (HERE / "photos").mkdir(exist_ok=True)

    print("Generating contact page...")
    write_contact_html()

    print("Generating QR codes...")
    make_qr(DEMO_VIDEO_URL, "demo_qr.png")
    make_qr(CONTACT_PAGE_URL, "contact_qr.png")


if __name__ == "__main__":
    main()