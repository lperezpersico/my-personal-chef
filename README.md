# 👩‍🍳 My Personal Chef

**My Personal Chef** is an AI-powered culinary assistant that combines **Computer Vision** and **Agentic Reasoning** to help you cook. Simply upload a photo of your ingredients, and the Chef will identify them and suggest a professional, step-by-step recipe tailored to your needs.

---

## 🚀 Key Features

* **Visual Ingredient Detection**: Uses `Llava` (via Ollama) to analyze your images and list ingredients.
* **Agentic Reasoning**: Powered by `Llama 3.2` and `LangGraph` to provide structured cooking advice.
* **Live Web Search**: Integrated with the `Tavily API` to fetch professional recipes and techniques when the local model needs more detail.
* **Optimized for Local Hardware**: Includes image preprocessing to handle low-RAM environments and ensure high performance on consumer laptops.

---

## 🛠️ Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/)
* **LLM Orchestration**: [LangChain](https://www.langchain.com/) & [LangGraph](https://langchain-ai.github.io/langgraph/)
* **Local Models**: [Ollama](https://ollama.com/) (`Llava` & `Llama 3.2`)
* **Search Tool**: [Tavily API](https://tavily.com/)
* **Image Processing**: [Pillow (PIL)](https://python-pillow.org/)

---

## 📋 Prerequisites

1.  **Install Ollama**: Download and install from [ollama.com](https://ollama.com/).
2.  **Download Models**:
    Abrí una terminal y ejecutá:
    ```bash
    ollama pull llava
    ollama pull llama3.2
    ```
3.  **Tavily API Key**: Get a free API key at [tavily.com](https://tavily.com/).

---

## 💻 Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/lperezpersico/my-personal-chef.git](https://github.com/lperezpersico/my-personal-chef.git)
    cd my-personal-chef
    ```

2.  **Create a Virtual Environment**:
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**:
    Create a `.env` file in the root folder and add your API key:
    ```text
    TAVILY_API_KEY=tvly-your-actual-key-here
    ```

---

## 🏃 How to Run

1.  **Ensure Ollama is running** in the background.
2.  **Launch the Streamlit app**:
    ```bash
    streamlit run app.py
    ```
3.  Open your browser at `http://localhost:8501`.

---

## 📂 Project Structure

* `app.py`: Main Streamlit interface and application logic.
* `chef_agent.py`: Agent definition using LangGraph and tool integration.
* `utils.py`: Image processing and Base64 conversion utilities.
* `requirements.txt`: List of necessary Python libraries.
* `.env`: Secret API keys (not included in the repo).

---