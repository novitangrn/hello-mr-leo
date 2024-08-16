import streamlit as st

# Inisialisasi session state untuk melacak halaman
if 'page' not in st.session_state:
    st.session_state.page = 1

# Fungsi untuk navigasi halaman
def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

# Tambahkan audio yang bisa diputar manual
audio_file = open('backsound.mp3', 'rb')  # Pastikan file audio berada di direktori yang benar
audio_bytes = audio_file.read()

# Menampilkan audio control di setiap halaman
st.audio(audio_bytes, format='audio/mp3')

# Halaman 1
if st.session_state.page == 1:
    st.title("Halaman 1")
    st.write("Ini adalah konten halaman 1.")
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
