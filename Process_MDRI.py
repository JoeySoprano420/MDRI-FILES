import argparse
from lexer import Lexer
from parser import Parser
from execution_engine import ExecutionEngine
from error_corrector import ErrorCorrector
from jit_compiler import JITCompiler
from logger import Logger
from plugin_manager import plugin_manager

def process_mdri(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Error correction
    error_corrector = ErrorCorrector()
    corrected_content = error_corrector.correct_errors(content)
    Logger.info("Error correction complete")

    # Tokenization
    lexer = Lexer(corrected_content)
    tokens = lexer.tokens
    Logger.debug(f"Tokens: {tokens}")

    # Parsing
    parser = Parser(tokens)
    ast = parser.ast
    Logger.debug(f"AST: {ast}")

    # JIT Compilation
    jit_compiler = JITCompiler()
    compiled_code = jit_compiler.compile(corrected_content)
    Logger.info("JIT compilation complete")

    # Execution
    execution_engine = ExecutionEngine(ast)
    execution_engine.execute()
    Logger.info("Execution complete")

    # Plugin execution
    plugin_manager.execute_plugins(corrected_content.splitlines())
    Logger.info("Plugin execution complete")

def main():
    parser = argparse.ArgumentParser(description='MDRI Processing Engine')
    parser.add_argument('file', help='Path to the MDRI file')
    args = parser.parse_args()

    process_mdri(args.file)

if __name__ == "__main__":
    main()
