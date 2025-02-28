import streamlit as st
import requests

# ✅ Update your FastAPI backend URL
API_URL = "https://prompt-refiner-api.onrender.com/refine-prompt/"

# ✅ Streamlit UI
st.title("🚀 Prompt Refiner")
st.write("Enter a raw prompt and get a refined version.")

# 📌 User Input
raw_prompt = st.text_area("Enter your raw prompt:", "")

tone = st.selectbox("Choose a tone:", ["neutral", "formal", "friendly"])
output_format = st.selectbox("Choose output format:", ["plain_text", "markdown"])

if st.button("Refine Prompt ✨"):
    if raw_prompt.strip() == "":
        st.error("❌ Please enter a prompt!")
    else:
        try:
            # 🔹 Send data to FastAPI
            payload = {
                "raw_prompt": raw_prompt,
                "tone": tone,
                "output_format": output_format
            }

            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                refined_text = response.json().get("refined_prompt", "⚠️ No response received.")
                st.success("✅ Refined Prompt:")
                st.write(refined_text)
            else:
                st.error(f"❌ Server Error: {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Connection Error: {e}")
