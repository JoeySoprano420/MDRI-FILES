import unittest
from execution_engine import ExecutionEngine

class TestExecutionEngine(unittest.TestCase):
    def test_execute_section(self):
        ast = [
            {
                'type': 'SECTION',
                'content': [
                    {
                        'type': '|*|',
                        'content': ['x = 10', 'y = 20']
                    }
                ]
            }
        ]
        engine = ExecutionEngine(ast)
        engine.execute()
        self.assertEqual(engine.global_vars['x'], 10)
        self.assertEqual(engine.global_vars['y'], 20)

if __name__ == '__main__':
    unittest.main()
