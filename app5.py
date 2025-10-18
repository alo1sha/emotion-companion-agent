import streamlit as st
from transformers import pipeline

# Load a pretrained sentiment analysis model from Hugging Face
emotion_model = pipeline("sentiment-analysis")

# App title and description
st.title("💬 Emotion Companion AI Agent")
st.write("Talk to me about your day, and I’ll try to understand how you feel 🤖")

# User input box
user_input = st.text_area("Type here 👇")

# When the button is pressed
if st.button("Analyze Emotion"):
    if user_input.strip():
        # Run the AI model
        result = emotion_model(user_input)[0]
        label = result['label']
        score = result['score']

        # Display the analysis
        st.subheader("Emotion Analysis:")
        st.write(f"🧠 Detected emotion: **{label}** (Confidence: {score:.2f})")

        # Generate an AI-based empathetic response
        if label == "POSITIVE":
            st.success("😄 I'm happy to hear that! Keep spreading positive energy 🌞")
        elif label == "NEGATIVE":
            st.warning("😔 Sounds like a tough day. Take care of yourself 💛")
        else:
            st.info("🙂 You seem balanced today — take a deep breath and enjoy your moment 🌿")
    else:
        st.write("🕵️‍♀️ Please type something first!")
