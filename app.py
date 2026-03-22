import streamlit as st
import google.generativeai as genai

# 1. Mengambil API Key dari pengaturan rahasia Streamlit
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# 2. Mengatur tampilan halaman web
st.set_page_config(page_title="Asisten Cerdas", page_icon="🤖")
st.title("🤖 Asisten Analisis & Laporan")
st.write("Masukkan pertanyaan atau data yang ingin dianalisis di bawah ini.")

# 3. Memilih model AI (Gemini 1.5 Pro/Flash)
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. Membuat kolom input untuk user
user_input = st.text_area("Apa yang bisa saya bantu hari ini?")

# 5. Logika ketika tombol ditekan
if st.button("Kirim"):
    if user_input:
        with st.spinner("Sedang memproses..."):
            # Mengirim prompt ke Gemini
            response = model.generate_content(user_input)
            # Menampilkan hasil di layar
            st.success("Selesai!")
            st.write(response.text)
    else:
        st.warning("Silakan masukkan teks terlebih dahulu.")
