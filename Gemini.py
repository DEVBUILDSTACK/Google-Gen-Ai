from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyAWQYyLMbsStYkJAkmNBwEIlhp2Cn7G1I0')
response = client.models.generate_content(
    model='gemini-1.5-flash', contents='What is Google Gemini'
)
print(response.text)