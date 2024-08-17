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

# Halaman 1
if st.session_state.page == 1:
    st.title("✨ Halaman Pertama ✨")
    st.write("selamat bertemu 19 Agustus ke-22 di bumi. selamat ulang tahun, Difa Fadli R. selamat bertambah tua. selamat menjadi om-om sesungguhnya.")
    st.write("iya, ini dibuat khusus buat ultah kamu hehe jangan geli plis ak gatau harus ngucapin kek gimana lagi.")
    st.write("ak dah bikin beberapa fitur, klik lezgo buat coba-coba.")

    # Tombol untuk memunculkan pop-up
    if st.button("lezgo"):
            st.write("play duluuu biar ga sepi")
            st.audio(audio_bytes, format='audio/mp3')
              
        with st.expander("survey about ur 21"):
            
            # question 1
            st.write("rate how was ur 21")
            st.slider('1-10', min_value=0, max_value=10)

            # question 2
            st.write("fav memory di 21")
            st.text_input('jawab di sini')
                    
            # question 3
            st.write("worst memory di 21")
            st.text_input('jawab di sini')

            # question 
            st.write("tempat terbaik yang dikunjungi di 21")
            st.text_input('jawab di sini')

            # question 
            st.write("makanan terenak yang dicoba di 21")
            st.text_input('jawab di sini')

            # question 
            st.write("film terbagus yang ditonton di 21")
            st.text_input('jawab di sini')

            # question 
            st.write("project terkeren yang dibuat di 21")
            st.text_input('jawab di sini')
            
            # question 
            st.write("janji jangan pernah nyerah di 22")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("ya"):
                    st.success("yey.")
            with col2:
                if st.button("engga"):
                    st.warning("aslinya ini iya cuma tulisannya engga.") 
                    
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
