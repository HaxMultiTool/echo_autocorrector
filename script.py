def replace_special_characters(input_file, output_file):
    replacements = {
        '|': '^|',
        '\\': '^\\',
        '/': '^/',
        '(': '^(',
        ')': '^)',
        '>': '^>',
        '<': '^<',
        '=': '^='
    }
    
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    for original, replacement in replacements.items():
        content = content.replace(original, replacement)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)

input_file = 'input.txt'
output_file = 'output.txt'
replace_special_characters(input_file, output_file)

print(f"Done! Results are written in [output.txt]")
