import unittest
from parser import Parser

class TestParser(unittest.TestCase):
    def test_parse_tokens(self):
        tokens = [
            ('SECTION', '<SECTION>'),
            ('BLOCK', '**'),
            ('ACTION', '|*|'),
            ('IDENTIFIER', 'Initialize'),
            ('IDENTIFIER', 'variables'),
            ('BLOCK', '**'),
            ('ENDSECTION', '</SECTION>')
        ]
        parser = Parser(tokens)
        expected_ast = [
            {
                'type': 'SECTION',
                'content': [
                    {
                        'type': '|*|',
                        'content': ['Initialize', 'variables']
                    }
                ]
            }
        ]
        self.assertEqual(parser.ast, expected_ast)

if __name__ == '__main__':
    unittest.main()
