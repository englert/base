import os
import pytest
import math
import random
from unittest.mock import patch

#from feladatsor import utolso_karakter, negativok_kivalogatasa
#from feladatsor import lista_atlag, negativok_szama, szorzat
#from feladatsor import Teglalap
#from feladatsor import pozitiv_szamok_a_fajlbol

# Tesztelés a kisebb függvénnyel
from feladatsor import kisebb
# A mock segítségével ellenőrizhető, a min függvény tiltott használata.
#from unittest.mock import patch
def test_kisebb():
    with patch('feladatsor.min', side_effect=Exception("A min() függvény használata itt tiltott!")) as mock_min:
        assert kisebb(7,2) == 2
        assert kisebb(2,7) == 2
        assert kisebb(-5, 5) == -5
        assert kisebb(5, -5) == -5
        assert kisebb(0, 0) == 0
        assert kisebb(3.14, 2.71) == 2.71
        assert kisebb(2.71, 3.14) == 2.71

# Tesztelés az abszolut függvénnyel
from feladatsor import abszolut
def test_abszolut():
    # A mock patch segítségével ellenőrizhető, az abs függvény tiltott használata.
    with patch('feladatsor.abs', side_effect=Exception("Az abs() függvény használata itt tiltott!")) as mock_abs:
        assert abszolut(5) == 5
        assert abszolut(-5) == 5
        assert abszolut(0) == 0
        assert abszolut(3.14) == 3.14
        assert abszolut(-3.14) == 3.14
        assert abszolut(2.71) == 2.71
        assert abszolut(-2.71) == 2.71
         

# Tesztelés a hattal_oszthato függvénnyel
from feladatsor import hattal_oszthato
def test_hattal_oszthato():
    assert hattal_oszthato(6) == True
    assert hattal_oszthato(12) == True
    assert hattal_oszthato(18) == True
    assert hattal_oszthato(24) == True
    assert hattal_oszthato(31) == False
    assert hattal_oszthato(0) == True  # 0 is osztható 6-tal
    assert hattal_oszthato(-6) == True
    assert hattal_oszthato(-12) == True
    assert hattal_oszthato(-18) == True
    assert hattal_oszthato(-24) == True
    assert hattal_oszthato(-31) == False
    assert hattal_oszthato(7) == False

# Tesztelés a maradek függvénnyel
from feladatsor import maradek
def test_maradek():
    assert maradek(10, 3) == 1
    assert maradek(10, 5) == 0
    assert maradek(10, 0) == None  # Nullával való osztás elkerülése
    assert maradek(10, -3) == -2
    assert maradek(-10, -3) == -1
    assert maradek(0, 5) == 0
    assert maradek(5, 5) == 0

# Tesztelés a legnagyobb függvénnyel
from feladatsor import legnagyobb
def test_legnagyobb():
    with patch('feladatsor.max', side_effect=Exception("A max() függvény használata itt tiltott!")) as mock_max:
        assert legnagyobb([1, 2, 3]) == 3
        assert legnagyobb([-1, -2, -3]) == -1
        assert legnagyobb([5, 5, 5]) == 5
        assert legnagyobb([1.1, 2.2, 3.3]) == 3.3
        assert legnagyobb([-1.1, -2.2, -3.3]) == -1.1
        assert legnagyobb([]) is None

# Tesztelés az osszeg függvénnyel
from feladatsor import osszeg
def test_osszeg():
    with patch('feladatsor.sum', side_effect=Exception("A sum() függvény használata itt tiltott!")) as mock_sum:
        assert osszeg([1, 2, 3]) == 6
        assert osszeg([-1, -2, -3]) == -6
        assert osszeg([5, 5, 5]) == 15
        assert osszeg([1.1, 2.2, 3.3]) == 6.6
        assert osszeg([-1.1, -2.2, -3.3]) == -6.6
        assert osszeg([]) == 0
        assert osszeg([0]) == 0
        assert osszeg([1000000, -1000000]) == 0

# Tesztelés az utolso_karakter függvénnyel
from feladatsor import utolso_karakter
def test_utolso_karakter(): 
    assert utolso_karakter("hello") == "o"
    assert utolso_karakter("world") == "d"
    assert utolso_karakter("") is None  # Üres string esetén None
    assert utolso_karakter("Python") == "n"
    assert utolso_karakter("12345") == "5"
    assert utolso_karakter("!@#$%^&*()") == ")"
    assert utolso_karakter(" ") == " "  # Egyetlen szókör esetén is visszaadja a szóközt
    assert utolso_karakter("a") == "a"  # Egyetlen karakter esetén is visszaadja
    assert utolso_karakter("é") == "é"  # Ékezett karakter esetén is visszaadja

# Tesztelés a negativok_kivalogatasa függvénnyel
from feladatsor import negativok_kivalogatasa    
def test_negativok_kivalogatasa():
    assert negativok_kivalogatasa([1, -2, 3, -4, 5]) == [-2, -4]
    assert negativok_kivalogatasa([-1, -2, -3]) == [-1, -2, -3]
    assert negativok_kivalogatasa([1, 2, 3]) == []
    assert negativok_kivalogatasa([]) == []
    assert negativok_kivalogatasa([-5, 0, 5]) == [-5]
    assert negativok_kivalogatasa([0]) == []
    assert negativok_kivalogatasa([-10, -20, 30]) == [-10, -20] 

# Tesztelés a lista_atlag függvénnyel
from feladatsor import lista_atlag
def test_lista_atlag():
    assert lista_atlag([1, 2, 3]) == 2.0
    assert lista_atlag([-1, -2, -3]) == -2.0
    assert lista_atlag([5, 5, 5]) == 5.0
    assert round(lista_atlag([1.1, 2.2, 3.3]),4) == 2.2
    assert round(lista_atlag([-1.1, -2.2, -3.3]),4) == -2.2
    assert lista_atlag([]) is None  # Üres lista esetén None
    assert lista_atlag([0]) == 0.0
    assert lista_atlag([1000000, -1000000]) == 0.0
    assert lista_atlag([1, 2, 3, 4, 5]) == 3.0  

# Tesztelés a negativok_szama függvénnyel
from feladatsor import negativok_szama
def test_negativok_szama(): 
    assert negativok_szama([1, -2, 3, -4, 5]) == 2
    assert negativok_szama([-1, -2, -3]) == 3
    assert negativok_szama([1, 2, 3]) == 0
    assert negativok_szama([]) == 0
    assert negativok_szama([-5, 0, 5]) == 1
    assert negativok_szama([0]) == 0
    assert negativok_szama([-10, -20, 30]) == 2     

# Tesztelés a szorzat függvénnyel
from feladatsor import szorzat
def test_szorzat():
    assert szorzat([1, 2, 3]) == 6
    assert szorzat([-1, -2, -3]) == -6
    assert szorzat([5, 5, 5]) == 125
    assert round(szorzat([1.1, 2.2, 3.3]),4) == 7.986
    assert round(szorzat([-1.1, -2.2, -3.3]),4) == -7.986
    assert szorzat([]) == 1  # Üres lista esetén az eredmény 1
    assert szorzat([0]) == 0  # Egyetlen nulla esetén az eredmény nulla
    assert szorzat([1000000, -1000000]) == -1000000000000

# Tesztelés a Teglalap osztály terulet, kerulet és atfogo metódusaival
from feladatsor import Teglalap
def test_teglalap_terulet():  
    teglalap = Teglalap(5, 10)
    assert teglalap.terulet() == 50
    teglalap2 = Teglalap(3, 4)
    assert teglalap2.terulet() == 12

def test_teglalap_kerulet():    
    teglalap = Teglalap(5, 10)
    assert teglalap.kerulet() == 30
    teglalap2 = Teglalap(3, 4)
    assert teglalap2.kerulet() == 14

def test_teglalap_atfogo():
    teglalap = Teglalap(5, 10)
    assert round(teglalap.atfogo(), 2) == 11.18  # √(5² + 10²) = √125 ≈ 11.18
    teglalap2 = Teglalap(3, 4)
    assert round(teglalap2.atfogo(), 2) == 5.0  # √(3² + 4²) = √25 = 5.0

# Tesztelés szaz_szam_fajlba függvénnyel
from feladatsor import szaz_szam_fajlba
def test_szaz_szam_fajlba(tmp_path):
    # A tmp_path egy ideiglenes könyvtárat biztosít a teszteléshez
    fajl_nev = tmp_path / "szamok.txt"
    szaz_szam_fajlba(fajl_nev)  # Meghívjuk a függvényt, hogy írja ki a számokat a fájlba

    # Ellenőrizzük, hogy a fájl létezik-e
    assert fajl_nev.exists()

    # Ellenőrizzük, hogy a fájl tartalma helyes-e
    with open(fajl_nev, 'r') as fajl:
        sorok = fajl.readlines()
        assert len(sorok) == 100  # 100 számot kell tartalmaznia
        for i in range(1, 101):
            assert sorok[i-1].strip() == str(i)  # Minden sorban az i számnak kell lennie

# Tesztelés utolso_karakter_a_fajlban   
from feladatsor import utolso_karakter_a_fajlban
def test_utolso_karakter_a_fajlban(tmp_path):
    # A tmp_path egy ideiglenes könyvtárat biztosít a teszteléshez
    fajl_nev = tmp_path / "szoveg.txt"
    
    # Létrehozunk egy fájlt, amely tartalmazza a tesztelendő szöveget
    with open(fajl_nev, 'w') as fajl:
        fajl.write("Hello, World!\n")
        fajl.write("Python tesztelés.\n")
        fajl.write("Ez az utolsó sor.")

    # Meghívjuk a függvényt, hogy olvassa ki az utolsó karaktert
    assert utolso_karakter_a_fajlban(fajl_nev) == '.' 
    # Létrehozunk egy fájlt, amely tartalmazza a tesztelendő szöveget
    with open(fajl_nev, 'w') as fajl:
        fajl.write("Hello!\n")
        fajl.write("tesztelés.\n")
        fajl.write("Ez az utolsó sor!")

    # Meghívjuk a függvényt, hogy olvassa ki az utolsó karaktert
    assert utolso_karakter_a_fajlban(fajl_nev) == '!'       

# Tesztelés a faktorialis függvénnyel
from feladatsor import faktorialis
def test_faktorialis():
    assert faktorialis(5) == 120  # 5! = 5 * 4 * 3 * 2 * 1 = 120
    assert faktorialis(0) == 1    # 0! = 1
    assert faktorialis(1) == 1    # 1! = 1
    assert faktorialis(3) == 6    # 3! = 3 * 2 * 1 = 6
    assert faktorialis(-5) is None # Negatív szám esetén None
    assert faktorialis(10) == 3628800 # 10! = 3628800
    assert faktorialis(20) == 2432902008176640000  #

# Tesztelés a szamok_osszege_a_fajlban függvénnyel
from feladatsor import szamok_osszege_a_fajlban
def test_szamok_osszege_a_fajlban(tmp_path):
    # A tmp_path egy ideiglenes könyvtárat biztosít a teszteléshez
    fajl_nev = tmp_path / "szamok.txt"
    
    # Létrehozunk egy fájlt, amely tartalmazza a tesztelendő számokat
    with open(fajl_nev, 'w') as fajl:
        for i in range(1, 101):
            fajl.write(f"{i}\n")  # Minden számot új sorba írunk

    # Meghívjuk a függvényt, hogy olvassa ki a számok összegét
    assert szamok_osszege_a_fajlban(fajl_nev) == 5050  # 1 + 2 + ... + 100 = 5050       

# Tesztelés a szamok_atlaga_a_fajlban függvénnyel
from feladatsor import szamok_atlaga_a_fajlban
def test_szamok_atlaga_a_fajlban(tmp_path): 
    # A tmp_path egy ideiglenes könyvtárat biztosít a teszteléshez
    fajl_nev = tmp_path / "szamok.txt"
    
    # Létrehozunk egy fájlt, amely tartalmazza a tesztelendő számokat
    with open(fajl_nev, 'w') as fajl:
        for i in range(1, 101):
            fajl.write(f"{i}\n")  # Minden számot új sorba írunk

    # Meghívjuk a függvényt, hogy olvassa ki a számok átlagát
    assert szamok_atlaga_a_fajlban(fajl_nev) == 50.5  # (1 + 2 + ... + 100) / 100 = 50.5  
    # Létrehozunk egy fájlt, amely tartalmazza a tesztelendő számokat
    with open(fajl_nev, 'w') as fajl:
        for i in range(1, 102):
            fajl.write(f"{i}\n")  # Minden számot új sorba írunk

    # Meghívjuk a függvényt, hogy olvassa ki a számok átlagát
    assert szamok_atlaga_a_fajlban(fajl_nev) == 51  # (1 + 2 + ... + 100) / 100 = 51  

# Tesztelés a szamok_szama_a_fajlban függvénnyel
from feladatsor import szamok_szama_a_fajlban
def test_szamok_szama_a_fajlban(tmp_path):
    # A tmp_path egy ideiglenes könyvtárat biztosít a teszteléshez
    fajl_nev = tmp_path / "szamok.txt"
    
    # Létrehozunk egy fájlt, amely tartalmazza a tesztelendő számokat
    with open(fajl_nev, 'w') as fajl:
        for i in range(1, 101):
            fajl.write(f"{i}\n")  # Minden számot új sorba írunk

    # Meghívjuk a függvényt, hogy olvassa ki a számok számát
    assert szamok_szama_a_fajlban(fajl_nev) == 100  # 100 szám van a fájlban   
# Létrehozunk egy fájlt, amely tartalmazza a tesztelendő számokat
    with open(fajl_nev, 'w') as fajl:
        for i in range(1, 102):
            fajl.write(f"{i}\n")  # Minden számot új sorba írunk

    # Meghívjuk a függvényt, hogy olvassa ki a számok számát
    assert szamok_szama_a_fajlban(fajl_nev) == 101  # 100 szám van a fájlban  

# A teszteléshez szükséges pytest csomag importálása
import pytest   


# A tesztek futtatása
if __name__ == "__main__":
    pytest.main([os.path.basename(__file__)])
    # A pytest.main() hívás automatikusan futtatja a teszteket
    # A fájl nevét át kell adni, hogy a pytest megtalálja
    # A pytest automatikusan észleli a tesztfüggvényeket,
    # amelyek 'test_' előtaggal kezdődnek
    # és futtatja azokat.       
    
# A pytest futtatása a parancssorból: pytest test_feladatsor.py