import unittest
from lexer import Lexer

class TestLexer(unittest.TestCase):
    def test_tokenize(self):
        content = "<SECTION>**|*| Initialize variables |**</SECTION>"
        lexer = Lexer(content)
        expected_tokens = [
            ('SECTION', '<SECTION>'),
            ('BLOCK', '**'),
            ('ACTION', '|*|'),
            ('IDENTIFIER', 'Initialize'),
            ('IDENTIFIER', 'variables'),
            ('BLOCK', '**'),
            ('ENDSECTION', '</SECTION>')
        ]
        self.assertEqual(lexer.tokens, expected_tokens)

if __name__ == '__main__':
    unittest.main()
