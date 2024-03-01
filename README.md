# Laporan Proyek Machine Learning - Hangga Bayu Krisna
**Topik dari proyek ini adalah Drug Recommendation using Content Based Filtering** untuk memenuhi submission dicoding

## DOMAIN PROYEK
### Latar Belakang
Di era modern ini, masalah kesehatan menjadi perhatian utama bagi masyarakat. Penyakit dan kondisi kesehatan dapat memengaruhi kualitas hidup seseorang secara signifikan. Salah satu aspek penting dalam upaya penyembuhan adalah pemilihan obat yang tepat sesuai dengan kondisi kesehatan yang dialami oleh pasien. Namun, dalam banyak kasus, proses pemilihan obat ini dapat menjadi kompleks dan memerlukan pengetahuan medis yang mendalam.

Dalam konteks ini, penggunaan teknologi dapat memberikan solusi yang efektif. Salah satu pendekatan yang dapat diterapkan adalah Content Based Filtering (CBF) dalam sistem rekomendasi obat. CBF merupakan metode yang berfokus pada karakteristik dan konten dari item yang direkomendasikan. Dalam konteks ini, konten yang dimaksud adalah kondisi kesehatan atau penyakit yang dialami oleh pasien.

Pemilihan obat yang tepat berdasarkan kondisi kesehatan dapat membantu meningkatkan efektivitas pengobatan dan mengurangi risiko efek samping yang tidak diinginkan. Dengan adanya sistem rekomendasi obat berbasis konten, diharapkan dapat memudahkan para profesional kesehatan maupun pasien dalam menemukan obat yang sesuai dengan kondisi spesifik yang dihadapi.

Sistem rekomendasi obat berbasis konten diharapkan secara signifikan memenuhi kebutuhan konkret dalam dunia kesehatan dengan menyediakan rekomendasi obat yang dipersonalisasi berdasarkan karakteristik individu pasien, riwayat penyakit, dan respon terhadap pengobatan sebelumnya. Sistem rekomendasi ini dapat berkontribusi pada peningkatan efisiensi dan efektivitas dalam manajemen kesehatan.

Catatan: Berdasarkan dari sumber dataset,  jenis data dan solusi rekomendasi yang diberikan oleh dataset ini semata-mata untuk tujuan pembelajaran Sistem Rekomendasi. Dataset tidak cocok untuk solusi rekomendasi obat di dunia nyata.

## BUSINESS UNDERSTANDING

Implementasi sistem rekomendasi obat berbasis konten dapat memberikan dampak ekonomi positif dengan mengurangi biaya perawatan jangka panjang melalui personalisasi pengobatan. Solusi ini juga dapat memberikan kontrol lebih atas kondisi kesehatan, dan memperbaiki interaksi pasien-dokter. Tantangan utama melibatkan integrasi dengan sistem kesehatan yang ada, perlindungan data pribadi, serta penerimaan dan adaptasi dari penyedia layanan kesehatan dan pasien terhadap pendekatan personalisasi.

### Problem Statements
Permasalahan yang diselesaikan oleh proyek ini adalah:

- Bagaimana _machine learning_ memahami kompleksitas data untuk membantu proses pemilihan obat berdasarkan kondisi kesehatan?
- Bagaimana _machine learning_ dapat memenuhi kebutuhan untuk menyederhanakan proses pemilihan obat dengan solusi yang efektif.
- Bagaimana _best practice_ (alur kerja) dalam pengerjaan _machine learning_ untuk membuat sistem rekomendasi pemilihan obat?

### Goals
Tujuan yang ingin dicapai adalah:
- Meningkatkan akurasi dan kecepatan pemilihan obat berdasarkan kondisi kesehatan pasien.
- Memberikan rekomendasi obat yang sesuai dengan karakteristik dan kebutuhan kesehatan individual.
- Meningkatkan efisiensi waktu para profesional kesehatan dalam memberikan saran obat.

### Solution statements
- Pengembangan sistem rekomendasi obat menggunakan Content Based Filtering (CBF).
- Integrasi data medis dan farmakologi untuk analisis yang akurat.
- Pemanfaatan algoritma cerdas dalam menghasilkan rekomendasi obat yang sesuai.
- Implementasi solusi dalam platform kesehatan digital untuk akses oleh profesional kesehatan dan pasien.

## DATA UNDERSTANDING

Data yang digunakan bersumber dari https://www.kaggle.com/datasets/jessicali9530/kuc-hackathon-winter-2018. Dataset tinjauan obat mencakup beberapa kolom atau atribut yang memberikan informasi tentang obat-obatan dan ulasan pengguna. Berikut adalah penjelasan untuk setiap kolom yang disebutkan:

- uniqueID: Ini adalah identifikasi unik atau kode yang digunakan untuk membedakan setiap baris atau entri dalam dataset. Kolom ini membantu dalam pengelompokan, pengurutan, atau pengaksesan data secara individual.

- drugName: Kolom ini berisi nama obat yang direkomendasikan atau diulas oleh pengguna. Nama obat ini dapat mencakup nama generik atau nama merek dari obat yang diresepkan.

- condition: Atribut ini menyediakan informasi tentang kondisi medis atau penyakit yang diobati dengan menggunakan obat yang disebutkan dalam baris tertentu. Misalnya, kondisi seperti diabetes, hipertensi, atau depresi.

- review: Ini adalah kolom yang berisi ulasan atau pendapat dari pengguna terkait dengan pengalaman mereka menggunakan obat yang tercantum. Ulasan ini dapat mencakup berbagai aspek seperti efektivitas, efek samping, atau pengalaman penggunaan secara umum.

- rating: Kolom ini mengindikasikan peringkat atau penilaian yang diberikan oleh pengguna terhadap obat yang mereka gunakan. Penilaian ini seringkali diberikan dalam bentuk angka atau bintang, di mana nilai yang lebih tinggi menunjukkan kepuasan atau efektivitas yang lebih baik.

- date: Atribut ini menunjukkan tanggal ulasan atau tanggal ketika ulasan obat diberikan oleh pengguna. Informasi ini dapat digunakan untuk melacak tren atau pola penggunaan obat dari waktu ke waktu.

- usefulCount: Kolom ini menghitung jumlah pengguna yang menemukan ulasan suatu obat berguna atau bermanfaat. Ini dapat digunakan sebagai metrik untuk mengevaluasi popularitas atau kepercayaan terhadap ulasan yang diberikan. Semakin tinggi nilai usefulCount, semakin banyak pengguna yang menilai ulasan tersebut bermanfaat.

### Exploratory Data Analyst
Telaah data (EDA) merupakan bagian dari data understanding (pemahaman data) yang secara umum terdiri dari : 

#### Analisis Atribut Numerik pada Data:
Tabel 1. Analisis Atribut Numerik
|index|uniqueID|rating|usefulCount|
|---|---|---|---|
|count|10000\.0|10000\.0|10000\.0|
|mean|117573\.7829|6\.9549|28\.1151|
|std|66751\.02774411536|3\.305201722413109|39\.15519588670822|
|min|6\.0|1\.0|0\.0|
|25%|59481\.75|4\.0|6\.0|
|50%|118683\.5|8\.0|16\.0|
|75%|175091\.5|10\.0|35\.0|
|max|232253\.0|10\.0|949\.0|


#### Univariate Analysis

![image](https://github.com/HanggaBayu/Daftar-Biodata-Siswa/assets/99377476/09f90eda-ef02-4238-bb68-5a5b33d80fbd)


Gambar 1. Tiga Puluh Kondisi/Penyakit Paling Umum Terjadi

Gambar 1 memberikan gambaran umum mengenai distribusi n kondisi atau penyakit tertentu. Ditemukan bahwa sebagian besar ulasan berkaitan dengan obat-obatan untuk kontrasepsi (Birth Control), depresi (Depression), dan penghilang rasa sakit (Pain), dengan jumlah ulasan yang signifikan. Selain itu, obat-obatan untuk kecemasan (Anxiety), jerawat (Acne), penurunan berat badan (Weight Loss), dan gangguan bipolar (Bipolar Disorder) juga menerima perhatian yang cukup besar. Hal ini memberikan wawasan tentang preferensi atau perhatian khusus pengguna terhadap berbagai kondisi kesehatan, yang dapat menjadi informasi berharga dalam pengembangan solusi kesehatan atau pemilihan obat.


![image](https://github.com/HanggaBayu/Daftar-Biodata-Siswa/assets/99377476/841d3215-bd1c-4b8c-82e4-94cc08e6c83b)


Gambar 2. Tiga Puluh Obat Paling Populer

![image](https://github.com/HanggaBayu/Daftar-Biodata-Siswa/assets/99377476/4d5e3f23-e80c-4eda-b9bd-9f2e3c4f0aee)


Gambar 3. Plotting 100 Obat Terpopuler Menggunakan _worcloud_

Gambar 2 dan 3 menunjukkan bahwa beberapa jenis obat lebih mendapat perhatian dari pengguna daripada yang lain. Levonorgestrel dan Etonogestrel memimpin dengan jumlah ulasan yang signifikan, menunjukkan popularitasnya di antara pengguna. Obat kombinasi seperti Ethinyl estradiol / norethindrone dan Ethinyl estradiol / levonorgestrel juga menerima perhatian yang tinggi. Nexplanon, Implanon, dan Phentermine juga mencatat jumlah ulasan yang cukup tinggi.


![image](https://github.com/HanggaBayu/Daftar-Biodata-Siswa/assets/99377476/6e609d96-9430-451c-a91a-3895411843e4)

Gambar 4. Jumlah Obat Terbanyak dalam Suatu Penyakit

Gambar 4 menunjukkan sejumlah besar obat terfokus pada pengobatan kondisi kesehatan tertentu. Birth Control mendominasi dengan 109 obat, menandakan adanya beragam opsi kontrasepsi yang tersedia. Pengobatan untuk Pain dan Depression juga mendapat perhatian yang signifikan, masing-masing dengan 90 dan 75 obat, mencerminkan keragaman terapi untuk mengatasi rasa sakit dan gangguan suasana hati. Acne dan Anxiety memiliki 57 dan 48 obat secara berturut-turut, menunjukkan upaya dalam mengatasi masalah kulit dan kecemasan. Selanjutnya, High Blood Pressure dan Insomnia masing-masing memiliki 47 dan 44 obat, mencerminkan fokus pada kondisi kesehatan kardiovaskular dan gangguan tidur. Bipolar Disorder dan Diabetes, Type 2 memiliki 44 dan 39 obat, menunjukkan ketersediaan terapi untuk gangguan suasana hati dan diabetes. Jumlah obat untuk Major Depressive Disorder mencapai 35, menandakan adanya upaya dalam merespons gangguan suasana hati yang serius. Keseluruhan, data ini memberikan pandangan terinci tentang variasi obat-obatan yang tersedia untuk berbagai kondisi kesehatan, mencerminkan kompleksitas dan keragaman dalam pendekatan pengobatan modern.


![image](https://github.com/HanggaBayu/Daftar-Biodata-Siswa/assets/99377476/f4f6d8fd-9e72-447c-9dbb-36511426f872)


Gambar 5.  jumlah Suatu Jenis Obat yang dapat Digunakan untuk Berbagai Kondisi

Pada Gambar 5 menjelaskan tentang jumlah obat untuk beberapa kondisi menunjukkan variasi dalam jenis obat yang digunakan untuk berbagai kondisi kesehatan. Gabapentin menduduki peringkat teratas dengan 15 kondisi, menunjukkan popularitasnya dalam pengobatan berbagai kondisi. Venlafaxine, Duloxetine, dan Amitriptyline, dengan masing-masing 14, 13, dan 11 kondisi, menonjol sebagai obat-obatan yang sering digunakan dalam berbagai kondisi


![image](https://github.com/HanggaBayu/Daftar-Biodata-Siswa/assets/99377476/24d472c2-0246-4ade-ae14-c65af21c33a1)


Gambar 6. Distribusi Numerik pada Dataset

Pada Gambar 6 dapat dilihat data dengan rating 10 dan 9 cukup mendominasi. Sementara pada useful count data dengan nilai 0 merupakan data terbanyak


![image](https://github.com/HanggaBayu/Daftar-Biodata-Siswa/assets/99377476/216c21d0-1426-40e2-bf13-0d5a21cacf08)

Gambar 7. Distribusi Rating Menggunakan Diagram Lingkaran

Gambar 7 menunjukkan distribusi rating pada dataset yang dilakukan dengan diagram lingkaran terlihat sekitar 31.2 % data memiliki rating 10

![image](https://github.com/HanggaBayu/Daftar-Biodata-Siswa/assets/99377476/290cbb11-b143-42af-9df0-6087e709ce3d)


Gambar 8. Distribusi Sentimen Positif/Negatif Menggunakan Diagram Lingkaran

Pada Gambar 8 kita dapat melihat distribusi sentimen positif mendominasi dengan persentase sebesar 69.6 %


## Data Preparation
Dalam data preparation dilakukan beberapa proses penting yang mencakup:

#### Pengecekan Data

Dataset terdiri dari 2 data, yaitu training dan testing. Selanjutnya untuk keperluan tugas ini , data yang digunakan merupakan data testing yang hanya menggunkaan 10.000 dikarenakan keterbatasan sumber daya komputasi penulis

Yang dilakukan pertama-tama adalah mengecek potensial pada data, sehingga dilakukan pengecekan untuk data kosong/NA dan pengecekan data dupplikat

- Identifikasi Nilai Hilang (NA):

Temukan kolom atau baris dengan nilai yang hilang atau tidak lengkap. Hapus Baris atau Kolom yang tidak memiliki nilai, namun jika sebagian besar data di suatu baris atau kolom hilang, pertimbangkan untuk menghapusnya. Jika kehilangan data bersifat terisolasi, pertimbangkan untuk menggantikan nilai yang hilang dengan nilai rata-rata, median, atau strategi pengisian data yang sesuai.

- Identifikasi Duplikat:
  
Cari dan temukan baris yang memiliki nilai yang sama untuk setiap atribut khususny dalam konteks ini adlaah apabila terdapat baris yang memiliki drug_name dan kondisi persis sama dengan baris lainnya. : Hapus baris yang diidentifikasi sebagai duplikat dari dataset.

#### Membuat dataset baru untuk CBF
Dengan kondisi dataset berupa hubungan many to many antar variabel, maka pembuatan dataset dilakukan untuk membuat tiap nilai pada kolom _drug name_ menjadi unik dan dalam kolom _condition_ merupakan gabungan dari kondisi-kondisi yang dapat disembuhkan oleh obat tersebut. Dataset review obat ini memiliki banyak jenis obat dan kondisinya, satu obat dapat berguna untuk beberapa kondisi atau hanya 1 kondisi dan begitu juga sebaliknya. Sehingga dataset yang sebelumnya perlu dilakukan modifikasi hingga didapat bentuk dataframe seperti berikut, di mana pada kolom satu _drug_name_ hanya memiliki satu jenis obat, kemudian kolom _kondisi_ dapat menampung beberapa kondisi dari suatu jenis obat. Selain itu untuk kebutuhan content-based filtering kali ini kolom yang digunakan hanya _drug_name_ dan _condition_

Tabel 2. Dataset baru (_data_merge_)
| index | drug_name     | condition                                             |
| ----- | ------------- | ----------------------------------------------------- |
| 1497  | Zyban         | Smoking Cessation                                     |
| 1498  | Zyclara       | Keratosis                                             |
| 1499  | Zyprexa       | Depression, Bipolar Disorde, Major Depressive Disorde |
| 1500  | Zyprexa Zydis | Paranoid Disorde                                      |
| 1501  | Zyrtec        | Urticaria, Allergic Rhinitis                          |
| 1502  | Zyrtec-D      | 4</span> users found this comment helpful.            |
| 1503  | Zytiga        | Prostate Cance                                        |
| 1504  | Zyvox         | Bacteremia                                            |
| 1505  | ella          | Emergency Contraception                               |
| 1506  | femhrt        | Menstrual Disorders, Postmenopausal Symptoms          |


## Modelling (CONTENT BASED FILTERING) and Result
Content-Based Filtering (CBF) adalah pendekatan dalam sistem rekomendasi di mana rekomendasi obat-obatan dipersonalisasi berdasarkan karakteristik obat yang pernah dikonsumsi oleh pengguna. Proses ini melibatkan ekstraksi fitur dari obat yang mencakup informasi seperti nama obat, dan penyakit yang sesuai. Dengan membuat profil pengguna berdasarkan fitur-fitur ini, sistem dapat mengukur kesamaan antara profil pengguna dan profil obat lain, kemudian memberikan rekomendasi obat baru yang memiliki karakteristik serupa. Dalam konteks rekomendasi obat, CBF membantu pengguna menemukan obat-obatan yang mungkin efektif untuk kondisi kesehatan tertentu berdasarkan preferensi dan pengalaman pengguna dengan obat-obatan sebelumnya.

### TF IDF VECTORIZER

Term Frequency-Inverse Document Frequency (TF-IDF) Vectorizer adalah suatu teknik dalam pemrosesan teks yang digunakan untuk mengubah teks menjadi representasi vektor numerik berdasarkan frekuensi kemunculan kata dan kepentingannya dalam suatu dokumen atau kumpulan dokumen. Dalam konteks penggunaan nilai-nilai pada kolom 'condition', setiap kondisi atau penyakit dapat dianggap sebagai "dokumen". 

- Inisialisasi TfidfVectorizer:
Menggunakan modul TfidfVectorizer dari scikit-learn untuk mengonversi teks ke representasi vektor TF-IDF.

- Fit dan Transform:

Menggunakan metode fit_transform untuk mengubah kolom 'condition' dalam dataset menjadi matriks TF-IDF.

- Ukuran Matriks TF-IDF:

Mengevaluasi ukuran matriks TF-IDF yang dihasilkan dengan menggunakan atribut shape.

- Transformasi ke Bentuk Matriks Dense:

Menggunakan metode todense() untuk mengonversi matriks TF-IDF ke dalam bentuk matriks dense.

- Membuat DataFrame untuk Melihat TF-IDF Matrix:

Membuat DataFrame dari matriks TF-IDF dengan menggunakan kolom dan indeks yang sesuai.


Tabel 3. Sampling dan Tampilan DataFrame Hasil Proses TF-IDF Matrix
|drug\_name|generalized|reflex|depression|12|vein|anorexia|nasal|cell|disorders|deficiency|male|sclerosis|mineral|fissure|embolism|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Aprepitant|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|MetroCream|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Zenatane|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Multivitamin with minerals|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.4508426339579077|0\.0|0\.0|0\.5105686758873368|0\.0|0\.0|
|Propoxyphene|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Prazosin|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Apixaban|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Patanase|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Telmisartan|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Vimovo|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Provera|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Nadolol|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Humulin N|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Sulfacetamide sodium / sulfur|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Ciprofloxacin|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|

Langkah-langkah ini secara keseluruhan menciptakan representasi numerik dari kondisi kesehatan dalam bentuk matriks TF-IDF, yang dapat digunakan untuk analisis lebih lanjut atau sebagai fitur masukan untuk model pembelajaran mesin. Semakin tinggi nilai matriks menunjukkan semakin erat hubungan antara jenis obat dengan suatu penyakit.

### Cosine Similiarty

Matriks cosine similarity, yang dihitung berdasarkan representasi TF-IDF dari nama obat (drug name), memberikan pandangan tentang sejauh mana obat satu mirip dengan yang lainnya dalam konteks kesehatan. Nilai cosine similarity tinggi antara dua obat menunjukkan kesamaan yang signifikan dalam cara obat tersebut digunakan untuk mengatasi kondisi kesehatan tertentu. Matriks ini dapat digunakan untuk mengidentifikasi obat-obatan yang memiliki kesamaan terapeutik atau mendukung dalam pengembangan sistem rekomendasi obat, di mana obat-obatan dengan cosine similarity yang tinggi dapat direkomendasikan berdasarkan pengobatan sebelumnya atau kondisi kesehatan yang serupa. Nilai-nilai cosine similarity mendekati 1 menunjukkan kemiripan yang tinggi, sementara nilai mendekati 0 menunjukkan kemiripan yang rendah. Matriks ini dapat digunakan untuk mencari obat-obatan yang memiliki kemiripan dalam kondisi pengobatan atau mendukung sistem rekomendasi obat berdasarkan kesamaan dalam konteks kesehatan.

Tabel 4. dataframe dari variabel cosine_sim dengan baris kolom berupa _drug_name_

|drug\_name|Desvenlafaxine|Clindesse|Claritin-D|Aspirin / dipyridamole|Mysoline|Denavir|Tofacitinib|Telmisartan|Demerol|Estraderm|
|---|---|---|---|---|---|---|---|---|---|---|
|Prazosin|0\.15331541200267046|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Xyrem|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Efavirenz / emtricitabine / tenofovir|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Tioconazole|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Aranesp|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Moxatag|0\.0|0\.32259927322000165|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Qsymia|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Hydrochlorothiazide|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|1\.0000000000000002|0\.0|0\.0|
|Chlorpheniramine / hydrocodone / pseudoephedrine|0\.0|0\.0|0\.5550532053932594|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|
|Cevimeline|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|

Menggunakan fungsi drug_recommendations('Abilify Discmelt') untuk mengoperasikan model rekomendasi obat berdasarkan cosine similarity dari matriks TF-IDF, dengan menggunakan obat "Abilify Discmelt" sebagai referensi. Dalam keluaran hasilnya, model merekomendasikan beberapa obat lain yang memiliki hubungan atau kesamaan terapeutik dengan "Abilify Discmelt" dalam konteks kondisi "Depression". Contoh rekomendasi tersebut mencakup obat-obatan seperti "Emsam," "Tofranil," "St. John's Wort," "Parnate," dan "Amoxapine," yang semuanya terkait dengan pengobatan kondisi depresi. Dengan cara ini, model menyajikan opsi obat-obatan lain yang mungkin relevan atau efektif untuk pengguna yang sebelumnya mengonsumsi "Abilify Discmelt" dan memiliki kondisi kesehatan terkait depresi.

Tabel 5. Hasil Rekomendasi

|index|drug\_name|condition|
|---|---|---|
|0|Emsam|Depression|
|1|Tofranil|Depression|
|2|St\. john's wort|Depression|
|3|Parnate|Depression|
|4|Amoxapine|Depression|

## EVALUATION

![1_KQ0veHTnTOnBX2CeOjHaDw](https://github.com/HanggaBayu/Daftar-Biodata-Siswa/assets/99377476/0f38779d-2276-447d-befc-13f26d2f6365)

Tabel 5. Referensi Obat

|index|drug\_name|condition|
|---|---|---|
|4|Abilify Discmelt|Depression|


Dalam tabel hasil , kita memiliki rekomendasi obat untuk kondisi "Depression" berdasarkan obat sebelumnya yang dikonsumsi, yaitu "Abilify Discmelt." Dapat dilihat sistem memberikan rekomendasi yang sepenuhnya sesuai dengan kondisi "Depression" dan obat sebelumnya tersebut, maka kita memiliki presisi 100%. Dengan kata lain, setiap obat yang direkomendasikan (Emsam, Tofranil, St. John's Wort, Parnate, Amoxapine) juga sesuai dengan kondisi dan obat sebelumnya.

## Kesimpulan
Berdasarkan tujuan yang telah disebutkan, kesimpulan dari model sistem rekomendasi adalah bahwa ia berhasil meningkatkan akurasi dan kecepatan pemilihan obat berdasarkan kondisi kesehatan pasien. Dengan menggunakan metode content-based filtering, model ini dapat memberikan rekomendasi obat yang sesuai dengan karakteristik dan kebutuhan kesehatan individual. Sebagai hasilnya, sistem ini meningkatkan efisiensi waktu para profesional kesehatan dalam memberikan saran obat kepada pasien.

Dengan adanya model ini, para profesional kesehatan dapat mengandalkan rekomendasi yang akurat dan disesuaikan dengan kondisi kesehatan pasien tanpa perlu melibatkan proses pemilihan obat yang manual dan memakan waktu. Ini tidak hanya membantu meningkatkan pelayanan kesehatan secara keseluruhan tetapi juga memberikan solusi yang efisien dan terfokus pada kebutuhan individu pasien. Namun, perlu diingat bahwa hasil dari model ini hanya untuk tujuan pembelajaran sistem rekomendasi dan tidak cocok untuk penggunaan praktis dalam memberikan rekomendasi obat di dunia nyata.
