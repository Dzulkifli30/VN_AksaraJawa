# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
image dora:
    "dora.png"
    zoom 0.5
image rakyat:
    "rakyat.png"
    zoom 0.3
image ajisaka sedih:
    "ajisaka sedih.png"
    zoom 1.2

# Deklarasikan karakter yang digunakan di game.

default Ajisaka = Character('Ajisaka', color="#8BF5FA")
default Rakyat = Character('Rakyat', color="#F8FFDB")
default Sembodo = Character('Sembodo', color="#16FF00")
default Dora = Character('Dora', color="#FBFF00")
label splashscreen:
    scene black
    with Pause(0.5)

    show text "Kelompok 5" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(0.5)

    return

# Game dimulai disini.
label start:
    # scene bg grey
    # show kaktus
    "Pada Zaman dahulu"
    scene bg gunung
    "Di Gunung Semeru ada sebuah padepokan atau pertapaan yang didiami oleh Ajisaka dengan dua orang pengikut setianya, yaitu Dora dan Sembodo"

label scene2:

    show rakyat at left
    # with dissolve
    Rakyat "Wahai Ajisaka, kehidupan masyarakat di kerajaan sedang tidak baik baik saja, banyak ancaman yang terjadi, Raja menyantap dan merninum darah rakyatnya sendiri. Satu per satu rakyat kerajaan Medang Kamulan dibawa ke istana untuk dijadikan santapan."
    Rakyat "Tolong lah aku dan keluargaku wahai Ajisaka"
    hide rakyat

label scene3:
    show ajisaka sedih
    "Ajisaka merasa resah dan bersalah mendengarkan penderitaan rakyat Medang Kamulan yang terancam dan teraniaya oleh rajanya"

    # show Ajisaka
    Ajisaka "Aku merasa bersalah, aku harus melakukan sesuatu"

label scene4:

    show Ajisaka at left
    Ajisaka "Dora dan Sembodo, aku harus segera turun gunung untuk membantu rakyat Medang Kamulan membebaskan diri dari rajanya yang zalim"

    Sembodo "Bagaimana dengan hamba berdua, Tuan?"

    Ajisaka "Saya tidak mungkin mengajak kalian berdua karena harus ada yang menjaga padepokan ini"

    Dora "Hamba menurut saja, Tuan"

menu:
    "Siapa yang akan kamu ajak?"

    "Ajak Mereka Berdua":
        jump scene4_1
    "Ajak Dora saja":
        jump scene4_2
    
label scene4_1:
    Ajisaka "Baiklah, kalian berdua ikut dengan ku"
    
    Sembodo "Lalu bagaimana pedepokan Tuan?"
    
    Ajisaka "Iya Juga, Aku khawatir jika tidak ada yang menjaga pedepokan, kalau begitu Dora ikut denganku, sedangkan kau Sembodo tetap di padepokan untuk menjaga pusaka"
    jump scene4_end

label scene4_2:
    Ajisaka "Baiklah, kalau begitu Dora ikut denganku, sedangkan kau Sembodo tetap di padepokan untuk menjaga pusaka"

    Sembodo "Baik, Tuan"
    jump scene4_end

label scene4_end:
    Ajisaka "tugasmu adalah menjaga padepokan dan senjata. Jangan sekali-sekali engkau meninggalkan padepokan ini dan jangan sekali-kali kau berikan pusaka ini kepada orang lain selain aku. Apakah kamu mengerti?"

    Sembodo "Mengerti, segala perintah Tuan, akan hamba laksanakan"

    Ajisaka "Baiklah, kalau begitu. Jagalah dirimu baik-baik dan ingat-ingat pesanku"

label scene5:
    Ajisaka "Mari kita berangkat ,Dora"

    Dora "Baik, Tuan"

label scene6:
    "Mereka menempuh petjalanan yang cukup berat melewati hutan belantara. Sesekali Dora mendahului tuannya untuk membuat jalan dengan cara membabat belukar atau menyingkirkan pohon yang tumbang. "

label scene7:
    Ajisaka "Kita perlu beristirahat Dora, kau juga terlihat lelah"

    Dora "Baik, Tuan"

    Ajisaka "Astaga, harusnya aku membawa pusaka karena pusaka itu akan sangat membantuku untuk menghadapi kesaktian Prabu 29 Dewata Cengkar"

    Dora "Lalu, Bagaimana Tuan? Apakah hamba hams kembali ke padepokan?"

    Ajisaka "Ya, kau, kembalilah ke padepokan dan mintalah pusaka itu pada Sembodo. In gat, jangan sekali-kali kau kembali ke sini sebelum membawa pusaka itu"

    Dora "Baiklah, hamba berjanji"

label scene8:
    "Dora Kembali ke pedepokan dengan kondisi lelah"

menu:
    # "Say Statement"
    "Lanjutkan Perjalanan":
        jump scene8_1
    "Istirahat Sebentar":
        jump scene8_2
    
label scene8_1:
    Dora "aku harus kembali melakukan perjalanan, nanti tuan akan menunggu ku sangat lama, aku tidak boleh melanjutkan isitirahat,"
    jump scene9

label scene8_2:

    Dora "Aku lelah, aku butuh istirahat"
    Dora "namun kasian ajisaka, ia bisa menunggu ku terlalu lama jika aku beristirahat"
    jump scene9
    
label scene9:
    Dora "Aku kembali karena junjungan kita Ajisaka menyuruhku mengambil tombak pusaka Kiai Konang darimu"

    Sembodo "Apa katamu?"
    Sembodo "Tidak bisa. Aku diperintah untuk menjaga tombak inj dan tidak memberikrumya kepada siapa pun"

    Dora "Tapi, junjungan kita sangat membutuhkan tombak itu untuk melawan Dewata Cengkar."
    Dora "Aku tidak boleh kembali tanpa pusaka itu"

    Sembodo "Aku tidak bisa. Aku sudah berjanji akan menjaga tombak ini"

    Dora "Aku juga sudah berjanji akan segera membawa tombak ini."
    Dora "Kamu harus menyerahkan tombak Kiai Konang. bu perintah"

    Sembodo "Jangan harap kau bisa mengambilnya dariku."
    Sembodo "Kalau aku menyerahkannya padamu, berarti aku tidak setia pada junjunganku"

label scene10:
    
    "Terjadi perang saudara antara sembodo dan dora"

label scene11:
    "Diperjalanan"
    "Ajisaka Khawatir karena dora tak kunjung kembali"

menu:
    "Tetap Menunggu":
        jump scene11_1
    "Menyusul Dora":
        jump scene11_2
    "Tinggalkan Dora":
        jump scene11_3

label scene11_1:

    Ajisaka "Dora sudah lama tidak kembali. aku harus lebih sabar menunggu nya"
    Ajisaka "tetapi ini sudah terlalu lama, aku sungguh khawatir"
    Ajisaka "aku sungguh gelisah, aku takut terjadi apa apa, aku harus kembali"
    jump scene12

label scene11_2:
    Ajisaka "Dora sudah lama tidak kembali."
    Ajisaka "Menurut perhitunganku seharusnya Dora sudah sampai."
    Ajisaka "aku sungguh gelisah, aku takut terjadi apa apa, aku harus kembali"
    jump scene12

label scene11_3:

    Ajisaka "dora terlalu lama, jika menunggu nya, kasian rakyat kerajaan medang kamulan, aku harus berangkat sendiri, biarkan dora menyusul nanti"
    Ajisaka "tetapi, jika aku nekat berangkat sendiri, tanpa dora dan tanpa pusaka, aku akan kewalahan menghadapi raja kerajaan medang"
    Ajisaka "aku sungguh gelisah, aku takut terjadi apa apa, aku harus kembali"
    jump scene12

label scene12:

    Ajisaka "Ada apa ini, mengapa padepokan ku seperti telah terjadi pertempuran hebat"

    Ajisaka "DORA! SEMBODO!"

    Ajisaka "Astaga, apa yang terjadi dengan kalian, ini salahku, aku yakin pesanku yang berbeda membuat keduanya bertengkar."

label scene13:

    "Ajisaka merasa sangat bersalah. Ia duduk termenung memandangi mayat dua punakawannya yang sangat setia itu."
    "Ia menyadari dan menyesali diri bahwa kematian dua punakawannya itu adalah kesalahannya karena telah memberi perintah dan pesan yang bertentangan."
    "Untuk mengabadikan kesetiaan kedua punakawannya, Ajisaka menciptakan aksara Jawa yang mengisahkan peristiwa tersebut."
    " Ha na ca ra ka :ana utusan (ada utusan) Data sa wa la : pada perang tanding (saling berkelahi) Pa dha ja ya nya : padha-padha sektine (sama-sama saktinya) Ma ga ba tha nga : padha dadi bathange (sama-sama gugur)"  
    
    return
