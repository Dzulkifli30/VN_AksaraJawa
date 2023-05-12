# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
# image bg blck = "images/blck.png"
# image kaktus = "images/kaktus.png"

# Deklarasikan karakter yang digunakan di game.

default Ajisaka = Character('Ajisaka', color="#8BF5FA")
default Prajurit = Character('Prajurit', color="#F8FFDB")
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
    # show kaktus
    "Pada Zaman dahulu"
    "Di Gunung Semeru ada sebuah padepokan atau pertapaan yang didiami oleh Ajisaka dengan dua orang pengikut setianya, yaitu Dora dan Sembodo"

label scene2:
    Prajurit "Wahai Ajisaka, kehidupan masyarakat di kerajaan sedang tidak baik baik saja, banyak ancaman yang terjadi, Raja menyantap dan merninum darah rakyatnya sendiri. Satu per satu rakyat kerajaan Medang Kamulan dibawa ke istana untuk dijadikan santapan"

label scene3:
    "Ajisaka merasa resah dan bersalah mendengarkan penderitaan rakyat Medang Kamulan yang terancam dan teraniaya oleh rajanya"

label scene4:
    Ajisaka "Dora dan Sembodo, aku harus segera tunm gunung untuk membantu rakyat Medang Kamulan membebaskan diri dari rajanya yang zalim"

    Sembodo "Bagaimana dengan hamba berdua, Tuan?"

    Ajisaka "Saya tidak mungkin mengajak kalian berdua karena harus ada yang menjaga padepokan ini"

    Dora "Hamba menurut saja, Tuan"

    Ajisaka "Baiklah, kalau begitu Dora ikut denganku, sedangkan kau Sembodo tetap di padepokan untuk menjaga pusaka"

    Sembodo "Baik, Tuan"

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

    Ajisaka "Astaga, harusnya aku membawa pusaka karena pusaka itu akan sangat membantu kuuntuk menghadapi kesaktian Prabu 29 Dewata Cengkar"

    Dora "Lalu, Bagaimana Tuan? Apakah hamba hams kembali ke padepokan?"

    Ajisaka "Ya, kau, kembalilah ke padepokan dan mintalah pusaka itu pada Sembodo. In gat, jangan sekali-kali kau kembali ke sini sebelum membawa pusaka itu"

    Dora "Baiklah, hamba berjanji"

label scene8:
    "Dora Kembali ke pedepokan dengan kondisi lelah"
    
label scene9:
    Dora "Aim kembali karena junjungan kita Ajisaka menyuruhku mengambil tombak pusaka Kiai Konang darimu"

    Sembodo "Apa kata.mu? Tidak bisa. Aku diperintah untuk menjaga tombak inj dan tidak memberikrumya kepada siapa pun"

    Dora "Tapi, junjungan kita sru1gat membutuhkan tombak itu untuk melawru1 Dewata Cengkar. Aku tidak boleh kembali tru1pa pusaka itu"

    Sembodo "Aim tidak bisa. Aim sudah berjanji akan menjaga tombak ini"

    Dora "Aku juga sudah berjanji akru1 segera membawa tombak ini. Kamu harus menyerahkan tombak Kiai Konang. bu perintah"

    Sembodo "Jangan harap kau bisa mengrunbilnya dariku. Kalau aku menyerahkrumya padamu, berarti aku tidak setia pada junjunganku"

label scene10:
    
    "Terjadi perang saudara antara sembodo dan dora"

label scene11:

    Ajisaka "Dora sudah lama tidak kembali. Menurut perhitunganku seharusnya Dora sudah sampai. aku sungguh gelisah, aku takut terjadi apa apa, aku harus kembali "

label scene12:

    Ajisaka "Ada apa ini, mengapa padepokan ku seperti telah terjadi pertempuran hebat"

    Ajisaka "DORA! SEMBODO!"

    Ajisaka "Astaga, apa yang terjadi dengan kalian, ini salahku, aku yakin pesanku yang berbeda membuat keduanya bertengkar."

label scene13:

    "Ajisaka merasa sangat bersalah. Ia duduk termenung memandangi mayat dua punakawannya yang sangat setia itu. Ia menyadari dan menyesali diri bahwa kematian dua punakawannya itu adalah kesalahannya karena telah memberi perintah dan pesan yang bertentangan.  "
    "Untuk mengabadikan kesetiaan kedua punakawannya, Ajisaka menciptakan aksara Jawa yang mengisahkan peristiwa tersebut. Ha na ca ra ka :ana utusan (ada utusan) Data sa wa la : pada perang tanding (saling berkelahi) Pa dha ja ya nya : padha-padha sektine (sama-sama saktinya) Ma ga ba tha nga : padha dadi bathange (sama-sama gugur) "  
    
    return
