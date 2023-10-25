import modul
import mod2.modul    #furt najprv zavola init v priecinku

def funkcia():
    print("main.py: funkcia")

print("main.py: start")

if __name__ == "__main__":
    print("main.py: __main__")
    funkcia()
    modul.funkcia()
    mod2.modul.funkcia()