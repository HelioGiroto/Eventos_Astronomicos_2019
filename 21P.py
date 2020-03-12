
line = '21P/Giacobini-Zinner,e,32.0059,195.3730,172.8480,3.496349,0.1507585,0.71054100,82.7184,03/12.0/2020,2000,g  9.0,6.0'

yh = ephem.readdb(line)

print(yh)

yh.compute('2020/03/12')
 
print(yh.earth_distance)

print(yh.mag)

yh.compute('2018/10/10')
 
print(yh.earth_distance)

print(yh.mag)
76.21
 

# fonts: 
# https://minorplanetcenter.net/iau/Ephemerides/Comets/Soft03Cmt.txt
# https://rhodesmill.org/pyephem/quick.html

