#RetoPassword

Es necesario contar con un virtualEnv de Python en el mismo directorio.

- El archivo validatron.py es el servidor flask que elige el password aleatorio y abre
  el endpoint para peticiones. Es necesario instalar Flask dentro del entorno virtual.
  El archivo validatron.py se ejecuta dentro del entorno virtual.

- El archivo peticiones.py es el archivo que arroja las peticiones con combinaciones hasta
  encontrar el password elegido al mismo servidor flask. Este se ejecuta en la terminal
  sin ningun entorno virtual.
