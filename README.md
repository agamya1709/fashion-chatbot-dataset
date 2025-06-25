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

  
