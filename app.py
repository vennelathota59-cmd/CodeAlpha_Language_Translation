import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translator", page_icon="🌍")

st.title("🌍 Language Translation App")

text = st.text_area("Enter text to translate")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Tamil": "ta",
    "Kannada": "kn"
}

source = st.selectbox("Source Language", list(languages.keys()))
target = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation Completed!")
        st.text_area("Translated Text", translated, height=150)