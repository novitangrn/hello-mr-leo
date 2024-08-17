import streamlit as st

# Inisialisasi session state untuk melacak halaman
if 'page' not in st.session_state:
    st.session_state.page = 1

# Fungsi untuk navigasi halaman
def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

# Halaman 1
if st.session_state.page == 1:
    st.title("✨ Halaman Pertama ✨")
    st.write("selamat bertemu Agustus ke-22 di bumi. selamat ulang tahun, Difa Fadli R. selamat bertambah tua. selamat menjadi om-om sesungguhnya. iya, ini dibuat khusus buat ultah kamu hehe jangan geli plis ak gatau harus ngucapin kek gimana lagi.")

    # Tombol untuk memunculkan pop-up
    if st.button("Tampilkan Pertanyaan"):
        with st.expander("Question Box"):
            st.write("Apakah Anda ingin melanjutkan?")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Yes"):
                    st.success("Anda memilih Yes.")
            with col2:
                if st.button("No"):
                    st.warning("Anda memilih No, tindakan tidak akan dilanjutkan.")

    if st.button("Next"):
        next_page()

# Halaman 2
elif st.session_state.page == 2:
    st.title("Halaman 2")
    st.write("Ini adalah konten halaman 2.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Previous"):
            prev_page()
    with col2:
        if st.button("Next"):
            next_page()

# Halaman 3
elif st.session_state.page == 3:
    st.title("Halaman 3")
    st.write("Ini adalah konten halaman 3.")
    if st.button("Previous"):
        prev_page()
