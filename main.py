from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field


# Load environment variables from the .env file.
load_dotenv()


class PromptInput(BaseModel):
    """Validate user input before sending it to the model."""

    text: str = Field(
        min_length=1,
        description="The user's question or prompt.",
    )


# Create the Gemini client once and reuse it for all interactions.
client = genai.Client()


SYSTEM_INSTRUCTION="""
You are Xictek AI Assistant, a professional AI chatbot.


Your responsibilities:
- Provide accurate and helpful answers.
- Be clear, concise, and professional.
- Explain technical concepts in simple language when needed.
- Do not make up information.
"""


def generate_response(prompt_text: str):
    """Generate a streaming response from Gemini."""

    # Validate user input (Pydantic Validation)
    validated_input = PromptInput(text=prompt_text)

    # Create a streaming intraction
    stream = client.interactions.create(
        model="gemini-3.8-flash",
        system_instruction=SYSTEM_INSTRUCTION,
        input=validated_input.text,
        stream=True,
        generation_config={
            "temperature": 0.3,
            "max_output_tokens": 2000
        },
    )


    # Yield text chunks as they arrive.
    for event in stream:
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                yield event.delta.text
