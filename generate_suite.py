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
    # Slide 12: Blank
    slides.append({
        'num': 12,
        'type': 'blank',
        'src': '',
        'label': 'Slide 12 — BLANK SLIDE (Your Own Story)'
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

print("Data serialized successfully.")
