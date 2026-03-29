import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl 

# Menyiapkan himpunan Fuzzy
suhu = ctrl.Antecedent(np.arange(0,40), 'suhu')
kelembapan = ctrl.Antecedent(np.arange(0,100), 'kelembapan')
kecepatan = ctrl.Consequent(np.arange(0,100), 'kecepatan')

# range suhu
suhu['Dingin'] = fuzz.trapmf(suhu.universe, [0, 0, 5, 15])
suhu['Sedang'] = fuzz.trimf(suhu.universe, [10, 20, 30])
suhu['Panas'] = fuzz.trapmf(suhu.universe, [25, 35, 40, 40])

# tingkat kelembapan
kelembapan['Kering'] = fuzz.trapmf(kelembapan.universe, [0, 0, 20, 40])
kelembapan['Normal'] = fuzz.trimf(kelembapan.universe, [30, 50, 70])
kelembapan['Lembap'] = fuzz.trapmf(kelembapan.universe, [60, 80, 100, 100])

# kecepatan kipas
kecepatan['Lambat'] = fuzz.trapmf(kecepatan.universe, [0, 0, 20, 40])
kecepatan['Normal'] = fuzz.trimf(kecepatan.universe, [30, 50, 70])
kecepatan['Cepat'] = fuzz.trapmf(kecepatan.universe, [60, 80, 100, 100])

# view
suhu.view()
kelembapan.view()
kecepatan.view()
input("enter")