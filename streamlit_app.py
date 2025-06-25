import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Title
st.title("🛍️ Fashion Chatbot")
st.markdown("Ask me anything about fashion shopping, returns, refunds, and more!")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("ClothesShopChatbotDataset_augmented.csv")
    df = df.dropna(subset=['Question', 'Answer'])
    return df

df = load_data()

# Vectorize questions
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Question'])

# Chat Interface
user_input = st.text_input("🧍 You:", placeholder="Ask me anything related to clothes shopping...")

if user_input:
    with st.spinner("Thinking..."):
        user_vec = vectorizer.transform([user_input])
        similarity = cosine_similarity(user_vec, X)
        idx = similarity.argmax()
        best_match = df.iloc[idx]

        st.success(f"🤖 Bot: {best_match['Answer']}")


