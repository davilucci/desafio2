#!/bin/bash

#descargando contenido de la pagina.

echo "descarga"

wget https://es.wikipedia.org/wiki/DevOps



#buscar palabra

read -p "Introduzca la palabra a buscar:   " palabra



grep -n $palabra /home/adrr/Documents/GIT/BOOTCAMP/bootcamp-2-challenge/Retos
