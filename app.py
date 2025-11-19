import streamlit as st
import pandas as pd

st.title('My First App')
st.write('Here is a list of my favorite foods:')

data = pd.DataFrame({
    'Food': ['Pizza', 'Burger', 'Sushi', 'Taco', 'Pasta'],
    'Rating': [4.5, 4.3, 4.8, 4.0, 4.2]
})

st.subheader('Favorite Foods')
st.dataframe(data)

st.bar_chart(data.set_index('Food'))

st.line_chart(data.set_index('Food'))

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.bar(data["Food"], data["Rating"], color="green")
ax.set_ylabel("Rating")
st.pyplot(fig)


tipe = st.selectbox("Pilih jenis grafik:", ["Bar", "Pie"])

if tipe == "Bar":
    st.bar_chart(data.set_index("Food"))
else:
    fig, ax = plt.subplots()
    ax.pie(data["Rating"], labels=data["Food"], autopct="%1.1f%%")
    st.pyplot(fig)


nilai = st.slider("Tampilkan data dengan rating minimum:", 0, 5, 3)
st.dataframe(data[data["Rating"] >= nilai])


import pandas as pd
import streamlit as st

st.title("Sebaran Lokasi Penanaman Mangrove 🌿")

data_peta = pd.DataFrame({
    'lokasi': ['Balikpapan', 'Samboja', 'Mahakam'],
    'lat': [-1.27, -1.10, -0.50],
    'lon': [116.83, 117.00, 117.25]
})

st.map(data_peta)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard Donasi Lingkungan 🌱")

data = pd.DataFrame({
    "Kampanye": ["Mangrove Balikpapan", "Pantai Samboja", "Delta Mahakam"],
    "Donasi": [120, 85, 60],
    "Target": [150, 100, 90]
})

kampanye = st.selectbox("Pilih kampanye:", data["Kampanye"])
row = data[data["Kampanye"] == kampanye].iloc[0]

st.metric("Donasi Saat Ini", f"{row['Donasi']} juta", delta=row['Donasi'] - row['Target'])
st.progress(row['Donasi'] / row['Target'])

fig, ax = plt.subplots()
ax.bar(data["Kampanye"], data["Donasi"], color="green")
ax.set_ylabel("Donasi (juta)")
st.pyplot(fig)

st.image("mangrove.png", caption="Kegiatan Penanaman Mangrove di Balikpapan")
st.markdown("""
### Tujuan Program
Meningkatkan kesadaran masyarakat terhadap pentingnya ekosistem mangrove.
""")