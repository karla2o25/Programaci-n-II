from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.gestor_prestamos import GestorPrestamos
from modelos.biblioteca import Biblioteca
from modelos.bibliotecario import Bibliotecario
from modelos.alumno import Alumno

#Crear biblioteca
biblioteca = Biblioteca("Biblioteca Central")

#Crear bibliotecario
bibliotecario1 = Bibliotecario("Carlos", "0001", "IA")

#Crear libros
libro1 = Libro("Pepa Pig", "Bucanero", "12345")
libro2 = Libro("Teoría de la Evolución del Ser Humano", "Jorge el curioso", "2026-03-07")

#Bibliotecario registra libros
bibliotecario1.registrar_libro(biblioteca, libro1)
bibliotecario1.registrar_libro(biblioteca, libro2)

#Libros disponibles
biblioteca.listar_libros()

#Crear usuario
alumno = Alumno("Karla", "A001", "Alumno")

#Crear gestor de prestamos
gestor = GestorPrestamos()

#Realizar prestamo
gestor.realizar_prestamo(libro1, alumno, "18-04-2026")

#Imprimir prestamo
gestor.listar_prestamos()

print(bibliotecario1.descripcion())
print(alumno.descripcion())

#usuario1 = Usuario("Valeria", "2521578", "Estudiante")

#gestor = GestorPrestamos()

#mensaje = gestor.realizar_prestamo(libro1, usuario1, "2026-03-07")

#print(mensaje)

#print(libro1.getDisponibilidad())

#gestor.listar_prestamos()

#print(libro1.getTitulo())

#print(libro1 == libro2)

#print(usuario1)

#print(usuario1.getTipoUsuario())

