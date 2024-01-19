import aux_functions as au
from astropy.coordinates import get_sun, EarthLocation, AltAz, get_moon
from astropy.time import Time
import numpy as np

arquivos = au.main_archives()

for arquivo in arquivos:
    with open(arquivo, 'r') as file:
        linhas = file.readlines()
        coordenadas, tempo = linhas[4:7], linhas[8:]
        coordenadas = [float(i.split(';')[1]) for i in coordenadas]
        tempo = [i[:16].replace(';', ' ') + ':00' for i in tempo]

    localizacao = EarthLocation(lat= coordenadas[0], lon= coordenadas[1],
                                height= coordenadas[2])

    tempo = [Time(i, scale='utc', location=localizacao) for i in tempo]

    info_sol =[get_sun(i).transform_to(AltAz(obstime= tempo, location=localizacao)) for i in tempo]
    altitude_sol = [i.alt.deg for i in info_sol]
    azimuth_sol = [i.az.deg for i in info_sol]
    distancia_sol = [i.distance for i in info_sol]

    print(altitude_sol[0], azimuth_sol[0], distancia_sol[0])
