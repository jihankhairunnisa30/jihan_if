# Data hasil panen
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 450
        }
    }
}

# 1. Menampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing.
print("Seluruh Data Hasil Panen:")
for lokasi, data in data_panen.items():
    print(f"Lokasi: {data['nama_lokasi']}")
    for tanaman, jumlah in data['hasil_panen'].items():
        print(f"  {tanaman}: {jumlah} kg")
    print()

# 2. Menampilkan jumlah hasil panen jagung dari lokasi2.
jumlah_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung di Kebun B: {jumlah_jagung_lokasi2} kg\n")

# 3. Menampilkan nama lokasi dari lokasi3.
nama_lokasi_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {nama_lokasi_lokasi3}\n")

# 4. Menyimpan jumlah hasil panen padi dan kedelai di variabel terpisah.
padi_lokasi = {}
kedelai_lokasi = {}

for lokasi, data in data_panen.items():
    padi_lokasi[lokasi] = data['hasil_panen']['padi']
    kedelai_lokasi[lokasi] = data['hasil_panen']['kedelai']

# Menampilkan hasil panen padi dan kedelai per lokasi
print("Hasil Panen Padi per Lokasi:")
for lokasi, padi in padi_lokasi.items():
    print(f"{data_panen[lokasi]['nama_lokasi']}: {padi} kg")

print("\nHasil Panen Kedelai per Lokasi:")
for lokasi, kedelai in kedelai_lokasi.items():
    print(f"{data_panen[lokasi]['nama_lokasi']}: {kedelai} kg")

# 5. Membuat percabangan untuk lokasi yang memerlukan perhatian khusus.
print("\nLokasi yang Memerlukan Perhatian Khusus:")
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']

    if padi > 1300 or jagung > 800:
        print(f"Lokasi {data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"Lokasi {data['nama_lokasi']} dalam kondisi baik.")
