import re

class Lexer:
    def __init__(self, content):
        self.tokens = self.tokenize(content)

    def tokenize(self, content):
        token_specification = [
            ('SECTION', r'<SECTION>'),
            ('ENDSECTION', r'</SECTION>'),
            ('BLOCK', r'\*\*'),
            ('ACTION', r'\|\*\|'),
            ('STATEMENT', r'\|\_\|'),
            ('REQUEST', r'\|\-\|'),
            ('AOT', r'\|\(<::>^<::>\)\|'),
            ('TASK', r'\|\ \|'),
            ('SIMULATION', r'\|\+\|'),
            ('PRINT', r'\|\=\|'),
            ('PASS', r'\|\^\|'),
            ('PLACEHOLDER', r'\|\#\|'),
            ('IDENTIFIER', r'\w+'),
            ('NEWLINE', r'\n'),
            ('SKIP', r'[ \t]+'),
            ('MISMATCH', r'.')
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
