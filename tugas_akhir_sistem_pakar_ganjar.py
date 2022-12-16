import streamlit as st
from PIL import Image

def update_multiselect_style():
    st.markdown(
        """
        <style>
            .stMultiSelect [data-baseweb="tag"] {
                height: fit-content;
            }
            .stMultiSelect [data-baseweb="tag"] span[title] {
                white-space: normal; max-width: 100%; overflow-wrap: anywhere;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    
st.title('Sistem Pakar Penentu Universitas Tujuan untuk Melanjutkan Pendidikan S2 yang Memiliki Program Studi AI atau Ilmu Komputer')

   
# Merepresentasikan basis aturan dan kasus dalam mode frame ke dalam tipe data dinamis yang menggunakan key

data = {
        'k1':{'IPK':3, 'IELTS Writing':7, 'IELTS Speaking':7, 'IELTS Reading': 7, 'IELTS Listening': 7, 'IELTS Overall': 7, 'iBT Overall': 100, 'D. Overall': 110, 'Pref':{'Banyak Orang Indonesia', 'Bahasa Lokal (Indonesia/Inggris)'}, 'Tujuan': 'Luar Negeri', 'solusi':'CMU', 'program': 'AI', 'gelar': 'Master of Science in Artificial Intelligence and Innovation'},
    
        'k2':{'IPK':3.7, 'IELTS Writing':6.5, 'IELTS Speaking':6.5, 'IELTS Reading': 6.5, 'IELTS Listening': 6.5, 'IELTS Overall': 7, 'iBT Writing': 22, 'iBT Speaking': 22, 'iBT Overall': 93 , 'Pref':{'Bahasa Lokal (Indonesia/Inggris)'}, 'Tujuan': 'Luar Negeri', 'solusi':'Toronto', 'program': "AI", 'gelar': 'Master of Science in Applied Computing (MScAC)'},
    
        'k3':{'IPK':3, 'IELTS Writing':8, 'IELTS Speaking':6, 'IELTS Reading': 7, 'IELTS Listening': 7, 'IELTS Overall': 7,'Pref':{'Gratis Pendaftaran', 'Kota Pelajar', 'Banyak Orang Indonesia', 'Bahasa Lokal (Indonesia/Inggris)', 'Negara Ramah Muslim'}, 'Tujuan': 'Luar Negeri', 'solusi':'Edinburgh'},
    
        'k4':{'IPK':3.7, 'IELTS Writing':7, 'IELTS Speaking':7, 'IELTS Reading': 7, 'IELTS Listening': 7, 'IELTS Overall': 7.5,'Pref':{'Kota Pelajar', 'Banyak Orang Indonesia', 'Bahasa Lokal (Indonesia/Inggris)', 'Negara Ramah Muslim'}, 'Tujuan': 'Luar Negeri', 'solusi':'Oxford'},
    
        'k5':{'IPK':3.3, 'IELTS Writing':6.5, 'IELTS Speaking':6.5,'IELTS Reading': 6.5, 'IELTS Listening': 6.5, 'IELTS Overall': 6.5,'Pref':{'Banyak Orang Indonesia', 'Bahasa Lokal (Indonesia/Inggris)'}, 'Tujuan': 'Luar Negeri', 'solusi':'NTU'},
    
        'k6':{'IPK':3, 'IELTS Writing':7, 'IELTS Speaking':7, 'IELTS Reading': 7, 'IELTS Listening': 7, 'IELTS Overall': 7.5,'Pref':{'Gratis Pendaftaran', 'Banyak Orang Indonesia', 'Bahasa Lokal (Indonesia/Inggris)'}, 'Tujuan': 'Luar Negeri', 'solusi':'Yale univ'},
    
        'k7':{'IPK':3.4, 'IELTS Writing':6.5, 'IELTS Speaking':6.5, 'IELTS Reading': 6.5, 'IELTS Listening': 6.5, 'IELTS Overall': 6.5,'Pref':{'Gratis Pendaftaran'}, 'Tujuan': 'Luar Negeri', 'solusi':'Copenhagen University'},
    
        'k8':{'IPK':3.2, 'IELTS Overall': 6.5, 'iBT Overall': 90, 'Pref':{'Gratis Pendaftaran', 'Negara Ramah Muslim', 'Termasuk Beasiswa'}, 'Tujuan': 'Luar Negeri', 'solusi':'MBZUAI', 'program':'AI - Machine Learning, Computer Vision, & Natural Language Processing', 'gelar': 'Master of Science'},
    
        'k9':{'IPK':3.2, 'IELTS Writing':5.5, 'IELTS Speaking':5.5, 'IELTS Reading': 5.5, 'IELTS Listening': 5.5, 'IELTS Overall': 6.5, 'iBT Writing': 17 , 'iBT Speaking': 17, 'iBT Reading': 17, 'iBT Listening': 17, 'iBT Overall': 79, 'Pref':{'Gratis Pendaftaran', 'Banyak Orang Indonesia', 'Negara Ramah Muslim', 'Termasuk Beasiswa'}, 'Tujuan': 'Luar Negeri', 'solusi':'KAUST', 'program':'CS', 'gelar': 'Master of Science'},
    
        'k10':{'IPK':2.2, 'IELTS Writing':6, 'IELTS Speaking':6, 'IELTS Reading': 6, 'IELTS Listening': 6, 'IELTS Overall': 6.5, 'iBT Writing': 21 , 'iBT Speaking': 18, 'iBT Reading': 13, 'iBT Listening': 12, 'iBT Overall': 79, 'Pref':{'Kota Pelajar', 'Banyak Orang Indonesia', 'Bahasa Lokal (Indonesia/Inggris)'}, 'Tujuan': 'Luar Negeri', 'solusi':'RMIT', 'program': 'AI', 'gelar': 'Master of Artificial Intelligence'},
    
        'k11':{'IPK':2.5, 'IELTS Writing':6, 'IELTS Speaking':6, 'IELTS Reading': 6, 'IELTS Listening': 6, 'IELTS Overall': 6, 'iBT Overall': 71, 'Pref':{'Gratis Pendaftaran', 'Banyak Orang Indonesia', 'Negara Ramah Muslim', 'Termasuk Beasiswa'}, 'Tujuan': 'Luar Negeri', 'solusi':'KFUPM', 'program': '1 year MX Program in AI ', 'gelar': 'Master of Science'},
    
        'k12':{'IPK':3, 'IELTS Writing':6.5, 'IELTS Speaking':6.5, 'IELTS Reading': 6.5, 'IELTS Listening': 6.5, 'IELTS Overall': 6.5, 'iBT Writing': 24 , 'iBT Speaking': 21, 'iBT Reading': 21, 'iBT Listening': 21, 'iBT Overall': 90, 'Pref':{'Gratis Pendaftaran', 'Kota Pelajar', 'Tanpa Wawancara', 'Tanpa Surat Rekomendasi', 'Banyak Orang Indonesia'}, 'Tujuan': 'Luar Negeri', 'solusi':'Groningen', 'program': 'AI', 'gelar': 'MSc in Artificial Intelligence'},
    
        'k13':{'IPK':2.5, 'TPA':450, 'ITP Overall': 400, 'IELTS Overall': 4, 'iBT Overall': 31, 'Pref':{'Kota Pelajar', 'Banyak Orang Indonesia','Bahasa Lokal (Indonesia/Inggris)', 'Negara Ramah Muslim'}, 'Tujuan': 'Dalam Negeri', 'solusi':'UGM', 'program': 'AI', 'gelar': 'Master of Computer Science in Artificial Intelligence (MCs.(AI))'},
    
        'k14':{'IPK':2.5, 'TPA': 475, 'ITP Overall': 475, 'IELTS Overall': 5, 'iBT Overall': 56,'Pref':{'Banyak Orang Indonesia', 'Bahasa Lokal (Indonesia/Inggris)', 'Negara Ramah Muslim'}, 'Tujuan': 'Dalam Negeri', 'solusi':'ITB'}
       }

#Streamlit
#Tab
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Perhitungan Pakar 🧑‍🏫", "log ranking 📊 ", "log persyaratan minimum 🎓", "log database matching 💯", "all databases 📚"])

# Layout

#Nama dan IPK
with tab1:
    cl0, cl00 = st.columns(2) 

    #Tujuan dalam/luar negeri?
    st.write("Pilih salah satu tujuan universitas ✈️🌎")
    cl0a, cl0b = st.columns(2)

    st.markdown("------")
    st.text("Masukkan nilai Bahasa Inggris-mu")
    tabi1, tabi2, tabi3, tabi4 = st.tabs(['IELTS', 'iBT', 'Duolingo', 'ITP'])

    st.markdown("------")
    st.text("Masukkan nilai akademik dari TPA/GRE-mu")
    taba1, taba2 = st.tabs(["TPA", "GRE"])

    kol1, kol2 = st.columns(2)
    kol0, kol00, kol000= st.columns([1, 10, 1])
    kol3, kol4, kol5 = st.columns(3)
    kol4a, kol4b, kol4c = st.columns([1,10,1])
    
with tab2:
    kol6, kol7 = st.columns(2)

with tab3:
    kol8, kol9 = st.columns(2)

with tab4:
    kol10, kol11 = st.columns(2)

with tab5:
    st.success("Seluruh Database")
    st.write("based on university AI and Computer Science Rank", data)



# Mode number
with cl0:
    nama = st.text_input("Nama Lengkap 🤩", placeholder="isi nama kamu")
with cl00:
    ipk = st.number_input("Masukkan Nilai IPK S1 (1-4) 🎓", step = 0.1, min_value = .0, max_value = 4.)
    
with cl0a: 
    dn = st.checkbox('Dalam Negeri')
    if dn:
        st.write("Wajib isi ITP dan TPA 🙏😊")

with cl0b:
    ln = st.checkbox('Luar Negeri')
    if ln:
        st.write("Silakan pilih salah satu sertifikasi bahasa inggris kecuali ITP, misalnya IELTS ✍️")

with tabi1:
    # IELTS
    # cle1a, cle1b = st.columns(2)
    ielts = st.checkbox("Gunakan IELTS")
    
    cle2, cle3, cle4, cle5, cle6= st.columns(5)
    
    if ielts:
        with cle2:
            ielts_w = st.number_input("IELTS Writing", step = 0.1, min_value = .0, max_value = 9.)
        with cle3:
            ielts_s = st.number_input("IELTS Speaking", step = 0.1, min_value = .0, max_value = 9.)
        with cle4:
            ielts_r = st.number_input("IELTS Reading", step = 0.1, min_value = .0, max_value = 9.)
        with cle5:
            ielts_l = st.number_input("IELTS Listening", step = 0.1, min_value = .0, max_value = 9.)
        with cle6:
            ielts_o = st.number_input("IELTS Overall", step = 0.1, min_value = .0, max_value = 9.);

with tabi2:
    #iBt
    # cli1a, cle1b = st.columns(2)
    ibt = st.checkbox("Gunakan iBT")
    
    cli2, cli3, cli4, cli5, cli6 = st.columns(5)
    
    if ibt:
        with cli2:
            ibt_w = st.number_input("iBT Writing", step = 0.1, min_value = .0, max_value = 30.)
        with cli3:
            ibt_s = st.number_input("iBT Speaking", step = 0.1, min_value = .0, max_value = 30.)
        with cli4:
            ibt_r = st.number_input("iBT Reading", step = 0.1, min_value = .0, max_value = 30.)
        with cli5:
            ibt_l = st.number_input("iBT Listening", step = 0.1, min_value = .0, max_value = 30.)
        with cli6:
            ibt_o = st.number_input("iBT Overall", step = 0.1, min_value = .0, max_value = 120.);

with tabi3: 
    #duolingo
    #cld1a, cle1b = st.columns(2)
    dlg = st.checkbox("Gunakan Duolingo")
    
    cld2, cld3, cld4, cld5, cld6 = st.columns(5)
    
    if dlg:
        with cld2:
            dlg_l = st.number_input("D. Literacy", step = 0.1, min_value = .0, max_value = 40.0)
        with cld3:
            dlg_cv = st.number_input("D. Conversation", step = 0.1, min_value = .0, max_value = 40.0)
        with cld4:
            dlg_cp = st.number_input("D. Comprehension", step = 0.1, min_value = .0, max_value = 40.0)
        with cld5:
            dlg_p = st.number_input("D. Production", step = 0.1, min_value = .0, max_value = 40.0)
        with cld6:
            dlg_o = st.number_input("D. Overall", step = 0.1, min_value = .0, max_value = 140.0);

with tabi4:  
    #ITP
    #kli1a, kli1b = st.columns(2)
    itp = st.checkbox("Gunakan ITP")
        
    kli2, kli3, kli4, kli5 = st.columns(4)
    
    if itp:
        with kli2:
            itp_l = st.number_input("ITP Listening", step = 0.1, min_value = .0, max_value = 200.0)
        with kli3:
            itp_s = st.number_input("ITP Structure", step = 0.1, min_value = .0, max_value = 200.0)
        with kli4:
            itp_r = st.number_input("ITP Reading", step = 0.1, min_value = None, max_value = 200.0)
        with kli5:
            itp_o = st.number_input("ITP Overall", step = 0.1, min_value = 310.0, max_value = 677.0);        

with taba1:
    n_tpa = st.checkbox("Isi TPA")
    if n_tpa:
        tpa = st.number_input("Masukkan nilai (200-800)", step = 0.1, min_value = 200.0, max_value = 800.0)


with taba2:
    gre = st.checkbox("Isi GRE")
    
    klgre1, klgre2, klgre3 = st.columns(3)
    
    if gre:
        with klgre1:
            gre_vr = st.number_input("GRE Verbal Reasoning", step = 0.1, min_value = .0, max_value = 170.0)
        with klgre2:
            gre_qr = st.number_input("GRE Quantitative Reasoning", step = 0.1, min_value = .0, max_value = 170.0)
        with klgre3:
            gre_aw = st.number_input("GRE Analytical Writing", step = 0.1, min_value = .0, max_value = 6.0)

        
update_multiselect_style()

with kol1:
    pref_list = st.multiselect("Masukkan Preferensi kamu", ['Gratis Pendaftaran', 'Tanpa Wawancara', 'Tanpa Surat Rekomendasi', 'Kota Pelajar', 'Banyak Orang Indonesia', 'Bahasa Lokal (Indonesia/Inggris)', 'Negara Ramah Muslim', 'Termasuk Beasiswa'])
#st.write("Ini", preferensi)
    mode_pref = st.selectbox("Pilih mode preferensi universitas tujuan", ("AND", "OR"))
    hitung = st.button("Hitung Prediksi")

if hitung:
    kasus = {}

    # Mode number
    kasus['IPK'] = ipk
    
    if dn and ln:
        kasus['Tujuan'] = "Dalam Negeri dan Luar Negeri"
    elif dn:
        kasus['Tujuan'] = "Dalam Negeri"
    elif ln:
        kasus['Tujuan'] = "Luar Negeri"
    
    if ielts:
        kasus['IELTS Writing'] = ielts_w
        kasus['IELTS Speaking'] = ielts_s
        kasus['IELTS Reading'] = ielts_r
        kasus['IELTS Listening'] = ielts_l
        kasus['IELTS Overall'] = ielts_o
    
    if ibt:
        kasus['iBT Writing'] = ibt_w
        kasus['iBT Speaking'] = ibt_s
        kasus['iBT Reading'] = ibt_r
        kasus['iBT Listening'] = ibt_l
        kasus['iBT Overall'] = ibt_o
    
    if dlg:
        kasus['D. Literacy'] = dlg_l
        kasus['D. Conversation'] = dlg_cv
        kasus['D. Comprehension'] = dlg_cp
        kasus['D. Production'] = dlg_p
        kasus['D. Overall'] = dlg_o
    
    if itp:
        kasus['ITP Listening'] = itp_l
        kasus['ITP Structure'] = itp_s
        kasus['ITP Reading'] = itp_r
        kasus['ITP Overall'] = itp_o
    
    if n_tpa:
        kasus['TPA'] = tpa
    
    if gre:
        kasus['GRE Verbal Reasoning'] = gre_vr
        kasus['GRE Quantitative Reasoning'] = gre_qr
        kasus['GRE Analytical Writing'] = gre_aw
    
    preferensi = dict.fromkeys(pref_list)  #udah jadi dictionary tapi ada value = None
    dict_preferensi = {x for x in preferensi} #membuat dict tanpa value, key only
    kasus["Pref"] = dict_preferensi
    
    if mode_pref == "AND":
    
        # Pencocokkan persis pada database

        ada_data_pref = {}
        no_data_pref = {}

        for (key, value) in data.items():
            if kasus["Pref"] == value["Pref"]:
                ada_data_pref[key] = value
            else:
                no_data_pref[key] = value   

        ada_data = {}
        no_data = {}

        for (key, value) in ada_data_pref.items():
            if kasus["Tujuan"] == value["Tujuan"]:
                ada_data[key] = value
                st.write("Test", ada_data) #Check
            else:
                no_data[key] = value       

        if len(ada_data) != 0:

            ipk_req = []
            ket_ipk = []

            for vals in ada_data.values():
                nbx = 0
                nb = 0

                b = []

                if vals['IPK'] <= kasus['IPK']:
                    b.append("IPK Terpenuhi ✅")
                    nbx += 1
                else:
                    b.append("IPK Tidak terpenuhi ❌")
                nb += 1

                ket_ipk.append(b)
                ipk_req.append(nbx/nb)  

            # Inisiasi variabel req bertipe list untuk menyimpan nilai kesamaan requirements setiap kasus

            if ielts:
                #IELTS
                ielts_req = []
                ket_ielts = []

                # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
                for vals in ada_data.values():
                    nrx = 0
                    nr = 0

                    a = []

                    if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(vals):
                        if vals['IELTS Writing'] <= kasus['IELTS Writing']:
                            a.append("IELTS Writing Terpenuhi ✅")
                            nrx += 1
                        else:
                            a.append("Writing Tidak terpenuhi ❌")
                        nr += 1

                        if vals['IELTS Speaking'] <= kasus['IELTS Speaking']:
                            a.append("IELTS Speaking Terpenuhi ✅")
                            nrx += 1
                        else:
                            a.append("Speaking Tidak terpenuhi ❌")
                        nr += 1

                        if vals['IELTS Reading'] <= kasus['IELTS Reading']:
                            a.append("IELTS Reading Terpenuhi ✅")
                            nrx += 1
                        else:
                            a.append("Reading Tidak terpenuhi ❌")
                        nr += 1

                        if vals['IELTS Listening'] <= kasus['IELTS Listening']:
                            a.append("IELTS Listening Terpenuhi ✅")
                            nrx += 1
                        else:
                            a.append("Listening Tidak terpenuhi ❌")
                        nr += 1

                        if vals['IELTS Overall'] <= kasus['IELTS Overall']:
                            a.append("IELTS Overall Terpenuhi ✅")
                            nrx += 1
                        else:
                            a.append("IELTS Overall Tidak terpenuhi ❌")
                        nr += 1

                        ket_ielts.append(a) #pakai extend list_extend() bisa katanya
                        ielts_req.append(nrx/nr)

                    elif "IELTS Overall" in vals:
                        if vals['IELTS Overall'] <= kasus['IELTS Overall']:
                            a.append("IELTS Overall Terpenuhi ✅")
                            nrx += 1
                        else:
                            a.append("IELTS Overall Tidak terpenuhi ❌")
                        nr += 1

                        ket_ielts.append(a) #pakai extend list_extend() bisa katanya
                        ielts_req.append(nrx/nr)

            if ibt:
                #iBT
                ibt_req = []
                ket_ibt = []

                # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
                for vals in ada_data.values():
                    nrxi = 0
                    nri = 0

                    c = []

                    #iBT
                    if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(vals):
                        if vals['iBT Writing'] <= kasus['iBT Writing']:
                            c.append("iBT Writing Terpenuhi ✅")
                            nrxi += 1
                        else:
                            c.append("iBT Writing Tidak terpenuhi ❌")
                        nri += 1

                        if vals['iBT Speaking'] <= kasus['iBT Speaking']:
                            c.append("iBT Speaking Terpenuhi ✅")
                            nrxi += 1
                        else:
                            c.append("iBT Speaking Tidak terpenuhi ❌")
                        nri += 1

                        if vals['iBT Reading'] <= kasus['iBT Reading']:
                            c.append("iBT Reading Terpenuhi ✅")
                            nrxi += 1
                        else:
                            c.append("iBT Reading Tidak terpenuhi ❌")
                        nri += 1

                        if vals['iBT Listening'] <= kasus['iBT Listening']:
                            c.append("iBT Listening Terpenuhi ✅")
                            nrxi += 1
                        else:
                            c.append("iBT Listening Tidak terpenuhi ❌")
                        nri += 1

                        if vals['iBT Overall'] <= kasus['iBT Overall']:
                            c.append("iBT Overall Terpenuhi ✅")
                            nrxi += 1
                        else:
                            c.append("iBT Overall Tidak terpenuhi ❌")
                        nri += 1

                        ket_ibt.append(c) #pakai extend list_extend() bisa katanya
                        ibt_req.append(nrxi/nri)

                    elif "iBT Overall" in vals:
                        if vals['iBT Overall'] <= kasus['iBT Overall']:
                            c.append("iBT Overall Terpenuhi ✅")
                            nrxi += 1
                        else:
                            c.append("iBT Overall Tidak terpenuhi ❌")
                        nri += 1

                        ket_ibt.append(c) #pakai extend list_extend() bisa katanya
                        ibt_req.append(nrxi/nri)

            #Duolingo

            if dlg:
                dlg_req = []
                ket_dlg = []
                # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
                for vals in ada_data.values():
                    nrxd = 0
                    nrd = 0

                    d = []

                    if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(vals):
                        if vals['D. Literacy'] <= kasus['D. Literacy']:
                            d.append("D. Literacy Terpenuhi ✅")
                            nrxd += 1
                        else:
                            d.append("D. Literacy Tidak terpenuhi ❌")
                        nrd += 1

                        if vals['D. Conversation'] <= kasus['D. Conversation']:
                            d.append("D. Conversation Terpenuhi ✅")
                            nrxd += 1
                        else:
                            d.append("D. Conversation Tidak terpenuhi ❌")
                        nrd += 1

                        if vals['D. Comprehension'] <= kasus['D. Comprehension']:
                            d.append("D. Comprehension Terpenuhi ✅")
                            nrxd += 1
                        else:
                            d.append("D. Comprehension Tidak terpenuhi ❌")
                        nrd += 1

                        if vals['D. Production'] <= kasus['D. Production']:
                            d.append("D. Production Reading Terpenuhi ✅")
                            nrxd += 1
                        else:
                            d.append("D. Production Tidak terpenuhi ❌")
                        nrd += 1

                        if vals['D. Overall'] <= kasus['D. Overall']:
                            d.append("D. Overall Terpenuhi ✅")
                            nrxd += 1
                        else:
                            d.append("D. Overall Tidak terpenuhi ❌")
                        nrd += 1

                        ket_dlg.append(d) #pakai extend list_extend() bisa katanya
                        dlg_req.append(nrxd/nrd)

                    elif "D. Overall" in vals:
                        if vals['D. Overall'] <= kasus['D. Overall']:
                            d.append("D. Overall Terpenuhi ✅")
                            nrxd += 1
                        else:
                            d.append("D. Overall Tidak terpenuhi ❌")
                        nrd += 1

                        ket_dlg.append(d) #pakai extend list_extend() bisa katanya
                        dlg_req.append(nrxd/nrd)

            #ITP
            if itp:
                itp_req = []
                ket_itp = []

                # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
                for vals in ada_data.values():
                    nix = 0 
                    ni = 0

                    e = []

                    #ITP
                    if {"ITP Listening", "ITP Structure", "ITP Reading", "ITP Overall"}.issubset(vals):
                        if vals['ITP Listening'] <= kasus['ITP Listening']:
                            e.append("ITP Listening Terpenuhi ✅")
                            nix += 1
                        else:
                            e.append("ITP Listening Tidak terpenuhi ❌")
                        ni += 1

                        if vals['ITP Structure'] <= kasus['ITP Structure']:
                            e.append("ITP Structure Terpenuhi ✅")
                            nix += 1
                        else:
                            e.append("ITP Structure Tidak terpenuhi ❌")
                        ni += 1

                        if vals['ITP Reading'] <= kasus['ITP Reading']:
                            e.append("ITP Reading Terpenuhi ✅")
                            nix += 1
                        else:
                            e.append("ITP Reading Tidak terpenuhi ❌")
                        ni += 1

                        if vals['ITP Overall'] <= kasus['ITP Overall']:
                            e.append("ITP Overall Terpenuhi ✅")
                            nix += 1
                        else:
                            e.append("ITP Overall Tidak terpenuhi ❌")
                        ni += 1

                        ket_itp.append(e) #pakai extend list_extend() bisa katanya
                        itp_req.append(nix/ni)

                    elif "ITP Overall" in vals:
                        if vals['ITP Overall'] <= kasus['ITP Overall']:
                            e.append("ITP Overall Terpenuhi ✅")
                            nix += 1
                        else:
                            e.append("ITP Overall Tidak terpenuhi ❌")
                        ni += 1

                        ket_itp.append(e) #pakai extend list_extend() bisa katanya
                        itp_req.append(nix/ni)

            if n_tpa:

                #TPA

                tpa_req = []
                ket_tpa = []

                # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
                for vals in ada_data.values():
                    ntx = 0
                    nt = 0

                    f = []

                    #ITP

                    if vals['TPA'] <= kasus['TPA']:
                        f.append("TPA Terpenuhi ✅")
                        ntx += 1
                    else:
                        f.append("TPA Tidak terpenuhi ❌")
                    nt += 1

                    ket_tpa.append(f) #pakai extend list_extend() bisa katanya
                    tpa_req.append(ntx/nt)

            if gre:
                #GRE

                gre_req = []
                ket_gre = []

                # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
                for vals in ada_data.values():
                    ngx = 0
                    ng = 0

                    g = []

                    #GRE

                    if vals['GRE Verbal Reasoning'] <= kasus['GRE Verbal Reasoning']:
                        g.append("GRE Verbal Reasoning Terpenuhi ✅")
                        ngx += 1
                    else:
                        g.append("GRE Verbal Reasoning Tidak terpenuhi ❌")
                    ng += 1

                    if vals['GRE Quantitative Reasoning'] <= kasus['GRE Quantitative Reasoning']:
                        g.append("GRE Quantitative Reasoning Terpenuhi ✅")
                        ngx += 1
                    else:
                        g.append("GRE Quantitative Reasoning Tidak terpenuhi ❌")
                    ng += 1

                    if vals['GRE Analytical Writing'] <= kasus['GRE Analytical Writing']:
                        g.append("GRE Analytical Writing Terpenuhi ✅")
                        ngx += 1
                    else:
                        g.append("GRE Analytical Writing Tidak terpenuhi ❌")
                    ng += 1

                    ket_gre.append(g) #pakai extend list_extend() bisa katanya
                    gre_req.append(ngx/ng)

            #Pref

            # Inisiasi variabel t bertipe list untuk menyimpan nilai kesamaan setiap kasus
            pref = []

            # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
            if len(kasus["Pref"]) != 0:
                for vals in ada_data.values():
                    npx = 0
                    npx += len(kasus['Pref'].intersection(vals['Pref']))
                    np = len(vals['Pref'])
                    pref.append(npx/np)
            else:
                for vals in ada_data.values():
                    npx = 0
                    pref.append(npx)


            #Perhitungan similaritas total

            # Inisiasi variabel t bertipe list untuk menyimpan nilai kesamaan setiap kasus
            total_sim = []

            # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
            for vals in ada_data.values():
                nx = 0
                n = 0 #Gak jadi dipakai

                if vals['IPK'] <= kasus['IPK']:
                    nx += 1
                n += 1

                #IELTS
                if 'IELTS Writing' in kasus and 'IELTS Writing' in vals:
                    if vals['IELTS Writing'] <= kasus['IELTS Writing']:
                        nx += 1
                    n += 1

                if 'IELTS Speaking' in kasus and 'IELTS Speaking' in vals:
                    if vals['IELTS Speaking'] <= kasus['IELTS Speaking']:
                        nx += 1
                    n += 1

                if 'IELTS Reading' in kasus and 'IELTS Reading' in vals:
                    if vals['IELTS Reading'] <= kasus['IELTS Reading']:
                        nx += 1
                    n += 1

                if 'IELTS Listening' in kasus and 'IELTS Listening' in vals:
                    if vals['IELTS Listening'] <= kasus['IELTS Listening']:
                        nx += 1
                    n += 1

                if 'IELTS Overall' in kasus and 'IELTS Overall' in vals:
                    if vals['IELTS Overall'] <= kasus['IELTS Overall']:
                        nx += 1
                    n += 1

                #iBT
                if 'iBT Writing' in kasus and 'iBT Writing' in vals:
                    if vals['iBT Writing'] <= kasus['iBT Writing']:
                        nx += 1
                    n += 1

                if 'iBT Speaking' in kasus and 'iBT Speaking' in vals:
                    if vals['iBT Speaking'] <= kasus['iBT Speaking']:
                        nx += 1
                    n += 1

                if 'iBT Reading' in kasus and 'iBT Reading' in vals:
                    if vals['iBT Reading'] <= kasus['iBT Reading']:
                        nx += 1
                    n += 1

                if 'iBT Listening' in kasus and 'iBT Listening' in vals:
                    if vals['iBT Listening'] <= kasus['iBT Listening']:
                        nx += 1
                    n += 1

                if 'iBT Overall' in kasus and 'iBT Overall' in vals:
                    if vals['iBT Overall'] <= kasus['iBT Overall']:
                        nx += 1
                    n += 1

                #Duolingo
                if 'D. Literacy' in kasus and 'D. Literacy' in vals:
                    if vals['D. Literacy'] <= kasus['D. Literacy']:
                        nx += 1
                    n += 1

                if 'D. Conversation' in kasus and 'D. Conversation' in vals:
                    if vals['D. Conversation'] <= kasus['D. Conversation']:
                        nx += 1
                    n += 1

                if 'D. Comprehension' in kasus and 'D. Comprehension' in vals:
                    if vals['D. Comprehension'] <= kasus['D. Comprehension']:
                        nx += 1
                    n += 1

                if 'D. Production' in kasus and 'D. Production' in vals:
                    if vals['D. Production'] <= kasus['D. Production']:
                        nx += 1
                    n += 1

                if 'D. Overall' in kasus and 'D. Overall' in vals:
                    if vals['D. Overall'] <= kasus['D. Overall']:
                        nx += 1
                    n += 1            

                #ITP
                if 'ITP Listening' in kasus and 'ITP Listening' in vals:
                    if vals['ITP Listening'] <= kasus['ITP Listening']:
                        nx += 1
                    n += 1

                if 'ITP Structure' in kasus and 'ITP Structure' in vals:
                    if vals['ITP Structure'] <= kasus['ITP Structure']:
                        nx += 1
                    n += 1

                if 'ITP Reading' in kasus and 'ITP Reading' in vals:
                    if vals['ITP Reading'] <= kasus['ITP Reading']:
                        nx += 1
                    n += 1

                if 'ITP Overall' in kasus and 'ITP Overall' in vals:
                    if vals['ITP Overall'] <= kasus['ITP Overall']:
                        nx += 1
                    n += 1 


                #TPA
                if 'TPA' in kasus and 'TPA' in vals:
                    if vals['TPA'] <= kasus['TPA']:
                        nx += 1
                    n += 1

                #GRE

                if 'GRE Verbal Reasoning' in kasus and 'GRE Verbal Reasoning' in vals:
                    if vals['GRE Verbal Reasoning'] <= kasus['GRE Verbal Reasoning']:
                        nx += 1
                    n += 1

                if 'GRE Quantitative Reasoning' in kasus and 'GRE Quantitative Reasoning' in vals:
                    if vals['GRE Quantitative Reasoning'] <= kasus['GRE Quantitative Reasoning']:
                        nx += 1
                    n += 1

                if 'GRE Analytical Writing' in kasus and 'GRE Analytical Writing' in vals:
                    if vals['GRE Analytical Writing'] <= kasus['GRE Analytical Writing']:
                        nx += 1
                    n += 1

                nx += len(kasus['Pref'].intersection(vals['Pref']))
                n += (len(vals['Pref']))

                total_sim.append(nx/n)             

            solusi = []
            for sol in ada_data:
                solusi.append(data[sol]['solusi'])

            #Bahasa inggris lolos setidaknya di salah satu

            rank = {}
            # Lolos dan lolos persyaratan minimal

            if ielts and ibt and dlg and itp and n_tpa and gre:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for g in ada_data.keys():
                    rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, "iBT Terpenuhi (%)": ibt_req[i]*100, "Duolingo terpenuhi (%)": dlg_req[i]*100, "ITP terpenuhi (%)": itp_req[i], "TPA terpenuhi (%)": tpa_req[i]*100, "GRE terpenuhi (%)": gre_req[i]*100, 'solusi': solusi[i]} 
                    i += 1

            elif ielts and ibt and dlg and itp and n_tpa:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for g in ada_data.keys():
                    rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, "iBT Terpenuhi (%)": ibt_req[i]*100, "Duolingo terpenuhi (%)": dlg_req[i]*100, "ITP terpenuhi (%)": itp_req[i]*100, "TPA terpenuhi (%)": tpa_req[i]*100, 'solusi': solusi[i]} 
                    i += 1        

            elif ielts and ibt and dlg:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for g in ada_data.keys():
                    rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, "iBT Terpenuhi (%)": ibt_req[i]*100, "Duolingo terpenuhi (%)": dlg_req[i]*100, 'solusi': solusi[i]} 
                    i += 1        

            elif ielts and ibt:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for (g, gi) in ada_data.items():
                    if {"IELTS Overall", "iBT Overall"}.issubset(gi): 
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, "iBT Terpenuhi (%)": ibt_req[i]*100, 'solusi': solusi[i]} 
                    elif "IELTS Overall" in gi:
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, 'solusi': solusi[i]} 
                    elif "iBT Overall" in gi:
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, "iBT Terpenuhi (%)": ibt_req[i]*100, 'solusi': solusi[i]}                     
                        i += 1        

            elif ielts and dlg:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for g in ada_data.keys():
                    rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, "Duolingo terpenuhi (%)": dlg_req[i]*100, 'solusi': solusi[i]} 
                    i += 1        

            elif dlg and ibt:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for g in ada_data.keys():
                    rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, "iBT Terpenuhi (%)": ibt_req[i]*100, "Duolingo terpenuhi (%)": dlg_req[i]*100, 'solusi': solusi[i]} 
                    i += 1 

            elif itp and n_tpa:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for g in ada_data.keys():
                    rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, "ITP terpenuhi (%)": itp_req[i]*100, "TPA terpenuhi (%)": tpa_req[i]*100, 'solusi': solusi[i]} 
                    i += 1                        

            elif itp:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for (g, gi) in ada_data.items():
                    if "ITP Overall" in gi:
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, "ITP terpenuhi (%)": itp_req[i]*100, 'solusi': solusi[i]} 
                        i += 1 

            elif ielts:
                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for (g, gi) in ada_data.items():
                    if "IELTS Overall" in gi:         
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, 'solusi': solusi[i]} 
                        i += 1  

            elif ielts and n_tpa:
                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for (g, gi) in ada_data.items():
                    if "IELTS Overall" in gi:         
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, "TPA terpenuhi (%)": tpa_req[i]*100, 'solusi': solusi[i]} 
                        i += 1  

            elif ibt:
                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for (g,gi) in ada_data.items(): 
                    if "iBT Overall" in gi:
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, "iBT Terpenuhi (%)": ibt_req[i]*100, 'solusi': solusi[i]} 
                        i += 1  

            elif dlg:
                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for (g, gi) in ada_data.items():
                    if "D. Overall" in gi:
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, "Duolingo terpenuhi (%)": dlg_req[i]*100, 'solusi': solusi[i]}      
                        i += 1  

            #Pengurutan berdasarkan IPK Terpenuhi

            if rank == {}:
                with kol2:
                    st.write("Silakan isi nilai bahasa inggris terlebih dahulu")
            else:
                urut = dict(sorted(rank.items(), key= lambda x:x[1]['IPK terpenuhi (%)'], reverse = True))
                # Using keys() + list()
                # Getting first key in dictionary
                urut_pertama = list(urut.keys())[0] #Gak dipake lagi

                # Using values() + list()
                # Getting value in first key in dictionary
                nilai_urut_pertama = list(urut.values())[0] #Gak dipake lagi

                # Pengelompokkan list ipk terpenuhi

                ipk_lolos = {}
                ipk_kurang = {}

                for (key, value) in urut.items():
                    if value['IPK terpenuhi (%)'] == 100:
                        ipk_lolos[key] = value
                    else:
                        ipk_kurang[key] = value

                if len(ipk_lolos) != 0:
                    urut_pertama_ipk_lolos = list(ipk_lolos.keys())[0]
                    nilai_urut_pertama_ipk_lolos = list(ipk_lolos.values())[0]
                if len(ipk_kurang) != 0:
                    urut_pertama_ipk_kurang = list(ipk_kurang.keys())[0]
                    nilai_urut_pertama_ipk_kurang = list(ipk_kurang.values())[0]

                # Pengelompokkan list IELTS terpenuhi
                if ielts and("IELTS Overall" in ada_data[urut_pertama]):
                    ielts_lolos = {}
                    ielts_kurang = {}

                    for (key, value) in urut.items():
                        if value['IELTS terpenuhi (%)'] == 100:
                            ielts_lolos[key] = value
                        else:
                            ielts_kurang[key] = value

                    if len(ielts_lolos) != 0:
                        urut_pertama_ielts_lolos = list(ielts_lolos.keys())[0]
                        nilai_urut_pertama_ielts_lolos = list(ielts_lolos.values())[0]
                    if len(ielts_kurang) != 0:
                        urut_pertama_ielts_kurang = list(ielts_kurang.keys())[0]
                        nilai_urut_pertama_ielts_kurang = list(ielts_kurang.values())[0]

                # Pengelompokkan list iBT terpenuhi
                if ibt and ("iBT Overall" in ada_data[urut_pertama]):
                    ibt_lolos = {}
                    ibt_kurang = {}

                    for (key, value) in urut.items():
                        if value['iBT Terpenuhi (%)'] == 100:
                            ibt_lolos[key] = value
                        else:
                            ibt_kurang[key] = value

                    if len(ibt_lolos) != 0:
                        urut_pertama_ibt_lolos = list(ibt_lolos.keys())[0]
                        nilai_urut_pertama_ibt_lolos = list(ibt_lolos.values())[0]
                    if len(ibt_kurang) != 0:
                        urut_pertama_ibt_kurang = list(ibt_kurang.keys())[0]
                        nilai_urut_pertama_ibt_kurang = list(ibt_kurang.values())[0]

                # Pengelompokkan list Duolingo terpenuhi
                if dlg and ("Duolingo Overall" in ada_data[urut_pertama]):
                    dlg_lolos = {}
                    dlg_kurang = {}

                    for (key, value) in urut.items():
                        if value['Duolingo terpenuhi (%)'] == 100:
                            dlg_lolos[key] = value
                        else:
                            dlg_kurang[key] = value

                    if len(dlg_lolos) != 0:
                        urut_pertama_dlg_lolos = list(dlg_lolos.keys())[0]
                        nilai_urut_pertama_dlg_lolos = list(dlg_lolos.values())[0]
                    if len(dlg_kurang) != 0:
                        urut_pertama_dlg_kurang = list(dlg_kurang.keys())[0]
                        nilai_urut_pertama_dlg_kurang = list(dlg_kurang.values())[0]

                # Pengelompokkan list ITP terpenuhi
                if itp and ("ITP Overall" in ada_data[urut_pertama]):
                    itp_lolos = {}
                    itp_kurang = {}

                    for (key, value) in urut.items():
                        if value['ITP terpenuhi (%)'] == 100:
                            itp_lolos[key] = value
                        else:
                            itp_kurang[key] = value

                    if len(itp_lolos) != 0:
                        urut_pertama_itp_lolos = list(itp_lolos.keys())[0]
                        nilai_urut_pertama_itp_lolos = list(itp_lolos.values())[0]
                    if len(itp_kurang) != 0:
                        urut_pertama_itp_kurang = list(itp_kurang.keys())[0]
                        nilai_urut_pertama_itp_kurang = list(itp_kurang.values())[0]

                # Pengelompokkan list TPA terpenuhi
                if n_tpa and ("TPA" in ada_data[urut_pertama]):
                    tpa_lolos = {}
                    tpa_kurang = {}

                    for (key, value) in urut.items():
                        if value['TPA terpenuhi (%)'] == 100:
                            tpa_lolos[key] = value
                        else:
                            tpa_kurang[key] = value

                    if len(tpa_lolos) != 0:
                        urut_pertama_tpa_lolos = list(tpa_lolos.keys())[0]
                        nilai_urut_pertama_tpa_lolos = list(tpa_lolos.values())[0]
                    if len(tpa_kurang) != 0:
                        urut_pertama_tpa_kurang = list(tpa_kurang.keys())[0]
                        nilai_urut_pertama_tpa_kurang = list(tpa_kurang.values())[0]

                # Pengelompokkan list GRE terpenuhi
                if gre and ("GRE" in ada_data[urut_pertama]):
                    gre_lolos = {}
                    gre_kurang = {}

                    for (key, value) in urut.items():
                        if value['GRE terpenuhi (%)'] == 100:
                            gre_lolos[key] = value
                        else:
                            gre_kurang[key] = value

                    if len(gre_lolos) != 0:
                        urut_pertama_gre_lolos = list(gre_lolos.keys())[0]
                        nilai_urut_pertama_gre_lolos = list(gre_lolos.values())[0]
                    if len(gre_kurang) != 0:
                        urut_pertama_gre_kurang = list(gre_kurang.keys())[0]
                        nilai_urut_pertama_gre_kurang = list(gre_kurang.values())[0]


                # Pengelompokkan list Inggris terpenuhi

                eng_lolos = {}
                eng_kurang = {}

                for (key, value) in urut.items():
                    #IELTS, iBT, Duolingo, ITP
                    if {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)', 'ITP terpenuhi (%)'}.issubset(value):
                        if value['IELTS terpenuhi (%)'] == 100 or value['iBT Terpenuhi (%)'] == 100 or value['Duolingo terpenuhi (%)'] == 100 or value['ITP terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]

                    #IELTS, iBT, Duolingo
                    if {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['IELTS terpenuhi (%)'] == 100 or value['iBT Terpenuhi (%)'] == 100 or value['Duolingo terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]

                    #IELTS dan iBT
                    if {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)'}.issubset(value):
                        if value['IELTS terpenuhi (%)'] == 100 or value['iBT Terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]   

                    #IELTS dan Duolingo
                    if {'IELTS terpenuhi (%)', 'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['IELTS terpenuhi (%)'] == 100 or value['Duolingo terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]

                    #iBT dan Dulingo
                    if {'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['iBT Terpenuhi (%)'] == 100 or value['Duolingo terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]

                    #IELTS 
                    if {'IELTS terpenuhi (%)'}.issubset(value):
                        if value['IELTS terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]   

                    #iBT
                    if {'iBT Terpenuhi (%)'}.issubset(value):
                        if value['iBT Terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]   

                    #Dulingo
                    if {'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['Duolingo terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]

                    #ITP
                    if {'ITP terpenuhi (%)'}.issubset(value):
                        if value['ITP terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]
                #TPA diatas

                #GRE diatas

                # Pengelompokkan lolos dan tidak lolos requirement, sudah diurutkan

                lolos = {}
                tidak_lolos = {}

                for (key, value) in urut.items():

                    #IELTS, iBT, Duolingo, ITP, TPA, GRE  
                    if {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)', 'ITP terpenuhi (%)', 'TPA terpenuhi (%)', 'GRE terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)'] == 100 or value['iBT Terpenuhi (%)']  == 100 or value['Duolingo terpenuhi (%)']  == 100  or value['ITP terpenuhi (%)'] == 100) or value['TPA terpenuhi (%)'] == 100 or value['GRE terpenuhi (%)'] == 100:
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #IELTS, iBT, Duolingo, ITP , TPA           
                    elif {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)', 'ITP terpenuhi (%)', 'TPA terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)'] == 100 or value['iBT Terpenuhi (%)']  == 100 or value['Duolingo terpenuhi (%)']  == 100  or value['ITP terpenuhi (%)'] == 100 or value['TPA terpenuhi (%)'] == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #IELTS, iBT, Duolingo, ITP         
                    elif {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)', 'ITP terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)'] == 100 or value['iBT Terpenuhi (%)']  == 100 or value['Duolingo terpenuhi (%)']  == 100  or value['ITP terpenuhi (%)'] == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value                        

                    #IELTS, iBT, Duolingo                        
                    elif {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)']  == 100  or value['iBT Terpenuhi (%)']  == 100 or value['Duolingo terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #IELTS, iBT                      
                    elif {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)']  == 100  or value['iBT Terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #IELTS, Duolingo                        
                    elif {'IELTS terpenuhi (%)', 'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)']  == 100  or value['Duolingo terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #iBT, Duolingo                        
                    elif {'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['iBT Terpenuhi (%)']  == 100 or value['Duolingo terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #IELTS                  
                    elif {'IELTS terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #iBT                      
                    elif {'iBT Terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['iBT Terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #Duolingo                        
                    elif {'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['Duolingo terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #ITP, TPA                  
                    elif {'ITP terpenuhi (%)', 'TPA terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['ITP terpenuhi (%)']  == 100 and value['TPA terpenuhi (%)'] == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #ITP                        
                    elif {'ITP terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['ITP terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value


                    #IELTS, TPA                  
                    elif {'IELTS terpenuhi (%)', 'TPA terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)']  == 100 and value['TPA terpenuhi (%)'] == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #iBT, TPA

                    #Duolingo, TPA

                # Using keys() + list()
                # Getting first key in dictionary

                st.write("Lolos?", lolos)
                st.write("Gak lolos?", tidak_lolos)

                if len(lolos) != 0:
                    urut_pertama_lolos = list(lolos.keys())[0]
                    nilai_urut_pertama_lolos = list(lolos.values())[0]
                if len(tidak_lolos) != 0:
                    urut_pertama_tidak_lolos = list(tidak_lolos.keys())[0]
                    nilai_urut_pertama_tidak_lolos = list(tidak_lolos.values())[0]

                # list Muhasabah ipk tiap univ
                muhasabah_ipk = {}

                j = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for g in ada_data.keys():
                    muhasabah_ipk[g] = ket_ipk[j]
                    j += 1

                #List muhasabah ielts tiap univ

                if ielts and ("IELTS Overall" in ada_data[urut_pertama]):
                    muhasabah_ielts = {}

                    ie = 0
                    for t in ada_data.keys():
                        muhasabah_ielts[t] = ket_ielts[ie]
                        ie += 1

                #List muhasabah iBT tiap univ
                if ibt and ("iBT Overall" in ada_data[urut_pertama]):
                    muhasabah_ibt = {}

                    ib = 0
                    for u in ada_data.keys():
                        muhasabah_ibt[u] = ket_ibt[ib]
                        ib += 1

                #List muhasabah duolingo tiap univ
                if dlg and ("Duolingo Overall" in ada_data[urut_pertama]):
                    muhasabah_duolingo = {}

                    dl = 0
                    for v in ada_data.keys():
                        muhasabah_duolingo[v] = ket_duolingo[dl]
                        dl += 1

                #List muhasabah ITP tiap univ     
                if itp and ("ITP Overall" in ada_data[urut_pertama]):
                    muhasabah_itp = {}

                    it = 0
                    for (w, wi) in ada_data.items():
                        if "ITP Overall" in wi:
                            muhasabah_itp[w] = ket_itp[it]
                            it += 1

                #List muhasabah TPA tiap univ                
                if n_tpa and ("TPA" in ada_data[urut_pertama]):
                    muhasabah_tpa = {}

                    tp = 0
                    for x in ada_data.keys():
                        muhasabah_tpa[x] = ket_tpa[tp]
                        tp += 1

                if gre and ("GRE" in ada_data[urut_pertama]):
                    #List muhasabah GRE tiap univ
                    muhasabah_gre = {}

                    gr = 0
                    for y in ada_data.keys():
                        muhasabah_gre[y] = ket_gre[gr]
                        gr += 1

                with kol00:
                    st.success("Evaluasi Similaritas Kasus Baru dengan database")
    ## 1.IPK Kurang!!
                    if len(ipk_lolos) == 0:
                        st.write("IPK kamu kurang, Silakan coba mode preferensi OR")
                        with kol4b:
                            st.success(f"Kondisi {nama}")
                            st.write("IPK = ", kasus['IPK'])

                            if ielts:
                                if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(kasus):
                                    st.write("IELTS Writing =", kasus['IELTS Writing'])
                                    st.write("IELTS Speaking =", kasus['IELTS Speaking'])
                                    st.write("IELTS Reading =", kasus['IELTS Reading'])
                                    st.write("IELTS Listening =", kasus['IELTS Listening'])
                                    st.write("IELTS Overall =", kasus['IELTS Overall'])
                                elif "IELTS Overall" in kasus:
                                    st.write("IELTS Overall =", kasus['IELTS Overall'])

                            if "Tujuan" in kasus:
                                st.write("Tujuan =", kasus['Tujuan'])

                            if ibt:
                                if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(kasus):
                                    st.write("iBT Writing =", kasus["iBT Writing"])
                                    st.write("iBT Speaking =", kasus["iBT Speaking"])
                                    st.write("iBT Reading =", kasus["iBT Reading"])
                                    st.write("iBT Listening =", kasus["iBT Listening"])
                                    st.write("iBT Overall =", kasus["iBT Overall"])
                                elif "iBT Overall" in kasus:
                                    st.write("iBT Overall =", kasus["iBT Overall"])

                            if dlg:
                                if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(kasus):
                                    st.write("D. Literacy =", kasus["D. Literacy"])
                                    st.write("D. Conversation =", kasus["D. Conversation"])
                                    st.write("D. Comprehension =", kasus["D. Comprehension"])
                                    st.write("D. Production =", kasus["D. Production"])
                                    st.write("D. Overall =", kasus["D. Overall"])
                                elif "D. Overall" in kasus:
                                    st.write("D. Overall =", kasus["D. Overall"])

                            if itp:
                                if "ITP Overall" in kasus:
                                    st.write("ITP Listening =", kasus["ITP Listening"])
                                    st.write("ITP Structure =", kasus["ITP Structure"])
                                    st.write("ITP Reading =", kasus["ITP Reading"])
                                    st.write("ITP Overall =", kasus["ITP Overall"])

                            if n_tpa:
                                if "TPA" in kasus:
                                    st.write("TPA =", kasus["TPA"])

                            if gre:
                                if "GRE Verbal Reasoning" in kasus:
                                    st.write("GRE Verbal Reasoning =", kasus["GRE Verbal Reasoning"])
                                    st.write("GRE Quantitative Reasoning =", kasus["GRE Quantitative Reasoning"])
                                    st.write("GRE Analytical Writing =", kasus["GRE Analytical Writing"])

                            #if "Gratis Pendaftaran" in kasus['Pref']:
                            st.write("Preferensi User =", kasus['Pref'])    


                        # Ini untuk yg OR nanti
                        #with kol3:
                         #   st.success(f"Syarat masuk {data[urut_pertama_ipk_lolos]['solusi']}")
                          #  st.write("IPK Minimum :", data[urut_pertama_ipk_lolos]['IPK'])
                           # st.write("IELTS Writing Minimum :", data[urut_pertama_ipk_lolos]["IELTS Writing"])
                            #st.write("IELTS Speaking Minimum :", data[urut_pertama_ipk_lolos]["IELTS Speaking"])
                            #st.write("IELTS Reading Minimum :", data[urut_pertama_ipk_lolos]["IELTS Reading"])
                            #st.write("IELTS Listening Minimum :", data[urut_pertama_ipk_lolos]["IELTS Listening"])
                            #st.write("IELTS Overall Minimum :", data[urut_pertama_ipk_lolos]["IELTS Overall"])
                            #st.write(f"Preferensi yang ada di {data[urut_pertama_ipk_lolos]['solusi']}", data[urut_pertama]['Pref'])

                        #with kol5:
                         #   st.success("Evaluasi Diri")
                          #  st.write(muhasabah[urut_pertama_ipk_lolos][0])
                           # st.write(muhasabah[urut_pertama_ipk_lolos][1])
                           # st.write(muhasabah[urut_pertama_ipk_lolos][2])
                           # st.write(muhasabah[urut_pertama_ipk_lolos][3])
                           # st.write(muhasabah[urut_pertama_ipk_lolos][4])
                           # st.write(muhasabah[urut_pertama_ipk_lolos][5])     

    ## 2. Lolos persyaratan minimum kampus

                    elif len(lolos) != 0:
                        st.write(f"Alhamdulillah semua persyaratan minimum kampus {nilai_urut_pertama_lolos['solusi']} telah kamu penuhi, berikut perbandingannya")

                        with kol3:
                            st.success(f"Syarat masuk {data[urut_pertama_lolos]['solusi']}")
                            st.write("IPK Minimum :", data[urut_pertama_lolos]['IPK'])
                            #IELTS
                            if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(data[urut_pertama_lolos]):  
                                st.write("IELTS Writing Minimum :", data[urut_pertama_lolos]["IELTS Writing"])
                                st.write("IELTS Speaking Minimum :", data[urut_pertama_lolos]["IELTS Speaking"])
                                st.write("IELTS Reading Minimum :", data[urut_pertama_lolos]["IELTS Reading"])
                                st.write("IELTS Listening Minimum :", data[urut_pertama_lolos]["IELTS Listening"])
                                st.write("IELTS Overall Minimum :", data[urut_pertama_lolos]["IELTS Overall"])

                            elif "IELTS Overall" in data[urut_pertama_lolos]:
                                st.write("IELTS Overall Minimum :", data[urut_pertama_lolos]["IELTS Overall"])

                            #iBT    
                            if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(data[urut_pertama_lolos]):  
                                st.write("iBT Writing Minimum :", data[urut_pertama_lolos]["iBT Writing"])
                                st.write("iBT Speaking Minimum :", data[urut_pertama_lolos]["iBT Speaking"])
                                st.write("iBT Reading Minimum :", data[urut_pertama_lolos]["iBT Reading"])
                                st.write("iBT Listening Minimum :", data[urut_pertama_lolos]["iBT Listening"])
                                st.write("iBT Overall Minimum :", data[urut_pertama_lolos]["iBT Overall"])

                            elif "iBT Overall" in data[urut_pertama_lolos]:
                                st.write("iBT Overall Minimum :", data[urut_pertama_lolos]["iBT Overall"])

                            #Duolingo    
                            if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(data[urut_pertama_lolos]):  
                                st.write("D. Literacy Minimum :", data[urut_pertama_lolos]["D. Literacy"])
                                st.write("D. Conversation Minimum :", data[urut_pertama_lolos]["D. Conversation"])
                                st.write("D. Comprehension Minimum :", data[urut_pertama_lolos]["D. Comprehension"])
                                st.write("D. Production Minimum :", data[urut_pertama_lolos]["D. Production"])
                                st.write("D. Overall Minimum :", data[urut_pertama_lolos]["D. Overall"])

                            elif "D. Overall" in data[urut_pertama_lolos]:
                                st.write("D. Overall Minimum :", data[urut_pertama_lolos]["D. Overall"])

                            #ITP    
                            if "ITP Overall" in data[urut_pertama_lolos]:  
                                st.write("ITP Overall Minimum :", data[urut_pertama_lolos]["ITP Overall"])

                            #TPA
                            if "TPA" in ada_data[urut_pertama]:
                                if len(tpa_lolos) != 0:
                                    if "TPA" in data[urut_pertama_lolos]:  
                                        st.write("TPA Minimum :", data[urut_pertama_lolos]["TPA"])

                            #GRE    
                            if {"GRE Verbal Reasoning", "GRE Quantitative Reasoning", "GRE Analytical"}.issubset(data[urut_pertama_lolos]):  
                                st.write("GRE Verbal Reasoning Minimum :", data[urut_pertama_lolos]["GRE Verbal Reasoning"])
                                st.write("GRE Quantitative Reasoning :", data[urut_pertama_lolos]["GRE Quantitative Reasoning"])
                                st.write("GRE Analytical Minimum :", data[urut_pertama_lolos]["GRE Analytical"])

                            st.write(f"Preferensi yang ada di {data[urut_pertama_lolos]['solusi']}", data[urut_pertama]['Pref'])                             

                        with kol4:
                            st.success(f"Kondisi {nama}")
                            st.write("IPK = ", kasus['IPK'])

                            if ielts:
                                st.write("IELTS Writing =", kasus['IELTS Writing'])
                                st.write("IELTS Speaking =", kasus['IELTS Speaking'])
                                st.write("IELTS Reading =", kasus['IELTS Reading'])
                                st.write("IELTS Listening =", kasus['IELTS Listening'])
                                st.write("IELTS Overall =", kasus['IELTS Overall'])

                            if ibt:
                                st.write("iBT Writing =", kasus['iBT Writing'])
                                st.write("iBT Speaking =", kasus['iBT Speaking'])
                                st.write("iBT Reading =", kasus['iBT Reading'])
                                st.write("iBT Listening =", kasus['iBT Listening'])
                                st.write("iBT Overall =", kasus['iBT Overall'])                        
                            if dlg:
                                st.write("Duolingo Literacy =", kasus['D. Literacy'])
                                st.write("Duoling Conversation =", kasus['D. Conversation'])
                                st.write("Duolingo Comprehension =", kasus['D. Comprehension'])
                                st.write("Duolingo Production =", kasus['D. Production'])
                                st.write("Duolingo Overall =", kasus['D. Overall'])  

                            if itp:
                                st.write("ITP Listening =", kasus['ITP Listening'])
                                st.write("ITP Structure =", kasus['ITP Structure'])
                                st.write("ITP Reading =", kasus['ITP Reading'])
                                st.write("ITP Overall =", kasus['ITP Overall'])                         
                            if n_tpa:
                                st.write("TPA =", kasus['TPA'])   

                            if gre:
                                st.write("GRE Verbal Reasoning =", kasus['GRE Verbal Reasoning'])
                                st.write("GRE Quantitative Reasoning =", kasus['GRE Quantitative Reasoning'])
                                st.write("GRE Analytical Writing =", kasus['GRE Analytical Writing'])

                            st.write("Preferensi User =", kasus['Pref'])

                        with kol5:
                            st.success("Evaluasi Diri")
                            st.write(muhasabah_ipk[urut_pertama_eng_lolos][0])

                            if ielts and ("IELTS Overall" in ada_data[urut_pertama]):
                                if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(data[urut_pertama_lolos]):  #Cek
                                    st.write(muhasabah_ielts[urut_pertama_ielts_lolos][0])
                                    st.write(muhasabah_ielts[urut_pertama_ielts_lolos][1])
                                    st.write(muhasabah_ielts[urut_pertama_ielts_lolos][2])
                                    st.write(muhasabah_ielts[urut_pertama_ielts_lolos][3])
                                    st.write(muhasabah_ielts[urut_pertama_ielts_lolos][4])
                                elif "IELTS Overall" in data[urut_pertama_lolos]: #cek
                                    st.write(muhasabah_ielts[urut_pertama_ielts_lolos][0])

                            #Display muhasabah iBT                                      

                            if ibt and ("iBT Overall" in ada_data[urut_pertama]):
                                if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(data[urut_pertama_ibt_lolos]):
                                    st.write(muhasabah_ibt[urut_pertama_ibt_lolos][0])
                                    st.write(muhasabah_ibt[urut_pertama_ibt_lolos][1])
                                    st.write(muhasabah_ibt[urut_pertama_ibt_lolos][2])
                                    st.write(muhasabah_ibt[urut_pertama_ibt_lolos][3])
                                    st.write(muhasabah_ibt[urut_pertama_ibt_lolos][4])
                                elif "iBT Overall" in data[urut_pertama_ibt_lolos]:
                                    st.write(muhasabah_ibt[urut_pertama_ibt_lolos][0])                                             

                            #Display muhasabah Duolingo                                  
                            if dlg and ("Duolingo Overall" in ada_data[urut_pertama]):
                                if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(data[urut_pertama_dlg_lolos]): 
                                    st.write(muhasabah_duolingo[urut_pertama_dlg_lolos][0])
                                    st.write(muhasabah_duolingo[urut_pertama_dlg_lolos][1])
                                    st.write(muhasabah_duolingo[urut_pertama_dlg_lolos][2])
                                    st.write(muhasabah_duolingo[urut_pertama_dlg_lolos][3])
                                    st.write(muhasabah_duolingo[urut_pertama_dlg_lolos][4])
                                elif "D. Overall" in data[urut_pertama_dlg_lolos]:
                                    st.write(muhasabah_duolingo[urut_pertama_dlg_lolos][0])                                         

                            #Display muhasabah ITP 
                            if itp and ("ITP Overall" in ada_data[urut_pertama]): 
                                if {"ITP Listening", "ITP Structure", "ITP Reading", "ITP Overall"}.issubset(data[urut_pertama_itp_lolos]):
                                    st.write(muhasabah_itp[urut_pertama_itp_lolos][0])
                                    st.write(muhasabah_itp[urut_pertama_itp_lolos][1])
                                    st.write(muhasabah_itp[urut_pertama_itp_lolos][2])
                                    st.write(muhasabah_itp[urut_pertama_itp_lolos][3])                                
                                elif "ITP Overall" in data[urut_pertama_itp_lolos]:
                                    st.write(muhasabah_itp[urut_pertama_itp_lolos][0])

                            #Display muhasabah TPA
                            if n_tpa and ("TPA" in ada_data[urut_pertama]):               
                                if"TPA" in data[urut_pertama_tpa_lolos]:
                                    st.write(muhasabah_tpa[urut_pertama_tpa_lolos][0])

                            #Display muhasabah GRE 
                            if gre and ("GRE" in ada_data[urut_pertama]):                                       
                                if"GRE Verbal Reasoning" in data[urut_pertama_gre_lolos]:
                                    st.write(muhasabah_gre[urut_pertama_gre_lolos][0])
                                    st.write(muhasabah_gre[urut_pertama_gre_lolos][1])
                                    st.write(muhasabah_gre[urut_pertama_gre_lolos][2])        

    ## 3. Inggris kurang, TPA Lolos                        
                    elif len(eng_lolos) == 0:

                        if urut_pertama_eng_kurang == "k1": #(1,1,G5,G8)
                            image = Image.open('cmu.png')
                        elif urut_pertama_eng_kurang == "k2":
                            image = Image.open('toronto.png')
                        elif urut_pertama_eng_kurang == 'k3':
                            image = Image.open('univ_edinburgh.png')
                        elif urut_pertama_eng_kurang == 'k4':
                            image = Image.open('univ_oxford.png')
                        elif urut_pertama_eng_kurang == 'k5':
                            image = Image.open('ntu.png')   
                        elif urut_pertama_eng_kurang == 'k6':
                            image = Image.open('yale.png')
                        elif urut_pertama_eng_kurang == 'k7':
                            image = Image.open('copenhagen.png')
                        elif urut_pertama_eng_kurang == 'k8':
                            image = Image.open('mbzuai.jpg')
                        elif urut_pertama_eng_kurang == 'k9':
                            image = Image.open('kaust.png')
                        elif urut_pertama_eng_kurang == 'k10':
                            image = Image.open('rmit.png')
                        elif urut_pertama_eng_kurang == 'k11':
                            image = Image.open('kfupm.png')
                        elif urut_pertama_eng_kurang == 'k12':
                            image = Image.open('groningen.png')
                        elif urut_pertama_eng_kurang == 'k13':
                            image = Image.open('ugm.png')
                        elif urut_pertama_eng_kurang == 'k14':
                            image = Image.open('itb.png')

                        st.image(image)

                        st.write(f"Agar kamu bisa tetap melanjutkan studi ke {nilai_urut_pertama_eng_kurang['solusi']}, kamu masih perlu meningkatkan nilai bahasa inggrismu agar mencapai persyaratan minimum, Semangat!! 🔥🔥")
                        with kol3:
                            st.success(f"Syarat masuk {data[urut_pertama_eng_kurang]['solusi']}")
                            st.write("IPK Minimum :", data[urut_pertama_eng_kurang]['IPK'])
                            #IELTS
                            if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(data[urut_pertama_eng_kurang]):  
                                st.write("IELTS Writing Minimum :", data[urut_pertama_eng_kurang]["IELTS Writing"])
                                st.write("IELTS Speaking Minimum :", data[urut_pertama_eng_kurang]["IELTS Speaking"])
                                st.write("IELTS Reading Minimum :", data[urut_pertama_eng_kurang]["IELTS Reading"])
                                st.write("IELTS Listening Minimum :", data[urut_pertama_eng_kurang]["IELTS Listening"])
                                st.write("IELTS Overall Minimum :", data[urut_pertama_eng_kurang]["IELTS Overall"])

                            elif "IELTS Overall" in data[urut_pertama_eng_kurang]:
                                st.write("IELTS Overall Minimum :", data[urut_pertama_eng_kurang]["IELTS Overall"])

                            #iBT
                            if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(data[urut_pertama_eng_kurang]):  
                                st.write("iBT Writing Minimum :", data[urut_pertama_eng_kurang]["iBT Writing"])
                                st.write("iBT Speaking Minimum :", data[urut_pertama_eng_kurang]["iBT Speaking"])
                                st.write("iBT Reading Minimum :", data[urut_pertama_eng_kurang]["iBT Reading"])
                                st.write("iBT Listening Minimum :", data[urut_pertama_eng_kurang]["iBT Listening"])
                                st.write("iBT Overall Minimum :", data[urut_pertama_eng_kurang]["iBT Overall"])

                            elif "iBT Overall" in data[urut_pertama_eng_kurang]:
                                st.write("iBT Overall Minimum :", data[urut_pertama_eng_kurang]["iBT Overall"])         

                            #Duolingo
                            if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(data[urut_pertama_eng_kurang]):  
                                st.write("D. Literacy Minimum :", data[urut_pertama_eng_kurang]["D. Literacy"])
                                st.write("D. Conversation Minimum :", data[urut_pertama_eng_kurang]["D. Conversation"])
                                st.write("D. Comprehension Minimum :", data[urut_pertama_eng_kurang]["D. Comprehension"])
                                st.write("D. Production Minimum :", data[urut_pertama_eng_kurang]["D. Production"])
                                st.write("D. Overall Minimum :", data[urut_pertama_eng_kurang]["D. Overall"])

                            elif "D. Overall" in data[urut_pertama_eng_kurang]:
                                st.write("D. Overall Minimum :", data[urut_pertama_eng_kurang]["D. Overall"])           

                            #ITP
                            if {"ITP Listening", "ITP Structure", "ITP Reading", "ITP Overall"}.issubset(data[urut_pertama]):  
                                st.write("ITP Listening Minimum :", data[urut_pertama_eng_kurang]["ITP Listening"])
                                st.write("ITP Structure Minimum :", data[urut_pertama_eng_kurang]["ITP Structure"])
                                st.write("ITP Reading Minimum :", data[urut_pertama_eng_kurang]["ITP Reading"])
                                st.write("ITP Overall Minimum :", data[urut_pertama_eng_kurang]["ITP Overall"])

                            elif "ITP Overall" in data[urut_pertama_eng_kurang]:
                                st.write("ITP Overall Minimum :", data[urut_pertama_eng_kurang]["ITP Overall"])         

                            #TPA
                            if "TPA" in ada_data[urut_pertama]:
                                if len(tpa_lolos) != 0:
                                    if {"TPA"}.issubset(data[urut_pertama_tpa_lolos]):  
                                        st.write("TPA Minimum :", data[urut_pertama_tpa_lolos]["TPA"])
                                elif len(tpa_lolos) == 0:
                                    if {"TPA"}.issubset(data[urut_pertama_tpa_kurang]):  
                                        st.write("TPA Minimum :", data[urut_pertama_tpa_kurang]["TPA"])

                            #GRE
                            if {"GRE Verbal Reasoning", "GRE Quantitative Reasoning", "GRE Analytical Writing"}.issubset(data[urut_pertama]):  
                                st.write("GRE Verbal Reasoning Minimum :", data[urut_pertama_eng_kurang]["GRE Verbal Reasoning"])
                                st.write("GRE Quantitative Reasoning Minimum :", data[urut_pertama_eng_kurang]["GRE Quantitative Reasoning"])
                                st.write("GRE Analytical Writing Minimum :", data[urut_pertama_eng_kurang]["GRE Analytical Writing"])

                            st.write(f"Preferensi yang ada di {data[urut_pertama_eng_kurang]['solusi']}", data[urut_pertama]['Pref'])

                        # Kondisi user alias kasus baru
                        with kol4:
                            st.success(f"Kondisi {nama}")
                            st.write("IPK = ", kasus['IPK'])

                            if ielts:
                                st.write("IELTS Writing =", kasus['IELTS Writing'])
                                st.write("IELTS Speaking =", kasus['IELTS Speaking'])
                                st.write("IELTS Reading =", kasus['IELTS Reading'])
                                st.write("IELTS Listening =", kasus['IELTS Listening'])
                                st.write("IELTS Overall =", kasus['IELTS Overall'])

                            if ibt:
                                st.write("iBT Writing =", kasus['iBT Writing'])
                                st.write("iBT Speaking =", kasus['iBT Speaking'])
                                st.write("iBT Reading =", kasus['iBT Reading'])
                                st.write("iBT Listening =", kasus['iBT Listening'])
                                st.write("iBT Overall =", kasus['iBT Overall'])         

                            if dlg:
                                st.write("Duolingo Literacy =", kasus['D. Literacy'])
                                st.write("Duoling Conversation =", kasus['D. Conversation'])
                                st.write("Duolingo Comprehension =", kasus['D. Comprehension'])
                                st.write("Duolingo Production =", kasus['D. Production'])
                                st.write("Duolingo Overall =", kasus['D. Overall'])  

                            if itp:
                                st.write("ITP Listening =", kasus['ITP Listening'])
                                st.write("ITP Structure =", kasus['ITP Structure'])
                                st.write("ITP Reading =", kasus['ITP Reading'])
                                st.write("ITP Overall =", kasus['ITP Overall'])    

                            if n_tpa:
                                st.write("TPA =", kasus['TPA'])   

                            if gre:
                                st.write("GRE Verbal Reasoning =", kasus['GRE Verbal Reasoning'])
                                st.write("GRE Quantitative Reasoning =", kasus['GRE Quantitative Reasoning'])
                                st.write("GRE Analytical Writing =", kasus['GRE Analytical Writing'])

                            st.write("Preferensi User =", kasus['Pref'])

                        with kol5:
                            st.success("Evaluasi Diri")
                            st.write(muhasabah_ipk[urut_pertama_eng_kurang][0])

                            # Display muhasabah ielts
                            if ielts and ("IELTS Overall" in ada_data[urut_pertama]):
                                if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(data[urut_pertama_eng_kurang]): 
                                    st.write(muhasabah_ielts[urut_pertama_eng_kurang][0])
                                    st.write(muhasabah_ielts[urut_pertama_eng_kurang][1])
                                    st.write(muhasabah_ielts[urut_pertama_eng_kurang][2])
                                    st.write(muhasabah_ielts[urut_pertama_eng_kurang][3])
                                    st.write(muhasabah_ielts[urut_pertama_eng_kurang][4])
                                elif "IELTS Overall" in data[urut_pertama_eng_kurang]:
                                    st.write(muhasabah_ielts[urut_pertama_eng_kurang][0])

                            #Display muhasabah iBT 
                            if ibt and ("iBT Overall" in ada_data[urut_pertama]):
                                if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(data[urut_pertama_eng_kurang]): 
                                    st.write(muhasabah_ibt[urut_pertama_eng_kurang][0])
                                    st.write(muhasabah_ibt[urut_pertama_eng_kurang][1])
                                    st.write(muhasabah_ibt[urut_pertama_eng_kurang][2])
                                    st.write(muhasabah_ibt[urut_pertama_eng_kurang][3])
                                    st.write(muhasabah_ibt[urut_pertama_eng_kurang][4])
                                elif "iBT Overall" in data[urut_pertama_eng_kurang]:
                                    st.write(muhasabah_ibt[urut_pertama_eng_kurang][0])                                             

                            #Display muhasabah Duolingo 
                            if dlg and ("Duolingo Overall" in ada_data[urut_pertama]):
                                if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(data[urut_pertama_eng_kurang]): 
                                    st.write(muhasabah_duolingo[urut_pertama_eng_kurang][0])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_kurang][1])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_kurang][2])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_kurang][3])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_kurang][4])
                                elif "D. Overall" in data[urut_pertama_eng_kurang]:
                                    st.write(muhasabah_duolingo[urut_pertama_eng_kurang][0])                                             

                            #Display muhasabah ITP  
                            if itp and ("ITP Overall" in ada_data[urut_pertama]):
                                if {"ITP Listening", "ITP Structure", "ITP Reading", "ITP Overall"}.issubset(data[urut_pertama_eng_kurang]):
                                    st.write(muhasabah_itp[urut_pertama_eng_kurang][0])
                                    st.write(muhasabah_itp[urut_pertama_eng_kurang][1])
                                    st.write(muhasabah_itp[urut_pertama_eng_kurang][2])                       
                                    st.write(muhasabah_itp[urut_pertama_eng_kurang][3])
                                elif "ITP Overall" in data[urut_pertama_eng_kurang]:
                                    st.write(muhasabah_itp[urut_pertama_eng_kurang][0])

                            #Display muhasabah TPA                                             
                            if "TPA" in ada_data[urut_pertama]:
                                if len(tpa_lolos) != 0:
                                    if "TPA" in data[urut_pertama_tpa_lolos]:
                                        st.write(muhasabah_tpa[urut_pertama_tpa_lolos][0])
                                if len(tpa_lolos) == 0:
                                    if {"TPA"}.issubset(data[urut_pertama_tpa_kurang]):  
                                        st.write(muhasabah_tpa[urut_pertama_tpa_kurang][0])

                            #Display muhasabah GRE                                                 
                            if "GRE Verbal Reasoning" in data[urut_pertama_eng_kurang]:
                                st.write(muhasabah_gre[urut_pertama_eng_kurang][0])
                                st.write(muhasabah_gre[urut_pertama_eng_kurang][1])
                                st.write(muhasabah_gre[urut_pertama_eng_kurang][2])

    ## 4. Inggris Lolos, TPA Kurang                        
                    elif len(eng_lolos) != 0: 

                        if urut_pertama_eng_lolos == "k1": #(1,1,G5,G8)
                            image = Image.open('cmu.png')
                        elif urut_pertama_eng_lolos == "k2":
                            image = Image.open('toronto.png')
                        elif urut_pertama_eng_lolos == 'k3':
                            image = Image.open('univ_edinburgh.png')
                        elif urut_pertama_eng_lolos == 'k4':
                            image = Image.open('univ_oxford.png')
                        elif urut_pertama_eng_lolos == 'k5':
                            image = Image.open('ntu.png')   
                        elif urut_pertama_eng_lolos == 'k6':
                            image = Image.open('yale.png')
                        elif urut_pertama_eng_lolos == 'k7':
                            image = Image.open('copenhagen.png')
                        elif urut_pertama_eng_lolos == 'k8':
                            image = Image.open('mbzuai.jpg')
                        elif urut_pertama_eng_lolos == 'k9':
                            image = Image.open('kaust.png')
                        elif urut_pertama_eng_lolos == 'k10':
                            image = Image.open('rmit.png')
                        elif urut_pertama_eng_lolos == 'k11':
                            image = Image.open('kfupm.png')
                        elif urut_pertama_eng_lolos == 'k12':
                            image = Image.open('groningen.png')
                        elif urut_pertama_eng_lolos == 'k13':
                            image = Image.open('ugm.png')
                        elif urut_pertama_eng_lolos == 'k14':
                            image = Image.open('itb.png')

                        st.image(image)

                        st.write(f"Agar kamu bisa tetap melanjutkan studi ke {nilai_urut_pertama_eng_lolos['solusi']}, kamu masih perlu meningkatkan nilai TPA-mu agar mencapai persyaratan minimum, Semangat!! 🔥🔥")
                        with kol3:
                            st.success(f"Syarat masuk {data[urut_pertama_eng_lolos]['solusi']}")
                            st.write("IPK Minimum :", data[urut_pertama_eng_lolos]['IPK'])
                            #IELTS
                            if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(data[urut_pertama_eng_lolos]):  
                                st.write("IELTS Writing Minimum :", data[urut_pertama_eng_lolos]["IELTS Writing"])
                                st.write("IELTS Speaking Minimum :", data[urut_pertama_eng_lolos]["IELTS Speaking"])
                                st.write("IELTS Reading Minimum :", data[urut_pertama_eng_lolos]["IELTS Reading"])
                                st.write("IELTS Listening Minimum :", data[urut_pertama_eng_lolos]["IELTS Listening"])
                                st.write("IELTS Overall Minimum :", data[urut_pertama_eng_lolos]["IELTS Overall"])

                            elif "IELTS Overall" in data[urut_pertama_eng_lolos]:
                                st.write("IELTS Overall Minimum :", data[urut_pertama_eng_lolos]["IELTS Overall"])

                            #iBT
                            if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(data[urut_pertama_eng_lolos]):  
                                st.write("iBT Writing Minimum :", data[urut_pertama_eng_lolos]["iBT Writing"])
                                st.write("iBT Speaking Minimum :", data[urut_pertama_eng_lolos]["iBT Speaking"])
                                st.write("iBT Reading Minimum :", data[urut_pertama_eng_lolos]["iBT Reading"])
                                st.write("iBT Listening Minimum :", data[urut_pertama_eng_lolos]["iBT Listening"])
                                st.write("iBT Overall Minimum :", data[urut_pertama_eng_lolos]["iBT Overall"])

                            elif "iBT Overall" in data[urut_pertama_eng_lolos]:
                                st.write("iBT Overall Minimum :", data[urut_pertama_eng_lolos]["iBT Overall"])         

                            #Duolingo
                            if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(data[urut_pertama_eng_lolos]):  
                                st.write("D. Literacy Minimum :", data[urut_pertama_eng_lolos]["D. Literacy"])
                                st.write("D. Conversation Minimum :", data[urut_pertama_eng_lolos]["D. Conversation"])
                                st.write("D. Comprehension Minimum :", data[urut_pertama_eng_lolos]["D. Comprehension"])
                                st.write("D. Production Minimum :", data[urut_pertama_eng_lolos]["D. Production"])
                                st.write("D. Overall Minimum :", data[urut_pertama_eng_lolos]["D. Overall"])

                            elif "D. Overall" in data[urut_pertama_eng_lolos]:
                                st.write("D. Overall Minimum :", data[urut_pertama_eng_lolos]["D. Overall"])           

                            #ITP
                            if {"ITP Listening", "ITP Structure", "ITP Reading", "ITP Overall"}.issubset(data[urut_pertama]):  
                                st.write("ITP Listening Minimum :", data[urut_pertama_eng_lolos]["ITP Listening"])
                                st.write("ITP Structure Minimum :", data[urut_pertama_eng_lolos]["ITP Structure"])
                                st.write("ITP Reading Minimum :", data[urut_pertama_eng_lolos]["ITP Reading"])
                                st.write("ITP Overall Minimum :", data[urut_pertama_eng_lolos]["ITP Overall"])

                            elif "ITP Overall" in data[urut_pertama_eng_lolos]:
                                st.write("ITP Overall Minimum :", data[urut_pertama_eng_lolos]["ITP Overall"])         

                            #TPA
                            if "TPA" in ada_data[urut_pertama]:
                                if len(tpa_lolos) == 0: 
                                    if {"TPA"}.issubset(data[urut_pertama_tpa_kurang]) :  
                                        st.write("TPA Minimum :", data[urut_pertama_tpa_kurang]["TPA"])  


                            #GRE
                            if {"GRE Verbal Reasoning", "GRE Quantitative Reasoning", "GRE Analytical Writing"}.issubset(data[urut_pertama]):  
                                st.write("GRE Verbal Reasoning Minimum :", data[urut_pertama_ielts_kurang]["GRE Verbal Reasoning"])
                                st.write("GRE Quantitative Reasoning Minimum :", data[urut_pertama_ielts_kurang]["GRE Quantitative Reasoning"])
                                st.write("GRE Analytical Writing Minimum :", data[urut_pertama_ielts_kurang]["GRE Analytical Writing"])

                            st.write(f"Preferensi yang ada di {data[urut_pertama_eng_lolos]['solusi']}", data[urut_pertama]['Pref'])

                        # Kondisi user alias kasus baru
                        with kol4:
                            st.success(f"Kondisi {nama}")
                            st.write("IPK = ", kasus['IPK'])

                            if ielts:
                                st.write("IELTS Writing =", kasus['IELTS Writing'])
                                st.write("IELTS Speaking =", kasus['IELTS Speaking'])
                                st.write("IELTS Reading =", kasus['IELTS Reading'])
                                st.write("IELTS Listening =", kasus['IELTS Listening'])
                                st.write("IELTS Overall =", kasus['IELTS Overall'])

                            if ibt:
                                st.write("iBT Writing =", kasus['iBT Writing'])
                                st.write("iBT Speaking =", kasus['iBT Speaking'])
                                st.write("iBT Reading =", kasus['iBT Reading'])
                                st.write("iBT Listening =", kasus['iBT Listening'])
                                st.write("iBT Overall =", kasus['iBT Overall'])         

                            if dlg:
                                st.write("Duolingo Literacy =", kasus['D. Literacy'])
                                st.write("Duoling Conversation =", kasus['D. Conversation'])
                                st.write("Duolingo Comprehension =", kasus['D. Comprehension'])
                                st.write("Duolingo Production =", kasus['D. Production'])
                                st.write("Duolingo Overall =", kasus['D. Overall'])  

                            if itp:
                                st.write("ITP Listening =", kasus['ITP Listening'])
                                st.write("ITP Structure =", kasus['ITP Structure'])
                                st.write("ITP Reading =", kasus['ITP Reading'])
                                st.write("ITP Overall =", kasus['ITP Overall'])    

                            if n_tpa:
                                st.write("TPA =", kasus['TPA'])   

                            if gre:
                                st.write("GRE Verbal Reasoning =", kasus['GRE Verbal Reasoning'])
                                st.write("GRE Quantitative Reasoning =", kasus['GRE Quantitative Reasoning'])
                                st.write("GRE Analytical Writing =", kasus['GRE Analytical Writing'])

                            st.write("Preferensi User =", kasus['Pref'])

                        with kol5:
                            st.success("Evaluasi Diri")
                            st.write(muhasabah_ipk[urut_pertama_eng_lolos][0])

                            # Display muhasabah ielts
                            if ielts and ("IELTS Overall" in ada_data[urut_pertama]):
                                if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(data[urut_pertama_eng_lolos]): 
                                    st.write(muhasabah_ielts[urut_pertama_eng_lolos][0])
                                    st.write(muhasabah_ielts[urut_pertama_eng_lolos][1])
                                    st.write(muhasabah_ielts[urut_pertama_eng_lolos][2])
                                    st.write(muhasabah_ielts[urut_pertama_eng_lolos][3])
                                    st.write(muhasabah_ielts[urut_pertama_eng_lolos][4])
                                elif "IELTS Overall" in data[urut_pertama_eng_lolos]:
                                    st.write(muhasabah_ielts[urut_pertama_eng_lolos][0])

                            #Display muhasabah iBT      
                            if ibt and ("iBT Overall" in ada_data[urut_pertama]):
                                if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(data[urut_pertama_eng_lolos]): 
                                    st.write(muhasabah_ibt[urut_pertama_eng_lolos][0])
                                    st.write(muhasabah_ibt[urut_pertama_eng_lolos][1])
                                    st.write(muhasabah_ibt[urut_pertama_eng_lolos][2])
                                    st.write(muhasabah_ibt[urut_pertama_eng_lolos][3])
                                    st.write(muhasabah_ibt[urut_pertama_eng_lolos][4])
                                elif "iBT Overall" in data[urut_pertama_eng_lolos]:
                                    st.write(muhasabah_ibt[urut_pertama_eng_lolos][0])                                             

                            #Display muhasabah Duolingo     
                            if dlg and ("Duolingo Overall" in ada_data[urut_pertama]):
                                if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(data[urut_pertama_eng_lolos]): 
                                    st.write(muhasabah_duolingo[urut_pertama_eng_lolos][0])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_lolos][1])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_lolos][2])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_lolos][3])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_lolos][4])
                                elif "D. Overall" in data[urut_pertama_eng_lolos]:
                                    st.write(muhasabah_duolingo[urut_pertama_eng_lolos][0])                                             

                            #Display muhasabah ITP     
                            if itp and ("ITP Overall" in ada_data[urut_pertama]):
                                if {"ITP Listening", "ITP Structure", "ITP Reading", "ITP Overall"}.issubset(data[urut_pertama_eng_lolos]):
                                    st.write(muhasabah_itp[urut_pertama_eng_lolos][0])
                                    st.write(muhasabah_itp[urut_pertama_eng_lolos][1])
                                    st.write(muhasabah_itp[urut_pertama_eng_lolos][2])         
                                    st.write(muhasabah_itp[urut_pertama_eng_lolos][3])
                                elif "ITP Overall" in data[urut_pertama_eng_lolos]:
                                    st.write(muhasabah_itp[urut_pertama_eng_lolos][0])

                            #Display muhasabah TPA                                             
                            if "TPA" in ada_data[urut_pertama]:
                                if len(tpa_lolos) == 0: 
                                    if "TPA" in data[urut_pertama_tpa_kurang]:
                                        st.write(muhasabah_tpa[urut_pertama_tpa_kurang][0])

                            #Display muhasabah GRE                                                 
                            if "GRE Verbal Reasoning" in data[urut_pertama_eng_lolos]:
                                st.write(muhasabah_gre[urut_pertama_eng_lolos][0])
                                st.write(muhasabah_gre[urut_pertama_eng_lolos][1])
                                st.write(muhasabah_gre[urut_pertama_eng_lolos][2])             


                with kol2:
                    # munculin logo univ
                    if len(lolos) == 0:
                        st.image(Image.open('sad.gif'))
                        st.write("Maaf kamu tidak memenuhi standar kampus manapun di basis data kami")
                        #st.write(f"Tapi jangan khawatir.. berdasarkan hasil kalkulasi, kamu masih berpeluang untuk diterima di {nilai_urut_pertama_tidak_lolos['solusi']} 😃")
                    else:
                        if urut_pertama_lolos == "k1": #(1,1,G5,G8)
                            image = Image.open('cmu.png')
                        elif urut_pertama_lolos == "k2":
                            image = Image.open('toronto.png')
                        elif urut_pertama_lolos == 'k3':
                            image = Image.open('univ_edinburgh.png')
                        elif urut_pertama_lolos == 'k4':
                            image = Image.open('univ_oxford.png')
                        elif urut_pertama_lolos == 'k5':
                            image = Image.open('ntu.png')   
                        elif urut_pertama_lolos == 'k6':
                            image = Image.open('yale.png')
                        elif urut_pertama_lolos == 'k7':
                            image = Image.open('copenhagen.png')
                        elif urut_pertama_lolos == 'k8':
                            image = Image.open('mbzuai.jpg')
                        elif urut_pertama_lolos == 'k9':
                            image = Image.open('kaust.png')
                        elif urut_pertama_lolos == 'k10':
                            image = Image.open('rmit.png')
                        elif urut_pertama_lolos == 'k11':
                            image = Image.open('kfupm.png')
                        elif urut_pertama_lolos == 'k12':
                            image = Image.open('groningen.png')
                        elif urut_pertama_lolos == 'k13':
                            image = Image.open('ugm.png')
                        elif urut_pertama_lolos == 'k14':
                            image = Image.open('itb.png')

                        st.image(image, caption = f"Selamat {nama}, Kamu cocok disini! 🎉") 

                        # printing initial key
                        st.write("Kasus baru ini mirip dengan kasus : " + str(urut_pertama_lolos))
                        st.success(" dengan similaritas: " + str(nilai_urut_pertama_lolos['similaritas']))


                with kol6:
                    st.success("Urutan database")
                    st.write("berdasarkan ranking Universitas 🎓🥇")
                    st.write(rank)
                with kol7:
                    st.success("Urutan hasil kalkulasi")
                    st.write("berdasarkan similaritas 🌟⭐=💯")
                    st.write(urut)
                    
                with kol8:
                    st.succsess("Lolos!! 😃🤲")
                    st.write(f"{nama} lolos persyaratan minimum di :")
                    st.write(lolos)
                with kol9:
                    st.success("Tidak lolos... 😭")
                    st.write(f"{nama} tidak lolos persyaratan minimum di :")
                    st.write(tidak_lolos)
            
                with kol10:
                    st.success("Cocok dengan database ✅")
                    st.write("Data baru cocok dengan basis data:", ada_data)
                with kol11:
                    st.success("Tidak cocok dengan database ❌")
                    st.write("Data baru tidak cocok dengan basis data:", no_data)

### OR Mode Pref
        else:
            with kol2:
                st.success("Mohon maaf, Kasus tidak ada yang cocok dengan seluruh basis data kami")
    
    elif mode_pref == "OR":
        ada_data = {}
        no_data = {}

        for (key, value) in data.items():
            if kasus["Tujuan"] == value["Tujuan"]:
                ada_data[key] = value

            else:
                no_data[key] = value     
        if len(ada_data) != 0:

            ipk_req = []
            ket_ipk = []

            for vals in ada_data.values():
                nbx = 0
                nb = 0

                b = []

                if vals['IPK'] <= kasus['IPK']:
                    b.append("IPK Terpenuhi ✅")
                    nbx += 1
                else:
                    b.append("IPK Tidak terpenuhi ❌")
                nb += 1

                ket_ipk.append(b)
                ipk_req.append(nbx/nb)  

            # Inisiasi variabel req bertipe list untuk menyimpan nilai kesamaan requirements setiap kasus

            if ielts:
                #IELTS
                ielts_req = []
                ket_ielts = []

                # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
                for vals in ada_data.values():
                    nrx = 0
                    nr = 0

                    a = []

                    if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(vals):
                        if vals['IELTS Writing'] <= kasus['IELTS Writing']:
                            a.append("IELTS Writing Terpenuhi ✅")
                            nrx += 1
                        else:
                            a.append("Writing Tidak terpenuhi ❌")
                        nr += 1

                        if vals['IELTS Speaking'] <= kasus['IELTS Speaking']:
                            a.append("IELTS Speaking Terpenuhi ✅")
                            nrx += 1
                        else:
                            a.append("Speaking Tidak terpenuhi ❌")
                        nr += 1

                        if vals['IELTS Reading'] <= kasus['IELTS Reading']:
                            a.append("IELTS Reading Terpenuhi ✅")
                            nrx += 1
                        else:
                            a.append("Reading Tidak terpenuhi ❌")
                        nr += 1

                        if vals['IELTS Listening'] <= kasus['IELTS Listening']:
                            a.append("IELTS Listening Terpenuhi ✅")
                            nrx += 1
                        else:
                            a.append("Listening Tidak terpenuhi ❌")
                        nr += 1

                        if vals['IELTS Overall'] <= kasus['IELTS Overall']:
                            a.append("IELTS Overall Terpenuhi ✅")
                            nrx += 1
                        else:
                            a.append("IELTS Overall Tidak terpenuhi ❌")
                        nr += 1

                        ket_ielts.append(a) #pakai extend list_extend() bisa katanya
                        ielts_req.append(nrx/nr)

                    elif "IELTS Overall" in vals:
                        if vals['IELTS Overall'] <= kasus['IELTS Overall']:
                            a.append("IELTS Overall Terpenuhi ✅")
                            nrx += 1
                        else:
                            a.append("IELTS Overall Tidak terpenuhi ❌")
                        nr += 1

                        ket_ielts.append(a) #pakai extend list_extend() bisa katanya
                        ielts_req.append(nrx/nr)

            if ibt:
                #iBT
                ibt_req = []
                ket_ibt = []

                # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
                for vals in ada_data.values():
                    nrxi = 0
                    nri = 0

                    c = []

                    #iBT
                    if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(vals):
                        if vals['iBT Writing'] <= kasus['iBT Writing']:
                            c.append("iBT Writing Terpenuhi ✅")
                            nrxi += 1
                        else:
                            c.append("iBT Writing Tidak terpenuhi ❌")
                        nri += 1

                        if vals['iBT Speaking'] <= kasus['iBT Speaking']:
                            c.append("iBT Speaking Terpenuhi ✅")
                            nrxi += 1
                        else:
                            c.append("iBT Speaking Tidak terpenuhi ❌")
                        nri += 1

                        if vals['iBT Reading'] <= kasus['iBT Reading']:
                            c.append("iBT Reading Terpenuhi ✅")
                            nrxi += 1
                        else:
                            c.append("iBT Reading Tidak terpenuhi ❌")
                        nri += 1

                        if vals['iBT Listening'] <= kasus['iBT Listening']:
                            c.append("iBT Listening Terpenuhi ✅")
                            nrxi += 1
                        else:
                            c.append("iBT Listening Tidak terpenuhi ❌")
                        nri += 1

                        if vals['iBT Overall'] <= kasus['iBT Overall']:
                            c.append("iBT Overall Terpenuhi ✅")
                            nrxi += 1
                        else:
                            c.append("iBT Overall Tidak terpenuhi ❌")
                        nri += 1

                        ket_ibt.append(c) #pakai extend list_extend() bisa katanya
                        ibt_req.append(nrxi/nri)

                    elif "iBT Overall" in vals:
                        if vals['iBT Overall'] <= kasus['iBT Overall']:
                            c.append("iBT Overall Terpenuhi ✅")
                            nrxi += 1
                        else:
                            c.append("iBT Overall Tidak terpenuhi ❌")
                        nri += 1

                        ket_ibt.append(c) #pakai extend list_extend() bisa katanya
                        ibt_req.append(nrxi/nri)

            #Duolingo

            if dlg:
                dlg_req = []
                ket_dlg = []
                # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
                for vals in ada_data.values():
                    nrxd = 0
                    nrd = 0

                    d = []

                    if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(vals):
                        if vals['D. Literacy'] <= kasus['D. Literacy']:
                            d.append("D. Literacy Terpenuhi ✅")
                            nrxd += 1
                        else:
                            d.append("D. Literacy Tidak terpenuhi ❌")
                        nrd += 1

                        if vals['D. Conversation'] <= kasus['D. Conversation']:
                            d.append("D. Conversation Terpenuhi ✅")
                            nrxd += 1
                        else:
                            d.append("D. Conversation Tidak terpenuhi ❌")
                        nrd += 1

                        if vals['D. Comprehension'] <= kasus['D. Comprehension']:
                            d.append("D. Comprehension Terpenuhi ✅")
                            nrxd += 1
                        else:
                            d.append("D. Comprehension Tidak terpenuhi ❌")
                        nrd += 1

                        if vals['D. Production'] <= kasus['D. Production']:
                            d.append("D. Production Reading Terpenuhi ✅")
                            nrxd += 1
                        else:
                            d.append("D. Production Tidak terpenuhi ❌")
                        nrd += 1

                        if vals['D. Overall'] <= kasus['D. Overall']:
                            d.append("D. Overall Terpenuhi ✅")
                            nrxd += 1
                        else:
                            d.append("D. Overall Tidak terpenuhi ❌")
                        nrd += 1

                        ket_dlg.append(d) #pakai extend list_extend() bisa katanya
                        dlg_req.append(nrxd/nrd)

                    elif "D. Overall" in vals:
                        if vals['D. Overall'] <= kasus['D. Overall']:
                            d.append("D. Overall Terpenuhi ✅")
                            nrxd += 1
                        else:
                            d.append("D. Overall Tidak terpenuhi ❌")
                        nrd += 1

                        ket_dlg.append(d) #pakai extend list_extend() bisa katanya
                        dlg_req.append(nrxd/nrd)

            #ITP
            if itp:
                itp_req = []
                ket_itp = []

                # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
                for vals in ada_data.values():
                    nix = 0 
                    ni = 0

                    e = []

                    #ITP
                    if {"ITP Listening", "ITP Structure", "ITP Reading", "ITP Overall"}.issubset(vals):
                        if vals['ITP Listening'] <= kasus['ITP Listening']:
                            e.append("ITP Listening Terpenuhi ✅")
                            nix += 1
                        else:
                            e.append("ITP Listening Tidak terpenuhi ❌")
                        ni += 1

                        if vals['ITP Structure'] <= kasus['ITP Structure']:
                            e.append("ITP Structure Terpenuhi ✅")
                            nix += 1
                        else:
                            e.append("ITP Structure Tidak terpenuhi ❌")
                        ni += 1

                        if vals['ITP Reading'] <= kasus['ITP Reading']:
                            e.append("ITP Reading Terpenuhi ✅")
                            nix += 1
                        else:
                            e.append("ITP Reading Tidak terpenuhi ❌")
                        ni += 1

                        if vals['ITP Overall'] <= kasus['ITP Overall']:
                            e.append("ITP Overall Terpenuhi ✅")
                            nix += 1
                        else:
                            e.append("ITP Overall Tidak terpenuhi ❌")
                        ni += 1

                        ket_itp.append(e) #pakai extend list_extend() bisa katanya
                        itp_req.append(nix/ni)

                    elif "ITP Overall" in vals:
                        if vals['ITP Overall'] <= kasus['ITP Overall']:
                            e.append("ITP Overall Terpenuhi ✅")
                            nix += 1
                        else:
                            e.append("ITP Overall Tidak terpenuhi ❌")
                        ni += 1

                        ket_itp.append(e) #pakai extend list_extend() bisa katanya
                        itp_req.append(nix/ni)

            if n_tpa:

                #TPA

                tpa_req = []
                ket_tpa = []

                # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
                for vals in ada_data.values():
                    ntx = 0
                    nt = 0

                    f = []

                    #ITP

                    if vals['TPA'] <= kasus['TPA']:
                        f.append("TPA Terpenuhi ✅")
                        ntx += 1
                    else:
                        f.append("TPA Tidak terpenuhi ❌")
                    nt += 1

                    ket_tpa.append(f) #pakai extend list_extend() bisa katanya
                    tpa_req.append(ntx/nt)

            if gre:
                #GRE

                gre_req = []
                ket_gre = []

                # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
                for vals in ada_data.values():
                    ngx = 0
                    ng = 0

                    g = []

                    #GRE

                    if vals['GRE Verbal Reasoning'] <= kasus['GRE Verbal Reasoning']:
                        g.append("GRE Verbal Reasoning Terpenuhi ✅")
                        ngx += 1
                    else:
                        g.append("GRE Verbal Reasoning Tidak terpenuhi ❌")
                    ng += 1

                    if vals['GRE Quantitative Reasoning'] <= kasus['GRE Quantitative Reasoning']:
                        g.append("GRE Quantitative Reasoning Terpenuhi ✅")
                        ngx += 1
                    else:
                        g.append("GRE Quantitative Reasoning Tidak terpenuhi ❌")
                    ng += 1

                    if vals['GRE Analytical Writing'] <= kasus['GRE Analytical Writing']:
                        g.append("GRE Analytical Writing Terpenuhi ✅")
                        ngx += 1
                    else:
                        g.append("GRE Analytical Writing Tidak terpenuhi ❌")
                    ng += 1

                    ket_gre.append(g) #pakai extend list_extend() bisa katanya
                    gre_req.append(ngx/ng)

            #Pref

            # Inisiasi variabel t bertipe list untuk menyimpan nilai kesamaan setiap kasus
            pref = []

            # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
            if len(kasus["Pref"]) != 0:
                for vals in ada_data.values():
                    npx = 0
                    npx += len(kasus['Pref'].intersection(vals['Pref']))
                    np = len(vals['Pref'])
                    pref.append(npx/np)
            else:
                for vals in ada_data.values():
                    npx = 0
                    pref.append(npx)


            #Perhitungan similaritas total

            # Inisiasi variabel t bertipe list untuk menyimpan nilai kesamaan setiap kasus
            total_sim = []

            # Perulangan untuk menghitung nilai kesamaan setiap kasus berdasarkan value
            for vals in ada_data.values():
                nx = 0
                n = 0 #Gak jadi dipakai untuk mode OR

                if vals['IPK'] <= kasus['IPK']:
                    nx += 1
                n += 1

                #IELTS
                if 'IELTS Writing' in kasus and 'IELTS Writing' in vals:
                    if vals['IELTS Writing'] <= kasus['IELTS Writing']:
                        nx += 1
                    n += 1

                if 'IELTS Speaking' in kasus and 'IELTS Speaking' in vals:
                    if vals['IELTS Speaking'] <= kasus['IELTS Speaking']:
                        nx += 1
                    n += 1

                if 'IELTS Reading' in kasus and 'IELTS Reading' in vals:
                    if vals['IELTS Reading'] <= kasus['IELTS Reading']:
                        nx += 1
                    n += 1

                if 'IELTS Listening' in kasus and 'IELTS Listening' in vals:
                    if vals['IELTS Listening'] <= kasus['IELTS Listening']:
                        nx += 1
                    n += 1

                if 'IELTS Overall' in kasus and 'IELTS Overall' in vals:
                    if vals['IELTS Overall'] <= kasus['IELTS Overall']:
                        nx += 1
                    n += 1

                #iBT
                if 'iBT Writing' in kasus and 'iBT Writing' in vals:
                    if vals['iBT Writing'] <= kasus['iBT Writing']:
                        nx += 1
                    n += 1

                if 'iBT Speaking' in kasus and 'iBT Speaking' in vals:
                    if vals['iBT Speaking'] <= kasus['iBT Speaking']:
                        nx += 1
                    n += 1

                if 'iBT Reading' in kasus and 'iBT Reading' in vals:
                    if vals['iBT Reading'] <= kasus['iBT Reading']:
                        nx += 1
                    n += 1

                if 'iBT Listening' in kasus and 'iBT Listening' in vals:
                    if vals['iBT Listening'] <= kasus['iBT Listening']:
                        nx += 1
                    n += 1

                if 'iBT Overall' in kasus and 'iBT Overall' in vals:
                    if vals['iBT Overall'] <= kasus['iBT Overall']:
                        nx += 1
                    n += 1

                #Duolingo
                if 'D. Literacy' in kasus and 'D. Literacy' in vals:
                    if vals['D. Literacy'] <= kasus['D. Literacy']:
                        nx += 1
                    n += 1

                if 'D. Conversation' in kasus and 'D. Conversation' in vals:
                    if vals['D. Conversation'] <= kasus['D. Conversation']:
                        nx += 1
                    n += 1

                if 'D. Comprehension' in kasus and 'D. Comprehension' in vals:
                    if vals['D. Comprehension'] <= kasus['D. Comprehension']:
                        nx += 1
                    n += 1

                if 'D. Production' in kasus and 'D. Production' in vals:
                    if vals['D. Production'] <= kasus['D. Production']:
                        nx += 1
                    n += 1

                if 'D. Overall' in kasus and 'D. Overall' in vals:
                    if vals['D. Overall'] <= kasus['D. Overall']:
                        nx += 1
                    n += 1            

                #ITP
                if 'ITP Listening' in kasus and 'ITP Listening' in vals:
                    if vals['ITP Listening'] <= kasus['ITP Listening']:
                        nx += 1
                    n += 1

                if 'ITP Structure' in kasus and 'ITP Structure' in vals:
                    if vals['ITP Structure'] <= kasus['ITP Structure']:
                        nx += 1
                    n += 1

                if 'ITP Reading' in kasus and 'ITP Reading' in vals:
                    if vals['ITP Reading'] <= kasus['ITP Reading']:
                        nx += 1
                    n += 1

                if 'ITP Overall' in kasus and 'ITP Overall' in vals:
                    if vals['ITP Overall'] <= kasus['ITP Overall']:
                        nx += 1
                    n += 1 


                #TPA
                if 'TPA' in kasus and 'TPA' in vals:
                    if vals['TPA'] <= kasus['TPA']:
                        nx += 1
                    n += 1

                #GRE

                if 'GRE Verbal Reasoning' in kasus and 'GRE Verbal Reasoning' in vals:
                    if vals['GRE Verbal Reasoning'] <= kasus['GRE Verbal Reasoning']:
                        nx += 1
                    n += 1

                if 'GRE Quantitative Reasoning' in kasus and 'GRE Quantitative Reasoning' in vals:
                    if vals['GRE Quantitative Reasoning'] <= kasus['GRE Quantitative Reasoning']:
                        nx += 1
                    n += 1

                if 'GRE Analytical Writing' in kasus and 'GRE Analytical Writing' in vals:
                    if vals['GRE Analytical Writing'] <= kasus['GRE Analytical Writing']:
                        nx += 1
                    n += 1

                nx += len(kasus['Pref'].intersection(vals['Pref']))
                n += (len(kasus['Pref']))

                total_sim.append(nx/n)             

            solusi = []
            for sol in ada_data:
                solusi.append(data[sol]['solusi'])

            #Bahasa inggris lolos setidaknya di salah satu

            rank = {}
            # Lolos dan lolos persyaratan minimal

            if ielts and ibt and dlg and itp and n_tpa and gre:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for g in ada_data.keys():
                    rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, "iBT Terpenuhi (%)": ibt_req[i]*100, "Duolingo terpenuhi (%)": dlg_req[i]*100, "ITP terpenuhi (%)": itp_req[i], "TPA terpenuhi (%)": tpa_req[i]*100, "GRE terpenuhi (%)": gre_req[i]*100, 'solusi': solusi[i]} 
                    i += 1

            elif ielts and ibt and dlg and itp and n_tpa:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for g in ada_data.keys():
                    rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, "iBT Terpenuhi (%)": ibt_req[i]*100, "Duolingo terpenuhi (%)": dlg_req[i]*100, "ITP terpenuhi (%)": itp_req[i]*100, "TPA terpenuhi (%)": tpa_req[i]*100, 'solusi': solusi[i]} 
                    i += 1        

            elif ielts and ibt and dlg:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for g in ada_data.keys():
                    rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, "iBT Terpenuhi (%)": ibt_req[i]*100, "Duolingo terpenuhi (%)": dlg_req[i]*100, 'solusi': solusi[i]} 
                    i += 1        

            elif ielts and ibt:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for (g, gi) in ada_data.items():
                    if {"IELTS Overall", "iBT Overall"}.issubset(gi): 
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, "iBT Terpenuhi (%)": ibt_req[i]*100, 'solusi': solusi[i]} 
                    elif "IELTS Overall" in gi:
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, 'solusi': solusi[i]} 
                    elif "iBT Overall" in gi:
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, "iBT Terpenuhi (%)": ibt_req[i]*100, 'solusi': solusi[i]}                     
                        i += 1        

            elif ielts and dlg:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for g in ada_data.keys():
                    rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, "Duolingo terpenuhi (%)": dlg_req[i]*100, 'solusi': solusi[i]} 
                    i += 1        

            elif dlg and ibt:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for g in ada_data.keys():
                    rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, "iBT Terpenuhi (%)": ibt_req[i]*100, "Duolingo terpenuhi (%)": dlg_req[i]*100, 'solusi': solusi[i]} 
                    i += 1 

            elif itp and n_tpa:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for g in ada_data.keys():
                    rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, "ITP terpenuhi (%)": itp_req[i]*100, "TPA terpenuhi (%)": tpa_req[i]*100, 'solusi': solusi[i]} 
                    i += 1                        

            elif itp:

                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for (g, gi) in ada_data.items():
                    if "ITP Overall" in gi:
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, "ITP terpenuhi (%)": itp_req[i]*100, 'solusi': solusi[i]} 
                        i += 1 

            elif ielts:
                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for (g, gi) in ada_data.items():
                    if "IELTS Overall" in gi:         
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, 'solusi': solusi[i]} 
                        i += 1  

            elif ielts and n_tpa:
                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for (g, gi) in ada_data.items():
                    if "IELTS Overall" in gi:         
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, 'IELTS terpenuhi (%)': ielts_req[i]*100, "TPA terpenuhi (%)": tpa_req[i]*100, 'solusi': solusi[i]} 
                        i += 1  

            elif ibt:
                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for (g,gi) in ada_data.items(): 
                    if "iBT Overall" in gi:
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, "iBT Terpenuhi (%)": ibt_req[i]*100, 'solusi': solusi[i]} 
                        i += 1  

            elif dlg:
                i = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for (g, gi) in ada_data.items():
                    if "D. Overall" in gi:
                        rank[g] = {'similaritas': total_sim[i], 'IPK terpenuhi (%)': ipk_req[i]*100, "Duolingo terpenuhi (%)": dlg_req[i]*100, 'solusi': solusi[i]}      
                        i += 1  

            #Pengurutan berdasarkan IPK Terpenuhi

            if rank == {}:
                with kol2:
                    st.write("Silakan isi nilai bahasa inggris terlebih dahulu")
            else:
                urut = dict(sorted(rank.items(), key= lambda x:x[1]['IPK terpenuhi (%)'], reverse = True))
                # Using keys() + list()
                # Getting first key in dictionary
                urut_pertama = list(urut.keys())[0] #Gak dipake lagi

                # Using values() + list()
                # Getting value in first key in dictionary
                nilai_urut_pertama = list(urut.values())[0] #Gak dipake lagi

                # Pengelompokkan list ipk terpenuhi

                ipk_lolos = {}
                ipk_kurang = {}

                for (key, value) in urut.items():
                    if value['IPK terpenuhi (%)'] == 100:
                        ipk_lolos[key] = value
                    else:
                        ipk_kurang[key] = value

                if len(ipk_lolos) != 0:
                    urut_pertama_ipk_lolos = list(ipk_lolos.keys())[0]
                    nilai_urut_pertama_ipk_lolos = list(ipk_lolos.values())[0]
                if len(ipk_kurang) != 0:
                    urut_pertama_ipk_kurang = list(ipk_kurang.keys())[0]
                    nilai_urut_pertama_ipk_kurang = list(ipk_kurang.values())[0]

                # Pengelompokkan list IELTS terpenuhi
                if ielts and("IELTS Overall" in ada_data[urut_pertama]):
                    ielts_lolos = {}
                    ielts_kurang = {}

                    for (key, value) in urut.items():
                        if value['IELTS terpenuhi (%)'] == 100:
                            ielts_lolos[key] = value
                        else:
                            ielts_kurang[key] = value

                    if len(ielts_lolos) != 0:
                        urut_pertama_ielts_lolos = list(ielts_lolos.keys())[0]
                        nilai_urut_pertama_ielts_lolos = list(ielts_lolos.values())[0]
                    if len(ielts_kurang) != 0:
                        urut_pertama_ielts_kurang = list(ielts_kurang.keys())[0]
                        nilai_urut_pertama_ielts_kurang = list(ielts_kurang.values())[0]

                # Pengelompokkan list iBT terpenuhi
                if ibt and ("iBT Overall" in ada_data[urut_pertama]):
                    ibt_lolos = {}
                    ibt_kurang = {}

                    for (key, value) in urut.items():
                        if value['iBT Terpenuhi (%)'] == 100:
                            ibt_lolos[key] = value
                        else:
                            ibt_kurang[key] = value

                    if len(ibt_lolos) != 0:
                        urut_pertama_ibt_lolos = list(ibt_lolos.keys())[0]
                        nilai_urut_pertama_ibt_lolos = list(ibt_lolos.values())[0]
                    if len(ibt_kurang) != 0:
                        urut_pertama_ibt_kurang = list(ibt_kurang.keys())[0]
                        nilai_urut_pertama_ibt_kurang = list(ibt_kurang.values())[0]

                # Pengelompokkan list Duolingo terpenuhi
                if dlg and ("Duolingo Overall" in ada_data[urut_pertama]):
                    dlg_lolos = {}
                    dlg_kurang = {}

                    for (key, value) in urut.items():
                        if value['Duolingo terpenuhi (%)'] == 100:
                            dlg_lolos[key] = value
                        else:
                            dlg_kurang[key] = value

                    if len(dlg_lolos) != 0:
                        urut_pertama_dlg_lolos = list(dlg_lolos.keys())[0]
                        nilai_urut_pertama_dlg_lolos = list(dlg_lolos.values())[0]
                    if len(dlg_kurang) != 0:
                        urut_pertama_dlg_kurang = list(dlg_kurang.keys())[0]
                        nilai_urut_pertama_dlg_kurang = list(dlg_kurang.values())[0]

                # Pengelompokkan list ITP terpenuhi
                if itp and ("ITP Overall" in ada_data[urut_pertama]):
                    itp_lolos = {}
                    itp_kurang = {}

                    for (key, value) in urut.items():
                        if value['ITP terpenuhi (%)'] == 100:
                            itp_lolos[key] = value
                        else:
                            itp_kurang[key] = value

                    if len(itp_lolos) != 0:
                        urut_pertama_itp_lolos = list(itp_lolos.keys())[0]
                        nilai_urut_pertama_itp_lolos = list(itp_lolos.values())[0]
                    if len(itp_kurang) != 0:
                        urut_pertama_itp_kurang = list(itp_kurang.keys())[0]
                        nilai_urut_pertama_itp_kurang = list(itp_kurang.values())[0]

                # Pengelompokkan list TPA terpenuhi
                if n_tpa and ("TPA" in ada_data[urut_pertama]):
                    tpa_lolos = {}
                    tpa_kurang = {}

                    for (key, value) in urut.items():
                        if value['TPA terpenuhi (%)'] == 100:
                            tpa_lolos[key] = value
                        else:
                            tpa_kurang[key] = value

                    if len(tpa_lolos) != 0:
                        urut_pertama_tpa_lolos = list(tpa_lolos.keys())[0]
                        nilai_urut_pertama_tpa_lolos = list(tpa_lolos.values())[0]
                    if len(tpa_kurang) != 0:
                        urut_pertama_tpa_kurang = list(tpa_kurang.keys())[0]
                        nilai_urut_pertama_tpa_kurang = list(tpa_kurang.values())[0]

                # Pengelompokkan list GRE terpenuhi
                if gre and ("GRE" in ada_data[urut_pertama]):
                    gre_lolos = {}
                    gre_kurang = {}

                    for (key, value) in urut.items():
                        if value['GRE terpenuhi (%)'] == 100:
                            gre_lolos[key] = value
                        else:
                            gre_kurang[key] = value

                    if len(gre_lolos) != 0:
                        urut_pertama_gre_lolos = list(gre_lolos.keys())[0]
                        nilai_urut_pertama_gre_lolos = list(gre_lolos.values())[0]
                    if len(gre_kurang) != 0:
                        urut_pertama_gre_kurang = list(gre_kurang.keys())[0]
                        nilai_urut_pertama_gre_kurang = list(gre_kurang.values())[0]


                # Pengelompokkan list Inggris terpenuhi

                eng_lolos = {}
                eng_kurang = {}

                for (key, value) in urut.items():
                    #IELTS, iBT, Duolingo, ITP
                    if {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)', 'ITP terpenuhi (%)'}.issubset(value):
                        if value['IELTS terpenuhi (%)'] == 100 or value['iBT Terpenuhi (%)'] == 100 or value['Duolingo terpenuhi (%)'] == 100 or value['ITP terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]

                    #IELTS, iBT, Duolingo
                    if {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['IELTS terpenuhi (%)'] == 100 or value['iBT Terpenuhi (%)'] == 100 or value['Duolingo terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]

                    #IELTS dan iBT
                    if {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)'}.issubset(value):
                        if value['IELTS terpenuhi (%)'] == 100 or value['iBT Terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]   

                    #IELTS dan Duolingo
                    if {'IELTS terpenuhi (%)', 'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['IELTS terpenuhi (%)'] == 100 or value['Duolingo terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]

                    #iBT dan Dulingo
                    if {'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['iBT Terpenuhi (%)'] == 100 or value['Duolingo terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]

                    #IELTS 
                    if {'IELTS terpenuhi (%)'}.issubset(value):
                        if value['IELTS terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]   

                    #iBT
                    if {'iBT Terpenuhi (%)'}.issubset(value):
                        if value['iBT Terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]   

                    #Dulingo
                    if {'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['Duolingo terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]

                    #ITP
                    if {'ITP terpenuhi (%)'}.issubset(value):
                        if value['ITP terpenuhi (%)'] == 100:
                            eng_lolos[key] = value
                        else:
                            eng_kurang[key] = value

                        if len(eng_lolos) != 0:
                            urut_pertama_eng_lolos = list(eng_lolos.keys())[0]
                            nilai_urut_pertama_eng_lolos = list(eng_lolos.values())[0]
                        if len(eng_kurang) != 0:
                            urut_pertama_eng_kurang = list(eng_kurang.keys())[0]
                            nilai_urut_pertama_eng_kurang = list(eng_kurang.values())[0]
                #TPA diatas

                #GRE diatas

                # Pengelompokkan lolos dan tidak lolos requirement, sudah diurutkan

                lolos = {}
                tidak_lolos = {}

                for (key, value) in urut.items():

                    #IELTS, iBT, Duolingo, ITP, TPA, GRE  
                    if {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)', 'ITP terpenuhi (%)', 'TPA terpenuhi (%)', 'GRE terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)'] == 100 or value['iBT Terpenuhi (%)']  == 100 or value['Duolingo terpenuhi (%)']  == 100  or value['ITP terpenuhi (%)'] == 100) or value['TPA terpenuhi (%)'] == 100 or value['GRE terpenuhi (%)'] == 100:
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #IELTS, iBT, Duolingo, ITP , TPA           
                    elif {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)', 'ITP terpenuhi (%)', 'TPA terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)'] == 100 or value['iBT Terpenuhi (%)']  == 100 or value['Duolingo terpenuhi (%)']  == 100  or value['ITP terpenuhi (%)'] == 100 or value['TPA terpenuhi (%)'] == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #IELTS, iBT, Duolingo, ITP         
                    elif {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)', 'ITP terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)'] == 100 or value['iBT Terpenuhi (%)']  == 100 or value['Duolingo terpenuhi (%)']  == 100  or value['ITP terpenuhi (%)'] == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value                        

                    #IELTS, iBT, Duolingo                        
                    elif {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)']  == 100  or value['iBT Terpenuhi (%)']  == 100 or value['Duolingo terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #IELTS, iBT                      
                    elif {'IELTS terpenuhi (%)', 'iBT Terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)']  == 100  or value['iBT Terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #IELTS, Duolingo                        
                    elif {'IELTS terpenuhi (%)', 'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)']  == 100  or value['Duolingo terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #iBT, Duolingo                        
                    elif {'iBT Terpenuhi (%)', 'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['iBT Terpenuhi (%)']  == 100 or value['Duolingo terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #IELTS                  
                    elif {'IELTS terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #iBT                      
                    elif {'iBT Terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['iBT Terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #Duolingo                        
                    elif {'Duolingo terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['Duolingo terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #ITP, TPA                  
                    elif {'ITP terpenuhi (%)', 'TPA terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['ITP terpenuhi (%)']  == 100 and value['TPA terpenuhi (%)'] == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #ITP                        
                    elif {'ITP terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['ITP terpenuhi (%)']  == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value


                    #IELTS, TPA                  
                    elif {'IELTS terpenuhi (%)', 'TPA terpenuhi (%)'}.issubset(value):
                        if value['IPK terpenuhi (%)'] == 100 and (value['IELTS terpenuhi (%)']  == 100 and value['TPA terpenuhi (%)'] == 100):
                            lolos[key] = value
                        else:
                            tidak_lolos[key] = value

                    #iBT, TPA

                    #Duolingo, TPA

                # Using keys() + list()
                # Getting first key in dictionary

                if len(lolos) != 0:
                    urut_pertama_lolos = list(lolos.keys())[0]
                    nilai_urut_pertama_lolos = list(lolos.values())[0]
                if len(tidak_lolos) != 0:
                    urut_pertama_tidak_lolos = list(tidak_lolos.keys())[0]
                    nilai_urut_pertama_tidak_lolos = list(tidak_lolos.values())[0]

                # list Muhasabah ipk tiap univ
                muhasabah_ipk = {}

                j = 0 # tipe data list dimulai dari 0 -> [0.0, 0.25 ...]
                for g in ada_data.keys():
                    muhasabah_ipk[g] = ket_ipk[j]
                    j += 1

                #List muhasabah ielts tiap univ

                if ielts and ("IELTS Overall" in ada_data[urut_pertama]):
                    muhasabah_ielts = {}

                    ie = 0
                    for t in ada_data.keys():
                        muhasabah_ielts[t] = ket_ielts[ie]
                        ie += 1

                #List muhasabah iBT tiap univ
                if ibt and ("iBT Overall" in ada_data[urut_pertama]):
                    muhasabah_ibt = {}

                    ib = 0
                    for u in ada_data.keys():
                        muhasabah_ibt[u] = ket_ibt[ib]
                        ib += 1

                #List muhasabah duolingo tiap univ
                if dlg and ("Duolingo Overall" in ada_data[urut_pertama]):
                    muhasabah_duolingo = {}

                    dl = 0
                    for v in ada_data.keys():
                        muhasabah_duolingo[v] = ket_duolingo[dl]
                        dl += 1

                #List muhasabah ITP tiap univ     
                if itp and ("ITP Overall" in ada_data[urut_pertama]):
                    muhasabah_itp = {}

                    it = 0
                    for (w, wi) in ada_data.items():
                        if "ITP Overall" in wi:
                            muhasabah_itp[w] = ket_itp[it]
                            it += 1

                #List muhasabah TPA tiap univ                
                if n_tpa and ("TPA" in ada_data[urut_pertama]):
                    muhasabah_tpa = {}

                    tp = 0
                    for x in ada_data.keys():
                        muhasabah_tpa[x] = ket_tpa[tp]
                        tp += 1

                if gre and ("GRE" in ada_data[urut_pertama]):
                    #List muhasabah GRE tiap univ
                    muhasabah_gre = {}

                    gr = 0
                    for y in ada_data.keys():
                        muhasabah_gre[y] = ket_gre[gr]
                        gr += 1

                with kol00:
                    st.success("Evaluasi Similaritas Kasus Baru dengan database")
    ## 1.IPK Kurang!!
                    if len(ipk_lolos) == 0:
                        st.write("IPK kamu kurang, Silakan coba mode preferensi OR")
                        with kol4b:
                            st.success(f"Kondisi {nama}")
                            st.write("IPK = ", kasus['IPK'])

                            if ielts:
                                if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(kasus):
                                    st.write("IELTS Writing =", kasus['IELTS Writing'])
                                    st.write("IELTS Speaking =", kasus['IELTS Speaking'])
                                    st.write("IELTS Reading =", kasus['IELTS Reading'])
                                    st.write("IELTS Listening =", kasus['IELTS Listening'])
                                    st.write("IELTS Overall =", kasus['IELTS Overall'])
                                elif "IELTS Overall" in kasus:
                                    st.write("IELTS Overall =", kasus['IELTS Overall'])

                            if "Tujuan" in kasus:
                                st.write("Tujuan =", kasus['Tujuan'])

                            if ibt:
                                if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(kasus):
                                    st.write("iBT Writing =", kasus["iBT Writing"])
                                    st.write("iBT Speaking =", kasus["iBT Speaking"])
                                    st.write("iBT Reading =", kasus["iBT Reading"])
                                    st.write("iBT Listening =", kasus["iBT Listening"])
                                    st.write("iBT Overall =", kasus["iBT Overall"])
                                elif "iBT Overall" in kasus:
                                    st.write("iBT Overall =", kasus["iBT Overall"])

                            if dlg:
                                if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(kasus):
                                    st.write("D. Literacy =", kasus["D. Literacy"])
                                    st.write("D. Conversation =", kasus["D. Conversation"])
                                    st.write("D. Comprehension =", kasus["D. Comprehension"])
                                    st.write("D. Production =", kasus["D. Production"])
                                    st.write("D. Overall =", kasus["D. Overall"])
                                elif "D. Overall" in kasus:
                                    st.write("D. Overall =", kasus["D. Overall"])

                            if itp:
                                if "ITP Overall" in kasus:
                                    st.write("ITP Listening =", kasus["ITP Listening"])
                                    st.write("ITP Structure =", kasus["ITP Structure"])
                                    st.write("ITP Reading =", kasus["ITP Reading"])
                                    st.write("ITP Overall =", kasus["ITP Overall"])

                            if n_tpa:
                                if "TPA" in kasus:
                                    st.write("TPA =", kasus["TPA"])

                            if gre:
                                if "GRE Verbal Reasoning" in kasus:
                                    st.write("GRE Verbal Reasoning =", kasus["GRE Verbal Reasoning"])
                                    st.write("GRE Quantitative Reasoning =", kasus["GRE Quantitative Reasoning"])
                                    st.write("GRE Analytical Writing =", kasus["GRE Analytical Writing"])

                            #if "Gratis Pendaftaran" in kasus['Pref']:
                            st.write("Preferensi User =", kasus['Pref'])    


                        # Ini untuk yg OR nanti
                        #with kol3:
                         #   st.success(f"Syarat masuk {data[urut_pertama_ipk_lolos]['solusi']}")
                          #  st.write("IPK Minimum :", data[urut_pertama_ipk_lolos]['IPK'])
                           # st.write("IELTS Writing Minimum :", data[urut_pertama_ipk_lolos]["IELTS Writing"])
                            #st.write("IELTS Speaking Minimum :", data[urut_pertama_ipk_lolos]["IELTS Speaking"])
                            #st.write("IELTS Reading Minimum :", data[urut_pertama_ipk_lolos]["IELTS Reading"])
                            #st.write("IELTS Listening Minimum :", data[urut_pertama_ipk_lolos]["IELTS Listening"])
                            #st.write("IELTS Overall Minimum :", data[urut_pertama_ipk_lolos]["IELTS Overall"])
                            #st.write(f"Preferensi yang ada di {data[urut_pertama_ipk_lolos]['solusi']}", data[urut_pertama]['Pref'])

                        #with kol5:
                         #   st.success("Evaluasi Diri")
                          #  st.write(muhasabah[urut_pertama_ipk_lolos][0])
                           # st.write(muhasabah[urut_pertama_ipk_lolos][1])
                           # st.write(muhasabah[urut_pertama_ipk_lolos][2])
                           # st.write(muhasabah[urut_pertama_ipk_lolos][3])
                           # st.write(muhasabah[urut_pertama_ipk_lolos][4])
                           # st.write(muhasabah[urut_pertama_ipk_lolos][5])     

    ## 2. Lolos persyaratan minimum kampus

                    elif len(lolos) != 0:
                        st.write(f"Alhamdulillah semua persyaratan minimum kampus {nilai_urut_pertama_lolos['solusi']} telah kamu penuhi, berikut perbandingannya")

                        with kol3:
                            st.success(f"Syarat masuk {data[urut_pertama_lolos]['solusi']}")
                            st.write("IPK Minimum :", data[urut_pertama_lolos]['IPK'])
                            #IELTS
                            if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(data[urut_pertama_lolos]):  
                                st.write("IELTS Writing Minimum :", data[urut_pertama_lolos]["IELTS Writing"])
                                st.write("IELTS Speaking Minimum :", data[urut_pertama_lolos]["IELTS Speaking"])
                                st.write("IELTS Reading Minimum :", data[urut_pertama_lolos]["IELTS Reading"])
                                st.write("IELTS Listening Minimum :", data[urut_pertama_lolos]["IELTS Listening"])
                                st.write("IELTS Overall Minimum :", data[urut_pertama_lolos]["IELTS Overall"])

                            elif "IELTS Overall" in data[urut_pertama_lolos]:
                                st.write("IELTS Overall Minimum :", data[urut_pertama_lolos]["IELTS Overall"])

                            #iBT    
                            if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(data[urut_pertama_lolos]):  
                                st.write("iBT Writing Minimum :", data[urut_pertama_lolos]["iBT Writing"])
                                st.write("iBT Speaking Minimum :", data[urut_pertama_lolos]["iBT Speaking"])
                                st.write("iBT Reading Minimum :", data[urut_pertama_lolos]["iBT Reading"])
                                st.write("iBT Listening Minimum :", data[urut_pertama_lolos]["iBT Listening"])
                                st.write("iBT Overall Minimum :", data[urut_pertama_lolos]["iBT Overall"])

                            elif "iBT Overall" in data[urut_pertama_lolos]:
                                st.write("iBT Overall Minimum :", data[urut_pertama_lolos]["iBT Overall"])

                            #Duolingo    
                            if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(data[urut_pertama_lolos]):  
                                st.write("D. Literacy Minimum :", data[urut_pertama_lolos]["D. Literacy"])
                                st.write("D. Conversation Minimum :", data[urut_pertama_lolos]["D. Conversation"])
                                st.write("D. Comprehension Minimum :", data[urut_pertama_lolos]["D. Comprehension"])
                                st.write("D. Production Minimum :", data[urut_pertama_lolos]["D. Production"])
                                st.write("D. Overall Minimum :", data[urut_pertama_lolos]["D. Overall"])

                            elif "D. Overall" in data[urut_pertama_lolos]:
                                st.write("D. Overall Minimum :", data[urut_pertama_lolos]["D. Overall"])

                            #ITP    
                            if "ITP Overall" in data[urut_pertama_lolos]:  
                                st.write("ITP Overall Minimum :", data[urut_pertama_lolos]["ITP Overall"])

                            #TPA
                            if "TPA" in ada_data[urut_pertama]:
                                if len(tpa_lolos) != 0:
                                    if "TPA" in data[urut_pertama_lolos]:  
                                        st.write("TPA Minimum :", data[urut_pertama_lolos]["TPA"])

                            #GRE    
                            if {"GRE Verbal Reasoning", "GRE Quantitative Reasoning", "GRE Analytical"}.issubset(data[urut_pertama_lolos]):  
                                st.write("GRE Verbal Reasoning Minimum :", data[urut_pertama_lolos]["GRE Verbal Reasoning"])
                                st.write("GRE Quantitative Reasoning :", data[urut_pertama_lolos]["GRE Quantitative Reasoning"])
                                st.write("GRE Analytical Minimum :", data[urut_pertama_lolos]["GRE Analytical"])

                            st.write(f"Preferensi yang ada di {data[urut_pertama_lolos]['solusi']}", data[urut_pertama]['Pref'])                             

                        with kol4:
                            st.success(f"Kondisi {nama}")
                            st.write("IPK = ", kasus['IPK'])

                            if ielts:
                                st.write("IELTS Writing =", kasus['IELTS Writing'])
                                st.write("IELTS Speaking =", kasus['IELTS Speaking'])
                                st.write("IELTS Reading =", kasus['IELTS Reading'])
                                st.write("IELTS Listening =", kasus['IELTS Listening'])
                                st.write("IELTS Overall =", kasus['IELTS Overall'])

                            if ibt:
                                st.write("iBT Writing =", kasus['iBT Writing'])
                                st.write("iBT Speaking =", kasus['iBT Speaking'])
                                st.write("iBT Reading =", kasus['iBT Reading'])
                                st.write("iBT Listening =", kasus['iBT Listening'])
                                st.write("iBT Overall =", kasus['iBT Overall'])                        
                            if dlg:
                                st.write("Duolingo Literacy =", kasus['D. Literacy'])
                                st.write("Duoling Conversation =", kasus['D. Conversation'])
                                st.write("Duolingo Comprehension =", kasus['D. Comprehension'])
                                st.write("Duolingo Production =", kasus['D. Production'])
                                st.write("Duolingo Overall =", kasus['D. Overall'])  

                            if itp:
                                st.write("ITP Listening =", kasus['ITP Listening'])
                                st.write("ITP Structure =", kasus['ITP Structure'])
                                st.write("ITP Reading =", kasus['ITP Reading'])
                                st.write("ITP Overall =", kasus['ITP Overall'])                         
                            if n_tpa:
                                st.write("TPA =", kasus['TPA'])   

                            if gre:
                                st.write("GRE Verbal Reasoning =", kasus['GRE Verbal Reasoning'])
                                st.write("GRE Quantitative Reasoning =", kasus['GRE Quantitative Reasoning'])
                                st.write("GRE Analytical Writing =", kasus['GRE Analytical Writing'])

                            st.write("Preferensi User =", kasus['Pref'])

                        with kol5:
                            st.success("Evaluasi Diri")
                            st.write(muhasabah_ipk[urut_pertama_eng_lolos][0])

                            if ielts and ("IELTS Overall" in ada_data[urut_pertama]):
                                if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(data[urut_pertama_lolos]):  #Cek
                                    st.write(muhasabah_ielts[urut_pertama_ielts_lolos][0])
                                    st.write(muhasabah_ielts[urut_pertama_ielts_lolos][1])
                                    st.write(muhasabah_ielts[urut_pertama_ielts_lolos][2])
                                    st.write(muhasabah_ielts[urut_pertama_ielts_lolos][3])
                                    st.write(muhasabah_ielts[urut_pertama_ielts_lolos][4])
                                elif "IELTS Overall" in data[urut_pertama_lolos]: #cek
                                    st.write(muhasabah_ielts[urut_pertama_ielts_lolos][0])

                            #Display muhasabah iBT                                      

                            if ibt and ("iBT Overall" in ada_data[urut_pertama]):
                                if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(data[urut_pertama_ibt_lolos]):
                                    st.write(muhasabah_ibt[urut_pertama_ibt_lolos][0])
                                    st.write(muhasabah_ibt[urut_pertama_ibt_lolos][1])
                                    st.write(muhasabah_ibt[urut_pertama_ibt_lolos][2])
                                    st.write(muhasabah_ibt[urut_pertama_ibt_lolos][3])
                                    st.write(muhasabah_ibt[urut_pertama_ibt_lolos][4])
                                elif "iBT Overall" in data[urut_pertama_ibt_lolos]:
                                    st.write(muhasabah_ibt[urut_pertama_ibt_lolos][0])                                             

                            #Display muhasabah Duolingo                                  
                            if dlg and ("Duolingo Overall" in ada_data[urut_pertama]):
                                if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(data[urut_pertama_dlg_lolos]): 
                                    st.write(muhasabah_duolingo[urut_pertama_dlg_lolos][0])
                                    st.write(muhasabah_duolingo[urut_pertama_dlg_lolos][1])
                                    st.write(muhasabah_duolingo[urut_pertama_dlg_lolos][2])
                                    st.write(muhasabah_duolingo[urut_pertama_dlg_lolos][3])
                                    st.write(muhasabah_duolingo[urut_pertama_dlg_lolos][4])
                                elif "D. Overall" in data[urut_pertama_dlg_lolos]:
                                    st.write(muhasabah_duolingo[urut_pertama_dlg_lolos][0])                                         

                            #Display muhasabah ITP 
                            if itp and ("ITP Overall" in ada_data[urut_pertama]): 
                                if {"ITP Listening", "ITP Structure", "ITP Reading", "ITP Overall"}.issubset(data[urut_pertama_itp_lolos]):
                                    st.write(muhasabah_itp[urut_pertama_itp_lolos][0])
                                    st.write(muhasabah_itp[urut_pertama_itp_lolos][1])
                                    st.write(muhasabah_itp[urut_pertama_itp_lolos][2])
                                    st.write(muhasabah_itp[urut_pertama_itp_lolos][3])                                
                                elif "ITP Overall" in data[urut_pertama_itp_lolos]:
                                    st.write(muhasabah_itp[urut_pertama_itp_lolos][0])

                            #Display muhasabah TPA
                            if n_tpa and ("TPA" in ada_data[urut_pertama]):               
                                if"TPA" in data[urut_pertama_tpa_lolos]:
                                    st.write(muhasabah_tpa[urut_pertama_tpa_lolos][0])

                            #Display muhasabah GRE 
                            if gre and ("GRE" in ada_data[urut_pertama]):                                       
                                if"GRE Verbal Reasoning" in data[urut_pertama_gre_lolos]:
                                    st.write(muhasabah_gre[urut_pertama_gre_lolos][0])
                                    st.write(muhasabah_gre[urut_pertama_gre_lolos][1])
                                    st.write(muhasabah_gre[urut_pertama_gre_lolos][2])        

    ## 3. Inggris kurang, TPA Lolos                        
                    elif len(eng_lolos) == 0:

                        if urut_pertama_eng_kurang == "k1": #(1,1,G5,G8)
                            image = Image.open('cmu.png')
                        elif urut_pertama_eng_kurang == "k2":
                            image = Image.open('toronto.png')
                        elif urut_pertama_eng_kurang == 'k3':
                            image = Image.open('univ_edinburgh.png')
                        elif urut_pertama_eng_kurang == 'k4':
                            image = Image.open('univ_oxford.png')
                        elif urut_pertama_eng_kurang == 'k5':
                            image = Image.open('ntu.png')   
                        elif urut_pertama_eng_kurang == 'k6':
                            image = Image.open('yale.png')
                        elif urut_pertama_eng_kurang == 'k7':
                            image = Image.open('copenhagen.png')
                        elif urut_pertama_eng_kurang == 'k8':
                            image = Image.open('mbzuai.jpg')
                        elif urut_pertama_eng_kurang == 'k9':
                            image = Image.open('kaust.png')
                        elif urut_pertama_eng_kurang == 'k10':
                            image = Image.open('rmit.png')
                        elif urut_pertama_eng_kurang == 'k11':
                            image = Image.open('kfupm.png')
                        elif urut_pertama_eng_kurang == 'k12':
                            image = Image.open('groningen.png')
                        elif urut_pertama_eng_kurang == 'k13':
                            image = Image.open('ugm.png')
                        elif urut_pertama_eng_kurang == 'k14':
                            image = Image.open('itb.png')

                        st.image(image)

                        st.write(f"Agar kamu bisa tetap melanjutkan studi ke {nilai_urut_pertama_eng_kurang['solusi']}, kamu masih perlu meningkatkan nilai bahasa inggrismu agar mencapai persyaratan minimum, Semangat!! 🔥🔥")
                        with kol3:
                            st.success(f"Syarat masuk {data[urut_pertama_eng_kurang]['solusi']}")
                            st.write("IPK Minimum :", data[urut_pertama_eng_kurang]['IPK'])
                            #IELTS
                            if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(data[urut_pertama_eng_kurang]):  
                                st.write("IELTS Writing Minimum :", data[urut_pertama_eng_kurang]["IELTS Writing"])
                                st.write("IELTS Speaking Minimum :", data[urut_pertama_eng_kurang]["IELTS Speaking"])
                                st.write("IELTS Reading Minimum :", data[urut_pertama_eng_kurang]["IELTS Reading"])
                                st.write("IELTS Listening Minimum :", data[urut_pertama_eng_kurang]["IELTS Listening"])
                                st.write("IELTS Overall Minimum :", data[urut_pertama_eng_kurang]["IELTS Overall"])

                            elif "IELTS Overall" in data[urut_pertama_eng_kurang]:
                                st.write("IELTS Overall Minimum :", data[urut_pertama_eng_kurang]["IELTS Overall"])

                            #iBT
                            if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(data[urut_pertama_eng_kurang]):  
                                st.write("iBT Writing Minimum :", data[urut_pertama_eng_kurang]["iBT Writing"])
                                st.write("iBT Speaking Minimum :", data[urut_pertama_eng_kurang]["iBT Speaking"])
                                st.write("iBT Reading Minimum :", data[urut_pertama_eng_kurang]["iBT Reading"])
                                st.write("iBT Listening Minimum :", data[urut_pertama_eng_kurang]["iBT Listening"])
                                st.write("iBT Overall Minimum :", data[urut_pertama_eng_kurang]["iBT Overall"])

                            elif "iBT Overall" in data[urut_pertama_eng_kurang]:
                                st.write("iBT Overall Minimum :", data[urut_pertama_eng_kurang]["iBT Overall"])         

                            #Duolingo
                            if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(data[urut_pertama_eng_kurang]):  
                                st.write("D. Literacy Minimum :", data[urut_pertama_eng_kurang]["D. Literacy"])
                                st.write("D. Conversation Minimum :", data[urut_pertama_eng_kurang]["D. Conversation"])
                                st.write("D. Comprehension Minimum :", data[urut_pertama_eng_kurang]["D. Comprehension"])
                                st.write("D. Production Minimum :", data[urut_pertama_eng_kurang]["D. Production"])
                                st.write("D. Overall Minimum :", data[urut_pertama_eng_kurang]["D. Overall"])

                            elif "D. Overall" in data[urut_pertama_eng_kurang]:
                                st.write("D. Overall Minimum :", data[urut_pertama_eng_kurang]["D. Overall"])           

                            #ITP
                            if {"ITP Listening", "ITP Structure", "ITP Reading", "ITP Overall"}.issubset(data[urut_pertama]):  
                                st.write("ITP Listening Minimum :", data[urut_pertama_eng_kurang]["ITP Listening"])
                                st.write("ITP Structure Minimum :", data[urut_pertama_eng_kurang]["ITP Structure"])
                                st.write("ITP Reading Minimum :", data[urut_pertama_eng_kurang]["ITP Reading"])
                                st.write("ITP Overall Minimum :", data[urut_pertama_eng_kurang]["ITP Overall"])

                            elif "ITP Overall" in data[urut_pertama_eng_kurang]:
                                st.write("ITP Overall Minimum :", data[urut_pertama_eng_kurang]["ITP Overall"])         

                            #TPA
                            if "TPA" in ada_data[urut_pertama]:
                                if len(tpa_lolos) != 0:
                                    if {"TPA"}.issubset(data[urut_pertama_tpa_lolos]):  
                                        st.write("TPA Minimum :", data[urut_pertama_tpa_lolos]["TPA"])
                                elif len(tpa_lolos) == 0:
                                    if {"TPA"}.issubset(data[urut_pertama_tpa_kurang]):  
                                        st.write("TPA Minimum :", data[urut_pertama_tpa_kurang]["TPA"])

                            #GRE
                            if {"GRE Verbal Reasoning", "GRE Quantitative Reasoning", "GRE Analytical Writing"}.issubset(data[urut_pertama]):  
                                st.write("GRE Verbal Reasoning Minimum :", data[urut_pertama_eng_kurang]["GRE Verbal Reasoning"])
                                st.write("GRE Quantitative Reasoning Minimum :", data[urut_pertama_eng_kurang]["GRE Quantitative Reasoning"])
                                st.write("GRE Analytical Writing Minimum :", data[urut_pertama_eng_kurang]["GRE Analytical Writing"])

                            st.write(f"Preferensi yang ada di {data[urut_pertama_eng_kurang]['solusi']}", data[urut_pertama]['Pref'])

                        # Kondisi user alias kasus baru
                        with kol4:
                            st.success(f"Kondisi {nama}")
                            st.write("IPK = ", kasus['IPK'])

                            if ielts:
                                st.write("IELTS Writing =", kasus['IELTS Writing'])
                                st.write("IELTS Speaking =", kasus['IELTS Speaking'])
                                st.write("IELTS Reading =", kasus['IELTS Reading'])
                                st.write("IELTS Listening =", kasus['IELTS Listening'])
                                st.write("IELTS Overall =", kasus['IELTS Overall'])

                            if ibt:
                                st.write("iBT Writing =", kasus['iBT Writing'])
                                st.write("iBT Speaking =", kasus['iBT Speaking'])
                                st.write("iBT Reading =", kasus['iBT Reading'])
                                st.write("iBT Listening =", kasus['iBT Listening'])
                                st.write("iBT Overall =", kasus['iBT Overall'])         

                            if dlg:
                                st.write("Duolingo Literacy =", kasus['D. Literacy'])
                                st.write("Duoling Conversation =", kasus['D. Conversation'])
                                st.write("Duolingo Comprehension =", kasus['D. Comprehension'])
                                st.write("Duolingo Production =", kasus['D. Production'])
                                st.write("Duolingo Overall =", kasus['D. Overall'])  

                            if itp:
                                st.write("ITP Listening =", kasus['ITP Listening'])
                                st.write("ITP Structure =", kasus['ITP Structure'])
                                st.write("ITP Reading =", kasus['ITP Reading'])
                                st.write("ITP Overall =", kasus['ITP Overall'])    

                            if n_tpa:
                                st.write("TPA =", kasus['TPA'])   

                            if gre:
                                st.write("GRE Verbal Reasoning =", kasus['GRE Verbal Reasoning'])
                                st.write("GRE Quantitative Reasoning =", kasus['GRE Quantitative Reasoning'])
                                st.write("GRE Analytical Writing =", kasus['GRE Analytical Writing'])

                            st.write("Preferensi User =", kasus['Pref'])

                        with kol5:
                            st.success("Evaluasi Diri")
                            st.write(muhasabah_ipk[urut_pertama_eng_kurang][0])

                            # Display muhasabah ielts
                            if ielts and ("IELTS Overall" in ada_data[urut_pertama]):
                                if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(data[urut_pertama_eng_kurang]): 
                                    st.write(muhasabah_ielts[urut_pertama_eng_kurang][0])
                                    st.write(muhasabah_ielts[urut_pertama_eng_kurang][1])
                                    st.write(muhasabah_ielts[urut_pertama_eng_kurang][2])
                                    st.write(muhasabah_ielts[urut_pertama_eng_kurang][3])
                                    st.write(muhasabah_ielts[urut_pertama_eng_kurang][4])
                                elif "IELTS Overall" in data[urut_pertama_eng_kurang]:
                                    st.write(muhasabah_ielts[urut_pertama_eng_kurang][0])

                            #Display muhasabah iBT 
                            if ibt and ("iBT Overall" in ada_data[urut_pertama]):
                                if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(data[urut_pertama_eng_kurang]): 
                                    st.write(muhasabah_ibt[urut_pertama_eng_kurang][0])
                                    st.write(muhasabah_ibt[urut_pertama_eng_kurang][1])
                                    st.write(muhasabah_ibt[urut_pertama_eng_kurang][2])
                                    st.write(muhasabah_ibt[urut_pertama_eng_kurang][3])
                                    st.write(muhasabah_ibt[urut_pertama_eng_kurang][4])
                                elif "iBT Overall" in data[urut_pertama_eng_kurang]:
                                    st.write(muhasabah_ibt[urut_pertama_eng_kurang][0])                                             

                            #Display muhasabah Duolingo 
                            if dlg and ("Duolingo Overall" in ada_data[urut_pertama]):
                                if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(data[urut_pertama_eng_kurang]): 
                                    st.write(muhasabah_duolingo[urut_pertama_eng_kurang][0])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_kurang][1])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_kurang][2])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_kurang][3])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_kurang][4])
                                elif "D. Overall" in data[urut_pertama_eng_kurang]:
                                    st.write(muhasabah_duolingo[urut_pertama_eng_kurang][0])                                             

                            #Display muhasabah ITP  
                            if itp and ("ITP Overall" in ada_data[urut_pertama]):
                                if {"ITP Listening", "ITP Structure", "ITP Reading", "ITP Overall"}.issubset(data[urut_pertama_eng_kurang]):
                                    st.write(muhasabah_itp[urut_pertama_eng_kurang][0])
                                    st.write(muhasabah_itp[urut_pertama_eng_kurang][1])
                                    st.write(muhasabah_itp[urut_pertama_eng_kurang][2])                       
                                    st.write(muhasabah_itp[urut_pertama_eng_kurang][3])
                                elif "ITP Overall" in data[urut_pertama_eng_kurang]:
                                    st.write(muhasabah_itp[urut_pertama_eng_kurang][0])

                            #Display muhasabah TPA                                             
                            if "TPA" in ada_data[urut_pertama]:
                                if len(tpa_lolos) != 0:
                                    if "TPA" in data[urut_pertama_tpa_lolos]:
                                        st.write(muhasabah_tpa[urut_pertama_tpa_lolos][0])
                                if len(tpa_lolos) == 0:
                                    if {"TPA"}.issubset(data[urut_pertama_tpa_kurang]):  
                                        st.write(muhasabah_tpa[urut_pertama_tpa_kurang][0])

                            #Display muhasabah GRE                                                 
                            if "GRE Verbal Reasoning" in data[urut_pertama_eng_kurang]:
                                st.write(muhasabah_gre[urut_pertama_eng_kurang][0])
                                st.write(muhasabah_gre[urut_pertama_eng_kurang][1])
                                st.write(muhasabah_gre[urut_pertama_eng_kurang][2])

    ## 4. Inggris Lolos, TPA Kurang                        
                    elif len(eng_lolos) != 0: 

                        if urut_pertama_eng_lolos == "k1": #(1,1,G5,G8)
                            image = Image.open('cmu.png')
                        elif urut_pertama_eng_lolos == "k2":
                            image = Image.open('toronto.png')
                        elif urut_pertama_eng_lolos == 'k3':
                            image = Image.open('univ_edinburgh.png')
                        elif urut_pertama_eng_lolos == 'k4':
                            image = Image.open('univ_oxford.png')
                        elif urut_pertama_eng_lolos == 'k5':
                            image = Image.open('ntu.png')   
                        elif urut_pertama_eng_lolos == 'k6':
                            image = Image.open('yale.png')
                        elif urut_pertama_eng_lolos == 'k7':
                            image = Image.open('copenhagen.png')
                        elif urut_pertama_eng_lolos == 'k8':
                            image = Image.open('mbzuai.jpg')
                        elif urut_pertama_eng_lolos == 'k9':
                            image = Image.open('kaust.png')
                        elif urut_pertama_eng_lolos == 'k10':
                            image = Image.open('rmit.png')
                        elif urut_pertama_eng_lolos == 'k11':
                            image = Image.open('kfupm.png')
                        elif urut_pertama_eng_lolos == 'k12':
                            image = Image.open('groningen.png')
                        elif urut_pertama_eng_lolos == 'k13':
                            image = Image.open('ugm.png')
                        elif urut_pertama_eng_lolos == 'k14':
                            image = Image.open('itb.png')

                        st.image(image)

                        st.write(f"Agar kamu bisa tetap melanjutkan studi ke {nilai_urut_pertama_eng_lolos['solusi']}, kamu masih perlu meningkatkan nilai TPA-mu agar mencapai persyaratan minimum, Semangat!! 🔥🔥")
                        with kol3:
                            st.success(f"Syarat masuk {data[urut_pertama_eng_lolos]['solusi']}")
                            st.write("IPK Minimum :", data[urut_pertama_eng_lolos]['IPK'])
                            #IELTS
                            if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(data[urut_pertama_eng_lolos]):  
                                st.write("IELTS Writing Minimum :", data[urut_pertama_eng_lolos]["IELTS Writing"])
                                st.write("IELTS Speaking Minimum :", data[urut_pertama_eng_lolos]["IELTS Speaking"])
                                st.write("IELTS Reading Minimum :", data[urut_pertama_eng_lolos]["IELTS Reading"])
                                st.write("IELTS Listening Minimum :", data[urut_pertama_eng_lolos]["IELTS Listening"])
                                st.write("IELTS Overall Minimum :", data[urut_pertama_eng_lolos]["IELTS Overall"])

                            elif "IELTS Overall" in data[urut_pertama_eng_lolos]:
                                st.write("IELTS Overall Minimum :", data[urut_pertama_eng_lolos]["IELTS Overall"])

                            #iBT
                            if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(data[urut_pertama_eng_lolos]):  
                                st.write("iBT Writing Minimum :", data[urut_pertama_eng_lolos]["iBT Writing"])
                                st.write("iBT Speaking Minimum :", data[urut_pertama_eng_lolos]["iBT Speaking"])
                                st.write("iBT Reading Minimum :", data[urut_pertama_eng_lolos]["iBT Reading"])
                                st.write("iBT Listening Minimum :", data[urut_pertama_eng_lolos]["iBT Listening"])
                                st.write("iBT Overall Minimum :", data[urut_pertama_eng_lolos]["iBT Overall"])

                            elif "iBT Overall" in data[urut_pertama_eng_lolos]:
                                st.write("iBT Overall Minimum :", data[urut_pertama_eng_lolos]["iBT Overall"])         

                            #Duolingo
                            if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(data[urut_pertama_eng_lolos]):  
                                st.write("D. Literacy Minimum :", data[urut_pertama_eng_lolos]["D. Literacy"])
                                st.write("D. Conversation Minimum :", data[urut_pertama_eng_lolos]["D. Conversation"])
                                st.write("D. Comprehension Minimum :", data[urut_pertama_eng_lolos]["D. Comprehension"])
                                st.write("D. Production Minimum :", data[urut_pertama_eng_lolos]["D. Production"])
                                st.write("D. Overall Minimum :", data[urut_pertama_eng_lolos]["D. Overall"])

                            elif "D. Overall" in data[urut_pertama_eng_lolos]:
                                st.write("D. Overall Minimum :", data[urut_pertama_eng_lolos]["D. Overall"])           

                            #ITP
                            if {"ITP Listening", "ITP Structure", "ITP Reading", "ITP Overall"}.issubset(data[urut_pertama]):  
                                st.write("ITP Listening Minimum :", data[urut_pertama_eng_lolos]["ITP Listening"])
                                st.write("ITP Structure Minimum :", data[urut_pertama_eng_lolos]["ITP Structure"])
                                st.write("ITP Reading Minimum :", data[urut_pertama_eng_lolos]["ITP Reading"])
                                st.write("ITP Overall Minimum :", data[urut_pertama_eng_lolos]["ITP Overall"])

                            elif "ITP Overall" in data[urut_pertama_eng_lolos]:
                                st.write("ITP Overall Minimum :", data[urut_pertama_eng_lolos]["ITP Overall"])         

                            #TPA
                            if "TPA" in ada_data[urut_pertama]:
                                if len(tpa_lolos) == 0: 
                                    if {"TPA"}.issubset(data[urut_pertama_tpa_kurang]) :  
                                        st.write("TPA Minimum :", data[urut_pertama_tpa_kurang]["TPA"])  


                            #GRE
                            if {"GRE Verbal Reasoning", "GRE Quantitative Reasoning", "GRE Analytical Writing"}.issubset(data[urut_pertama]):  
                                st.write("GRE Verbal Reasoning Minimum :", data[urut_pertama_ielts_kurang]["GRE Verbal Reasoning"])
                                st.write("GRE Quantitative Reasoning Minimum :", data[urut_pertama_ielts_kurang]["GRE Quantitative Reasoning"])
                                st.write("GRE Analytical Writing Minimum :", data[urut_pertama_ielts_kurang]["GRE Analytical Writing"])

                            st.write(f"Preferensi yang ada di {data[urut_pertama_eng_lolos]['solusi']}", data[urut_pertama]['Pref'])

                        # Kondisi user alias kasus baru
                        with kol4:
                            st.success(f"Kondisi {nama}")
                            st.write("IPK = ", kasus['IPK'])

                            if ielts:
                                st.write("IELTS Writing =", kasus['IELTS Writing'])
                                st.write("IELTS Speaking =", kasus['IELTS Speaking'])
                                st.write("IELTS Reading =", kasus['IELTS Reading'])
                                st.write("IELTS Listening =", kasus['IELTS Listening'])
                                st.write("IELTS Overall =", kasus['IELTS Overall'])

                            if ibt:
                                st.write("iBT Writing =", kasus['iBT Writing'])
                                st.write("iBT Speaking =", kasus['iBT Speaking'])
                                st.write("iBT Reading =", kasus['iBT Reading'])
                                st.write("iBT Listening =", kasus['iBT Listening'])
                                st.write("iBT Overall =", kasus['iBT Overall'])         

                            if dlg:
                                st.write("Duolingo Literacy =", kasus['D. Literacy'])
                                st.write("Duoling Conversation =", kasus['D. Conversation'])
                                st.write("Duolingo Comprehension =", kasus['D. Comprehension'])
                                st.write("Duolingo Production =", kasus['D. Production'])
                                st.write("Duolingo Overall =", kasus['D. Overall'])  

                            if itp:
                                st.write("ITP Listening =", kasus['ITP Listening'])
                                st.write("ITP Structure =", kasus['ITP Structure'])
                                st.write("ITP Reading =", kasus['ITP Reading'])
                                st.write("ITP Overall =", kasus['ITP Overall'])    

                            if n_tpa:
                                st.write("TPA =", kasus['TPA'])   

                            if gre:
                                st.write("GRE Verbal Reasoning =", kasus['GRE Verbal Reasoning'])
                                st.write("GRE Quantitative Reasoning =", kasus['GRE Quantitative Reasoning'])
                                st.write("GRE Analytical Writing =", kasus['GRE Analytical Writing'])

                            st.write("Preferensi User =", kasus['Pref'])

                        with kol5:
                            st.success("Evaluasi Diri")
                            st.write(muhasabah_ipk[urut_pertama_eng_lolos][0])

                            # Display muhasabah ielts
                            if ielts and ("IELTS Overall" in ada_data[urut_pertama]):
                                if {"IELTS Writing", "IELTS Speaking", "IELTS Reading", "IELTS Listening", "IELTS Overall"}.issubset(data[urut_pertama_eng_lolos]): 
                                    st.write(muhasabah_ielts[urut_pertama_eng_lolos][0])
                                    st.write(muhasabah_ielts[urut_pertama_eng_lolos][1])
                                    st.write(muhasabah_ielts[urut_pertama_eng_lolos][2])
                                    st.write(muhasabah_ielts[urut_pertama_eng_lolos][3])
                                    st.write(muhasabah_ielts[urut_pertama_eng_lolos][4])
                                elif "IELTS Overall" in data[urut_pertama_eng_lolos]:
                                    st.write(muhasabah_ielts[urut_pertama_eng_lolos][0])

                            #Display muhasabah iBT      
                            if ibt and ("iBT Overall" in ada_data[urut_pertama]):
                                if {"iBT Writing", "iBT Speaking", "iBT Reading", "iBT Listening", "iBT Overall"}.issubset(data[urut_pertama_eng_lolos]): 
                                    st.write(muhasabah_ibt[urut_pertama_eng_lolos][0])
                                    st.write(muhasabah_ibt[urut_pertama_eng_lolos][1])
                                    st.write(muhasabah_ibt[urut_pertama_eng_lolos][2])
                                    st.write(muhasabah_ibt[urut_pertama_eng_lolos][3])
                                    st.write(muhasabah_ibt[urut_pertama_eng_lolos][4])
                                elif "iBT Overall" in data[urut_pertama_eng_lolos]:
                                    st.write(muhasabah_ibt[urut_pertama_eng_lolos][0])                                             

                            #Display muhasabah Duolingo     
                            if dlg and ("Duolingo Overall" in ada_data[urut_pertama]):
                                if {"D. Literacy", "D. Conversation", "D. Comprehension", "D. Production", "D. Overall"}.issubset(data[urut_pertama_eng_lolos]): 
                                    st.write(muhasabah_duolingo[urut_pertama_eng_lolos][0])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_lolos][1])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_lolos][2])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_lolos][3])
                                    st.write(muhasabah_duolingo[urut_pertama_eng_lolos][4])
                                elif "D. Overall" in data[urut_pertama_eng_lolos]:
                                    st.write(muhasabah_duolingo[urut_pertama_eng_lolos][0])                                             

                            #Display muhasabah ITP     
                            if itp and ("ITP Overall" in ada_data[urut_pertama]):
                                if {"ITP Listening", "ITP Structure", "ITP Reading", "ITP Overall"}.issubset(data[urut_pertama_eng_lolos]):
                                    st.write(muhasabah_itp[urut_pertama_eng_lolos][0])
                                    st.write(muhasabah_itp[urut_pertama_eng_lolos][1])
                                    st.write(muhasabah_itp[urut_pertama_eng_lolos][2])         
                                    st.write(muhasabah_itp[urut_pertama_eng_lolos][3])
                                elif "ITP Overall" in data[urut_pertama_eng_lolos]:
                                    st.write(muhasabah_itp[urut_pertama_eng_lolos][0])

                            #Display muhasabah TPA                                             
                            if "TPA" in ada_data[urut_pertama]:
                                if len(tpa_lolos) == 0: 
                                    if "TPA" in data[urut_pertama_tpa_kurang]:
                                        st.write(muhasabah_tpa[urut_pertama_tpa_kurang][0])

                            #Display muhasabah GRE                                                 
                            if "GRE Verbal Reasoning" in data[urut_pertama_eng_lolos]:
                                st.write(muhasabah_gre[urut_pertama_eng_lolos][0])
                                st.write(muhasabah_gre[urut_pertama_eng_lolos][1])
                                st.write(muhasabah_gre[urut_pertama_eng_lolos][2])             


                with kol2:
                    # munculin logo univ
                    if len(lolos) == 0:
                        st.image(Image.open('sad.gif'))
                        st.write("Maaf kamu tidak memenuhi standar kampus manapun di basis data kami")
                        #st.write(f"Tapi jangan khawatir.. berdasarkan hasil kalkulasi, kamu masih berpeluang untuk diterima di {nilai_urut_pertama_tidak_lolos['solusi']} 😃")
                    else:
                        if urut_pertama_lolos == "k1": #(1,1,G5,G8)
                            image = Image.open('cmu.png')
                        elif urut_pertama_lolos == "k2":
                            image = Image.open('toronto.png')
                        elif urut_pertama_lolos == 'k3':
                            image = Image.open('univ_edinburgh.png')
                        elif urut_pertama_lolos == 'k4':
                            image = Image.open('univ_oxford.png')
                        elif urut_pertama_lolos == 'k5':
                            image = Image.open('ntu.png')   
                        elif urut_pertama_lolos == 'k6':
                            image = Image.open('yale.png')
                        elif urut_pertama_lolos == 'k7':
                            image = Image.open('copenhagen.png')
                        elif urut_pertama_lolos == 'k8':
                            image = Image.open('mbzuai.jpg')
                        elif urut_pertama_lolos == 'k9':
                            image = Image.open('kaust.png')
                        elif urut_pertama_lolos == 'k10':
                            image = Image.open('rmit.png')
                        elif urut_pertama_lolos == 'k11':
                            image = Image.open('kfupm.png')
                        elif urut_pertama_lolos == 'k12':
                            image = Image.open('groningen.png')
                        elif urut_pertama_lolos == 'k13':
                            image = Image.open('ugm.png')
                        elif urut_pertama_lolos == 'k14':
                            image = Image.open('itb.png')

                        st.image(image, caption = f"Selamat {nama}, Kamu cocok disini! 🎉") 

                        # printing initial key
                        st.write("Kasus baru ini mirip dengan kasus : " + str(urut_pertama_lolos))
                        st.success(" dengan similaritas: " + str(nilai_urut_pertama_lolos['similaritas']))


                with kol6:
                    st.success("Urutan database")
                    st.write("berdasarkan ranking Universitas 🎓🥇")
                    st.write(rank)
                with kol7:
                    st.success("Urutan hasil kalkulasi")
                    st.write("berdasarkan similaritas 🌟⭐=💯")
                    st.write(urut)
                    
                with kol8:
                    st.success("Tidak lolos... 😭")
                    st.write(f"{nama} lolos persyaratan minimum di :")
                    st.write(lolos)
                with kol9:
                    st.success("Tidak lolos... 😭")
                    st.write(f"{nama} tidak lolos persyaratan minimum di :")
                    st.write(tidak_lolos)
            
                with kol10:
                    st.success("Cocok dengan database ✅")
                    st.write("Data baru cocok dengan basis data:", ada_data)
                with kol11:
                    st.success("Tidak cocok dengan database ❌")
                    st.write("Data baru tidak cocok dengan basis data:", no_data)
                
        else:
            with kol2:
                st.success("Mohon maaf, Kasus tidak ada yang cocok dengan seluruh basis data kami")

