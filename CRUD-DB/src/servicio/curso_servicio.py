from modelo.curso import curso

class CursoServicio:
    @staticmethod
    def crear_curso(nombre):
        curso = curso.create(nombre=nombre)
        return curso
    
    @staticmethod
    def mostrar_cursos():
        return list(curso.select())