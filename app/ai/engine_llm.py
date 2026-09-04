import os

from dotenv import load_dotenv
from openai import OpenAI

from app.ai.base_llm import BaseLLM

load_dotenv()


class EngineLLM(BaseLLM):

    def __init__(self):

        self.client = OpenAI(

            api_key=os.getenv("MISTRAL_API_KEY"),

            base_url="https://api.mistral.ai/v1",

        )

        self.model = "mistral-small-latest"

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = self.client.chat.completions.create(

            model=self.model,

            messages=[

                {

                    "role": "user",

                    "content": prompt,

                }

            ],

            temperature=0.3,

        )

        return response.choices[0].message.content