# 1. -------------------------- (2 pont)
def kisebb(szam1, szam2):
    ''' A függvény két számot kap argumentumként 
    és visszatér a kisebbik számmal.

    Nem használhatod a min nevű függvényt!
    '''
    ... # Itt kell implementálni a kisebb függvényt
    
      


# 2. -------------------------- (2 pont)
def abszolut(szam): 
    ''' A függvény visszatér a szam abszolút értékével.
    Nem használhatod az abs nevű függvényt!
    '''
    ... # Itt kell implementálni az abszolut függvényt
    


# 3. -------------------------- (2 pont)
def hattal_oszthato(szam):  
    ''' A függvény visszatér True-val, ha a szam hattal osztható, 
    és False-al, ha nem.
    '''
    ... # Itt kell implementálni a hattal_oszthato függvényt
     
    
# 4. -------------------------- (2 pont)
def maradek(szam1, szam2):
    ''' A függvény visszatér a szam1 és szam2 hányadosának maradékával.
    Nullával való osztás esetén térjen vissza None-nal.
    '''
    


# 5. -------------------------- (2 pont)
def legnagyobb(lista):
    '''    A függvény visszatér a lista legnagyobb számával.
    Ha a lista üres, akkor None-t ad vissza.
    Nem használhatod a max nevű függvényt!
    '''
    ... # Itt kell implementálni a legnagyobb függvényt
    

# 6. -------------------------- (2 pont)
def osszeg(lista):
    ''' A függvény visszatér a lista elemeinek összegével.
    Ha a lista üres, akkor 0-t ad vissza.
    Nem használhatod a sum nevű függvényt!
    '''
    ... # Itt kell implementálni az osszeg függvényt
     


# 7. -------------------------- (2 pont)
def utolso_karakter(text):
    ''' A függvény a text nevű string utolsó karakterét adja vissza.
    Ha a text üres, akkor None-t ad vissza.
    '''
    ... # Itt kell implementálni az utolso_karakter függvényt
     

# 8. -------------------------- (2 pont)
def negativok_kivalogatasa(lista): 
    ''' A függvény, visszatér egy listával, 
    amely a lista negatív számait tartalmazza.
    '''
    ... # Itt kell implementálni a negativok_kivalogatasa függvényt
               



# 9. -------------------------- (2 pont)   
def lista_atlag(lista):             
    '''  A függvény a listában levő számok átlagával tér vissza.
    Ha a lista üres, akkor None-t ad vissza.
    '''
    ... # Itt kell implementálni a lista_atlag függvényt
    

# 10. -------------------------- (2 pont)
def negativok_szama(lista):
    '''  A függvény, visszatér lista negativ számainak számával.
    Üres lista esetén 0 a visszatérési érték.
    '''
    ... # Itt kell implementálni a negativok_szama függvényt
    
# 11. -------------------------- (2 pont)
def szorzat(lista):
    '''  A függvény, visszatér a lista számainak szorzatával.
    Üres lista esetén 1 a visszatérési érték.
    '''
    ... # Itt kell implementálni a szorzat függvényt
    


# 12. 13. 14. -------------------------- 
'''
Feladat: Téglalap osztály definiálása. 
[Objektumorientált programozás]
Hozz létre egy osztályt Teglalap néven.
A Teglalap osztály lehetővé teszi a téglalap oldalhosszúságainak tárolását.
---- 12. -------------------------- 
A Teglalap osztály rendelkezik egy kerulet() nevü metódussal,   (2 pont) 
    amely az osztály segítségével létrehozott objektum metódusaként 
        visszaadja az adott objektum kerületét.
---- 13. -------------------------- 
A Teglalap osztály rendelkezik egy terulet() nevü metódussal, (2 pont) 
    amely az osztály segítségével létrehozott objektum metódusaként 
        visszaadja az adott objektum területét.
---- 14. -------------------------- 
A Teglalap osztály rendelkezik egy atfogo() nevü metódussal, (2 pont) 
    amely az osztály segítségével létrehozott objektum metódusaként 
        visszaadja az adott objektum átfogóját.
'''
class Teglalap:
    ... # Itt kell definiálni a Teglalap osztályt és a metódusokat


# 15. -------------------------- (2 pont)
def szaz_szam_fajlba(fajl_nev):
    ''' A függvény 1-től 100-ig egyesével kiírja a számokat egy fájlba.
    Minden szám kerüljön új sorba.
    A fájl nevét paraméterként kapja meg a függvény.
    '''
    ... # Itt kell implementálni a szaz_szam_fajlba függvényt
    
# 16. -------------------------- (2 pont)
def utolso_karakter_a_fajlban(fajl_nev):
    ''' A függvény visszatér a szövegfájl utolsó karakterével.
    A fájl nevét paraméterként kapja meg a függvény.
    '''
    ... # Itt kell implementálni az utolso_karakter_a_fajlban függvényt
    
# 17. -------------------------- (2 pont)
def faktorialis(szam):
    ''' A függvény visszatér az (egész) szam faktoriálisával.
    Például: 5! = 5 * 4 * 3 * 2 * 1 = 120
    Például: 0! = 1
    Negatív számnak nincs faktoriálisa, ebben az esetben térjen vissza None-nal.
    '''
    ... # Itt kell implementálni a faktorialis függvényt
    



# 18. -------------------------- (2 pont)
def szamok_osszege_a_fajlban(fajl_nev):     
    ''' A függvény visszatér a szövegfájlban levő számok összegével.
    Minden szám új sorban van a fájlban.
    '''
    ... # Itt kell implementálni a szamok_osszege_a_fajlban függvényt
    

# 19. -------------------------- (2 pont)
def szamok_atlaga_a_fajlban(fajl_nev):
    ''' A függvény visszatér a szövegfájlban levő egész számok átlagával.
    Minden szám új sorban van a fájlban.
    '''
    ... # Itt kell implementálni a szamok_atlaga_a_fajlban függvényt
    
# 20. -------------------------- (2 pont)
def szamok_szama_a_fajlban(fajl_nev):
    ''' A függvény visszatér a szövegfájlban levő egész számok számával.
    Minden szám új sorban van a fájlban.
    '''
    ... # Itt kell implementálni a szamok_szama_a_fajlban függvényt
          
