import streamlit as st

st.set_page_config(page_title="Web Arwani", page_icon="🚀")

st.title("Web Streamlit Pertama 🚀")
st.write("Halo! Aplikasi ini berhasil jalan dan siap online.")

nama = st.text_input("Ketik nama kamu:")
if st.button("Sapa Saya"):
    st.success(f"Mantap {nama or 'Arwani'}, web kamu sudah jalan!")