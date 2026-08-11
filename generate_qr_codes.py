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
        "title": "prof. dr hab. inż.",
        "affil": 1,
        "email": "kova@pg.edu.pl",
        "photo": "zdzislaw_kowalczuk.webp",
        "slug": "kowalczuk",
        "bio": (
            'Zdzisław Kowalczuk (ORCID: <a href="https://orcid.org/0000-0001-9174-546X" '
            'target="_blank" rel="noopener">0000-0001-9174-546X</a>) obtained his MSc in '
            "Electronics and PhD degrees at Gdańsk University of Technology (GUT) in 1978 "
            "and 1986, respectively, and his DSc (habilitated doctor's) degree at the "
            "Silesian University of Technology in 1993. The title of professor was awarded "
            "by the President of Poland in 2003. Since 1978 he has been at the Faculty of "
            "Electronics, Telecommunications, and Informatics at GUT, where he is a Full "
            "Professor of Automation and Robotics. He is President of the Polish Society "
            "for Measurement, Automation and Robotics (POLSPAR, the NMO of IFAC) and "
            "served as Chair of the IFAC Technical Committee on Intelligent Autonomous "
            "Vehicles (TC 7.5) from 2020 to 2026. He is a member of IEEE (Life Senior from "
            "2025) and of the Committee on Automation and Robotics of the Polish Academy "
            "of Sciences. His research interests include autonomous agents, cognitive "
            "architectures, artificial emotions, scheduling variable control, the ISD "
            "framework, system identification, and fault detection. He is the originator "
            "of the eQualia hypothesis and author of over 30 books, 130 journal articles "
            "(over 50 in JCR), over 250 conference papers, and 80 book chapters. His "
            "Google Scholar citation index exceeds 3,800 (Hirsch index 18–24). He is a "
            "recipient of awards from the Minister of National Education in 1990, 2003, "
            "and 2025, and the Polish National Science Foundation Award in automatic "
            "control (1999)."
        ),
    },
    {
        "name": "Digna David",
        "affil": 2,
        "email": "s206959@student.pg.edu.pl",
        "photo": "digna_david.jpg",
        "slug": "digna-david",
        "linkedin": "https://linkedin.com/in/digna-sukeerthi-abisha-david-131639223",
        "portfolio": "https://dignadavid04.github.io",
        "bio": (
            "Digna David holds a Bachelor's degree in Electronics and Communication "
            "Engineering from Anna University, India. She is currently pursuing a "
            "Master's degree in Automatic Control, Cybernetics and Robotics at Gdańsk "
            "University of Technology, Poland. She has professional experience as an "
            "Embedded Systems Engineer at Capgemini in embedded Linux and IoT systems. "
            "Her research interests include cognitive robotics, artificial intelligence, "
            "and affective computing, with a focus on emotional models in autonomous "
            "agents."
        ),
    },
    {
        "name": "Dilbrin Mustafa",
        "affil": 2,
        "email": "s201872@student.pg.edu.pl",
        "photo": "dilbrin_mustafa.png",
        "slug": "dilbrin-mustafa",
        "linkedin": "https://linkedin.com/in/dilbrin-azad-767437294",
        "portfolio": "https://dilbrin-mustafa.github.io",
        "bio": (
            "Dilbrin Mustafa holds a Bachelor's degree in Information Security from "
            "Duhok Polytechnic University (2018–2022). He works as a Full Stack "
            "Developer at Lelav Technology, building web applications across both the "
            "frontend and backend. He is currently pursuing a Master's degree in "
            "Automatic Control, Cybernetics and Robotics at Gdańsk University of "
            "Technology, where he focuses on bridging software development with "
            "intelligent automation. His interests include full-stack web development, "
            "Python programming, and control systems."
        ),
    },
    {
        "name": "Zhangirkhan Baurzhanov",
        "affil": 2,
        "email": "s207317@student.pg.edu.pl",
        "photo": "zhangirkhan_baurzhanov.png",
        "slug": "zhangirkhan-baurzhanov",
        "linkedin": "https://linkedin.com/in/zhangirkhan-baurzhanov",
        "bio": (
            "Zhangirkhan Baurzhanov holds a Bachelor's degree in Metrology Engineering "
            "from West Kazakhstan Agrarian Technical University named after Zhangir Khan "
            "(2020–2024). He worked as a Metrology Engineer at Munai Gas Engineering "
            "LLP, verifying and calibrating measuring instruments to industry standards "
            "and supporting clients on-site through a mobile laboratory. He is currently "
            "completing a Master's degree in Automatic Control, Cybernetics and Robotics "
            "at Gdańsk University of Technology (expected September 2026), with a "
            "growing focus on automation, control systems, and machine vision. His "
            "standards-driven background in metrology now shapes his approach to "
            "automation and quality-control problems."
        ),
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
  main.about{ justify-content:flex-start; padding-top:clamp(14px,2.4vh,24px); }
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
  a.email{
    color:var(--blue); text-decoration:none; word-break:break-all;
    font-size:clamp(8.5px,1.9vw,13.5px);
  }
  a.email:hover{ text-decoration:underline; }
  .person-link{ display:flex; flex-direction:column; align-items:center; gap:6px; text-decoration:none; }
  .person-link:hover h4{ text-decoration:underline; }
  .icon-row{ display:flex; gap:8px; }
  a.linkedin, a.portfolio{
    display:inline-flex; align-items:center; justify-content:center;
    width:clamp(18px,3.4vw,24px); height:clamp(18px,3.4vw,24px);
    border-radius:50%; background:var(--blue); color:#fff;
  }
  a.linkedin svg, a.portfolio svg{ width:60%; height:60%; }
  a.linkedin:hover, a.portfolio:hover{ background:var(--navy); }
  .affil-legend{
    margin-top:clamp(8px,1.6vh,14px); text-align:center;
    color:#8592a3; font-size:clamp(8.5px,1.8vw,11px);
  }

  .back-link{
    display:inline-block; margin:0 0 clamp(8px,1.6vh,14px);
    color:var(--blue); text-decoration:none; font-weight:600;
    font-size:clamp(10px,2vw,13px);
  }
  .back-link:hover{ text-decoration:underline; }
  .bio-list{ display:flex; flex-direction:column; gap:clamp(14px,2.4vh,24px); }
  .bio-card{
    display:flex; gap:clamp(12px,2.4vw,20px); align-items:flex-start;
    background:#fff; border:1px solid var(--line); border-radius:var(--radius);
    padding:clamp(12px,2.4vh,22px) clamp(12px,2.4vw,22px);
  }
  .bio-card .avatar-wrap{
    width:clamp(52px,10vw,88px); height:clamp(52px,10vw,88px); flex:none;
  }
  .bio-card .bio-body{ min-width:0; }
  .bio-card h3{ margin:0; font-weight:600; font-size:clamp(13px,2.8vw,19px); }
  .bio-card .role{ margin:2px 0 8px; color:#5a6472; font-size:clamp(9.5px,2vw,13px); }
  .bio-card p.bio-text{
    margin:0 0 8px; color:var(--ink); font-size:clamp(9.5px,2vw,13.5px); line-height:1.55;
  }
  .bio-card p.bio-text a{ color:var(--blue); text-decoration:none; }
  .bio-card p.bio-text a:hover{ text-decoration:underline; }

  footer{
    flex:0 0 auto;
    background:var(--light); text-align:center;
    color:var(--navy); font-weight:600;
    padding:clamp(10px,2vh,20px) clamp(14px,4vw,20px);
    font-size:clamp(9.5px,2vw,12.5px);
  }
  footer .conf{ display:block; margin-top:4px; font-weight:500; color:#4a5568; font-size:.95em; }
"""


LINKEDIN_ICON_SVG = (
    '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
    '<path d="M20.45 20.45h-3.55v-5.57c0-1.33-.02-3.03-1.85-3.03-1.85 0-2.14 1.45'
    '-2.14 2.94v5.66H9.36V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.38-1.85 3.6 0 4.27 '
    '2.37 4.27 5.46zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12z'
    'M7.11 20.45H3.56V9h3.55z"/></svg>'
)

# Generic "link" glyph (chain-link), used for personal-site/portfolio links.
PORTFOLIO_ICON_SVG = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M10 13a5 5 0 0 0 7.07 0l2.83-2.83a5 5 0 0 0-7.07-7.07L11.5 4.5"/>'
    '<path d="M14 11a5 5 0 0 0-7.07 0L4.1 13.83a5 5 0 0 0 7.07 7.07L12.5 19.5"/>'
    "</svg>"
)


def render_icon_links(m: dict) -> str:
    icons = []
    if m.get("linkedin"):
        icons.append(
            f'<a class="linkedin" href="{m["linkedin"]}" target="_blank" '
            f'rel="noopener" aria-label="{m["name"]} on LinkedIn">{LINKEDIN_ICON_SVG}</a>'
        )
    if m.get("portfolio"):
        icons.append(
            f'<a class="portfolio" href="{m["portfolio"]}" target="_blank" '
            f'rel="noopener" aria-label="{m["name"]}\'s portfolio">{PORTFOLIO_ICON_SVG}</a>'
        )
    if not icons:
        return ""
    return '\n          <div class="icon-row">' + "".join(icons) + "</div>"


def about_page_filename(m: dict) -> str:
    return f"about-{m['slug']}.html"


def render_member(m: dict) -> str:
    dept = AFFILIATIONS[m["affil"]]
    title_prefix = f"{m['title']} " if m.get("title") else ""
    return f"""        <div class="member">
          <a class="person-link" href="{about_page_filename(m)}">
            <div class="avatar-wrap">
              <img src="photos/{m['photo']}" alt="{m['name']}"
                   onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
              <div class="fallback">{initials(m['name'])}</div>
            </div>
            <h4>{title_prefix}{m['name']}<sup>{m['affil']}</sup></h4>
          </a>
          <p class="role">{dept}</p>
          <a class="email mono" href="mailto:{m['email']}">{m['email']}</a>
        </div>"""


def render_bio_card(m: dict) -> str:
    dept = AFFILIATIONS[m["affil"]]
    title_prefix = f"{m['title']} " if m.get("title") else ""
    return f"""        <div class="bio-card">
          <div class="avatar-wrap">
            <img src="photos/{m['photo']}" alt="{m['name']}"
                 onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
            <div class="fallback">{initials(m['name'])}</div>
          </div>
          <div class="bio-body">
            <h3>{title_prefix}{m['name']}<sup>{m['affil']}</sup></h3>
            <p class="role">{dept}</p>
            <p class="bio-text">{m['bio']}</p>
            <a class="email mono" href="mailto:{m['email']}">{m['email']}</a>{render_icon_links(m)}
          </div>
        </div>"""


HEADER_HTML = """  <header>
    <div class="logo"><img src="University_logo.png" alt="Gdańsk University of Technology"></div>
    <h1>Interactivity of a Mobile Robot: A Case Study of the
        Autonomous Airport Assistant <span class="accent">CarryBot</span></h1>
    <p class="subtitle">30th International Conference on Methods and Models
       in Automation and Robotics (MMAR 2026) · Miedzyzdroje, Poland</p>
  </header>"""

FOOTER_HTML = """  <footer>
    Department of Intelligent Interactive Systems &amp; Department of Decision Systems and Robotics
    <span class="conf">Faculty of Electronics, Telecommunications and Informatics, Gdańsk University of Technology, Gdańsk, Poland</span>
  </footer>"""


def page_shell(title: str, description: str, main_html: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="University_logo.png">
<link rel="icon" href="University_logo.png">
<style>{CSS}</style>
</head>
<body>

{HEADER_HTML}

{main_html}

{FOOTER_HTML}

</body>
</html>
"""


def render_html() -> str:
    members_html = "\n".join(render_member(m) for m in TEAM)
    affil_legend = "  &nbsp;&nbsp;·&nbsp;&nbsp; ".join(
        f"<sup>{k}</sup>{v}" for k, v in AFFILIATIONS.items()
    )

    main_html = f"""  <main>
    <p class="section-label">Contacts</p>
    <div class="team">
{members_html}
    </div>
    <p class="affil-legend">{affil_legend}</p>
  </main>"""

    return page_shell(
        "CarryBot — Contacts",
        "Project team and contact details for CarryBot, presented at MMAR 2026.",
        main_html,
    )


def render_about_page(m: dict) -> str:
    main_html = f"""  <main class="about">
    <a class="back-link" href="contact.html">&larr; Back to Contacts</a>
    <p class="section-label">About</p>
    <div class="bio-list">
{render_bio_card(m)}
    </div>
  </main>"""

    return page_shell(
        f"CarryBot — {m['name']}",
        f"Biography and contact details for {m['name']}, CarryBot project team.",
        main_html,
    )


def write_contact_html():
    (HERE / "contact.html").write_text(render_html(), encoding="utf-8")
    print("  wrote contact.html")


def write_about_pages():
    for m in TEAM:
        filename = about_page_filename(m)
        (HERE / filename).write_text(render_about_page(m), encoding="utf-8")
        print(f"  wrote {filename}")


def make_qr(data, filename):
    img = qrcode.make(data, error_correction=qrcode.constants.ERROR_CORRECT_M)
    img.save(HERE / filename)
    print(f"  wrote {filename}  ->  {data}")


def main():
    (HERE / "photos").mkdir(exist_ok=True)

    print("Generating contact page...")
    write_contact_html()
    write_about_pages()

    print("Generating QR codes...")
    make_qr(DEMO_VIDEO_URL, "demo_qr.png")
    make_qr(CONTACT_PAGE_URL, "contact_qr.png")


if __name__ == "__main__":
    main()