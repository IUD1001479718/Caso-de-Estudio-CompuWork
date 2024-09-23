class Departamento:
    def __init__(self, nombre):
        self._nombre = nombre
        self._empleados = []  # Lista para almacenar empleados asignados

    # Métodos getter y setter
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    # Métodos para añadir y eliminar empleados del departamento
    def asignar_empleado(self, empleado):
        if empleado not in self._empleados:
            self._empleados.append(empleado)

    def eliminar_empleado(self, empleado):
        if empleado in self._empleados:
            self._empleados.remove(empleado)

    # Mostrar empleados asignados al departamento
    def mostrar_empleados(self):
        if self._empleados:
            print(f"Empleados en {self._nombre}:")
            for empleado in self._empleados:
                empleado.mostrar_informacion()
        else:
            print(f"No hay empleados asignados al departamento {self._nombre}.")
