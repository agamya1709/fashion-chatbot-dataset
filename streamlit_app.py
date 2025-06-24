import streamlit as st
import pandas as pd
import difflib

# Load datasets
@st.cache_data
def load_data():
    df_aug = pd.read_csv("ClothesShopChatbotDataset_augmented.csv")
    df_styles = pd.read_csv("styles.csv")
    return df_aug, df_styles

df_aug, df_styles = load_data()

questions = df_aug['question'].fillna("").tolist()
answers = df_aug['answer'].fillna("").tolist()

# Streamlit UI
st.title("🧥 Fashion Chatbot")
st.write("Ask me anything related to fashion, clothing, or style suggestions!")

user_input = st.text_input("You:", "What should I wear for a wedding?")

if user_input:
    # Find the closest match
    best_match = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.4)
    if best_match:
        best_idx = questions.index(best_match[0])
        best_response = answers[best_idx]
    else:
        best_response = "I'm sorry, I didn't understand that. Could you please rephrase?"

    st.markdown("**Chatbot:** " + best_response)

    # Optional: fashion style matching
    if "recommend" in user_input.lower() or "wear" in user_input.lower():
        st.subheader("👗 Suggested Styles")
        suggested_styles = df_styles.sample(3)
        for _, row in suggested_styles.iterrows():
            st.markdown(f"**{row['style_name']}** - {row['description']}")




