import os

FOLDER = "/xampp/"
print("skusiam soamriny")
def listdir(cesta,spaces=0):
    try:
        d = os.listdir(cesta)
    except PermissionError:
        print("RISKO JE SKAREDY A TU NEMAS PRISTUP")
        return
    for i in d:
        this_path = cesta + "/" + i
        this_path = os.path.abspath((this_path))
        isdir = os.path.isdir(this_path)

        if isdir:

            print(f"{(spaces+13) * ' '}{i}/")

            listdir(this_path,spaces+3)
        else:
            size = os.path.getsize(this_path)
            print(f"{size:10}{(spaces+3)* ' '}{i}")
if __name__ == "__main__":
    listdir(FOLDER)