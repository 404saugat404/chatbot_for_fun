import streamlit as st
import google.generativeai as genai


# Set the API key
api_key = 'your api key'

# Configure the generative AI with the API key
genai.configure(api_key=api_key)

# Initialize the GenerativeModel
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get a response from the model
def get_response(prompt):
    response = model.generate_content(prompt)  # Generate content using the prompt
    return response.text  # Directly access the text attribute of the response

# Streamlit app layout
st.title("Chatbot")

if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# User input
user_input_key = "input_" + str(len(st.session_state.conversation))  # Create a unique key for each input field
user_input = st.text_input("You:", key=user_input_key)

# Process input and generate response
if st.button("Send"):
    if user_input:
        st.session_state.conversation.append(("You", user_input))
        bot_response = get_response(user_input)
        st.session_state.conversation.append(("Bot", bot_response))
        user_input_key = "input_" + str(len(st.session_state.conversation))  # Update the key for the next input field
        st.text_input("You:", value="", key=user_input_key)  # Use the updated key for the next input field

# Display conversation
for speaker, text in st.session_state.conversation:
    st.write(f"**{speaker}**: {text}")
