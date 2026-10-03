# 🤖 Simple Gemini Chatbot

A simple AI chatbot built with **Python, Google's Gemini API, and Streamlit**.

This project demonstrates the fundamentals of building an LLM-powered application, including user input validation, Gemini API integration, system prompts, streaming responses, error handling, chat history, and a clean web-based interface.

---

## 1. What You Build

This project is a **Streamlit-based AI chatbot** that:

- Accepts questions from the user through a web interface.
- Validates user input using Pydantic.
- Sends validated input to Google's Gemini model.
- Uses a system prompt to control the AI assistant's behavior.
- Receives the model response as a stream.
- Displays the response incrementally in the UI.
- Maintains conversation history during the current session.
- Provides a loading state while generating responses.
- Handles validation and API errors gracefully.
- Separates frontend and backend responsibilities.

### Workflow

```text
User Input
    ↓
Streamlit UI
    ↓
Pydantic Validation
    ↓
System Prompt + User Input
    ↓
Gemini API
    ↓
Streaming Response
    ↓
Streamlit UI
    ↓
Chat History
```

---

## 2. Project Structure

The application follows a simple modular structure:

```text
project/
│
├── app.py              # Streamlit frontend / UI
├── main.py             # Gemini API and backend logic
├── requirements.txt    # Project dependencies
├── .env                # API credentials (not committed)
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

### `app.py`

Responsible for the user interface:

- Streamlit page configuration
- Chat input
- Chat history display
- Loading state
- Streaming response display
- Error messages

### `main.py`

Responsible for backend logic:

- Environment variable loading
- Pydantic validation
- System prompt
- Gemini client initialization
- Gemini API interaction
- Streaming event processing
- Error handling

This separation makes the application easier to understand, maintain, and extend.

---

## 3. Technologies Used

- **Python** — Core programming language.
- **Streamlit** — Web-based user interface.
- **Google GenAI SDK** — Integration with Google's Gemini API.
- **Gemini** — Large language model used to generate responses.
- **Pydantic** — Validation of user input.
- **python-dotenv** — Loads environment variables from the `.env` file.
- **Conda** — Python environment management.

---

## 4. How to Run

### Step 1: Clone the repository

```bash
git clone <your-repository-url>

cd <your-repository-name>
```

### Step 2: Create and activate a virtual environment

Create your Conda environment:

```bash
conda create -n chatbot python=3.12
```

Activate the environment:

```bash
conda activate chatbot
```

### Step 3: Install dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### Step 4: Configure the API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

The `.env` file should **not** be committed to GitHub.

Make sure `.env` is included in your `.gitignore`:

```text
.env
```

### Step 5: Run the application

Because the project now uses Streamlit, run the application with:

```bash
streamlit run app.py
```

Streamlit will start the local web application and provide a local URL in the terminal.

Open the provided URL in your browser.

---

## 5. API Integration Approach

The application uses Google's GenAI SDK to communicate with the Gemini model.

The backend integration follows these steps:

### 1. Load environment variables

The API key is stored in the `.env` file and loaded using `python-dotenv`.

```python
load_dotenv()
```

The API key is not hard-coded into the source code.

---

### 2. Create the Gemini client

A Gemini client is initialized once and reused throughout the application.

```python
client = genai.Client()
```

This keeps the API client setup separate from individual user requests.

---

### 3. Validate user input

User input is passed through a Pydantic model before being sent to Gemini.

```text
Raw User Input
      ↓
Pydantic Model
      ↓
Validated Input
```

The current validation requires the input to contain at least **one character**.

---

### 4. Apply the system prompt

The application uses a system prompt to define the assistant's general behavior.

The system prompt instructs the model to:

- Provide accurate and clear answers.
- Explain technical concepts in a beginner-friendly way.
- Use simple language when possible.
- Communicate uncertainty when appropriate.
- Avoid inventing information.

Conceptually:

```text
System Prompt
      +
User Input
      ↓
Gemini Model
```

---

### 5. Send the request

The validated input and system instruction are sent to the Gemini model using the Google GenAI SDK.

The application uses streaming mode:

```python
stream=True
```

---

### 6. Stream the response

Instead of waiting for the complete response, Gemini sends response events incrementally.

```text
Gemini
   ↓
Stream Events
   ↓
Text Delta Events
   ↓
Streamlit UI
```

The frontend uses Streamlit's `st.write_stream()` to display the response as it arrives.

---

## 6. Error Handling

The application includes multiple layers of error handling.

### Input validation errors

Invalid user input is handled using Pydantic:

```text
Invalid Input
     ↓
ValidationError
     ↓
User-friendly warning
```

### Gemini API errors

Streaming API errors are detected and converted into application-level errors rather than being displayed as normal AI responses.

```text
Gemini API Error
       ↓
RuntimeError
       ↓
Streamlit Error Message
```

### Unexpected errors

Unexpected application errors are caught and presented using a generic user-friendly message.

This prevents raw technical errors from unnecessarily being exposed to the user.

---

## 7. Chat History

The Streamlit frontend uses `st.session_state` to maintain chat history during the current application session.

```text
User Message
      ↓
Session State
      ↓
Display in Chat
      ↓
Assistant Response
      ↓
Session State
```

This allows previous messages to remain visible while the user continues the conversation.

> Note: The current implementation stores chat history in Streamlit session state for the UI. It does not yet implement persistent database storage or long-term conversation memory.

---

## 8. Loading State

The application provides a loading indicator while the response is being generated.

```text
User submits question
        ↓
"Thinking..."
        ↓
Gemini response starts
        ↓
Streaming response
```

This provides feedback to the user that the application is processing the request.

---

## 9. What You Learned

This project helped build the fundamentals required for developing LLM applications.

### Python

- Functions
- User input handling
- Exception handling
- Variables and constants
- Iterating over streamed events
- Modular code organization
- Generator functions

### Pydantic

- Creating a `BaseModel`
- Defining validated fields
- Using `Field`
- Applying minimum string-length validation
- Separating raw input from validated input
- Handling `ValidationError`

### Gemini API Integration

- Loading API credentials from environment variables
- Creating a Gemini client
- Sending input to a Gemini model
- Using system instructions
- Receiving streamed responses
- Processing streaming events
- Handling API errors

### Streamlit

- Creating a web-based AI interface
- `st.chat_input()`
- `st.chat_message()`
- `st.session_state`
- `st.spinner()`
- `st.write_stream()`
- Displaying user-friendly errors

### Application Design

The project also introduced an important software-engineering principle:

```text
                 Application
                     │
          ┌──────────┴──────────┐
          ↓                     ↓
      Frontend               Backend
      app.py                 main.py
          │                     │
          ↓                     ↓
    User Interface       Gemini API Logic
          │                     │
          └──────────┬──────────┘
                     ↓
              AI Response
```

Each component has a clear responsibility.

---

## 10. Current Features

The current version includes:

- ✅ Streamlit web interface
- ✅ Gemini API integration
- ✅ User input validation
- ✅ System prompt
- ✅ Streaming responses
- ✅ Loading state
- ✅ Error handling
- ✅ Chat history
- ✅ Modular frontend/backend structure
- ✅ Environment variable configuration
- ✅ Secure API key handling through `.env`

---

## 11. What Could Improve Next

The current project intentionally focuses on the fundamentals. The following improvements can be explored in future versions:

- Conversation memory using Gemini interaction history
- Persistent conversation storage
- Clear chat functionality
- Structured model output
- RAG (Retrieval-Augmented Generation)
- Embeddings
- Vector databases
- Document ingestion
- Tool calling
- External API integration
- MCP integration
- Agentic workflows
- Multi-step task execution
- Automated testing
- Logging and observability
- Production-oriented project structure
- Deployment

These improvements would gradually move the project from a simple LLM chatbot toward a more capable **AI application and eventually an agentic system**.

---

## 12. Project Evolution

### Version 1 — Command-Line Chatbot

The initial version focused on the fundamentals:

```text
User
 ↓
Pydantic
 ↓
Gemini API
 ↓
Streaming
 ↓
Terminal
```

### Version 2 — Streamlit AI Chatbot

The project was then improved with:

- A clean Streamlit interface
- Modular frontend/backend architecture
- System prompt
- Loading state
- Error handling
- Chat history
- Improved user experience

The architecture became:

```text
User
 ↓
Streamlit Frontend
 ↓
Backend Function
 ↓
Pydantic Validation
 ↓
System Prompt
 ↓
Gemini API
 ↓
Streaming Response
 ↓
Streamlit UI
```

This version provides a stronger foundation for future LLM and AI-agent projects.

---

## 13. Future Direction

This project is being developed progressively from a simple LLM application toward more advanced AI systems.

```text
Simple Chatbot
      ↓
Streaming Chatbot
      ↓
Structured Outputs
      ↓
Conversation Memory
      ↓
RAG
      ↓
Tool Calling
      ↓
MCP
      ↓
Agentic Workflows
      ↓
Production AI Application

