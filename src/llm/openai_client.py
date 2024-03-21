from openai import OpenAI

from src.config import Config


class Openai:
    def __init__(self):
        config = Config()
        api_key = config.get_openai_api_key()
        self.client = OpenAI(api_key=api_key)

    def inference(self, model_id: str, prompt: str) -> str:
        print("openai")
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt.strip(),
                }
            ],
            model=model_id,
        )
        print("openai")
        return chat_completion.choices[0].message.content
