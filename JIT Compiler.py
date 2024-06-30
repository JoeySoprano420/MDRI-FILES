import ctypes

class JITCompiler:
    def __init__(self):
        self.code_cache = {}

    def compile(self, code):
        if code in self.code_cache:
            return self.code_cache[code]
        
        compiled_code = self._compile_code(code)
        self.code_cache[code] = compiled_code
        return compiled_code

    def _compile_code(self, code):
        # Using ctypes to compile and execute code dynamically
        code_object = compile(code, '<string>', 'exec')
        exec(code_object)
        return code_object
