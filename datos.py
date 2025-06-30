from posts.models import Director, Genero, Pelicula


generos = ['Drama', 'Acción', 'Comedia', 'Ciencia ficción', 'Aventura']
for g in generos:
    Genero.objects.get_or_create(nombre=g)


peliculas = [
    {"titulo": "El Padrino", "director": "Francis Ford Coppola", "nacionalidad": "EE.UU.", "genero": "Drama", "año": 1972},
    {"titulo": "Pulp Fiction", "director": "Quentin Tarantino", "nacionalidad": "EE.UU.", "genero": "Drama", "año": 1994},
    {"titulo": "El caballero oscuro", "director": "Christopher Nolan", "nacionalidad": "Reino Unido", "genero": "Acción", "año": 2008},
    {"titulo": "Forrest Gump", "director": "Robert Zemeckis", "nacionalidad": "EE.UU.", "genero": "Comedia", "año": 1994},
    {"titulo": "Matrix", "director": "Lana Wachowski", "nacionalidad": "EE.UU.", "genero": "Ciencia ficción", "año": 1999},
    {"titulo": "Titanic", "director": "James Cameron", "nacionalidad": "Canadá", "genero": "Drama", "año": 1997},
    {"titulo": "Inception", "director": "Christopher Nolan", "nacionalidad": "Reino Unido", "genero": "Ciencia ficción", "año": 2010},
    {"titulo": "Parásitos", "director": "Bong Joon-ho", "nacionalidad": "Corea del Sur", "genero": "Drama", "año": 2019},
    {"titulo": "Star Wars", "director": "George Lucas", "nacionalidad": "EE.UU.", "genero": "Ciencia ficción", "año": 1977},
    {"titulo": "Gladiador", "director": "Ridley Scott", "nacionalidad": "Reino Unido", "genero": "Acción", "año": 2000},
    {"titulo": "La La Land", "director": "Damien Chazelle", "nacionalidad": "EE.UU.", "genero": "Drama", "año": 2016},
    {"titulo": "El Señor de los Anillos", "director": "Peter Jackson", "nacionalidad": "Nueva Zelanda", "genero": "Aventura", "año": 2001},
    {"titulo": "Toy Story", "director": "John Lasseter", "nacionalidad": "EE.UU.", "genero": "Comedia", "año": 1995},
    {"titulo": "Intensamente", "director": "Pete Docter", "nacionalidad": "EE.UU.", "genero": "Comedia", "año": 2015},
    {"titulo": "Coco", "director": "Lee Unkrich", "nacionalidad": "EE.UU.", "genero": "Comedia", "año": 2017},
    {"titulo": "The Social Network", "director": "David Fincher", "nacionalidad": "EE.UU.", "genero": "Drama", "año": 2010},
    {"titulo": "Interstellar", "director": "Christopher Nolan", "nacionalidad": "Reino Unido", "genero": "Ciencia ficción", "año": 2014},
    {"titulo": "Django Unchained", "director": "Quentin Tarantino", "nacionalidad": "EE.UU.", "genero": "Acción", "año": 2012},
    {"titulo": "La lista de Schindler", "director": "Steven Spielberg", "nacionalidad": "EE.UU.", "genero": "Drama", "año": 1993},
    {"titulo": "Amélie", "director": "Jean-Pierre Jeunet", "nacionalidad": "Francia", "genero": "Comedia", "año": 2001},
]

# Crear registros en la base de datos
for peli in peliculas:
    director, _ = Director.objects.get_or_create(nombre=peli["director"], defaults={"nacionalidad": peli["nacionalidad"]})
    genero = Genero.objects.get(nombre=peli["genero"])
    Pelicula.objects.get_or_create(
        titulo=peli["titulo"],
        director=director,
        genero=genero,
        año=peli["año"]
    )
