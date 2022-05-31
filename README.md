# Tracker

Pasos para ejecutar el proyecto con Docker:

1) Bajar el repositorio mediante: GIT CLONE  https://github.com/PabloVitelli/Tracker
2) El video a analizar se encuentra dentro de la carpeta "Proyecto" con el nombre "input.mkv"
3) Las condiciones iniciales son cargadas del archivo "initial_conditions.json"
4) Se ejecutara la imagen Docker dentro de la carpeta "Proyecto": docker run -v "$(pwd)/:/app" proyecto
5) El software generara un video en la carpeta "Proyecto" con el nombre de "tracking.mp4"

Pasos para ejecutar el proyecto en un enviroment Anaconda:
1) Bajar el repositorio mediante: GIT CLONE  https://github.com/PabloVitelli/Tracker
2) Crear un enviroment con Anaconda: conda create --name Envi Python=3.8
3) Instalar las dependencias de "requirement.txt"
4) El video a analizar se encuentra dentro de la carpeta "Proyecto" con el nombre "input.mkv"
5) Las condiciones iniciales son cargadas del archivo "initial_conditions.json"
6) El software generara un video en la carpeta "Proyecto" con el nombre de "tracking.mp4"

#
Ejemplo de Salida del tracker:

![Futbol](https://user-images.githubusercontent.com/54893624/171250191-d7b66af6-e480-4252-9161-d8d1eadaf544.gif)
