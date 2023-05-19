# Listas Multidimensionales
# Perseverance: es el robot que se envio a Martes


site = [
    ['@37.7897442', '-122.3900165, 17.7z', '18/05/2023 14:31'],
    ['@41.3809', '2.1202449,17z', '18/05/2023 14:31'],
    ['@40.4377968', '-3.9913462,11z', '18/05/2023 14:31'],
    ['@41.8902142', '12.489656,17z', '18/05/2023 14:31'],
    ['@-22.951911', '-43.2130621,17z', '18/05/2023 14:31'],
    ['@-13.2263255', '72.5021924,17z', '18/05/2023 14:31'],
    ['@40.4318222', '116.5604877,16.09z', '18/05/2023 14:31'],
    ['@30.3284555', '35.4253078, 15z', '18/05/2023 14:31'],
    ['@27.1751495', '78.0372498,17z', '18/05/2023 14:31'],
    ['@30.0444242', '31.2331367,17z', '18/05/2023 14:31']
]

indice_longitud = 0
indice_latitud = 1
indice_fecha = 2

# for coordenada in historial:
#     print(coordenada)

for i in range(len(site)):
    for j in range(len(site[i])):
        print(site[i][j])


# Como crear un array multidimensional desde cero
array_datos = [[]]
array_datos[0].append('Arturo')
array_datos[0].append('Cabrera')

array_datos.append([])
array_datos[1].append('gnuxdar')
array_datos[1].append('AC Tecnology')

array_datos.append([])
array_datos[2].append('Ecuador')
array_datos[2].append('Venezuela')
print(array_datos)
