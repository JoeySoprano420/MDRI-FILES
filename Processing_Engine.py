import re

def parse_mdri(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    sections = re.findall(r'<SECTION>(.*?)</SECTION>', content, re.DOTALL)
    for section in sections:
        process_section(section)

def process_section(section):
    blocks = re.findall(r'\*\*(.*?)\*\*', section, re.DOTALL)
    for block in blocks:
        lines = block.strip().split('\n')
        action_type = lines[0].strip()

        if action_type.startswith('|*|'):
            process_action(lines[1:])
        elif action_type.startswith('|_|'):
            process_statements(lines[1:])
        elif action_type.startswith('|-|'):
            process_request(lines[1:])
        elif action_type.startswith('|(<::>^<::>)|'):
            process_aot_scan(lines[1:])
        elif action_type.startswith('|+|'):
            process_simulation(lines[1:])
        # Add more cases as needed

def process_action(lines):
    for line in lines:
        exec(line.strip())

def process_statements(lines):
    for line in lines:
        exec(line.strip())

def process_request(lines):
    for line in lines:
        exec(line.strip())

def process_aot_scan(lines):
    for line in lines:
        exec(line.strip())

def process_simulation(lines):
    for line in lines:
        exec(line.strip())

# Example usage
parse_mdri('example.mdri')
