import streamlit as st
from deep_translator import GoogleTranslator

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)
st.sidebar.title("🌍 AI Translator")

st.sidebar.info("""
### About

This application translates text into multiple languages using Google Translator API.

### Technologies

- Python
- Streamlit
- deep-translator
""")

# -----------------------------
# Title
# -----------------------------
st.title("🌍 AI Language Translation App")
st.write("Translate text instantly into multiple languages using Artificial Intelligence.")

# -----------------------------
# Text Input
# -----------------------------
text = st.text_area(
    "Enter text to translate",
    height=150,
    placeholder="Type your text here..."
)

# Character Counter
st.caption(f"Characters: {len(text)}")
if text:
    st.caption(f"Words: {len(text.split())}")

# -----------------------------
# Language List
# -----------------------------
languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Turkish": "tr",
    "Dutch": "nl",
    "Greek": "el",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id",
    "Polish": "pl"
}

# -----------------------------
# Language Selection
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    source = st.selectbox("Source Language", list(languages.keys()))

with col2:
    target = st.selectbox("Target Language", list(languages.keys()))

# -----------------------------
# Buttons
# -----------------------------
col3, col4 = st.columns(2)

with col3:
    translate_btn = st.button("🌐 Translate")

with col4:
    clear_btn = st.button("🗑️ Clear")

# -----------------------------
# Clear Button
# -----------------------------
if clear_btn:
    st.rerun()

# -----------------------------
# Translate
# -----------------------------
if translate_btn:

    if text.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)
            st.subheader("📜 Translation History")

            st.write("Original Text:")
            st.info(text)

            st.write("Translated Text:")
            st.success(translated)

            st.success("✅ Translation Completed Successfully!")
            st.balloons()

            st.text_area(
                "Translated Text",
                translated,
                height=150
            )

            st.download_button(
                label="📥 Download Translation",
                data=translated,
                file_name="translated_text.txt",
                mime="text/plain"
            )

        except Exception:
            st.error("❌ Translation failed. Please try again.")

# -----------------------------
# About Section
# -----------------------------
st.markdown("---")

st.subheader("😄 About This App")

st.write("""
🌍 **Lost in translation? Don't worry—we've got you!**

This AI-powered translator converts your text into different languages within seconds. Whether you're learning a new language, completing assignments, chatting with friends, or planning your next trip, this app is here to make translation quick and easy.

### ✨ Features
- 🌐 Supports 25+ Languages
- ⚡ Fast AI-powered Translation
- 📊 Character & Word Counter
- 📥 Download Translated Text
- 🛡️ Error Handling
- 🎈 Fun Success Animation

**Type ➜ Translate ➜ Smile 😊**
""")

st.markdown("---")
st.caption("💻 Developed by Vennela Thota | CodeAlpha AI Internship Project")