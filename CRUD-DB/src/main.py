from basedato.db import db
from modelo.curso import curso
from modelo.estudiante import estudiante
from controlador.estudiante_controlador import EstudianteControlador
from controlador.curso_controlador import CursoControlador

def menu():
    print("1- Crear curso")
    print("2- Mostrar cursos")
    print("3- Salir")

def main():
    db.connect()
    db.create_tables([curso])

    print("Bienvenido al sistema de gestión de estudiantes")

    while True:
        print("------------")
        menu()
        opcion = int(input("¿Qué tipo de acción necesitas realizar?"))

        if opcion == 1:
            nombre = input("Ingrese el nombre del curso: ")
            CursoControlador.crear(nombre)
            print("Curso creado exitosamente.")
        elif opcion == 2:
            print("---Listado de cursos---")
            cursos = CursoControlador.mostrar()
            if cursos:
                for curso in cursos:
                    print(f"Curso: {curso.nombre}")
                else:
                    print("No hay cursos disponibles.")
            elif opcion == 3:
                break

            else:
                print("Opción inválida. Intenta nuevamente.")
            
        if __name__ == '__main__':
            main()