from servicio.curso_servicio import CursoServicio

class CursoControlador():

    def crear(nombre):
        return CursoServicio.crear_curso(nombre)
    
    def mostrar():
        return CursoServicio.mostrar_cursos()