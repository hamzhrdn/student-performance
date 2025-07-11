# **Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech**
## **Business Understanding**
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Hal ini dapat dilihat dari tingginya presentase siswa yang dropout di angka 32.12% dari jumlah keseluruhan siswa. Jumlah dropout yang tinggi menjadi permasalahan yang besar bagi sebuah institusi pendidikan yang akan berdampak kedepannya.

## **Permasalahan Bisnis**
Permasalahan yang dialami oleh Jaya Jaya Institut yakni meliputi tingginya tingkat dropout siswa yang mencapai lebih dari 30%. Angka ini tergolong sangat tinggi jika dibandingkan rata-rata institusi pendidikan lainnya yang menjadi tolok ukur. Tingginya tingkat dropout ini akan membawa dampak negatif kedepannya bagi institusi, antara lain:

1. Menurunnya tingkat kepercayaan bagi calon pendaftar siswa baru terhadap kualitas institusi
2. Kerugian finansial yang berarti kehilangan pendapatan yang telah dianggarkan untuk operasional, pengembangan fasilitas, dan gaji staf.
3. Menurunnya moral komunitas akademik yang dapat memengaruhi lingkungan pendidikan.

## **Cakupan Proyek**
Sebagai upaya untuk mengatasi permasalahan tersebut, proyek ini dibuat untuk melakukan identifikasi terhadap faktor-faktor yang dapat memengaruhi tingginya tingkat dropout pada siswa, analisa dilakukan dengan menggunakan parameter-parameter berikut:
1. Finansial
2. Keluarga
3. Usia
Hasil analisis disajikan dalam bentuk visualisasi data pada sebuah dashboard untuk menunjukkan pengaruh setiap faktor terhadap tingkat dropout. Selain itu, proyek ini juga memberikan model machine learning untuk melakukan prediksi terhadap kondisi siswa dalam keputusan untuk dropout.

## **Persiapan**
Sumber data: [Jaya-jaya Institute](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:
- Menjalankan Python Notebook
1. Membuat environment python
    ```
        conda create --name jaya-institute python=3.9
    ```
2. Aktivasi environment
    ```
        conda activate jaya-institute
    ```
3. Instal package yang dibutuhkan
    ```
        pip install -r requirements.txt
    ```

- Menjalankan Dashboard Metabase
Pastikan Docker sudah terinstall di sistem
1. Pull Image Metabase
   ```
   docker pull metabase/metabase
   ```
2. Jalankan Container Metabase
   ```
   docker run -d -p 3000:3000 --name metabase metabase/metabase
   ```
3. Akses Metabase (Akses di [Metabase](http://localhost:3000))
4. Login Credential
5. Akses Dashboard
   
- Menjalankan App Simulasi
1. Mengubah directory terminal
   ```
        cd [path-directory]
   ```
2. Running App
   ```
        run streamlit app.py
   ```
3. Input data masukan
4. Predict
# **Business Dashboard**
![Dashboard 1](dashboard\hamzhrdn-dashboard1.png)
Berdasarkan gambar Dashboard 1, dashboard monitor mahasiswa ini menyajikan analisis terhadap data 4.424 total mahasiswa, dengan fokus utama pada status kelulusan dan demografi usia. Data menunjukkan tingkat kelulusan berada di angka 49,93%, sementara tingkat Dropout tercatat sebesar 32,12%, dan sisanya 17,9% masih berstatus terdaftar. Analisis demografis menunjukkan bahwa rata-rata usia mahasiswa saat pertama kali mendaftar adalah 23,27 tahun, dengan grafik batang yang memperlihatkan bahwa kelompok usia 15 - 22,5 tahun merupakan kelompok dengan jumlah pendaftar tertinggi secara absolut untuk semua kategori (lulus, dropout, dan terdaftar), di mana jumlahnya menurun drastis seiring dengan bertambahnya usia pendaftaran. 

![Dashboard 2](dashboard\hamzhrdn-dashboard2.png)
Berdasarkan gambar Dashboard 2, terdapat Bar Chart yang menunjukkan performa akademik pada ketiga kategori siswa. Pada siswa dropout memiliki rata-rata nilai cukup rendah dibanding kategori lainnya dan rata-rata nilai yang menurun pada semester berikutnya. Kemudian pada grafik korelasi antara beban studi dengan tingkat diterima oleh akademik, berdasarkan grafik tersebut semakin tinggi beban studi yang diajukan oleh siswa maka semakin tinggi tingkat penerimaan oleh akademik. Hal ini menandakan akademik akan memproritaskan siswa dengan beban studi yang tinggi. Selain itu, terdapat korelasi antara kondisi finansial dengan tingkat dropout siswa. Pada mahasiswa penerima beasiswa memiliki angka dropout yang sangat rendah (134) dibandingkan dengan yang tidak menerima beasiswa (1.287). Ini menunjukkan bahwa dukungan finansial berperan penting dalam menjaga retensi mahasiswa. Kemudian pada faktor keuangan, s  iswa yang memiliki utang menunjukkan tingkat dropout yang sangat tinggi, yaitu sekitar 48.9% (246 dari 503 siswa). Angka ini jauh lebih tinggi dibandingkan siswa yang tidak memiliki utang, yang tingkat dropout-nya hanya sekitar 7.2% (282 dari 3.921 siswa)  

![Dashboard 3](dashboard\hamzhrdn-dashboard3.png)
Berdasarkan gambar Dashboard 3, terdapat table list yang menunjukkan perbandingan Graduation Rate dan Dropout Rate pada masing-masing Course. Pada tabel tersebut menunjukkan course Biofuel Production Technologies memiliki tingkat dropout yang paling tinggi di angka 0.67 dan graduation yang salah satu paling rendah setelah Informatics Engineering. Pada course dengan tingkat kelulusan yang paling tinggi dicapai oleh jurusan Nursing yang mencapai tingkat kelulusan di angka 0.72 dan dengan angka dropout yang paling rendah di angka 0.15.

## Credential Metabase
email: user1234@mail.com
password: User1234

# **Conclusion**
Berdasarkan analisis data dan pemodelan machine learning, kesimpulan berikut disusun untuk menjawab permasalahan tingginya tingkat Dropout di Jaya-jaya Institut:

1. Performa Akademik Menjadi Indikator Utama: Terdapat korelasi kuat antara performa akademik dengan status kelulusan mahasiswa. Mahasiswa yang berisiko dropout cenderung memiliki rata-rata nilai yang rendah sejak semester pertama dan mengalami penurunan performa pada semester berikutnya.

2. Kondisi Finansial Merupakan Faktor Krusial: Ketidakstabilan finansial adalah pendorong utama tingkat dropout. Mahasiswa yang tidak menerima beasiswa memiliki kecenderungan dropout yang jauh lebih tinggi. Secara spesifik, mahasiswa yang memiliki utang menunjukkan risiko dropout yang sangat tinggi mencapai 48.9%, dibandingkan dengan mahasiswa tanpa utang yang hanya 7.2%.

3. Jurusan Berpengaruh pada Tingkat Kelulusan: Pilihan program studi atau jurusan memiliki dampak terhadap tingkat dropout. Jurusan seperti Biofuel Production Technologies mencatatkan tingkat dropout tertinggi (0.67), sementara jurusan Nursing memiliki tingkat kelulusan tertinggi (0.72) dan tingkat dropout terendah (0.15).

# **Rekomendasi Action Items**
Untuk mengatasi permasalahan tingginya tingkat dropout dan mencegahnya di masa depan, berikut adalah beberapa rekomendasi tindakan yang dapat diambil oleh Jaya Jaya Institut:
1. Mengembangkan program intervensi terhadap akademik siswa, dengan membuat suatu sistem deteksi dini bagi siswa yang mengalami penurunan performa akademik sehingga dapat memberikan program lanjutan mengenai bimbingan akademik, konseling, dan lain sebagainya untuk membantu memperbaiki nilai sebelum semester berikutnya.
2. Memberikan skema dukungan finansial, dengan memperluas cakupan program beasiswa terutama pada siswa yang berpotensi dalam akademik namun mengalami kendala secara finansial serta dapat menyediakan opsi bantuan dana darurat bagi mahasiswa.
3. Melakukan evaluasi dan audit pada jurusan dengan tingkat dropout yang tinggi mencakup keseluruhan aspek akademik.
4. Implementasi model prediktif untuk memberikan tanda pada siswa dengan probabilitas tinggi untuk dropout.