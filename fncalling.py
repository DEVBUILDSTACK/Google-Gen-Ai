# import random
# import client 

# def get_current_weather(location: str) -> str:
#     """Example method. Returns the current weather.

#     Args:
#         location: The city and state, e.g. San Francisco, CA
#     """

#     return random.choice(["sunny", "raining", "snowing", "fog"])


# response = client.models.generate_content(
#     model=MODEL_ID,
#     contents="What is the weather like in Boston?",
#     config=GenerateContentConfig(
#         tools=[get_current_weather],
#         temperature=0,
#     ),
# )

# display(Markdown(response.text))