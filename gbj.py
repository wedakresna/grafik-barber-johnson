import matplotlib.pyplot as plt
import numpy as np

# ==============================
# INPUT DATA
# ==============================
BOR = 75          # persen
ALOS = 4.5        # hari
TOI = 2.0         # hari
BTO = 10
periode_hari = 30

# ==============================
# SETUP GRAFIK
# ==============================
plt.figure(figsize=(8, 8))
plt.xlabel("TOI (hari)")
plt.ylabel("ALOS / LOS (hari)")
plt.title("Grafik Barber Johnson")

plt.xlim(0, 10)
plt.ylim(0, 15)

# ==============================
# GARIS BANTU BOR
# ==============================
LOS_bor = BOR / 10
TOI_bor = 10 - LOS_bor

plt.plot([0, TOI_bor], [0, LOS_bor], label=f"BOR = {BOR}%", linestyle="--")

# ==============================
# GARIS BANTU BTO
# ==============================
titik_bto = periode_hari / BTO
plt.plot([titik_bto, titik_bto], [0, titik_bto], linestyle=":")
plt.plot([0, titik_bto], [titik_bto, titik_bto], linestyle=":")
plt.plot([0, titik_bto], [0, titik_bto], label=f"BTO = {BTO}")

# ==============================
# DAERAH EFISIEN
# ==============================
toi_min, toi_max = 1, 3
los_max = 12

plt.fill(
    [toi_min, toi_max, toi_max, toi_min],
    [0, 0, los_max, los_max],
    color="green",
    alpha=0.15,
    label="Daerah Efisien"
)

# ==============================
# TITIK BARBER JOHNSON
# ==============================
plt.scatter(TOI, ALOS, color="red", zorder=5)
plt.text(TOI + 0.1, ALOS, "Titik BJ", color="red")

# ==============================
# FINAL TOUCH
# ==============================
plt.legend()
plt.grid(True)
plt.show()
