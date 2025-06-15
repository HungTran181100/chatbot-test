import os
from dotenv import load_dotenv
import googlegenerativeai as genai
import streamlit as st

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

model = genai.GenerativeModel(
    "gemini-2.0-flash-lite",
    system_instruction=""" 
                Bạn là một giáo viên dạy lập trình ngôn ngữ python. 
                1. Hãy hướng dẫn học sinh giải các bài tập liên quan đến lập trình thật chi tiết.
                2. Hỗ trợ những câu hỏi lý thuyết.
                3. Không hỗ trợ những chức năng không liên quan đến lập trình

""",
)

input_text = st.text_input("Nhập nội dung của bạn tại đây", key="input")
submit = st.button("Gửi")

response = None
if input_text and submit:
    response = model.generate_content(input_text)

mess = st.empty()

if response:
    mess.markdown(response.text)
