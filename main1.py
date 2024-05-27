from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def gpt_calling(input_text):
    client = OpenAI(
                    api_key= os.getenv("OPENAI_API_KEY"),
                    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": input_text}],
        max_tokens=1000,
        temperature=0.8    
    )
    output = response.choices[0].message.content
    return output

x=input("Enter your Prompt: ")

print(gpt_calling(x))