import re

class Lexer:
    def __init__(self, content):
        self.tokens = self.tokenize(content)

    def tokenize(self, content):
        # Tokenization logic with advanced regex for nested structures
        token_specification = [
            ('SECTION', r'<SECTION>'),         # Section start
            ('ENDSECTION', r'</SECTION>'),     # Section end
            ('BLOCK', r'\*\*'),                # Block start/end
            ('ACTION', r'\|\*\|'),             # Action block
            ('STATEMENT', r'\|\_\|'),          # Statement block
            ('REQUEST', r'\|\-\|'),            # Request block
            ('AOT', r'\|\(<::>^<::>\)\|'),     # AOT scan block
            ('TASK', r'\|\ \|'),               # Task block
            ('SIMULATION', r'\|\+\|'),         # Simulation block
            ('PRINT', r'\|\=\|'),              # Print block
            ('PASS', r'\|\^\|'),               # Pass block
            ('PLACEHOLDER', r'\|\#\|'),        # Placeholder block
            ('IDENTIFIER', r'\w+'),            # Identifiers
            ('NEWLINE', r'\n'),                # Line breaks
            ('SKIP', r'[ \t]+'),               # Skip over spaces and tabs
            ('MISMATCH', r'.')                 # Any other character
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        get_token = re.compile(tok_regex).match
        line_no = 1
        line_start = 0
        tokens = []
        mo = get_token(content)
        while mo is not None:
            kind = mo.lastgroup
            value = mo.group(kind)
            if kind == 'NEWLINE':
                line_start = mo.end()
                line_no += 1
            elif kind != 'SKIP' and kind != 'MISMATCH':
                tokens.append((kind, value))
            mo = get_token(content, mo.end())
        return tokens
