# README

## Perfect Draw NPC Generator

This Python application uses OpenAI's GPT-3 model to generate non-player characters (NPCs) for the card game Perfect Draw. The application is built with Streamlit and uses the OpenAI API to generate the NPC descriptions.

### How it works

The application takes a type of NPC as input (e.g., shopkeeper, mage, psychotic) and generates a detailed description of the NPC, including their appearance, personality, and a short backstory. It also generates a deck gimmick, power card moves, and simple card moves for the NPC.

The generated text is in markdown format, so it can be easily copied and pasted into a markdown file.

### Setup

1. Clone the repository
2. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key. You can do this by creating a `.env` file in the root directory of the project, and adding your API key like so:

```env
API_KEY=your_openai_api_key
```

4. Run the Streamlit app:

```bash
streamlit run main.py
```

### Usage

1. Enter a type of NPC in the text box.
2. Click the "Generate NPC" button.
3. Wait for the NPC description to be generated. This can take around 5-10 seconds.
4. Copy the generated markdown text and use it as needed.

### Support

If you find this tool useful and would like to support its development and the upkeep of the OpenAI costs, you can donate via the PayPal button in the application.

### Contact

For any feedback or questions, feel free to reach out to me on discord: @adamkostandy (I am on the Perfect Draw server)

### Note

This application is not affiliated with or endorsed by OpenAI or the creators of Perfect Draw.