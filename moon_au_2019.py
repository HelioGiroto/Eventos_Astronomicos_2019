#!/usr/bin/python3
#coding: utf-8
# Este Script calculará a distância entre a Lua e a Terra nos 365 dias de 2019.

import ephem			# Instalar este módulo com PIP - Ver: https://pypi.python.org/pypi/ephem/
lua = ephem.Moon()		# Objeto (Lua) a ser pesquisado).
dia = ephem.Date('2019/01/01')	# data convertida em aaaa/mm/dd

print()

arq=open("moon_au_2019.csv", "a+")

for i in range(366):	
	data = ephem.Date(dia)					# Para não imprimir em data Linux, mas em formato aaaa/m/d		
	constelacao = ephem.constellation(ephem.Moon(dia))	# Nome da constelação em que a Lua será vista
	au = ephem.Moon(dia).earth_distance			# UA - distância da terra.
	
	arq.write( str(data) + str(";") + str(au) + str(";") + str(constelacao) )
	arq.write('\n')

	dia += 1	# Avança um dia e volta a realizar o laço de dias e anos até atingir o limite.

arq.close()
print('HOJE, a Lua está em:', ephem.constellation(ephem.Moon(ephem.now())), 'à', ephem.Moon(ephem.now()).earth_distance, 'UA da Terra.') 
print()


# Para ver lista das 50 maiores aproximações de Vênus da Terra.
# $ cat moon_au_2019.csv | sort -t';' -k3 | head -n50 | cat -n		
# Autor: Helio Giroto
