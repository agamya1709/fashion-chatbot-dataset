# 👗 Fashion Assistant Chatbot

An intelligent fashion chatbot that answers customer queries and suggests clothing styles. Built using **Streamlit** for a web interface and **JupyterLite** for lightweight, browser-based notebook access.

# 🌐 Live Demos

🔷 Streamlit App: https://fashion-chatbot-dataset-bd53cgmuwmdab28z3wshw2.streamlit.app/

🔷 JupyterLite Notebook:Untitled8.iypnb
![image](https://github.com/user-attachments/assets/8ee4d023-7dbb-401f-aca8-4ebc6d17f795)

## 📁 Datasets Used

- `ClothesShopChatbotDataset_augmented.csv` – preprocessed Q&A for chatbot training
- `styles.csv` – metadata for real-world fashion items (category, gender, name)
- ClothesShopChatbotDataset.csv

## 🛠️ Tech Stack
Category                       Tools Used

Programming                    Python 3.x

Notebook Support               JupyterLite

Frontend                       Streamlit

Data Handling                  Pandas

Dataset Storage                ClothesShopChatbotDataset_augmented.csv, styles.csv,ClothesShopChatbotDataset.csv

📝 **Data Handling**

-chatbot_dataset: Contains augmented customer queries with "Question", "Answer", and "Context" fields for common retail interactions.

-styles.csv: Filterable by gender, masterCategory, and productDisplayName. Used to recommend fashion items.

-Null Handling: Rows with missing essential fields are dropped using dropna().

-Style Sampling: Random top-5 matches are returned based on the inferred gender/category of query.

🚚 **Deployment Options**

✅ Streamlit Cloud
✅ GitHub Pages (JupyterLite notebooks)

🌐 **User Interface**

Built using Streamlit
Friendly and responsive interface for user interactions

📘 **JupyterLite Notebook**

A JupyterLite notebook is included to demonstrate data exploration, cleaning, and logic testing.
Useful for students, researchers, and developers reviewing logic before deployment.

📝 **How It Works**

User inputs a question via the Streamlit interface.
The app checks for a matching question in ClothesShopChatbotDataset_augmented.csv.
If matched → Returns the appropriate response.
If not matched → Analyzes query for gender/category → Samples matching products from styles.csv.

🔧 **Setup Instructions**

cd fashion-assistant-chatbot
📦 **Install Dependencies**
pip install -r requirements.txt
▶️ **Run the Streamlit App**
streamlit run streamlit_app.py
