from google import genai
from google.genai import types

client = genai.Client(api_key='YOUR_API_KEY')
response = client.models.generate_content(
    model='gemini-1.5-flash', contents='What is Google Gemini'
)
print(response.text)