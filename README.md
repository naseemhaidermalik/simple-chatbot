# Simple Gemini Chatbot

A simple command-line chatbot built with Python and Google's Gemini API. The project demonstrates the fundamentals of building an LLM-powered application, including user input, Pydantic validation, API integration, and streamed model responses.

## 1. What You Build

This project is a **command-line AI chatbot** that:

- Accepts questions from the user.
- Validates user input using Pydantic.
- Sends the validated input to Google's Gemini model.
- Receives the model response as a stream.
- Displays the response incrementally in the terminal.
- Allows the user to exit the chatbot by typing `exit`.
- Supports up to 15 interactions per execution.

### Workflow

```text
User Input
    ↓
Pydantic Validation
    ↓
Gemini API
    ↓
Streaming Response
    ↓
Terminal Output
```

## 2. Technology Used

- **Python** — Core programming language.
- **Google GenAI SDK** — Integration with Google's Gemini API.
- **Gemini** — Large language model used to generate responses.
- **Pydantic** — Validation of user input.
- **python-dotenv** — Loads environment variables from the `.env` file.
- **Conda** — Python environment management.

## 3. How to Run It

### Step 1: Clone the repository

```bash
git clone <your-repository-url>
cd <your-repository-name>
```

### Step 2: Create and activate a virtual environment

Create your Conda environment and activate it:

```bash
conda create -n chatbot python=3.12
conda activate chatbot
```

### Step 3: Install dependencies

Install the required packages:

```
pip install -r requirements.txt
```

### Step 4: Configure the API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

The `.env` file should **not** be committed to GitHub.

Make sure `.env` is included in your `.gitignore` file:

```text
.env
```

### Step 5: Run the chatbot

```bash
python main.py
```

Then enter your question:

```text
Enter your question (or type 'exit' to quit): How does machine learning work?
```

To stop the chatbot:

```text
exit
```

## 4. API Integration Approach

The application uses Google's GenAI SDK to communicate with the Gemini model.

The integration follows these steps:

### 1. Load environment variables

The API key is stored in the `.env` file and loaded using `python-dotenv`.

### 2. Create the Gemini client

A Gemini client is initialized once and reused throughout the application.

### 3. Validate user input

User input is passed through a Pydantic model before being sent to the API.

```text
Raw Input
    ↓
Pydantic Model
    ↓
Validated Input
```

The current validation requires the input to contain at least three characters.

### 4. Send the request

The validated text is sent to the Gemini model using the GenAI SDK.

### 5. Stream the response

The application uses streaming so that generated text can be displayed incrementally rather than waiting for the complete response.

```text
Gemini
  ↓
Stream Events
  ↓
Text Delta Events
  ↓
Terminal
```

## 5. What You Learned

This project helped build the fundamentals required for developing LLM applications.

### Python

- User input with `input()`
- `while` loops
- Conditional statements
- Exception handling
- Variables and constants
- Iterating over streamed events

### Pydantic

- Creating a `BaseModel`
- Defining validated fields
- Using `Field`
- Applying minimum string-length validation
- Separating raw input from validated input

### LLM API Integration

- Loading API credentials from environment variables
- Creating a GenAI client
- Sending input to a Gemini model
- Receiving streamed responses
- Processing streaming events

### Application Design

The project also introduced an important software-engineering principle:

```text
User Input
    ↓
Validation
    ↓
API
    ↓
Response Processing
    ↓
Output
```

Each stage has a clear responsibility.

## 6. What Would Improve Next

The current project intentionally focuses on the fundamentals. The following improvements could be explored in future versions:

- Conversation history and memory
- Better error handling and recovery
- Structured model output
- System instructions and configurable prompts
- RAG (Retrieval-Augmented Generation)
- Vector databases
- Tool calling
- External API integration
- MCP integration
- Agentic workflows and multi-step task execution
- Automated testing
- Logging and observability
- Production-oriented project structure

These improvements would gradually move the project from a simple LLM chatbot toward a more capable **AI agent system**.