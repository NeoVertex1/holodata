# holodata
## Schema-Driven Metadata for AI Prompts

---

**Holodata is an attempt to make system prompts more accessible for developers, etc. The format and goal are to make prompt engineering easier to implement. The overall aim includes more ambitious ideals, such as enabling agents to achieve greater accuracy and freedom.**

---

holodata allows easy integration of system prompts into workflows by ultilizing self-referential recursive system for autonomous metadata generation, leveraging metamorphic reasoning, fractal self-similarity, and dynamic abstraction for scalable insights.

---

![holodata](images/holodata_dec10.png)




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


