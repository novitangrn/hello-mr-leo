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
            with st.form(key='survey_form'):
                # Pertanyaan 1
                rate_21 = st.slider('rate how was ur 21', min_value=0, max_value=10)
                
                # Pertanyaan 2
                fav_memory = st.text_input('fav memory di 21', key='fav_memory')
        
                # Pertanyaan 3
                worst_memory = st.text_input('worst memory di 21', key='worst_memory')
        
                # Pertanyaan 4
                best_place = st.text_input('tempat terbaik yang dikunjungi di 21', key='best_place')
        
                # Pertanyaan 5
                best_food = st.text_input('makanan terenak yang dicoba di 21', key='best_food')
        
                # Pertanyaan 6
                best_movie = st.text_input('film terbagus yang ditonton di 21', key='best_movie')
        
                # Pertanyaan 7
                coolest_project = st.text_input('project terkeren yang dibuat di 21', key='coolest_project')
        
                submit_button = st.button(label='Submit')
    
                if submit_button:
                    st.success("u did well di 21!")
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
