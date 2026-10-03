import streamlit as st

from main import generate_response


st.title("🤖 Xictek AI Assistant")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User input
if prompt := st.chat_input("Enter your question..."):

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):

        # Create a placeholder for the response
        response_placeholder = st.empty()

        # Show "Thinking..." while waiting for the first token
        response_placeholder.markdown("💭 *Thinking...*")

        full_response = ""

        # Start streaming response
        response_stream = generate_response(prompt)

        for chunk in response_stream:

            # Add each streamed chunk
            full_response += chunk

            # Replace "Thinking..." with the actual response
            response_placeholder.markdown(full_response)

    # Save AI response
    if full_response:
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": full_response,
            }
        )