"""
generate_site.py
Run this script to (re)generate your GitHub Pages website files.
Usage: python generate_site.py
"""

import os

OUTPUT_DIR = "."  # Files are written to the current directory

# ── Configuration — edit these ──────────────────────────────────────────────
NAME = "Dhruvil Patel"
LINKEDIN_URL = "https://www.linkedin.com/in/dhruvilptl07"
# ────────────────────────────────────────────────────────────────────────────

INDEX_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{NAME}</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      font-family: 'DM Sans', sans-serif;
      background: #a8c4a3;
      color: #1a2e18;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 80px 24px 60px;
    }}

    header {{ text-align: center; margin-bottom: 72px; }}

    h1 {{
      font-family: 'Playfair Display', serif;
      font-size: clamp(3rem, 8vw, 6.5rem);
      font-weight: 700;
      letter-spacing: -1px;
      color: #1a2e18;
      line-height: 1.05;
    }}

    h1 span {{
      display: block;
      width: 60px;
      height: 3px;
      background: #c9a84c;
      margin: 20px auto 0;
      border-radius: 2px;
    }}

    .card-grid {{
      display: grid;
      grid-template-columns: 1fr;
      width: 100%;
      max-width: 480px;
    }}

    .card {{
      display: block;
      text-decoration: none;
      background: #b5ceb1;
      border: 0.5px solid #8fb08a;
      padding: 36px 40px;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      border-radius: 12px;
      transition: background 0.25s ease, border-color 0.25s ease;
    }}

    .card::after {{
      content: '';
      position: absolute;
      left: 0; top: 0;
      width: 3px; height: 100%;
      background: #c9a84c;
      transform: scaleY(0);
      transform-origin: bottom;
      transition: transform 0.25s ease;
    }}

    .card:hover {{ background: #bdd3b9; border-color: #7aa375; }}
    .card:hover::after {{ transform: scaleY(1); }}

    .card-label {{
      font-size: 11px;
      font-weight: 500;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      color: #c9a84c;
      margin-bottom: 8px;
    }}

    .card-title {{
      font-family: 'Playfair Display', serif;
      font-size: 1.5rem;
      color: #1a2e18;
      font-weight: 700;
    }}

    .card-arrow {{
      position: absolute;
      right: 40px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 20px;
      color: #7a9975;
      transition: color 0.25s, right 0.2s;
    }}
    .card:hover .card-arrow {{ color: #c9a84c; right: 32px; }}

    .linkedin-btn {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin-top: 52px;
      text-decoration: none;
      background: transparent;
      border: 1px solid #8fb08a;
      color: #1a2e18;
      font-family: 'DM Sans', sans-serif;
      font-size: 14px;
      font-weight: 500;
      letter-spacing: 0.5px;
      padding: 14px 28px;
      border-radius: 8px;
      cursor: pointer;
      transition: background 0.2s, border-color 0.2s, color 0.2s;
    }}

    .linkedin-btn svg {{
      width: 18px; height: 18px;
      fill: #0a66c2;
      flex-shrink: 0;
      transition: transform 0.2s;
    }}

    .linkedin-btn:hover {{
      background: #bdd3b9;
      border-color: #0a66c2;
      color: #1a2e18;
    }}
    .linkedin-btn:hover svg {{ transform: scale(1.1); }}
  </style>
</head>
<body>

  <header>
    <h1>{NAME}<span></span></h1>
  </header>

  <div class="card-grid">
    <a class="card" href="page.html">
      <div class="card-label">01</div>
      <div class="card-title">Explore</div>
      <span class="card-arrow">&#8594;</span>
    </a>
  </div>

  <a class="linkedin-btn" href="{LINKEDIN_URL}" target="_blank" rel="noopener noreferrer">
    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
      <path d="M20.447 20.452H17.21v-5.569c0-1.327-.024-3.037-1.852-3.037-1.854 0-2.137 1.446-2.137 2.941v5.665H9.985V9h3.107v1.561h.044c.433-.82 1.49-1.684 3.066-1.684 3.278 0 3.883 2.157 3.883 4.963l-.001 6.612zM5.337 7.433a1.806 1.806 0 1 1 0-3.612 1.806 1.806 0 0 1 0 3.612zm1.554 13.019H3.782V9h3.109v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.226.792 24 1.771 24h20.451C23.205 24 24 23.226 24 22.271V1.729C24 .774 23.205 0 22.225 0z"/>
    </svg>
    Connect on LinkedIn
  </a>

</body>
</html>
"""

PAGE_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Page — {NAME}</title>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>
  <style>
    body {{
      font-family: 'DM Sans', sans-serif;
      background: #a8c4a3;
      color: #1a2e18;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 24px;
    }}
    a {{
      color: #c9a84c;
      text-decoration: none;
      font-size: 14px;
      letter-spacing: 0.5px;
    }}
    a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <p style="color:#444; font-size:13px; letter-spacing:2px; text-transform:uppercase;">Coming soon</p>
  <a href="index.html">&larr; Back home</a>
</body>
</html>
"""


def write_file(filename, content):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ {filename}")


if __name__ == "__main__":
    print("Generating website files...")
    write_file("index.html", INDEX_HTML)
    write_file("page.html", PAGE_HTML)
    print("\nDone! Push these files to your GitHub repo and enable GitHub Pages.")
    print("Don't forget to replace YOUR-LINKEDIN-USERNAME in the LINKEDIN_URL variable.")
