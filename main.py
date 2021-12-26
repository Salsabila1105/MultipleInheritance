class Ricecooker:
  def __init__(self,nama_merk,tuas,mode): 
    self.nama_merk = nama_merk
    self.tuas = tuas 
    self.mode = mode

class TypeRicecooker:
  def __init__(self,temperature):
    self.temperature = temperature
    self.temperaturesekarang = self.temperature + 50
    print('Temperature Ricecooker sekarang = ', self.temperaturesekarang)

class ModernRicecooker: 
  def __init__(self,nama_merk,tuas,mode,temperature):
    Ricecooker.__init__(self,nama_merk,tuas,mode)
    TypeRicecooker.__init__(self, temperature)

YoungMa= ModernRicecooker('YoungMa', 'ON', 'Cook',100)
print(YoungMa.nama_merk)
print(YoungMa.tuas)
print(YoungMa.mode)
print(YoungMa.temperature)

