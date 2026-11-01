import json, os

out_dir = r'C:\Users\Singh\.gemini\antigravity\scratch\ssb-wat-simulator'

with open(os.path.join(out_dir, 'wat_sets.json'), 'r', encoding='utf-8') as f:
    sets_data = json.load(f)

formatted_sets = []
all_words_flat = []

for idx, s in enumerate(sets_data):
    words = [item['word'].upper() for item in s]
    formatted_sets.append({
        'id': idx + 1,
        'title': f'Set {idx + 1}',
        'count': len(words),
        'preview': f"{words[0]} ... {words[-1]}",
        'words': words
    })
    all_words_flat.extend(words)

sets_json_str = json.dumps(formatted_sets)
all_words_json_str = json.dumps(all_words_flat)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SSB DIPR WAT Simulator — Official 800+ Practice Sets</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-primary: #0a0f1d;
      --bg-card: #111a2e;
      --bg-card-border: #1e293b;
      --accent-gold: #f59e0b;
      --accent-gold-glow: rgba(245, 158, 11, 0.25);
      --accent-blue: #38bdf8;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --font-display: 'Cinzel', serif;
      --font-body: 'Inter', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    /* DIPR Projector Light Mode (Official SSB Hall condition) */
    body.dipr-projector {{
      --bg-primary: #f1f5f9;
      --bg-card: #ffffff;
      --bg-card-border: #cbd5e1;
      --accent-gold: #b45309;
      --accent-gold-glow: rgba(180, 83, 9, 0.15);
      --accent-blue: #0284c7;
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
      transition: background-color 0.25s ease, color 0.25s ease;
      overflow-x: hidden;
    }}

    /* Header */
    header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem 2rem;
      border-bottom: 1px solid var(--bg-card-border);
      background: rgba(17, 26, 46, 0.6);
      backdrop-filter: blur(10px);
    }}
    body.dipr-projector header {{
      background: rgba(255, 255, 255, 0.85);
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .brand-badge {{
      background: linear-gradient(135deg, #f59e0b, #d97706);
      color: #000;
      font-weight: 800;
      font-size: 0.85rem;
      padding: 0.25rem 0.6rem;
      border-radius: 4px;
      letter-spacing: 1px;
    }}

    .brand h1 {{
      font-family: var(--font-display);
      font-size: 1.25rem;
      letter-spacing: 1px;
    }}

    .header-actions {{
      display: flex;
      gap: 0.75rem;
      align-items: center;
    }}

    .btn-secondary {{
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      color: var(--text-main);
      padding: 0.5rem 1rem;
      border-radius: 6px;
      font-size: 0.85rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-weight: 500;
      transition: all 0.2s ease;
    }}
    .btn-secondary:hover {{
      border-color: var(--accent-gold);
      color: var(--accent-gold);
    }}

    /* Main Container */
    main {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      width: 100%;
      max-width: 1100px;
      margin: 0 auto;
    }}

    /* Setup Card */
    .setup-card {{
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 12px;
      padding: 2.5rem;
      width: 100%;
      max-width: 720px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }}

    .setup-title {{
      font-size: 1.6rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
      color: var(--text-main);
      text-align: center;
    }}

    .setup-subtitle {{
      color: var(--text-muted);
      text-align: center;
      margin-bottom: 1.75rem;
      font-size: 0.95rem;
      line-height: 1.5;
    }}

    .info-banner {{
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 8px;
      padding: 0.75rem 1rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .info-banner strong {{
      color: var(--accent-blue);
    }}

    .grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
      margin-bottom: 1.5rem;
    }}

    .form-group {{
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }}

    .form-group label {{
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    select, input[type="number"] {{
      background: var(--bg-primary);
      border: 1px solid var(--bg-card-border);
      color: var(--text-main);
      padding: 0.75rem 1rem;
      border-radius: 8px;
      font-size: 0.92rem;
      outline: none;
      transition: border-color 0.2s;
    }}
    select:focus, input[type="number"]:focus {{
      border-color: var(--accent-gold);
    }}

    .badge-count {{
      display: inline-block;
      background: rgba(56, 189, 248, 0.15);
      color: var(--accent-blue);
      padding: 0.25rem 0.6rem;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 600;
      margin-left: 0.5rem;
    }}

    .mode-selector {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 1.5rem;
    }}

    .mode-option {{
      border: 1px solid var(--bg-card-border);
      border-radius: 8px;
      padding: 1rem;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
      transition: all 0.2s ease;
      background: var(--bg-primary);
    }}
    .mode-option.active {{
      border-color: var(--accent-gold);
      background: var(--accent-gold-glow);
    }}
    .mode-option strong {{
      font-size: 0.95rem;
    }}
    .mode-option span {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}

    .options-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2rem;
      padding: 0.75rem 1rem;
      background: var(--bg-primary);
      border-radius: 8px;
      border: 1px solid var(--bg-card-border);
    }}

    .checkbox-label {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.9rem;
      cursor: pointer;
      user-select: none;
    }}

    .btn-start {{
      width: 100%;
      background: linear-gradient(135deg, #f59e0b, #d97706);
      color: #0b1320;
      font-weight: 800;
      font-size: 1.15rem;
      padding: 1rem;
      border-radius: 8px;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 15px rgba(245, 158, 11, 0.4);
      transition: transform 0.15s, box-shadow 0.15s;
      letter-spacing: 0.5px;
    }}
    .btn-start:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(245, 158, 11, 0.5);
    }}

    /* Active Test Screen */
    .test-screen {{
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 100%;
      height: 100%;
      max-width: 900px;
      position: relative;
    }}

    .test-top-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      margin-bottom: 2rem;
      padding: 0 1rem;
    }}

    .counter-tag {{
      font-family: var(--font-mono);
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--accent-gold);
      background: var(--bg-card);
      padding: 0.5rem 1.25rem;
      border-radius: 30px;
      border: 1px solid var(--bg-card-border);
    }}

    .timer-ring-container {{
      position: relative;
      width: 80px;
      height: 80px;
    }}

    .timer-ring-svg {{
      transform: rotate(-90deg);
      width: 80px;
      height: 80px;
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
      stroke-dasharray: 226.2;
      stroke-dashoffset: 0;
      transition: stroke-dashoffset 0.1s linear, stroke 0.3s ease;
    }}

    .timer-number {{
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      font-family: var(--font-mono);
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--text-main);
    }}

    /* Word Box */
    .word-display-card {{
      background: var(--bg-card);
      border: 2px solid var(--bg-card-border);
      border-radius: 16px;
      width: 100%;
      min-height: 260px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 2rem;
      box-shadow: 0 15px 40px rgba(0,0,0,0.3);
      position: relative;
      overflow: hidden;
    }}

    .progress-bar-linear {{
      position: absolute;
      bottom: 0;
      left: 0;
      height: 6px;
      width: 100%;
      background: var(--bg-primary);
    }}

    .progress-bar-fill {{
      height: 100%;
      width: 100%;
      background: linear-gradient(90deg, var(--accent-gold), #ef4444);
      transition: width 0.1s linear;
    }}

    .flashed-word {{
      font-size: clamp(2.5rem, 6.5vw, 5rem);
      font-weight: 800;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: var(--text-main);
      text-align: center;
      user-select: none;
      animation: wordPop 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}

    @keyframes wordPop {{
      0% {{ opacity: 0; transform: scale(0.92); }}
      100% {{ opacity: 1; transform: scale(1); }}
    }}

    /* Typing input for digital practice mode */
    .typing-container {{
      width: 100%;
      margin-top: 1.5rem;
      display: none;
    }}
    .typing-input {{
      width: 100%;
      background: var(--bg-card);
      border: 2px solid var(--bg-card-border);
      color: var(--text-main);
      font-size: 1.15rem;
      padding: 1rem 1.25rem;
      border-radius: 10px;
      outline: none;
      font-family: var(--font-body);
      transition: border-color 0.2s;
    }}
    .typing-input:focus {{
      border-color: var(--accent-gold);
    }}

    /* Test Controls */
    .controls-row {{
      display: flex;
      gap: 1rem;
      margin-top: 2rem;
      align-items: center;
    }}

    .control-btn {{
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      color: var(--text-main);
      padding: 0.75rem 1.4rem;
      border-radius: 8px;
      font-size: 0.95rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.15s ease;
    }}
    .control-btn:hover {{
      border-color: var(--accent-gold);
      color: var(--accent-gold);
    }}

    .control-btn.btn-danger:hover {{
      border-color: #ef4444;
      color: #ef4444;
    }}

    /* Review Screen */
    .review-screen {{
      display: none;
      width: 100%;
      max-width: 880px;
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 12px;
      padding: 2.5rem;
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }}

    .review-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.5rem;
      border-bottom: 1px solid var(--bg-card-border);
      padding-bottom: 1rem;
    }}

    .review-table-container {{
      max-height: 480px;
      overflow-y: auto;
      border: 1px solid var(--bg-card-border);
      border-radius: 8px;
      margin-bottom: 1.5rem;
    }}

    table.review-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }}

    table.review-table th, table.review-table td {{
      padding: 0.75rem 1rem;
      border-bottom: 1px solid var(--bg-card-border);
      font-size: 0.9rem;
    }}

    table.review-table th {{
      background: var(--bg-primary);
      position: sticky;
      top: 0;
      color: var(--accent-gold);
      font-weight: 700;
      text-transform: uppercase;
      font-size: 0.8rem;
      letter-spacing: 0.5px;
    }}

    /* Modal for Managing 800 Words */
    .modal-overlay {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(4px);
      z-index: 999;
      justify-content: center;
      align-items: center;
      padding: 1.5rem;
    }}

    .modal-card {{
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 12px;
      width: 100%;
      max-width: 760px;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      padding: 2rem;
      box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }}

    .modal-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
    }}

    .modal-header h3 {{
      font-size: 1.3rem;
      font-weight: 700;
    }}

    .modal-body {{
      flex: 1;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }}

    textarea.word-input-area {{
      width: 100%;
      height: 300px;
      background: var(--bg-primary);
      border: 1px solid var(--bg-card-border);
      border-radius: 8px;
      color: var(--text-main);
      padding: 1rem;
      font-family: var(--font-mono);
      font-size: 0.9rem;
      line-height: 1.5;
      outline: none;
      resize: vertical;
    }}
    textarea.word-input-area:focus {{
      border-color: var(--accent-gold);
    }}

    .modal-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 1.5rem;
      gap: 1rem;
    }}

    /* Shortcuts guide footer */
    .shortcuts-bar {{
      margin-top: auto;
      padding: 0.75rem 2rem;
      background: rgba(17, 26, 46, 0.5);
      border-top: 1px solid var(--bg-card-border);
      display: flex;
      justify-content: center;
      gap: 2rem;
      font-size: 0.8rem;
      color: var(--text-muted);
    }}
    .shortcuts-bar kbd {{
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 4px;
      padding: 0.15rem 0.4rem;
      font-family: var(--font-mono);
      color: var(--accent-gold);
      font-size: 0.75rem;
    }}

    /* Fullscreen tweaks */
    :fullscreen .word-display-card {{
      min-height: 50vh;
      border: none;
      box-shadow: none;
    }}
    :fullscreen main {{
      justify-content: center;
    }}
  </style>
</head>
<body>

  <!-- Navigation / Header -->
  <header>
    <div class="brand">
      <span class="brand-badge">DIPR</span>
      <h1>SSB WAT SIMULATOR</h1>
    </div>
    <div class="header-actions">
      <button class="btn-secondary" id="btnToggleTheme" title="Toggle between Dark Hall and Official DIPR Light Projector Mode">
        <span id="themeIcon">☀️</span> <span id="themeLabel">Projector Mode</span>
      </button>
      <button class="btn-secondary" id="btnOpenWordManager">
        📝 <span>Word Bank</span> <span class="badge-count" id="headerWordCount">1,259 Words</span>
      </button>
      <button class="btn-secondary" id="btnToggleFullscreen" title="Toggle Fullscreen">
        ⛶ <span>Fullscreen</span>
      </button>
    </div>
  </header>

  <!-- Main View Area -->
  <main>

    <!-- 1. SETUP SCREEN -->
    <section class="setup-card" id="setupScreen">
      <h2 class="setup-title">Word Association Test (WAT)</h2>
      <p class="setup-subtitle">
        Official DIPR psychological battery simulation loaded with all <strong>21 Practice Sets ({len(all_words_flat)} words)</strong> from your PDF.
      </p>

      <div class="info-banner">
        <div>📄 Source: <strong>800 WAT for Practice...pdf</strong></div>
        <div>Loaded: <strong>21 Sets (60 Words/Set)</strong></div>
      </div>

      <div class="form-group" style="margin-bottom: 1.25rem;">
        <label for="selectSet">Select Practice Set</label>
        <select id="selectSet">
          <option value="random_60" selected>🎲 Random 60 Words (Simulate Full Board Test)</option>
          <option value="random_30">⚡ Quick Practice (30 Random Words)</option>
          <optgroup label="── OFFICIAL DIPR SETS (60 Words Each) ──">
'''

for s in formatted_sets:
    html_content += f'            <option value="set_{s["id"]}">Set {s["id"]} ({s["count"]} Words: {s["preview"]})</option>\n'

html_content += f'''          </optgroup>
          <optgroup label="── OTHER OPTIONS ──">
            <option value="all">🔥 Full Marathon (All {len(all_words_flat)} Words)</option>
            <option value="custom">✏️ My Custom Word Bank</option>
          </optgroup>
        </select>
      </div>

      <div class="grid-2">
        <div class="form-group">
          <label for="selectDuration">Interval Per Word</label>
          <select id="selectDuration">
            <option value="15" selected>15 Seconds (Official DIPR Standard)</option>
            <option value="12">12 Seconds (Pressure / Stress Training)</option>
            <option value="10">10 Seconds (Ultra-Speed Instinct)</option>
            <option value="18">18 Seconds (Beginner Pace)</option>
          </select>
        </div>

        <div class="form-group">
          <label for="selectOrder">Word Order</label>
          <select id="selectOrder">
            <option value="sequential" selected>Original Order (As in PDF Set)</option>
            <option value="shuffle">Shuffled (Randomized)</option>
          </select>
        </div>
      </div>

      <div class="form-group" style="margin-bottom: 1.25rem;">
        <label>Practice Mode</label>
        <div class="mode-selector">
          <div class="mode-option active" id="modePaper" onclick="selectPracticeMode('paper')">
            <strong>📝 Pen & Paper (Recommended)</strong>
            <span>Exact SSB exam condition. Write in your notebook while words flash.</span>
          </div>
          <div class="mode-option" id="modeTyping" onclick="selectPracticeMode('typing')">
            <strong>⌨️ Digital Typing</strong>
            <span>Type responses directly on screen. Auto-saves for post-test psychological review.</span>
          </div>
        </div>
      </div>

      <div class="options-row">
        <label class="checkbox-label">
          <input type="checkbox" id="chkAudioBeep" checked>
          <span>Audio beep on word change</span>
        </label>
        <label class="checkbox-label">
          <input type="checkbox" id="chkWarningTick">
          <span>Tick at last 3 seconds</span>
        </label>
      </div>

      <button class="btn-start" id="btnStartTest">
        COMMENCE TEST (START)
      </button>
    </section>

    <!-- 2. ACTIVE TEST SCREEN -->
    <section class="test-screen" id="testScreen">
      <div class="test-top-bar">
        <div class="counter-tag" id="wordProgress">WORD 1 / 60</div>
        
        <div class="timer-ring-container">
          <svg class="timer-ring-svg" viewBox="0 0 80 80">
            <circle class="timer-ring-bg" cx="40" cy="40" r="36" />
            <circle class="timer-ring-progress" id="timerCircle" cx="40" cy="40" r="36" />
          </svg>
          <div class="timer-number" id="timerText">15</div>
        </div>
      </div>

      <div class="word-display-card" id="wordCard">
        <div class="flashed-word" id="flashedWord">LEADER</div>
        <div class="progress-bar-linear">
          <div class="progress-bar-fill" id="linearProgressBar"></div>
        </div>
      </div>

      <!-- Typing mode input field -->
      <div class="typing-container" id="typingContainer">
        <input 
          type="text" 
          class="typing-input" 
          id="typingInput" 
          placeholder="Write your spontaneous association here (press Enter or wait)..." 
          autocomplete="off"
        />
      </div>

      <div class="controls-row">
        <button class="control-btn" id="btnPauseResume">
          <span id="pauseIcon">⏸</span> <span id="pauseLabel">Pause</span>
        </button>
        <button class="control-btn" id="btnNextWord" title="Skip to Next Word (Arrow Right)">
          <span>Next Word ❯</span>
        </button>
        <button class="control-btn btn-danger" id="btnAbortTest">
          <span>✕ End Test</span>
        </button>
      </div>
    </section>

    <!-- 3. REVIEW SCREEN -->
    <section class="review-screen" id="reviewScreen">
      <div class="review-header">
        <div>
          <h2 id="reviewTitle">Set Completed!</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 0.25rem;">
            Review your flashed words and associations to evaluate Officer Like Qualities (OLQs).
          </p>
        </div>
        <button class="btn-secondary" id="btnExportLog">📋 Copy All Responses</button>
      </div>

      <div class="review-table-container">
        <table class="review-table">
          <thead>
            <tr>
              <th style="width: 10%;">#</th>
              <th style="width: 25%;">Flashed Word</th>
              <th style="width: 65%;">Your Response / Association</th>
            </tr>
          </thead>
          <tbody id="reviewTableBody">
            <!-- Dynamically populated -->
          </tbody>
        </table>
      </div>

      <div style="display: flex; justify-content: space-between; gap: 1rem;">
        <button class="btn-secondary" id="btnBackToHome">← Return to Setup</button>
        <button class="btn-start" style="width: auto; padding: 0.75rem 2rem;" id="btnRetake">Start Another Batch</button>
      </div>
    </section>

  </main>

  <!-- KEYBOARD SHORTCUTS BAR -->
  <footer class="shortcuts-bar">
    <div><kbd>Space</kbd> Pause / Resume</div>
    <div><kbd>→</kbd> or <kbd>Enter</kbd> Next Word</div>
    <div><kbd>F</kbd> Fullscreen</div>
    <div><kbd>Esc</kbd> Exit Test</div>
  </footer>

  <!-- 4. MODAL: MANAGE & PASTE WORDS -->
  <div class="modal-overlay" id="wordModal">
    <div class="modal-card">
      <div class="modal-header">
        <h3>Word Bank Management ({len(all_words_flat)} Words Loaded)</h3>
        <button class="btn-secondary" style="padding: 0.25rem 0.6rem;" id="btnCloseModal">✕</button>
      </div>
      <div class="modal-body">
        <p style="font-size: 0.9rem; color: var(--text-muted);">
          All 21 sets from your PDF are loaded. You can inspect them below, edit, or upload additional words.
        </p>
        <div style="display: flex; gap: 0.5rem; align-items: center; margin-bottom: 0.5rem;">
          <input type="file" id="fileUploadWordBank" accept=".txt,.csv" style="display: none;">
          <button class="btn-secondary" style="font-size: 0.85rem;" onclick="document.getElementById('fileUploadWordBank').click()">
            📂 Upload Custom .txt / .csv
          </button>
          <button class="btn-secondary" style="font-size: 0.85rem; margin-left: auto;" id="btnResetOfficialSets">
            🔄 Reset to Original 21 PDF Sets
          </button>
        </div>
        <textarea class="word-input-area" id="txtWordBank" placeholder="Words list..."></textarea>
        <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; color: var(--text-muted);">
          <span id="modalDetectedCount">Detected: 0 words</span>
          <span style="font-size: 0.8rem; color: var(--accent-gold);">💡 Tip: Negative words test maturity & calmness</span>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn-secondary" id="btnCancelModal">Cancel</button>
        <button class="btn-start" style="width: auto; padding: 0.6rem 1.75rem;" id="btnSaveWordBank">
          Save Word Bank
        </button>
      </div>
    </div>
  </div>

  <script>
    // --- EMBEDDED OFFICIAL 21 SETS FROM PDF ---
    const OFFICIAL_SETS = {sets_json_str};
    const ALL_WORDS_FLAT = {all_words_json_str};

    // --- APPLICATION STATE ---
    let wordBank = [...ALL_WORDS_FLAT];
    let currentSessionWords = [];
    let currentIndex = 0;
    let timerDuration = 15;
    let timerRemaining = 15;
    let timerInterval = null;
    let isPaused = false;
    let practiceMode = 'paper'; // 'paper' or 'typing'
    let candidateResponses = {{}};

    // Audio Context (Synthesized Beep)
    let audioCtx = null;

    function initAudio() {{
      if (!audioCtx) {{
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }}
    }}

    function playBeep(freq = 880, duration = 0.12, type = 'sine') {{
      if (!document.getElementById('chkAudioBeep').checked) return;
      try {{
        initAudio();
        if (audioCtx.state === 'suspended') {{
          audioCtx.resume();
        }}
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      }} catch (e) {{
        console.warn('Audio play failed:', e);
      }}
    }}

    function playTick() {{
      if (!document.getElementById('chkWarningTick').checked) return;
      playBeep(440, 0.05, 'triangle');
    }}

    // --- WORD PARSER & STORAGE ---
    function parseWordsFromText(text) {{
      if (!text) return [];
      const lines = text.split(/[\\n,;]+/);
      const cleanWords = lines.map(line => {{
        return line
          .replace(/^\\s*\\d+[\\.\\)\\-\\:]\\s*/, '')
          .replace(/^===.*===$/, '')
          .replace(/["'“”]/g, '')
          .trim();
      }}).filter(w => w.length > 0 && !/^\\d+$/.test(w));
      
      const unique = [];
      const seen = new Set();
      for (const w of cleanWords) {{
        const upper = w.toUpperCase();
        if (!seen.has(upper)) {{
          seen.add(upper);
          unique.push(upper);
        }}
      }}
      return unique;
    }}

    function loadSavedWordBank() {{
      const stored = localStorage.getItem('ssb_wat_custom_bank');
      if (stored) {{
        try {{
          const parsed = JSON.parse(stored);
          if (Array.isArray(parsed) && parsed.length > 0) {{
            wordBank = parsed;
            updateWordCountUI();
            return;
          }}
        }} catch (e) {{
          console.error(e);
        }}
      }}
      wordBank = [...ALL_WORDS_FLAT];
      updateWordCountUI();
    }}

    function saveWordBank(words) {{
      wordBank = words;
      localStorage.setItem('ssb_wat_custom_bank', JSON.stringify(words));
      updateWordCountUI();
    }}

    function updateWordCountUI() {{
      const count = wordBank.length;
      document.getElementById('headerWordCount').textContent = `${{count.toLocaleString()}} Words`;
      document.getElementById('modalDetectedCount').textContent = `Total in Bank: ${{count.toLocaleString()}} words`;
    }}

    // --- TEST LIFECYCLE ---
    function selectPracticeMode(mode) {{
      practiceMode = mode;
      document.getElementById('modePaper').classList.toggle('active', mode === 'paper');
      document.getElementById('modeTyping').classList.toggle('active', mode === 'typing');
    }}

    function startTest() {{
      const setChoice = document.getElementById('selectSet').value;
      const durationOption = parseInt(document.getElementById('selectDuration').value, 10);
      const orderOption = document.getElementById('selectOrder').value;

      timerDuration = durationOption || 15;

      let pool = [];

      if (setChoice.startsWith('set_')) {{
        const setId = parseInt(setChoice.replace('set_', ''), 10);
        const found = OFFICIAL_SETS.find(s => s.id === setId);
        if (found) {{
          pool = [...found.words];
        }}
      }} else if (setChoice === 'random_60') {{
        pool = [...ALL_WORDS_FLAT];
        shuffleArray(pool);
        pool = pool.slice(0, 60);
      }} else if (setChoice === 'random_30') {{
        pool = [...ALL_WORDS_FLAT];
        shuffleArray(pool);
        pool = pool.slice(0, 30);
      }} else if (setChoice === 'all') {{
        pool = [...ALL_WORDS_FLAT];
      }} else if (setChoice === 'custom') {{
        pool = [...wordBank];
      }}

      if (orderOption === 'shuffle' && !setChoice.startsWith('random_')) {{
        shuffleArray(pool);
      }}

      currentSessionWords = pool;

      if (currentSessionWords.length === 0) {{
        alert("Selected word set is empty!");
        return;
      }}

      currentIndex = 0;
      candidateResponses = {{}};
      isPaused = false;

      // Switch screens
      document.getElementById('setupScreen').style.display = 'none';
      document.getElementById('reviewScreen').style.display = 'none';
      document.getElementById('testScreen').style.display = 'flex';

      // Setup typing UI
      const typingContainer = document.getElementById('typingContainer');
      if (practiceMode === 'typing') {{
        typingContainer.style.display = 'block';
        document.getElementById('typingInput').value = '';
      }} else {{
        typingContainer.style.display = 'none';
      }}

      updatePauseUI();
      displayCurrentWord();
      startWordTimer();
    }}

    function shuffleArray(arr) {{
      for (let i = arr.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
      }}
    }}

    function displayCurrentWord() {{
      const word = currentSessionWords[currentIndex];
      const wordElement = document.getElementById('flashedWord');
      wordElement.textContent = word;

      // Trigger pop animation
      wordElement.style.animation = 'none';
      wordElement.offsetHeight;
      wordElement.style.animation = 'wordPop 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275)';

      // Counter
      document.getElementById('wordProgress').textContent = `WORD ${{currentIndex + 1}} / ${{currentSessionWords.length}}`;

      // Typing input
      if (practiceMode === 'typing') {{
        const input = document.getElementById('typingInput');
        input.value = candidateResponses[word] || '';
        input.focus();
      }}

      // Transition chime
      playBeep(980, 0.15);
    }}

    function startWordTimer() {{
      clearInterval(timerInterval);
      timerRemaining = timerDuration;
      updateTimerUI(timerRemaining);

      const tickRateMs = 100;
      let elapsedInSecond = 0;

      timerInterval = setInterval(() => {{
        if (isPaused) return;

        elapsedInSecond += tickRateMs;
        if (elapsedInSecond >= 1000) {{
          elapsedInSecond = 0;
          timerRemaining--;

          if (timerRemaining <= 3 && timerRemaining > 0) {{
            playTick();
          }}

          if (timerRemaining <= 0) {{
            recordCurrentResponse();
            nextWord();
            return;
          }}
        }}

        const currentSecondsRemaining = timerRemaining - (elapsedInSecond / 1000);
        updateTimerUI(Math.max(0, currentSecondsRemaining));
      }}, tickRateMs);
    }}

    function updateTimerUI(seconds) {{
      const wholeSec = Math.ceil(seconds);
      document.getElementById('timerText').textContent = wholeSec;

      const fraction = Math.max(0, seconds / timerDuration);

      const circumference = 226.2;
      const offset = circumference * (1 - fraction);
      const circle = document.getElementById('timerCircle');
      circle.style.strokeDashoffset = offset;

      if (fraction <= 0.25) {{
        circle.style.stroke = '#ef4444';
      }} else if (fraction <= 0.5) {{
        circle.style.stroke = '#f59e0b';
      }} else {{
        circle.style.stroke = 'var(--accent-gold)';
      }}

      document.getElementById('linearProgressBar').style.width = `${{fraction * 100}}%`;
    }}

    function recordCurrentResponse() {{
      if (practiceMode === 'typing') {{
        const currentWord = currentSessionWords[currentIndex];
        const text = document.getElementById('typingInput').value.trim();
        candidateResponses[currentWord] = text || "(No response entered)";
      }}
    }}

    function nextWord() {{
      recordCurrentResponse();
      currentIndex++;
      if (currentIndex >= currentSessionWords.length) {{
        finishTest();
      }} else {{
        displayCurrentWord();
        startWordTimer();
      }}
    }}

    function togglePause() {{
      isPaused = !isPaused;
      updatePauseUI();
    }}

    function updatePauseUI() {{
      document.getElementById('pauseIcon').textContent = isPaused ? '▶' : '⏸';
      document.getElementById('pauseLabel').textContent = isPaused ? 'Resume' : 'Pause';
      document.getElementById('wordCard').style.opacity = isPaused ? '0.6' : '1';
    }}

    function abortTest() {{
      if (confirm("Are you sure you want to stop the test? Your completed responses will be saved for review.")) {{
        finishTest();
      }}
    }}

    function finishTest() {{
      clearInterval(timerInterval);
      document.getElementById('testScreen').style.display = 'none';
      document.getElementById('reviewScreen').style.display = 'block';

      populateReviewTable();
    }}

    function populateReviewTable() {{
      const tbody = document.getElementById('reviewTableBody');
      tbody.innerHTML = '';

      const count = practiceMode === 'typing' ? currentSessionWords.length : currentIndex;
      const wordsToReview = currentSessionWords.slice(0, Math.max(count, currentIndex));

      wordsToReview.forEach((word, idx) => {{
        const tr = document.createElement('tr');
        const resp = candidateResponses[word] || (practiceMode === 'typing' ? '—' : 'Written on paper');
        tr.innerHTML = `
          <td style="font-family: var(--font-mono); color: var(--text-muted);">${{idx + 1}}</td>
          <td><strong style="color: var(--accent-gold); letter-spacing: 1px;">${{word}}</strong></td>
          <td>${{escapeHtml(resp)}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function escapeHtml(str) {{
      return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    }}

    // --- MODAL & FILE UPLOAD ---
    const wordModal = document.getElementById('wordModal');
    const txtWordBank = document.getElementById('txtWordBank');

    document.getElementById('btnOpenWordManager').addEventListener('click', () => {{
      let textLines = [];
      OFFICIAL_SETS.forEach(s => {{
        textLines.push(`=== SET ${{s.id}} (${{s.count}} WORDS) ===`);
        s.words.forEach((w, i) => textLines.push(`${{i + 1}}. ${{w}}`));
        textLines.push('');
      }});
      txtWordBank.value = textLines.join('\\n');
      updateModalDetectedCount();
      wordModal.style.display = 'flex';
    }});

    function closeModal() {{
      wordModal.style.display = 'none';
    }}

    document.getElementById('btnCloseModal').addEventListener('click', closeModal);
    document.getElementById('btnCancelModal').addEventListener('click', closeModal);

    txtWordBank.addEventListener('input', updateModalDetectedCount);

    function updateModalDetectedCount() {{
      const words = parseWordsFromText(txtWordBank.value);
      document.getElementById('modalDetectedCount').textContent = `Detected: ${{words.length}} valid words`;
    }}

    document.getElementById('btnResetOfficialSets').addEventListener('click', () => {{
      localStorage.removeItem('ssb_wat_custom_bank');
      wordBank = [...ALL_WORDS_FLAT];
      let textLines = [];
      OFFICIAL_SETS.forEach(s => {{
        textLines.push(`=== SET ${{s.id}} (${{s.count}} WORDS) ===`);
        s.words.forEach((w, i) => textLines.push(`${{i + 1}}. ${{w}}`));
        textLines.push('');
      }});
      txtWordBank.value = textLines.join('\\n');
      updateModalDetectedCount();
      updateWordCountUI();
      alert("Reset to official 21 sets from your PDF!");
    }});

    document.getElementById('fileUploadWordBank').addEventListener('change', (e) => {{
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (event) => {{
        txtWordBank.value = event.target.result;
        updateModalDetectedCount();
      }};
      reader.readAsText(file);
    }});

    document.getElementById('btnSaveWordBank').addEventListener('click', () => {{
      const parsed = parseWordsFromText(txtWordBank.value);
      if (parsed.length === 0) {{
        alert("Please enter at least one valid word!");
        return;
      }}
      saveWordBank(parsed);
      closeModal();
      alert(`Successfully saved ${{parsed.length}} words to your custom word bank!`);
    }});

    // --- THEME & FULLSCREEN ---
    let isLightProjector = false;
    document.getElementById('btnToggleTheme').addEventListener('click', () => {{
      isLightProjector = !isLightProjector;
      document.body.classList.toggle('dipr-projector', isLightProjector);
      document.getElementById('themeIcon').textContent = isLightProjector ? '🌙' : '☀️';
      document.getElementById('themeLabel').textContent = isLightProjector ? 'Dark Hall' : 'Projector Mode';
    }});

    document.getElementById('btnToggleFullscreen').addEventListener('click', () => {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(() => {{}});
      }} else {{
        if (document.exitFullscreen) {{
          document.exitFullscreen();
        }}
      }}
    }});

    // --- KEYBOARD SHORTCUTS ---
    window.addEventListener('keydown', (e) => {{
      const isTyping = document.activeElement === document.getElementById('typingInput');
      const inModal = document.activeElement === txtWordBank;

      if (inModal) return;

      if (document.getElementById('testScreen').style.display === 'flex') {{
        if (e.code === 'Space' && !isTyping) {{
          e.preventDefault();
          togglePause();
        }} else if (e.code === 'ArrowRight' && !isTyping) {{
          e.preventDefault();
          nextWord();
        }} else if (e.code === 'Enter' && isTyping) {{
          e.preventDefault();
          nextWord();
        }} else if (e.code === 'Escape') {{
          e.preventDefault();
          abortTest();
        }}
      }}

      if (e.key === 'f' || e.key === 'F') {{
        if (!isTyping && !inModal) {{
          e.preventDefault();
          document.getElementById('btnToggleFullscreen').click();
        }}
      }}
    }});

    // --- BUTTON EVENT LISTENERS ---
    document.getElementById('btnStartTest').addEventListener('click', startTest);
    document.getElementById('btnPauseResume').addEventListener('click', togglePause);
    document.getElementById('btnNextWord').addEventListener('click', nextWord);
    document.getElementById('btnAbortTest').addEventListener('click', abortTest);

    document.getElementById('btnBackToHome').addEventListener('click', () => {{
      document.getElementById('reviewScreen').style.display = 'none';
      document.getElementById('setupScreen').style.display = 'block';
    }});

    document.getElementById('btnRetake').addEventListener('click', () => {{
      startTest();
    }});

    document.getElementById('btnExportLog').addEventListener('click', () => {{
      let exportText = `=== SSB WAT SESSION REPORT ===\\n`;
      exportText += `Date: ${{new Date().toLocaleString()}}\\n`;
      exportText += `Total Words: ${{currentSessionWords.length}}\\n\\n`;

      currentSessionWords.forEach((word, idx) => {{
        const resp = candidateResponses[word] || '(Paper response)';
        exportText += `${{idx + 1}}. [${{word}}] => ${{resp}}\\n`;
      }});

      navigator.clipboard.writeText(exportText).then(() => {{
        alert("Report copied to clipboard! You can paste it into notes or share for assessment.");
      }}).catch(() => {{
        alert("Failed to auto-copy. Please select and copy directly from the table.");
      }});
    }});

    // Initialize on load
    loadSavedWordBank();
  </script>
</body>
</html>
'''

with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated index.html successfully with all 21 PDF sets!")
