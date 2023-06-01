# Nama  : Kiki Indiani
# Kelas : R1
# NIM   : 210511046

class Perusahaan:
    def __init__(self, name):
        self.name = name
        self.karyawan = Karyawan()
        print("PT. Sinar Bulan")

class Data:
    def __init__(self, name, sience, placed):
        self.name = name
        self.sience = sience
        self.placed = placed

class Karyawan:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print("Nama: ",item.name,",Sejak", item.sience,",penempatan",item.placed)

    def remove_item(self, item):
        self.items.remove(item)

perusahaan = Perusahaan(" ")
data1 = Data("Kiki Indiani", 2021, "Semarang")
data2 = Data("Grandies Silvania", 2019,"Cirebon")
data3 = Data("Fitri Amalia", 2020, "Jakarta Selatan")
print("-"*150)
perusahaan.karyawan.add_item(data1)
perusahaan.karyawan.add_item(data2)
perusahaan.karyawan.add_item(data3)
perusahaan.karyawan.items
print("-"*150)
print(" ")