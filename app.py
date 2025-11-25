import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Dashboard Restoran: Analisis Menu Makanan')
st.markdown("""
Selamat menikmati hidangan di restoran kami! Sebagai pelayan, saya mohon bantuan Anda untuk memberikan ulasan atas 10 jenis makanan favorit pelanggan yang telah Anda coba saat berkunjung:
Beri rating (1-5), tambahkan deskripsi singkat, dan lokasi dummy untuk memahami tren dan distribusi.
Dashboard ini memberikan wawasan tentang menu populer, bandingkan rating, lihat pola tren, proporsi pasar, sebaran lokasi, dan akumulasi preferensi.
Hal ini membantu pemilik restoran memutuskan fokus menu, optimasi penawaran, dan strategi pemasaran. Terima kasih atas umpan balik Anda!
""")

# Input for 10 foods
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

data = pd.DataFrame({
    'Food': foods,
    'Rating': ratings
})

st.header('Ringkasan Data Menu')
st.dataframe(data)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Makanan Tertinggi", data.loc[data['Rating'].idxmax(), 'Food'], f"{data['Rating'].max():.1f}")
with col2:
    st.metric("Rata-Rata Rating", f"{data['Rating'].mean():.1f}")
with col3:
    st.metric("Total Menu", len(data))

st.header('Visualisasi Rating Makanan')
st.subheader('Bar Chart: Perbandingan Rating')
st.write('Grafik batang menunjukkan perbandingan rating antar menu. Menu tinggi batang lebih suka pelanggan.')
st.bar_chart(data.set_index('Food'))

st.subheader('Line Chart: Pola Rating')
st.write('Grafik garis menunjukkan bagaimana rating berubah antar menu. Bantu lihat tren kesukaan.')
st.line_chart(data.set_index('Food'))

st.subheader('Pilih Visualisasi Tambahan')
tipe = st.selectbox("Pilih chart:", ["Pole Chart (Circle)", "Bar Chart Custom"])
if tipe == "Pole Chart (Circle)":
    st.write('Pie chart menunjukkan persentase rating per menu. Bantu lihat proporsi kesukaan.')
    fig, ax = plt.subplots()
    ax.pie(data["Rating"], labels=data["Food"], autopct="%1.1f%%")
    st.pyplot(fig)
else:
    st.write('Bar chart hijau menunjukkan rating langsung. Pilih untuk fokus pada perbandingan nilai.')
    fig, ax = plt.subplots()
    ax.bar(data["Food"], data["Rating"], color="green")
    ax.set_ylabel("Rating")
    st.pyplot(fig)


nilai = st.slider("Tampilkan data dengan rating minimum:", 0, 5, 3)
st.dataframe(data[data["Rating"] >= nilai])

st.subheader('Map: Sebaran Lokasi Restoran')
st.write('Peta menunjukkan lokasi dummy restoran sesuai menu. Bantu analisis ekspansi atau sebaran pasar.')
data_map = pd.DataFrame({
    'lokasi': foods[:10],  # Use food names as locations, or could make input for lat lon but keep simple
    'lat': [-6.2088, -7.2575, -6.9175, -8.3405, 3.5952, -7.7956, -5.1477, -6.9667, -2.9761, -0.0174][:len(foods)],
    'lon': [106.8456, 112.7521, 107.6191, 115.0920, 98.6722, 110.3695, 119.4318, 110.4167, 104.7754, 109.3250][:len(foods)]
})
st.map(data_map)

st.subheader('Area Chart: Akumulasi Rating')
st.write('Area chart menunjukkan akumulasi rating dengan area warna. Ideal untuk lihat total fokus menu.')
st.area_chart(data.set_index('Food'))
