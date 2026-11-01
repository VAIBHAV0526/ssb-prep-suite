import re

with open(r'C:\Users\Singh\.gemini\antigravity\scratch\ssb-wat-simulator\build_full_suite.py', 'r', encoding='utf-8') as f:
    text = f.read()

chars = set(re.findall(r'[^\x00-\x7F]', text))
emojis = [c for c in chars if ord(c) > 0x2000]
print(f"Found {len(emojis)} non-ASCII chars:")
for c in sorted(emojis, key=lambda x: ord(x)):
    print(f"U+{ord(c):04X}: {repr(c)}")
