
# Tested the following code using Google's Colab works Fine 
# For more Info -> https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_2_0_flash.ipynb
# This is an example of Python Function (Automatic Function Calling)

from IPython.display import HTML, Markdown, display
from google import genai
from google.genai.types import (
    FunctionDeclaration,
    GenerateContentConfig,
    GoogleSearch,
    Part,
    Retrieval,
    SafetySetting,
    Tool,
    VertexAISearch,
)

client = genai.Client(api_key='YOUR_API_KEY')


def get_current_weather(location: str) -> str:
    """Example method. Returns the current weather.

    Args:
        location: The city and state, e.g. San Francisco, CA
    """
    import random

    return random.choice(["sunny", "raining", "snowing", "fog"])


response = client.models.generate_content(
    model='gemini-2.0-flash-exp',
    contents="What is the weather like in Boston?",
    config=GenerateContentConfig(
        tools=[get_current_weather],
        temperature=0,
    ),
)

display(Markdown(response.text))