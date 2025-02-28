🚀 Streamlit Prompt Refiner

📝 Overview
This is a **Streamlit** web app that connects with a **FastAPI** backend to refine user prompts using Google's Gemini API.

🔹 Features
- Users enter a **raw prompt**.
- Choose **tone** (neutral, formal, friendly).
- Select **output format** (plain text, markdown).
- Calls **FastAPI backend** to refine the prompt.
- Displays the **refined prompt**.

 🛠️ Setup Instructions

 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/your-streamlit-repo.git
cd your-streamlit-repo

2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

3️⃣ Run the Streamlit App
bash
Copy
Edit
streamlit run app.py

🚀 Deployment (Optional)
To deploy this Streamlit app on Render, follow these steps:

Create a new Web Service on Render.
Select Streamlit runtime.
Set the Start Command:
bash
Copy
Edit
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
Deploy and get your public Streamlit URL! 🎉

