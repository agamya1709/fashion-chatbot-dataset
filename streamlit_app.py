import streamlit as st
import pandas as pd

# Load CSV
@st.cache_data
def load_data():
    df = pd.read_csv("ClothesShopChatbotDataset_augmented.csv")
    df = df.dropna(subset=['Question', 'Answer'])
    return df

df = load_data()

st.title("🛍️ Fashion Chatbot")
st.write("Ask me about returns, refunds, orders, or anything fashion related!")

user_input = st.text_input("Your question:")

def find_best_match(query, questions):
    query = query.lower()
    for i, q in enumerate(questions):
        if query in q.lower():
            return i
    return None

if user_input:
    index = find_best_match(user_input, df["Question"])
    if index is not None:
        st.success("🤖 " + df["Answer"].iloc[index])
    else:
        st.warning("🤖 Sorry, I don't know how to answer that. Please try rephrasing your question.")



