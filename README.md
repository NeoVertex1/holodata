# holodata
## Schema-Driven Metadata for AI Prompts

---

**holodata wants to make high-quality and tested system prompts more accessible**

---

holodata allows easy integration of system prompts into workflows by ultilizing self-referential recursive system for autonomous metadata generation, leveraging metamorphic reasoning, fractal self-similarity, and dynamic abstraction for scalable insights.

---

![holodata](images/holodata_dec10.png)




---
#### RUN WITH OPENAI API:

```python
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
```
---

**DOWNLOAD MANUALLY: Fetch the XML Content:**

First, retrieve the XML content from the CDN using `curl`:

```bash
curl -s https://cdn.jsdelivr.net/gh/NeoVertex1/holodata@main/holodata.xml -o system_prompt.xml
```

---

**RUN WITH OLLAMA: Create a `Modelfile`:**

- Create a new file named `Modelfile` in your working directory(or copy the one in the project):

  ```bash
  touch Modelfile
  ```

- Open the `Modelfile` in a text editor and define its content:

  ```bash
  FROM qwen2.5:7b

  SYSTEM """
  [Paste or import the content of holodata.xml here]
  """
  ```

**3. Create the Custom Model:**

Use the `Modelfile` to create a new model in Ollama:

```bash
ollama create custom_qwen2.5:7b -f ./Modelfile
```

This command creates a new model named `custom_qwen2.5:7b` based on the configuration specified in the `Modelfile`.

**4. Run the Custom Model:**

Now, you can run your custom model with the specified system prompt:

```bash
ollama run custom_qwen2.5:7b
```

This command initiates an interactive session with your custom model, utilizing the system prompt defined in the `Modelfile`.

**Additional Resources:**

- **Ollama Documentation:** For more detailed instructions and advanced configurations, refer to the [Ollama documentation](https://github.com/ollama/ollama/blob/main/docs/modelfile.md).



---

#### CDN LINK:

[https://cdn.jsdelivr.net/gh/NeoVertex1/holodata@main/holodata.xml](https://cdn.jsdelivr.net/gh/NeoVertex1/holodata@main/holodata.xml)


Example usage on a web injection:

`<link src="https://cdn.jsdelivr.net/gh/NeoVertex1/holodata@main/holodata.xml">`


>author's note:

>Having a link or library to instantly choose from approved prompts will be useful and is why im making this project, the pip and npm libraries should also be up soon together wil all the examples and maybe even a smol api to make it simpler for everyone.


