# My Personal Chef

My Personal Chef is an AI-powered culinary assistant that combines computer vision with agentic reasoning to help you cook from what you have at home. Upload a photo of your ingredients, and the agent will identify them and suggest a structured, step-by-step recipe tailored to your preferences.

---

## Features

- **Visual ingredient detection**: Uses LLaVA (via Ollama) to analyze images and extract a list of available ingredients.
- **Agentic recipe generation**: Powered by Llama 3.2 and LangGraph, the agent reasons over the detected ingredients and user preferences to produce a professional recipe.
- **Live web search**: Integrates the Tavily API to fetch accurate measurements, techniques, and recipes when the local model needs supplementary information.
- **Local-first architecture**: All inference runs locally via Ollama, with no cloud dependency beyond the Tavily search tool.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | [Streamlit](https://streamlit.io/) |
| LLM Orchestration | [LangChain](https://www.langchain.com/) & [LangGraph](https://langchain-ai.github.io/langgraph/) |
| Local Models | [Ollama](https://ollama.com/) — LLaVA & Llama 3.2 |
| Web Search | [Tavily API](https://tavily.com/) |
| Image Processing | [Pillow](https://python-pillow.org/) |

---

## Prerequisites

Before running the project, complete the following steps:

**1. Install Ollama**

Download and install Ollama from [ollama.com](https://ollama.com/), then pull the required models:

```bash
ollama pull llava
ollama pull llama3.2
```

**2. Get a Tavily API key**

Create a free account at [tavily.com](https://tavily.com/) and copy your API key.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/lperezpersico/my-personal-chef.git
cd my-personal-chef

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

Copy the provided example and fill in your key:

```bash
cp .env.example .env
```

Then edit `.env` and replace the placeholder with your actual key.

---

## Usage

Make sure Ollama is running in the background, then launch the app:

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`.

1. Upload a photo of your available ingredients (JPG or PNG).
2. Optionally, type a specific request in the text field (e.g., "something quick and healthy").
3. Click **Let's cook!** and wait for the agent to generate a full recipe.

---

## Project Structure

```
my-personal-chef/
├── app.py              # Streamlit interface and main application logic
├── chef_agent.py       # LangGraph agent definition and tool integration
├── utils.py            # Image preprocessing and Base64 encoding
├── requirements.txt    # Python dependencies
├── .env.example        # Template for required environment variables
└── .env                # API keys (not committed to version control)
```

---

## Environment Variables

| Variable | Description |
|---|---|
| `TAVILY_API_KEY` | API key for the Tavily web search integration |
