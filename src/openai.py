import requests
from openai import OpenAI

#  fetch XML content from the URL 

# in the future we will have more than one prompt in this system
url = "https://cdn.jsdelivr.net/gh/NeoVertex1/holodata@main/holodata.xml"
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad HTTP responses (e.g., 404, 500)
    xml_content = response.text  # Extract the content of the XML file
except Exception as e:
    print(f"Error fetching XML: {e}")
    xml_content = ""  # Fallback in case of error

# Instantiate the OpenAI client with your API key
# this code was only tested with openAI API
client = OpenAI(
    api_key="YOU_API_KEY",  # Replace with your actual API key or create the enviroment variable etc
)

# Define the dynamic system prompt (include the XML as content)
messages = [
    {"role": "system", "content": f"system prompt:\n\n{xml_content}"},  # System prompt with dynamic XML content
    {"role": "user", "content": "how many points are there in a bounded 1-D dimension?"}  # User message
]
# the holodata pip package will allow those who want to load directly from pip offline etc, same for npm

# Make a request to the Chat Completions API
try:
    response = client.chat.completions.create(
        model="gpt-4o-2024-11-20",  # Specify model 
        messages=messages,
    )

    # assistant's response
    assistant_reply = response.choices[0].message.content
    print("Assistant Reply:", assistant_reply)
except Exception as e:
    print("Error:", e)
