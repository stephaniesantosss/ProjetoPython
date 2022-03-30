from pygeocoder import Geocoder

endereco = '1222, Lins de Vasconcelos, Sao Paulo, SP'

print(Geocoder('AIzaSyASoDbwBH-dZLFRQm55lzB-Non1qWTXTBs').geocode(endereco).coordinates)
