import streamlit as st
import pandas as pd

st.set_page_config(page_title="🧺 Fashion Chatbot Preprocessor", layout="wide")
st.title("🧺 Fashion Chatbot Dataset Augmentor")

# File Uploads
styles_file = st.file_uploader("Upload `styles.csv`", type="csv")
chatbot_file = st.file_uploader("Upload `ClothesShopChatbotDataset.csv`", type="csv")

if styles_file and chatbot_file:
    # Load and clean styles.csv
    df_styles = pd.read_csv(styles_file)
    df_styles = df_styles.dropna(axis=1, how='all')
    st.subheader("📦 Styles Dataset Preview")
    st.dataframe(df_styles.head())

    # Load and clean chatbot dataset
    chatbot_df = pd.read_csv(chatbot_file)
    chatbot_df = chatbot_df.dropna(axis=1, how='all')
    st.subheader("🗨️ Chatbot Dataset Preview")
    st.dataframe(chatbot_df.head())

    # Gap data to be added
    gap_data = [
        {"Question": "I want to return this dress and get a refund.", "Context": "refund_request", "Answer": "Sure, please provide your order ID to initiate a refund."},
        {"Question": "This is taking too long. I want to speak to a manager.", "Context": "escalation", "Answer": "I'm escalating this issue to our senior support team."},
        {"Question": "Where can I leave feedback about my purchase?", "Context": "feedback_request", "Answer": "You can leave feedback after delivery via the app or click the feedback link sent to your email."},
        {"Question": "Has my support ticket been closed?", "Context": "ticket_status", "Answer": "Your support ticket was successfully resolved and closed. Let us know if you need more help!"},
        {"Question": "What is your return policy?", "Context": "general_inquiry", "Answer": "You can return any product within 7 days of delivery."},
        {"Question": "How do I get a refund for my item?", "Context": "refund_request", "Answer": "To get a refund, go to your Orders section, select the item, and tap on 'Return or Refund'. It only takes a few steps!"},
        {"Question": "Can I get a refund without contacting support?", "Context": "refund_request", "Answer": "Yes! You can start a return directly through the app or website—no need to talk to support."},
        {"Question": "When will I get my refund?", "Context": "refund_timeline", "Answer": "Once we receive your returned item, the refund is processed within 3–5 business days."},
        {"Question": "Do you charge for return shipping?", "Context": "refund_shipping", "Answer": "Return shipping is completely free for most products. We’ll provide a prepaid label during return initiation."},
        {"Question": "What is your refund policy?", "Context": "refund_policy", "Answer": "You can return any unused product within 7 days of delivery for a full refund. Items must be in their original condition with tags intact."},
        {"Question": "How do I know if my item is eligible for a refund?", "Context": "refund_eligibility", "Answer": "Refunds are available on items returned within 7 days, in unused condition, and not part of final sale or hygiene-restricted categories."},
        {"Question": "What happens if I miss the return window?", "Context": "refund_policy", "Answer": "If the 7-day window is missed, the refund may not be possible. Still, you can reach out via the Help Center for special cases."},
        {"Question": "Can I exchange instead of refunding?", "Context": "exchange_request", "Answer": "Yes! During the return process, simply choose 'Exchange' and select your preferred size or color—super easy!"},
        {"Question": "I paid already. Why is my order not confirmed?", "Context": "payment_unconfirmed", "Answer": "Sorry! Payments can take up to 30 mins. If still unconfirmed, contact support with your transaction ID."},
        {"Question": "It’s been over 30 minutes, but my order is still not confirmed.", "Context": "payment_escalation", "Answer": "Thanks for your patience! Please share your payment ID or transaction ref so our support team can verify it."}
    ]

    # Create new DataFrame and concatenate
    gaps_df = pd.DataFrame(gap_data)
    chatbot_augmented = pd.concat([chatbot_df, gaps_df], ignore_index=True)

    st.subheader("✨ Augmented Chatbot Dataset")
    st.dataframe(chatbot_augmented.tail(15))  # Show only the new entries

    # Download button
    csv = chatbot_augmented.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Augmented Dataset", csv, "ClothesShopChatbotDataset_augmented.csv", "text/csv")
else:
    st.info("📂 Please upload both datasets to proceed.")






