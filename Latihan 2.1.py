berat = eval(input(f"Masukkan Berat Badan    = "))
tinggi = eval(input(f"Masukkann Tinggi Badan  = "))
tinggi1 = tinggi / 100
tinggi2 = tinggi1 ** 2
print("=============================================")
print(f"Menghitung BMI (Body Mass Index)")
rumus = berat / tinggi2
print(f"BMI = Berat / Tinggi")
print(f"Body Mass Index yang diharapkan adalah {rumus}")