import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

st.set_page_config(page_title="🛍️ Local Fashion Chatbot", layout="wide")
st.title("🤖 Offline Fashion Chatbot (No Billing Needed)")

# Upload CSVs
st.sidebar.header("📂 Upload Your Files")
styles_file = st.sidebar.file_uploader("Upload `styles.csv`", type="csv")
original_file = st.sidebar.file_uploader("Upload `ClothesShopChatbotDataset.csv`", type="csv")
augmented_file = st.sidebar.file_uploader("Upload `ClothesShopChatbotDataset_augmented.csv`", type="csv")

# Load CSVs
def load_csv(file, name):
    try:
        df = pd.read_csv(file)
        st.sidebar.success(f"✅ Loaded {name} ({len(df)} rows)")
        return df
    except Exception as e:
        st.sidebar.error(f"❌ Failed to load {name}: {e}")
        return None

styles_df = load_csv(styles_file, "styles.csv") if styles_file else None
original_df = load_csv(original_file, "Original Chatbot Dataset") if original_file else None
augmented_df = load_csv(augmented_file, "Augmented Chatbot Dataset") if augmented_file else None

# Select dataset
dataset_choice = st.radio("🧠 Choose dataset to use:", ["Original", "Augmented"])
selected_df = original_df if dataset_choice == "Original" else augmented_df

# Load embedding model
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# Handle chat
query = st.text_input("💬 Ask something about orders, returns, style, etc...")

if query and selected_df is not None:
    with st.spinner("Thinking..."):
        questions = selected_df["Question"].fillna("").tolist()
        answers = selected_df["Answer"].fillna("").tolist()
        query_embedding = model.encode([query])
        question_embeddings = model.encode(questions)
        scores = cosine_similarity(query_embedding, question_embeddings)[0]
        top_idx = np.argmax(scores)

        st.success(f"🤖 {answers[top_idx]}")
        with st.expander("🔍 Matched Question"):
            st.markdown(questions[top_idx])
        st.caption(f"🧠 Similarity: {round(scores[top_idx], 2)}")

# Show style preview
if styles_df is not None:
    st.subheader("👗 Style Dataset Preview")
    st.dataframe(styles_df.head())

