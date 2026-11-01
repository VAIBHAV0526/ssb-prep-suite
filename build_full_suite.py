import json, os

out_dir = r'C:\Users\Singh\.gemini\antigravity\scratch\ssb-wat-simulator'

# Load WAT
with open(os.path.join(out_dir, 'wat_sets.json'), 'r', encoding='utf-8') as f:
    wat_sets_data = json.load(f)

wat_sets = []
all_wat_words = []
for idx, s in enumerate(wat_sets_data):
    words = [item['word'].upper() for item in s]
    wat_sets.append({
        'id': idx + 1,
        'title': f'Set {idx + 1}',
        'count': len(words),
        'preview': f"{words[0]} ... {words[-1]}",
        'words': words
    })
    all_wat_words.extend(words)

# Load SRT
with open(os.path.join(out_dir, 'srt_data.json'), 'r', encoding='utf-8') as f:
    srt_sets = json.load(f)

# Build TAT Sets from 137 images
total_tat_images = 137
tat_sets = []
pics_per_set = 11
num_full_sets = total_tat_images // pics_per_set

for s_idx in range(num_full_sets):
    start = s_idx * pics_per_set + 1
    end = start + pics_per_set - 1
    slides = []
    for img_idx in range(start, end + 1):
        slides.append({
            'num': len(slides) + 1,
            'type': 'image',
            'src': f'tat_images/tat_{img_idx:03d}.jpg',
            'label': f'Picture {len(slides) + 1}'
        })
    slides.append({
        'num': 12,
        'type': 'blank',
        'src': '',
        'label': 'Slide 12 — BLANK SLIDE (Own Story)'
    })
    tat_sets.append({
        'id': s_idx + 1,
        'title': f'TAT Set {s_idx + 1}',
        'desc': f'11 Pictures (tat_{start:03d} to tat_{end:03d}) + 1 Blank Slide',
        'slides': slides
    })

wat_sets_json = json.dumps(wat_sets)
all_wat_words_json = json.dumps(all_wat_words)
srt_sets_json = json.dumps(srt_sets)
tat_sets_json = json.dumps(tat_sets)

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SSB Master Suite — Complete DIPR Psychology & OIR Testing Platform</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <script src="jszip.min.js"></script>
  <script>
    if (typeof JSZip === 'undefined') {{
      const s = document.createElement('script');
      s.src = 'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js';
      document.head.appendChild(s);
    }}
  </script>
  <style>
    :root {{
      --bg-primary: #0a0f1d;
      --bg-card: #111a2e;
      --bg-card-border: #1e293b;
      --accent-gold: #f59e0b;
      --accent-gold-glow: rgba(245, 158, 11, 0.25);
      --accent-blue: #38bdf8;
      --accent-green: #10b981;
      --accent-red: #ef4444;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --font-display: 'Cinzel', serif;
      --font-body: 'Inter', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    body.dipr-projector {{
      --bg-primary: #f1f5f9;
      --bg-card: #ffffff;
      --bg-card-border: #cbd5e1;
      --accent-gold: #b45309;
      --accent-gold-glow: rgba(180, 83, 9, 0.15);
      --accent-blue: #0284c7;
      --accent-green: #059669;
      --accent-red: #dc2626;
      --text-main: #0f172a;
      --text-muted: #64748b;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background-color: var(--bg-primary);
      color: var(--text-main);
      font-family: var(--font-body);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      transition: background-color 0.3s ease, color 0.3s ease;
    }}

    header {{
      background: var(--bg-card);
      border-bottom: 1px solid var(--bg-card-border);
      padding: 0.75rem 1.5rem;
      position: sticky;
      top: 0;
      z-index: 50;
      backdrop-filter: blur(8px);
    }}

    .header-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      max-width: 1400px;
      margin: 0 auto;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .brand-badge {{
      background: linear-gradient(135deg, var(--accent-gold), #d97706);
      color: #000;
      font-weight: 800;
      font-size: 0.75rem;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      letter-spacing: 1px;
    }}

    .brand h1 {{
      font-family: var(--font-display);
      font-size: 1.25rem;
      letter-spacing: 1.5px;
      font-weight: 800;
      background: linear-gradient(to right, #f8fafc, #94a3b8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    body.dipr-projector .brand h1 {{
      background: linear-gradient(to right, #0f172a, #334155);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .sub-nav {{
      display: flex;
      gap: 0.5rem;
      overflow-x: auto;
      padding: 0.6rem 0 0.2rem;
      max-width: 1400px;
      margin: 0 auto;
      scrollbar-width: thin;
    }}

    .nav-tab {{
      background: transparent;
      border: 1px solid transparent;
      color: var(--text-muted);
      padding: 0.45rem 0.9rem;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .nav-tab:hover {{
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.05);
    }}

    .nav-tab.active {{
      background: rgba(245, 158, 11, 0.12);
      border-color: var(--accent-gold);
      color: var(--accent-gold);
    }}

    main {{
      flex: 1;
      max-width: 1400px;
      width: 100%;
      margin: 0 auto;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
    }}

    .module-container {{
      display: none;
      width: 100%;
      animation: fadeIn 0.25s ease-out;
    }}

    .module-container.active {{
      display: block;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .card-box {{
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 12px;
      padding: 1.75rem;
      margin: 0 auto;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
    }}

    .section-title {{
      font-family: var(--font-display);
      font-size: 1.6rem;
      margin-bottom: 0.5rem;
      color: var(--accent-gold);
      text-align: center;
    }}

    .section-subtitle {{
      color: var(--text-muted);
      font-size: 0.95rem;
      text-align: center;
      margin-bottom: 1.75rem;
      line-height: 1.5;
    }}

    .form-group {{
      margin-bottom: 1.25rem;
    }}

    .form-group label {{
      display: block;
      font-size: 0.85rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 0.4rem;
      color: var(--text-muted);
    }}

    select, input[type="text"], input[type="number"], textarea {{
      width: 100%;
      background: var(--bg-primary);
      border: 1px solid var(--bg-card-border);
      border-radius: 6px;
      padding: 0.65rem 0.9rem;
      color: var(--text-main);
      font-family: var(--font-body);
      font-size: 0.95rem;
      outline: none;
      transition: border-color 0.2s;
    }}

    select:focus, input[type="text"]:focus, input[type="number"]:focus, textarea:focus {{
      border-color: var(--accent-gold);
    }}

    .grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
    }}

    @media (max-width: 768px) {{
      .grid-2 {{
        grid-template-columns: 1fr;
      }}
    }}

    .btn-start {{
      background: linear-gradient(135deg, var(--accent-gold), #d97706);
      color: #000;
      border: none;
      padding: 0.85rem 1.75rem;
      border-radius: 6px;
      font-size: 1rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      cursor: pointer;
      width: 100%;
      margin-top: 1rem;
      transition: all 0.2s ease;
      box-shadow: 0 4px 14px var(--accent-gold-glow);
    }}

    .btn-start:hover {{
      transform: translateY(-1px);
      box-shadow: 0 6px 20px rgba(245, 158, 11, 0.35);
    }}

    .btn-secondary {{
      background: transparent;
      border: 1px solid var(--bg-card-border);
      color: var(--text-main);
      padding: 0.5rem 1rem;
      border-radius: 6px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .btn-secondary:hover {{
      border-color: var(--accent-gold);
      color: var(--accent-gold);
    }}

    .mode-selector {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.75rem;
      margin-bottom: 1.25rem;
    }}

    .mode-option {{
      border: 1px solid var(--bg-card-border);
      border-radius: 8px;
      padding: 0.75rem 1rem;
      cursor: pointer;
      transition: all 0.2s;
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }}

    .mode-option.active {{
      border-color: var(--accent-gold);
      background: rgba(245, 158, 11, 0.08);
    }}

    .mode-option strong {{
      font-size: 0.95rem;
    }}

    .mode-option span {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}

    .timer-ring-container {{
      position: relative;
      width: 80px;
      height: 80px;
    }}

    .timer-ring-svg {{
      width: 100%;
      height: 100%;
      transform: rotate(-90deg);
    }}

    .timer-ring-bg {{
      fill: none;
      stroke: var(--bg-card-border);
      stroke-width: 6;
    }}

    .timer-ring-progress {{
      fill: none;
      stroke: var(--accent-gold);
      stroke-width: 6;
      stroke-linecap: round;
      stroke-dasharray: 226;
      stroke-dashoffset: 0;
      transition: stroke-dashoffset 0.1s linear;
    }}

    .timer-number {{
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      font-family: var(--font-mono);
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--text-main);
    }}

    .info-banner {{
      background: rgba(56, 189, 248, 0.08);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 8px;
      padding: 0.75rem 1rem;
      margin-bottom: 1.5rem;
      font-size: 0.85rem;
      color: var(--accent-blue);
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.5rem;
    }}

    /* AI Evaluation Cards & Buttons */
    .ai-eval-card {{
      background: rgba(56, 189, 248, 0.05);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 12px;
      padding: 1.25rem;
      margin-bottom: 1.5rem;
    }}

    .ai-model-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.45rem 0.85rem;
      border-radius: 6px;
      border: 1px solid;
      font-size: 0.82rem;
      font-weight: 600;
      text-decoration: none;
      transition: transform 0.15s, opacity 0.15s;
    }}

    .ai-model-btn:hover {{
      transform: translateY(-1px);
      opacity: 0.9;
    }}

    /* TAT Elements */
    .tat-display-card {{
      background: var(--bg-primary);
      border: 2px solid var(--bg-card-border);
      border-radius: 16px;
      min-height: 480px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 100%;
      position: relative;
      overflow: hidden;
      padding: 1.5rem;
    }}

    .tat-image-container {{
      max-width: 100%;
      max-height: 440px;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: hidden;
      border-radius: 8px;
    }}

    .tat-image-container img {{
      max-width: 100%;
      max-height: 440px;
      object-fit: contain;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
    }}

    .tat-phase-badge {{
      display: inline-block;
      padding: 0.25rem 0.75rem;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}

    .phase-viewing {{
      background: rgba(56, 189, 248, 0.15);
      color: var(--accent-blue);
      border: 1px solid var(--accent-blue);
    }}

    .phase-writing {{
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-green);
      border: 1px solid var(--accent-green);
    }}

    /* SRT */
    .srt-booklet {{
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      max-height: calc(100vh - 280px);
      overflow-y: auto;
      padding-right: 0.5rem;
    }}

    .srt-item {{
      background: var(--bg-primary);
      border: 1px solid var(--bg-card-border);
      border-radius: 8px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      transition: border-color 0.2s;
    }}
    .srt-item:focus-within {{
      border-color: var(--accent-gold);
    }}

    .srt-prompt {{
      font-size: 1.05rem;
      font-weight: 600;
      line-height: 1.5;
    }}

    .srt-input {{
      width: 100%;
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      color: var(--text-main);
      padding: 0.75rem 1rem;
      border-radius: 6px;
      font-size: 0.95rem;
      outline: none;
    }}

    /* SDT */
    .sdt-editor-box {{
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      width: 100%;
    }}

    .sdt-card {{
      background: var(--bg-primary);
      border: 1px solid var(--bg-card-border);
      border-radius: 8px;
      padding: 1.5rem;
    }}

    .sdt-label {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--accent-gold);
      margin-bottom: 0.25rem;
    }}

    .sdt-help {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 0.75rem;
    }}

    .sdt-textarea {{
      width: 100%;
      height: 120px;
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      color: var(--text-main);
      padding: 0.75rem 1rem;
      border-radius: 6px;
      font-size: 0.95rem;
      font-family: var(--font-body);
      outline: none;
      resize: vertical;
    }}

    /* OIR */
    .oir-workspace {{
      display: grid;
      grid-template-columns: 1.4fr 1fr;
      gap: 1.5rem;
      width: 100%;
      height: calc(100vh - 160px);
    }}

    .oir-pdf-viewer {{
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 12px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      height: 100%;
    }}

    .oir-omr-pane {{
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 12px;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      height: 100%;
      overflow: hidden;
    }}

    .omr-grid-container {{
      flex: 1;
      overflow-y: auto;
      padding-right: 0.5rem;
      margin-top: 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }}

    .omr-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.45rem 0.75rem;
      border-radius: 6px;
      background: var(--bg-primary);
      border: 1px solid var(--bg-card-border);
    }}

    .omr-q-num {{
      font-family: var(--font-mono);
      font-weight: 700;
      font-size: 0.85rem;
      width: 32px;
      color: var(--text-muted);
    }}

    .omr-options {{
      display: flex;
      gap: 0.5rem;
    }}

    .omr-bubble {{
      width: 30px;
      height: 30px;
      border-radius: 50%;
      border: 1px solid var(--bg-card-border);
      background: var(--bg-card);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-mono);
      font-weight: 700;
      font-size: 0.8rem;
      cursor: pointer;
      transition: all 0.15s ease;
      user-select: none;
    }}

    .omr-bubble:hover {{
      border-color: var(--accent-gold);
    }}

    .omr-bubble.selected {{
      background: var(--accent-gold);
      color: #000;
      border-color: var(--accent-gold);
      box-shadow: 0 0 10px var(--accent-gold-glow);
    }}

    /* Performance Progress Tracker Styles */
    .stat-cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1rem;
      margin-bottom: 2rem;
    }}
    .stat-card {{
      background: var(--bg-primary);
      border: 1px solid var(--bg-card-border);
      border-radius: 8px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }}
    .stat-title {{
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-muted);
      font-weight: 600;
    }}
    .stat-value {{
      font-family: var(--font-mono);
      font-size: 1.6rem;
      font-weight: 700;
      color: var(--accent-gold);
    }}
    .stat-bar-bg {{
      width: 100%;
      height: 6px;
      background: var(--bg-card);
      border-radius: 3px;
      overflow: hidden;
    }}
    .stat-bar-fill {{
      height: 100%;
      background: var(--accent-gold);
      border-radius: 3px;
      transition: width 0.3s ease;
    }}
    .set-pills-wrap {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-top: 0.5rem;
    }}
    .set-pill {{
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      border: 1px solid var(--bg-card-border);
      background: var(--bg-card);
      font-size: 0.8rem;
      font-family: var(--font-mono);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.15s ease;
    }}
    .set-pill:hover {{
      border-color: var(--accent-gold);
      color: var(--text-main);
    }}
    .set-pill.completed {{
      border-color: var(--accent-green);
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-green);
    }}

    /* Toast Notification */
    #toastNotice {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--accent-gold);
      color: #000;
      padding: 0.75rem 1.25rem;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.9rem;
      box-shadow: 0 4px 16px rgba(0,0,0,0.4);
      z-index: 9999;
      opacity: 0;
      transform: translateY(10px);
      transition: opacity 0.2s, transform 0.2s;
      pointer-events: none;
    }}
    #toastNotice.visible {{
      opacity: 1;
      transform: translateY(0);
    }}
  </style>
</head>
<body>

  <!-- TOAST NOTIFICATION -->
  <div id="toastNotice">Copied to Clipboard!</div>

  <!-- GLOBAL HEADER -->
  <header>
    <div class="header-top">
      <div class="brand">
        <span class="brand-badge">DIPR</span>
        <h1>SSB MASTER SUITE</h1>
      </div>
      <div class="header-actions">
        <button class="btn-secondary" id="btnToggleTheme">
          <span id="themeIcon">☀️</span> <span id="themeLabel">Projector Mode</span>
        </button>
        <button class="btn-secondary" id="btnToggleFullscreen">
          ⛶ <span>Fullscreen</span>
        </button>
      </div>
    </div>

    <!-- SUB NAVIGATION / TEST SELECTOR -->
    <nav class="sub-nav">
      <button class="nav-tab active" data-tab="tab-progress" style="color: var(--accent-gold); border-color: rgba(245, 158, 11, 0.4);">
        📈 My Progress & Mastery
      </button>
      <button class="nav-tab" data-tab="tab-wat">⚡ WAT (60 Words)</button>
      <button class="nav-tab" data-tab="tab-tat">🖼️ TAT (12 Pictures)</button>
      <button class="nav-tab" data-tab="tab-srt">📝 SRT (60 Situations)</button>
      <button class="nav-tab" data-tab="tab-sdt">👤 SDT (Self Description)</button>
      <button class="nav-tab" data-tab="tab-oir">📊 OIR (PDF + OMR)</button>
      <button class="nav-tab" data-tab="tab-fullmock">🎯 Full Mock Battery</button>
      <button class="nav-tab" data-tab="tab-ai-assessor" style="border-color: rgba(56, 189, 248, 0.4); color: var(--accent-blue);">
        🤖 AI Assessor (Free Evaluation)
      </button>
    </nav>
  </header>

  <!-- MAIN VIEWPORT -->
  <main>

    <!-- ==============================================================
         0. PROGRESS & PERFORMANCE TRACKER (DO NOT REPEAT ENGINE)
         ============================================================== -->
    <section class="module-container active" id="tab-progress">
      <div class="card-box" style="max-width: 1040px;">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--bg-card-border); padding-bottom: 1rem; margin-bottom: 1.5rem;">
          <div>
            <h2 class="section-title" style="text-align: left; margin: 0;">Performance & Preparation Tracker</h2>
            <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 0.25rem;">
              Track completed sets, avoid unintentional repeats, and finish your target before your SSB reporting date.
            </p>
          </div>
          <div style="display: flex; gap: 0.5rem;">
            <button class="btn-secondary" onclick="exportProgressJSON()">📥 Backup Progress</button>
            <input type="file" id="importProgressInput" accept=".json" style="display: none;">
            <button class="btn-secondary" onclick="document.getElementById('importProgressInput').click()">📤 Restore Progress</button>
          </div>
        </div>

        <!-- STATS OVERVIEW -->
        <div class="stat-cards-grid">
          <div class="stat-card">
            <span class="stat-title">WAT Mastery (21 Sets)</span>
            <span class="stat-value" id="progWatVal">0 / 21</span>
            <div class="stat-bar-bg"><div class="stat-bar-fill" id="progWatBar" style="width: 0%;"></div></div>
          </div>
          <div class="stat-card">
            <span class="stat-title">TAT Mastery (12 Sets)</span>
            <span class="stat-value" id="progTatVal">0 / 12</span>
            <div class="stat-bar-bg"><div class="stat-bar-fill" id="progTatBar" style="width: 0%; background: var(--accent-blue);"></div></div>
          </div>
          <div class="stat-card">
            <span class="stat-title">SRT Mastery (2 Sets)</span>
            <span class="stat-value" id="progSrtVal">0 / 2</span>
            <div class="stat-bar-bg"><div class="stat-bar-fill" id="progSrtBar" style="width: 0%; background: var(--accent-green);"></div></div>
          </div>
          <div class="stat-card">
            <span class="stat-title">Total Sessions Logged</span>
            <span class="stat-value" id="progTotalSessions">0</span>
            <span style="font-size: 0.75rem; color: var(--text-muted);">Practiced without repeats</span>
          </div>
        </div>

        <!-- SMART NEXT UNATTEMPTED RECOMMENDATION -->
        <div style="background: rgba(245, 158, 11, 0.1); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 8px; padding: 1.25rem; margin-bottom: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
          <div>
            <strong style="color: var(--accent-gold); font-size: 1.05rem;">🎯 Next Recommended Unattempted Drill:</strong>
            <div style="color: var(--text-main); font-size: 0.95rem; margin-top: 0.25rem;" id="nextRecText">
              Loading recommendations...
            </div>
          </div>
          <button class="btn-start" style="width: auto; padding: 0.65rem 1.75rem; font-size: 0.9rem;" id="btnLaunchNextRec">
            Launch Next Set ❯
          </button>
        </div>

        <!-- SET COMPLETION BREAKDOWN -->
        <div style="display: flex; flex-direction: column; gap: 1.75rem;">
          
          <div>
            <strong style="color: var(--accent-gold); font-size: 1rem;">⚡ Word Association Test Sets (WAT 1 to 21)</strong>
            <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.15rem;">Click any set to launch or view status:</p>
            <div class="set-pills-wrap" id="pillsWat"></div>
          </div>

          <div>
            <strong style="color: var(--accent-blue); font-size: 1rem;">🖼️ Thematic Apperception Test Sets (TAT 1 to 12)</strong>
            <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.15rem;">11 Pictures + 1 Blank Slide each:</p>
            <div class="set-pills-wrap" id="pillsTat"></div>
          </div>

          <div>
            <strong style="color: var(--accent-green); font-size: 1rem;">📝 Situation Reaction Test Sets (SRT 1 and 2)</strong>
            <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.15rem;">60 Situations each in 30 minutes:</p>
            <div class="set-pills-wrap" id="pillsSrt"></div>
          </div>

        </div>

        <!-- RECENT ACTIVITY LOG -->
        <div style="margin-top: 2.5rem; border-top: 1px solid var(--bg-card-border); padding-top: 1.5rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <strong style="font-size: 1.05rem;">📜 Practice History & Log</strong>
            <button class="btn-secondary" style="font-size: 0.8rem; padding: 0.3rem 0.6rem; color: var(--accent-red);" onclick="clearPracticeHistory()">Clear History</button>
          </div>
          <div style="max-height: 280px; overflow-y: auto; border: 1px solid var(--bg-card-border); border-radius: 8px;">
            <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.85rem;">
              <thead>
                <tr style="background: var(--bg-primary); color: var(--accent-gold); text-transform: uppercase;">
                  <th style="padding: 0.6rem 1rem;">Timestamp</th>
                  <th style="padding: 0.6rem 1rem;">Module</th>
                  <th style="padding: 0.6rem 1rem;">Set / Item</th>
                  <th style="padding: 0.6rem 1rem;">Result</th>
                </tr>
              </thead>
              <tbody id="historyTableBody"></tbody>
            </table>
          </div>
        </div>

      </div>
    </section>

    <!-- ==============================================================
         1. WAT MODULE
         ============================================================== -->
    <section class="module-container" id="tab-wat">
      
      <!-- WAT SETUP -->
      <div class="card-box" id="watSetupScreen">
        <h2 class="section-title">Word Association Test (WAT)</h2>
        <p class="section-subtitle">
          60 Words flashed for 15 seconds each. Instant spontaneous positive thought without preaching or clichés.
        </p>

        <div class="info-banner">
          <div>📄 Loaded: <strong>21 Sets ({len(all_wat_words)} Words)</strong></div>
          <div>Interval: <strong>15 Seconds / Word</strong></div>
        </div>

        <div class="form-group">
          <label>Select Practice Set</label>
          <select id="watSelectSet">
            <option value="next_unattempted" selected>🎯 Next Unattempted Set (Recommended - No Repeat)</option>
            <option value="random_60">🎲 Random 60 Words (Simulate Full Board Test)</option>
            <option value="random_30">⚡ Quick Practice (30 Random Words)</option>
            <optgroup label="── OFFICIAL DIPR SETS (60 Words Each) ──" id="watOptGroupSets">
'''

for s in wat_sets:
    html += f'              <option value="set_{s["id"]}">Set {s["id"]} ({s["count"]} Words: {s["preview"]})</option>\n'

html += f'''            </optgroup>
            <optgroup label="── OTHER ──">
              <option value="all">🔥 Marathon (All {len(all_wat_words)} Words)</option>
            </optgroup>
          </select>
        </div>

        <div class="grid-2">
          <div class="form-group">
            <label>Timing Pace</label>
            <select id="watSelectDuration">
              <option value="15" selected>15 Seconds (Official DIPR Standard)</option>
              <option value="12">12 Seconds (Pressure Drill)</option>
              <option value="10">10 Seconds (Ultra Speed)</option>
              <option value="18">18 Seconds (Beginner Pace)</option>
            </select>
          </div>
          <div class="form-group">
            <label>Order</label>
            <select id="watSelectOrder">
              <option value="sequential" selected>Original Order</option>
              <option value="shuffle">Shuffled (Randomized)</option>
            </select>
          </div>
        </div>

        <div class="form-group">
          <label>Practice Mode</label>
          <div class="mode-selector">
            <div class="mode-option active" id="watModePaper" onclick="setWatMode('paper')">
              <strong>📝 Pen & Paper (Recommended)</strong>
              <span>Exact SSB exam condition. Write in your notebook as words flash.</span>
            </div>
            <div class="mode-option" id="watModeTyping" onclick="setWatMode('typing')">
              <strong>⌨️ Digital Typing</strong>
              <span>Type your spontaneous responses directly on screen.</span>
            </div>
          </div>
        </div>

        <button class="btn-start" onclick="startWatTest()">START WAT SESSION</button>
      </div>

      <!-- WAT ACTIVE TEST -->
      <div class="card-box" id="watActiveScreen" style="display: none; max-width: 900px; padding: 2rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: 2rem;">
          <div style="font-family: var(--font-mono); font-weight: 700; color: var(--accent-gold); font-size: 1.1rem;" id="watProgressTag">
            WORD 1 / 60
          </div>
          <div class="timer-ring-container">
            <svg class="timer-ring-svg" viewBox="0 0 80 80">
              <circle class="timer-ring-bg" cx="40" cy="40" r="36" />
              <circle class="timer-ring-progress" id="watTimerCircle" cx="40" cy="40" r="36" />
            </svg>
            <div class="timer-number" id="watTimerNum">15</div>
          </div>
        </div>

        <div style="background: var(--bg-primary); border: 2px solid var(--bg-card-border); border-radius: 16px; min-height: 240px; display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; position: relative; overflow: hidden; padding: 2rem;">
          <div style="font-size: clamp(2.8rem, 7vw, 5rem); font-weight: 800; letter-spacing: 3px; text-transform: uppercase;" id="watFlashedWord">
            LEADER
          </div>
          <div style="position: absolute; bottom: 0; left: 0; height: 6px; width: 100%; background: rgba(255,255,255,0.05);">
            <div style="height: 100%; width: 100%; background: linear-gradient(90deg, var(--accent-gold), #ef4444); transition: width 0.1s linear;" id="watLinearBar"></div>
          </div>
        </div>

        <div id="watTypingArea" style="width: 100%; margin-top: 1.5rem; display: none;">
          <input type="text" id="watInput" style="width: 100%; padding: 1rem; border-radius: 8px; font-size: 1.1rem; background: var(--bg-primary); border: 1px solid var(--bg-card-border); color: var(--text-main);" placeholder="Write your spontaneous association here..." autocomplete="off">
        </div>

        <div style="display: flex; gap: 1rem; margin-top: 2rem; justify-content: center;">
          <button class="btn-secondary" onclick="toggleWatPause()"><span id="watPauseIcon">⏸</span> <span id="watPauseLabel">Pause</span></button>
          <button class="btn-secondary" onclick="nextWatWord()">Next Word ❯</button>
          <button class="btn-secondary" style="color: var(--accent-red);" onclick="abortWatTest()">✕ End Test</button>
        </div>
      </div>

      <!-- WAT REVIEW -->
      <div class="card-box" id="watReviewScreen" style="display: none; max-width: 940px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <h2>WAT Test Completed!</h2>
            <p style="color: var(--text-muted); font-size: 0.9rem;">Review your words and evaluate with AI for free.</p>
          </div>
          <div style="display: flex; gap: 0.5rem;">
            <button class="btn-secondary" onclick="copyWatResponses()">📋 Raw Words List</button>
          </div>
        </div>

        <!-- AI EVALUATION CARD -->
        <div class="ai-eval-card">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; flex-wrap: wrap;">
            <div>
              <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="font-size: 1.3rem;">🤖</span>
                <strong style="color: var(--accent-blue); font-size: 1.1rem;">Free AI Psychologist Evaluation (ChatGPT / Claude / Gemini)</strong>
              </div>
              <p style="color: var(--text-muted); font-size: 0.85rem; margin-top: 0.35rem; max-width: 620px; line-height: 1.45;">
                Get your 60 words and sentences graded by an AI trained as a <strong>Senior DIPR Psychologist</strong>. It checks against the 15 OLQs, flags preaching ("should/must") or passive pessimism, and gives officer-grade rewrites.
              </p>
            </div>
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
              <button class="btn-start" style="width: auto; padding: 0.6rem 1.25rem; font-size: 0.85rem; background: var(--accent-blue); color: #000;" onclick="copyWatAiPrompt()">📋 Copy AI Assessor Prompt</button>
              <button class="btn-secondary" style="font-size: 0.85rem; padding: 0.6rem 1rem;" onclick="downloadWatAiDossier()">📥 Download Dossier (.txt)</button>
            </div>
          </div>
          <div style="margin-top: 1rem; padding-top: 0.75rem; border-top: 1px solid var(--bg-card-border); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--text-muted);">Step 2: Paste into your favorite free AI chat:</span>
            <div style="display: flex; gap: 0.5rem;">
              <a href="https://chatgpt.com" target="_blank" class="ai-model-btn" style="background: rgba(16, 185, 129, 0.15); border-color: var(--accent-green); color: var(--accent-green);">🚀 ChatGPT (Free) ↗</a>
              <a href="https://claude.ai" target="_blank" class="ai-model-btn" style="background: rgba(217, 119, 6, 0.15); border-color: #d97706; color: #fbbf24;">🟣 Claude (Free) ↗</a>
              <a href="https://gemini.google.com" target="_blank" class="ai-model-btn" style="background: rgba(56, 189, 248, 0.15); border-color: var(--accent-blue); color: var(--accent-blue);">✨ Google Gemini (Free) ↗</a>
            </div>
          </div>
        </div>

        <div style="max-height: 480px; overflow-y: auto; border: 1px solid var(--bg-card-border); border-radius: 8px; margin-bottom: 1.5rem;">
          <table style="width: 100%; border-collapse: collapse; text-align: left;">
            <thead>
              <tr style="background: var(--bg-primary); color: var(--accent-gold); font-size: 0.85rem; text-transform: uppercase;">
                <th style="padding: 0.75rem 1rem;">#</th>
                <th style="padding: 0.75rem 1rem;">Word</th>
                <th style="padding: 0.75rem 1rem;">Response</th>
              </tr>
            </thead>
            <tbody id="watReviewTbody"></tbody>
          </table>
        </div>
        <button class="btn-secondary" onclick="resetWatToSetup()">← Return to Setup</button>
      </div>

    </section>

    <!-- ==============================================================
         2. TAT MODULE
         ============================================================== -->
    <section class="module-container" id="tab-tat">
      
      <!-- TAT SETUP -->
      <div class="card-box" id="tatSetupScreen">
        <h2 class="section-title">Thematic Apperception Test (TAT)</h2>
        <p class="section-subtitle">
          12 Slides (11 authentic picture slides + 1 Blank Slide). 30 seconds observation followed by 4 minutes story writing per slide.
        </p>

        <div class="info-banner">
          <div>📸 Source: <strong>All Tat Combined .pdf (137 Pictures)</strong></div>
          <div>Sets: <strong>12 Official Sets (12 Slides Each)</strong></div>
        </div>

        <div class="form-group">
          <label>Select TAT Set</label>
          <select id="tatSelectSet">
            <option value="next_unattempted" selected>🎯 Next Unattempted TAT Set (No Repeat)</option>
            <option value="random_11">🎲 Random 11 Pictures + Slide 12 Blank</option>
            <optgroup label="── OFFICIAL 12-SLIDE SETS ──" id="tatOptGroupSets">
'''

for s in tat_sets:
    html += f'              <option value="tat_set_{s["id"]}">{s["title"]} ({s["desc"]})</option>\n'

html += f'''            </optgroup>
          </select>
        </div>

        <div class="grid-2">
          <div class="form-group">
            <label>Viewing Phase (Picture on Screen)</label>
            <select id="tatViewTime">
              <option value="30" selected>30 Seconds (Official DIPR Standard)</option>
              <option value="20">20 Seconds (Fast Observation)</option>
              <option value="45">45 Seconds (Relaxed / Training)</option>
            </select>
          </div>
          <div class="form-group">
            <label>Writing Phase (Screen Blank / Narrative)</label>
            <select id="tatWriteTime">
              <option value="240" selected>4 Minutes (Official DIPR Standard)</option>
              <option value="180">3 Minutes (High Speed)</option>
              <option value="300">5 Minutes (Beginner)</option>
            </select>
          </div>
        </div>

        <div class="form-group">
          <label>Practice Mode</label>
          <div class="mode-selector">
            <div class="mode-option active" id="tatModePaper" onclick="setTatMode('paper')">
              <strong>📝 Pen & Paper (Recommended)</strong>
              <span>Observe picture on screen, then write your story in your SSB booklet.</span>
            </div>
            <div class="mode-option" id="tatModeTyping" onclick="setTatMode('typing')">
              <strong>⌨️ Digital Typing</strong>
              <span>Type your story directly with Hero, Action & Outcome boxes.</span>
            </div>
          </div>
        </div>

        <button class="btn-start" onclick="startTatTest()">START TAT SESSION</button>
      </div>

      <!-- TAT ACTIVE TEST -->
      <div class="card-box" id="tatActiveScreen" style="display: none; max-width: 960px; padding: 2rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: 1.5rem;">
          <div>
            <div style="font-family: var(--font-mono); font-weight: 700; color: var(--accent-gold); font-size: 1.15rem;" id="tatSlideTag">
              SLIDE 1 / 12
            </div>
            <div style="margin-top: 0.25rem;">
              <span class="tat-phase-badge phase-viewing" id="tatPhaseBadge">👁️ OBSERVATION PHASE (30s)</span>
            </div>
          </div>

          <div class="timer-ring-container">
            <svg class="timer-ring-svg" viewBox="0 0 80 80">
              <circle class="timer-ring-bg" cx="40" cy="40" r="36" />
              <circle class="timer-ring-progress" id="tatTimerCircle" cx="40" cy="40" r="36" />
            </svg>
            <div class="timer-number" id="tatTimerNum">30</div>
          </div>
        </div>

        <!-- TAT DISPLAY CARD -->
        <div class="tat-display-card" id="tatDisplayCard">
          <div class="tat-image-container" id="tatImgWrap">
            <img id="tatCurrentImg" src="" alt="TAT Picture">
          </div>
          <div class="tat-blank-slide" id="tatBlankSlide" style="display: none; text-align: center;">
            <h2 style="font-size: 2.2rem; margin-bottom: 1rem; color: var(--accent-gold);">BLANK SLIDE (12 / 12)</h2>
            <p style="font-size: 1.1rem; max-width: 600px; line-height: 1.6; color: #cbd5e1;">
              This is the 12th Slide. Write a story of your own choice, drawing from personal achievements, social service, adventurous experience, or constructive goals.
            </p>
          </div>
          <div id="tatWritingPrompt" style="display: none; text-align: center; padding: 2rem;">
            <h3 style="font-size: 1.8rem; color: var(--accent-green); margin-bottom: 0.5rem;">✍️ WRITING PHASE</h3>
            <p style="color: var(--text-muted); font-size: 1.05rem;">
              Observe the past (what led to it), present (hero's planned action), and constructive future outcome.
            </p>
          </div>
        </div>

        <div id="tatTypingContainer" style="display: none; width: 100%; margin-top: 1.5rem;">
          <textarea id="tatStoryInput" style="width: 100%; height: 160px; background: var(--bg-primary); border: 1px solid var(--bg-card-border); color: var(--text-main); padding: 1rem; border-radius: 8px; font-family: var(--font-body); font-size: 0.95rem; resize: vertical;" placeholder="Type your story here (Hero, Situation, Action taken, Resolution)..."></textarea>
        </div>

        <div style="display: flex; gap: 1rem; margin-top: 1.5rem; justify-content: center;">
          <button class="btn-secondary" onclick="toggleTatPause()"><span id="tatPauseIcon">⏸</span> <span id="tatPauseLabel">Pause</span></button>
          <button class="btn-secondary" style="border-color: var(--accent-green); color: var(--accent-green);" onclick="advanceTatPhaseEarly()">
            Finished Writing ➔ Next Slide
          </button>
          <button class="btn-secondary" style="color: var(--accent-red);" onclick="abortTatTest()">✕ End Test</button>
        </div>
      </div>

      <!-- TAT REVIEW -->
      <div class="card-box" id="tatReviewScreen" style="display: none; max-width: 960px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <h2>TAT Session Completed!</h2>
            <p style="color: var(--text-muted); font-size: 0.9rem;">12 Slides completed successfully.</p>
          </div>
          <button class="btn-secondary" onclick="copyTatResponses()">📋 Raw Stories</button>
        </div>

        <!-- MULTIMODAL AI EVALUATION PACKAGE -->
        <div class="ai-eval-card" style="border-color: rgba(56, 189, 248, 0.4);">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; flex-wrap: wrap;">
            <div>
              <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="font-size: 1.3rem;">🖼️🤖</span>
                <strong style="color: var(--accent-blue); font-size: 1.1rem;">Free Multimodal TAT Evaluation (Images + Stories)</strong>
              </div>
              <p style="color: var(--text-muted); font-size: 0.85rem; margin-top: 0.35rem; max-width: 620px; line-height: 1.45;">
                Download the complete package containing all <strong>slide picture images (.jpg) + your stories + the Senior DIPR Assessor Prompt</strong>. Upload them directly into ChatGPT-4o, Claude 3.5, or Gemini to evaluate how well your Hero, Action, and Resolution match the visual stimulus and the 15 OLQs!
              </p>
            </div>
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
              <button class="btn-start" id="btnDownloadTatZip" style="width: auto; padding: 0.6rem 1.25rem; font-size: 0.85rem; background: var(--accent-gold); color: #000;" onclick="downloadTatZipPackage()">
                📦 Download Package (.ZIP: Images + Prompt)
              </button>
              <button class="btn-secondary" style="font-size: 0.85rem; padding: 0.6rem 1rem;" onclick="copyTatAiPrompt()">
                📋 Copy Prompt & Stories
              </button>
              <button class="btn-secondary" style="font-size: 0.85rem; padding: 0.6rem 1rem;" onclick="downloadTatAiDossier()">
                📥 Download Text (.txt)
              </button>
            </div>
          </div>
          <div style="margin-top: 1rem; padding-top: 0.75rem; border-top: 1px solid var(--bg-card-border); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--text-muted);">Step 2: Upload images & prompt to free AI chat:</span>
            <div style="display: flex; gap: 0.5rem;">
              <a href="https://chatgpt.com" target="_blank" class="ai-model-btn" style="background: rgba(16, 185, 129, 0.15); border-color: var(--accent-green); color: var(--accent-green);">🚀 ChatGPT (Free) ↗</a>
              <a href="https://claude.ai" target="_blank" class="ai-model-btn" style="background: rgba(217, 119, 6, 0.15); border-color: #d97706; color: #fbbf24;">🟣 Claude (Free) ↗</a>
              <a href="https://gemini.google.com" target="_blank" class="ai-model-btn" style="background: rgba(56, 189, 248, 0.15); border-color: var(--accent-blue); color: var(--accent-blue);">✨ Google Gemini (Free) ↗</a>
            </div>
          </div>
        </div>

        <div id="tatReviewList" style="max-height: 520px; overflow-y: auto; display: flex; flex-direction: column; gap: 1rem; margin-bottom: 1.5rem;"></div>
        <button class="btn-secondary" onclick="resetTatToSetup()">← Return to Setup</button>
      </div>

    </section>

    <!-- ==============================================================
         3. SRT MODULE
         ============================================================== -->
    <section class="module-container" id="tab-srt">
      
      <!-- SRT SETUP -->
      <div class="card-box" id="srtSetupScreen">
        <h2 class="section-title">Situation Reaction Test (SRT)</h2>
        <p class="section-subtitle">
          60 Real-world challenging situations in 30 minutes. Demonstrates practical intelligence, speed of decision, and social responsibility.
        </p>

        <div class="info-banner">
          <div>📋 Bank: <strong>2 Official DIPR Sets (120 Situations)</strong></div>
          <div>Allotted Time: <strong>30 Minutes for 60 Situations</strong></div>
        </div>

        <div class="form-group">
          <label>Select SRT Set</label>
          <select id="srtSelectSet">
            <option value="next_unattempted" selected>🎯 Next Unattempted SRT Set (No Repeat)</option>
            <option value="1">DIPR Official SRT Set 1 (60 Situations)</option>
            <option value="2">DIPR Official SRT Set 2 (60 Situations)</option>
            <option value="random">🎲 Random 60 Situations</option>
          </select>
        </div>

        <div class="form-group">
          <label>Practice Style</label>
          <div class="mode-selector">
            <div class="mode-option active" id="srtModeBooklet" onclick="setSrtMode('booklet')">
              <strong>📖 Full Booklet Mode (30:00 Timer)</strong>
              <span>All 60 situations scrollable with live clock, jump back & forth like real paper booklet.</span>
            </div>
            <div class="mode-option" id="srtModeFlash" onclick="setSrtMode('flash')">
              <strong>⚡ 30s Flash Mode</strong>
              <span>Each situation flashes on screen for 30 seconds automatically.</span>
            </div>
          </div>
        </div>

        <button class="btn-start" onclick="startSrtTest()">COMMENCE SRT SESSION (30 MINS)</button>
      </div>

      <!-- SRT ACTIVE SCREEN (BOOKLET MODE) -->
      <div class="card-box" id="srtActiveScreen" style="display: none; max-width: 960px;">
        <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 1px solid var(--bg-card-border);">
          <div>
            <h3 style="font-size: 1.3rem;">Situation Reaction Booklet</h3>
            <span style="font-size: 0.85rem; color: var(--text-muted);" id="srtCompletedCount">Answered: 0 / 60</span>
          </div>
          <div style="display: flex; align-items: center; gap: 1rem;">
            <div style="font-family: var(--font-mono); font-size: 1.8rem; font-weight: 700; color: var(--accent-gold);" id="srtMasterTimer">
              30:00
            </div>
            <button class="btn-start" style="width: auto; padding: 0.6rem 1.5rem; font-size: 0.9rem;" onclick="submitSrtTest()">
              Submit Test
            </button>
          </div>
        </div>

        <div class="srt-booklet" id="srtBookletList"></div>
      </div>

      <!-- SRT REVIEW -->
      <div class="card-box" id="srtReviewScreen" style="display: none; max-width: 960px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <h2>SRT Test Summary</h2>
            <p style="color: var(--text-muted); font-size: 0.9rem;" id="srtReviewStats">Attempted: 60 / 60</p>
          </div>
          <button class="btn-secondary" onclick="copySrtResponses()">📋 Raw Reactions</button>
        </div>

        <!-- AI EVALUATION CARD -->
        <div class="ai-eval-card">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; flex-wrap: wrap;">
            <div>
              <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="font-size: 1.3rem;">🤖</span>
                <strong style="color: var(--accent-blue); font-size: 1.1rem;">Free AI Psychologist SRT Evaluation</strong>
              </div>
              <p style="color: var(--text-muted); font-size: 0.85rem; margin-top: 0.35rem; max-width: 620px; line-height: 1.45;">
                Evaluate completeness of reaction, speed of decision, and sense of responsibility. Flags evasion ("called police and watched") and provides concise military-grade solutions.
              </p>
            </div>
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
              <button class="btn-start" style="width: auto; padding: 0.6rem 1.25rem; font-size: 0.85rem; background: var(--accent-blue); color: #000;" onclick="copySrtAiPrompt()">📋 Copy AI Assessor Prompt</button>
              <button class="btn-secondary" style="font-size: 0.85rem; padding: 0.6rem 1rem;" onclick="downloadSrtAiDossier()">📥 Download Dossier (.txt)</button>
            </div>
          </div>
          <div style="margin-top: 1rem; padding-top: 0.75rem; border-top: 1px solid var(--bg-card-border); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--text-muted);">Step 2: Paste into free AI chat:</span>
            <div style="display: flex; gap: 0.5rem;">
              <a href="https://chatgpt.com" target="_blank" class="ai-model-btn" style="background: rgba(16, 185, 129, 0.15); border-color: var(--accent-green); color: var(--accent-green);">🚀 ChatGPT (Free) ↗</a>
              <a href="https://claude.ai" target="_blank" class="ai-model-btn" style="background: rgba(217, 119, 6, 0.15); border-color: #d97706; color: #fbbf24;">🟣 Claude (Free) ↗</a>
              <a href="https://gemini.google.com" target="_blank" class="ai-model-btn" style="background: rgba(56, 189, 248, 0.15); border-color: var(--accent-blue); color: var(--accent-blue);">✨ Google Gemini (Free) ↗</a>
            </div>
          </div>
        </div>

        <div id="srtReviewContent" style="max-height: 480px; overflow-y: auto; display: flex; flex-direction: column; gap: 1rem; margin-bottom: 1.5rem;"></div>
        <button class="btn-secondary" onclick="resetSrtToSetup()">← Return to Setup</button>
      </div>

    </section>

    <!-- ==============================================================
         4. SDT MODULE
         ============================================================== -->
    <section class="module-container" id="tab-sdt">
      <div class="card-box" style="max-width: 960px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; border-bottom: 1px solid var(--bg-card-border); padding-bottom: 1rem;">
          <div>
            <h2 class="section-title" style="text-align: left; margin: 0;">Self Description Test (SDT)</h2>
            <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 0.25rem;">
              5 Official DIPR Paragraphs. 15 Minutes allotted. Be honest, balanced, and growth-oriented.
            </p>
          </div>
          <div style="display: flex; align-items: center; gap: 1rem;">
            <div style="font-family: var(--font-mono); font-size: 1.8rem; font-weight: 700; color: var(--accent-gold);" id="sdtTimer">
              15:00
            </div>
            <button class="btn-secondary" id="btnSdtTimerToggle" onclick="toggleSdtTimer()">Start Timer</button>
          </div>
        </div>

        <!-- AI EVALUATION CARD FOR SDT -->
        <div class="ai-eval-card">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; flex-wrap: wrap;">
            <div>
              <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="font-size: 1.3rem;">🤖</span>
                <strong style="color: var(--accent-blue); font-size: 1.1rem;">Free AI SDT Triangulation & Authenticity Check</strong>
              </div>
              <p style="color: var(--text-muted); font-size: 0.85rem; margin-top: 0.35rem; max-width: 620px; line-height: 1.45;">
                AI compares your Parents, Teachers, Friends, and Self assessment to detect discrepancies, fake weaknesses ("perfectionist"), and prepare you for Interviewing Officer cross-examination.
              </p>
            </div>
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
              <button class="btn-start" style="width: auto; padding: 0.6rem 1.25rem; font-size: 0.85rem; background: var(--accent-blue); color: #000;" onclick="copySdtAiPrompt()">📋 Copy AI Assessor Prompt</button>
              <button class="btn-secondary" style="font-size: 0.85rem; padding: 0.6rem 1rem;" onclick="downloadSdtAiDossier()">📥 Download Dossier (.txt)</button>
            </div>
          </div>
          <div style="margin-top: 1rem; padding-top: 0.75rem; border-top: 1px solid var(--bg-card-border); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--text-muted);">Step 2: Paste into free AI chat:</span>
            <div style="display: flex; gap: 0.5rem;">
              <a href="https://chatgpt.com" target="_blank" class="ai-model-btn" style="background: rgba(16, 185, 129, 0.15); border-color: var(--accent-green); color: var(--accent-green);">🚀 ChatGPT (Free) ↗</a>
              <a href="https://claude.ai" target="_blank" class="ai-model-btn" style="background: rgba(217, 119, 6, 0.15); border-color: #d97706; color: #fbbf24;">🟣 Claude (Free) ↗</a>
              <a href="https://gemini.google.com" target="_blank" class="ai-model-btn" style="background: rgba(56, 189, 248, 0.15); border-color: var(--accent-blue); color: var(--accent-blue);">✨ Google Gemini (Free) ↗</a>
            </div>
          </div>
        </div>

        <div class="sdt-editor-box">
          <div class="sdt-card">
            <div class="sdt-label">1. Parents' Opinion</div>
            <div class="sdt-help">What do your father and mother think of you? (Habits, obedience, responsibility, emotional bond)</div>
            <textarea class="sdt-textarea" id="sdt1" placeholder="My parents consider me to be..."></textarea>
          </div>

          <div class="sdt-card">
            <div class="sdt-label">2. Teachers' / Instructors' Opinion</div>
            <div class="sdt-help">What do your teachers/professors think of you? (Grasp, punctuality, participation, sincerity)</div>
            <textarea class="sdt-textarea" id="sdt2" placeholder="My teachers describe me as..."></textarea>
          </div>

          <div class="sdt-card">
            <div class="sdt-label">3. Friends' / Colleagues' Opinion</div>
            <div class="sdt-help">What do your friends or peers say about you? (Trustworthiness, helping nature, fun to be with, crisis support)</div>
            <textarea class="sdt-textarea" id="sdt3" placeholder="My close friends appreciate that I..."></textarea>
          </div>

          <div class="sdt-card">
            <div class="sdt-label">4. Your Own Opinion (Self Assessment)</div>
            <div class="sdt-help">What are your genuine strengths and authentic modifiable weaknesses?</div>
            <textarea class="sdt-textarea" id="sdt4" placeholder="I consider myself to be... Areas where I can improve include..."></textarea>
          </div>

          <div class="sdt-card">
            <div class="sdt-label">5. Future Aspirations (What you want to become)</div>
            <div class="sdt-help">What kind of officer, professional, and citizen do you strive to develop into?</div>
            <textarea class="sdt-textarea" id="sdt5" placeholder="In the future, I aspire to become an officer who..."></textarea>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; margin-top: 1.5rem; gap: 1rem;">
          <button class="btn-secondary" onclick="saveSdtLocal()">💾 Save Draft</button>
          <button class="btn-start" style="width: auto; padding: 0.75rem 2rem;" onclick="copySdtText()">📋 Copy All 5 Paragraphs</button>
        </div>
      </div>
    </section>

    <!-- ==============================================================
         5. OIR MODULE (PDF UPLOAD + DIGITAL OMR SHEET)
         ============================================================== -->
    <section class="module-container" id="tab-oir">
      <div style="width: 100%; display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
        <div>
          <h2 style="font-size: 1.5rem; font-weight: 700;">Officer Intelligence Rating (OIR) Test</h2>
          <p style="color: var(--text-muted); font-size: 0.85rem;">Upload your Verbal/Non-Verbal Question Paper PDF & mark responses on the live OMR.</p>
        </div>
        <div style="display: flex; gap: 0.75rem; align-items: center;">
          <input type="file" id="oirPdfInput" accept=".pdf" style="display: none;">
          <button class="btn-secondary" onclick="document.getElementById('oirPdfInput').click()">
            📂 Upload OIR PDF
          </button>
          <div style="background: var(--bg-card); border: 1px solid var(--bg-card-border); padding: 0.4rem 0.8rem; border-radius: 6px; font-family: var(--font-mono); font-size: 1.3rem; font-weight: 700; color: var(--accent-gold);" id="oirTimerNum">
            20:00
          </div>
          <button class="btn-secondary" id="btnOirTimerToggle" onclick="toggleOirTimer()">Start Timer</button>
          <button class="btn-start" style="width: auto; padding: 0.5rem 1.25rem; font-size: 0.85rem;" onclick="submitOirOMR()">Submit OMR</button>
        </div>
      </div>

      <div class="oir-workspace">
        <div class="oir-pdf-viewer">
          <div id="oirPdfPlaceholder" style="flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 2rem; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📑</div>
            <h3 style="margin-bottom: 0.5rem;">No OIR Question Paper Loaded</h3>
            <p style="color: var(--text-muted); max-width: 440px; font-size: 0.9rem; margin-bottom: 1.5rem;">
              Upload any OIR test PDF (e.g. 50 Verbal/Non-Verbal questions) to view questions here and solve them directly using the OMR sheet on the right.
            </p>
            <button class="btn-start" style="width: auto; padding: 0.75rem 2rem;" onclick="document.getElementById('oirPdfInput').click()">
              Upload OIR PDF File
            </button>
          </div>
          <iframe id="oirPdfIframe" style="width: 100%; height: 100%; border: none; display: none;"></iframe>
        </div>

        <div class="oir-omr-pane">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--bg-card-border); padding-bottom: 0.75rem;">
            <div>
              <strong style="font-size: 1.05rem;">Digital OMR Sheet</strong>
              <div style="font-size: 0.8rem; color: var(--text-muted);" id="oirAttemptStats">Marked: 0 / 50 Questions</div>
            </div>
            <div style="display: flex; gap: 0.5rem;">
              <select id="oirQuestionCount" onchange="generateOmrRows()" style="padding: 0.35rem 0.6rem; font-size: 0.85rem;">
                <option value="40">40 Questions</option>
                <option value="50" selected>50 Questions</option>
                <option value="60">60 Questions</option>
              </select>
            </div>
          </div>

          <div class="omr-grid-container" id="omrRowsList"></div>
        </div>
      </div>
    </section>

    <!-- ==============================================================
         6. FULL MOCK BATTERY MODULE
         ============================================================== -->
    <section class="module-container" id="tab-fullmock">
      <div class="card-box" style="max-width: 820px; text-align: center;">
        <h2 class="section-title">Stage 2 Psychological Battery Mock</h2>
        <p class="section-subtitle">
          Experience the authentic, unbroken 3-hour psychological testing schedule of Services Selection Board (SSB).
        </p>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; text-align: left; margin-bottom: 2rem;">
          <div style="background: var(--bg-primary); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--bg-card-border);">
            <strong style="color: var(--accent-gold);">1. TAT (Thematic Apperception)</strong>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">12 Slides (11 pictures + 1 blank). 30s view, 4 min write per slide.</p>
          </div>
          <div style="background: var(--bg-primary); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--bg-card-border);">
            <strong style="color: var(--accent-gold);">2. WAT (Word Association)</strong>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">60 Words. 15 seconds per word continuous.</p>
          </div>
          <div style="background: var(--bg-primary); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--bg-card-border);">
            <strong style="color: var(--accent-gold);">3. SRT (Situation Reaction)</strong>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">60 Situations. Exactly 30 minutes to complete.</p>
          </div>
          <div style="background: var(--bg-primary); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--bg-card-border);">
            <strong style="color: var(--accent-gold);">4. SDT (Self Description)</strong>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">5 Paragraphs (Parents, Teachers, Friends, Self, Aim). 15 minutes.</p>
          </div>
        </div>

        <button class="btn-start" style="max-width: 400px; margin: 0 auto;" onclick="launchFullMockBattery()">
          🚀 COMMENCE FULL BATTERY SIMULATION
        </button>
      </div>
    </section>

    <!-- ==============================================================
         7. DEDICATED AI ASSESSOR (FREE EVALUATION HUB)
         ============================================================== -->
    <section class="module-container" id="tab-ai-assessor">
      <div class="card-box" style="max-width: 1040px;">
        <div style="border-bottom: 1px solid var(--bg-card-border); padding-bottom: 1rem; margin-bottom: 1.5rem;">
          <h2 class="section-title" style="text-align: left; margin: 0;">🤖 AI Psychologist Evaluation Hub (100% Free)</h2>
          <p style="color: var(--text-muted); font-size: 0.95rem; margin-top: 0.25rem; line-height: 1.5;">
            Evaluate your SSB responses for free using modern foundation models (ChatGPT-4o, Claude 3.5 Sonnet, or Google Gemini). Download test stimuli (including high-res TAT images) and copy expert Senior DIPR Psychologist prompts with 1 click.
          </p>
        </div>

        <!-- 3-STEP WORKFLOW GUIDE -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-bottom: 2rem;">
          <div style="background: var(--bg-primary); border: 1px solid var(--bg-card-border); border-radius: 8px; padding: 1.25rem;">
            <div style="font-size: 1.6rem; margin-bottom: 0.5rem;">📥 1. Download Stimuli & Prompt</div>
            <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.45;">
              Select any TAT set to download a <strong>ready-to-upload ZIP</strong> containing the slide images and your stories, or copy the formatted prompt for WAT, SRT, or SDT.
            </p>
          </div>
          <div style="background: var(--bg-primary); border: 1px solid var(--bg-card-border); border-radius: 8px; padding: 1.25rem;">
            <div style="font-size: 1.6rem; margin-bottom: 0.5rem;">💬 2. Open Free AI Chat</div>
            <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.45;">
              Open <a href="https://chatgpt.com" target="_blank" style="color: var(--accent-green); text-decoration: underline;">ChatGPT</a>, <a href="https://claude.ai" target="_blank" style="color: #fbbf24; text-decoration: underline;">Claude</a>, or <a href="https://gemini.google.com" target="_blank" style="color: var(--accent-blue); text-decoration: underline;">Gemini</a>. You do not need any paid developer API key!
            </p>
          </div>
          <div style="background: var(--bg-primary); border: 1px solid var(--bg-card-border); border-radius: 8px; padding: 1.25rem;">
            <div style="font-size: 1.6rem; margin-bottom: 0.5rem;">🎖️ 3. Get OLQ Scoring</div>
            <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.45;">
              The AI roleplays as a <strong>Senior DIPR Assessor</strong>, grading your responses across the 15 OLQs, highlighting red flags, and rewriting them into officer-level responses.
            </p>
          </div>
        </div>

        <!-- ON-DEMAND SET PACKAGE DOWNLOADER -->
        <div style="background: rgba(245, 158, 11, 0.05); border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 12px; padding: 1.5rem; margin-bottom: 2rem;">
          <h3 style="color: var(--accent-gold); margin-bottom: 0.75rem; font-size: 1.2rem;">📦 On-Demand Test Stimuli & Prompt Generator</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1.25rem;">
            Even if you practiced in a physical notebook, select any set below to generate the exact DIPR prompt and slide images package for evaluation.
          </p>

          <div class="grid-2">
            <div class="form-group">
              <label>Select Test Type</label>
              <select id="hubSelectType" onchange="updateHubOptions()">
                <option value="tat" selected>🖼️ Thematic Apperception Test (TAT) — With Slide Images ZIP</option>
                <option value="wat">⚡ Word Association Test (WAT) — 60 Words List</option>
                <option value="srt">📝 Situation Reaction Test (SRT) — 60 Situations</option>
                <option value="sdt">👤 Self Description Test (SDT) — 5 Dimensions</option>
              </select>
            </div>
            <div class="form-group">
              <label>Select Set</label>
              <select id="hubSelectSet"></select>
            </div>
          </div>

          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 0.5rem;">
            <button class="btn-start" style="width: auto; padding: 0.65rem 1.5rem; font-size: 0.9rem;" id="btnHubDownload" onclick="executeHubDownload()">
              📦 Download Package / Dossier
            </button>
            <button class="btn-secondary" style="font-size: 0.9rem;" onclick="executeHubCopyPrompt()">
              📋 Copy Prompt to Clipboard
            </button>
          </div>
        </div>

        <!-- 15 OLQS REFERENCE ACCORDION -->
        <div style="border-top: 1px solid var(--bg-card-border); padding-top: 1.5rem;">
          <h3 style="color: var(--accent-blue); margin-bottom: 1rem; font-size: 1.15rem;">📋 Official 15 Officer Like Qualities (OLQ) Assessment Matrix</h3>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem;">
            <div style="background: var(--bg-primary); border: 1px solid var(--bg-card-border); border-radius: 8px; padding: 1rem;">
              <strong style="color: var(--accent-gold); font-size: 0.9rem;">Factor I: Planning & Organising</strong>
              <ul style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.5rem; padding-left: 1.2rem; line-height: 1.6;">
                <li>1. Effective Intelligence</li>
                <li>2. Reasoning Ability</li>
                <li>3. Organising Ability</li>
                <li>4. Power of Expression</li>
              </ul>
            </div>
            <div style="background: var(--bg-primary); border: 1px solid var(--bg-card-border); border-radius: 8px; padding: 1rem;">
              <strong style="color: var(--accent-blue); font-size: 0.9rem;">Factor II: Social Adjustment</strong>
              <ul style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.5rem; padding-left: 1.2rem; line-height: 1.6;">
                <li>5. Social Adaptability</li>
                <li>6. Co-operation</li>
                <li>7. Sense of Responsibility</li>
              </ul>
            </div>
            <div style="background: var(--bg-primary); border: 1px solid var(--bg-card-border); border-radius: 8px; padding: 1rem;">
              <strong style="color: var(--accent-green); font-size: 0.9rem;">Factor III: Social Effectiveness</strong>
              <ul style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.5rem; padding-left: 1.2rem; line-height: 1.6;">
                <li>8. Initiative</li>
                <li>9. Self-Confidence</li>
                <li>10. Speed of Decision</li>
                <li>11. Ability to Influence Group</li>
                <li>12. Liveliness</li>
              </ul>
            </div>
            <div style="background: var(--bg-primary); border: 1px solid var(--bg-card-border); border-radius: 8px; padding: 1rem;">
              <strong style="color: var(--accent-red); font-size: 0.9rem;">Factor IV: Dynamic</strong>
              <ul style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.5rem; padding-left: 1.2rem; line-height: 1.6;">
                <li>13. Determination</li>
                <li>14. Courage</li>
                <li>15. Stamina</li>
              </ul>
            </div>
          </div>
        </div>

      </div>
    </section>

  </main>

  <script>
    // ==============================================================
    // DATA STORES
    // ==============================================================
    const WAT_SETS = {wat_sets_json};
    const ALL_WAT_WORDS = {all_wat_words_json};
    const SRT_SETS = {srt_sets_json};
    const TAT_SETS = {tat_sets_json};

    // ==============================================================
    // TOAST HELPER
    // ==============================================================
    function showToast(msg) {{
      const t = document.getElementById('toastNotice');
      t.textContent = msg;
      t.classList.add('visible');
      setTimeout(() => t.classList.remove('visible'), 2400);
    }}

    // ==============================================================
    // NAVIGATION
    // ==============================================================
    const tabs = document.querySelectorAll('.nav-tab');
    const modules = document.querySelectorAll('.module-container');

    tabs.forEach(tab => {{
      tab.addEventListener('click', () => {{
        tabs.forEach(t => t.classList.remove('active'));
        modules.forEach(m => m.classList.remove('active'));

        tab.classList.add('active');
        const targetId = tab.getAttribute('data-tab');
        document.getElementById(targetId).classList.add('active');
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }});
    }});

    // ==============================================================
    // PROGRESS TRACKER & NO-REPEAT ENGINE
    // ==============================================================
    const STORAGE_KEY = 'ssb_master_progress';

    function getProgressData() {{
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) {{
        return {{
          watCompleted: [],
          tatCompleted: [],
          srtCompleted: [],
          history: []
        }};
      }}
      try {{
        return JSON.parse(raw);
      }} catch (e) {{
        return {{ watCompleted: [], tatCompleted: [], srtCompleted: [], history: [] }};
      }}
    }}

    function saveProgressData(data) {{
      localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
      updateProgressDashboard();
      updateDropdownBadges();
    }}

    function markWatSetDone(id) {{
      const p = getProgressData();
      if (!p.watCompleted.includes(id)) p.watCompleted.push(id);
      p.history.unshift({{
        date: new Date().toLocaleString(),
        module: 'WAT',
        item: `Set ${{id}} (60 Words)`,
        result: 'Completed'
      }});
      saveProgressData(p);
    }}

    function markTatSetDone(id) {{
      const p = getProgressData();
      if (!p.tatCompleted.includes(id)) p.tatCompleted.push(id);
      p.history.unshift({{
        date: new Date().toLocaleString(),
        module: 'TAT',
        item: `Set ${{id}} (12 Slides)`,
        result: 'Completed'
      }});
      saveProgressData(p);
    }}

    function markSrtSetDone(id) {{
      const p = getProgressData();
      if (!p.srtCompleted.includes(id)) p.srtCompleted.push(id);
      p.history.unshift({{
        date: new Date().toLocaleString(),
        module: 'SRT',
        item: `Set ${{id}} (60 Situations)`,
        result: 'Completed'
      }});
      saveProgressData(p);
    }}

    function logCompletedSession(mod, item, result) {{
      const p = getProgressData();
      p.history.unshift({{
        date: new Date().toLocaleString(),
        module: mod,
        item: item,
        result: result
      }});
      saveProgressData(p);
    }}

    function clearPracticeHistory() {{
      if (confirm("Reset practice history? (Completed sets records will be cleared)")) {{
        localStorage.removeItem(STORAGE_KEY);
        updateProgressDashboard();
        updateDropdownBadges();
      }}
    }}

    function exportProgressJSON() {{
      const data = getProgressData();
      const blob = new Blob([JSON.stringify(data, null, 2)], {{ type: 'application/json' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `ssb_progress_backup_${{new Date().toISOString().slice(0,10)}}.json`;
      a.click();
    }}

    document.getElementById('importProgressInput').addEventListener('change', (e) => {{
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (evt) => {{
        try {{
          const parsed = JSON.parse(evt.target.result);
          if (parsed && Array.isArray(parsed.watCompleted)) {{
            saveProgressData(parsed);
            alert("Progress successfully restored!");
          }} else {{
            alert("Invalid backup file format.");
          }}
        }} catch(err) {{
          alert("Error parsing backup JSON: " + err.message);
        }}
      }};
      reader.readAsText(file);
    }});

    function updateProgressDashboard() {{
      const p = getProgressData();
      const watDone = p.watCompleted.length;
      const tatDone = p.tatCompleted.length;
      const srtDone = p.srtCompleted.length;

      document.getElementById('progWatVal').textContent = `${{watDone}} / ${{WAT_SETS.length}}`;
      document.getElementById('progWatBar').style.width = `${{(watDone / WAT_SETS.length) * 100}}%`;

      document.getElementById('progTatVal').textContent = `${{tatDone}} / ${{TAT_SETS.length}}`;
      document.getElementById('progTatBar').style.width = `${{(tatDone / TAT_SETS.length) * 100}}%`;

      document.getElementById('progSrtVal').textContent = `${{srtDone}} / 2`;
      document.getElementById('progSrtBar').style.width = `${{(srtDone / 2) * 100}}%`;

      document.getElementById('progTotalSessions').textContent = p.history.length;

      // Pills for WAT
      const pillsWat = document.getElementById('pillsWat');
      pillsWat.innerHTML = '';
      WAT_SETS.forEach(s => {{
        const isDone = p.watCompleted.includes(s.id);
        const pill = document.createElement('div');
        pill.className = `set-pill ${{isDone ? 'completed' : ''}}`;
        pill.innerHTML = `${{isDone ? '✅' : '⚡'}} Set ${{s.id}}`;
        pill.onclick = () => {{
          document.querySelector('[data-tab="tab-wat"]').click();
          document.getElementById('watSelectSet').value = `set_${{s.id}}`;
        }};
        pillsWat.appendChild(pill);
      }});

      // Pills for TAT
      const pillsTat = document.getElementById('pillsTat');
      pillsTat.innerHTML = '';
      TAT_SETS.forEach(s => {{
        const isDone = p.tatCompleted.includes(s.id);
        const pill = document.createElement('div');
        pill.className = `set-pill ${{isDone ? 'completed' : ''}}`;
        pill.innerHTML = `${{isDone ? '✅' : '🖼️'}} TAT ${{s.id}}`;
        pill.onclick = () => {{
          document.querySelector('[data-tab="tab-tat"]').click();
          document.getElementById('tatSelectSet').value = `tat_set_${{s.id}}`;
        }};
        pillsTat.appendChild(pill);
      }});

      // Pills for SRT
      const pillsSrt = document.getElementById('pillsSrt');
      pillsSrt.innerHTML = '';
      [1, 2].forEach(num => {{
        const isDone = p.srtCompleted.includes(num);
        const pill = document.createElement('div');
        pill.className = `set-pill ${{isDone ? 'completed' : ''}}`;
        pill.innerHTML = `${{isDone ? '✅' : '📝'}} SRT Set ${{num}}`;
        pill.onclick = () => {{
          document.querySelector('[data-tab="tab-srt"]').click();
          document.getElementById('srtSelectSet').value = `${{num}}`;
        }};
        pillsSrt.appendChild(pill);
      }});

      // Next Recommendation
      calculateNextRecommendation(p);

      // History Table
      const tbody = document.getElementById('historyTableBody');
      tbody.innerHTML = '';
      if (p.history.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="4" style="padding: 1.5rem; text-align: center; color: var(--text-muted);">No practice sessions recorded yet. Start any test to log your progress!</td></tr>';
      }} else {{
        p.history.slice(0, 30).forEach(h => {{
          const tr = document.createElement('tr');
          tr.style.borderBottom = '1px solid var(--bg-card-border)';
          tr.innerHTML = `
            <td style="padding: 0.6rem 1rem; color: var(--text-muted); font-family: var(--font-mono); font-size: 0.8rem;">${{h.date}}</td>
            <td style="padding: 0.6rem 1rem; font-weight: 700;">${{h.module}}</td>
            <td style="padding: 0.6rem 1rem;">${{h.item}}</td>
            <td style="padding: 0.6rem 1rem; color: var(--accent-green); font-weight: 600;">${{h.result}}</td>
          `;
          tbody.appendChild(tr);
        }});
      }}
    }}

    function calculateNextRecommendation(p) {{
      const nextWat = WAT_SETS.find(s => !p.watCompleted.includes(s.id));
      const nextTat = TAT_SETS.find(s => !p.tatCompleted.includes(s.id));
      const nextSrt = [1, 2].find(s => !p.srtCompleted.includes(s));

      const recDiv = document.getElementById('nextRecText');
      const btnRec = document.getElementById('btnLaunchNextRec');

      if (nextWat) {{
        recDiv.innerHTML = `<strong>WAT Set ${{nextWat.id}}</strong> (60 Words: ${{nextWat.preview}}) &mdash; Unattempted`;
        btnRec.onclick = () => {{
          document.querySelector('[data-tab="tab-wat"]').click();
          document.getElementById('watSelectSet').value = `set_${{nextWat.id}}`;
        }};
      }} else if (nextTat) {{
        recDiv.innerHTML = `<strong>TAT Set ${{nextTat.id}}</strong> (11 Pictures + Slide 12 Blank) &mdash; Unattempted`;
        btnRec.onclick = () => {{
          document.querySelector('[data-tab="tab-tat"]').click();
          document.getElementById('tatSelectSet').value = `tat_set_${{nextTat.id}}`;
        }};
      }} else if (nextSrt) {{
        recDiv.innerHTML = `<strong>SRT Set ${{nextSrt}}</strong> (60 Situations in 30 Mins) &mdash; Unattempted`;
        btnRec.onclick = () => {{
          document.querySelector('[data-tab="tab-srt"]').click();
          document.getElementById('srtSelectSet').value = `${{nextSrt}}`;
        }};
      }} else {{
        recDiv.innerHTML = `🏆 <strong style="color: var(--accent-green);">All Official Sets Mastered!</strong> Full syllabus completed. Practice Full Mock Battery next!`;
        btnRec.textContent = 'Launch Full Mock ❯';
        btnRec.onclick = () => document.querySelector('[data-tab="tab-fullmock"]').click();
      }}
    }}

    function updateDropdownBadges() {{
      const p = getProgressData();
      const watGroup = document.getElementById('watOptGroupSets');
      if (watGroup) {{
        Array.from(watGroup.options).forEach(opt => {{
          const setId = parseInt(opt.value.replace('set_', ''), 10);
          const isDone = p.watCompleted.includes(setId);
          const clean = opt.textContent.replace('✅ [COMPLETED] ', '');
          opt.textContent = isDone ? `✅ [COMPLETED] ${{clean}}` : clean;
        }});
      }}

      const tatGroup = document.getElementById('tatOptGroupSets');
      if (tatGroup) {{
        Array.from(tatGroup.options).forEach(opt => {{
          const setId = parseInt(opt.value.replace('tat_set_', ''), 10);
          const isDone = p.tatCompleted.includes(setId);
          const clean = opt.textContent.replace('✅ [COMPLETED] ', '');
          opt.textContent = isDone ? `✅ [COMPLETED] ${{clean}}` : clean;
        }});
      }}
    }}

    function loadProgress() {{
      updateProgressDashboard();
      updateDropdownBadges();
      updateHubOptions();
    }}

    // ==============================================================
    // 1. WAT ENGINE
    // ==============================================================
    let watWords = [];
    let watIndex = 0;
    let watDuration = 15;
    let watRemaining = 15;
    let watInterval = null;
    let watPaused = false;
    let watMode = 'paper';
    let watResponses = {{}};
    let watCurrentSetId = null;

    function setWatMode(m) {{
      watMode = m;
      document.getElementById('watModePaper').classList.toggle('active', m === 'paper');
      document.getElementById('watModeTyping').classList.toggle('active', m === 'typing');
    }}

    function startWatTest() {{
      const setChoice = document.getElementById('watSelectSet').value;
      watDuration = parseInt(document.getElementById('watSelectDuration').value, 10);
      const order = document.getElementById('watSelectOrder').value;

      watCurrentSetId = null;
      if (setChoice === 'next_unattempted') {{
        const p = getProgressData();
        const next = WAT_SETS.find(s => !p.watCompleted.includes(s.id)) || WAT_SETS[0];
        watWords = [...next.words];
        watCurrentSetId = next.id;
      }} else if (setChoice.startsWith('set_')) {{
        const id = parseInt(setChoice.replace('set_', ''), 10);
        const s = WAT_SETS.find(x => x.id === id);
        watWords = [...s.words];
        watCurrentSetId = id;
      }} else if (setChoice === 'random_60') {{
        const copy = [...ALL_WAT_WORDS];
        shuffle(copy);
        watWords = copy.slice(0, 60);
      }} else if (setChoice === 'random_30') {{
        const copy = [...ALL_WAT_WORDS];
        shuffle(copy);
        watWords = copy.slice(0, 30);
      }} else if (setChoice === 'all') {{
        watWords = [...ALL_WAT_WORDS];
      }}

      if (order === 'shuffle') shuffle(watWords);

      watIndex = 0;
      watResponses = {{}};
      watPaused = false;

      document.getElementById('watSetupScreen').style.display = 'none';
      document.getElementById('watReviewScreen').style.display = 'none';
      document.getElementById('watActiveScreen').style.display = 'block';

      document.getElementById('watTypingArea').style.display = watMode === 'typing' ? 'block' : 'none';

      displayWatWord();
      runWatTimer();
    }}

    function displayWatWord() {{
      const w = watWords[watIndex];
      document.getElementById('watFlashedWord').textContent = w;
      document.getElementById('watProgressTag').textContent = `WORD ${{watIndex + 1}} / ${{watWords.length}}`;

      const inp = document.getElementById('watInput');
      inp.value = watResponses[w] || '';
      if (watMode === 'typing') inp.focus();

      playAudioBeep(600, 0.08);
    }}

    function runWatTimer() {{
      clearInterval(watInterval);
      watRemaining = watDuration;
      updateWatTimerUI();

      watInterval = setInterval(() => {{
        if (watPaused) return;
        watRemaining--;
        updateWatTimerUI();

        if (watRemaining <= 0) {{
          nextWatWord();
        }}
      }}, 1000);
    }}

    function updateWatTimerUI() {{
      document.getElementById('watTimerNum').textContent = watRemaining;
      const circle = document.getElementById('watTimerCircle');
      const offset = 226 - (watRemaining / watDuration) * 226;
      circle.style.strokeDashoffset = offset;

      const bar = document.getElementById('watLinearBar');
      bar.style.width = `${{(watRemaining / watDuration) * 100}}%`;
    }}

    function recordWatResponse() {{
      if (watIndex < watWords.length) {{
        const w = watWords[watIndex];
        watResponses[w] = document.getElementById('watInput').value.trim() || '(No response typed)';
      }}
    }}

    function nextWatWord() {{
      recordWatResponse();
      watIndex++;
      if (watIndex >= watWords.length) {{
        finishWatTest();
      }} else {{
        displayWatWord();
        runWatTimer();
      }}
    }}

    function toggleWatPause() {{
      watPaused = !watPaused;
      document.getElementById('watPauseIcon').textContent = watPaused ? '▶' : '⏸';
      document.getElementById('watPauseLabel').textContent = watPaused ? 'Resume' : 'Pause';
    }}

    function abortWatTest() {{
      if (confirm("End WAT session? Completed responses will be shown.")) finishWatTest();
    }}

    function finishWatTest() {{
      clearInterval(watInterval);
      if (watCurrentSetId) {{
        markWatSetDone(watCurrentSetId);
      }} else {{
        logCompletedSession('WAT', 'Random 60 Drill', '60 Words Practiced');
      }}

      document.getElementById('watActiveScreen').style.display = 'none';
      document.getElementById('watReviewScreen').style.display = 'block';

      const tbody = document.getElementById('watReviewTbody');
      tbody.innerHTML = '';
      const list = watWords.slice(0, Math.max(watIndex, 1));
      list.forEach((w, i) => {{
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="padding: 0.6rem 1rem; border-bottom: 1px solid var(--bg-card-border); font-family: var(--font-mono); color: var(--text-muted);">${{i + 1}}</td>
          <td style="padding: 0.6rem 1rem; border-bottom: 1px solid var(--bg-card-border); color: var(--accent-gold); font-weight: 700;">${{w}}</td>
          <td style="padding: 0.6rem 1rem; border-bottom: 1px solid var(--bg-card-border);">${{escapeHtml(watResponses[w] || (watMode === 'typing' ? '—' : 'Written in notebook'))}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function copyWatResponses() {{
      let t = "=== WAT RESPONSES ===\\n";
      watWords.slice(0, Math.max(watIndex, 1)).forEach((w, i) => {{
        t += `${{i + 1}}. [${{w}}] => ${{watResponses[w] || 'Written on paper'}}\\n`;
      }});
      navigator.clipboard.writeText(t).then(() => showToast("Copied responses to clipboard!"));
    }}

    function resetWatToSetup() {{
      document.getElementById('watReviewScreen').style.display = 'none';
      document.getElementById('watSetupScreen').style.display = 'block';
    }}

    // ==============================================================
    // 2. TAT ENGINE
    // ==============================================================
    let tatSlides = [];
    let tatIndex = 0;
    let tatPhase = 'viewing';
    let tatViewDuration = 30;
    let tatWriteDuration = 240;
    let tatRemaining = 30;
    let tatInterval = null;
    let tatPaused = false;
    let tatMode = 'paper';
    let tatStories = {{}};
    let tatCurrentSetId = null;

    function setTatMode(m) {{
      tatMode = m;
      document.getElementById('tatModePaper').classList.toggle('active', m === 'paper');
      document.getElementById('tatModeTyping').classList.toggle('active', m === 'typing');
    }}

    function startTatTest() {{
      const setChoice = document.getElementById('tatSelectSet').value;
      tatViewDuration = parseInt(document.getElementById('tatViewTime').value, 10);
      tatWriteDuration = parseInt(document.getElementById('tatWriteTime').value, 10);

      tatCurrentSetId = null;
      if (setChoice === 'next_unattempted') {{
        const p = getProgressData();
        const next = TAT_SETS.find(s => !p.tatCompleted.includes(s.id)) || TAT_SETS[0];
        tatSlides = [...next.slides];
        tatCurrentSetId = next.id;
      }} else if (setChoice.startsWith('tat_set_')) {{
        const id = parseInt(setChoice.replace('tat_set_', ''), 10);
        const s = TAT_SETS.find(x => x.id === id);
        tatSlides = [...s.slides];
        tatCurrentSetId = id;
      }} else if (setChoice === 'random_11') {{
        const indices = [];
        while (indices.length < 11) {{
          const r = Math.floor(Math.random() * total_tat_images) + 1;
          if (!indices.includes(r)) indices.push(r);
        }}
        tatSlides = indices.map((idx, i) => ({{
          num: i + 1,
          type: 'image',
          src: `tat_images/tat_${{String(idx).padStart(3, '0')}}.jpg`,
          label: `Picture ${{i + 1}}`
        }}));
        tatSlides.push({{
          num: 12,
          type: 'blank',
          src: '',
          label: 'Slide 12 — BLANK SLIDE (Own Story)'
        }});
      }}

      tatIndex = 0;
      tatStories = {{}};
      tatPaused = false;

      document.getElementById('tatSetupScreen').style.display = 'none';
      document.getElementById('tatReviewScreen').style.display = 'none';
      document.getElementById('tatActiveScreen').style.display = 'block';

      commenceTatSlide();
    }}

    function commenceTatSlide() {{
      const s = tatSlides[tatIndex];
      document.getElementById('tatSlideTag').textContent = `SLIDE ${{s.num}} / ${{tatSlides.length}}`;

      const inp = document.getElementById('tatStoryInput');
      inp.value = tatStories[s.num] || '';

      startTatPhase('viewing');
    }}

    function startTatPhase(phase) {{
      tatPhase = phase;
      const s = tatSlides[tatIndex];
      const badge = document.getElementById('tatPhaseBadge');
      const imgWrap = document.getElementById('tatImgWrap');
      const blankDiv = document.getElementById('tatBlankSlide');
      const writingPrompt = document.getElementById('tatWritingPrompt');
      const typingWrap = document.getElementById('tatTypingContainer');

      if (phase === 'viewing') {{
        badge.className = 'tat-phase-badge phase-viewing';
        badge.textContent = `👁️ OBSERVATION PHASE (${{tatViewDuration}}s)`;
        tatRemaining = tatViewDuration;

        if (s.type === 'blank') {{
          imgWrap.style.display = 'none';
          blankDiv.style.display = 'block';
        }} else {{
          blankDiv.style.display = 'none';
          imgWrap.style.display = 'flex';
          document.getElementById('tatCurrentImg').src = s.src;
        }}

        writingPrompt.style.display = 'none';
        typingWrap.style.display = 'none';
        playAudioBeep(700, 0.15);
      }} else {{
        badge.className = 'tat-phase-badge phase-writing';
        badge.textContent = `✍️ WRITING PHASE (${{Math.floor(tatWriteDuration/60)}} MINS)`;
        tatRemaining = tatWriteDuration;

        imgWrap.style.display = 'none';
        blankDiv.style.display = 'none';
        writingPrompt.style.display = 'block';

        if (tatMode === 'typing') {{
          typingWrap.style.display = 'block';
          document.getElementById('tatStoryInput').focus();
        }} else {{
          typingWrap.style.display = 'none';
        }}
        playAudioBeep(500, 0.25);
      }}

      runTatTimer();
    }}

    function runTatTimer() {{
      clearInterval(tatInterval);
      updateTatTimerUI();

      tatInterval = setInterval(() => {{
        if (tatPaused) return;
        tatRemaining--;
        updateTatTimerUI();

        if (tatRemaining <= 0) {{
          if (tatPhase === 'viewing') {{
            startTatPhase('writing');
          }} else {{
            advanceTatSlide();
          }}
        }}
      }}, 1000);
    }}

    function updateTatTimerUI() {{
      document.getElementById('tatTimerNum').textContent = tatRemaining;
      const maxT = tatPhase === 'viewing' ? tatViewDuration : tatWriteDuration;
      const circle = document.getElementById('tatTimerCircle');
      const offset = 226 - (tatRemaining / maxT) * 226;
      circle.style.strokeDashoffset = offset;
    }}

    function recordTatStory() {{
      const s = tatSlides[tatIndex];
      tatStories[s.num] = document.getElementById('tatStoryInput').value.trim() || '(No story typed)';
    }}

    function advanceTatPhaseEarly() {{
      if (tatPhase === 'viewing') {{
        startTatPhase('writing');
      }} else {{
        advanceTatSlide();
      }}
    }}

    function advanceTatSlide() {{
      recordTatStory();
      tatIndex++;
      if (tatIndex >= tatSlides.length) {{
        finishTatTest();
      }} else {{
        commenceTatSlide();
      }}
    }}

    function toggleTatPause() {{
      tatPaused = !tatPaused;
      document.getElementById('tatPauseIcon').textContent = tatPaused ? '▶' : '⏸';
      document.getElementById('tatPauseLabel').textContent = tatPaused ? 'Resume' : 'Pause';
    }}

    function abortTatTest() {{
      if (confirm("End TAT test now? Stories written so far will be displayed.")) finishTatTest();
    }}

    function finishTatTest() {{
      clearInterval(tatInterval);
      if (tatCurrentSetId) {{
        markTatSetDone(tatCurrentSetId);
      }} else {{
        logCompletedSession('TAT', 'Random 11+Blank Drill', '12 Stories Practiced');
      }}

      document.getElementById('tatActiveScreen').style.display = 'none';
      document.getElementById('tatReviewScreen').style.display = 'block';

      const wrap = document.getElementById('tatReviewList');
      wrap.innerHTML = '';
      tatSlides.slice(0, Math.max(tatIndex, 1)).forEach(s => {{
        const card = document.createElement('div');
        card.style = 'background: var(--bg-primary); border: 1px solid var(--bg-card-border); border-radius: 8px; padding: 1rem; display: flex; gap: 1rem;';
        const imgMarkup = s.type === 'blank' 
          ? '<div style="width: 100px; height: 75px; background: #000; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; border-radius: 4px;">BLANK</div>'
          : `<img src="${{s.src}}" style="width: 100px; height: 75px; object-fit: cover; border-radius: 4px;">`;
        
        card.innerHTML = `
          ${{imgMarkup}}
          <div style="flex: 1;">
            <strong style="color: var(--accent-gold);">Slide ${{s.num}}: ${{s.label}}</strong>
            <p style="margin-top: 0.5rem; font-size: 0.9rem; line-height: 1.5;">${{escapeHtml(tatStories[s.num] || 'Written in booklet')}}</p>
          </div>
        `;
        wrap.appendChild(card);
      }});
    }}

    function copyTatResponses() {{
      let t = "=== TAT STORIES ===\\n";
      tatSlides.slice(0, Math.max(tatIndex, 1)).forEach(s => {{
        t += `\\n[Slide ${{s.num}}: ${{s.label}}]\\n${{tatStories[s.num] || 'Written in booklet'}}\\n`;
      }});
      navigator.clipboard.writeText(t).then(() => showToast("Copied stories to clipboard!"));
    }}

    function resetTatToSetup() {{
      document.getElementById('tatReviewScreen').style.display = 'none';
      document.getElementById('tatSetupScreen').style.display = 'block';
    }}

    // ==============================================================
    // 3. SRT ENGINE
    // ==============================================================
    let srtList = [];
    let srtResponses = {{}};
    let srtRemainingSec = 1800;
    let srtInterval = null;
    let srtMode = 'booklet';
    let srtCurrentSetId = null;

    function setSrtMode(m) {{
      srtMode = m;
      document.getElementById('srtModeBooklet').classList.toggle('active', m === 'booklet');
      document.getElementById('srtModeFlash').classList.toggle('active', m === 'flash');
    }}

    function startSrtTest() {{
      let setChoice = document.getElementById('srtSelectSet').value;
      srtCurrentSetId = null;

      if (setChoice === 'next_unattempted') {{
        const p = getProgressData();
        const next = [1, 2].find(s => !p.srtCompleted.includes(s)) || 1;
        setChoice = String(next);
      }}

      if (setChoice === '1') {{
        srtList = [...SRT_SETS[0]];
        srtCurrentSetId = 1;
      }} else if (setChoice === '2') {{
        srtList = [...SRT_SETS[1]];
        srtCurrentSetId = 2;
      }} else {{
        const all = [...SRT_SETS[0], ...SRT_SETS[1]];
        shuffle(all);
        srtList = all.slice(0, 60);
      }}

      srtResponses = {{}};
      srtRemainingSec = 1800;

      document.getElementById('srtSetupScreen').style.display = 'none';
      document.getElementById('srtReviewScreen').style.display = 'none';
      document.getElementById('srtActiveScreen').style.display = 'block';

      renderSrtBooklet();
      runSrtMasterTimer();
    }}

    function renderSrtBooklet() {{
      const wrap = document.getElementById('srtBookletList');
      wrap.innerHTML = '';

      srtList.forEach((sit, idx) => {{
        const item = document.createElement('div');
        item.className = 'srt-item';
        item.innerHTML = `
          <div class="srt-prompt">
            <span style="color: var(--accent-gold); font-family: var(--font-mono); font-weight: 700; margin-right: 0.5rem;">#${{idx + 1}}</span>
            ${{sit}}
          </div>
          <input type="text" class="srt-input" placeholder="He..." oninput="recordSrtInput(${{idx}}, this.value)">
        `;
        wrap.appendChild(item);
      }});
    }}

    function recordSrtInput(idx, val) {{
      srtResponses[idx] = val;
      updateSrtProgressCount();
    }}

    function updateSrtProgressCount() {{
      const filled = Object.values(srtResponses).filter(v => v.trim().length > 0).length;
      document.getElementById('srtCompletedCount').textContent = `Answered: ${{filled}} / ${{srtList.length}}`;
    }}

    function runSrtMasterTimer() {{
      clearInterval(srtInterval);
      srtInterval = setInterval(() => {{
        srtRemainingSec--;
        const m = Math.floor(srtRemainingSec / 60);
        const s = srtRemainingSec % 60;
        document.getElementById('srtMasterTimer').textContent = `${{String(m).padStart(2, '0')}}:${{String(s).padStart(2, '0')}}`;

        if (srtRemainingSec <= 0) {{
          clearInterval(srtInterval);
          alert("Time is up! 30 Minutes over for Situation Reaction Test.");
          submitSrtTest();
        }}
      }}, 1000);
    }}

    function submitSrtTest() {{
      clearInterval(srtInterval);
      const filled = Object.values(srtResponses).filter(v => v.trim().length > 0).length;

      if (srtCurrentSetId) {{
        markSrtSetDone(srtCurrentSetId);
      }} else {{
        logCompletedSession('SRT', `Attempted ${{filled}} Situations`, 'Test Submitted');
      }}

      document.getElementById('srtActiveScreen').style.display = 'none';
      document.getElementById('srtReviewScreen').style.display = 'block';

      document.getElementById('srtReviewStats').textContent = `Completed ${{filled}} / ${{srtList.length}} Situations in allotted time`;

      const wrap = document.getElementById('srtReviewContent');
      wrap.innerHTML = '';
      srtList.forEach((sit, i) => {{
        const div = document.createElement('div');
        div.style = 'background: var(--bg-primary); border: 1px solid var(--bg-card-border); border-radius: 8px; padding: 1rem;';
        div.innerHTML = `
          <strong>#${{i + 1}}: ${{sit}}</strong>
          <p style="margin-top: 0.4rem; color: var(--accent-gold);">${{escapeHtml(srtResponses[i] || '(Unanswered)')}}</p>
        `;
        wrap.appendChild(div);
      }});
    }}

    function copySrtResponses() {{
      let t = "=== SRT RESPONSES ===\\n";
      srtList.forEach((sit, i) => {{
        t += `${{i + 1}}. ${{sit}} => ${{srtResponses[i] || '(Unanswered)'}}\\n`;
      }});
      navigator.clipboard.writeText(t).then(() => showToast("Copied SRT responses!"));
    }}

    function resetSrtToSetup() {{
      document.getElementById('srtReviewScreen').style.display = 'none';
      document.getElementById('srtSetupScreen').style.display = 'block';
    }}

    // ==============================================================
    // 4. SDT ENGINE
    // ==============================================================
    let sdtSec = 900;
    let sdtInterval = null;
    let sdtRunning = false;

    function toggleSdtTimer() {{
      sdtRunning = !sdtRunning;
      const btn = document.getElementById('btnSdtTimerToggle');
      if (sdtRunning) {{
        btn.textContent = 'Pause Timer';
        sdtInterval = setInterval(() => {{
          sdtSec--;
          const m = Math.floor(sdtSec / 60);
          const s = sdtSec % 60;
          document.getElementById('sdtTimer').textContent = `${{String(m).padStart(2, '0')}}:${{String(s).padStart(2, '0')}}`;
          if (sdtSec <= 0) {{
            clearInterval(sdtInterval);
            alert("15 Minutes time over for Self Description Test!");
            logCompletedSession('SDT', 'Full 5 Paragraphs', '15m Session Completed');
          }}
        }}, 1000);
      }} else {{
        btn.textContent = 'Resume Timer';
        clearInterval(sdtInterval);
      }}
    }}

    function saveSdtLocal() {{
      const d = {{
        p1: document.getElementById('sdt1').value,
        p2: document.getElementById('sdt2').value,
        p3: document.getElementById('sdt3').value,
        p4: document.getElementById('sdt4').value,
        p5: document.getElementById('sdt5').value
      }};
      localStorage.setItem('ssb_sdt_draft', JSON.stringify(d));
      logCompletedSession('SDT', 'Draft Updated', 'Saved in browser');
      showToast("Draft saved in browser!");
    }}

    function copySdtText() {{
      let t = "=== SELF DESCRIPTION TEST (SDT) ===\\n\\n";
      t += "1. PARENTS' OPINION:\\n" + (document.getElementById('sdt1').value || '—') + "\\n\\n";
      t += "2. TEACHERS' OPINION:\\n" + (document.getElementById('sdt2').value || '—') + "\\n\\n";
      t += "3. FRIENDS' OPINION:\\n" + (document.getElementById('sdt3').value || '—') + "\\n\\n";
      t += "4. SELF ASSESSMENT:\\n" + (document.getElementById('sdt4').value || '—') + "\\n\\n";
      t += "5. FUTURE ASPIRATIONS:\\n" + (document.getElementById('sdt5').value || '—') + "\\n";
      navigator.clipboard.writeText(t).then(() => showToast("Copied all 5 paragraphs to clipboard!"));
    }}

    // ==============================================================
    // 5. OIR ENGINE
    // ==============================================================
    let oirResponses = {{}};
    let oirSec = 1200;
    let oirInterval = null;
    let oirRunning = false;

    document.getElementById('oirPdfInput').addEventListener('change', (e) => {{
      const file = e.target.files[0];
      if (!file) return;
      const url = URL.createObjectURL(file);
      document.getElementById('oirPdfPlaceholder').style.display = 'none';
      const iframe = document.getElementById('oirPdfIframe');
      iframe.src = url;
      iframe.style.display = 'block';
      logCompletedSession('OIR', file.name, 'PDF Loaded for practice');
    }});

    function generateOmrRows() {{
      const count = parseInt(document.getElementById('oirQuestionCount').value, 10);
      const wrap = document.getElementById('omrRowsList');
      wrap.innerHTML = '';
      oirResponses = {{}};

      for (let i = 1; i <= count; i++) {{
        const row = document.createElement('div');
        row.className = 'omr-row';
        row.innerHTML = `
          <span class="omr-q-num">${{i}}.</span>
          <div class="omr-options">
            <div class="omr-bubble" onclick="selectOmrBubble(${{i}}, 'A', this)">A</div>
            <div class="omr-bubble" onclick="selectOmrBubble(${{i}}, 'B', this)">B</div>
            <div class="omr-bubble" onclick="selectOmrBubble(${{i}}, 'C', this)">C</div>
            <div class="omr-bubble" onclick="selectOmrBubble(${{i}}, 'D', this)">D</div>
          </div>
        `;
        wrap.appendChild(row);
      }}
      updateOmrAttemptStats();
    }}

    function selectOmrBubble(qNum, opt, el) {{
      const row = el.closest('.omr-row');
      row.querySelectorAll('.omr-bubble').forEach(b => b.classList.remove('selected'));
      el.classList.add('selected');
      oirResponses[qNum] = opt;
      updateOmrAttemptStats();
    }}

    function updateOmrAttemptStats() {{
      const marked = Object.keys(oirResponses).length;
      const total = parseInt(document.getElementById('oirQuestionCount').value, 10);
      document.getElementById('oirAttemptStats').textContent = `Marked: ${{marked}} / ${{total}} Questions`;
    }}

    function toggleOirTimer() {{
      oirRunning = !oirRunning;
      const btn = document.getElementById('btnOirTimerToggle');
      if (oirRunning) {{
        btn.textContent = 'Pause';
        oirInterval = setInterval(() => {{
          oirSec--;
          const m = Math.floor(oirSec / 60);
          const s = oirSec % 60;
          document.getElementById('oirTimerNum').textContent = `${{String(m).padStart(2, '0')}}:${{String(s).padStart(2, '0')}}`;
          if (oirSec <= 0) {{
            clearInterval(oirInterval);
            alert("OIR Allotted time over!");
            submitOirOMR();
          }}
        }}, 1000);
      }} else {{
        btn.textContent = 'Resume';
        clearInterval(oirInterval);
      }}
    }}

    function submitOirOMR() {{
      const total = parseInt(document.getElementById('oirQuestionCount').value, 10);
      const marked = Object.keys(oirResponses).length;
      logCompletedSession('OIR', `${{marked}}/${{total}} Marked`, 'Test Completed');
      let summary = `OIR Test Completed!\\nMarked: ${{marked}} / ${{total}}\\nUnanswered: ${{total - marked}}\\n\\nCopy your marked answers?`;
      if (confirm(summary)) {{
        let t = "=== OIR ANSWER SHEET ===\\n";
        for (let i = 1; i <= total; i++) {{
          t += `Q${{i}}: ${{oirResponses[i] || '—'}}\\n`;
        }}
        navigator.clipboard.writeText(t).then(() => showToast("OMR Answer sheet copied to clipboard!"));
      }}
    }}

    // ==============================================================
    // 6. FULL MOCK BATTERY LAUNCHER
    // ==============================================================
    function launchFullMockBattery() {{
      if (confirm("Commence Full Stage 2 Psychological Mock Test?\\n\\nSchedule:\\n1. 12 TAT Stories (approx 50 mins)\\n2. 60 WAT Words (15 mins)\\n3. 60 SRT Situations (30 mins)\\n4. 5 SDT Paragraphs (15 mins)")) {{
        document.querySelector('[data-tab="tab-tat"]').click();
        startTatTest();
      }}
    }}

    // ==============================================================
    // 7. AI EVALUATION PROMPT GENERATORS & DOWNLOADERS
    // ==============================================================

    function generateWatPrompt(wordsList, responsesMap, label) {{
      let t = `Act as an expert Senior DIPR (Defence Institute of Psychological Research) Psychologist and Services Selection Board (SSB) Assessor evaluating a candidate for the Indian Armed Forces (Army, Navy, Air Force).\\n\\n`;
      t += `Task: Evaluate the candidate's spontaneous responses in the Word Association Test (${{label || 'WAT 60 Words'}}).\\n\\n`;
      t += `### DIPR EVALUATION CRITERIA & 15 OLQS:\\n`;
      t += `Assess the candidate across the 4 Psychological Factors and 15 Officer Like Qualities (OLQs):\\n`;
      t += `1. Factor I (Planning & Organizing): Effective Intelligence, Reasoning Ability, Organizing Ability, Power of Expression.\\n`;
      t += `2. Factor II (Social Adjustment): Social Adaptability, Cooperation, Sense of Responsibility.\\n`;
      t += `3. Factor III (Social Effectiveness): Initiative, Self Confidence, Speed of Decision, Ability to Influence Group, Liveliness.\\n`;
      t += `4. Factor IV (Dynamic): Determination, Courage, Stamina.\\n\\n`;
      t += `### KEY PSYCHOLOGICAL RED FLAGS TO CATCH:\\n`;
      t += `- Preaching / Moralizing / Advising: Using words like 'should', 'must', 'ought to', 'always', 'never'.\\n`;
      t += `- Universal / Factual statements (e.g. 'Sun rises in east') which reveal no personal subconscious trait.\\n`;
      t += `- Negative / Passive associations (e.g. associating 'FAIL', 'WAR', 'SAD', 'DEFEAT' with death or depression rather than overcoming them).\\n`;
      t += `- Lack of action: Sentences lacking active verbs or personal agency.\\n\\n`;
      t += `### CANDIDATE'S WAT RESPONSES (${{wordsList.length}} Words):\\n`;
      wordsList.forEach((w, i) => {{
        t += `${{i + 1}}. [${{w}}] => ${{responsesMap[w] || '(Written on paper in notebook)'}}\\n`;
      }});
      t += `\\n### FORMAT YOUR PSYCHOLOGIST EVALUATION REPORT AS FOLLOWS:\\n`;
      t += `1. **Overall Psychological Impression & OLQ Factor Profile** (Strengths & growth areas across Factors I-IV).\\n`;
      t += `2. **Top 5 Strongest Responses** (Explain the specific OLQ projected).\\n`;
      t += `3. **Critical Red Flags & Weak Responses** (Identify passive, preachy, or depressive responses).\\n`;
      t += `4. **Rewritten Officer-Grade Model Responses** for all weak responses (showing how an officer responds in 4-6 concise words).\\n`;
      t += `5. **Final Recommendation Score** (Recommended / Borderline / Not Recommended) with concrete action tips.\\n`;
      return t;
    }}

    function generateTatPrompt(slidesList, storiesMap, label) {{
      let t = `Act as an expert Senior DIPR Psychologist and SSB Assessor evaluating a candidate for the Indian Armed Forces.\\n\\n`;
      t += `Task: Evaluate the candidate's stories written for the Thematic Apperception Test (${{label || 'TAT 12 Slides'}}).\\n`;
      t += `[NOTE: The candidate has uploaded the respective slide image(s) or the slide details are given below].\\n\\n`;
      t += `### DIPR 3-STAGE TAT EVALUATION PROTOCOL:\\n`;
      t += `1. **Stimulus Fidelity**: Did the candidate perceive the cues in the image (characters, background, mood, objects) or write an artificial pre-coached story?\\n`;
      t += `2. **Hero Analysis**: Central character's age, gender, mood, occupation. Does the hero lead by example, organize others, and accept responsibility?\\n`;
      t += `3. **3-Part Narrative**: (a) What led to the situation, (b) What action is being taken by the hero & team, (c) Positive, realistic final outcome.\\n`;
      t += `4. **Red Flags to Detect**: Over-the-top heroism (fighting 10 goons, unrealistic bravery), unnecessary tragedies (suicide, deaths, chronic illness), selfish motive (working only for money/award), or passing the buck (calling police and doing nothing).\\n\\n`;
      t += `### CANDIDATE'S TAT STORIES:\\n`;
      slidesList.forEach(s => {{
        t += `\\n=======================================================\\n`;
        t += `[Slide ${{s.num}}: ${{s.label}}] (Source: ${{s.src || 'Blank Slide - Candidate Choice'}})\\n`;
        t += `Candidate's Story:\\n${{storiesMap[s.num] || '(Story written in paper booklet)'}}\\n`;
      }});
      t += `\\n=======================================================\\n`;
      t += `\\n### FORMAT YOUR EVALUATION REPORT AS FOLLOWS:\\n`;
      t += `1. **Slide-by-Slide Psychological Breakdown**: Perception check, Hero evaluation, OLQs observed, rating (Recommended / Borderline / Unsuitable).\\n`;
      t += `2. **DIPR Model Rewrite**: Provide a concise, officer-grade model story for the 2 weakest slides.\\n`;
      t += `3. **Blank Slide (Slide 12) In-Depth Analysis**: What core subconscious desires and life values does the candidate reveal?\\n`;
      t += `4. **Final Recommendation Verdict**: Psychological suitability for Armed Forces training.\\n`;
      return t;
    }}

    function generateSrtPrompt(sList, respMap, label) {{
      let t = `Act as an expert Senior DIPR Psychologist and SSB Assessor evaluating a candidate for the Indian Armed Forces.\\n\\n`;
      t += `Task: Evaluate the candidate's Situation Reaction Test (${{label || 'SRT 60 Situations'}}).\\n\\n`;
      t += `### DIPR EVALUATION CRITERIA:\\n`;
      t += `1. **Completeness of Reaction**: Did the candidate complete the action cycle (Action + Resolution), or leave it midway?\\n`;
      t += `2. **Resourcefulness & Speed of Decision**: Utilization of tools, manpower, and logical sequence.\\n`;
      t += `3. **Sense of Responsibility**: Did the hero personally step forward or evade duty ('reported to police and went away')?\\n`;
      t += `4. **Presence of Mind**: Calm, non-panicky reaction under pressure.\\n\\n`;
      t += `### CANDIDATE'S SRT RESPONSES:\\n`;
      sList.forEach((sit, i) => {{
        t += `${{i + 1}}. ${{sit}} => ${{respMap[i] || '(Unanswered)'}}\\n`;
      }});
      t += `\\n### FORMAT YOUR EVALUATION AS FOLLOWS:\\n`;
      t += `1. **Quantitative Performance**: Total attempted, completed reactions vs incomplete/evasive reactions.\\n`;
      t += `2. **OLQ Matrix Assessment** across Factor I, II, III, and IV.\\n`;
      t += `3. **Flagged Weak Reactions & Officer-Grade Rewrites** (Concise, telepathic, action-oriented military answers).\\n`;
      t += `4. **Psychologist's Overall Verdict**.\\n`;
      return t;
    }}

    function generateSdtPrompt(p1, p2, p3, p4, p5) {{
      let t = `Act as an expert Senior DIPR Psychologist and SSB Assessor evaluating a candidate for the Indian Armed Forces.\\n\\n`;
      t += `Task: Evaluate the candidate's Self Description Test (SDT) across all 5 dimensions.\\n\\n`;
      t += `### CANDIDATE'S 5 PARAGRAPHS:\\n`;
      t += `1. PARENTS' OPINION:\\n${{p1 || '—'}}\\n\\n`;
      t += `2. TEACHERS' / INSTRUCTORS' OPINION:\\n${{p2 || '—'}}\\n\\n`;
      t += `3. FRIENDS' / PEERS' OPINION:\\n${{p3 || '—'}}\\n\\n`;
      t += `4. SELF ASSESSMENT (STRENGTHS & WEAKNESSES):\\n${{p4 || '—'}}\\n\\n`;
      t += `5. FUTURE ASPIRATIONS & TRAITS WISH TO DEVELOP:\\n${{p5 || '—'}}\\n\\n`;
      t += `### PSYCHOLOGICAL EVALUATION CRITERIA:\\n`;
      t += `1. **Triangulation Check**: Consistency across Parents, Teachers, Friends, and Self assessment. (Are there contradictions?)\\n`;
      t += `2. **Authenticity vs Fake Pre-Coaching**: Are the weaknesses genuine and modifiable, or artificial clichés like 'I work too hard'?\\n`;
      t += `3. **Interviewing Officer (IO) Correlation**: Likely trap questions the IO will ask based on these admissions.\\n`;
      t += `4. **Refined Officer-Grade SDT Version**.\\n`;
      return t;
    }}

    function downloadTextFile(filename, text) {{
      const blob = new Blob([text], {{ type: 'text/plain;charset=utf-8' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }}

    // --- WAT Evaluation Actions ---
    function copyWatAiPrompt() {{
      const list = watWords.slice(0, Math.max(watIndex, 1));
      const prompt = generateWatPrompt(list, watResponses, watCurrentSetId ? `WAT Set ${{watCurrentSetId}}` : 'WAT Custom Set');
      navigator.clipboard.writeText(prompt).then(() => showToast("Copied WAT AI Assessor Prompt!"));
    }}

    function downloadWatAiDossier() {{
      const list = watWords.slice(0, Math.max(watIndex, 1));
      const prompt = generateWatPrompt(list, watResponses, watCurrentSetId ? `WAT Set ${{watCurrentSetId}}` : 'WAT Custom Set');
      downloadTextFile(`WAT_Evaluation_Dossier_Set_${{watCurrentSetId || 'session'}}.txt`, prompt);
    }}

    // --- TAT Evaluation Actions & ZIP Bundler ---
    function copyTatAiPrompt() {{
      const slides = tatSlides.slice(0, Math.max(tatIndex, 1));
      const prompt = generateTatPrompt(slides, tatStories, tatCurrentSetId ? `TAT Set ${{tatCurrentSetId}}` : 'TAT Custom Set');
      navigator.clipboard.writeText(prompt).then(() => showToast("Copied TAT Prompt & Stories!"));
    }}

    function downloadTatAiDossier() {{
      const slides = tatSlides.slice(0, Math.max(tatIndex, 1));
      const prompt = generateTatPrompt(slides, tatStories, tatCurrentSetId ? `TAT Set ${{tatCurrentSetId}}` : 'TAT Custom Set');
      downloadTextFile(`TAT_Evaluation_Dossier_Set_${{tatCurrentSetId || 'session'}}.txt`, prompt);
    }}

    async function downloadTatZipPackage(customSetId) {{
      const setId = customSetId || tatCurrentSetId || 1;
      const btn = document.getElementById('btnDownloadTatZip');
      const originalText = btn ? btn.innerHTML : '';
      if (btn) {{
        btn.innerHTML = '⏳ Zipping Images + Prompt...';
        btn.disabled = true;
      }}

      try {{
        if (typeof JSZip === 'undefined') {{
          throw new Error("JSZip library loading. Please try again in 2 seconds.");
        }}

        const zip = new JSZip();
        const folder = zip.folder(`SSB_TAT_Set_${{setId}}_Package`);

        // Slides to package
        let slidesToPack = [];
        if (!customSetId && tatSlides.length > 0) {{
          slidesToPack = tatSlides.slice(0, Math.max(tatIndex, 1));
        }} else {{
          const target = TAT_SETS.find(s => s.id === setId) || TAT_SETS[0];
          slidesToPack = target.slides;
        }}

        // Prompt file
        const promptText = generateTatPrompt(slidesToPack, tatStories, `TAT Set ${{setId}}`);
        folder.file(`DIPR_TAT_Evaluation_Prompt.txt`, promptText);

        // Fetch slide images and pack them
        for (const s of slidesToPack) {{
          if (s.type === 'image' && s.src) {{
            try {{
              const resp = await fetch(s.src);
              if (resp.ok) {{
                const blob = await resp.blob();
                const fname = `Slide_${{String(s.num).padStart(2, '0')}}_${{s.src.split('/').pop()}}`;
                folder.file(fname, blob);
              }}
            }} catch(err) {{
              console.warn('Could not bundle image:', s.src, err);
            }}
          }}
        }}

        const zipBlob = await zip.generateAsync({{ type: 'blob' }});
        const url = URL.createObjectURL(zipBlob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `SSB_TAT_Set_${{setId}}_Evaluation_Package.zip`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);

        alert("✅ TAT AI Package Downloaded!\\n\\nPackage contains:\\n1. All Slide Images (tat_xxx.jpg)\\n2. DIPR Senior Psychologist Evaluation Prompt\\n\\nUpload the images and paste the prompt into ChatGPT, Claude, or Gemini for a free psychological assessment!");
      }} catch(e) {{
        alert("Downloading text prompt instead: " + e.message);
        downloadTatAiDossier();
      }} finally {{
        if (btn) {{
          btn.innerHTML = originalText;
          btn.disabled = false;
        }}
      }}
    }}

    // --- SRT Evaluation Actions ---
    function copySrtAiPrompt() {{
      const prompt = generateSrtPrompt(srtList, srtResponses, srtCurrentSetId ? `SRT Set ${{srtCurrentSetId}}` : 'SRT Custom Set');
      navigator.clipboard.writeText(prompt).then(() => showToast("Copied SRT AI Assessor Prompt!"));
    }}

    function downloadSrtAiDossier() {{
      const prompt = generateSrtPrompt(srtList, srtResponses, srtCurrentSetId ? `SRT Set ${{srtCurrentSetId}}` : 'SRT Custom Set');
      downloadTextFile(`SRT_Evaluation_Dossier_Set_${{srtCurrentSetId || 'session'}}.txt`, prompt);
    }}

    // --- SDT Evaluation Actions ---
    function copySdtAiPrompt() {{
      const p1 = document.getElementById('sdt1').value;
      const p2 = document.getElementById('sdt2').value;
      const p3 = document.getElementById('sdt3').value;
      const p4 = document.getElementById('sdt4').value;
      const p5 = document.getElementById('sdt5').value;
      const prompt = generateSdtPrompt(p1, p2, p3, p4, p5);
      navigator.clipboard.writeText(prompt).then(() => showToast("Copied SDT AI Assessor Prompt!"));
    }}

    function downloadSdtAiDossier() {{
      const p1 = document.getElementById('sdt1').value;
      const p2 = document.getElementById('sdt2').value;
      const p3 = document.getElementById('sdt3').value;
      const p4 = document.getElementById('sdt4').value;
      const p5 = document.getElementById('sdt5').value;
      const prompt = generateSdtPrompt(p1, p2, p3, p4, p5);
      downloadTextFile(`SDT_Evaluation_Dossier.txt`, prompt);
    }}

    // --- AI HUB ON-DEMAND GENERATOR ---
    function updateHubOptions() {{
      const type = document.getElementById('hubSelectType').value;
      const sel = document.getElementById('hubSelectSet');
      sel.innerHTML = '';

      if (type === 'tat') {{
        TAT_SETS.forEach(s => {{
          const opt = document.createElement('option');
          opt.value = s.id;
          opt.textContent = `${{s.title}} (11 Pictures + 1 Blank Slide)`;
          sel.appendChild(opt);
        }});
        document.getElementById('btnHubDownload').textContent = '📦 Download Slide Images & Prompt (.ZIP)';
      }} else if (type === 'wat') {{
        WAT_SETS.forEach(s => {{
          const opt = document.createElement('option');
          opt.value = s.id;
          opt.textContent = `WAT Set ${{s.id}} (${{s.count}} Words: ${{s.preview}})`;
          sel.appendChild(opt);
        }});
        document.getElementById('btnHubDownload').textContent = '📥 Download Word List & Prompt (.txt)';
      }} else if (type === 'srt') {{
        [1, 2].forEach(n => {{
          const opt = document.createElement('option');
          opt.value = n;
          opt.textContent = `SRT Official Set ${{n}} (60 Situations)`;
          sel.appendChild(opt);
        }});
        document.getElementById('btnHubDownload').textContent = '📥 Download Situations & Prompt (.txt)';
      }} else if (type === 'sdt') {{
        const opt = document.createElement('option');
        opt.value = '1';
        opt.textContent = 'Standard DIPR 5-Paragraph Self Description';
        sel.appendChild(opt);
        document.getElementById('btnHubDownload').textContent = '📥 Download SDT Framework & Prompt (.txt)';
      }}
    }}

    function executeHubDownload() {{
      const type = document.getElementById('hubSelectType').value;
      const val = parseInt(document.getElementById('hubSelectSet').value, 10);

      if (type === 'tat') {{
        downloadTatZipPackage(val);
      }} else if (type === 'wat') {{
        const s = WAT_SETS.find(x => x.id === val) || WAT_SETS[0];
        const dummyResp = {{}};
        s.words.forEach(w => dummyResp[w] = '(Write or paste your responses here)');
        const prompt = generateWatPrompt(s.words, dummyResp, `WAT Set ${{val}}`);
        downloadTextFile(`WAT_Set_${{val}}_Prompt_Dossier.txt`, prompt);
      }} else if (type === 'srt') {{
        const list = val === 1 ? SRT_SETS[0] : SRT_SETS[1];
        const dummyResp = {{}};
        list.forEach((_, i) => dummyResp[i] = '(Write or paste your reaction here)');
        const prompt = generateSrtPrompt(list, dummyResp, `SRT Set ${{val}}`);
        downloadTextFile(`SRT_Set_${{val}}_Prompt_Dossier.txt`, prompt);
      }} else if (type === 'sdt') {{
        const prompt = generateSdtPrompt('', '', '', '', '');
        downloadTextFile(`SDT_Prompt_Template.txt`, prompt);
      }}
    }}

    function executeHubCopyPrompt() {{
      const type = document.getElementById('hubSelectType').value;
      const val = parseInt(document.getElementById('hubSelectSet').value, 10);

      if (type === 'tat') {{
        const s = TAT_SETS.find(x => x.id === val) || TAT_SETS[0];
        const dummyResp = {{}};
        s.slides.forEach(sl => dummyResp[sl.num] = '(Write or paste your story here)');
        const prompt = generateTatPrompt(s.slides, dummyResp, `TAT Set ${{val}}`);
        navigator.clipboard.writeText(prompt).then(() => showToast(`Copied TAT Set ${{val}} Evaluation Prompt!`));
      }} else if (type === 'wat') {{
        const s = WAT_SETS.find(x => x.id === val) || WAT_SETS[0];
        const dummyResp = {{}};
        s.words.forEach(w => dummyResp[w] = '(Write or paste your responses here)');
        const prompt = generateWatPrompt(s.words, dummyResp, `WAT Set ${{val}}`);
        navigator.clipboard.writeText(prompt).then(() => showToast(`Copied WAT Set ${{val}} Evaluation Prompt!`));
      }} else if (type === 'srt') {{
        const list = val === 1 ? SRT_SETS[0] : SRT_SETS[1];
        const dummyResp = {{}};
        list.forEach((_, i) => dummyResp[i] = '(Write or paste your reaction here)');
        const prompt = generateSrtPrompt(list, dummyResp, `SRT Set ${{val}}`);
        navigator.clipboard.writeText(prompt).then(() => showToast(`Copied SRT Set ${{val}} Evaluation Prompt!`));
      }} else if (type === 'sdt') {{
        const prompt = generateSdtPrompt('', '', '', '', '');
        navigator.clipboard.writeText(prompt).then(() => showToast("Copied SDT Evaluation Prompt Template!"));
      }}
    }}

    // ==============================================================
    // UTILITIES
    // ==============================================================
    function shuffle(arr) {{
      for (let i = arr.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
      }}
    }}

    function escapeHtml(str) {{
      return (str || '').replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    }}

    function playAudioBeep(freq = 600, duration = 0.1) {{
      try {{
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.frequency.value = freq;
        gain.gain.setValueAtTime(0.08, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
        osc.start();
        osc.stop(ctx.currentTime + duration);
      }} catch (e) {{}}
    }}

    // Theme toggle
    let isLight = false;
    document.getElementById('btnToggleTheme').addEventListener('click', () => {{
      isLight = !isLight;
      document.body.classList.toggle('dipr-projector', isLight);
      document.getElementById('themeIcon').textContent = isLight ? '🌙' : '☀️';
      document.getElementById('themeLabel').textContent = isLight ? 'Dark Hall' : 'Projector Mode';
    }});

    // Fullscreen toggle
    document.getElementById('btnToggleFullscreen').addEventListener('click', () => {{
      if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {{}});
      else if (document.exitFullscreen) document.exitFullscreen();
    }});

    // Init on load
    generateOmrRows();
    loadProgress();
  </script>
</body>
</html>
'''

with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated with AI Evaluation Hub and 1-Click Multimodal Downloaders!")
