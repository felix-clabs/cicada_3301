import re

with open('pages_and_ciphers.md') as f:
    text = f.read()

# Find all occurrences of Red Text
red_texts = re.findall(r'### Red Text\n(.*?)(?=\n###|\n\* |\Z)', text, re.DOTALL)
print('Found', len(red_texts), 'red text blocks in pages_and_ciphers.md')

for i, rt in enumerate(red_texts):
    print(f'Red text {i}:', rt[:30].replace('\n', ' '))
