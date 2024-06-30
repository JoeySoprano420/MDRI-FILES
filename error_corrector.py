import openai

class ErrorCorrector:
    def __init__(self):
        openai.api_key = 'YOUR_API_KEY'

    def correct_errors(self, content):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Correct the syntax errors in the following content:\n\n{content}",
            max_tokens=1024
        )
        corrected_content = response.choices[0].text.strip()
        return corrected_content
