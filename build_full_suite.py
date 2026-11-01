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

# Load TAT Sets
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
        'label': 'Slide 12 — Blank Slide (Candidate Story)'
    })
    tat_sets.append({
        'id': s_idx + 1,
        'title': f'TAT Set {s_idx + 1}',
        'desc': f'11 Pictures (tat_{start:03d} to tat_{end:03d}) + 1 Blank Slide',
        'slides': slides
    })

# Load GTO Datasets
with open(os.path.join(out_dir, 'lecturette_topics.json'), 'r', encoding='utf-8') as f:
    lecturette_data = json.load(f)

with open(os.path.join(out_dir, 'gd_topics.json'), 'r', encoding='utf-8') as f:
    gd_topics_data = json.load(f)

wat_sets_json = json.dumps(wat_sets)
all_wat_words_json = json.dumps(all_wat_words)
srt_sets_json = json.dumps(srt_sets)
tat_sets_json = json.dumps(tat_sets)
lecturette_data_json = json.dumps(lecturette_data)
gd_topics_json = json.dumps(gd_topics_data)

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SSB Master Suite — Complete DIPR Psychology, GTO & OIR Testing Platform</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Rajdhani:wght@500;600;700&display=swap" rel="stylesheet">
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
      --bg-base: #070a10;
      --bg-surface: #0e1420;
      --bg-surface-elevated: #151e2e;
      --border-subtle: #1e293b;
      --border-focus: #3b82f6;
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-tertiary: #64748b;
      --accent-brass: #d97706;
      --accent-brass-subtle: rgba(217, 119, 6, 0.12);
      --accent-brass-glow: rgba(217, 119, 6, 0.28);
      --accent-ready: #10b981;
      --accent-ready-subtle: rgba(16, 185, 129, 0.12);
      --accent-alert: #ef4444;
      --accent-intel: #38bdf8;
      --accent-intel-subtle: rgba(56, 189, 248, 0.1);
      
      --font-ui: 'Inter', -apple-system, sans-serif;
      --font-tactical: 'Rajdhani', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;

      --radius-sm: 4px;
      --radius-md: 6px;
      --radius-lg: 10px;
    }}

    body.projector-hall {{
      --bg-base: #f1f5f9;
      --bg-surface: #ffffff;
      --bg-surface-elevated: #f8fafc;
      --border-subtle: #cbd5e1;
      --border-focus: #0284c7;
      --text-primary: #0f172a;
      --text-secondary: #475569;
      --text-tertiary: #64748b;
      --accent-brass: #b45309;
      --accent-brass-subtle: rgba(180, 83, 9, 0.1);
      --accent-brass-glow: rgba(180, 83, 9, 0.2);
      --accent-ready: #059669;
      --accent-ready-subtle: rgba(5, 150, 105, 0.12);
      --accent-alert: #dc2626;
      --accent-intel: #0284c7;
      --accent-intel-subtle: rgba(2, 132, 199, 0.1);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background-color: var(--bg-base);
      color: var(--text-primary);
      font-family: var(--font-ui);
      font-size: 15px;
      line-height: 1.5;
      min-height: 100vh;
      margin: 0;
      padding: 0;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
      transition: background-color 0.25s ease, color 0.25s ease;
    }}

    /* ==============================================================
       APP LAYOUT & VERTICAL SIDEBAR NAVIGATION
       ============================================================== */
    .app-layout {{
      display: flex;
      width: 100%;
      min-height: 100vh;
      align-items: stretch;
      position: relative;
    }}

    /* VERTICAL SIDEBAR OF TITLES */
    .sidebar-nav {{
      width: 275px;
      min-width: 275px;
      max-width: 275px;
      background: var(--bg-surface);
      border-right: 1px solid var(--border-subtle);
      height: 100vh;
      position: sticky;
      top: 0;
      z-index: 120;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      overflow-x: hidden;
      scrollbar-width: thin;
      scrollbar-color: var(--border-subtle) transparent;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), margin-left 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .sidebar-nav::-webkit-scrollbar {{
      width: 4px;
    }}
    .sidebar-nav::-webkit-scrollbar-thumb {{
      background: var(--border-subtle);
      border-radius: 2px;
    }}

    body.sidebar-collapsed .sidebar-nav {{
      margin-left: -275px;
    }}

    /* SIDEBAR HEADER BRANDING */
    .sidebar-header {{
      padding: 1.15rem 1.15rem 1rem 1.15rem;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--bg-surface);
    }}

    .brand-mark {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      color: inherit;
    }}

    .insignia {{
      background: var(--accent-brass);
      color: #000;
      font-family: var(--font-tactical);
      font-weight: 700;
      font-size: 0.82rem;
      letter-spacing: 1px;
      padding: 0.25rem 0.5rem;
      border-radius: var(--radius-sm);
    }}

    .title-group {{
      display: flex;
      flex-direction: column;
    }}

    .title-group h1 {{
      font-family: var(--font-tactical);
      font-size: 1.22rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      line-height: 1.1;
      text-transform: uppercase;
    }}

    .title-group span {{
      font-size: 0.7rem;
      color: var(--text-tertiary);
      letter-spacing: 0.5px;
    }}

    /* VERTICAL NAVIGATION LIST OF TITLES */
    .nav-vertical-menu {{
      flex: 1;
      padding: 0.65rem 0.6rem;
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
    }}

    .nav-section-title {{
      font-family: var(--font-tactical);
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: var(--text-tertiary);
      padding: 0.75rem 0.65rem 0.25rem 0.65rem;
      user-select: none;
    }}
    .nav-section-title:first-child {{
      padding-top: 0.25rem;
    }}

    .op-tab {{
      width: 100%;
      background: transparent;
      border: 1px solid transparent;
      border-radius: var(--radius-md);
      color: var(--text-secondary);
      font-family: var(--font-tactical);
      font-size: 0.92rem;
      font-weight: 600;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 0.58rem 0.75rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.65rem;
      text-align: left;
      white-space: nowrap;
      transition: color 0.15s ease, background 0.15s ease, border-color 0.15s ease;
      position: relative;
    }}

    .op-tab .tab-indicator {{
      width: 3px;
      height: 16px;
      border-radius: 2px;
      background: transparent;
      transition: background 0.15s ease;
      flex-shrink: 0;
    }}

    .op-tab .tab-label {{
      flex: 1;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .op-tab:hover {{
      background: var(--bg-surface-elevated);
      color: var(--text-primary);
      border-color: var(--border-subtle);
    }}

    .op-tab.active {{
      background: var(--accent-brass-subtle);
      color: var(--accent-brass);
      border-color: rgba(217, 119, 6, 0.3);
      font-weight: 700;
    }}

    .op-tab.active .tab-indicator {{
      background: var(--accent-brass);
    }}

    .op-tab.intel-tab {{
      color: var(--accent-intel);
    }}

    .op-tab.intel-tab:hover {{
      border-color: rgba(56, 189, 248, 0.3);
    }}

    .op-tab.intel-tab.active {{
      background: var(--accent-intel-subtle);
      border-color: rgba(56, 189, 248, 0.35);
    }}

    .op-tab.intel-tab.active .tab-indicator {{
      background: var(--accent-intel);
    }}

    /* SIDEBAR FOOTER */
    .sidebar-footer {{
      padding: 0.85rem 1.15rem;
      border-top: 1px solid var(--border-subtle);
      background: var(--bg-surface);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .sidebar-status {{
      display: flex;
      align-items: center;
      gap: 0.45rem;
      font-size: 0.68rem;
      font-family: var(--font-mono);
      color: var(--text-tertiary);
      letter-spacing: 0.5px;
    }}

    .sidebar-status .status-dot {{
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--accent-ready);
      box-shadow: 0 0 6px var(--accent-ready);
    }}

    /* MAIN VIEWPORT */
    .main-viewport {{
      flex: 1;
      min-width: 0;
      display: flex;
      flex-direction: column;
      min-height: 100vh;
      background: var(--bg-base);
    }}

    /* VIEWPORT TOP CONSOLE HEADER */
    .viewport-header {{
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 0.65rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }}

    .viewport-left {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }}

    .sidebar-toggle-btn {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      width: 32px;
      height: 32px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 1.05rem;
      line-height: 1;
      transition: all 0.15s ease;
    }}
    .sidebar-toggle-btn:hover {{
      color: var(--text-primary);
      border-color: var(--accent-brass);
    }}

    .current-module-tracker {{
      display: flex;
      align-items: center;
      gap: 0.45rem;
      font-family: var(--font-tactical);
      letter-spacing: 0.5px;
    }}

    .current-module-prefix {{
      font-size: 0.75rem;
      color: var(--text-tertiary);
      font-weight: 600;
      text-transform: uppercase;
    }}

    .current-module-name {{
      font-size: 1.05rem;
      color: var(--text-primary);
      font-weight: 700;
      text-transform: uppercase;
    }}

    .console-actions {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .console-btn {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      font-family: var(--font-ui);
      font-size: 0.82rem;
      font-weight: 600;
      padding: 0.42rem 0.8rem;
      border-radius: var(--radius-md);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.15s ease;
    }}

    .console-btn:hover {{
      color: var(--text-primary);
      border-color: var(--text-tertiary);
    }}

    /* MOBILE / RESPONSIVE DRAWER */
    .sidebar-backdrop {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.65);
      z-index: 110;
      opacity: 0;
      transition: opacity 0.25s ease;
    }}

    @media (max-width: 992px) {{
      .sidebar-nav {{
        position: fixed;
        top: 0;
        left: 0;
        height: 100vh;
        transform: translateX(-100%);
        margin-left: 0 !important;
        box-shadow: 4px 0 24px rgba(0,0,0,0.5);
      }}

      .sidebar-nav.open {{
        transform: translateX(0);
      }}

      .sidebar-backdrop.active {{
        display: block;
        opacity: 1;
      }}

      .viewport-header {{
        padding: 0.65rem 1rem;
      }}

      main {{
        padding: 1rem 0.75rem;
      }}
    }}

    /* MAIN VIEWPORT & WORKSPACE */
    main {{
      flex: 1;
      max-width: 1400px;
      width: 100%;
      margin: 0 auto;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
    }}

    .workspace-module {{
      display: none;
      width: 100%;
      animation: moduleEnter 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .workspace-module.active {{
      display: block;
    }}

    @keyframes moduleEnter {{
      from {{ opacity: 0; transform: translateY(4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .command-panel {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      margin: 0 auto;
    }}

    .module-heading {{
      font-family: var(--font-tactical);
      font-size: 1.6rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      color: var(--text-primary);
      margin-bottom: 0.3rem;
    }}

    .module-desc {{
      color: var(--text-secondary);
      font-size: 0.92rem;
      margin-bottom: 1.5rem;
      line-height: 1.5;
      max-width: 760px;
    }}

    .tactical-ribbon {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 0.75rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 1.5rem;
      font-size: 0.85rem;
    }}

    .ribbon-item {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--text-secondary);
    }}

    .ribbon-item strong {{
      color: var(--text-primary);
      font-family: var(--font-mono);
      font-size: 0.85rem;
    }}

    .param-group {{
      margin-bottom: 1.25rem;
    }}

    .param-label {{
      display: block;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-tertiary);
      text-transform: uppercase;
      letter-spacing: 0.6px;
      margin-bottom: 0.4rem;
    }}

    select, input[type="text"], input[type="number"], textarea {{
      width: 100%;
      background: var(--bg-base);
      border: 1px solid var(--border-subtle);
      color: var(--text-primary);
      padding: 0.65rem 0.85rem;
      border-radius: var(--radius-md);
      font-family: var(--font-ui);
      font-size: 0.92rem;
      outline: none;
      transition: border-color 0.15s ease;
    }}

    select:focus, input[type="text"]:focus, textarea:focus {{
      border-color: var(--accent-brass);
    }}

    .grid-duo {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
    }}

    @media (max-width: 768px) {{
      .grid-duo {{
        grid-template-columns: 1fr;
      }}
    }}

    .btn-engage {{
      background: var(--accent-brass);
      color: #05080f;
      border: none;
      font-family: var(--font-tactical);
      font-size: 1.05rem;
      font-weight: 700;
      letter-spacing: 0.75px;
      text-transform: uppercase;
      padding: 0.85rem 1.5rem;
      border-radius: var(--radius-md);
      cursor: pointer;
      width: 100%;
      margin-top: 1rem;
      transition: filter 0.15s ease, transform 0.15s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
    }}

    .btn-engage:hover {{
      filter: brightness(1.1);
      transform: translateY(-1px);
    }}

    .btn-aux {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-primary);
      font-family: var(--font-ui);
      font-size: 0.85rem;
      font-weight: 600;
      padding: 0.55rem 1rem;
      border-radius: var(--radius-md);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.15s ease;
    }}

    .btn-aux:hover {{
      border-color: var(--text-tertiary);
    }}

    .format-selector {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.75rem;
      margin-bottom: 1.25rem;
    }}

    .format-card {{
      border: 1px solid var(--border-subtle);
      background: var(--bg-base);
      border-radius: var(--radius-md);
      padding: 0.85rem 1rem;
      cursor: pointer;
      transition: border-color 0.15s, background-color 0.15s;
    }}

    .format-card.selected {{
      border-color: var(--accent-brass);
      background: var(--accent-brass-subtle);
    }}

    .format-card strong {{
      display: block;
      font-size: 0.95rem;
      font-family: var(--font-tactical);
      letter-spacing: 0.5px;
      margin-bottom: 0.2rem;
    }}

    .format-card span {{
      font-size: 0.8rem;
      color: var(--text-secondary);
      line-height: 1.4;
      display: block;
    }}

    /* TESTING THEATER (WAT) */
    .theater-canvas {{
      background: #020408;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 2.5rem 1.5rem;
      min-height: 340px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
      box-shadow: inset 0 0 80px rgba(0, 0, 0, 0.7);
    }}

    body.projector-hall .theater-canvas {{
      background: #060911;
      border-color: #0f172a;
    }}

    .stimulus-word {{
      font-family: var(--font-tactical);
      font-size: clamp(3rem, 9vw, 5.8rem);
      font-weight: 700;
      letter-spacing: 4px;
      color: #ffffff;
      text-transform: uppercase;
      text-align: center;
      user-select: none;
      animation: stimulusPop 0.18s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    @keyframes stimulusPop {{
      from {{ transform: scale(0.96); opacity: 0; }}
      to {{ transform: scale(1); opacity: 1; }}
    }}

    .pace-meter-bar {{
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 4px;
      background: rgba(255, 255, 255, 0.08);
    }}

    .pace-meter-fill {{
      height: 100%;
      background: var(--accent-brass);
      transition: width 0.1s linear;
    }}

    .precision-clock {{
      width: 72px;
      height: 72px;
      position: relative;
    }}

    .clock-svg {{
      width: 100%;
      height: 100%;
      transform: rotate(-90deg);
    }}

    .clock-track {{
      fill: none;
      stroke: var(--border-subtle);
      stroke-width: 5;
    }}

    .clock-fill {{
      fill: none;
      stroke: var(--accent-brass);
      stroke-width: 5;
      stroke-linecap: round;
      stroke-dasharray: 226;
      stroke-dashoffset: 0;
      transition: stroke-dashoffset 0.1s linear;
    }}

    .clock-digits {{
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      font-family: var(--font-tactical);
      font-size: 1.6rem;
      font-weight: 700;
      color: var(--text-primary);
    }}

    /* TAT OBSERVATION FRAME */
    .tat-observation-frame {{
      background: #020408;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      min-height: 480px;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      position: relative;
    }}

    .tat-observation-frame img {{
      max-width: 100%;
      max-height: 460px;
      object-fit: contain;
      box-shadow: 0 4px 24px rgba(0,0,0,0.6);
    }}

    .phase-pill {{
      font-family: var(--font-tactical);
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      padding: 0.25rem 0.75rem;
      border-radius: var(--radius-sm);
      display: inline-block;
    }}
    .phase-pill.observe {{
      background: var(--accent-intel-subtle);
      border: 1px solid var(--accent-intel);
      color: var(--accent-intel);
    }}
    .phase-pill.write {{
      background: var(--accent-ready-subtle);
      border: 1px solid var(--accent-ready);
      color: var(--accent-ready);
    }}

    /* SRT LOG BOOKLET */
    .srt-scroll-deck {{
      display: flex;
      flex-direction: column;
      gap: 1rem;
      max-height: calc(100vh - 280px);
      overflow-y: auto;
      padding-right: 0.5rem;
    }}

    .srt-entry {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.15rem 1.25rem;
      transition: border-color 0.15s;
    }}
    .srt-entry:focus-within {{
      border-color: var(--accent-brass);
    }}

    .srt-num {{
      font-family: var(--font-tactical);
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--accent-brass);
      margin-right: 0.5rem;
    }}

    .srt-situation-text {{
      font-size: 0.98rem;
      font-weight: 500;
      line-height: 1.5;
      margin-bottom: 0.75rem;
    }}

    /* DIGITAL OMR */
    .omr-grid-scroll {{
      flex: 1;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
      padding-right: 0.4rem;
    }}

    .omr-line {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.4rem 0.75rem;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
    }}

    .omr-num {{
      font-family: var(--font-mono);
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-tertiary);
      width: 28px;
    }}

    .bubble-cluster {{
      display: flex;
      gap: 0.5rem;
    }}

    .omr-bubble-cell {{
      width: 28px;
      height: 28px;
      border-radius: 50%;
      border: 1px solid var(--border-subtle);
      background: var(--bg-base);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-tactical);
      font-weight: 700;
      font-size: 0.85rem;
      cursor: pointer;
      user-select: none;
      transition: all 0.15s ease;
    }}

    .omr-bubble-cell:hover {{
      border-color: var(--accent-brass);
    }}

    .omr-bubble-cell.filled {{
      background: var(--accent-brass);
      color: #000;
      border-color: var(--accent-brass);
    }}

    /* GROUP DISCUSSION (GD) SYNDICATE DECK */
    .gd-roster {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 0.75rem;
      margin-bottom: 1.5rem;
    }}

    @media (max-width: 768px) {{
      .gd-roster {{
        grid-template-columns: repeat(3, 1fr);
      }}
    }}

    .syndicate-avatar {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 0.85rem 0.5rem;
      text-align: center;
      position: relative;
      transition: all 0.2s ease;
    }}

    .syndicate-avatar.speaking {{
      border-color: var(--accent-brass);
      box-shadow: 0 0 16px var(--accent-brass-glow);
    }}

    .syndicate-avatar.you {{
      border-color: var(--accent-intel);
    }}
    .syndicate-avatar.you.speaking {{
      border-color: var(--accent-ready);
      box-shadow: 0 0 16px rgba(16, 185, 129, 0.35);
    }}

    .avatar-chest {{
      font-family: var(--font-tactical);
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-primary);
      display: block;
    }}

    .avatar-archetype {{
      font-size: 0.72rem;
      color: var(--text-tertiary);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-top: 0.15rem;
      display: block;
    }}

    .avatar-status {{
      display: inline-block;
      font-size: 0.7rem;
      font-weight: 600;
      padding: 0.1rem 0.4rem;
      border-radius: var(--radius-sm);
      margin-top: 0.4rem;
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-secondary);
    }}
    .syndicate-avatar.speaking .avatar-status {{
      background: var(--accent-brass);
      color: #000;
    }}
    .syndicate-avatar.you.speaking .avatar-status {{
      background: var(--accent-ready);
      color: #000;
    }}

    .gd-leads-banner {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.15rem;
      margin-bottom: 1.25rem;
    }}

    .leads-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.75rem;
      margin-top: 0.75rem;
    }}

    @media (max-width: 768px) {{
      .leads-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .lead-box {{
      background: var(--bg-base);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 0.75rem;
      font-size: 0.85rem;
      line-height: 1.4;
      color: var(--text-secondary);
      transition: all 0.2s ease;
    }}

    .lead-box.active {{
      border-color: var(--accent-brass);
      color: var(--text-primary);
      background: var(--accent-brass-subtle);
    }}

    .gd-feed {{
      height: 280px;
      overflow-y: auto;
      background: var(--bg-base);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      margin-bottom: 1.25rem;
    }}

    .feed-entry {{
      padding: 0.65rem 0.85rem;
      border-radius: var(--radius-sm);
      background: var(--bg-surface-elevated);
      border-left: 3px solid var(--border-subtle);
      font-size: 0.88rem;
      line-height: 1.45;
    }}
    .feed-entry.you {{
      border-left-color: var(--accent-ready);
      background: rgba(16, 185, 129, 0.08);
    }}
    .feed-entry.peer {{
      border-left-color: var(--accent-brass);
    }}

    .feed-meta {{
      font-family: var(--font-tactical);
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--accent-brass);
      margin-bottom: 0.2rem;
      display: flex;
      justify-content: space-between;
    }}
    .feed-entry.you .feed-meta {{
      color: var(--accent-ready);
    }}

    .airtime-bar-wrap {{
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-bottom: 1.25rem;
    }}

    /* LECTURETTE CUE CARD & STAGE */
    .lecturette-card {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      max-width: 680px;
      margin: 0 auto 1.5rem auto;
      box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }}

    .topic-tier-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.85rem 1rem;
      border-radius: var(--radius-md);
      background: var(--bg-base);
      border: 1px solid var(--border-subtle);
      margin-bottom: 0.75rem;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .topic-tier-row:hover {{
      border-color: var(--accent-brass);
    }}
    .topic-tier-row.selected {{
      border-color: var(--accent-brass);
      background: var(--accent-brass-subtle);
    }}

    .tier-tag {{
      font-family: var(--font-tactical);
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 0.15rem 0.5rem;
      border-radius: var(--radius-sm);
    }}
    .tier-1 {{ background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid #ef4444; }}
    .tier-2 {{ background: rgba(217, 119, 6, 0.15); color: #fbbf24; border: 1px solid #d97706; }}
    .tier-3 {{ background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid #38bdf8; }}
    .tier-4 {{ background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid #10b981; }}

    .posture-mirror-video {{
      width: 100%;
      max-width: 380px;
      height: 240px;
      object-fit: cover;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-subtle);
      background: #000;
      transform: scaleX(-1); /* Mirror view */
    }}

    /* EVALUATION DISPATCH CARD */
    .eval-dispatch-card {{
      background: var(--accent-intel-subtle);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: var(--radius-lg);
      padding: 1.35rem;
      margin-bottom: 1.5rem;
    }}

    .dispatch-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 1rem;
      flex-wrap: wrap;
    }}

    .dispatch-title {{
      font-family: var(--font-tactical);
      font-size: 1.2rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      color: var(--accent-intel);
      text-transform: uppercase;
    }}

    .dispatch-desc {{
      font-size: 0.88rem;
      color: var(--text-secondary);
      margin-top: 0.35rem;
      max-width: 640px;
      line-height: 1.45;
    }}

    .dispatch-actions {{
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}

    .model-links-row {{
      margin-top: 1rem;
      padding-top: 0.75rem;
      border-top: 1px solid rgba(56, 189, 248, 0.2);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.6rem;
    }}

    .model-chip {{
      display: inline-flex;
      align-items: center;
      padding: 0.4rem 0.75rem;
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
      font-weight: 600;
      text-decoration: none;
      transition: opacity 0.15s, transform 0.15s;
    }}
    .model-chip:hover {{
      opacity: 0.9;
      transform: translateY(-1px);
    }}
    .chip-chatgpt {{ background: rgba(16, 185, 129, 0.15); border: 1px solid var(--accent-ready); color: var(--accent-ready); }}
    .chip-claude {{ background: rgba(217, 119, 6, 0.15); border: 1px solid #d97706; color: #fbbf24; }}
    .chip-gemini {{ background: rgba(56, 189, 248, 0.15); border: 1px solid var(--accent-intel); color: var(--accent-intel); }}

    /* PROGRESS & MASTERY METRICS */
    .metric-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      margin-bottom: 2rem;
    }}

    .metric-slate {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.15rem 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }}

    .metric-label {{
      font-size: 0.78rem;
      color: var(--text-tertiary);
      text-transform: uppercase;
      font-weight: 600;
      letter-spacing: 0.5px;
    }}

    .metric-digit {{
      font-family: var(--font-tactical);
      font-size: 2rem;
      font-weight: 700;
      color: var(--text-primary);
      line-height: 1;
    }}

    .metric-bar-bg {{
      width: 100%;
      height: 4px;
      background: var(--bg-base);
      border-radius: 2px;
      overflow: hidden;
      margin-top: 0.25rem;
    }}

    .metric-bar-fill {{
      height: 100%;
      background: var(--accent-brass);
      border-radius: 2px;
      transition: width 0.3s ease;
    }}

    .pill-grid {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.45rem;
      margin-top: 0.6rem;
    }}

    .inventory-pill {{
      padding: 0.35rem 0.7rem;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-subtle);
      background: var(--bg-surface-elevated);
      font-size: 0.8rem;
      font-family: var(--font-mono);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.15s ease;
    }}

    .inventory-pill:hover {{
      border-color: var(--accent-brass);
      color: var(--accent-brass);
    }}

    .inventory-pill.cleared {{
      border-color: var(--accent-ready);
      background: var(--accent-ready-subtle);
      color: var(--accent-ready);
    }}

    #tacticalToast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--accent-brass);
      color: #000;
      padding: 0.65rem 1.15rem;
      border-radius: var(--radius-md);
      font-family: var(--font-tactical);
      font-size: 1rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      box-shadow: 0 4px 16px rgba(0,0,0,0.5);
      z-index: 9999;
      opacity: 0;
      transform: translateY(8px);
      transition: opacity 0.2s, transform 0.2s;
      pointer-events: none;
    }}
    #tacticalToast.visible {{
      opacity: 1;
      transform: translateY(0);
    }}
  </style>
</head>
<body>

  <!-- TOAST NOTIFICATION -->
  <div id="tacticalToast">DISPATCH COPIED TO CLIPBOARD</div>

  <div class="app-layout">
    <!-- VERTICAL SIDEBAR NAVIGATION OF TITLES -->
    <aside class="sidebar-nav" id="sidebarNav">
      <div class="sidebar-header">
        <div class="brand-mark">
          <span class="insignia">DIPR</span>
          <div class="title-group">
            <h1>SSB Master Suite</h1>
            <span>Psychology &amp; GTO Console</span>
          </div>
        </div>
      </div>

      <!-- VERTICAL NAVIGATION TRACK -->
      <nav class="nav-vertical-menu" aria-label="Testing Modules">
        <div class="nav-section-title">COMMAND &amp; PERFORMANCE</div>
        <button class="op-tab active" data-tab="tab-progress">
          <span class="tab-indicator"></span>
          <span class="tab-label">Mission Mastery</span>
        </button>

        <div class="nav-section-title">STAGE I (SCREENING)</div>
        <button class="op-tab" data-tab="tab-oir">
          <span class="tab-indicator"></span>
          <span class="tab-label">OIR (OMR Console)</span>
        </button>

        <div class="nav-section-title">STAGE II (PSYCHOLOGICAL BATTERY)</div>
        <button class="op-tab" data-tab="tab-wat">
          <span class="tab-indicator"></span>
          <span class="tab-label">WAT (60 Words)</span>
        </button>
        <button class="op-tab" data-tab="tab-tat">
          <span class="tab-indicator"></span>
          <span class="tab-label">TAT (12 Slides)</span>
        </button>
        <button class="op-tab" data-tab="tab-srt">
          <span class="tab-indicator"></span>
          <span class="tab-label">SRT (60 Scenarios)</span>
        </button>
        <button class="op-tab" data-tab="tab-sdt">
          <span class="tab-indicator"></span>
          <span class="tab-label">SDT (Self Description)</span>
        </button>

        <div class="nav-section-title">STAGE II (GTO VERBAL ARENA)</div>
        <button class="op-tab" data-tab="tab-gd">
          <span class="tab-indicator"></span>
          <span class="tab-label">Group Discussion (GD)</span>
        </button>
        <button class="op-tab" data-tab="tab-lecturette">
          <span class="tab-indicator"></span>
          <span class="tab-label">Lecturette (250+ Topics)</span>
        </button>

        <div class="nav-section-title">SIMULATION &amp; EVALUATION</div>
        <button class="op-tab" data-tab="tab-fullmock">
          <span class="tab-indicator"></span>
          <span class="tab-label">Full Mock Battery</span>
        </button>
        <button class="op-tab intel-tab" data-tab="tab-ai-assessor">
          <span class="tab-indicator"></span>
          <span class="tab-label">AI Evaluation Dispatch</span>
        </button>
      </nav>

      <div class="sidebar-footer">
        <div class="sidebar-status">
          <span class="status-dot"></span>
          <span>STANDALONE CLIENT READY</span>
        </div>
      </div>
    </aside>

    <!-- BACKDROP FOR MOBILE DRAWER -->
    <div class="sidebar-backdrop" id="sidebarBackdrop"></div>

    <!-- MAIN VIEWPORT -->
    <div class="main-viewport">
      <!-- VIEWPORT TOP BAR -->
      <header class="viewport-header">
        <div class="viewport-left">
          <button class="sidebar-toggle-btn" id="btnToggleSidebar" title="Toggle Navigation Sidebar">
            ☰
          </button>
          <div class="current-module-tracker">
            <span class="current-module-prefix">MODULE /</span>
            <span class="current-module-name" id="currentModuleLabel">Mission Mastery</span>
          </div>
        </div>
        <div class="console-actions">
          <button class="console-btn" id="btnToggleTheme" title="Toggle Daylight Projector / Dark Hall">
            <span id="themeLabel">Projector Hall</span>
          </button>
          <button class="console-btn" id="btnToggleFullscreen" title="Fullscreen Mode">
            Fullscreen
          </button>
        </div>
      </header>

      <!-- MAIN WORKSPACE -->
      <main>

    <!-- ==============================================================
         0. MISSION MASTERY (DO NOT REPEAT ENGINE)
         ============================================================== -->
    <section class="workspace-module active" id="tab-progress">
      <div class="command-panel" style="max-width: 1040px;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid var(--border-subtle); padding-bottom: 1.25rem; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
          <div>
            <h2 class="module-heading">Preparation & Performance Tracker</h2>
            <p class="module-desc" style="margin-bottom: 0;">
              Zero-repeat operational control. Track psychological tests, OIR sets, and GTO verbal drills systematically.
            </p>
          </div>
          <div style="display: flex; gap: 0.5rem;">
            <button class="btn-aux" onclick="exportProgressJSON()">Backup Progress</button>
            <input type="file" id="importProgressInput" accept=".json" style="display: none;">
            <button class="btn-aux" onclick="document.getElementById('importProgressInput').click()">Restore Progress</button>
          </div>
        </div>

        <!-- METRIC CARDS -->
        <div class="metric-grid">
          <div class="metric-slate">
            <span class="metric-label">WAT Syllabus (21 Sets)</span>
            <div class="metric-digit" id="progWatVal">0 / 21</div>
            <div class="metric-bar-bg"><div class="metric-bar-fill" id="progWatBar" style="width: 0%;"></div></div>
          </div>
          <div class="metric-slate">
            <span class="metric-label">TAT Syllabus (12 Sets)</span>
            <div class="metric-digit" id="progTatVal" style="color: var(--accent-intel);">0 / 12</div>
            <div class="metric-bar-bg"><div class="metric-bar-fill" id="progTatBar" style="width: 0%; background: var(--accent-intel);"></div></div>
          </div>
          <div class="metric-slate">
            <span class="metric-label">SRT Syllabus (2 Sets)</span>
            <div class="metric-digit" id="progSrtVal" style="color: var(--accent-ready);">0 / 2</div>
            <div class="metric-bar-bg"><div class="metric-bar-fill" id="progSrtBar" style="width: 0%; background: var(--accent-ready);"></div></div>
          </div>
          <div class="metric-slate">
            <span class="metric-label">GD Sessions Completed</span>
            <div class="metric-digit" id="progGdVal" style="color: var(--accent-brass);">0</div>
            <span style="font-size: 0.75rem; color: var(--text-tertiary);">Simulated syndicate drills</span>
          </div>
          <div class="metric-slate">
            <span class="metric-label">Lecturettes Delivered</span>
            <div class="metric-digit" id="progLecVal" style="color: #a855f7;">0</div>
            <span style="font-size: 0.75rem; color: var(--text-tertiary);">From 250+ topic bank</span>
          </div>
        </div>

        <!-- RECOMMENDED NEXT ACTION -->
        <div style="background: var(--accent-brass-subtle); border: 1px solid var(--accent-brass); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
          <div>
            <strong style="font-family: var(--font-tactical); font-size: 1.1rem; color: var(--accent-brass); letter-spacing: 0.5px; text-transform: uppercase;">
              Recommended Next Objective:
            </strong>
            <div style="color: var(--text-primary); font-size: 0.95rem; margin-top: 0.25rem;" id="nextRecText">
              Scanning unattempted sets...
            </div>
          </div>
          <button class="btn-engage" style="width: auto; margin-top: 0; padding: 0.65rem 1.75rem; font-size: 0.95rem;" id="btnLaunchNextRec">
            Launch Set
          </button>
        </div>

        <!-- SETS INVENTORY GRID -->
        <div style="display: flex; flex-direction: column; gap: 1.75rem;">
          <div>
            <strong style="font-family: var(--font-tactical); font-size: 1.05rem; letter-spacing: 0.5px; color: var(--accent-brass); text-transform: uppercase;">
              Word Association Test Sets (WAT 1 to 21)
            </strong>
            <div class="pill-grid" id="pillsWat"></div>
          </div>

          <div>
            <strong style="font-family: var(--font-tactical); font-size: 1.05rem; letter-spacing: 0.5px; color: var(--accent-intel); text-transform: uppercase;">
              Thematic Apperception Test Sets (TAT 1 to 12)
            </strong>
            <div class="pill-grid" id="pillsTat"></div>
          </div>

          <div>
            <strong style="font-family: var(--font-tactical); font-size: 1.05rem; letter-spacing: 0.5px; color: var(--accent-ready); text-transform: uppercase;">
              Situation Reaction Test Sets (SRT 1 and 2)
            </strong>
            <div class="pill-grid" id="pillsSrt"></div>
          </div>
        </div>

        <!-- SESSION HISTORY -->
        <div style="margin-top: 2.5rem; border-top: 1px solid var(--border-subtle); padding-top: 1.5rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <strong style="font-family: var(--font-tactical); font-size: 1.1rem; letter-spacing: 0.5px; text-transform: uppercase;">Operation Log</strong>
            <button class="btn-aux" style="font-size: 0.78rem; padding: 0.3rem 0.6rem; color: var(--accent-alert);" onclick="clearPracticeHistory()">Clear History</button>
          </div>
          <div style="max-height: 260px; overflow-y: auto; border: 1px solid var(--border-subtle); border-radius: var(--radius-md);">
            <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.85rem;">
              <thead>
                <tr style="background: var(--bg-surface-elevated); color: var(--accent-brass); font-family: var(--font-tactical); font-size: 0.9rem; letter-spacing: 0.5px; text-transform: uppercase;">
                  <th style="padding: 0.6rem 1rem;">Timestamp</th>
                  <th style="padding: 0.6rem 1rem;">Module</th>
                  <th style="padding: 0.6rem 1rem;">Set / Item</th>
                  <th style="padding: 0.6rem 1rem;">Status</th>
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
    <section class="workspace-module" id="tab-wat">
      <div class="command-panel" id="watSetupScreen" style="max-width: 860px;">
        <h2 class="module-heading">Word Association Test (WAT)</h2>
        <p class="module-desc">
          60 Stimulus words projected at 15-second intervals. Project immediate, positive, action-driven thoughts reflecting your natural subconscious qualities.
        </p>

        <div class="tactical-ribbon">
          <div class="ribbon-item">Repository: <strong>21 Sets ({len(all_wat_words)} Words)</strong></div>
          <div class="ribbon-item">Interval: <strong>15 Seconds / Word</strong></div>
        </div>

        <div class="param-group">
          <label class="param-label">Select Practice Set</label>
          <select id="watSelectSet">
            <option value="next_unattempted" selected>Next Unattempted Set (No Repeat Guarantee)</option>
            <option value="random_60">Random 60 Words (Full Board Simulation)</option>
            <option value="random_30">Rapid 30 Words Drill</option>
            <optgroup label="── OFFICIAL DIPR 60-WORD SETS ──" id="watOptGroupSets">
'''

for s in wat_sets:
    html += f'              <option value="set_{s["id"]}">Set {s["id"]} ({s["count"]} Words: {s["preview"]})</option>\n'

html += f'''            </optgroup>
            <optgroup label="── MARATHON ──">
              <option value="all">Complete Repository ({len(all_wat_words)} Words)</option>
            </optgroup>
          </select>
        </div>

        <div class="grid-duo">
          <div class="param-group">
            <label class="param-label">Cadence Pace</label>
            <select id="watSelectDuration">
              <option value="15" selected>15 Seconds (Official DIPR Standard)</option>
              <option value="12">12 Seconds (Stress Induction)</option>
              <option value="10">10 Seconds (High Speed)</option>
              <option value="18">18 Seconds (Training Cadence)</option>
            </select>
          </div>
          <div class="param-group">
            <label class="param-label">Order</label>
            <select id="watSelectOrder">
              <option value="sequential" selected>Original Order</option>
              <option value="shuffle">Shuffled</option>
            </select>
          </div>
        </div>

        <div class="param-group">
          <label class="param-label">Practice Style</label>
          <div class="format-selector">
            <div class="format-card selected" id="watModePaper" onclick="setWatMode('paper')">
              <strong>Pen & Paper (Recommended)</strong>
              <span>Replicates real SSB board condition. Write responses in a physical notebook as words flash.</span>
            </div>
            <div class="format-card" id="watModeTyping" onclick="setWatMode('typing')">
              <strong>Digital Typing</strong>
              <span>Type your response directly into the on-screen input field during the 15-second window.</span>
            </div>
          </div>
        </div>

        <button class="btn-engage" onclick="startWatTest()">Commence WAT Drill</button>
      </div>

      <!-- WAT ACTIVE TEST THEATER -->
      <div class="command-panel" id="watActiveScreen" style="display: none; max-width: 920px; padding: 2rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: 2rem;">
          <div style="font-family: var(--font-tactical); font-size: 1.4rem; font-weight: 700; color: var(--accent-brass);" id="watProgressTag">
            WORD 1 / 60
          </div>
          <div class="precision-clock">
            <svg class="clock-svg" viewBox="0 0 80 80">
              <circle class="clock-track" cx="40" cy="40" r="36" />
              <circle class="clock-fill" id="watTimerCircle" cx="40" cy="40" r="36" />
            </svg>
            <div class="clock-digits" id="watTimerNum">15</div>
          </div>
        </div>

        <div class="theater-canvas">
          <div class="stimulus-word" id="watFlashedWord">LEADER</div>
          <div class="pace-meter-bar">
            <div class="pace-meter-fill" id="watLinearBar"></div>
          </div>
        </div>

        <div id="watTypingArea" style="width: 100%; margin-top: 1.5rem; display: none;">
          <input type="text" id="watInput" style="padding: 0.9rem; font-size: 1.1rem;" placeholder="Type spontaneous response here..." autocomplete="off">
        </div>

        <div style="display: flex; gap: 0.75rem; margin-top: 2rem; justify-content: center; flex-wrap: wrap;">
          <button class="btn-aux" onclick="toggleWatPause()"><span id="watPauseLabel">Pause</span></button>
          <button class="btn-aux" onclick="nextWatWord()">Next Word</button>
          <button class="btn-aux" style="color: var(--accent-alert);" onclick="abortWatTest()">Abort Test</button>
        </div>
      </div>

      <!-- WAT REVIEW SCREEN -->
      <div class="command-panel" id="watReviewScreen" style="display: none; max-width: 960px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <h2 class="module-heading">WAT Drill Completed</h2>
            <p class="module-desc" style="margin-bottom: 0;">Review your stimulus responses and evaluate with AI for free.</p>
          </div>
          <button class="btn-aux" onclick="copyWatResponses()">Copy Raw Words</button>
        </div>

        <div class="eval-dispatch-card">
          <div class="dispatch-header">
            <div>
              <div class="dispatch-title">
                AI Psychologist Evaluation (ChatGPT / Claude / Gemini)
              </div>
              <p class="dispatch-desc">
                Evaluate your responses using an AI prompted as a <strong>Senior DIPR Psychologist</strong>. It checks against the 15 OLQs, flags preaching (e.g. <em>'should/must'</em>), and provides concise, officer-grade model answers.
              </p>
            </div>
            <div class="dispatch-actions">
              <button class="btn-engage" style="width: auto; margin-top: 0; padding: 0.55rem 1.25rem; font-size: 0.9rem; background: var(--accent-intel);" onclick="copyWatAiPrompt()">Copy AI Assessor Prompt</button>
              <button class="btn-aux" onclick="downloadWatAiDossier()">Download Dossier</button>
            </div>
          </div>
          <div class="model-links-row">
            <span style="font-size: 0.8rem; color: var(--text-tertiary);">Step 2: Paste prompt into your chosen chat model:</span>
            <div style="display: flex; gap: 0.5rem;">
              <a href="https://chatgpt.com" target="_blank" class="model-chip chip-chatgpt">ChatGPT ↗</a>
              <a href="https://claude.ai" target="_blank" class="model-chip chip-claude">Claude ↗</a>
              <a href="https://gemini.google.com" target="_blank" class="model-chip chip-gemini">Gemini ↗</a>
            </div>
          </div>
        </div>

        <div style="max-height: 480px; overflow-y: auto; border: 1px solid var(--border-subtle); border-radius: var(--radius-md); margin-bottom: 1.5rem;">
          <table style="width: 100%; border-collapse: collapse; text-align: left;">
            <thead>
              <tr style="background: var(--bg-surface-elevated); color: var(--accent-brass); font-family: var(--font-tactical); font-size: 0.88rem; text-transform: uppercase;">
                <th style="padding: 0.75rem 1rem;">#</th>
                <th style="padding: 0.75rem 1rem;">Stimulus Word</th>
                <th style="padding: 0.75rem 1rem;">Candidate Response</th>
              </tr>
            </thead>
            <tbody id="watReviewTbody"></tbody>
          </table>
        </div>
        <button class="btn-aux" onclick="resetWatToSetup()">Return to Setup</button>
      </div>
    </section>

    <!-- ==============================================================
         2. TAT MODULE
         ============================================================== -->
    <section class="workspace-module" id="tab-tat">
      <div class="command-panel" id="tatSetupScreen" style="max-width: 860px;">
        <h2 class="module-heading">Thematic Apperception Test (TAT)</h2>
        <p class="module-desc">
          12 Slides (11 authentic visual stimuli + 1 blank slide). 30 seconds observation followed by 4 minutes story writing per slide.
        </p>

        <div class="tactical-ribbon">
          <div class="ribbon-item">Slide Imagery: <strong>137 Authentic DIPR Plates</strong></div>
          <div class="ribbon-item">Syllabus: <strong>12 Official Sets (12 Slides Each)</strong></div>
        </div>

        <div class="param-group">
          <label class="param-label">Select TAT Set</label>
          <select id="tatSelectSet">
            <option value="next_unattempted" selected>Next Unattempted Set (No Repeat Guarantee)</option>
            <option value="random_11">Random 11 Pictures + Slide 12 Blank</option>
            <optgroup label="── OFFICIAL 12-SLIDE SETS ──" id="tatOptGroupSets">
'''

for s in tat_sets:
    html += f'              <option value="tat_set_{s["id"]}">{s["title"]} ({s["desc"]})</option>\n'

html += f'''            </optgroup>
          </select>
        </div>

        <div class="grid-duo">
          <div class="param-group">
            <label class="param-label">Observation Window (Image on Screen)</label>
            <select id="tatViewTime">
              <option value="30" selected>30 Seconds (Official DIPR Standard)</option>
              <option value="20">20 Seconds (High Speed Perception)</option>
              <option value="45">45 Seconds (Training Cadence)</option>
            </select>
          </div>
          <div class="param-group">
            <label class="param-label">Narrative Window (Story Writing)</label>
            <select id="tatWriteTime">
              <option value="240" selected>4 Minutes (Official DIPR Standard)</option>
              <option value="180">3 Minutes (Speed Drill)</option>
              <option value="300">5 Minutes (Training Cadence)</option>
            </select>
          </div>
        </div>

        <div class="param-group">
          <label class="param-label">Practice Style</label>
          <div class="format-selector">
            <div class="format-card selected" id="tatModePaper" onclick="setTatMode('paper')">
              <strong>Pen & Paper (Recommended)</strong>
              <span>Observe the visual stimuli on screen and write your 12 narratives in your physical booklet.</span>
            </div>
            <div class="format-card" id="tatModeTyping" onclick="setTatMode('typing')">
              <strong>Digital Typing</strong>
              <span>Type your story directly into the on-screen narrative editor during the 4-minute writing phase.</span>
            </div>
          </div>
        </div>

        <button class="btn-engage" onclick="startTatTest()">Commence TAT Drill</button>
      </div>

      <!-- TAT ACTIVE STAGE -->
      <div class="command-panel" id="tatActiveScreen" style="display: none; max-width: 960px; padding: 2rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: 1.5rem;">
          <div>
            <div style="font-family: var(--font-tactical); font-size: 1.4rem; font-weight: 700; color: var(--accent-brass);" id="tatSlideTag">
              SLIDE 1 / 12
            </div>
            <div style="margin-top: 0.25rem;">
              <span class="phase-pill observe" id="tatPhaseBadge">Observation Phase (30s)</span>
            </div>
          </div>

          <div class="precision-clock">
            <svg class="clock-svg" viewBox="0 0 80 80">
              <circle class="clock-track" cx="40" cy="40" r="36" />
              <circle class="clock-fill" id="tatTimerCircle" cx="40" cy="40" r="36" />
            </svg>
            <div class="clock-digits" id="tatTimerNum">30</div>
          </div>
        </div>

        <div class="tat-observation-frame" id="tatDisplayCard">
          <div id="tatImgWrap" style="display: flex; justify-content: center; align-items: center; width: 100%; height: 100%;">
            <img id="tatCurrentImg" src="" alt="TAT Stimulus">
          </div>
          <div id="tatBlankSlide" style="display: none; text-align: center; padding: 2rem;">
            <h2 style="font-family: var(--font-tactical); font-size: 2.8rem; color: var(--accent-brass); margin-bottom: 0.5rem;">BLANK SLIDE (12 / 12)</h2>
            <p style="color: var(--text-secondary); max-width: 580px; margin: 0 auto; line-height: 1.6;">
              This is the 12th Slide. Create a story of your own choice depicting constructive initiative, community leadership, adventure, or personal goals.
            </p>
          </div>
          <div id="tatWritingPrompt" style="display: none; text-align: center; padding: 2rem;">
            <h3 style="font-family: var(--font-tactical); font-size: 2.2rem; color: var(--accent-ready); margin-bottom: 0.4rem;">NARRATIVE PHASE</h3>
            <p style="color: var(--text-secondary); font-size: 0.95rem;">
              Synthesize past context (what led to it), active present measures, and a realistic positive resolution.
            </p>
          </div>
        </div>

        <div id="tatTypingContainer" style="display: none; width: 100%; margin-top: 1.5rem;">
          <textarea id="tatStoryInput" style="height: 160px;" placeholder="Type your narrative here (Hero identification, situation, action taken, constructive outcome)..."></textarea>
        </div>

        <div style="display: flex; gap: 0.75rem; margin-top: 1.5rem; justify-content: center; flex-wrap: wrap;">
          <button class="btn-aux" onclick="toggleTatPause()"><span id="tatPauseLabel">Pause</span></button>
          <button class="btn-aux" style="border-color: var(--accent-ready); color: var(--accent-ready);" onclick="advanceTatPhaseEarly()">
            Finished Writing — Next Slide
          </button>
          <button class="btn-aux" style="color: var(--accent-alert);" onclick="abortTatTest()">Abort Test</button>
        </div>
      </div>

      <!-- TAT REVIEW SCREEN -->
      <div class="command-panel" id="tatReviewScreen" style="display: none; max-width: 960px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <h2 class="module-heading">TAT Session Completed</h2>
            <p class="module-desc" style="margin-bottom: 0;">12 Slides recorded. Ready for multimodal AI assessment.</p>
          </div>
          <button class="btn-aux" onclick="copyTatResponses()">Copy Raw Stories</button>
        </div>

        <div class="eval-dispatch-card">
          <div class="dispatch-header">
            <div>
              <div class="dispatch-title">
                Multimodal TAT Evaluation (Images + Stories)
              </div>
              <p class="dispatch-desc">
                Download the package containing all <strong>slide picture images (.jpg) + your stories + the Senior DIPR Assessor Prompt</strong>. Upload them directly into ChatGPT-4o, Claude 3.5, or Gemini to evaluate how well your Hero and Action match the visual stimulus and the 15 OLQs!
              </p>
            </div>
            <div class="dispatch-actions">
              <button class="btn-engage" id="btnDownloadTatZip" style="width: auto; margin-top: 0; padding: 0.55rem 1.25rem; font-size: 0.9rem;" onclick="downloadTatZipPackage()">
                Download Package (ZIP: Images + Prompt)
              </button>
              <button class="btn-aux" onclick="copyTatAiPrompt()">Copy Prompt</button>
              <button class="btn-aux" onclick="downloadTatAiDossier()">Download Text</button>
            </div>
          </div>
          <div class="model-links-row">
            <span style="font-size: 0.8rem; color: var(--text-tertiary);">Step 2: Upload images & prompt to free AI chat:</span>
            <div style="display: flex; gap: 0.5rem;">
              <a href="https://chatgpt.com" target="_blank" class="model-chip chip-chatgpt">ChatGPT ↗</a>
              <a href="https://claude.ai" target="_blank" class="model-chip chip-claude">Claude ↗</a>
              <a href="https://gemini.google.com" target="_blank" class="model-chip chip-gemini">Gemini ↗</a>
            </div>
          </div>
        </div>

        <div id="tatReviewList" style="max-height: 520px; overflow-y: auto; display: flex; flex-direction: column; gap: 1rem; margin-bottom: 1.5rem;"></div>
        <button class="btn-aux" onclick="resetTatToSetup()">Return to Setup</button>
      </div>
    </section>

    <!-- ==============================================================
         3. SRT MODULE
         ============================================================== -->
    <section class="workspace-module" id="tab-srt">
      <div class="command-panel" id="srtSetupScreen" style="max-width: 860px;">
        <h2 class="module-heading">Situation Reaction Test (SRT)</h2>
        <p class="module-desc">
          60 Real-world crises and dilemmas in 30 minutes. Demonstrates practical intelligence, speed of decision, and sense of personal responsibility.
        </p>

        <div class="tactical-ribbon">
          <div class="ribbon-item">Question Bank: <strong>2 Official DIPR Sets (120 Scenarios)</strong></div>
          <div class="ribbon-item">Time Standard: <strong>30 Minutes for 60 Scenarios</strong></div>
        </div>

        <div class="param-group">
          <label class="param-label">Select SRT Set</label>
          <select id="srtSelectSet">
            <option value="next_unattempted" selected>Next Unattempted Set (No Repeat Guarantee)</option>
            <option value="1">DIPR Official SRT Set 1 (60 Scenarios)</option>
            <option value="2">DIPR Official SRT Set 2 (60 Scenarios)</option>
            <option value="random">Random 60 Scenarios</option>
          </select>
        </div>

        <div class="param-group">
          <label class="param-label">Presentation Format</label>
          <div class="format-selector">
            <div class="format-card selected" id="srtModeBooklet" onclick="setSrtMode('booklet')">
              <strong>Full Booklet Mode (30:00 Timer)</strong>
              <span>Scrollable 60-scenario ledger with live clock. Replicates paper booklet navigation.</span>
            </div>
            <div class="format-card" id="srtModeFlash" onclick="setSrtMode('flash')">
              <strong>30s Flash Mode</strong>
              <span>Each situation flashes on screen individually for 30 seconds.</span>
            </div>
          </div>
        </div>

        <button class="btn-engage" onclick="startSrtTest()">Commence SRT Drill (30 Mins)</button>
      </div>

      <!-- SRT ACTIVE WORKSPACE -->
      <div class="command-panel" id="srtActiveScreen" style="display: none; max-width: 960px;">
        <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: 1.25rem; padding-bottom: 1rem; border-bottom: 1px solid var(--border-subtle);">
          <div>
            <h3 style="font-family: var(--font-tactical); font-size: 1.3rem;">Situation Reaction Ledger</h3>
            <span style="font-size: 0.85rem; color: var(--text-secondary);" id="srtCompletedCount">Attempted: 0 / 60</span>
          </div>
          <div style="display: flex; align-items: center; gap: 1rem;">
            <div style="font-family: var(--font-tactical); font-size: 2.2rem; font-weight: 700; color: var(--accent-brass);" id="srtMasterTimer">
              30:00
            </div>
            <button class="btn-engage" style="width: auto; margin-top: 0; padding: 0.55rem 1.5rem; font-size: 0.95rem;" onclick="submitSrtTest()">
              Submit Booklet
            </button>
          </div>
        </div>

        <div class="srt-scroll-deck" id="srtBookletList"></div>
      </div>

      <!-- SRT REVIEW SCREEN -->
      <div class="command-panel" id="srtReviewScreen" style="display: none; max-width: 960px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <h2 class="module-heading">SRT Session Completed</h2>
            <p class="module-desc" style="margin-bottom: 0;" id="srtReviewStats">Attempted: 60 / 60</p>
          </div>
          <button class="btn-aux" onclick="copySrtResponses()">Copy Reactions</button>
        </div>

        <div class="eval-dispatch-card">
          <div class="dispatch-header">
            <div>
              <div class="dispatch-title">
                AI SRT Evaluation
              </div>
              <p class="dispatch-desc">
                Evaluate completeness of reaction, speed of decision, and sense of responsibility. Flags evasion (e.g. <em>'called police and watched'</em>) and provides concise military-grade solutions.
              </p>
            </div>
            <div class="dispatch-actions">
              <button class="btn-engage" style="width: auto; margin-top: 0; padding: 0.55rem 1.25rem; font-size: 0.9rem; background: var(--accent-intel);" onclick="copySrtAiPrompt()">Copy AI Assessor Prompt</button>
              <button class="btn-aux" onclick="downloadSrtAiDossier()">Download Dossier</button>
            </div>
          </div>
          <div class="model-links-row">
            <span style="font-size: 0.8rem; color: var(--text-tertiary);">Step 2: Paste into free AI chat:</span>
            <div style="display: flex; gap: 0.5rem;">
              <a href="https://chatgpt.com" target="_blank" class="model-chip chip-chatgpt">ChatGPT ↗</a>
              <a href="https://claude.ai" target="_blank" class="model-chip chip-claude">Claude ↗</a>
              <a href="https://gemini.google.com" target="_blank" class="model-chip chip-gemini">Gemini ↗</a>
            </div>
          </div>
        </div>

        <div id="srtReviewContent" style="max-height: 480px; overflow-y: auto; display: flex; flex-direction: column; gap: 1rem; margin-bottom: 1.5rem;"></div>
        <button class="btn-aux" onclick="resetSrtToSetup()">Return to Setup</button>
      </div>
    </section>

    <!-- ==============================================================
         4. SDT MODULE
         ============================================================== -->
    <section class="workspace-module" id="tab-sdt">
      <div class="command-panel" style="max-width: 960px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 1rem; flex-wrap: wrap; gap: 1rem;">
          <div>
            <h2 class="module-heading">Self Description Test (SDT)</h2>
            <p class="module-desc" style="margin-bottom: 0;">
              5 Official DIPR Dimensions. 15 Minutes allotted. Be honest, balanced, and growth-oriented.
            </p>
          </div>
          <div style="display: flex; align-items: center; gap: 1rem;">
            <div style="font-family: var(--font-tactical); font-size: 2.2rem; font-weight: 700; color: var(--accent-brass);" id="sdtTimer">
              15:00
            </div>
            <button class="btn-aux" id="btnSdtTimerToggle" onclick="toggleSdtTimer()">Start Timer</button>
          </div>
        </div>

        <div class="eval-dispatch-card">
          <div class="dispatch-header">
            <div>
              <div class="dispatch-title">
                SDT Triangulation & Authenticity Check
              </div>
              <p class="dispatch-desc">
                AI cross-references your Parents, Teachers, Friends, and Self assessments to detect contradictions, fake weaknesses (e.g. <em>'perfectionist'</em>), and prepare you for Interviewing Officer questions.
              </p>
            </div>
            <div class="dispatch-actions">
              <button class="btn-engage" style="width: auto; margin-top: 0; padding: 0.55rem 1.25rem; font-size: 0.9rem; background: var(--accent-intel);" onclick="copySdtAiPrompt()">Copy AI Assessor Prompt</button>
              <button class="btn-aux" onclick="downloadSdtAiDossier()">Download Dossier</button>
            </div>
          </div>
          <div class="model-links-row">
            <span style="font-size: 0.8rem; color: var(--text-tertiary);">Step 2: Paste into free AI chat:</span>
            <div style="display: flex; gap: 0.5rem;">
              <a href="https://chatgpt.com" target="_blank" class="model-chip chip-chatgpt">ChatGPT ↗</a>
              <a href="https://claude.ai" target="_blank" class="model-chip chip-claude">Claude ↗</a>
              <a href="https://gemini.google.com" target="_blank" class="model-chip chip-gemini">Gemini ↗</a>
            </div>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 1.25rem;">
          <div class="param-group">
            <label class="param-label">1. Parents' Opinion</label>
            <textarea id="sdt1" style="height: 100px;" placeholder="What do your parents honestly perceive in your habits, sense of responsibility, emotional maturity, and conduct?"></textarea>
          </div>

          <div class="param-group">
            <label class="param-label">2. Teachers' / Instructors' Opinion</label>
            <textarea id="sdt2" style="height: 100px;" placeholder="What do your professors or commanding mentors say regarding your intellect, discipline, teamwork, and sincerity?"></textarea>
          </div>

          <div class="param-group">
            <label class="param-label">3. Friends' / Peers' Opinion</label>
            <textarea id="sdt3" style="height: 100px;" placeholder="What do your close friends appreciate most about you, and what help do they seek in times of crisis?"></textarea>
          </div>

          <div class="param-group">
            <label class="param-label">4. Your Own Opinion (Self Assessment)</label>
            <textarea id="sdt4" style="height: 100px;" placeholder="State your genuine strengths and authentic, remediable weaknesses that you are currently working on."></textarea>
          </div>

          <div class="param-group">
            <label class="param-label">5. Future Aspirations (Qualities Striving to Develop)</label>
            <textarea id="sdt5" style="height: 100px;" placeholder="What qualities do you wish to cultivate to become an effective military leader and responsible citizen?"></textarea>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; margin-top: 1.5rem; gap: 1rem; flex-wrap: wrap;">
          <button class="btn-aux" onclick="saveSdtLocal()">Save Draft</button>
          <button class="btn-engage" style="width: auto; margin-top: 0; padding: 0.65rem 2rem; font-size: 0.95rem;" onclick="copySdtText()">Copy 5 Paragraphs</button>
        </div>
      </div>
    </section>

    <!-- ==============================================================
         5. OIR MODULE
         ============================================================== -->
    <section class="workspace-module" id="tab-oir">
      <div style="width: 100%; display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.75rem;">
        <div>
          <h2 class="module-heading" style="font-size: 1.4rem; margin: 0;">Officer Intelligence Rating (OIR) Console</h2>
          <p style="color: var(--text-secondary); font-size: 0.85rem;">Upload your Verbal/Non-Verbal Question Paper PDF and mark responses on the live digital OMR.</p>
        </div>
        <div style="display: flex; gap: 0.6rem; align-items: center;">
          <input type="file" id="oirPdfInput" accept=".pdf" style="display: none;">
          <button class="btn-aux" onclick="document.getElementById('oirPdfInput').click()">Upload OIR PDF</button>
          <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); padding: 0.35rem 0.75rem; border-radius: var(--radius-sm); font-family: var(--font-tactical); font-size: 1.4rem; font-weight: 700; color: var(--accent-brass);" id="oirTimerNum">
            20:00
          </div>
          <button class="btn-aux" id="btnOirTimerToggle" onclick="toggleOirTimer()">Start Timer</button>
          <button class="btn-engage" style="width: auto; margin-top: 0; padding: 0.45rem 1.25rem; font-size: 0.9rem;" onclick="submitOirOMR()">Submit OMR</button>
        </div>
      </div>

      <div style="display: grid; grid-template-columns: 1.35fr 1fr; gap: 1.25rem; width: 100%; height: calc(100vh - 160px);">
        <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); overflow: hidden; display: flex; flex-direction: column; height: 100%;">
          <div id="oirPdfPlaceholder" style="flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 2rem; text-align: center;">
            <h3 style="font-family: var(--font-tactical); font-size: 1.5rem; margin-bottom: 0.4rem;">No OIR Paper Loaded</h3>
            <p style="color: var(--text-secondary); max-width: 420px; font-size: 0.9rem; margin-bottom: 1.5rem;">
              Upload any OIR test PDF (e.g. 50 Verbal/Non-Verbal questions) to inspect problems on the left while marking answers on the live OMR punch sheet.
            </p>
            <button class="btn-engage" style="width: auto; margin-top: 0; padding: 0.65rem 2rem; font-size: 0.95rem;" onclick="document.getElementById('oirPdfInput').click()">
              Upload OIR PDF File
            </button>
          </div>
          <iframe id="oirPdfIframe" style="width: 100%; height: 100%; border: none; display: none;"></iframe>
        </div>

        <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: 1.25rem; display: flex; flex-direction: column; height: 100%; overflow: hidden;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-subtle); padding-bottom: 0.75rem;">
            <div>
              <strong style="font-family: var(--font-tactical); font-size: 1.15rem; letter-spacing: 0.5px; text-transform: uppercase;">Digital OMR Sheet</strong>
              <div style="font-size: 0.8rem; color: var(--text-tertiary);" id="oirAttemptStats">Marked: 0 / 50 Questions</div>
            </div>
            <select id="oirQuestionCount" onchange="generateOmrRows()" style="padding: 0.35rem 0.6rem; font-size: 0.82rem; width: auto;">
              <option value="40">40 Questions</option>
              <option value="50" selected>50 Questions</option>
              <option value="60">60 Questions</option>
            </select>
          </div>

          <div class="omr-grid-scroll" id="omrRowsList" style="margin-top: 0.75rem;"></div>
        </div>
      </div>
    </section>

    <!-- ==============================================================
         6. GROUP DISCUSSION (GD) MODULE (NEW)
         ============================================================== -->
    <section class="workspace-module" id="tab-gd">
      <!-- GD SETUP -->
      <div class="command-panel" id="gdSetupScreen" style="max-width: 900px;">
        <h2 class="module-heading">Group Discussion (GD) Syndicate Simulator</h2>
        <p class="module-desc">
          Experience an authentic 8-candidate SSB syndicate debate. Virtual peers present arguments across 3 GTO leads. Test your ability to intervene, articulate points without shouting, influence the group, and maintain optimal airtime.
        </p>

        <div class="tactical-ribbon">
          <div class="ribbon-item">Syndicate Size: <strong>8 Candidates (Chest 2, 4, 7, 9 & YOU)</strong></div>
          <div class="ribbon-item">Debate Protocol: <strong>3 Distinct GTO Leads (15 Minutes)</strong></div>
        </div>

        <div class="param-group">
          <label class="param-label">Select Discussion Topic</label>
          <select id="gdSelectTopic">
            <option value="random" selected>Random Syndicate Topic (Recommended)</option>
'''

for sc in gd_topics_data:
    html += f'            <option value="{sc["id"]}">{sc["title"]} [{sc["category"]}]</option>\n'

html += f'''          </select>
        </div>

        <div class="grid-duo">
          <div class="param-group">
            <label class="param-label">Session Duration</label>
            <select id="gdSelectDuration">
              <option value="900" selected>15 Minutes (Official DIPR Standard)</option>
              <option value="600">10 Minutes (Accelerated Pressure Drill)</option>
              <option value="1200">20 Minutes (Full GTO Session)</option>
            </select>
          </div>
          <div class="param-group">
            <label class="param-label">Virtual Syndicate Voice Audio</label>
            <select id="gdSelectAudio">
              <option value="voice_on" selected>Voice Synthesis Enabled (Peers Speak Aloud)</option>
              <option value="voice_off">Muted (Visual Transcript Dialogue Only)</option>
            </select>
          </div>
        </div>

        <div class="param-group">
          <label class="param-label">Your Input Mode</label>
          <div class="format-selector">
            <div class="format-card selected" id="gdModeVoice" onclick="setGdInputMode('voice')">
              <strong>Microphone & Voice Input (Recommended)</strong>
              <span>Speak into your mic. Your interventions are transcribed live into the syndicate transcript.</span>
            </div>
            <div class="format-card" id="gdModeText" onclick="setGdInputMode('text')">
              <strong>Keyboard Text Input</strong>
              <span>Type your arguments and submit points via text for quiet environments.</span>
            </div>
          </div>
        </div>

        <button class="btn-engage" onclick="startGdSession()">Commence Group Discussion</button>
      </div>

      <!-- GD ACTIVE SYNDICATE ARENA -->
      <div class="command-panel" id="gdActiveScreen" style="display: none; max-width: 1040px;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.25rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 1rem; flex-wrap: wrap; gap: 1rem;">
          <div>
            <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-brass); text-transform: uppercase; letter-spacing: 0.5px;" id="gdActiveCategory">
              Defense & Security
            </div>
            <h3 style="font-family: var(--font-tactical); font-size: 1.35rem; color: var(--text-primary); margin-top: 0.2rem;" id="gdActiveTitle">
              Topic Title
            </h3>
          </div>
          <div style="display: flex; align-items: center; gap: 1rem;">
            <div style="font-family: var(--font-tactical); font-size: 2.2rem; font-weight: 700; color: var(--accent-brass);" id="gdMasterTimer">
              15:00
            </div>
            <button class="btn-aux" style="color: var(--accent-alert);" onclick="abortGdSession()">Abort Session</button>
          </div>
        </div>

        <!-- SYNDICATE ROSTER -->
        <div class="gd-roster">
          <div class="syndicate-avatar" id="avatarChest2">
            <span class="avatar-chest">CHEST 2</span>
            <span class="avatar-archetype">Analytical / Facts</span>
            <span class="avatar-status" id="statusChest2">Listening</span>
          </div>
          <div class="syndicate-avatar" id="avatarChest4">
            <span class="avatar-chest">CHEST 4</span>
            <span class="avatar-archetype">Assertive / Fast</span>
            <span class="avatar-status" id="statusChest4">Listening</span>
          </div>
          <div class="syndicate-avatar you" id="avatarYou">
            <span class="avatar-chest">YOU</span>
            <span class="avatar-archetype">Candidate</span>
            <span class="avatar-status" id="statusYou">Floor Free</span>
          </div>
          <div class="syndicate-avatar" id="avatarChest7">
            <span class="avatar-chest">CHEST 7</span>
            <span class="avatar-archetype">Consensus / Diplomat</span>
            <span class="avatar-status" id="statusChest7">Listening</span>
          </div>
          <div class="syndicate-avatar" id="avatarChest9">
            <span class="avatar-chest">CHEST 9</span>
            <span class="avatar-archetype">Contrarian / Depth</span>
            <span class="avatar-status" id="statusChest9">Listening</span>
          </div>
        </div>

        <!-- 3 LEADS PROGRESSION BANNER -->
        <div class="gd-leads-banner">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
            <strong style="font-family: var(--font-tactical); font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.5px; color: var(--accent-brass);">
              GTO Discussion Leads (Topic Angles)
            </strong>
            <span style="font-size: 0.8rem; color: var(--text-tertiary);" id="gdPhaseLeadTag">Focusing on Lead 1</span>
          </div>
          <div class="leads-grid" id="gdLeadsGrid">
            <div class="lead-box active" id="gdLeadBox1">Lead 1</div>
            <div class="lead-box" id="gdLeadBox2">Lead 2</div>
            <div class="lead-box" id="gdLeadBox3">Lead 3</div>
          </div>
        </div>

        <!-- AIRTIME GAUGE -->
        <div class="airtime-bar-wrap">
          <span style="font-size: 0.8rem; font-weight: 600; color: var(--text-tertiary); text-transform: uppercase; white-space: nowrap;">
            Your Airtime: <strong id="gdAirtimePercent" style="color: var(--accent-ready);">0%</strong>
          </span>
          <div style="flex: 1; height: 6px; background: var(--bg-surface-elevated); border-radius: 3px; overflow: hidden;">
            <div id="gdAirtimeFill" style="width: 0%; height: 100%; background: var(--accent-ready); transition: width 0.3s ease;"></div>
          </div>
          <span style="font-size: 0.78rem; color: var(--text-secondary);" id="gdAirtimeAdvice">Target: 15% - 22%</span>
        </div>

        <!-- SYNDICATE TRANSCRIPT FEED -->
        <div class="gd-feed" id="gdTranscriptFeed">
          <div style="color: var(--text-tertiary); font-size: 0.85rem; text-align: center; margin: auto;">
            Discussion commencing. The GTO has laid down the topic. Listen to peers and prepare to intervene.
          </div>
        </div>

        <!-- CANDIDATE ACTION DOCK -->
        <div style="display: flex; flex-direction: column; gap: 0.75rem;">
          <div style="display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap;">
            <button class="btn-engage" id="btnIntervene" style="flex: 1; margin-top: 0; background: var(--accent-ready); font-size: 1.05rem;" onclick="toggleCandidateIntervention()">
              Intervene & Speak (Microphone)
            </button>
            <button class="btn-aux" id="btnToggleGdAudio" onclick="toggleGdAudioMute()">
              Mute Voices
            </button>
          </div>

          <div id="gdTextInputArea" style="display: none; gap: 0.5rem;">
            <input type="text" id="gdTextInput" placeholder="Type your argument/counter-point and press Enter..." onkeydown="if(event.key==='Enter') submitCandidateTextArgument()">
            <button class="btn-aux" style="border-color: var(--accent-ready); color: var(--accent-ready); white-space: nowrap;" onclick="submitCandidateTextArgument()">
              Submit Point
            </button>
          </div>
        </div>
      </div>

      <!-- GD REVIEW & AI GTO DISPATCH SCREEN -->
      <div class="command-panel" id="gdReviewScreen" style="display: none; max-width: 960px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <h2 class="module-heading">Group Discussion Session Complete</h2>
            <p class="module-desc" style="margin-bottom: 0;" id="gdReviewSummary">Session review & GTO performance analysis.</p>
          </div>
          <button class="btn-aux" onclick="copyGdTranscript()">Copy Full Transcript</button>
        </div>

        <!-- GTO AI EVALUATION DISPATCH -->
        <div class="eval-dispatch-card">
          <div class="dispatch-header">
            <div>
              <div class="dispatch-title">
                GTO AI Evaluation Dispatch (ChatGPT / Claude / Gemini)
              </div>
              <p class="dispatch-desc">
                Evaluate your performance using an AI prompted as a <strong>Senior Services Selection Board Group Testing Officer (GTO)</strong>. It assesses reasoning ability, group influence, power of expression, listening courtesy, and recommends model interventions.
              </p>
            </div>
            <div class="dispatch-actions">
              <button class="btn-engage" style="width: auto; margin-top: 0; padding: 0.55rem 1.25rem; font-size: 0.9rem; background: var(--accent-intel);" onclick="copyGdAiPrompt()">Copy GTO Evaluation Prompt</button>
              <button class="btn-aux" onclick="downloadGdAiDossier()">Download Dossier</button>
            </div>
          </div>
          <div class="model-links-row">
            <span style="font-size: 0.8rem; color: var(--text-tertiary);">Step 2: Paste into free AI chat:</span>
            <div style="display: flex; gap: 0.5rem;">
              <a href="https://chatgpt.com" target="_blank" class="model-chip chip-chatgpt">ChatGPT ↗</a>
              <a href="https://claude.ai" target="_blank" class="model-chip chip-claude">Claude ↗</a>
              <a href="https://gemini.google.com" target="_blank" class="model-chip chip-gemini">Gemini ↗</a>
            </div>
          </div>
        </div>

        <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.5rem;">
          <h4 style="font-family: var(--font-tactical); font-size: 1.15rem; color: var(--accent-brass); margin-bottom: 0.5rem; text-transform: uppercase;">
            Participation Telemetry
          </h4>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; font-size: 0.9rem;">
            <div>Interventions Made: <strong id="telemetryInterventions" style="color: var(--accent-ready);">0</strong></div>
            <div>Airtime Share: <strong id="telemetryAirtime" style="color: var(--accent-ready);">0%</strong></div>
            <div>Target Ideal: <strong>15% - 22%</strong></div>
          </div>
        </div>

        <div style="max-height: 400px; overflow-y: auto; border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1rem; background: var(--bg-base); margin-bottom: 1.5rem;" id="gdReviewTranscript"></div>

        <button class="btn-aux" onclick="resetGdToSetup()">Return to Setup</button>
      </div>
    </section>

    <!-- ==============================================================
         7. LECTURETTE MODULE (250+ TOPICS) (NEW)
         ============================================================== -->
    <section class="workspace-module" id="tab-lecturette">
      <!-- LECTURETTE SETUP -->
      <div class="command-panel" id="lecSetupScreen" style="max-width: 900px;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.25rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 1rem; flex-wrap: wrap; gap: 1rem;">
          <div>
            <h2 class="module-heading">Lecturette Trainer (250+ DIPR Topics)</h2>
            <p class="module-desc" style="margin-bottom: 0;">
              3 Minutes Preparation followed by 3 Minutes Delivery. Master structure, pacing, posture, and poise. Acoustic warning bells sound at 2:30 (single chime) and 3:00 (double chime).
            </p>
          </div>
          <button class="btn-aux" onclick="shuffleLecturetteCard()">Draw Random Card</button>
        </div>

        <div class="tactical-ribbon">
          <div class="ribbon-item">Topic Repository: <strong>251 Authentic SSB Topics</strong></div>
          <div class="ribbon-item">Card Structure: <strong>4 Tiers (Defense, National, Social, Basic)</strong></div>
        </div>

        <!-- 4-TIER CUE CARD DISPLAY -->
        <div class="lecturette-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 0.5rem;">
            <strong style="font-family: var(--font-tactical); font-size: 1.1rem; color: var(--accent-brass); text-transform: uppercase;" id="lecCardTitle">
              DIPR Cue Card #1
            </strong>
            <span style="font-size: 0.8rem; color: var(--text-tertiary);">Select 1 topic to deliver:</span>
          </div>

          <div id="lecCardTopicsList"></div>
        </div>

        <!-- ON-DEMAND TOPIC SEARCH -->
        <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.5rem;">
          <label class="param-label">Or Search All 251 Topics</label>
          <div style="display: flex; gap: 0.5rem; margin-bottom: 0.75rem;">
            <input type="text" id="lecSearchInput" placeholder="Filter by keyword (e.g. Space, Defense, Education, China, EV)..." oninput="filterLecturetteTopics()">
            <select id="lecFilterTier" onchange="filterLecturetteTopics()" style="width: 200px;">
              <option value="all">All 4 Tiers</option>
              <option value="tier1">Tier 1: Geopolitics & Defense</option>
              <option value="tier2">Tier 2: National Strategy</option>
              <option value="tier3">Tier 3: Social & Science</option>
              <option value="tier4">Tier 4: Basic & Sports</option>
            </select>
          </div>
          <div id="lecSearchResults" style="max-height: 160px; overflow-y: auto; display: flex; flex-direction: column; gap: 0.4rem;"></div>
        </div>

        <div class="grid-duo">
          <div class="param-group">
            <label class="param-label">Preparation Time</label>
            <select id="lecPrepDuration">
              <option value="180" selected>3 Minutes (Official DIPR Standard)</option>
              <option value="90">1.5 Minutes (Fast Mental Drill)</option>
              <option value="0">Skip Prep (Immediate Delivery)</option>
            </select>
          </div>
          <div class="param-group">
            <label class="param-label">Posture & Eye Contact Mirror</label>
            <select id="lecMirrorOption">
              <option value="mirror_on" selected>Webcam Mirror Enabled (Check Stance & Eye Contact)</option>
              <option value="mirror_off">Mirror Disabled</option>
            </select>
          </div>
        </div>

        <button class="btn-engage" id="btnStartLecturette" onclick="startLecturetteFlow()">
          Commence 3-Minute Preparation
        </button>
      </div>

      <!-- LECTURETTE PREPARATION STAGE (3 MINS) -->
      <div class="command-panel" id="lecPrepScreen" style="display: none; max-width: 900px; padding: 2rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 1rem;">
          <div>
            <span class="phase-pill observe">PREPARATION PHASE (3:00)</span>
            <h3 style="font-family: var(--font-tactical); font-size: 1.6rem; color: var(--accent-brass); margin-top: 0.35rem;" id="lecPrepTopicTitle">
              Selected Topic
            </h3>
          </div>
          <div class="precision-clock">
            <svg class="clock-svg" viewBox="0 0 80 80">
              <circle class="clock-track" cx="40" cy="40" r="36" />
              <circle class="clock-fill" id="lecPrepClockCircle" cx="40" cy="40" r="36" />
            </svg>
            <div class="clock-digits" id="lecPrepClockNum">3:00</div>
          </div>
        </div>

        <div class="param-group">
          <label class="param-label">Mental Scratchpad (Structure your points)</label>
          <p style="font-size: 0.82rem; color: var(--text-tertiary); margin-bottom: 0.4rem;">
            Recommended Formula: 1. Introduction & Background (30s) ➔ 2. Key Dimensions & Data (90s) ➔ 3. Challenges & Ground Realities (30s) ➔ 4. Conclusion & Officer's Way Forward (30s).
          </p>
          <textarea id="lecScratchpad" style="height: 180px;" placeholder="Jot down quick bullet points (Intro, Pros/Cons, Way forward)..."></textarea>
        </div>

        <div style="display: flex; gap: 0.75rem; justify-content: center; margin-top: 1.5rem;">
          <button class="btn-engage" style="width: auto; margin-top: 0; background: var(--accent-ready);" onclick="advanceToLecturetteDelivery()">
            Ready to Speak ➔ Proceed to Delivery
          </button>
          <button class="btn-aux" style="color: var(--accent-alert);" onclick="abortLecturette()">Abort Drill</button>
        </div>
      </div>

      <!-- LECTURETTE DELIVERY STAGE (3 MINS) -->
      <div class="command-panel" id="lecDeliveryScreen" style="display: none; max-width: 960px; padding: 2rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 1rem;">
          <div>
            <span class="phase-pill write" id="lecDeliveryPhaseTag">DELIVERY PHASE (3:00)</span>
            <h3 style="font-family: var(--font-tactical); font-size: 1.7rem; color: var(--accent-brass); margin-top: 0.35rem;" id="lecDeliveryTopicTitle">
              Selected Topic
            </h3>
          </div>
          <div class="precision-clock">
            <svg class="clock-svg" viewBox="0 0 80 80">
              <circle class="clock-track" cx="40" cy="40" r="36" />
              <circle class="clock-fill" id="lecDeliveryClockCircle" cx="40" cy="40" r="36" />
            </svg>
            <div class="clock-digits" id="lecDeliveryClockNum">3:00</div>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.5rem;">
          <!-- POSTURE MIRROR -->
          <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1rem; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div style="font-size: 0.8rem; font-weight: 600; color: var(--text-tertiary); text-transform: uppercase; margin-bottom: 0.5rem;">
              Posture & Eye Contact Mirror
            </div>
            <video id="lecWebcamVideo" class="posture-mirror-video" autoplay playsinline muted></video>
            <span style="font-size: 0.75rem; color: var(--text-tertiary); margin-top: 0.4rem;">Maintains local camera stream only. No video leaves your browser.</span>
          </div>

          <!-- SPEECH TRANSCRIPT / SCRATCHPAD -->
          <div style="display: flex; flex-direction: column; gap: 0.5rem;">
            <div style="font-size: 0.8rem; font-weight: 600; color: var(--text-tertiary); text-transform: uppercase;">
              Live Transcribed Speech
            </div>
            <div id="lecLiveTranscript" style="flex: 1; min-height: 180px; max-height: 240px; overflow-y: auto; background: var(--bg-base); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 0.85rem; font-size: 0.9rem; line-height: 1.5; color: var(--text-secondary);">
              Microphone active. Begin your delivery. Speech will be transcribed live for AI GTO grading.
            </div>
            <div style="font-size: 0.78rem; color: var(--accent-brass);" id="lecBellStatus">
              Acoustic Bell: Warning chime at 2:30 (30s remaining), Final bell at 3:00.
            </div>
          </div>
        </div>

        <div style="display: flex; gap: 0.75rem; justify-content: center;">
          <button class="btn-engage" style="width: auto; margin-top: 0; background: var(--accent-ready);" onclick="finishLecturette()">
            Conclude Lecturette Ahead of Time
          </button>
          <button class="btn-aux" style="color: var(--accent-alert);" onclick="abortLecturette()">Abort</button>
        </div>
      </div>

      <!-- LECTURETTE REVIEW & AI GTO EVALUATION -->
      <div class="command-panel" id="lecReviewScreen" style="display: none; max-width: 960px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <h2 class="module-heading">Lecturette Delivery Complete</h2>
            <p class="module-desc" style="margin-bottom: 0;" id="lecReviewSubtitle">Topic review & speech transcript.</p>
          </div>
          <button class="btn-aux" onclick="copyLecturetteTranscript()">Copy Speech Transcript</button>
        </div>

        <div class="eval-dispatch-card">
          <div class="dispatch-header">
            <div>
              <div class="dispatch-title">
                GTO AI Lecturette Evaluation (ChatGPT / Claude / Gemini)
              </div>
              <p class="dispatch-desc">
                Evaluate your delivery using an AI prompted as a <strong>Senior Services Selection Board Group Testing Officer (GTO)</strong>. It assesses structure (Intro-Body-Conclusion), factual depth, speech pacing, clarity, and provides a model officer lecturette outline.
              </p>
            </div>
            <div class="dispatch-actions">
              <button class="btn-engage" style="width: auto; margin-top: 0; padding: 0.55rem 1.25rem; font-size: 0.9rem; background: var(--accent-intel);" onclick="copyLecturetteAiPrompt()">Copy GTO Evaluation Prompt</button>
              <button class="btn-aux" onclick="downloadLecturetteAiDossier()">Download Dossier</button>
            </div>
          </div>
          <div class="model-links-row">
            <span style="font-size: 0.8rem; color: var(--text-tertiary);">Step 2: Paste into free AI chat:</span>
            <div style="display: flex; gap: 0.5rem;">
              <a href="https://chatgpt.com" target="_blank" class="model-chip chip-chatgpt">ChatGPT ↗</a>
              <a href="https://claude.ai" target="_blank" class="model-chip chip-claude">Claude ↗</a>
              <a href="https://gemini.google.com" target="_blank" class="model-chip chip-gemini">Gemini ↗</a>
            </div>
          </div>
        </div>

        <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.5rem;">
          <h4 style="font-family: var(--font-tactical); font-size: 1.15rem; color: var(--accent-brass); margin-bottom: 0.5rem; text-transform: uppercase;">
            Delivery Summary
          </h4>
          <div style="font-size: 0.92rem; line-height: 1.6;">
            <div>Topic: <strong id="lecReviewTopic" style="color: var(--accent-brass);">Topic Name</strong></div>
            <div>Delivery Duration: <strong id="lecReviewDuration" style="color: var(--accent-ready);">3:00 Minutes</strong></div>
          </div>
        </div>

        <div class="param-group">
          <label class="param-label">Your Speech Transcript</label>
          <div id="lecFinalTranscriptBox" style="background: var(--bg-base); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1.15rem; font-size: 0.92rem; line-height: 1.6; max-height: 320px; overflow-y: auto;"></div>
        </div>

        <button class="btn-aux" onclick="resetLecturetteToSetup()">Return to Setup</button>
      </div>
    </section>

    <!-- ==============================================================
         8. FULL MOCK BATTERY
         ============================================================== -->
    <section class="workspace-module" id="tab-fullmock">
      <div class="command-panel" style="max-width: 820px; text-align: center;">
        <h2 class="module-heading">Stage 2 Full Battery Simulation</h2>
        <p class="module-desc" style="margin: 0 auto 2rem auto;">
          Experience the authentic, unbroken testing schedule of Services Selection Board (SSB) across Psychology and GTO.
        </p>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; text-align: left; margin-bottom: 2rem;">
          <div style="background: var(--bg-surface-elevated); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
            <strong style="font-family: var(--font-tactical); font-size: 1.1rem; color: var(--accent-brass); display: block; margin-bottom: 0.25rem;">1. TAT (Thematic Apperception)</strong>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">12 Slides (11 visual stimuli + 1 blank slide). 30s observation, 4 min writing per slide.</p>
          </div>
          <div style="background: var(--bg-surface-elevated); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
            <strong style="font-family: var(--font-tactical); font-size: 1.1rem; color: var(--accent-brass); display: block; margin-bottom: 0.25rem;">2. WAT (Word Association)</strong>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">60 Words flashed at 15 seconds each continuously under high pace.</p>
          </div>
          <div style="background: var(--bg-surface-elevated); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
            <strong style="font-family: var(--font-tactical); font-size: 1.1rem; color: var(--accent-brass); display: block; margin-bottom: 0.25rem;">3. SRT (Situation Reaction)</strong>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">60 Real-world challenging situations to solve in exactly 30 minutes.</p>
          </div>
          <div style="background: var(--bg-surface-elevated); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
            <strong style="font-family: var(--font-tactical); font-size: 1.1rem; color: var(--accent-brass); display: block; margin-bottom: 0.25rem;">4. GTO Verbal Battery</strong>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">15-Minute Syndicate Group Discussion + 3-Minute Lecturette Delivery.</p>
          </div>
        </div>

        <button class="btn-engage" style="max-width: 400px; margin: 0 auto;" onclick="launchFullMockBattery()">
          Commence Full Battery Simulation
        </button>
      </div>
    </section>

    <!-- ==============================================================
         9. AI ASSESSOR DISPATCH HUB
         ============================================================== -->
    <section class="workspace-module" id="tab-ai-assessor">
      <div class="command-panel" style="max-width: 1040px;">
        <div style="border-bottom: 1px solid var(--border-subtle); padding-bottom: 1.25rem; margin-bottom: 1.5rem;">
          <h2 class="module-heading" style="color: var(--accent-intel);">AI Psychologist & GTO Evaluation Hub</h2>
          <p class="module-desc" style="margin-bottom: 0;">
            Zero-cost, professional grading across Psychological tests (TAT, WAT, SRT, SDT) and GTO verbal drills (GD, Lecturette) using free foundation models (ChatGPT-4o, Claude 3.5 Sonnet, or Google Gemini).
          </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-bottom: 2rem;">
          <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1.25rem;">
            <div style="font-family: var(--font-tactical); font-size: 1.3rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.4rem;">
              1. Extract Stimuli & Prompt
            </div>
            <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.5;">
              Select any test set (WAT, TAT image ZIP, SRT, SDT, GD, Lecturette) to copy the expert DIPR Assessor evaluation prompt.
            </p>
          </div>
          <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1.25rem;">
            <div style="font-family: var(--font-tactical); font-size: 1.3rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.4rem;">
              2. Deploy to Free AI Chat
            </div>
            <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.5;">
              Open <a href="https://chatgpt.com" target="_blank" style="color: var(--accent-ready); font-weight: 600;">ChatGPT</a>, <a href="https://claude.ai" target="_blank" style="color: #fbbf24; font-weight: 600;">Claude</a>, or <a href="https://gemini.google.com" target="_blank" style="color: var(--accent-intel); font-weight: 600;">Gemini</a>. Zero developer API key required.
            </p>
          </div>
          <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1.25rem;">
            <div style="font-family: var(--font-tactical); font-size: 1.3rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.4rem;">
              3. Receive 15 OLQ Scoring
            </div>
            <p style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.5;">
              The AI roleplays as a <strong>Senior DIPR Assessor</strong>, grading your responses across the 15 OLQs, highlighting red flags, and rewriting them into officer-level responses.
            </p>
          </div>
        </div>

        <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1.5rem; margin-bottom: 2rem;">
          <h3 style="font-family: var(--font-tactical); font-size: 1.25rem; font-weight: 700; color: var(--accent-brass); margin-bottom: 0.35rem; text-transform: uppercase;">
            On-Demand Test Package Downloader
          </h3>
          <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 1.25rem;">
            Select any test below to generate the exact prompt dossier or stimulus package for AI review:
          </p>

          <div class="grid-duo">
            <div class="param-group">
              <label class="param-label">Select Test Type</label>
              <select id="hubSelectType" onchange="updateHubOptions()">
                <option value="tat" selected>Thematic Apperception Test (TAT) — With Slide Images ZIP</option>
                <option value="wat">Word Association Test (WAT) — 60 Words List</option>
                <option value="srt">Situation Reaction Test (SRT) — 60 Scenarios</option>
                <option value="sdt">Self Description Test (SDT) — 5 Dimensions</option>
                <option value="gd">Group Discussion (GD) — Full Syndicate Debate</option>
                <option value="lecturette">Lecturette — 4-Tier Topic Outline</option>
              </select>
            </div>
            <div class="param-group">
              <label class="param-label">Select Specific Item / Set</label>
              <select id="hubSelectSet"></select>
            </div>
          </div>

          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 0.5rem;">
            <button class="btn-engage" style="width: auto; margin-top: 0; padding: 0.65rem 1.5rem; font-size: 0.95rem;" id="btnHubDownload" onclick="executeHubDownload()">
              Download Package / Dossier
            </button>
            <button class="btn-aux" onclick="executeHubCopyPrompt()">
              Copy Prompt to Clipboard
            </button>
          </div>
        </div>
      </div>
    </section>

      </main>
    </div><!-- /.main-viewport -->
  </div><!-- /.app-layout -->

  <script>
    // DATA REPOSITORIES
    const WAT_SETS = {wat_sets_json};
    const ALL_WAT_WORDS = {all_wat_words_json};
    const SRT_SETS = {srt_sets_json};
    const TAT_SETS = {tat_sets_json};
    const LECTURETTE_DATA = {lecturette_data_json};
    const GD_TOPICS = {gd_topics_json};

    function showToast(msg) {{
      const t = document.getElementById('tacticalToast');
      t.textContent = msg;
      t.classList.add('visible');
      setTimeout(() => t.classList.remove('visible'), 2200);
    }}

    // NAVIGATION & VERTICAL SIDEBAR
    const tabs = document.querySelectorAll('.op-tab');
    const modules = document.querySelectorAll('.workspace-module');
    const sidebarNav = document.getElementById('sidebarNav');
    const sidebarBackdrop = document.getElementById('sidebarBackdrop');
    const btnToggleSidebar = document.getElementById('btnToggleSidebar');
    const currentModuleLabel = document.getElementById('currentModuleLabel');

    function updateActiveModuleLabel(tab) {{
      if (!currentModuleLabel || !tab) return;
      const labelSpan = tab.querySelector('.tab-label');
      currentModuleLabel.textContent = labelSpan ? labelSpan.textContent.trim() : tab.textContent.trim();
    }}

    tabs.forEach(tab => {{
      tab.addEventListener('click', () => {{
        tabs.forEach(t => t.classList.remove('active'));
        modules.forEach(m => m.classList.remove('active'));

        tab.classList.add('active');
        const targetId = tab.getAttribute('data-tab');
        const targetModule = document.getElementById(targetId);
        if (targetModule) {{
          targetModule.classList.add('active');
        }}
        updateActiveModuleLabel(tab);

        // Close mobile drawer if open
        if (window.innerWidth <= 992 && sidebarNav) {{
          sidebarNav.classList.remove('open');
          if (sidebarBackdrop) sidebarBackdrop.classList.remove('active');
        }}

        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }});
    }});

    if (btnToggleSidebar) {{
      btnToggleSidebar.addEventListener('click', () => {{
        if (window.innerWidth <= 992) {{
          const isOpen = sidebarNav.classList.toggle('open');
          if (sidebarBackdrop) sidebarBackdrop.classList.toggle('active', isOpen);
        }} else {{
          document.body.classList.toggle('sidebar-collapsed');
        }}
      }});
    }}

    if (sidebarBackdrop) {{
      sidebarBackdrop.addEventListener('click', () => {{
        if (sidebarNav) sidebarNav.classList.remove('open');
        sidebarBackdrop.classList.remove('active');
      }});
    }}

    // PROGRESS TRACKER
    const STORAGE_KEY = 'ssb_master_progress';

    function getProgressData() {{
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return {{ watCompleted: [], tatCompleted: [], srtCompleted: [], gdCompleted: 0, lecCompleted: 0, history: [] }};
      try {{
        const parsed = JSON.parse(raw);
        if (!parsed.gdCompleted) parsed.gdCompleted = 0;
        if (!parsed.lecCompleted) parsed.lecCompleted = 0;
        return parsed;
      }} catch (e) {{
        return {{ watCompleted: [], tatCompleted: [], srtCompleted: [], gdCompleted: 0, lecCompleted: 0, history: [] }};
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
      p.history.unshift({{ date: getFormattedTimestamp(), module: 'WAT', item: `Set ${{id}} (60 Words)`, result: 'Completed' }});
      saveProgressData(p);
    }}

    function markTatSetDone(id) {{
      const p = getProgressData();
      if (!p.tatCompleted.includes(id)) p.tatCompleted.push(id);
      p.history.unshift({{ date: getFormattedTimestamp(), module: 'TAT', item: `Set ${{id}} (12 Slides)`, result: 'Completed' }});
      saveProgressData(p);
    }}

    function markSrtSetDone(id) {{
      const p = getProgressData();
      if (!p.srtCompleted.includes(id)) p.srtCompleted.push(id);
      p.history.unshift({{ date: getFormattedTimestamp(), module: 'SRT', item: `Set ${{id}} (60 Scenarios)`, result: 'Completed' }});
      saveProgressData(p);
    }}

    function markGdDone(topicTitle, airtime) {{
      const p = getProgressData();
      p.gdCompleted = (p.gdCompleted || 0) + 1;
      p.history.unshift({{ date: getFormattedTimestamp(), module: 'GD', item: topicTitle, result: `${{airtime}}% Airtime` }});
      saveProgressData(p);
    }}

    function markLecturetteDone(topicTitle) {{
      const p = getProgressData();
      p.lecCompleted = (p.lecCompleted || 0) + 1;
      p.history.unshift({{ date: getFormattedTimestamp(), module: 'Lecturette', item: topicTitle, result: 'Delivered (3m)' }});
      saveProgressData(p);
    }}

    function logCompletedSession(mod, item, result) {{
      const p = getProgressData();
      p.history.unshift({{ date: getFormattedTimestamp(), module: mod, item: item, result: result }});
      saveProgressData(p);
    }}

    function getFormattedTimestamp() {{
      const d = new Date();
      return d.toLocaleDateString() + ' ' + d.toLocaleTimeString([], {{hour: '2-digit', minute:'2-digit'}});
    }}

    function clearPracticeHistory() {{
      if (confirm("Reset operation logs and completed status?")) {{
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
            alert("Progress state restored successfully!");
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

      document.getElementById('progGdVal').textContent = p.gdCompleted || 0;
      document.getElementById('progLecVal').textContent = p.lecCompleted || 0;

      // Pills for WAT
      const pillsWat = document.getElementById('pillsWat');
      pillsWat.innerHTML = '';
      WAT_SETS.forEach(s => {{
        const isDone = p.watCompleted.includes(s.id);
        const pill = document.createElement('div');
        pill.className = `inventory-pill ${{isDone ? 'cleared' : ''}}`;
        pill.innerHTML = `${{isDone ? '✓ ' : ''}}Set ${{s.id}}`;
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
        pill.className = `inventory-pill ${{isDone ? 'cleared' : ''}}`;
        pill.innerHTML = `${{isDone ? '✓ ' : ''}}TAT ${{s.id}}`;
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
        pill.className = `inventory-pill ${{isDone ? 'cleared' : ''}}`;
        pill.innerHTML = `${{isDone ? '✓ ' : ''}}SRT Set ${{num}}`;
        pill.onclick = () => {{
          document.querySelector('[data-tab="tab-srt"]').click();
          document.getElementById('srtSelectSet').value = `${{num}}`;
        }};
        pillsSrt.appendChild(pill);
      }});

      calculateNextRecommendation(p);

      // History Table
      const tbody = document.getElementById('historyTableBody');
      tbody.innerHTML = '';
      if (p.history.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="4" style="padding: 1.25rem; text-align: center; color: var(--text-tertiary);">No practice sessions logged yet. Begin any test to register activity.</td></tr>';
      }} else {{
        p.history.slice(0, 30).forEach(h => {{
          const tr = document.createElement('tr');
          tr.style.borderBottom = '1px solid var(--border-subtle)';
          tr.innerHTML = `
            <td style="padding: 0.6rem 1rem; color: var(--text-tertiary); font-family: var(--font-mono); font-size: 0.8rem;">${{h.date}}</td>
            <td style="padding: 0.6rem 1rem; font-weight: 600;">${{h.module}}</td>
            <td style="padding: 0.6rem 1rem;">${{h.item}}</td>
            <td style="padding: 0.6rem 1rem; color: var(--accent-ready); font-weight: 600;">${{h.result}}</td>
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
        recDiv.innerHTML = `<strong>TAT Set ${{nextTat.id}}</strong> (11 Pictures + 1 Blank Slide) &mdash; Unattempted`;
        btnRec.onclick = () => {{
          document.querySelector('[data-tab="tab-tat"]').click();
          document.getElementById('tatSelectSet').value = `tat_set_${{nextTat.id}}`;
        }};
      }} else if (nextSrt) {{
        recDiv.innerHTML = `<strong>SRT Set ${{nextSrt}}</strong> (60 Scenarios in 30 Mins) &mdash; Unattempted`;
        btnRec.onclick = () => {{
          document.querySelector('[data-tab="tab-srt"]').click();
          document.getElementById('srtSelectSet').value = `${{nextSrt}}`;
        }};
      }} else {{
        recDiv.innerHTML = `<strong style="color: var(--accent-ready);">Complete Syllabus Mastered.</strong> All official sets cleared. Proceed with Stage 2 Full Mock Battery.`;
        btnRec.textContent = 'Launch Full Mock';
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
          const clean = opt.textContent.replace('✓ [CLEARED] ', '');
          opt.textContent = isDone ? `✓ [CLEARED] ${{clean}}` : clean;
        }});
      }}

      const tatGroup = document.getElementById('tatOptGroupSets');
      if (tatGroup) {{
        Array.from(tatGroup.options).forEach(opt => {{
          const setId = parseInt(opt.value.replace('tat_set_', ''), 10);
          const isDone = p.tatCompleted.includes(setId);
          const clean = opt.textContent.replace('✓ [CLEARED] ', '');
          opt.textContent = isDone ? `✓ [CLEARED] ${{clean}}` : clean;
        }});
      }}
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
      document.getElementById('watModePaper').classList.toggle('selected', m === 'paper');
      document.getElementById('watModeTyping').classList.toggle('selected', m === 'typing');
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

      playAudioBeep(640, 0.08);
    }}

    function runWatTimer() {{
      clearInterval(watInterval);
      watRemaining = watDuration;
      updateWatTimerUI();

      watInterval = setInterval(() => {{
        if (watPaused) return;
        watRemaining--;
        updateWatTimerUI();

        if (watRemaining <= 0) nextWatWord();
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
      document.getElementById('watPauseLabel').textContent = watPaused ? 'Resume' : 'Pause';
    }}

    function abortWatTest() {{
      if (confirm("Terminate WAT drill? Current recorded responses will be displayed.")) finishWatTest();
    }}

    function finishWatTest() {{
      clearInterval(watInterval);
      if (watCurrentSetId) markWatSetDone(watCurrentSetId);
      else logCompletedSession('WAT', 'Random 60 Drill', 'Completed');

      document.getElementById('watActiveScreen').style.display = 'none';
      document.getElementById('watReviewScreen').style.display = 'block';

      const tbody = document.getElementById('watReviewTbody');
      tbody.innerHTML = '';
      const list = watWords.slice(0, Math.max(watIndex, 1));
      list.forEach((w, i) => {{
        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid var(--border-subtle)';
        tr.innerHTML = `
          <td style="padding: 0.65rem 1rem; color: var(--text-tertiary); font-family: var(--font-mono); font-size: 0.85rem;">${{i + 1}}</td>
          <td style="padding: 0.65rem 1rem; color: var(--accent-brass); font-weight: 700; font-family: var(--font-tactical); font-size: 1.1rem; letter-spacing: 0.5px;">${{w}}</td>
          <td style="padding: 0.65rem 1rem;">${{escapeHtml(watResponses[w] || (watMode === 'typing' ? '—' : 'Written in notebook'))}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function copyWatResponses() {{
      let t = "=== WAT RESPONSES ===\\n";
      watWords.slice(0, Math.max(watIndex, 1)).forEach((w, i) => {{
        t += `${{i + 1}}. [${{w}}] => ${{watResponses[w] || 'Written on paper'}}\\n`;
      }});
      navigator.clipboard.writeText(t).then(() => showToast("RESPONSES COPIED TO CLIPBOARD"));
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
      document.getElementById('tatModePaper').classList.toggle('selected', m === 'paper');
      document.getElementById('tatModeTyping').classList.toggle('selected', m === 'typing');
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
        tatSlides.push({{ num: 12, type: 'blank', src: '', label: 'Slide 12 — Blank Slide (Candidate Story)' }});
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
        badge.className = 'phase-pill observe';
        badge.textContent = `Observation Phase (${{tatViewDuration}}s)`;
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
        playAudioBeep(680, 0.12);
      }} else {{
        badge.className = 'phase-pill write';
        badge.textContent = `Narrative Phase (${{Math.floor(tatWriteDuration/60)}} Mins)`;
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
        playAudioBeep(520, 0.2);
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
          if (tatPhase === 'viewing') startTatPhase('writing');
          else advanceTatSlide();
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
      if (tatPhase === 'viewing') startTatPhase('writing');
      else advanceTatSlide();
    }}

    function advanceTatSlide() {{
      recordTatStory();
      tatIndex++;
      if (tatIndex >= tatSlides.length) finishTatTest();
      else commenceTatSlide();
    }}

    function toggleTatPause() {{
      tatPaused = !tatPaused;
      document.getElementById('tatPauseLabel').textContent = tatPaused ? 'Resume' : 'Pause';
    }}

    function abortTatTest() {{
      if (confirm("Terminate TAT session? Completed stories will be preserved.")) finishTatTest();
    }}

    function finishTatTest() {{
      clearInterval(tatInterval);
      if (tatCurrentSetId) markTatSetDone(tatCurrentSetId);
      else logCompletedSession('TAT', 'Random 11+Blank Drill', 'Completed');

      document.getElementById('tatActiveScreen').style.display = 'none';
      document.getElementById('tatReviewScreen').style.display = 'block';

      const wrap = document.getElementById('tatReviewList');
      wrap.innerHTML = '';
      tatSlides.slice(0, Math.max(tatIndex, 1)).forEach(s => {{
        const card = document.createElement('div');
        card.style = 'background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1.15rem; display: flex; gap: 1.25rem; align-items: flex-start;';
        const imgMarkup = s.type === 'blank' 
          ? '<div style="width: 110px; height: 80px; background: #000; color: #fff; display: flex; align-items: center; justify-content: center; font-family: var(--font-tactical); font-size: 0.9rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">BLANK</div>'
          : `<img src="${{s.src}}" style="width: 110px; height: 80px; object-fit: cover; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">`;
        
        card.innerHTML = `
          ${{imgMarkup}}
          <div style="flex: 1;">
            <strong style="color: var(--accent-brass); font-family: var(--font-tactical); font-size: 1.1rem; letter-spacing: 0.5px;">Slide ${{s.num}}: ${{s.label}}</strong>
            <p style="margin-top: 0.4rem; font-size: 0.92rem; line-height: 1.55; color: var(--text-primary);">${{escapeHtml(tatStories[s.num] || 'Written in booklet')}}</p>
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
      navigator.clipboard.writeText(t).then(() => showToast("STORIES COPIED TO CLIPBOARD"));
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
      document.getElementById('srtModeBooklet').classList.toggle('selected', m === 'booklet');
      document.getElementById('srtModeFlash').classList.toggle('selected', m === 'flash');
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
        item.className = 'srt-entry';
        item.innerHTML = `
          <div class="srt-situation-text">
            <span class="srt-num">#${{idx + 1}}</span>
            ${{sit}}
          </div>
          <input type="text" placeholder="He..." oninput="recordSrtInput(${{idx}}, this.value)">
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
      document.getElementById('srtCompletedCount').textContent = `Attempted: ${{filled}} / ${{srtList.length}}`;
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
          alert("Allotted time (30 minutes) elapsed for Situation Reaction Test.");
          submitSrtTest();
        }}
      }}, 1000);
    }}

    function submitSrtTest() {{
      clearInterval(srtInterval);
      const filled = Object.values(srtResponses).filter(v => v.trim().length > 0).length;
      if (srtCurrentSetId) markSrtSetDone(srtCurrentSetId);
      else logCompletedSession('SRT', `Attempted ${{filled}} Scenarios`, 'Submitted');

      document.getElementById('srtActiveScreen').style.display = 'none';
      document.getElementById('srtReviewScreen').style.display = 'block';
      document.getElementById('srtReviewStats').textContent = `Attempted ${{filled}} / ${{srtList.length}} Scenarios in allotted 30 minutes`;

      const wrap = document.getElementById('srtReviewContent');
      wrap.innerHTML = '';
      srtList.forEach((sit, i) => {{
        const div = document.createElement('div');
        div.style = 'background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1.15rem;';
        div.innerHTML = `
          <strong style="color: var(--text-primary); font-size: 0.95rem;">#${{i + 1}}: ${{sit}}</strong>
          <p style="margin-top: 0.45rem; color: var(--accent-brass); font-size: 0.92rem;">${{escapeHtml(srtResponses[i] || '(Unanswered)')}}</p>
        `;
        wrap.appendChild(div);
      }});
    }}

    function copySrtResponses() {{
      let t = "=== SRT RESPONSES ===\\n";
      srtList.forEach((sit, i) => {{
        t += `${{i + 1}}. ${{sit}} => ${{srtResponses[i] || '(Unanswered)'}}\\n`;
      }});
      navigator.clipboard.writeText(t).then(() => showToast("REACTIONS COPIED TO CLIPBOARD"));
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
            alert("15 Minutes elapsed for Self Description Test.");
            logCompletedSession('SDT', 'Full 5 Paragraphs', 'Completed');
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
      logCompletedSession('SDT', 'Draft Updated', 'Saved');
      showToast("SDT DRAFT PRESERVED IN BROWSER");
    }}

    function copySdtText() {{
      let t = "=== SELF DESCRIPTION TEST (SDT) ===\\n\\n";
      t += "1. PARENTS' OPINION:\\n" + (document.getElementById('sdt1').value || '—') + "\\n\\n";
      t += "2. TEACHERS' OPINION:\\n" + (document.getElementById('sdt2').value || '—') + "\\n\\n";
      t += "3. FRIENDS' OPINION:\\n" + (document.getElementById('sdt3').value || '—') + "\\n\\n";
      t += "4. SELF ASSESSMENT:\\n" + (document.getElementById('sdt4').value || '—') + "\\n\\n";
      t += "5. FUTURE ASPIRATIONS:\\n" + (document.getElementById('sdt5').value || '—') + "\\n";
      navigator.clipboard.writeText(t).then(() => showToast("5 PARAGRAPHS COPIED TO CLIPBOARD"));
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
      logCompletedSession('OIR', file.name, 'PDF Loaded');
    }});

    function generateOmrRows() {{
      const count = parseInt(document.getElementById('oirQuestionCount').value, 10);
      const wrap = document.getElementById('omrRowsList');
      wrap.innerHTML = '';
      oirResponses = {{}};

      for (let i = 1; i <= count; i++) {{
        const row = document.createElement('div');
        row.className = 'omr-line';
        row.innerHTML = `
          <span class="omr-num">${{i}}.</span>
          <div class="bubble-cluster">
            <div class="omr-bubble-cell" onclick="selectOmrBubble(${{i}}, 'A', this)">A</div>
            <div class="omr-bubble-cell" onclick="selectOmrBubble(${{i}}, 'B', this)">B</div>
            <div class="omr-bubble-cell" onclick="selectOmrBubble(${{i}}, 'C', this)">C</div>
            <div class="omr-bubble-cell" onclick="selectOmrBubble(${{i}}, 'D', this)">D</div>
          </div>
        `;
        wrap.appendChild(row);
      }}
      updateOmrAttemptStats();
    }}

    function selectOmrBubble(qNum, opt, el) {{
      const row = el.closest('.omr-line');
      row.querySelectorAll('.omr-bubble-cell').forEach(b => b.classList.remove('filled'));
      el.classList.add('filled');
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
            alert("Allotted OIR testing time expired.");
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
      logCompletedSession('OIR', `${{marked}}/${{total}} Marked`, 'Completed');
      let summary = `OIR Test Complete!\\nMarked: ${{marked}} / ${{total}}\\nUnanswered: ${{total - marked}}\\n\\nCopy response sheet to clipboard?`;
      if (confirm(summary)) {{
        let t = "=== OIR ANSWER SHEET ===\\n";
        for (let i = 1; i <= total; i++) {{
          t += `Q${{i}}: ${{oirResponses[i] || '—'}}\\n`;
        }}
        navigator.clipboard.writeText(t).then(() => showToast("OMR RESPONSES COPIED TO CLIPBOARD"));
      }}
    }}

    // ==============================================================
    // 6. GROUP DISCUSSION (GD) ENGINE
    // ==============================================================
    let gdCurrentScenario = null;
    let gdRemainingSec = 900;
    let gdTotalDuration = 900;
    let gdInterval = null;
    let gdSpeechMuted = false;
    let gdInputMode = 'voice';
    let gdCandidateSpeaking = false;
    let gdCandidateSpeakingSec = 0;
    let gdCandidateInterventions = 0;
    let gdTranscriptHistory = [];
    let gdRecognition = null;
    let gdPeerQueue = [];

    function setGdInputMode(m) {{
      gdInputMode = m;
      document.getElementById('gdModeVoice').classList.toggle('selected', m === 'voice');
      document.getElementById('gdModeText').classList.toggle('selected', m === 'text');
      const txtArea = document.getElementById('gdTextInputArea');
      if (txtArea) txtArea.style.display = m === 'text' ? 'flex' : 'none';
    }}

    function toggleGdAudioMute() {{
      gdSpeechMuted = !gdSpeechMuted;
      document.getElementById('btnToggleGdAudio').textContent = gdSpeechMuted ? 'Unmute Voices' : 'Mute Voices';
      if (gdSpeechMuted && window.speechSynthesis) window.speechSynthesis.cancel();
    }}

    function startGdSession() {{
      const topicChoice = document.getElementById('gdSelectTopic').value;
      gdTotalDuration = parseInt(document.getElementById('gdSelectDuration').value, 10);
      gdRemainingSec = gdTotalDuration;
      gdSpeechMuted = document.getElementById('gdSelectAudio').value === 'voice_off';
      document.getElementById('btnToggleGdAudio').textContent = gdSpeechMuted ? 'Unmute Voices' : 'Mute Voices';

      if (topicChoice === 'random') {{
        const rIdx = Math.floor(Math.random() * GD_TOPICS.length);
        gdCurrentScenario = GD_TOPICS[rIdx];
      }} else {{
        const id = parseInt(topicChoice, 10);
        gdCurrentScenario = GD_TOPICS.find(x => x.id === id) || GD_TOPICS[0];
      }}

      // Init telemetry
      gdCandidateSpeaking = false;
      gdCandidateSpeakingSec = 0;
      gdCandidateInterventions = 0;
      gdTranscriptHistory = [];
      gdPeerQueue = [...gdCurrentScenario.peer_dialogues];

      document.getElementById('gdSetupScreen').style.display = 'none';
      document.getElementById('gdReviewScreen').style.display = 'none';
      document.getElementById('gdActiveScreen').style.display = 'block';

      document.getElementById('gdActiveTitle').textContent = gdCurrentScenario.title;
      document.getElementById('gdActiveCategory').textContent = gdCurrentScenario.category;

      // Populate leads
      document.getElementById('gdLeadBox1').textContent = gdCurrentScenario.leads[0];
      document.getElementById('gdLeadBox2').textContent = gdCurrentScenario.leads[1];
      document.getElementById('gdLeadBox3').textContent = gdCurrentScenario.leads[2];

      document.getElementById('gdTranscriptFeed').innerHTML = `
        <div style="color: var(--text-tertiary); font-size: 0.85rem; text-align: center; margin: 0.5rem 0;">
          GTO has initiated the floor. Topic: "${{gdCurrentScenario.title}}". Listen actively and intervene strategically.
        </div>
      `;

      initSpeechRecognition();
      runGdMasterTimer();
    }}

    function initSpeechRecognition() {{
      if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {{
        const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
        gdRecognition = new SpeechRec();
        gdRecognition.continuous = true;
        gdRecognition.interimResults = true;
        gdRecognition.lang = 'en-IN';

        gdRecognition.onresult = (event) => {{
          let interimTranscript = '';
          for (let i = event.resultIndex; i < event.results.length; ++i) {{
            if (event.results[i].isFinal) {{
              const finalTxt = event.results[i][0].transcript.trim();
              if (finalTxt.length > 0) recordCandidateContribution(finalTxt);
            }}
          }}
        }};
      }}
    }}

    function runGdMasterTimer() {{
      clearInterval(gdInterval);
      gdInterval = setInterval(() => {{
        gdRemainingSec--;
        const elapsedSec = gdTotalDuration - gdRemainingSec;
        const m = Math.floor(gdRemainingSec / 60);
        const s = gdRemainingSec % 60;
        document.getElementById('gdMasterTimer').textContent = `${{String(m).padStart(2, '0')}}:${{String(s).padStart(2, '0')}}`;

        if (gdCandidateSpeaking) {{
          gdCandidateSpeakingSec++;
        }}

        updateAirtimeTelemetry();
        checkLeadPhase(elapsedSec);
        checkPeerDialogueQueue(elapsedSec);

        if (gdRemainingSec <= 0) {{
          clearInterval(gdInterval);
          finishGdSession();
        }}
      }}, 1000);
    }}

    function checkLeadPhase(elapsedSec) {{
      const third = Math.floor(gdTotalDuration / 3);
      const b1 = document.getElementById('gdLeadBox1');
      const b2 = document.getElementById('gdLeadBox2');
      const b3 = document.getElementById('gdLeadBox3');
      const tag = document.getElementById('gdPhaseLeadTag');

      if (elapsedSec < third) {{
        b1.classList.add('active'); b2.classList.remove('active'); b3.classList.remove('active');
        tag.textContent = 'Focusing on Lead 1';
      }} else if (elapsedSec < third * 2) {{
        b1.classList.remove('active'); b2.classList.add('active'); b3.classList.remove('active');
        tag.textContent = 'Progressed to Lead 2';
      }} else {{
        b1.classList.remove('active'); b2.classList.remove('active'); b3.classList.add('active');
        tag.textContent = 'Consensus on Lead 3';
      }}
    }}

    function checkPeerDialogueQueue(elapsedSec) {{
      if (gdCandidateSpeaking) return; // Yield when candidate is speaking
      if (gdPeerQueue.length === 0) return;

      const nextItem = gdPeerQueue[0];
      if (elapsedSec >= nextItem.time_sec) {{
        gdPeerQueue.shift();
        triggerPeerSpeech(nextItem.speaker, nextItem.text);
      }}
    }}

    function triggerPeerSpeech(speaker, text) {{
      setAvatarSpeaking(speaker, true);
      addFeedEntry('peer', speaker, text);

      if (!gdSpeechMuted && window.speechSynthesis) {{
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'en-IN';
        if (speaker === 'Chest 2') {{ utterance.pitch = 1.0; utterance.rate = 1.05; }}
        else if (speaker === 'Chest 4') {{ utterance.pitch = 1.15; utterance.rate = 1.15; }}
        else if (speaker === 'Chest 7') {{ utterance.pitch = 0.9; utterance.rate = 0.95; }}
        else {{ utterance.pitch = 1.0; utterance.rate = 1.0; }}

        utterance.onend = () => setAvatarSpeaking(speaker, false);
        utterance.onerror = () => setAvatarSpeaking(speaker, false);
        window.speechSynthesis.speak(utterance);
      }} else {{
        setTimeout(() => setAvatarSpeaking(speaker, false), 5000);
      }}
    }}

    function setAvatarSpeaking(speaker, isSpeaking) {{
      const map = {{
        'Chest 2': {{ el: 'avatarChest2', st: 'statusChest2' }},
        'Chest 4': {{ el: 'avatarChest4', st: 'statusChest4' }},
        'Chest 7': {{ el: 'avatarChest7', st: 'statusChest7' }},
        'Chest 9': {{ el: 'avatarChest9', st: 'statusChest9' }}
      }};
      const target = map[speaker];
      if (target) {{
        const node = document.getElementById(target.el);
        const statusNode = document.getElementById(target.st);
        if (node) node.classList.toggle('speaking', isSpeaking);
        if (statusNode) statusNode.textContent = isSpeaking ? 'Speaking' : 'Listening';
      }}
    }}

    function toggleCandidateIntervention() {{
      gdCandidateSpeaking = !gdCandidateSpeaking;
      const btn = document.getElementById('btnIntervene');
      const avatarYou = document.getElementById('avatarYou');
      const statusYou = document.getElementById('statusYou');

      if (gdCandidateSpeaking) {{
        gdCandidateInterventions++;
        if (window.speechSynthesis) window.speechSynthesis.cancel();
        clearAllPeerSpeakingStyles();

        btn.textContent = 'Yield Floor / Finished Speaking';
        btn.style.background = 'var(--accent-alert)';
        avatarYou.classList.add('speaking');
        statusYou.textContent = 'Floor Held';

        if (gdRecognition) {{
          try {{ gdRecognition.start(); }} catch(e) {{}}
        }}
      }} else {{
        btn.textContent = 'Intervene & Speak (Microphone)';
        btn.style.background = 'var(--accent-ready)';
        avatarYou.classList.remove('speaking');
        statusYou.textContent = 'Floor Free';

        if (gdRecognition) {{
          try {{ gdRecognition.stop(); }} catch(e) {{}}
        }}
      }}
    }}

    function clearAllPeerSpeakingStyles() {{
      ['avatarChest2', 'avatarChest4', 'avatarChest7', 'avatarChest9'].forEach(id => {{
        const node = document.getElementById(id);
        if (node) node.classList.remove('speaking');
      }});
      ['statusChest2', 'statusChest4', 'statusChest7', 'statusChest9'].forEach(id => {{
        const node = document.getElementById(id);
        if (node) node.textContent = 'Listening';
      }});
    }}

    function submitCandidateTextArgument() {{
      const inp = document.getElementById('gdTextInput');
      const txt = inp.value.trim();
      if (!txt) return;
      recordCandidateContribution(txt);
      inp.value = '';
    }}

    function recordCandidateContribution(txt) {{
      addFeedEntry('you', 'YOU (Candidate)', txt);
      gdCandidateSpeakingSec += 8; // Credit text points as airtime
      updateAirtimeTelemetry();
    }}

    function addFeedEntry(type, speaker, text) {{
      const feed = document.getElementById('gdTranscriptFeed');
      const div = document.createElement('div');
      div.className = `feed-entry ${{type}}`;
      div.innerHTML = `
        <div class="feed-meta">
          <span>${{speaker}}</span>
          <span style="font-size: 0.75rem; color: var(--text-tertiary);">${{getFormattedTimestamp()}}</span>
        </div>
        <div>${{escapeHtml(text)}}</div>
      `;
      feed.appendChild(div);
      feed.scrollTop = feed.scrollHeight;
      gdTranscriptHistory.push({{ speaker: speaker, text: text }});
    }}

    function updateAirtimeTelemetry() {{
      const elapsed = Math.max(gdTotalDuration - gdRemainingSec, 1);
      const pct = Math.min(Math.round((gdCandidateSpeakingSec / elapsed) * 100), 100);
      document.getElementById('gdAirtimePercent').textContent = `${{pct}}%`;
      document.getElementById('gdAirtimeFill').style.width = `${{pct}}%`;

      const advice = document.getElementById('gdAirtimeAdvice');
      if (pct < 10) advice.textContent = 'Low participation — step in soon';
      else if (pct <= 25) advice.textContent = 'Optimal participation window (15% - 22%)';
      else advice.textContent = 'High airtime — allow peers to contribute';
    }}

    function abortGdSession() {{
      if (confirm("Terminate Group Discussion session? Current contributions will be logged.")) finishGdSession();
    }}

    function finishGdSession() {{
      clearInterval(gdInterval);
      if (window.speechSynthesis) window.speechSynthesis.cancel();
      if (gdRecognition) {{
        try {{ gdRecognition.stop(); }} catch(e) {{}}
      }}

      const elapsed = Math.max(gdTotalDuration - gdRemainingSec, 1);
      const pct = Math.min(Math.round((gdCandidateSpeakingSec / elapsed) * 100), 100);
      markGdDone(gdCurrentScenario.title, pct);

      document.getElementById('gdActiveScreen').style.display = 'none';
      document.getElementById('gdReviewScreen').style.display = 'block';

      document.getElementById('gdReviewSummary').textContent = `Topic: "${{gdCurrentScenario.title}}" | Completed in ${{Math.floor(elapsed/60)}} mins`;
      document.getElementById('telemetryInterventions').textContent = gdCandidateInterventions;
      document.getElementById('telemetryAirtime').textContent = `${{pct}}%`;

      const wrap = document.getElementById('gdReviewTranscript');
      wrap.innerHTML = '';
      if (gdTranscriptHistory.length === 0) {{
        wrap.innerHTML = '<div style="color: var(--text-tertiary); text-align: center;">No dialogue recorded during this session.</div>';
      }} else {{
        gdTranscriptHistory.forEach(item => {{
          const p = document.createElement('div');
          p.style.marginBottom = '0.75rem';
          const isYou = item.speaker.includes('YOU');
          p.innerHTML = `<strong style="color: ${{isYou ? 'var(--accent-ready)' : 'var(--accent-brass)'}};">${{item.speaker}}:</strong> ${{escapeHtml(item.text)}}`;
          wrap.appendChild(p);
        }});
      }}
    }}

    function copyGdTranscript() {{
      let t = `=== GROUP DISCUSSION TRANSCRIPT ===\\nTopic: ${{gdCurrentScenario.title}}\\n\\n`;
      gdTranscriptHistory.forEach(item => {{
        t += `[${{item.speaker}}]: ${{item.text}}\\n\\n`;
      }});
      navigator.clipboard.writeText(t).then(() => showToast("GD TRANSCRIPT COPIED"));
    }}

    function copyGdAiPrompt() {{
      const prompt = buildGdAiPrompt();
      navigator.clipboard.writeText(prompt).then(() => showToast("GTO EVALUATION PROMPT COPIED"));
    }}

    function downloadGdAiDossier() {{
      const prompt = buildGdAiPrompt();
      downloadTextFile(`GD_Evaluation_Dossier_${{gdCurrentScenario.id}}.txt`, prompt);
    }}

    function buildGdAiPrompt() {{
      let t = `Act as an expert Senior Services Selection Board Group Testing Officer (GTO) evaluating a candidate for the Indian Armed Forces in a Group Discussion (GD).\\n\\n`;
      t += `TOPIC: "${{gdCurrentScenario.title}}" [Category: ${{gdCurrentScenario.category}}]\\n`;
      t += `GTO LEADS:\\n1. ${{gdCurrentScenario.leads[0]}}\\n2. ${{gdCurrentScenario.leads[1]}}\\n3. ${{gdCurrentScenario.leads[2]}}\\n\\n`;
      t += `CANDIDATE TELEMETRY:\\n- Interventions Made: ${{gdCandidateInterventions}}\\n- Airtime Share: ${{Math.round((gdCandidateSpeakingSec / Math.max(gdTotalDuration - gdRemainingSec, 1)) * 100)}}% (Ideal: 15% - 22%)\\n\\n`;
      t += `COMPLETE SYNDICATE DISCUSSION TRANSCRIPT:\\n`;
      gdTranscriptHistory.forEach(item => {{
        t += `[${{item.speaker}}]: ${{item.text}}\\n`;
      }});
      t += `\\n### GTO EVALUATION DIRECTIVES:\\n`;
      t += `1. **OLQ Assessment**: Assess Reasoning Ability, Power of Expression, Ability to Influence the Group, and Cooperation.\\n`;
      t += `2. **Substance vs Rhetoric**: Did the candidate cite facts and logical frameworks, or speak superficial generic generalities?\\n`;
      t += `3. **Group Dynamics**: Did the candidate listen and build on peer points, or talk over others aggressively?\\n`;
      t += `4. **Model Officer Interventions**: Provide 2 exemplary, high-impact statements showing how a recommended candidate would have guided this debate.\\n`;
      t += `5. **GTO Verdict**: (Recommended / Borderline / Not Recommended) with concrete remediation advice.\\n`;
      return t;
    }}

    function resetGdToSetup() {{
      document.getElementById('gdReviewScreen').style.display = 'none';
      document.getElementById('gdSetupScreen').style.display = 'block';
    }}

    // ==============================================================
    // 7. LECTURETTE ENGINE (250+ TOPICS)
    // ==============================================================
    let lecCurrentCard = null;
    let lecSelectedTopic = null;
    let lecPrepRemaining = 180;
    let lecPrepInterval = null;
    let lecDeliveryRemaining = 180;
    let lecDeliveryInterval = null;
    let lecWebcamStream = null;
    let lecRecognition = null;
    let lecTranscribedSpeech = '';

    function shuffleLecturetteCard() {{
      const cards = LECTURETTE_DATA.cards;
      const rIdx = Math.floor(Math.random() * cards.length);
      renderLecturetteCard(cards[rIdx]);
    }}

    function renderLecturetteCard(card) {{
      lecCurrentCard = card;
      document.getElementById('lecCardTitle').textContent = card.title;
      const wrap = document.getElementById('lecCardTopicsList');
      wrap.innerHTML = '';

      card.topics.forEach((item, idx) => {{
        const row = document.createElement('div');
        row.className = `topic-tier-row ${{idx === 0 ? 'selected' : ''}}`;
        if (idx === 0) lecSelectedTopic = item;

        row.onclick = () => {{
          wrap.querySelectorAll('.topic-tier-row').forEach(r => r.classList.remove('selected'));
          row.classList.add('selected');
          lecSelectedTopic = item;
        }};

        row.innerHTML = `
          <div>
            <strong style="color: var(--text-primary); font-size: 0.95rem;">${{item.topic}}</strong>
            <div style="font-size: 0.78rem; color: var(--text-tertiary);">${{item.tier_name}}</div>
          </div>
          <span class="tier-tag tier-${{item.tier}}">Tier ${{item.tier}}</span>
        `;
        wrap.appendChild(row);
      }});
    }}

    function filterLecturetteTopics() {{
      const q = document.getElementById('lecSearchInput').value.trim().toLowerCase();
      const tierFilter = document.getElementById('lecFilterTier').value;
      const resultsWrap = document.getElementById('lecSearchResults');
      resultsWrap.innerHTML = '';

      if (!q && tierFilter === 'all') {{
        resultsWrap.innerHTML = '<div style="font-size: 0.8rem; color: var(--text-tertiary);">Type in the box above to filter 251 topics.</div>';
        return;
      }}

      let matches = [];
      const tiers = LECTURETTE_DATA.tiers;

      ['tier1', 'tier2', 'tier3', 'tier4'].forEach(tKey => {{
        if (tierFilter === 'all' || tierFilter === tKey) {{
          tiers[tKey].forEach(topicStr => {{
            if (!q || topicStr.toLowerCase().includes(q)) {{
              const tierNum = tKey.replace('tier', '');
              matches.push({{ topic: topicStr, tier: tierNum }});
            }}
          }});
        }}
      }});

      if (matches.length === 0) {{
        resultsWrap.innerHTML = '<div style="font-size: 0.8rem; color: var(--text-tertiary);">No matching topics found.</div>';
        return;
      }}

      matches.slice(0, 20).forEach(m => {{
        const item = document.createElement('div');
        item.style = 'background: var(--bg-base); border: 1px solid var(--border-subtle); padding: 0.45rem 0.75rem; border-radius: var(--radius-sm); font-size: 0.85rem; display: flex; justify-content: space-between; align-items: center; cursor: pointer;';
        item.innerHTML = `<span>${{m.topic}}</span> <span class="tier-tag tier-${{m.tier}}">Tier ${{m.tier}}</span>`;
        item.onclick = () => {{
          lecSelectedTopic = {{ topic: m.topic, tier: m.tier, tier_name: `Tier ${{m.tier}} Topic` }};
          showToast(`Selected: ${{m.topic}}`);
          startLecturetteFlow();
        }};
        resultsWrap.appendChild(item);
      }});
    }}

    function startLecturetteFlow() {{
      if (!lecSelectedTopic) lecSelectedTopic = lecCurrentCard ? lecCurrentCard.topics[0] : {{ topic: 'Cyber Warfare', tier: 1 }};
      const prepChoice = parseInt(document.getElementById('lecPrepDuration').value, 10);

      document.getElementById('lecSetupScreen').style.display = 'none';
      document.getElementById('lecReviewScreen').style.display = 'none';

      if (prepChoice === 0) {{
        advanceToLecturetteDelivery();
      }} else {{
        document.getElementById('lecPrepScreen').style.display = 'block';
        document.getElementById('lecPrepTopicTitle').textContent = lecSelectedTopic.topic;
        lecPrepRemaining = prepChoice;
        runLecturettePrepTimer();
      }}
    }}

    function runLecturettePrepTimer() {{
      clearInterval(lecPrepInterval);
      updateLecturettePrepUI();

      lecPrepInterval = setInterval(() => {{
        lecPrepRemaining--;
        updateLecturettePrepUI();

        if (lecPrepRemaining <= 0) {{
          clearInterval(lecPrepInterval);
          advanceToLecturetteDelivery();
        }}
      }}, 1000);
    }}

    function updateLecturettePrepUI() {{
      const m = Math.floor(lecPrepRemaining / 60);
      const s = lecPrepRemaining % 60;
      document.getElementById('lecPrepClockNum').textContent = `${{m}}:${{String(s).padStart(2, '0')}}`;
      const circle = document.getElementById('lecPrepClockCircle');
      const offset = 226 - (lecPrepRemaining / 180) * 226;
      circle.style.strokeDashoffset = offset;
    }}

    function advanceToLecturetteDelivery() {{
      clearInterval(lecPrepInterval);
      document.getElementById('lecPrepScreen').style.display = 'none';
      document.getElementById('lecDeliveryScreen').style.display = 'block';

      document.getElementById('lecDeliveryTopicTitle').textContent = lecSelectedTopic.topic;
      lecDeliveryRemaining = 180;
      lecTranscribedSpeech = '';
      document.getElementById('lecLiveTranscript').textContent = 'Listening... Speak clearly. Warning bell at 2:30.';

      initLecturetteSpeechRec();

      const mirrorOpt = document.getElementById('lecMirrorOption').value;
      if (mirrorOpt === 'mirror_on') startWebcamMirror();

      runLecturetteDeliveryTimer();
    }}

    function startWebcamMirror() {{
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {{
        navigator.mediaDevices.getUserMedia({{ video: true, audio: false }})
          .then(stream => {{
            lecWebcamStream = stream;
            const video = document.getElementById('lecWebcamVideo');
            video.srcObject = stream;
          }})
          .catch(err => console.warn('Webcam permission not granted:', err));
      }}
    }}

    function stopWebcamMirror() {{
      if (lecWebcamStream) {{
        lecWebcamStream.getTracks().forEach(t => t.stop());
        lecWebcamStream = null;
      }}
    }}

    function initLecturetteSpeechRec() {{
      if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {{
        const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
        lecRecognition = new SpeechRec();
        lecRecognition.continuous = true;
        lecRecognition.interimResults = true;
        lecRecognition.lang = 'en-IN';

        lecRecognition.onresult = (event) => {{
          let interim = '';
          for (let i = event.resultIndex; i < event.results.length; ++i) {{
            if (event.results[i].isFinal) {{
              lecTranscribedSpeech += event.results[i][0].transcript.trim() + ' ';
            }} else {{
              interim += event.results[i][0].transcript;
            }}
          }}
          document.getElementById('lecLiveTranscript').textContent = lecTranscribedSpeech + (interim ? ` (${{interim}}...)` : '');
        }};

        try {{ lecRecognition.start(); }} catch(e) {{}}
      }}
    }}

    function runLecturetteDeliveryTimer() {{
      clearInterval(lecDeliveryInterval);
      updateLecturetteDeliveryUI();

      lecDeliveryInterval = setInterval(() => {{
        lecDeliveryRemaining--;
        updateLecturetteDeliveryUI();

        // 2:30 mark (30 seconds remaining)
        if (lecDeliveryRemaining === 30) {{
          playBellChime(1); // Single chime
          document.getElementById('lecBellStatus').textContent = 'WARNING BELL RING: 30 seconds remaining!';
          document.getElementById('lecBellStatus').style.color = 'var(--accent-alert)';
        }}

        // 3:00 mark (Time up)
        if (lecDeliveryRemaining <= 0) {{
          clearInterval(lecDeliveryInterval);
          playBellChime(2); // Double chime
          alert("Time is up! 3 Minutes elapsed for Lecturette.");
          finishLecturette();
        }}
      }}, 1000);
    }}

    function updateLecturetteDeliveryUI() {{
      const m = Math.floor(lecDeliveryRemaining / 60);
      const s = lecDeliveryRemaining % 60;
      document.getElementById('lecDeliveryClockNum').textContent = `${{m}}:${{String(s).padStart(2, '0')}}`;
      const circle = document.getElementById('lecDeliveryClockCircle');
      const offset = 226 - (lecDeliveryRemaining / 180) * 226;
      circle.style.strokeDashoffset = offset;
    }}

    function playBellChime(count = 1) {{
      for (let i = 0; i < count; i++) {{
        setTimeout(() => {{
          try {{
            const ctx = new (window.AudioContext || window.webkitAudioContext)();
            const osc1 = ctx.createOscillator();
            const osc2 = ctx.createOscillator();
            const gain = ctx.createGain();

            osc1.type = 'sine';
            osc1.frequency.setValueAtTime(880, ctx.currentTime);
            osc2.type = 'sine';
            osc2.frequency.setValueAtTime(1760, ctx.currentTime);

            gain.gain.setValueAtTime(0.35, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.2);

            osc1.connect(gain);
            osc2.connect(gain);
            gain.connect(ctx.destination);

            osc1.start(); osc2.start();
            osc1.stop(ctx.currentTime + 1.2);
            osc2.stop(ctx.currentTime + 1.2);
          }} catch(e) {{}}
        }}, i * 400);
      }}
    }}

    function abortLecturette() {{
      if (confirm("Terminate Lecturette drill?")) {{
        clearInterval(lecPrepInterval);
        clearInterval(lecDeliveryInterval);
        stopWebcamMirror();
        if (lecRecognition) try {{ lecRecognition.stop(); }} catch(e) {{}}
        resetLecturetteToSetup();
      }}
    }}

    function finishLecturette() {{
      clearInterval(lecDeliveryInterval);
      stopWebcamMirror();
      if (lecRecognition) try {{ lecRecognition.stop(); }} catch(e) {{}}

      markLecturetteDone(lecSelectedTopic.topic);

      document.getElementById('lecDeliveryScreen').style.display = 'none';
      document.getElementById('lecReviewScreen').style.display = 'block';

      document.getElementById('lecReviewTopic').textContent = lecSelectedTopic.topic;
      document.getElementById('lecReviewSubtitle').textContent = `Delivered under 3-minute exam conditions.`;
      document.getElementById('lecFinalTranscriptBox').textContent = lecTranscribedSpeech.trim() || '(Speech transcribed or delivered verbally. Use prompt below to generate model lecturette).';
    }}

    function copyLecturetteTranscript() {{
      navigator.clipboard.writeText(lecTranscribedSpeech.trim() || 'No speech recorded').then(() => showToast("LECTURETTE TRANSCRIPT COPIED"));
    }}

    function copyLecturetteAiPrompt() {{
      const prompt = buildLecturetteAiPrompt();
      navigator.clipboard.writeText(prompt).then(() => showToast("GTO LECTURETTE PROMPT COPIED"));
    }}

    function downloadLecturetteAiDossier() {{
      const prompt = buildLecturetteAiPrompt();
      downloadTextFile(`Lecturette_Evaluation_${{lecSelectedTopic.topic.replace(/\\s+/g, '_')}}.txt`, prompt);
    }}

    function buildLecturetteAiPrompt() {{
      let t = `Act as an expert Senior Services Selection Board Group Testing Officer (GTO) evaluating a candidate for the Indian Armed Forces in a Lecturette.\\n\\n`;
      t += `TOPIC: "${{lecSelectedTopic.topic}}" [Tier: ${{lecSelectedTopic.tier}} - ${{lecSelectedTopic.tier_name || ''}}]\\n`;
      t += `DELIVERY TIME: 3 Minutes (Standard DIPR format)\\n\\n`;
      t += `CANDIDATE'S PREPARATION SCRATCHPAD NOTES:\\n${{document.getElementById('lecScratchpad').value || '(Mental outline without written notes)'}}\\n\\n`;
      t += `CANDIDATE'S TRANSCRIBED SPEECH:\\n${{lecTranscribedSpeech.trim() || '(Delivered verbally in exam hall)'}}\\n\\n`;
      t += `### GTO EVALUATION DIRECTIVES:\\n`;
      t += `1. **Structural Coherence**: Did the speech follow a clear progression: Introduction (30s) ➔ Key Dimensions & Facts (90s) ➔ Challenges & Ground Realities (30s) ➔ Officer's Constructive Conclusion (30s)?\\n`;
      t += `2. **Knowledge Depth & Facts**: Did the candidate present specific data, historical context, and geopolitical/national significance, or superficial commentary?\\n`;
      t += `3. **Power of Expression**: Evaluate clarity, vocabulary, pace, and conviction.\\n`;
      t += `4. **Model Officer Lecturette Speech**: Provide a complete, 3-minute, spoken-word military-grade model lecturette for this topic.\\n`;
      t += `5. **GTO Verdict & Targeted Recommendations**.\\n`;
      return t;
    }}

    function resetLecturetteToSetup() {{
      document.getElementById('lecReviewScreen').style.display = 'none';
      document.getElementById('lecSetupScreen').style.display = 'block';
    }}

    // ==============================================================
    // 8. FULL MOCK BATTERY LAUNCHER
    // ==============================================================
    function launchFullMockBattery() {{
      if (confirm("Commence Full Stage 2 Psychological & GTO Mock Test?\\n\\nSchedule:\\n1. 12 TAT Stories (approx 50 mins)\\n2. 60 WAT Words (15 mins)\\n3. 60 SRT Scenarios (30 mins)\\n4. 5 SDT Paragraphs (15 mins)\\n5. 15-Min Syndicate Group Discussion\\n6. 3-Min Lecturette Delivery")) {{
        document.querySelector('[data-tab="tab-tat"]').click();
        startTatTest();
      }}
    }}

    // ==============================================================
    // 9. AI EVALUATION PROMPT GENERATORS & DOWNLOADERS
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
      t += `3. **Flagged Weak Reactions & Officer-Grade Rewrites** (Concise, action-oriented military answers).\\n`;
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
      t += `1. **Triangulation Check**: Consistency across Parents, Teachers, Friends, and Self assessment.\\n`;
      t += `2. **Authenticity vs Fake Pre-Coaching**: Are the weaknesses genuine and modifiable?\\n`;
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

    function copyWatAiPrompt() {{
      const list = watWords.slice(0, Math.max(watIndex, 1));
      const prompt = generateWatPrompt(list, watResponses, watCurrentSetId ? `WAT Set ${{watCurrentSetId}}` : 'WAT Custom Set');
      navigator.clipboard.writeText(prompt).then(() => showToast("WAT EVALUATION PROMPT COPIED"));
    }}

    function downloadWatAiDossier() {{
      const list = watWords.slice(0, Math.max(watIndex, 1));
      const prompt = generateWatPrompt(list, watResponses, watCurrentSetId ? `WAT Set ${{watCurrentSetId}}` : 'WAT Custom Set');
      downloadTextFile(`WAT_Evaluation_Dossier_Set_${{watCurrentSetId || 'session'}}.txt`, prompt);
    }}

    function copyTatAiPrompt() {{
      const slides = tatSlides.slice(0, Math.max(tatIndex, 1));
      const prompt = generateTatPrompt(slides, tatStories, tatCurrentSetId ? `TAT Set ${{tatCurrentSetId}}` : 'TAT Custom Set');
      navigator.clipboard.writeText(prompt).then(() => showToast("TAT PROMPT & STORIES COPIED"));
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
        btn.innerHTML = 'Zipping Images + Prompt...';
        btn.disabled = true;
      }}

      try {{
        if (typeof JSZip === 'undefined') throw new Error("JSZip library initializing. Please retry in 2 seconds.");

        const zip = new JSZip();
        const folder = zip.folder(`SSB_TAT_Set_${{setId}}_Package`);

        let slidesToPack = [];
        if (!customSetId && tatSlides.length > 0) slidesToPack = tatSlides.slice(0, Math.max(tatIndex, 1));
        else {{
          const target = TAT_SETS.find(s => s.id === setId) || TAT_SETS[0];
          slidesToPack = target.slides;
        }}

        const promptText = generateTatPrompt(slidesToPack, tatStories, `TAT Set ${{setId}}`);
        folder.file(`DIPR_TAT_Evaluation_Prompt.txt`, promptText);

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

        alert("TAT AI Package Downloaded!\\n\\nContains:\\n1. Slide images (.jpg)\\n2. DIPR Senior Psychologist Evaluation Prompt\\n\\nUpload the images and paste the prompt into ChatGPT, Claude, or Gemini for a free psychological assessment.");
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

    function copySrtAiPrompt() {{
      const prompt = generateSrtPrompt(srtList, srtResponses, srtCurrentSetId ? `SRT Set ${{srtCurrentSetId}}` : 'SRT Custom Set');
      navigator.clipboard.writeText(prompt).then(() => showToast("SRT EVALUATION PROMPT COPIED"));
    }}

    function downloadSrtAiDossier() {{
      const prompt = generateSrtPrompt(srtList, srtResponses, srtCurrentSetId ? `SRT Set ${{srtCurrentSetId}}` : 'SRT Custom Set');
      downloadTextFile(`SRT_Evaluation_Dossier_Set_${{srtCurrentSetId || 'session'}}.txt`, prompt);
    }}

    function copySdtAiPrompt() {{
      const p1 = document.getElementById('sdt1').value;
      const p2 = document.getElementById('sdt2').value;
      const p3 = document.getElementById('sdt3').value;
      const p4 = document.getElementById('sdt4').value;
      const p5 = document.getElementById('sdt5').value;
      const prompt = generateSdtPrompt(p1, p2, p3, p4, p5);
      navigator.clipboard.writeText(prompt).then(() => showToast("SDT EVALUATION PROMPT COPIED"));
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

    // ON-DEMAND AI HUB
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
        document.getElementById('btnHubDownload').textContent = 'Download Slide Images & Prompt (ZIP)';
      }} else if (type === 'wat') {{
        WAT_SETS.forEach(s => {{
          const opt = document.createElement('option');
          opt.value = s.id;
          opt.textContent = `WAT Set ${{s.id}} (${{s.count}} Words: ${{s.preview}})`;
          sel.appendChild(opt);
        }});
        document.getElementById('btnHubDownload').textContent = 'Download Word List & Prompt (.txt)';
      }} else if (type === 'srt') {{
        [1, 2].forEach(n => {{
          const opt = document.createElement('option');
          opt.value = n;
          opt.textContent = `SRT Official Set ${{n}} (60 Scenarios)`;
          sel.appendChild(opt);
        }});
        document.getElementById('btnHubDownload').textContent = 'Download Scenarios & Prompt (.txt)';
      }} else if (type === 'sdt') {{
        const opt = document.createElement('option');
        opt.value = '1';
        opt.textContent = 'Standard DIPR 5-Paragraph Self Description';
        sel.appendChild(opt);
        document.getElementById('btnHubDownload').textContent = 'Download SDT Framework & Prompt (.txt)';
      }} else if (type === 'gd') {{
        GD_TOPICS.forEach(sc => {{
          const opt = document.createElement('option');
          opt.value = sc.id;
          opt.textContent = `${{sc.title}} [${{sc.category}}]`;
          sel.appendChild(opt);
        }});
        document.getElementById('btnHubDownload').textContent = 'Download GD Scenario & GTO Prompt (.txt)';
      }} else if (type === 'lecturette') {{
        LECTURETTE_DATA.cards.forEach(c => {{
          const opt = document.createElement('option');
          opt.value = c.card_id;
          opt.textContent = `${{c.title}}: ${{c.topics[0].topic}}...`;
          sel.appendChild(opt);
        }});
        document.getElementById('btnHubDownload').textContent = 'Download Card Topics & GTO Prompt (.txt)';
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
      }} else if (type === 'gd') {{
        const sc = GD_TOPICS.find(x => x.id === val) || GD_TOPICS[0];
        let p = `Act as an expert Senior GTO evaluating a Group Discussion on: "${{sc.title}}"\\nLEADS:\\n1. ${{sc.leads[0]}}\\n2. ${{sc.leads[1]}}\\n3. ${{sc.leads[2]}}\\n\\n[Paste your discussion transcript or candidate arguments here]`;
        downloadTextFile(`GD_Topic_${{val}}_Dossier.txt`, p);
      }} else if (type === 'lecturette') {{
        const card = LECTURETTE_DATA.cards.find(x => x.card_id === val) || LECTURETTE_DATA.cards[0];
        let p = `Act as a Senior GTO evaluating a Lecturette presentation.\\nTOPICS:\\n1. ${{card.topics[0].topic}}\\n2. ${{card.topics[1].topic}}\\n3. ${{card.topics[2].topic}}\\n4. ${{card.topics[3].topic}}\\n\\n[Paste your speech transcript or delivery points here]`;
        downloadTextFile(`Lecturette_Card_${{val}}_Dossier.txt`, p);
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
        navigator.clipboard.writeText(prompt).then(() => showToast(`TAT SET ${{val}} PROMPT COPIED`));
      }} else if (type === 'wat') {{
        const s = WAT_SETS.find(x => x.id === val) || WAT_SETS[0];
        const dummyResp = {{}};
        s.words.forEach(w => dummyResp[w] = '(Write or paste your responses here)');
        const prompt = generateWatPrompt(s.words, dummyResp, `WAT Set ${{val}}`);
        navigator.clipboard.writeText(prompt).then(() => showToast(`WAT SET ${{val}} PROMPT COPIED`));
      }} else if (type === 'srt') {{
        const list = val === 1 ? SRT_SETS[0] : SRT_SETS[1];
        const dummyResp = {{}};
        list.forEach((_, i) => dummyResp[i] = '(Write or paste your reaction here)');
        const prompt = generateSrtPrompt(list, dummyResp, `SRT Set ${{val}}`);
        navigator.clipboard.writeText(prompt).then(() => showToast(`SRT SET ${{val}} PROMPT COPIED`));
      }} else if (type === 'sdt') {{
        const prompt = generateSdtPrompt('', '', '', '', '');
        navigator.clipboard.writeText(prompt).then(() => showToast("SDT PROMPT TEMPLATE COPIED"));
      }} else if (type === 'gd') {{
        const sc = GD_TOPICS.find(x => x.id === val) || GD_TOPICS[0];
        let p = `Act as an expert Senior GTO evaluating a Group Discussion on: "${{sc.title}}"\\nLEADS:\\n1. ${{sc.leads[0]}}\\n2. ${{sc.leads[1]}}\\n3. ${{sc.leads[2]}}\\n\\n[Paste your discussion transcript or candidate arguments here]`;
        navigator.clipboard.writeText(p).then(() => showToast(`GD TOPIC ${{val}} PROMPT COPIED`));
      }} else if (type === 'lecturette') {{
        const card = LECTURETTE_DATA.cards.find(x => x.card_id === val) || LECTURETTE_DATA.cards[0];
        let p = `Act as a Senior GTO evaluating a Lecturette presentation.\\nTOPICS:\\n1. ${{card.topics[0].topic}}\\n2. ${{card.topics[1].topic}}\\n3. ${{card.topics[2].topic}}\\n4. ${{card.topics[3].topic}}\\n\\n[Paste your speech transcript or delivery points here]`;
        navigator.clipboard.writeText(p).then(() => showToast(`LECTURETTE CARD ${{val}} PROMPT COPIED`));
      }}
    }}

    // UTILITIES
    function shuffle(arr) {{
      for (let i = arr.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
      }}
    }}

    function escapeHtml(str) {{
      return (str || '').replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    }}

    function playAudioBeep(freq = 640, duration = 0.1) {{
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

    document.getElementById('btnToggleTheme').addEventListener('click', () => {{
      const isLight = document.body.classList.toggle('projector-hall');
      document.getElementById('themeLabel').textContent = isLight ? 'Dark Hall' : 'Projector Hall';
    }});

    document.getElementById('btnToggleFullscreen').addEventListener('click', () => {{
      if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {{}});
      else if (document.exitFullscreen) document.exitFullscreen();
    }});

    // INIT ON LOAD
    updateActiveModuleLabel(document.querySelector('.op-tab.active'));
    generateOmrRows();
    loadProgress();
    shuffleLecturetteCard();
  </script>
</body>
</html>
'''

with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html compiled successfully with GD and Lecturette modules!")
