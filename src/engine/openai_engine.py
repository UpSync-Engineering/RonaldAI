import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_openai_response(prompt, engine="text-davinci-002", max_tokens=256, temperature=0.7):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temperature,    # Higher for more creativity
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text
