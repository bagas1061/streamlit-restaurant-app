# Laporan Tugas 3: Pembuatan Dashboard Analisis Menu Restoran dengan Streamlit
### Muhammad Bagas Setiawan 
### 10231061


## Pendahuluan
Tugas praktikum ini bertujuan untuk membangun aplikasi dashboard sederhana menggunakan framework Streamlit untuk menganalisis menu restoran berdasarkan data ulasan dari pelanggan. Aplikasi ini memungkinkan pengguna memasukkan data 10 jenis makanan favorit, termasuk rating (1-5), dan menampilkan analisis visual seperti grafik perbandingan, distrbusi, dan peta lokasi dummy restoran. Dashboard memberikan wawasan bagi pemilik restoran untuk mengoptimalkan menu dan strategi pemasaran.

## Langkah-Langkah Pengerjaan

### 1. Instalasi dan Setup Lingkungan
- Pastikan Python terinstal (versi 3.7+).
- Instal pustaka yang diperlukan:
  ```
  pip install streamlit pandas matplotlib
  ```
- Buat file `app.py` di direktori kerja `/Users/bagasxy/tugas-week10/deploy-streamlit`.
- Jalankan aplikasi dengan perintah `streamlit run app.py`.

### 2. Import Pustaka
Kode awal mengimpor pustaka yang diperlukan:
```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
```
- `streamlit`: Framework utama untuk membuat dashboard interaktif.
- `pandas`: Untuk manipulasi data (DataFrame).
- `matplotlib`: Untuk visualisasi chart tambahan.

### 3. Struktur Utama Aplikasi
Aplikasi menggunakan struktur Streamlit dengan elemen seperti judul, markdown, input forms, dan visualisasi.

#### a. Judul dan Deskripsi
```python
st.title('Dashboard Restoran: Analisis Menu Makanan')
st.markdown("""
Selamat menikmati hidangan di restoran kami! Sebagai pelayan, saya mohon bantuan Anda untuk memberikan ulasan atas 10 jenis makanan favorit pelanggan yang telah Anda coba saat berkunjung:
Beri rating (1-5), tambahkan deskripsi singkat, dan lokasi dummy untuk memahami tren dan distribusi.
Dashboard ini memberikan wawasan tentang menu populer, bandingkan rating, lihat pola tren, proporsi pasar, sebaran lokasi, dan akumulasi preferensi.
Hal ini membantu pemilik restoran memutuskan fokus menu, optimasi penawaran, dan strategi pemasaran. Terima kasih atas umpan balik Anda!
""")
st.image("restoran.png", caption="Restoran Kami - Terima Kasih Atas Kunjungan Anda!")
```
- **st.title()**: Menampilkan judul halaman utama.
- **st.markdown()**: Menampilkan teks deskripsi. Telah dimodifikasi untuk terdengar seperti pelayan yang meminta ulasan, bukan teks netral.
- **st.image()**: Menampilkan gambar restoran di bawah deskripsi agar antarmuka lebih menarik.
- Modifikasi: Ubah deskripsi menjadi lebih personal dan interaktif.

#### b. Input Data Makanan
```python
st.header('Input Data 10 Makanan')
foods = []
ratings = []
for i in range(1, 11):
    col1, col2 = st.columns(2)
    with col1:
        food = st.text_input(f'Nama Makanan {i}', key=f'food{i}', value=f'Food {i}', disabled=False)
        foods.append(food)
    with col2:
        rating = st.slider(f'Rating {i}', 0.0, 5.0, 4.0, key=f'rate{i}')
        ratings.append(rating)
```
- Menggunakan loop untuk 10 input.
- `st.columns(2)`: Membuat layout dua kolom.
- `st.text_input()`: Input nama makanan.
- `st.slider()`: Input rating dalam rentang 0-5.
- Data disimpan dalam list `foods` dan `ratings`.

#### c. Membuat DataFrame
```python
data = pd.DataFrame({
    'Food': foods,
    'Rating': ratings
})
```
- Menggabungkan list menjadi DataFrame Pandas untuk analisis dan visualisasi.

### 4. Ringkasan Data
```python
st.header('Ringkasan Data Menu')
st.dataframe(data)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Makanan Tertinggi", data.loc[data['Rating'].idxmax(), 'Food'], f"{data['Rating'].max():.1f}")
with col2:
    st.metric("Rata-Rata Rating", f"{data['Rating'].mean():.1f}")
with col3:
    st.metric("Total Menu", len(data))
```
- `st.dataframe()`: Menampilkan tabel data.
- `st.columns(3)`: Layout tiga kolom untuk metrik.
- `st.metric()`: Menampilkan angka ringkasan seperti makanan tertinggi, rata-rata, dan total.

### 5. Visualisasi Data
Aplikasi menyediakan beberapa jenis visualisasi. Berikut adalah placeholder untuk screenshot dari masing-masing visualisasi:

#### a. Bar Chart dan Line Chart
```python
st.header('Visualisasi Rating Makanan')
st.subheader('Bar Chart: Perbandingan Rating')
st.write('Grafik batang menunjukkan perbandingan rating antar menu...')
st.bar_chart(data.set_index('Food'))
```
![Screenshot Bar Chart Visualisasi Rating](bar_chart_placeholder.png)

```python
st.subheader('Line Chart: Pola Rating')
st.write('Grafik garis menunjukkan bagaimana rating berubah antar menu...')
st.line_chart(data.set_index('Food'))
```
![Screenshot Line Chart Pola Rating](line_chart_placeholder.png)

- `st.bar_chart()` dan `st.line_chart()`: Gunakan DataFrame dengan index 'Food'.

#### b. Visualisasi Tambahan (Pie atau Bar Custom)
```python
st.subheader('Pilih Visualisasi Tambahan')
tipe = st.selectbox("Pilih chart:", ["Pole Chart (Circle)", "Bar Chart Custom"])
if tipe == "Pole Chart (Circle)":
    fig, ax = plt.subplots()
    ax.pie(data["Rating"], labels=data["Food"], autopct="%1.1f%%")
    st.pyplot(fig)
else:
    fig, ax = plt.subplots()
    ax.bar(data["Food"], data["Rating"], color="green")
    ax.set_ylabel("Rating")
    st.pyplot(fig)
```
![Screenshot Pie Chart Persentase Rating](pie_chart_placeholder.png)
![Screenshot Bar Chart Custom Rating](bar_custom_placeholder.png)

- `st.selectbox()`: Pilihan interaktif untuk jenis chart.
- `plt.subplots()`: Membuat figure untuk pie/bar chart.
- `st.pyplot()`: Menampilkan chart matlplotlib.

#### c. Filter Data dengan Slider
```python
nilai = st.slider("Tampilkan data dengan rating minimum:", 0, 5, 3)
st.dataframe(data[data["Rating"] >= nilai])
```
- `st.slider()`: Slider untuk filter rating minimum.
- Filter DataFrame dan tampilkan hasil.

#### d. Peta Lokasi Dummy Restoran
```python
st.subheader('Map: Sebaran Lokasi Restoran')
st.write('Peta menunjukkan lokasi dummy restoran sesuai menu...')
data_map = pd.DataFrame({
    'lokasi': foods[:10],
    'lat': [-6.2088, -7.2575, -6.9175, -8.3405, 3.5952, -7.7956, -5.1477, -6.9667, -2.9761, -0.0174][:len(foods)],
    'lon': [106.8456, 112.7521, 107.6191, 115.0920, 98.6722, 110.3695, 119.4318, 110.4167, 104.7754, 109.3250][:len(foods)]
})
st.map(data_map)
```
![Screenshot Peta Sebaran Lokasi Restoran](map_placeholder.png)

- `st.map()`: Menampilkan peta berdasarkan DataFrame dengan kolom 'lat' dan 'lon'.
- Koordinat diperbarui dari dummy menjadi yang mewakili kota-kota Indonesia seperti Jakarta, Surabaya, dll.

#### e. Area Chart Akumulasi Rating
```python
st.subheader('Area Chart: Akumulasi Rating')
st.write('Area chart menunjukkan akumulasi rating...')
st.area_chart(data.set_index('Food'))
```
![Screenshot Area Chart Akumulasi Rating](area_chart_placeholder.png)

- `st.area_chart()`: Chart area untuk akumulasi.

### 6. Link Deploy



## Kesimpulan
Praktikum ini berhasil membangun dashboard interaktif dengan Streamlit, mencakup input data, analisis, dan visualisasi. Modifikasi terbaru membuat antarmuka lebih menarik dan realistis. Aplikasi dapat diperluas dengan fitur lebih lanjut seperti penyimpanan data atau integrasi database.
