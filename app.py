import streamlit as st
import random

# 🎯 Page Config
st.set_page_config(
    page_title="AURA Emotion AI",
    page_icon="🔥",
    layout="centered"
)

# 🧠 Emotion Logic
def predict(text):
    emotions = {
        "happy": ["joy", "smile", "excited"],
        "sad": ["alone", "tired", "lost"],
        "angry": ["rage", "furious", "annoyed"],
        "neutral": ["okay", "fine", "normal"]
    }

    text = text.lower()

    if "happy" in text:
        emotion = "happy"
    elif "sad" in text:
        emotion = "sad"
    elif "angry" in text:
        emotion = "angry"
    else:
        emotion = "neutral"

    word = random.choice(emotions[emotion])
    return word, emotion


# 🎨 UI
st.title("🔥 AURA Emotion Detection AI")
st.markdown("### Understand emotions from text using AI")

st.write("👉 Detect emotion")
st.write("👉 Predict next word")

# 📝 Input
text = st.text_input("💬 Enter your text")

# 🚀 Button
if st.button("Predict"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text")
    else:
        word, emotion = predict(text)

        st.success(f"✨ Next Word: {word}")
        st.info(f"🧠 Emotion: {emotion}")

        emoji_map = {
            "happy": "😊",
            "sad": "😢",
            "angry": "😡",
            "neutral": "😐"
        }

        st.markdown(f"### Emotion: {emoji_map[emotion]}")
