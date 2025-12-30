# grafik-barber-johnson
This repository contains a Python-based system to automatically generate a Barber Johnson Chart (GBJ) for hospital bed efficiency analysis using BOR, ALOS, TOI, and BTO indicators.

# Grafik Barber Johnson Otomatis (Python)

Repository ini berisi program Python untuk membuat Grafik Barber Johnson (GBJ) secara otomatis sebagai alat evaluasi efisiensi penggunaan tempat tidur rumah sakit.

Grafik ini mengintegrasikan empat indikator utama:
- Bed Occupancy Rate (BOR)
- Average Length of Stay (ALOS)
- Turn Over Interval (TOI)
- Bed Turn Over (BTO)

Program ini dibuat mengikuti kaidah pembuatan Grafik Barber Johnson secara manual dan mengotomatisasinya dalam bentuk visualisasi grafik.

---

## Fitur
- Membuat sumbu TOI (horizontal) dan ALOS/LOS (vertikal)
- Menggambar garis bantu BOR
- Menggambar garis bantu BTO
- Menampilkan daerah efisien
- Menampilkan titik Barber Johnson berdasarkan data input
- Mudah disesuaikan untuk kebutuhan rumah sakit dan laporan periodik

---

## Kebutuhan Sistem
- Python 3.9 atau lebih baru
- Library:
  - numpy
  - matplotlib

---

## Instalasi

1. Clone repository ini:
```bash
git clone https://github.com/username/grafik-barber-johnson-python.git
cd grafik-barber-johnson-python
