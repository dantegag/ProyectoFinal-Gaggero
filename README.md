# Pagina
TuPrimeraPagina+Gaggero
✅ Instrucciones para correr el proyecto Django

1. Clonar el repositorio
git clone https://github.com/tu_usuario/TuPrimeraPagina-Gaggero.git
cd TuPrimeraPagina-Gaggero
2. Crear el entorno virtual
En Windows:

python -m venv venv
venv\Scripts\activate
En macOS/Linux:

python3 -m venv venv
source venv/bin/activate
3. Instalar dependencias
pip install -r requirements.txt


pip freeze > requirements.txt
4. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate
5. Cargar datos iniciales (películas, directores, géneros)
Opción A: usando el script datos.py (más flexible)

python manage.py shell < datos.py


* Orden sugerido para probar la aplicación
Ingresar a /directores/ y agregar algunos directores.

Ir a /generos/ y crear algunos géneros.

Ir a /peliculas/ y agregar películas utilizando los directores y géneros creados.

Finalmente, en la página principal (/), usar el buscador para buscar por título o por nombre del director.


¿Dónde están las funcionalidades?

Página principal: /
Formulario de búsqueda.

Se puede buscar por nombre de película o por director.

Muestra los resultados coincidentes.

Películas: /peliculas/
Formulario para agregar nuevas películas.

Lista de todas las películas cargadas.

Directores: /directores/
Formulario para agregar directores (nombre y nacionalidad).

Lista de directores disponibles.

Géneros: /generos/
Formulario para agregar géneros (acción, drama, etc).

Lista de géneros.
