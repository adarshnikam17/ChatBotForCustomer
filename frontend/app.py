import os
import streamlit as st
import sqlite3
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Create OpenAI client (NEW WAY)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------- FAQ Database ----------
def find_answer(query):
    try:
        conn = sqlite3.connect("../backend/faqs.db")

        cursor = conn.cursor()

        cursor.execute(
            "SELECT answer FROM faqs WHERE question LIKE ?",
            ('%' + query + '%',)
        )

        result = cursor.fetchone()
        conn.close()

        return result[0] if result else None

    except sqlite3.OperationalError as e:
        return f"Database error: {e}"


# ---------- AI Response ----------
def ai_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # ✅ modern model
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error fetching AI response: {e}"


# ---------- Streamlit UI ----------
st.title("AI-Powered Customer Support Chatbot")

user_input = st.text_input("You:")

if user_input:

    # First check FAQ database
    response = find_answer(user_input)

    if response:
        st.write(f"Bot: {response}")
    else:
        ai_bot_response = ai_response(user_input)
        st.write(f"Bot: {ai_bot_response}")
