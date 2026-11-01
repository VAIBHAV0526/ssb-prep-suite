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
# 11 pictures per set + 1 blank slide (#12)
total_tat_images = 137
tat_sets = []
pics_per_set = 11
num_full_sets = total_tat_images // pics_per_set # 12 sets

for s_idx in range(num_full_sets):
    start = s_idx * pics_per_set + 1
    end = start + pics_per_set - 1
    slides = []
    for img_idx in range(start, end + 1):
        slides.append({
            'num': len(slides) + 1,
            'type': 'image',
            'src': f'tat_images/tat_{img_idx:03d}.jpg',
            'label': f'TAT Picture {len(slides) + 1}'
        })
    # Slide 12 is blank slide
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

print(f"Prepared: {len(wat_sets)} WAT sets, {len(srt_sets)} SRT sets, {len(tat_sets)} TAT sets.")
