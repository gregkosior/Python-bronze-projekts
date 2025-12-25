# dane projektu obliczenia matematyczne i dzialania na tekscie program bedzie wykonywal obliczenia 
# dla zestawuw liczb calkowitych i zmieno przecinkowych 

Kurs = "Gdansk","Gdynia"
cena = 4 #cena za jeden km
Podatek = 20 #praczent jaki bierze korpo
cena_klijenta = 5 #cena klijenta za 1 km
odleglosc =  21 #jaka jest odleglosc z gdanska do gsyni
# chcemy obliczyc ile zarobim za kurs 
wynik = cena * odleglosc
print(wynik)
wynik2= wynik * Podatek /100
print(wynik2)
wynik3 = wynik -wynik2
print(wynik3)
wynik4 = cena_klijenta * odleglosc
print(wynik4)


print ("Jazda do gadnska \n","Wysla cenowo",wynik4,"\nja zarobilem po podatku ",wynik3)