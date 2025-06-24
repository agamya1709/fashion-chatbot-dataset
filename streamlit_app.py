import streamlit as st
import pandas as pd
import openai
import numpy as np

st.set_page_config(page_title="🛍️ Fashion Chatbot", layout="wide")
st.title("🧠 Fashion Support Chatbot")

# Sidebar: API Key input
api_key = st.sidebar.text_input("🔑 Enter your OpenAI API Key", type="password")
if not api_key:
    st.warning("Please enter your OpenAI API key to continue.")
    st.stop()
openai.api_key = api_key

# Upload CSVs
st.sidebar.subheader("📂 Upload Your CSV Files")
styles_file = st.sidebar.file_uploader("Upload `styles.csv`", type="csv")
original_file = st.sidebar.file_uploader("Upload `ClothesShopChatbotDataset.csv`", type="csv")
augmented_file = st.sidebar.file_uploader("Upload `ClothesShopChatbotDataset_augmented.csv`", type="csv")

# Helper: load CSV
def load_csv(file, name):
    try:
        df = pd.read_csv(file)
        st.sidebar.success(f"✅ Loaded {name} ({len(df)} rows)")
        return df
    except Exception as e:
        st.sidebar.error(f"❌ Failed to load {name}: {e}")
        return None

# Load datasets
styles_df = load_csv(styles_file, "styles.csv") if styles_file else None
original_df = load_csv(original_file, "Chatbot Dataset") if original_file else None
augmented_df = load_csv(augmented_file, "Augmented Chatbot Dataset") if augmented_file else None

# Select dataset
st.subheader("💬 Chat with the Bot")
query = st.text_input("Ask me anything about your orders, returns, styles...")

dataset_choice = st.radio("📄 Choose a dataset to chat with:", ["Original", "Augmented"])
selected_df = original_df if dataset_choice == "Original" else augmented_df

# Get OpenAI embedding
def get_embedding(text):
    try:
        response = openai.Embedding.create(
            input=text,
            model="text-embedding-ada-002"
        )
        return response["data"][0]["embedding"]
    except Exception as e:
        st.error(f"Embedding error: {e}")
        return None

# Cosine similarity (manual version without sklearn)
def cosine_sim(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Handle query
if query and selected_df is not None:
    st.info("🔍 Matching your query with most relevant answer...")
    try:
        user_emb = get_embedding(query)
        best_score = -1
        best_match = None

        for _, row in selected_df.iterrows():
            question = row["Question"]
            emb = get_embedding(question)
            if emb:
                score = cosine_sim(user_emb, emb)
                if score > best_score:
                    best_score = score
                    best_match = row

        if best_match is not None:
            st.success(f"🤖 **Answer**: {best_match['Answer']}")
            with st.expander("📝 Matched Question"):
                st.markdown(best_match["Question"])
            st.caption(f"🧠 Similarity score: {round(best_score, 2)}")
        else:
            st.warning("❓ No suitable answer found.")

    except Exception as e:
        st.error(f"Something went wrong: {e}")
else:
    st.caption("👆 Upload CSVs and ask a question to begin.")

# Show previews (optional)
if styles_df is not None:
    st.subheader("👗 Style Dataset Preview")
    st.dataframe(styles_df.head())

if original_df is not None and augmented_df is not None:
    with st.expander("🆚 Compare Original and Augmented Chatbot Data"):
        col1, col2 = st.columns(2)
        col1.write("📄 Original")
        col1.dataframe(original_df.sample(5))
        col2.write("📄 Augmented")
        col2.dataframe(augmented_df.sample(5))









