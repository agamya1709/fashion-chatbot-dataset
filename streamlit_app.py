import streamlit as st
import pandas as pd

# Load all required CSVs
@st.cache_data
def load_data():
    df_chat = pd.read_csv("ClothesShopChatbotDataset_augmented.csv")
    df_styles = pd.read_csv("styles.csv")

    df_chat = df_chat.dropna(subset=["Question", "Answer"])
    df_styles = df_styles.dropna(subset=["productDisplayName", "gender", "masterCategory"])

    return df_chat, df_styles

df_chat, df_styles = load_data()

# UI
st.title("👗 Fashion Assistant Chatbot")
st.subheader("Ask about returns, refunds, exchanges, or fashion style suggestions!")

user_query = st.text_input("🧠 Ask your question here:")

# Search for best match in FAQ
def get_answer(user_input):
    user_input = user_input.lower()
    for i, q in enumerate(df_chat["Question"]):
        if user_input in q.lower():
            return df_chat["Answer"].iloc[i]
    return None

# Style suggestion (optional)
def suggest_styles(gender=None, category=None):
    filtered = df_styles.copy()

    if gender:
        filtered = filtered[filtered["gender"].str.lower() == gender.lower()]
    if category:
        filtered = filtered[filtered["masterCategory"].str.lower() == category.lower()]

    return filtered["productDisplayName"].sample(min(5, len(filtered))) if not filtered.empty else []

# Chatbot logic
if user_query:
    response = get_answer(user_query)
    
    if response:
        st.success("🤖 " + response)
    else:
        st.warning("🤖 I couldn’t find a perfect answer, but here are some style suggestions!")
        gender_guess = "Men" if "men" in user_query.lower() else "Women" if "women" in user_query.lower() else None
        category_guess = "Apparel" if "shirt" in user_query.lower() or "dress" in user_query.lower() else None
        
        suggestions = suggest_styles(gender=gender_guess, category=category_guess)

        if not suggestions.empty:
            st.info("👕 Style Suggestions:")
            for style in suggestions:
                st.write(f"• {style}")
        else:
            st.write("No matching styles found.")




