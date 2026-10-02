from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field


# Load environment variables from the .env file.
load_dotenv()


class Input(BaseModel):
    """Validate user input before sending it to the model."""

    text: str = Field(
        min_length=3,
        description="The user's question or prompt.",
    )


# Create the Gemini client once and reuse it for all interactions.
client = genai.Client()

MAX_INTERACTIONS = 15

count = 0

while count < MAX_INTERACTIONS:
    text = input("Enter your question (or type 'exit' to quit): ")

    if text == "exit":
        break

    try:
        # Validate the user's input before sending it to Gemini.
        validated_input = Input(text=text)

        stream = client.interactions.create(
            model="gemini-3.8-flash",
            input=validated_input.text,
            stream=True,
        )

        for event in stream:
            if event.event_type == "step.delta":
                if event.delta.type == "text":
                    print(event.delta.text, end="", flush=True)

        print()
        count += 1

    except Exception as e:
        print(f"Error: {e}")

