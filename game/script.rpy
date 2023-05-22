# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
image rakyat:
    "rakyat.png"
    zoom 0.3
image rakyat sedih:
    "rakyat sedih.png"
    zoom 0.3
image ajisaka sedih:
    "ajisaka sedih.png"
    zoom 1.7
image ajisaka biasa:
    "ajisaka biasa.png"
    zoom 1.7
image ajisaka resah:
    "ajisaka resah.png"
    zoom 1.5
image ajisaka:
    "ajisaka.png"
    zoom 1.8
image sembodo:
    "sembodo.png"
    zoom 0.7
image sembodo marah:
    "sembodo marah.png"
    zoom 1.28
image sembodo kiri:
    "sembodo kiri.png"
    zoom 0.7
image dora:
    "dora.png"
    zoom 1.45
image dora marah:
    "dora marah.png"
    zoom 1.45

# Deklarasikan karakter yang digunakan di game.

default Ajisaka = Character('Ajisaka', color="#8BF5FA")
default Rakyat = Character('Rakyat', color="#F8FFDB")
default Sembodo = Character('Sembodo', color="#16FF00")
default Dora = Character('Dora', color="#FBFF00")
label splashscreen:
    $ renpy.movie_cutscene('images/opening.webm')

    return

# Game dimulai disini.
label start:
    stop music fadeout 1.0
    # scene bg grey
    # show kaktus
    play music "audio/awalan.mp3" fadein 1.0 volume 0.5
    "Pada Zaman dahulu"
    scene bg gunung
    with fade
    "Di Gunung Semeru ada sebuah padepokan atau pertapaan yang didiami oleh Ajisaka dengan dua orang pengikut setianya, yaitu Dora dan Sembodo"

label scene2:

    show rakyat
    with dissolve
    show rakyat sedih:
        ease 0.5 zoom 1.2
    Rakyat "Wahai Ajisaka, kehidupan masyarakat di kerajaan sedang tidak baik-baik saja, banyak ancaman yang terjadi, Raja menyantap dan meninum darah rakyatnya sendiri. Satu persatu rakyat kerajaan Medang Kamulan dibawa ke istana untuk dijadikan santapan."
    Rakyat "Tolonglah aku dan keluargaku wahai Ajisaka"
    show rakyat sedih:
        ease 0.5 zoom 1
    hide rakyat

label scene3:
    scene padepokan
    with fade
    show ajisaka biasa
    "Ajisaka merasa resah dan bersalah mendengarkan penderitaan rakyat Medang Kamulan yang terancam dan teraniaya oleh rajanya"

    # show Ajisaka
    Ajisaka "Aku merasa bersalah, aku harus melakukan sesuatu"
    hide ajisaka biasa with dissolve

label scene4:

    show ajisaka at left
    show sembodo at right
    show dora
    show ajisaka:
        ease 0.5 zoom 1.2
    Ajisaka "Dora dan Sembodo, aku harus segera turun gunung untuk membantu rakyat Medang Kamulan membebaskan diri dari rajanya yang zalim"
    show ajisaka:
        ease 0.5 zoom 1
    show sembodo:
        ease 0.5 zoom 1.2
    Sembodo "Bagaimana dengan Hamba berdua, Tuan?"
    show sembodo:
        ease 0.5 zoom 1
    show ajisaka:
        ease 0.5 zoom 1.2
    Ajisaka "Saya tidak mungkin mengajak kalian berdua karena harus ada yang menjaga padepokan ini"
    show ajisaka:
        ease 0.5 zoom 1
    show dora:
        ease 0.5 zoom 1.2
    Dora "Hamba menurut saja, Tuan"
    show dora:
        ease 0.5 zoom 1
    hide sembodo
    hide dora
    show ajisaka

menu:
    "Siapa yang akan kamu ajak?"
    
    "Ajak Mereka Berdua":
        jump scene4_1
    "Ajak Dora saja":
        jump scene4_2
    
label scene4_1:
    show ajisaka:
        ease 0.5 zoom 1.2
    Ajisaka "Baiklah, kalian berdua ikut dengan ku"
    show ajisaka:
        ease 0.5 zoom 1
    show sembodo at right
    show sembodo:
        ease 0.5 zoom 1.2
    Sembodo "Lalu bagaimana dengan Padepokan Tuan?"
    show sembodo:
        ease 0.5 zoom 1
    show ajisaka:
        ease 0.5 zoom 1.2
    Ajisaka "Iya Juga, Aku khawatir jika tidak ada yang menjaga padepokan, kalau begitu Dora ikut denganku, sedangkan kau Sembodo tetap di padepokan untuk menjaga pusaka"
    show ajisaka:
        ease 0.5 zoom 1
    jump scene4_end

label scene4_2:
    show ajisaka:
        ease 0.5 zoom 1.2
    Ajisaka "Baiklah, kalau begitu Dora ikut denganku, sedangkan kau Sembodo tetap di padepokan untuk menjaga pusaka"
    show ajisaka:
        ease 0.5 zoom 1
    show sembodo at right:
        ease 0.5 zoom 1.2
    Sembodo "Baik, Tuan"
    show sembodo:
        ease 0.5 zoom 1
    jump scene4_end

label scene4_end:
    show ajisaka:
        ease 0.5 zoom 1.2
    Ajisaka "tugasmu adalah menjaga padepokan dan pusaka. Jangan sekali-sekali engkau meninggalkan padepokan ini dan jangan sekali-kali kau berikan pusaka ini kepada orang lain selain aku. Apakah kamu mengerti?"
    show ajisaka:
        ease 0.5 zoom 1
    show sembodo:
        ease 0.5 zoom 1.2
    Sembodo "Mengerti, segala perintah Tuan, akan hamba laksanakan"
    show sembodo:
        ease 0.5 zoom 1
    show ajisaka:
        ease 0.5 zoom 1.2
    Ajisaka "Baiklah, kalau begitu. Jagalah dirimu baik-baik dan ingatlah pesan-pesanku"
    show ajisaka:
        ease 0.5 zoom 1
    stop music fadeout 0.5
    
label scene5:
    scene padepokan
    with fade
    show ajisaka at left:
        ease 0.5 zoom 1.2
    Ajisaka "Mari kita berangkat, Dora"
    show ajisaka:
        ease 0.5 zoom 1
    show dora at right:
        ease 0.5 zoom 1.2
    Dora "Baik, Tuan"
    show dora:
        ease 0.5 zoom 1

label scene6:
    scene bg hutan
    with fade
    play music "audio/hutan.mp3" fadein 1.0 volume 0.5
    play sound "audio/burung.mp3"
    "Mereka menempuh perjalanan yang cukup berat melewati hutan belantara. Sesekali Dora mendahului tuannya untuk membuat jalan dengan cara membabat belukar atau menyingkirkan pohon yang tumbang. "

label scene7:
    show ajisaka at left:
        ease 0.5 zoom 1.2
    Ajisaka "Kita perlu beristirahat Dora, kau juga terlihat lelah"
    show ajisaka:
        ease 0.5 zoom 1
    show dora at right:
        ease 0.5 zoom 1.2
    Dora "Baik, Tuan"
    show dora:
        ease 0.5 zoom 1
    scene gua widodaren
    with fade
    show ajisaka at left:
        ease 0.5 zoom 1.2
    Ajisaka "Astaga, harusnya aku membawa pusaka karena pusaka itu akan sangat membantuku untuk menghadapi kesaktian Raja Dewata Cengkar"
    show ajisaka:
        ease 0.5 zoom 1
    show dora:
        ease 0.5 zoom 1.2
    Dora "Lalu, Bagaimana Tuan? Apakah hamba harus kembali ke padepokan?"
    show dora:
        ease 0.5 zoom 1
    show ajisaka:
        ease 0.5 zoom 1.2
    Ajisaka "Kembalilah kau ke padepokan dan mintalah pusaka itu pada Sembodo! Ingat, jangan sekali-kali kau kembali ke sini sebelum membawa pusaka itu!"
    show ajisaka:
        ease 0.5 zoom 1
    show dora:
        ease 0.5 zoom 1.2
    Dora "Baiklah, hamba berjanji"
    show dora:
        ease 0.5 zoom 1
    stop music fadeout 1.0

label scene8:
    scene bg malam hutan
    with fade
    show dora at center
    "Dora Kembali ke padepokan dengan kondisi lelah"

menu:
    # "Say Statement"
    "Lanjutkan Perjalanan":
        jump scene8_1
    "Istirahat Sebentar":
        jump scene8_2
    
label scene8_1:
    show dora
    Dora "Aku harus kembali melakukan perjalanan, nanti Tuan akan menungguku sangat lama. Aku tidak boleh melanjutkan isitirahat."
    jump scene9

label scene8_2:

    Dora "Aku lelah, aku butuh istirahat"
    show dora
    Dora "Namun, bila aku istirahat Tuan Ajisaka akan menungguku terlalu lama"
    jump scene9
    
label scene9:
    scene padepokan
    with fade
    show dora at right:
        ease 0.5 zoom 1.2
    Dora "Aku kembali karena Tuan kita Ajisaka menyuruhku mengambil pusaka Kiai Konang darimu"
    show dora:
        ease 0.5 zoom 1
    show sembodo kiri at left:
        ease 0.5 zoom 1.2
    Sembodo "Apa katamu?"
    Sembodo "Tidak bisa. Aku diperintah untuk menjaga pusaka ini dan tidak memberikannya kepada siapa pun"
    show sembodo kiri:
        ease 0.5 zoom 1
    play music "audio/tegang.mp3" fadein 1.0 volume 0.5
    show dora marah:
        ease 0.5 zoom 1.2
    Dora "Tapi, Tuan kita sangat membutuhkan pusaka itu untuk melawan Raja Dewata Cengkar."
    Dora "Aku tidak boleh kembali tanpa pusaka itu"
    show dora marah:
        ease 0.5 zoom 1
    show sembodo marah:
        ease 0.5 zoom 1.2
    Sembodo "Aku tidak bisa. Aku sudah berjanji akan menjaga pusaka ini"
    show sembodo marah:
        ease 0.5 zoom 1
    show dora marah:
        ease 0.5 zoom 1.2
    Dora "Aku juga sudah berjanji akan segera membawa pusaka ini."
    Dora "Kamu harus menyerahkan pusaka Kiai Konang! Ini perintah!"
    show dora marah:
        ease 0.5 zoom 1
    show sembodo marah:
        ease 0.5 zoom 1.2
    Sembodo "Jangan harap kau bisa mengambilnya dariku."
    Sembodo "Kalau aku menyerahkannya padamu, berarti aku tidak setia kepada Tuan ku"
    show sembodo marah:
        ease 0.5 zoom 1
    stop music fadeout 0.5
label scene10:
    scene black
    play sound "audio/pedang.mp3"
    "Terjadi perang saudara antara Sembodo dan Dora"

label scene11:
    scene Gua widodaren
    with fade
    "Di Hutan"
    show ajisaka biasa at center
    "Ajisaka Khawatir karena Dora tak kunjung kembali."

menu:
    "Tetap Menunggu":
        jump scene11_1
    "Menyusul Dora":
        jump scene11_2
    "Tinggalkan Dora":
        jump scene11_3

label scene11_1:
    show ajisaka at center
    with dissolve
    Ajisaka "Dora sudah lama tidak kembali. Aku harus lebih sabar menunggu nya"
    show ajisaka resah at center
    with dissolve
    Ajisaka "Tetapi ini sudah terlalu lama, aku sungguh khawatir"
    Ajisaka "Aku sungguh gelisah, aku takut terjadi apa-apa, aku harus kembali"
    jump scene12

label scene11_2:
    show ajisaka resah at center
    with dissolve
    Ajisaka "Dora sudah lama tidak kembali."
    Ajisaka "Menurut perhitunganku seharusnya Dora sudah sampai."
    Ajisaka "Aku sungguh gelisah, aku takut terjadi apa apa, aku harus kembali"
    jump scene12

label scene11_3:
    show ajisaka at center
    with dissolve
    Ajisaka "Dora terlalu lama, jika menunggu nya, kasian rakyat kerajaan Medang Kamulan, aku harus berangkat sendiri, biarkan Dora menyusul nanti"
    Ajisaka "Tetapi, jika aku nekat berangkat sendiri, tanpa Dora dan tanpa pusaka, aku akan kewalahan menghadapi Raja Dewata Cengkar"
    show ajisaka resah at center
    with dissolve
    Ajisaka "Aku sungguh gelisah, aku takut terjadi apa-apa, aku harus kembali."
    jump scene12

label scene12:
    scene padepokan rusak
    with fade
    show ajisaka
    Ajisaka "Ada apa ini, mengapa padepokan ku seperti telah terjadi pertempuran hebat."
    show ajisaka sedih
    with dissolve

    Ajisaka "DORA! SEMBODO!"

    Ajisaka "Astaga, apa yang terjadi dengan kalian?"
    Ajisaka "Ini salahku, aku yakin pesanku yang berbeda membuat keduanya bertengkar."

label scene13:
    scene kuburan
    with fade
    "Ajisaka merasa sangat bersalah. Ia duduk termenung memandangi mayat dua pengikutnya yang sangat setia."
    "Ia sadar dan menyesal bahwa kematian dua pengikut itu adalah kesalahannya karena telah memberi perintah dan pesan yang bertentangan."
    "Untuk mengabadikan kesetiaan kedua pengikutnya, Ajisaka menciptakan Aksara Jawa yang mengisahkan peristiwa tersebut."
    " Ha na ca ra ka :ana utusan (ada utusan)"
    " Data sa wa la : pada perang tanding (saling berkelahi)"
    " Pa dha ja ya nya : padha-padha sektine (sama-sama saktinya)"
    " Ma ga ba tha nga : padha dadi bathange (sama-sama gugur)"

label tamat:
    scene black
    with Pause(0.5)
    
    show text "Tamat" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    return
