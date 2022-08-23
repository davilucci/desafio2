import os
import shutil

os.makedirs("foo/dummy")
os.makedirs("foo/empty")

archivo = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "file1.txt"), "w")
archivo = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "file2.txt"), "w")
with open("file1.txt","w") as file:
    file.write("No me gusta bash, prefiero PYTHON! JAJAJAJAJAJAJAJ\n")
    
shutil.move("file1.txt", "foo/dummy")
shutil.move("file2.txt", "foo/dummy")



### os.path.realpath(__file__) nos devuelve la ruta absoluta del script actual.

### os.path.dirname() nos da la ruta de la carpeta.

### os.path.join() une las rutas utilizando el separador del sistema.

### Como resultado tendrás la ruta absoluta del archivo de destino###
    
