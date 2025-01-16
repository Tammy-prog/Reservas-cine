class AsientoReservadoError(Exception):
    """Se lanza cuando se intenta reservar un asiento ya reservado."""
    pass

class AsientoNoReservadoError(Exception):
    """Se lanza cuando se intenta cancelar un asiento no reservado."""
    pass

class AsientoNoEncontradoError(Exception):
    """Se lanza cuando el asiento buscado no existe en la sala."""
    pass

class AsientoDuplicadoError(Exception):
    """Se lanza cuando se intenta agregar un asiento ya existente."""
    pass


def validar_entrada(valor, mensaje_error):
    """
    Valida que un valor sea positivo y mayor que cero.
    """
    if not isinstance(valor, (int, float)):
        raise ValueError(f"{mensaje_error} Debe ser un número.")
    if valor <= 0:
        raise ValueError(mensaje_error)


def validar_tipo_booleano(valor, mensaje_error):
    """
    Valida que un valor sea de tipo booleano.
    """
    if not isinstance(valor, bool):
        raise ValueError(mensaje_error)


def calcular_precio(precio_base, dia_espectador, es_mayor_65):
    """
    Calcula el precio final aplicando descuentos si corresponde.
    """
    descuento = 0
    if dia_espectador:
        descuento += 0.20
    if es_mayor_65:
        descuento += 0.30
    return precio_base * (1 - descuento)


class Asiento:
    def __init__(self, numero, fila, precio_base):
        """
        Constructor de la clase Asiento.
        Inicializa un asiento con número, fila, precio base y estado de reserva.
        Valida que el número, la fila y el precio base sean positivos.
        """
        validar_entrada(numero, "El número del asiento debe ser mayor que cero.")
        validar_entrada(fila, "La fila del asiento debe ser mayor que cero.")
        validar_entrada(precio_base, "El precio base debe ser mayor que cero.")
        self.__numero = numero
        self.__fila = fila
        self.__reservado = False
        self.__precio_base = precio_base
        self.__precio_actual = precio_base

    @property
    def numero(self):
        """Devuelve el número del asiento."""
        return self.__numero

    @property
    def fila(self):
        """Devuelve la fila del asiento."""
        return self.__fila

    @property
    def reservado(self):
        """Indica si el asiento está reservado."""
        return self.__reservado

    @property
    def precio_actual(self):
        """Devuelve el precio actual del asiento, incluyendo descuentos si aplica."""
        return self.__precio_actual

    def reservar(self, es_mayor_65, dia_espectador):
        """
        Reserva el asiento si está disponible, calculando el precio con los descuentos correspondientes.
        Parámetros:
        - es_mayor_65 (bool): Indica si el espectador tiene más de 65 años.
        - dia_espectador (bool): Indica si es el día del espectador.
        Lanza una excepción si el asiento ya está reservado.
        """
        validar_tipo_booleano(es_mayor_65, "El parámetro es_mayor_65 debe ser un booleano.")
        validar_tipo_booleano(dia_espectador, "El parámetro dia_espectador debe ser un booleano.")

        if self.__reservado:
            raise AsientoReservadoError(f"El asiento {self.__fila}-{self.__numero} ya está reservado.")

        self.__precio_actual = calcular_precio(self.__precio_base, dia_espectador, es_mayor_65)
        self.__reservado = True

    def cancelar_reserva(self):
        """
        Cancela la reserva del asiento, devolviéndolo a su estado inicial.
        Lanza una excepción si el asiento no está reservado.
        """
        if not self.__reservado:
            raise AsientoNoReservadoError(f"El asiento {self.__fila}-{self.__numero} no está reservado.")

        self.__reservado = False
        self.__precio_actual = self.__precio_base

    def __str__(self):
        """
        Devuelve una representación en cadena del asiento, indicando su estado y precio.
        """
        estado = "Reservado" if self.__reservado else "Disponible"
        return f"Asiento {self.__fila}-{self.__numero}: {estado}, Precio: {self.__precio_actual:.2f}"


class SalaCine:
    def __init__(self, precio_base, descuento_dia=0.20, descuento_mayor_65=0.30):
        """
        Inicializa la sala con precios base y configuraciones de descuentos.
        """
        validar_entrada(precio_base, "El precio base debe ser mayor que cero.")
        validar_entrada(descuento_dia, "El descuento del día debe ser mayor o igual a cero.")
        validar_entrada(descuento_mayor_65, "El descuento para mayores de 65 años debe ser mayor o igual a cero.")

        if descuento_dia > 1 or descuento_mayor_65 > 1:
            raise ValueError("Los descuentos no pueden exceder el 100%.")

        self.__precio_base = precio_base
        self.__descuento_dia = descuento_dia
        self.__descuento_mayor_65 = descuento_mayor_65
        self.__asientos = []

    def agregar_asiento(self, numero, fila):
        """
        Agrega un asiento a la sala si no existe otro con el mismo número y fila.
        Lanza una excepción si el asiento ya existe.
        """
        validar_entrada(numero, "El número del asiento debe ser mayor que cero.")
        validar_entrada(fila, "La fila del asiento debe ser mayor que cero.")

        if any(asiento.numero == numero and asiento.fila == fila for asiento in self.__asientos):
            raise AsientoDuplicadoError(f"El asiento {fila}-{numero} ya existe.")

        nuevo_asiento = Asiento(numero, fila, self.__precio_base)
        self.__asientos.append(nuevo_asiento)

    def buscar_asiento(self, numero, fila):
        """
        Busca un asiento en la sala por su número y fila.
        Devuelve el asiento si lo encuentra; de lo contrario, lanza una excepción.
        """
        validar_entrada(numero, "El número del asiento debe ser mayor que cero.")
        validar_entrada(fila, "La fila del asiento debe ser mayor que cero.")

        for asiento in self.__asientos:
            if asiento.numero == numero and asiento.fila == fila:
                return asiento
        raise AsientoNoEncontradoError(f"El asiento {fila}-{numero} no existe.")

    def reservar_asiento(self, numero, fila, es_mayor_65, dia_espectador):
        """
        Reserva un asiento específico aplicando descuentos si aplica.
        Parámetros:
        - numero (int): Número del asiento.
        - fila (int): Fila del asiento.
        - es_mayor_65 (bool): Indica si el espectador tiene más de 65 años.
        - dia_espectador (bool): Indica si es el día del espectador.
        Lanza una excepción si el asiento no existe o ya está reservado.
        """
        validar_tipo_booleano(es_mayor_65, "El parámetro es_mayor_65 debe ser un booleano.")
        validar_tipo_booleano(dia_espectador, "El parámetro dia_espectador debe ser un booleano.")

        asiento = self.buscar_asiento(numero, fila)
        asiento.reservar(es_mayor_65, dia_espectador)

    def cancelar_reserva(self, numero, fila):
        """
        Cancela la reserva de un asiento específico.
        Lanza una excepción si el asiento no existe o no está reservado.
        """
        asiento = self.buscar_asiento(numero, fila)
        asiento.cancelar_reserva()

    def mostrar_asientos(self):
        """
        Imprime los asientos en un formato tabular.
        """
        print(f"{'Fila':<10}{'Número':<10}{'Estado':<15}{'Precio':<10}")
        print("-" * 45)
        for asiento in self.__asientos:
            estado = "Reservado" if asiento.reservado else "Disponible"
            print(f"{asiento.fila:<10}{asiento.numero:<10}{estado:<15}{asiento.precio_actual:.2f}")

    def guardar_estado(self, archivo):
        """
        Guarda el estado actual de la sala en un archivo.
        """
        with open(archivo, 'w') as f:
            for asiento in self.__asientos:
                estado = "Reservado" if asiento.reservado else "Disponible"
                f.write(f"{asiento.fila},{asiento.numero},{estado},{asiento.precio_actual:.2f}\n")

    def cargar_estado(self, archivo):
        """
        Carga el estado de la sala desde un archivo.
        """
        with open(archivo, 'r') as f:
            for linea in f:
                fila, numero, estado, precio = linea.strip().split(',')
                nuevo_asiento = Asiento(int(numero), int(fila), self.__precio_base)
                if estado == "Reservado":
                    nuevo_asiento.reservar(False, False)  # Ajusta los parámetros según necesidad.
                self.__asientos.append(nuevo_asiento)


# Ejemplo de uso
def main():
    """
    Función principal para demostrar el uso de las clases Asiento y SalaCine.
    Crea una sala de cine, agrega asientos, los muestra, reserva un asiento y cancela la reserva.
    """
    precio_base = 10.0
    sala = SalaCine(precio_base)

    try:
        # Agregar asientos
        sala.agregar_asiento(1, 1)
        sala.agregar_asiento(2, 1)

        # Mostrar asientos
        print("Asientos disponibles:")
        sala.mostrar_asientos()

        # Reservar asiento
        print("\nReservando asiento 1-1 para un mayor de 65 en día del espectador...")
        sala.reservar_asiento(1, 1, es_mayor_65=True, dia_espectador=True)

        # Mostrar asientos después de la reserva
        print("\nEstado de los asientos:")
        sala.mostrar_asientos()

        # Cancelar reserva
        print("\nCancelando reserva del asiento 1-1...")
        sala.cancelar_reserva(1, 1)

        # Mostrar asientos después de cancelar la reserva
        print("\nEstado final de los asientos:")
        sala.mostrar_asientos()

        # Guardar estado en archivo
        print("\nGuardando estado de la sala en archivo...")
        sala.guardar_estado("estado_sala.txt")

        # Cargar estado desde archivo
        print("\nCargando estado de la sala desde archivo...")
        sala.cargar_estado("estado_sala.txt")
        sala.mostrar_asientos()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
