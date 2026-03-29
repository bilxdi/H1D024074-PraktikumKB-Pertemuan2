import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl 

# Menyiapkan himpunan Fuzzy
suhu = ctrl.Antecedent(np.arange(0, 40), 'suhu')
kelembapan = ctrl.Antecedent(np.arange(0, 100), 'kelembapan')
kecepatan = ctrl.Consequent(np.arange(0, 100), 'kecepatan')

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

# aturan fuzzy
aturan1 = ctrl.Rule(suhu['Dingin'] & kelembapan['Kering'], kecepatan['Normal'])
aturan2 = ctrl.Rule(suhu['Dingin'] & kelembapan['Normal'], kecepatan['Lambat'])
aturan3 = ctrl.Rule(suhu['Dingin'] & kelembapan['Lembap'], kecepatan['Lambat'])

aturan4 = ctrl.Rule(suhu['Sedang'] & kelembapan['Kering'], kecepatan['Cepat'])
aturan5 = ctrl.Rule(suhu['Sedang'] & kelembapan['Normal'], kecepatan['Normal'])
aturan6 = ctrl.Rule(suhu['Sedang'] & kelembapan['Lembap'], kecepatan['Normal'])

aturan7 = ctrl.Rule(suhu['Panas'] & kelembapan['Kering'], kecepatan['Cepat'])
aturan8 = ctrl.Rule(suhu['Panas'] & kelembapan['Normal'], kecepatan['Cepat'])
aturan9 = ctrl.Rule(suhu['Panas'] & kelembapan['Lembap'], kecepatan['Normal'])

# engine dan system
engine = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4, aturan5, aturan6, aturan7, aturan8, aturan9])
system = ctrl.ControlSystemSimulation(engine)

# input
suhux = float(input("Masukkan suhu (0-40 C): "))
kelembapanx = float(input("Masukkan kelembapan (0-100): "))

# compute
system.input['suhu'] = suhux
system.input['kelembapan'] = kelembapanx
system.compute()
print("Kecepatan:", int(system.output['kecepatan']))

# view
# suhu.view()
# kelembapan.view()
kecepatan.view(sim=system)
input("Tekan ENTER untuk selesai")