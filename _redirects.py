with open('collector.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the specific line
old_line = "      const slug = toSlug(gameName);"
new_line = "      const slug = game.slug || toSlug(gameName);"

if old_line in content:
    content = content.replace(old_line, new_line)
    
    with open('collector_modified.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Modified collector.js")
else:
    print("Could not find the exact line. Let me search for it.")
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if "slug = toSlug(gameName)" in line:
            print(f"Found at line {i}: {line}")
            lines[i] = line.replace("toSlug(gameName)", "game.slug || toSlug(gameName)")
            
    with open('collector_modified.js', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print("Modified by searching")