import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl 

# Menyiapkan himpunan Fuzzy
suhu = ctrl.Antecedent(np.arange(0,40), 'suhu')
kelembapan = ctrl.Antecedent(np.arange(0,100), 'kelembapan')
kecepatan = ctrl.Consequent(np.arange(0,100), 'kecepatan')

# range suhu
suhu['Dingin'] = fuzz.trimf(suhu.universe, [0, 0, 20])
suhu['Sedang'] = fuzz.trimf(suhu.universe, [10, 20, 30])
suhu['Panas'] = fuzz.trimf(suhu.universe, [20, 40, 40])

# tingkat kelembapan
kelembapan['Kering'] = fuzz.trimf(kelembapan.universe, [0, 2, 4])
kelembapan['Normal'] = fuzz.trimf(kelembapan.universe, [3, 5, 7])
kelembapan['Lembap'] = fuzz.trimf(kelembapan.universe, [6, 8, 10])

# kecepatan kipas
kecepatan['Buruk'] = fuzz.trimf(kecepatan.universe, [0, 2, 4])
kecepatan['Cukup'] = fuzz.trimf(kecepatan.universe, [3, 5, 7])
kecepatan['Baik'] = fuzz.trimf(kecepatan.universe, [6, 8, 10])

suhu.view()
kelembapan.view()
kecepatan.view()
input("enter")