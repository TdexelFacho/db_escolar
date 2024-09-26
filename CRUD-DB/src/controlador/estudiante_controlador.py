from servicio.estudiante_servicio import EstudianteServicio

class EstudianteControlador():
    def crear (nombre, DNI, gmail, telefono, fecha_nacimiento, curso_id):
        return EstudianteServicio.crear_estudiante(nombre, DNI, gmail, telefono, fecha_nacimiento, curso_id)
    
    def mostrar():
        return EstudianteServicio.mostrar_estudiante()