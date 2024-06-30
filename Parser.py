class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.ast = self.parse_tokens()

    def parse_tokens(self):
        ast = []
        while self.pos < len(self.tokens):
            token_type, token_value = self.tokens[self.pos]
            if token_type == 'SECTION':
                ast.append(self.parse_section())
            else:
                self.pos += 1
        return ast

    def parse_section(self):
        self.pos += 1  # Skip SECTION token
        section_content = []
        while self.pos < len(self.tokens):
            token_type, token_value = self.tokens[self.pos]
            if token_type == 'ENDSECTION':
                self.pos += 1  # Skip ENDSECTION token
                break
            elif token_type == 'BLOCK':
                section_content.append(self.parse_block())
            else:
                self.pos += 1
        return {'type': 'SECTION', 'content': section_content}

    def parse_block(self):
        block_type = self.tokens[self.pos][1]
        self.pos += 1  # Skip BLOCK token
        block_content = []
        while self.pos < len(self.tokens):
            token_type, token_value = self.tokens[self.pos]
            if token_type == 'BLOCK':
                self.pos += 1  # Skip BLOCK token
                break
            else:
                block_content.append(token_value)
                self.pos += 1
        return {'type': block_type, 'content': block_content}
