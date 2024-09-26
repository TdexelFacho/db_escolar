from modelo.curso import Curso
from modelo.estudiante import Estudiante

class EstudianteServicio:

    @staticmethod
    def crear_estudiante(nombre, curso_id):
        curso= curso.get(Curso.id == curso_id)
        estudiante = estudiante.create(nombre=nombre, curso=curso)
        return estudiante
    
    @staticmethod
    def mostrar_estudiante():
        return list(Estudiante.select())
    
    @staticmethod
    def eliminar_estudiante(id):
        estudiante = estudiante.get(estudiante.id == id)
        estudiante.delete_instance()
        return estudiante