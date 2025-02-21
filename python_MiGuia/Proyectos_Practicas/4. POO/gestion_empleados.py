class Empleado:
    def __init__(self, id_empleado, nombre ,puesto, salario):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
    
    def mostrar_informacion(self):
        return(f"ID: {self.id_empleado} - Nombre {self.nombre} - Puesto {self.puesto} - Salario {self.salario:.2f} ")
    
    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * (porcentaje/100)
    
    def cambiar_puesto(self, nuevo_puesto):
        self.puesto = nuevo_puesto 

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    
    def eliminar_empleado(self,id_empleado):
        for empleado in self.empleados:
            if empleado.id_empleado == id_empleado:
                self.empleados.remove(id_empleado)
                return True
        return False
    
    def calcular_gasto_salario(self):
        return sum(empleado.salario for empleado in self.empleados)
    
    def listar_empleados(self):
        if not self.empleados:
            return(f"No hay empleados en el departamento")
        return "\n".join([empleado.mostrar_informacion() for empleado in self.empleados])
        """
        Itera sobre la lista self.empleados.
        Por cada objeto empleado, llama al método mostrar_informacion, que devuelve una cadena con la información del empleado (como nombre, puesto y salario).
        Esto genera una lista de cadenas con la información de todos los empleados."""
        """
        Parámetro self:
        Hace referencia a la instancia actual de la clase Departamento.
        A través de self, la función accede a los atributos de la instancia, como self.empleados y self.nombre."""

class GestorEmpleados:
    def __init__(self):
        self.departamentos = {}
    
    def agregar_departamento(self, nombre_departamento):
        if nombre_departamento not in self.departamentos:
            self.departamentos[nombre_departamento] = Departamento(nombre_departamento)
            print(f"Departamento '{nombre_departamento}' agregado.")
        else:
            print(f"El departamento '{nombre_departamento}' ya existe. ")
    
    def agregar_empleado(self, empleado):
        if empleado in self.empleados:
            print(f"Empleado {empleado.nombre} ya registrado")
            return
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nombre} agregado exitosamente")
        
    

    #def agregar_empleado
    #def eliminar_empleado
    #  def calcular_gasto_salarios
    #def listar_empleados


