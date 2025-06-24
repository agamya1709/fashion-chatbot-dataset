import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="🧠 Fashion Chatbot", layout="centered")
st.title("👗 Fashion Support Chatbot")

# Upload the dataset
uploaded_file = st.file_uploader("📂 Upload `ClothesShopChatbotDataset.csv`", type="csv")

# Load model
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

if uploaded_file:
    # Read and clean the dataset
    try:
        df = pd.read_csv(uploaded_file)
        df.dropna(subset=["Question", "Answer"], inplace=True)
    except Exception as e:
        st.error(f"Failed to read CSV: {e}")
        st.stop()

    # Precompute question embeddings
    @st.cache_data
    def compute_embeddings(questions):
        return model.encode(questions, convert_to_tensor=True)

    question_embeddings = compute_embeddings(df["Question"].tolist())

    # Chat input
    user_query = st.text_input("💬 Ask a question about your order, refund, or style...")

    if user_query:
        # Encode user query
        user_embedding = model.encode([user_query], convert_to_tensor=True)

        # Compute cosine similarity
        similarity_scores = cosine_similarity(user_embedding, question_embeddings)[0]
        top_idx = similarity_scores.argmax()
        best_match = df.iloc[top_idx]

        # Display result
        st.markdown(f"**🤖 Chatbot:** {best_match['Answer']}")
        with st.expander("🔍 Matched Question"):
            st.markdown(f"`{best_match['Question']}`")

else:
    st.info("📁 Please upload your chatbot dataset to get started.")








