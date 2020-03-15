# Práctica Final KeepCoding BootCamp 0

**Cómo funciona**
Se crea un simulador de inversiones en Cryptomonedas con Python. 

Las instrucciones para ejecutar el proyecto son:
1. Clonar el proyecto en local o descargarse el zip
2. Se puede ejecutar de 2 formas:
	- A través de Visual Studio Code: una vez se tenga el proyecto en local, deberá abrirse en VSC situarse en el archivo main.py y ejecutarlo.
	- A través del terminal (CMD): a través del terminal, habrá que acceder a la carpeta donde esté alojado el proyecto y ejecutar el comando "python main.py".

**El proyecto**

El proyecto se divide en 3 partes:

 1. Tabla: aparecerán los valores que queramos añadir con la fecha, hora, la moneda que queremos cambiar, la cantidad de la moneda, la moneda a la que queramos hacer el cambio junto con su cantidad y precio unitario. En esta sección encontramos 2 botones:
	 - Nueva transacción: habilita la parte "Nueva Transacción".
	 - Clear: elimina todos los registros de la tabla.

  

 2. Nueva transacción: en esta parte del proyecto se realizarán cálculos (para visualizar la conversión entre las monedas y el precio unitario de la moneda elegida). El funcionamiento de los botones es el siguiente:
	 - Calcular: muestra la cantidad de las monedas y el precio unitario de la que quiero cambiar.
	 - Cancelar: cancela el cálculo.
	 - Aceptar: añade los valores calculados a la tabla.

3. Inversión €: se encuentra el botón calcular. Cuando se pulsa, programa hace una equivalencia de los euros invertidos en compra de cryptomonedas y el valor actual en euros de todos los cambios a cryptomonedas . 

**Cómo funciona la base de datos**

Se ha creado la aplicación con Python 3.7. Para la gestión de la Base de Datos se ha utilizado SQLite3 y se crea automáticamente siguiento las indicaciones del archivo "schema.sql".   

