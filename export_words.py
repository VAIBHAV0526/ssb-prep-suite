import pypdf, re, json, os

pdf_path = r'C:\Users\Singh\Downloads\800 WAT for Practice...pdf'
out_dir = r'C:\Users\Singh\.gemini\antigravity\scratch\ssb-wat-simulator'

reader = pypdf.PdfReader(pdf_path)
lines = []
for page in reader.pages:
    lines.extend((page.extract_text() or '').split('\n'))

sets = []
cur_set = []

i = 0
while i < len(lines):
    line = lines[i].strip()
    i += 1
    if not line:
        continue
    if line.lower() in ['s/no word use', 's/no', 'word use']:
        continue
    m = re.match(r'^(\d+)[\.\)]\s*(.*)', line)
    if m:
        num = int(m.group(1))
        word_part = m.group(2).strip()
        
        while word_part.endswith('/') and i < len(lines):
            next_line = lines[i].strip()
            if not re.match(r'^\d+[\.\)]', next_line) and next_line.lower() not in ['s/no word use', 's/no']:
                word_part += next_line
                i += 1
            else:
                break
        
        word = re.split(r'\s{2,}|\t', word_part)[0].strip()
        word = word.replace('/', ' / ')
        word = re.sub(r'\s+', ' ', word).strip()

        if num == 1 and len(cur_set) > 20:
            sets.append(cur_set)
            cur_set = []
        cur_set.append({'num': num, 'word': word})

if cur_set:
    sets.append(cur_set)

# Save JSON
with open(os.path.join(out_dir, 'wat_sets.json'), 'w', encoding='utf-8') as f:
    json.dump(sets, f, indent=2)

# Save clean plain text
all_words_plain = []
with open(os.path.join(out_dir, 'all_words.txt'), 'w', encoding='utf-8') as f:
    for idx, s in enumerate(sets):
        f.write(f'=== SET {idx+1} ===\n')
        for item in s:
            f.write(f"{item['num']}. {item['word']}\n")
            all_words_plain.append(item['word'])
        f.write('\n')

print(f'Successfully exported {len(sets)} sets with {len(all_words_plain)} words total.')
