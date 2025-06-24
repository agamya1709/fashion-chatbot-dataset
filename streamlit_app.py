import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load augmented chatbot dataset and styles
@st.cache_data
def load_data():
    df_aug = pd.read_csv("ClothesShopChatbotDataset_augmented.csv")
    df_styles = pd.read_csv("styles.csv")
    return df_aug, df_styles

df_aug, df_styles = load_data()

# Preprocess and vectorize chatbot questions
questions = df_aug['question'].fillna("").tolist()
answers = df_aug['answer'].fillna("").tolist()
vectorizer = TfidfVectorizer().fit(questions)
question_vectors = vectorizer.transform(questions)

# Streamlit UI
st.title("🧥 Fashion Chatbot")
st.write("Ask me anything related to fashion, clothing, or style suggestions!")

user_input = st.text_input("You:", "What should I wear for a wedding?")

if user_input:
    # Vectorize user query and compute similarity
    input_vector = vectorizer.transform([user_input])
    similarity_scores = cosine_similarity(input_vector, question_vectors)
    best_idx = similarity_scores.argmax()
    best_response = answers[best_idx]

    st.markdown("**Chatbot:** " + best_response)

    # Optional: fashion style matching
    if "recommend" in user_input.lower() or "wear" in user_input.lower():
        st.subheader("👗 Suggested Styles")
        suggested_styles = df_styles.sample(3)  # You can add logic to match styles by occasion/type
        for _, row in suggested_styles.iterrows():
            st.markdown(f"**{row['style_name']}** - {row['description']}")


