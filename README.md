# MachineLearning-NLP-01
Projek Machine Learning mengenai NLP (Natural Language Processing) untuk tugas 
 
Submission 1 Kursus Pengembang Machine Learning Dicoding Academy

Projek dipublish pada github https://github.com/Abito21/MachineLearning-NLP-01 

Projek yang saya buat untuk memenuhi tugas submission pertama kursus Belajar Pengembang Machine Learning di Dicoding Academy, dijelaskan sebagai berikut

## •	Data Preparation

Data yang digunakan adalah dataset bbc-new-data yang diunduh melalui kaggle https://www.kaggle.com/hgultekin/bbcnewsarchive kemudian agar lebih mudah mengaksesnya saya menyimpannya di google drive.

Data memiliki 4 objek yaitu category, filename, title dan content

 ![image](https://user-images.githubusercontent.com/67644383/160244489-14332b19-9e6b-4e80-860a-b0b245c8b7ea.png)

Menampilkan 10 baris data dari 4 kolom objek yang ada, terlihat sebagai berikut

![image](https://user-images.githubusercontent.com/67644383/160244539-68a0fd7b-7d61-4e0a-851f-b1450d0ebc10.png)

Kolom filename tidak relevan karena hanya menenjukkan nama file tiap baris data, sehingga hanya menggunakan tiga kolom yaitu title, content dan category menunjukkan klasifikasi dari data bbc-news.

Melakukan data cleaning dengan membersihkan data dari objek yang tidak digunakan untuk melakukan pelatihan model machine learning seperti huruf kapital, mengubah objek numerik dan objek lain menjadi string, pengelompokan data berdasarkan kata bedan, kata sifat, maupun kata keterangan. Sehingga data akan terlihat seperti dibawah ini.

![image](https://user-images.githubusercontent.com/67644383/160244558-f8496ee7-1ec6-47f7-bd8e-9efa7643139b.png)

Membuat kategori multiclass terdiri dari business, entertainment, politics, sport dan tech.

![image](https://user-images.githubusercontent.com/67644383/160244570-389cb1bd-f78f-4d48-8318-67fa35083501.png)

Terlebih dahulu melakukan tokenization untuk memisahkan elemen kata, sequence menghitung nilai objek kata dan padding mengenali objek kata.

## •	Data Modelling

Membuat model machine learning menggunakan framework tensorflow yang akan digunakan untuk melakukan pelatihan dataset

![image](https://user-images.githubusercontent.com/67644383/160244586-31fe100f-07bd-4787-b1b5-e5b2eb2477c6.png)

## •	Metrik Akurasi

![image](https://user-images.githubusercontent.com/67644383/160244601-7d1bbfe9-af6a-4be8-a850-7d66e21c8dcd.png)
 
Hasilnya mendapatkan accuracy sebesar 99% dan untuk validation accuracy sebesar 85%.
