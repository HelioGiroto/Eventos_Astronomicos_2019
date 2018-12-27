#!/usr/bin/python3
#coding: utf-8
# Este Script calculará a distância entre a Lua e a Terra nos 365 dias de 2019.

import ephem			# Instalar este módulo com PIP - Ver: https://pypi.python.org/pypi/ephem/
lua = ephem.Moon()		# Objeto (Lua) a ser pesquisado).
dia = ephem.Date('2019/01/01')	# data convertida em aaaa/mm/dd

print()

arq=open("moon_au_2019.csv", "a+")	# Este será o arquivo CSV que todos os dados estarão impressos

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


# Para ver lista das 50 maiores aproximações (menor distância) entre a Lua e Terra:
# $ sort -nk2 moon_au_2019.csv | head -n50

# Lista do maior PERIGEU (+ próx.) de cada mês (ordenados por mês):
# $ for i in $(seq 1 12); do grep "/${i}/" moon_au_2019.csv | sort -nk2 | head -n1; done

# Lista dos maiores PERIGEUS (+ próx) do ano (um por mês ordenados por UA):
# $ for i in $(seq 1 12); do grep "/${i}/" moon_au_2019.csv | sort -nk2 | head -n1; done | sort -nk2

# Autor: Helio Giroto
