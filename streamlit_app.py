
import streamlit as st
import pandas as pd
import openai
import os

# App title
st.title("🛍️ Fashion Chatbot")

# Sidebar: API Key input
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
if not api_key:
    st.warning("Please enter your OpenAI API key to continue.")
    st.stop()
openai.api_key = api_key

# Load datasets
@st.cache_data
def load_data():
    df_chat = pd.read_csv("ClothesShopChatbotDataset.csv")
    df_styles = pd.read_csv("styles.csv")
    df_aug=pd.read_csv("ClothesShopChatbotDataset_augmented.csv")
    return df_chat, df_styles,df_aug

df_chat, df_styles,df_aug = load_data()

# Chat Interface
user_input = st.text_input("👤 You:", placeholder="Ask me anything about fashion...")

if user_input:
    with st.spinner("Thinking..."):
        # Prompt engineering with context
        context = "\n".join(
            df_chat["Question"] + ": " + df_chat["Answer"]
        )
        prompt = f"{context}\nUser: {user_input}\nBot:"

        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150,
                temperature=0.7
            )
            bot_response = response.choices[0].text.strip()
            st.success(f"🤖 Bot: {bot_response}")

        except Exception as e:
            st.error(f"Error: {str(e)}")
