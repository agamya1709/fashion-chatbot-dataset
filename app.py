import streamlit as st
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

# Load the ResNet50 model
@st.cache_resource
def load_model():
    return ResNet50(weights='imagenet', include_top=False, pooling='avg')

model = load_model()

# Function to extract features from an image
def extract_features(img_path):
    try:
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        features = model.predict(x)
        return features.flatten()
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return None

# Build the database of features
@st.cache_resource
def build_feature_db(image_dir="images"):
    features_db = []
    image_paths = []
    for filename in os.listdir(image_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            path = os.path.join(image_dir, filename)
            features = extract_features(path)
            if features is not None:
                features_db.append(features)
                image_paths.append(path)
    return features_db, image_paths

# Streamlit UI
st.set_page_config(page_title="Fashion Image Search", layout="wide")
st.title("👗 Fashion Image-Based Search")
st.markdown("Upload a fashion item image to find visually similar styles from your dataset.")

# Load dataset features
image_dir = "images"
if not os.path.exists(image_dir):
    st.warning("Please create an `images/` folder and add some fashion images.")
else:
    features_db, image_paths = build_feature_db(image_dir)

    # Upload query image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        query_path = "temp_query.jpg"
        with open(query_path, "wb") as f:
            f.write(uploaded_file.read())

        st.image(query_path, caption="Uploaded Image", use_column_width=False, width=250)
        query_features = extract_features(query_path)

        # Find and show similar images
        if query_features is not None and features_db:
            sims = cosine_similarity([query_features], features_db)[0]
            top_indices = np.argsort(sims)[-5:][::-1]

            st.subheader("Top 5 Similar Fashion Items")
            cols = st.columns(5)
            for i, idx in enumerate(top_indices):
                with cols[i]:
                    st.image(image_paths[idx], width=150, caption=f"Score: {sims[idx]:.2f}")
        elif not features_db:
            st.error("No fashion images found in your `images/` folder.")
