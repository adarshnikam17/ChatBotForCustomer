import openai
import sqlite3
from dotenv import load_dotenv


import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY') 

def create_table():
    conn = sqlite3.connect('faqs.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS faqs (
        question TEXT,
        answer TEXT
    )
    ''')
    cursor.execute('''
    INSERT INTO faqs (question, answer)
    VALUES 
    ("What are your operating hours?", "We are open from 9 AM to 9 PM daily."),
    ("How can I track my order?", "You can track your order using the tracking link sent via email.")
    ''')
    conn.commit()
    conn.close()

def find_answer(query):
    conn = sqlite3.connect('faqs.db')
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM faqs WHERE question LIKE ?", ('%' + query + '%',))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def ai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

create_table()

user_query = "How can I track my order?"

response = find_answer(user_query)
if response:
    print(f"Database answer: {response}")
else:
    
    print(f"AI answer: {ai_response(user_query)}")
