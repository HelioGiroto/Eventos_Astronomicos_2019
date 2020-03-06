# EXEMPLOS DE COMANDOS DOS MÓDULOS SKYFIELD E EPHEM... 
# Módulos de astronomia em Python 3.x:

'''
https://github.com/skyfielders/python-skyfield/issues/228



Escolha qualuqer data que seja inverno no hemisfério Sul. Posicione no Stellarium qualquer lugar no Sul ou na Antártida e vc verá o Cruzeiro do Sul na mesma hora. O próprio programa calcula a diferença do fuso e se nota que em toda parte do Sul do planeta a constelação é vista. Tente isso. Por tanto, se vc traz isso para o mapa da pizza vc percebe a falta de sentido porque o Cruzeiro do Sul não pode estar em toda a borda da pizza na mesma hora.﻿


PRINCIPAL TXT DE LINHAS DAS CONSTELAÇÕES:
bound_edges_18.txt

Andromeda ,And ,Andromeda ,1,38,4
Antlia ,Ant ,Air Pump ,10.2,-35,3
Apus ,Aps ,Bird of Paradise ,16,-75,3
Aquarius ,Aqr ,Water Carrier ,22.3,-8,6
Aquila ,Aql ,Eagle ,19.7,3,4
Ara ,Ara ,Altar ,17.5,-53,4
Aries ,Ari ,Ram ,2.8,18.8,4
Auriga ,Aur ,Charioteer ,5.6,38,4
Boötes ,Boo ,Herdsman ,14.7,34,4
Caelum ,Cae ,Chisel ,4.8,-38,3
Camelopardalis ,Cam ,Giraffe ,5.5,75,5
Cancer ,Cnc ,Crab ,8.7,20,4
Canes Venatici ,CVn ,Hunting Dogs ,13,40,4
Canis Major ,CMa ,Big Dog ,6.5,-20,4
Canis Minor ,CMi ,Little Dog ,7.5,12,4
Capricornus ,Cap ,Goat ,21,-16,4
Carina ,Car ,Keel ,8.5,-64,5
Cassiopeia ,Cas ,Cassiopeia ,0.5,60.5,4
Centaurus ,Cen ,Centaur ,13.6,-45,5
Cepheus ,Cep ,Cepheus ,23,75,4
Cetus ,Cet ,Whale ,1.7,-7,6
Chamaeleon ,Cha ,Chameleon ,11,-79,4
Circinus ,Cir ,Compasses ,14.8,-62,4
Columba ,Col ,Dove ,5.8,-35,4
Coma Berenices ,Com ,Berenice's Hair ,12.4,22.5,4
Corona Australis ,CrA ,Southern Crown ,18.6,-42,3
Corona Borealis ,CrB ,Northern Crown ,15.8,33,4
Corvus ,Crv ,Crow ,12.4,-18,4
Crater ,Crt ,Cup ,11.4,-16,4
Crux ,Cru ,Southern Cross ,13.2,-60.8,4
Cygnus ,Cyg ,Swan ,19.95,40.8,5
Delphinus ,Del ,Dolphin ,20.5,12,3
Dorado ,Dor ,Goldfish ,5.1,-60,4
Draco ,Dra ,Dragon ,16.5,72,5
Equuleus ,Equ ,Little Horse ,21.2,8,3
Eridanus ,Eri ,River ,3.8,-30,6
Fornax ,For ,Furnace ,2.7,-32,4
Gemini ,Gem ,Twins ,7,20,4
Grus ,Gru ,Crane ,22.5,-44,4
Hercules ,Her ,Hercules ,17.55,30,5
Horologium ,Hor ,Clock ,3.3,-53,4
Hydra ,Hya ,Hydra (Sea Serpent) ,11.15,-15,10
Hydrus ,Hyi ,Water Serpent (male) ,2.5,-70,4
Indus ,Ind ,Indian ,21.5,-60,4
Lacerta ,Lac ,Lizard ,22.5,46,4
Leo ,Leo ,Lion ,10.8,20,4
Leo Minor ,LMi ,Smaller Lion ,10.3,32,4
Lepus ,Lep ,Hare ,5.6,-18,4
Libra ,Lib ,Balance ,15.2,-17,4
Lupus ,Lup ,Wolf ,15.3,-41,4
Lynx ,Lyn ,Lynx ,8.2,47,4
Lyra ,Lyr ,Lyre ,18.8,37,3
Mensa ,Men ,Table ,5.7,-77,4
Microscopium ,Mic ,Microscope ,21.15,-37,3
Monoceros ,Mon ,Unicorn ,6.7,-3.5,4
Musca ,Mus ,Fly ,12.6,-70,4
Norma ,Nor ,Square ,16,-50,4
Octans ,Oct ,Octant ,22,-85,4
Ophiucus ,Oph ,Serpent Holder ,17.3,-9,6
Orion ,Ori ,Orion ,5.8,0,4
Pavo ,Pav ,Peacock ,19.5,-67,4
Pegasus ,Peg ,Winged Horse ,22.7,20,6
Perseus ,Per ,Perseus ,3.6,47,4
Phoenix ,Phe ,Phoenix ,0.7,-49,5
Pictor ,Pic ,Easel ,5.6,-54,4
Pisces ,Psc ,Fishes ,0.5,14,6
Pisces Austrinus ,PsA ,Southern Fish ,22.3,-31,4
Puppis ,Pup ,Stern ,7.6,-31,4
Pyxis ,Pyx ,Compass ,8.95,-30,4
Reticulum ,Ret ,Reticle ,3.9,-60,3
Sagitta ,Sge ,Arrow ,19.6,15,4
Sagittarius ,Sgr ,Archer ,18.5,-27,4
Scorpius ,Sco ,Scorpion ,16.8,-30,4
Sculptor ,Scl ,Sculptor ,0.5,-32,5
Scutum ,Sct ,Shield ,18.7,-10,3
Serpens ,Ser ,Serpent ,17.1,2,6.5
Sextans ,Sex ,Sextant ,10.2,-1,4
Taurus ,Tau ,Bull ,4.6,18,4
Telescopium ,Tel ,Telescope ,19.3,-52,4
Triangulum ,Tri ,Triangle ,2.2,33,4
Triangulum Australe ,TrA ,Southern Triangle ,16,-65,3
Tucana ,Tuc ,Toucan ,23.7,-67,4
Ursa Major ,UMa ,Great Bear ,11.5,55,6
Ursa Minor ,UMi ,Little Bear ,15,78,4
Vela ,Vel ,Sails ,9.6,-48,4
Virgo ,Vir ,Virgin ,13,3,5
Volans ,Vol ,Flying Fish ,7.8,-70,4
Vulpecula ,Vul ,Fox ,20.2,25,4

'''
#efemerides:
# https://ssd.jpl.nasa.gov/horizons.cgi



# novo modulo python:
# https://rhodesmill.org/skyfield/

# nome dos planetas:
# http://docs.astropy.org/en/stable/api/astropy.coordinates.get_body.html?highlight=jupiter

# constelattion: 
# http://docs.astropy.org/en/stable/api/astropy.coordinates.SkyCoord.html#astropy.coordinates.SkyCoord.get_constellation


# http://docs.astropy.org/en/stable/api/astropy.coordinates.get_constellation.html#astropy.coordinates.get_constellation


import readline
for i in range(readline.get_current_history_length()):
...     print (readline.get_history_item(i + 1))

import astropy
astropy.coordinates.get_constellation('Jupiter')
astropy.coordinates.get_constellation('Jupiter')
astropy.coordinates.get_constellation('Mars')
astropy.coordinates.get_constellation('mars')


from skyfield.api import load
ts = load.timescale()
planets = load('de421.bsp')
print(planets)

from skyfield.api import Topos, load

ts = load.timescale()
ts

t = ts.now()
t

mars = planets['mars']
mars
earth = planets['earth']
earth
astrometric = earth.at(t).observe(mars)
astrometric


medida = earth.at(t).observe(mars)

apparent = earth.at(t).observe(mars).apparent()
apparent
astrometric = earth.observe(mars)
apparent = earth.at(t).observe(mars).apparent()
apparent = earth.at(t).observe(mars)
apparent
print(apparent)


t = ts.utc(2018, 12, 16)	# aqui podia ser 3 variáveis: ano, mes, dia - sendo mudadas por um laço!!!
t = ts.utc()

print(earth.at(t).position.au)
print(mars.at(t).position.au)


astrometric = earth.at(ts.utc(2018,12,16)).observe(mars)
print(astrometric.position.au)

ra, dec, distance = astrometric.radec()



print(ra.hstr())
print(dec.dstr())
print(distance)
app = astrometric.apparent()
alt, az, distance = app.altaz()
app
alt.dstr()
print(alt.dstr())
alt, az, distance = astronomic.altaz()
alt, az, distance = astronometric.altaz()
astrometric
alt, az, distance = astrometric.altaz()



---------------------------
>>> from skyfield.api import load
>>> ts = load.timescale()
>>> planets = load('de421.bsp')
>>> t = ts.now()
>>> 
>>> mars = planets['mars']
>>> earth = planets['earth']
>>> 
>>> medida = earth.at(t).observe(mars)
>>> 
>>> ra, dec, distance = medida.radec()
>>> 

>>> print(medida.position)
[ 1.10968811 -0.19018788 -0.09740996] au
>>> 
>>> print(medida.position.au)
[ 1.10968811 -0.19018788 -0.09740996]
>>> 
>>> print(medida.velocity)
[0.01045855 0.01016793 0.00489107] au/day


>>> print(ra.hstr())	# ou apenas print(ra)
23h 21m 05.92s

>>> print(dec.dstr())	# ou apenas print(dec)
-04deg 56' 41.7"

>>> print(distance)	# 
1.13007 au

-----------------------------------

>>> from skyfield.api import load
>>> ts = load.timescale()
>>> planetas = load('de421.bsp')
>>> t = ts.now()

>>> venus = planetas['venus']
>>> terra = planetas['earth']
>>> terra_venus = terra.at(t).observe(venus)

>>> terra_venus.radec()
(<Angle 14h 30m 07.99s>, <Angle -11deg 44' 25.9">, <Distance 0.516115 au>)


# Tente isso: 
>>> terra_venus.radec()[0]
<Angle 14h 30m 07.99s>
>>> 
>>> 
>>> terra_venus.radec()[1]
<Angle -11deg 44' 25.9">
>>> 
>>> 
>>> terra_venus.radec()[2]
<Distance 0.516115 au>


# Faremos melhor que acima! A lista tranferimos para 3 variáveis:
>>> ra, dec, distancia = terra_venus.radec()
 

>>> print(ra)
14h 30m 07.99s

>>> print(dec)
-11deg 44' 25.9"

>>> print(distancia)
0.516115 au


# Exemplos para laços:
terra_venus = earth.at(ts.utc(2018,12,16)).observe(mars)
terra_venus = earth.at(ts.utc(ano,mes,dia)).observe(mars)

-----------------------------------

 
# FONTE: https://pypi.org/project/skyfield/ (ABAIXO):


from skyfield.api import load

planets = load('de421.bsp')
earth, mars = planets['earth'], planets['mars']

ts = load.timescale()
t = ts.now()
position = earth.at(t).observe(mars)
ra, dec, distance = position.radec()

print(ra)
print(dec)
print(distance)


# EXEMPLOS COM LAÇO:
ano = 2020
mes = 6
>>> for dia in range(30):
...     terra_venus = earth.at(ts.utc(ano, mes, dia)).observe(venus)
...     print(dia, end='')
...     terra_venus.radec()
... 









