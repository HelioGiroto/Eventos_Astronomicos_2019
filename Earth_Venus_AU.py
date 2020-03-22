import ephem
venus = ephem.Venus()
dia = ephem.Date('2020/01/01')

for i in range(366):
   date = ephem.Date(dia)
   au = ephem.Venus(dia).earth_distance
   print(str(date) + ' = ' + str(au))
   dia += 1
 
# Este script usando EPHEM não é tão preciso na distancia como o skyfield!!
# Ver script mais preciso em: https://github.com/HelioGiroto/Eventos_Astronomicos_2019/blob/master/terra_venus_distancia.py
