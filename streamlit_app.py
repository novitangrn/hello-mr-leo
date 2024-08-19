import streamlit as st
from pymongo import MongoClient
import pandas as pd

mongo_url = "mongodb+srv://august:august08@august.b3qut.mongodb.net/"
PAGE_ICON = "assets/Letter.png"

st.set_page_config(
    page_title="Three Days Notice",
    page_icon=PAGE_ICON,
)

if 'page' not in st.session_state:
    st.session_state.page = 1

if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

@st.cache_resource
def get_mongo_client():
    return MongoClient(mongo_url)

def save_to_mongo_text(data):
    try:
        client = get_mongo_client()
        db = client['Agustus']
        collection = db['page_1']
        result = collection.insert_one(data)
    except Exception as e:
        st.error("kok error si bjir............")

def save_to_mongo_cb(data):
    try:
        client = get_mongo_client()
        db = client['Agustus']
        collection = db['page_2']
        result = collection.insert_one(data)
    except Exception as e:
        st.error("kok error si bjir............")

def next_page():
    st.session_state.page += 1
    #st.experimental_rerun()

def prev_page():
    st.session_state.page -= 1
    #st.experimental_rerun()

audio_file = open('assets/backsound.mp3', 'rb')

# Page 1
if st.session_state.page == 1:
    st.title("3-Days Notice Letter")
    st.divider()
    surat = """
    <p>  <p?

    <p style="text-align: right;">Surabaya, 19 Agustus 2024</p>

    <p>Yth. Sdr. Difa Fadli R.,</p>

    <p>Saya menulis surat ini untuk memberitahukan keputusan saya untuk mengundurkan diri dari situasi apapun itu yang melibatkan saya dengan Saudara. Saya memberikan pemberitahuan ini 3 hari sebelumnya, dan hari terakhir saya akan jatuh pada Kamis, 22 Agustus 2024. Keputusan ini diambil karena alasan pribadi yang tidak bisa dihindari.</p>

    <p>Saya sangat bersyukur atas pengalaman dan kesempatan yang telah diberikan. Saya ingin menyampaikan rasa terima kasih kepada Saudara atas segala cerita, insight, dan dukungan yang telah saya terima.</p>

    <p>Sekali lagi, saya mengucapkan terima kasih atas kesempatan yang tidak pernah diprediksi akan saya alami ini. Saya berharap baik saya maupun Saudara dapat sama-sama melanjutkan cerita di jalan masng-masing.</p>

    <p style="margin-top: 50px;">Hormat saya,</p>
    <p>Novita A.</p>
    """
    st.markdown(surat, unsafe_allow_html=True)
    st.divider()
    
    st.info("always click one of these buttons twice.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Acc"):
            next_page()
    with col2:
        if st.button("Reject"):
            next_page()

# Page 2
elif st.session_state.page == 2:
    st.title("whatever your choice, it's always should be 'acc'")
    st.write("jco identik sama resign kan ya, pol? sorry karena ngajuin ini di ultah kamu... kamu selamat ulang tahun ya.. panjang umur dan sehat selalu. all the best buat kamu.")
    st.write("aku banyak banget salah ke kamu. suka tiba-tiba bt, suka tiba-tiba ilang, suka tiba-tiba ga jelas. problematik banget, maaf udah banyak ngerepotin dan jadi beban kamu.")
    st.write("makasih banyak pol buat semuanyaaa. ak seneng bisa kenal kamu.")
    
    if st.button("Back"):
        next_page()
    
# Page 3
elif st.session_state.page == 3:
    st.title("HAIIII! IH JUJUR INI JELEK BGT DRAMANYA BJRLAAAA😩")
    st.write("ini boongan ya pooooyyy. enak aja resign resign HAHAHAHAA.")
    st.image("assets/img10.jpg",  use_column_width="auto")

    st.info("btw disclaimer, slalu klik dua kali di tombol apapun yaw..")
    if st.button("Next"):
        next_page()

# Page 4
elif st.session_state.page == 4:
    st.title("✨ Halaman Pertama ✨")
    st.image("assets/img11.jpeg",  use_column_width="auto")
    st.write("selamat bertemu 19 Agustus ke-22 kamu di bumi! selamat ulang tahun, Difa Fadli. selamat bertambah tua. selamat menjadi om-om sesungguhnya.")
    st.write("iya, ini dibuat khusus buat ultah kamu hehe jangan kaget jangan geli plis ak gatau harus ngucapin kek gimana lagi.")
    st.write("btw ak dah bikin beberapa fitur, tapi agaknya nyita waktu. jadi buka pas lagi luang aja yaaa. nihhh klik lezgo buat coba-coba.")

    if st.button("lezgo"):
        next_page()

# Page 5
elif st.session_state.page == 5:
    #st.write("play duluuu biar ga sepi")
    #st.audio(audio_file, format='audio/mp3')

    st.title("survey dikit tentang 21 kamu yaw 🤩")

    with st.expander("open me open me 🌟"):
        with st.form(key='survey_form'):

            rate_21 = st.slider('rate how was ur 21', min_value=0, max_value=10)
            
            st.info("yang ini beres ngetik jangan langsung klik enter ya.")

            worst_memory = st.text_input('worst memory di 21', key='fav_memory')
            fav_memory = st.text_input('fav memory di 21', key='worst_memory')
            best_place = st.text_input('tempat terbaik yang dikunjungi di 21', key='best_place')
            best_food = st.text_input('makanan terenak yang dicoba di 21', key='best_food')
            best_movie = st.text_input('film terbagus yang ditonton di 21', key='best_movie')
            coolest_project = st.text_input('project terkeren yang dibuat di 21', key='coolest_project')
            st.info("pertanyaan-pertanyaan di atas buat callback memorimu di 21. terusin yang baik-baik, yang jelek-jelek lupain yaaa 🙇‍♀️")
    
            submit_button = st.form_submit_button(label='udah?  ayo next.')

            if submit_button:
                # Mengatur data yang akan disimpan
                data = {
                    "rate_21": rate_21,
                    "fav_memory": fav_memory,
                    "worst_memory": worst_memory,
                    "best_place": best_place,
                    "best_food": best_food,
                    "best_movie": best_movie,
                    "coolest_project": coolest_project
                }
                save_to_mongo_text(data)
                st.session_state.form_submitted = True
                next_page()

# Page 6
elif st.session_state.page == 6:
    st.title("yey you did well di 21, poypoy!")
    st.write("tau ga siiii aku seneng banget ketemu dan kenal sama kamu. inget ga aku pernah bilang kalo ak sempet nge-drop komen di reels instagram tentang seseorang?")
    
    with st.expander("kubocorin sekarang deh..."):
        st.image("assets/img1.jpeg", caption="belum lewat yaaa wkwk" , use_column_width="auto")
        st.write("bukti:")
        st.image("assets/img2.jpeg", caption="bukti 1", use_column_width="auto")
        st.image("assets/img3.jpeg", caption="bukti 2", use_column_width="auto")
        st.write("jujur ini bikin malu HAHAHA😭😢 plis kamu jangan ngerasa gimana gimana yaaa ini cuma fyi sama funfact aja.")
        
    col1, col2 = st.columns(2)
    with col1:
        if st.button("next, next!"):
            next_page()

# Page 7
elif st.session_state.page == 7:
    st.title("ngomong-ngomong soal funfact...")
    st.write("mr. ISTJ Leo, nih ak kumpulin sedikit funfact soal ur MBTI dan ur zodiac.")

    with st.expander("ISTJ funfacts"):
        st.markdown("ISTJ, Si Inspektur adalah singkatan dari **introvert**, **sensing**, **thinking**, dan **judging**. Secara umum, ISTJ adalah seorang pribadi cukup individualis, namun memiliki tujuan yang jelas. Sangat rasional dalam mengambil setiap keputusan sehari-hari. ISTJ melakukan tindakan dengan hati - hati dan terencana ")
        st.image("assets/img13.jpg", caption="ISTJ inside vs outside" , use_column_width="auto")
        st.image("assets/img14.jpeg", caption="INTJ ISTJ comparison", use_column_width="auto")
        st.image("assets/img17.jpeg", caption="ISTJ bingo, kekny kamu nyoret semuanya.", use_column_width="auto")
        st.markdown('''
        - ISTJ adalah seorang **pribadi yang bertanggung jawab.** Ia melaksanakan setiap tugasnya dengan sangat teliti, terstruktur, dan 100% tuntas.
        - ISTJ adalah **kepribadian yang memiliki ketelitian terbaik dibandingkan siapapun.**
        - ISTJ adalah **seorang perencana handal, senang menjalani hidup secara terencana.**
        - ISTJ memiliki **karakter yang sangat tenang**. Dalam situasi di mana semua orang merasa panik, ISTJ adalah orang yang paling tenang dan tetap bisa berpikir secara dingin.
        - ISTJ tidak terlalu suka hal-hal berbau perasaan. Ia tidak terlalu peka dengan perasaan dirinya sendiri maupun orang lain di sekitarnya. Itulah mengapa ia memiliki kesan yang cukup dingin.
        ''')
        

    with st.expander("leo funfacts"):
        st.image("assets/leo.jpeg", caption="rasi leo" , use_column_width="auto")
        st.image("assets/img19.jpg", caption="regulus comparing to the sun" , use_column_width="auto")

        st.write("some facts astronomically n astrologically:")
        st.markdown('''
        - Dalam mitologi Yunani, Leo sering dikaitkan dengan Singa Nemea, makhluk yang dikalahkan oleh pahlawan legendaris Heracles (Hercules)."
        - Regulus (Alpha Leonis), bintang paling terang di Leo, adalah salah satu dari empat Bintang Kerajaan Persia dan sering disebut "Jantung Singa."
        - Bentuk konstelasi Leo menyerupai surai singa yang megah, dengan Regulus sebagai jantung atau kepala.
        - Menurut astrologi, orang yang lahir di bawah tanda zodiak Leo diyakini memiliki sifat-sifat seperti percaya diri, kesetiaan, dan rasa percaya diri yang kuat.
        - Leo sering dikaitkan dengan "Spring Equinox," yang menandai dimulainya musim semi.
        - Leo merupakan salah satu dari sedikit rasi bintang yang benar-benar menyerupai namanya, yakni singa.
        - Hujan meteor Leo Quadrantid terjadi pada bulan Januari dan berasosiasi dengan konstelasi Leo.
        - Regulus adalah salah satu bintang paling terang di langit malam, dan namanya berasal dari kata Latin "regulus," yang berarti "raja kecil."
        - Regulus adalah bintang yang berotasi cepat, dengan periode rotasi hanya 15,9 jam.
        ''')

    with st.expander("19th august funfacts"):
        st.image("assets/2002.png", caption="moon phase birthday tahun 2002" , use_column_width="auto")
        st.divider()
        st.image("assets/2024.jpeg", caption="moon phase birthday tahun 2024" , use_column_width="auto")
        st.divider()
        st.image("assets/img20.jpg", caption="2002 fashion" , use_column_width="auto")
        st.divider()
        st.image("assets/img21.jpg", caption="2002 cars" , use_column_width="auto")
        st.divider()
        st.image("assets/img23.jpeg", caption="august 2002 cartoon" , use_column_width="auto")
        st.divider()
        st.image("assets/img22.jpeg", caption="19th august 2002 fact" , use_column_width="auto")
        st.divider()
        st.image("assets/img24.jpeg", caption="18th august 2002 stats" , use_column_width="auto")
        st.write("")


    st.write("tapi kalo kamu uninterested dengan funfact yang beberapa bukan fact banget, u can skip by clicking this next button 👇")
    if st.button("next!"):
        next_page()

# Page 8
elif st.session_state.page == 8:
    st.title("ak juga udah ngumpulin quote of the day alias kata-kata hari ini buat jadi motivasi sewaktu-waktu.")
    
    st.divider()
    tabs = st.tabs(
        ["qotd #1️⃣", "qotd #2️⃣", "qotd #3️⃣", "qotd #4️⃣", "qotd #5️⃣", "qotd #6️⃣", "qotd #7️⃣", "qotd #8️⃣", 
        "qotd #9️⃣", "qotd #1️⃣0️⃣", "qotd #1️⃣1️⃣", "qotd #1️⃣2️⃣", "qotd #1️⃣3️⃣", "qotd #1️⃣4️⃣", "qotd #1️⃣5️⃣"]
    )

    # Menampilkan gambar pada masing-masing tab
    for i, tab in enumerate(tabs, start=1):
        with tab:
            st.image(f"assets/qotd{i}.jpg", caption=f"qotd{i}", use_column_width="auto")

    st.divider()

    st.write("dan lagi, kalo kamu uninterested dengan qotd yang sesungguhnya sangat amat memotivasi ini, u still can skip by clicking one of these buttons.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("balik ke funfact?"):
            prev_page()
    with col2:
        if st.button("next, next!"):
            next_page()


# Page 9
elif st.session_state.page == 9:
    st.title("sekali lagi.. happy birthday, dipoooy! 🤍")
    st.info("skarang masuk ke section wishes ya...")
    st.markdown("versi singkatnya, **i wish you all the best, poy.**")
    st.write("versi detailnya, banyak.")

    wishes = [
        "sehat selalu",
        "serta mulia",
        "panjang umurnya",
        "dikasih rezeki tumpah-tumpah",
        "lancar segala urusannya",
        "bahagia selalu",
        "dihilangkan semua sakitnya",
        "bisa upgrade diri jadi yang lebih baik",
        "selalu diberi petunjuk sama yang Di Atas",
        "dikasih semangat buat konsisten di semua hal-hal baik",
        "selalu beruntung dan berhasil di segala hal yang kamu inginkan",
        "senantiasa dikelilingi orang baik (termasuk ak hehe😎)",
        "(isi sendiri doa sendiri aku aamiin-in)"
    ]

    # Membuat string Markdown dari list
    bullet_wishes = "\n".join([f"* {wish}" for wish in wishes])

    # Menampilkan poin-poin dengan st.markdown
    st.markdown(bullet_wishes)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("balik ke qotd?"):
            prev_page()
    with col2:
        if st.button("next aja"):
            next_page()


# Page 10
elif st.session_state.page == 10:
    st.title("arsip  arsip📂📁")
    st.write("mau throwback ngga? dulu kt knapa seru bgt bjir ak ketawa sendiri pas bikin page iniii. ni yaaa ak ingetin how it started + captionnyaaa HAHAHA")

    with st.expander("once upon a time cenah 🧩"):
        st.image("assets/img4.jpeg", caption="subuh-subuh bgt ya HAHA. ini masih biasa aja." , use_column_width="auto")
        st.divider()
        st.image("assets/img5.jpeg", caption="ini dah mulai awkwkardsksk cos u tidak bertanya balik🫵🫵 tiba-tiba keluar sabda cewe tidak pernah salah😩" , use_column_width="auto")
        st.divider()
        st.image("assets/img6.jpeg", caption="sepik pertama kamu niii kulempar balik ke depanmu" , use_column_width="auto")
        st.divider()
        st.image("assets/img7.jpeg", caption="mutualan tapi kamunya agak mbulet" , use_column_width="auto")
        st.divider()
        st.image("assets/img8.jpeg", caption="bagian terlucu versi akkk" , use_column_width="auto")
        st.divider()

    with st.expander("honest thought (tapi agak cringe pls gausa dibuka gapapa)"):
        st.write("aksjdjkadjakjd poy you're only 2 months old in my mind but you already can stand, walk, or even run in there. it's nice to meet outstanding baby like you. ive told you something that life is about give and take kan? but somehow i don't mind if i only do give when it comes to you??? 🙇‍♀️🙇‍♀️")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("balik ke qotd?"):
            prev_page()
    with col2:
        if st.button("next aja"):
            next_page()


# Page 11
elif st.session_state.page == 11:
    st.title("💡 hasil dan pembahasan sejak how it started 💡")
    st.divider()
    st.write("setelah hampir 2 bulan yang ternyata tidak eperti ekpektasi awal itu, didapatkan similarities antara ak sm kamu sebagaimana tabel berikut (sesuai janji)")

    st.subheader("similarities")
    sims = [
        "2002",
        "mother tongue ngapak",
        "anak pertama",
        "adik cewe baru masuk SMP",
        "gasuka pedes",
        "prefer tempat-tempat dingin",
        "MBTI IxTJ",
        "interest ke coding dan IT",
        "golongan darah O",
        "tim matcha",
        "suka donat",
        "pelupa"
    ]

    df = pd.DataFrame({
        "no": range(1, len(sims) + 1),  
        "kesamaan": sims                    
    })

    st.write(df.to_html(index=False), unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        table {
            width: 100%;
        }
        th, td {
            text-align: center;
        }
        th:first-child, td:first-child {
            width: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.divider()

    st.write("seiring dengan berjalannya waktu, terdapat hal-hal yang mungkin bisa terjadi. untuk mengantisipasi munculnya situasi yang tidak diinginkan, berikut merupakan beberapa hal yang sekiranya dapat disepakati oleh kedua pihak.")
    st.write("pihak pertama ak aja de, kamu pihak kedua ya wkwk. kedua pihak buat sebutan pihak pertama dan kedua secara bersamaan.")
    st.subheader("memorandum of understanding (MoU)")
    st.write("")

    items = [
        "konsep relasi kedua pihak adalah berteman level ttms😩✊",
        "kedua pihak sepakat untuk saling mengerti jika pihak lain tidak bisa membalas pesan karena alasan pribadi.",
        "selama di level ttms, kedua pihak diharapkan untuk life update setidaknya setiap hari.",
        "resign adalah bentuk pengunduran diri dari rutinitas sehari-hari antara kedua pihak, menurunkan level ttms menjadi regular friendship.",
        "SOP resign adalah dengan aturan 3 days notice dengan hitungan hari kerja.",
        "jika kedua pihak resmi resign, semua jenis obrolan dan informasi masing-masing dari kedua pihak berhenti di kedua pihak.",
        "tidak ada konsep unfriend dan blokir memblokir. Hubungan kedua pihak harus diselesaikan dengan cara yang baik.",
        "observasi adalah bentuk pencarian pengganti pihak pertama oleh pihak kedua dan sebaliknya.",
        "kedua pihak diperbolehkan melakukan observasi dan memiliki kewajiban untuk terbuka pada pihak lainnya.",
        "jika observasi telah terbukti berhasil, hal-hal yang mengenai pemindahan kekuasaan dan lain-lain diselenggarakan dengan cara seksama dan dalam tempo yang sesingkat-singkatnya."
    ]
    
    st.info("centang box untuk menyetujui.")

    responses = {}
    for i, item in enumerate(items):
        responses[f'item_{i+1}'] = st.checkbox(item)

    # buttons
    if st.button("acc acc!"):
        try:
            save_to_mongo_cb(responses)
            st.session_state['next_step'] = True
            st.success("okayyy! skarang next lagi, atau mau nambah pasal?")
        except Exception as e:
            st.error("bjir kok error si............")

    if 'next_step' in st.session_state and st.session_state['next_step']:
        if st.button("next lagi."):
            next_page()

    if st.button("mau nambah/revisi pasal."):
        st.session_state['add_pasal'] = True

    if 'add_pasal' in st.session_state and st.session_state['add_pasal']:
        pasal_baru = st.text_area('silakan ketikkan seluruh pasal yang mau ditambahkan/direvisi di sini.')
        if st.button('send and next!'):
            try:
                new_data = {"pasal_baru": pasal_baru}
                save_to_mongo_text(new_data)
                st.success("oke udah kekirim. hasil keluar setelah review pihak lain ya hehehe")
                next_page()
            except Exception as e:
                st.error("bjir kok error si............")

# Page 12
elif st.session_state.page == 12:
    st.title("last page🎇🎆✨🎉🎊")
    st.subheader("yey sampe di halaman terakhir.")
    st.write("cape ngga? wkwk niatnya tu mau 3 page aja tapi ternyata kurang hehe. ini page trakhir bgt kok.")

    st.divider()

    with st.expander("final questions❓⏬🔽"):
        harapan = st.text_area('harapan di umur 22 (boleh ketik sini, boleh dalam hati aja)')
        st.write("")
        rate_2 = st.slider('kabar rate 7/10 kemarin plis😥', min_value=0, max_value=10)
        st.write("")
        kesan_pesan = st.text_area('kesan pesan (boleh ketik sini, boleh dalam hati aja)')

        if st.button("submit. iya ril ini terakhir."):

            data_3 = {
                "harapan": harapan,
                "rate_2": rate_2,
                "kesan_pesan": kesan_pesan
            }
            save_to_mongo_text(data_3)
            st.success("wkwk yeyyy beneran dah selesai.")


    with st.expander("update 3 2 1"):
        st.image("assets/img9.jpeg", use_column_width="auto")

        larangan = [
            "tidur cukup yaaa, begadang terus engga baik...",
            "makan teratur, makan yang sehat sehat aja jugaa",
            "yang terakhir ini gapapa pake jangan hehe. jangan mendem semua masalah sendiri poy, im all ears kalo kamu butuh temen ceritaaa",
        ]

        perintah = [
            "jaga diri kamu wahai officially 22 y.o. grown up man. vitaminnya jangan lupaaa.",
            "segera lenyapkan dan move dari semua yang bikin kamu sakit. gigi bolong kamu contohnya."
        ]

        bullet_larangan = "\n".join([f"* {l}" for l in larangan])
        bullet_perintah = "\n".join([f"* {p}" for p in perintah])
        
        st.markdown("<h4 style='text-align: center;'>3 larangan</h4>", unsafe_allow_html=True)
        st.markdown("- ~~jangan observasi dulu~~")
        st.write("BECANDAAA. ngga ada larangan buat kamu poy. ini lebih ke saran???")  
        st.markdown(bullet_larangan)
        st.divider()

        st.markdown("<h4 style='text-align: center;'>2 permintaan</h4>", unsafe_allow_html=True)
        st.write("tetep sama:")
        st.markdown(bullet_perintah)
        st.divider()
        
        st.markdown("<h4 style='text-align: center;'>1 pesan</h4>", unsafe_allow_html=True)
        st.markdown("setop ngira ak pengin cepet-cepet resign ya dipoy. buka mata kepala sampe mata kaki kamuuu. kecuali kalo kamu emang mau begitu aku bisa fleksibel.")
    
    st.write("")
    st.write("")
    st.write("sumpah sekarang udah. semoga ga terlalu bikin pusing ya hehe.")
    st.write("sekali lagi selamat ulang tahun, dipoy sayang🤍")
    st.write("")
    st.write("")

    if st.button("finish🏁   kabarin kalo uda sampe akhir siniii."):
        wa_link = "https://wa.me/083166510535"
        st.write(f"<meta http-equiv='refresh' content='0; url={wa_link}'>", unsafe_allow_html=True)
