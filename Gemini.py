# Tested the following code using Google's Colab works Fine 
# For more Info -> https://ai.google.dev/gemini-api/docs/sdks
# This is an Quickstart to use Google Gen AI SDK

from google import genai

client = genai.Client(api_key='YOUR_API_KEY')
response = client.models.generate_content(
    model='gemini-1.5-flash', contents='What is Google Gemini'
)

print(response.text)