# app.py
import streamlit as st
import pandas as pd
from fuzzywuzzy import process
from chat_api import call_deepseek

@st.cache_data
def load_data():
    return pd.read_excel("mecsu_data.xlsx")  # đổi đúng tên file của bạn

df = load_data()

st.title("🔎 Chatbot Tìm Kiếm Sản Phẩm - Mecsu.vn")
user_input = st.text_input("Bạn cần tìm sản phẩm gì?")

if user_input:
    with st.spinner("💬 Đang xử lý câu hỏi..."):
        prompt = f"""Bạn là một trợ lý tìm kiếm sản phẩm. Hãy chuyển câu sau thành dạng chuẩn chỉ gồm những thông số quan trọng: chất liệu, tiêu chuẩn DIN, kích thước. Nếu câu không đầy đủ hoặc không khớp, hãy trả về "Không tìm thấy".Câu gốc: '{user_input}'
                """

        #prompt = f"Hãy chuẩn hóa hoặc sửa lại mô tả sau để dễ tìm kiếm sản phẩm, chỉ cần cho tôi mã sản phẩm và link sản phẩm: '{user_input}'"
        normalized = call_deepseek(prompt)

    st.write(f"🧠 Hiểu là: **{normalized}**")

    descriptions = df["Description"].tolist()
    matches = process.extract(normalized, descriptions, limit=5)

    st.subheader("📦 Kết quả gợi ý:")
    for desc, score in matches:
        item = df[df["Description"] == desc].iloc[0]
        st.markdown(f"""
        **{item['Description']}**  
        🔹 Mã hãng: `{item['Part Number']}`  
        🔗 [Xem chi tiết trên Mecsu.vn]({item['Link']})  
        ---
        """)
