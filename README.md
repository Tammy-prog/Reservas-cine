# Reservas-cine
Proyecto Final del curso de Python becado por IBM

Sistema de Reservas para un Cine con Tarifas Especiales
Descripción: Desarrolla una aplicación en Python para gestionar las reservas de asientos
en una sala de cine, incluyendo un sistema de precios con descuentos en ciertos días y
tarifas reducidas para personas mayores.
Requisitos:
1. Clases y Objetos:
o Clase Asiento: Representa un asiento en la sala con los siguientes
atributos:
▪ numero: Número del asiento.
▪ fila: Fila del asiento.
▪ reservado: Estado de la reserva (True o False).
▪ precio: Precio del asiento (varía según el día y la edad del
espectador).
o Clase SalaCine: Administra una lista de asientos y permite las siguientes
operaciones:
1. Agregar un asiento: Añadir un asiento a la sala (verificando que no
esté ya registrado).
2. Reservar asiento: Cambiar el estado de un asiento a reservado,
asignando el precio correspondiente.
3. Cancelar reserva: Devolver un asiento a su estado disponible.
4. Mostrar asientos: Listar todos los asientos, indicando si están
reservados y su precio (aplicando descuentos).
5. Buscar asiento: Permitir la búsqueda de un asiento por número y
fila.
2. Sistema de Precios:
o Precio base: Fija un precio estándar para la entrada de cine.
o Día del espectador: El precio se reduce un 20% los miércoles.
o Descuento para mayores de 65 años: Los espectadores mayores de 65
años reciben un 30% de descuento sobre el precio base.
3. Validaciones y Manejo de Excepciones:
o Validar que el número de asiento y la fila son válidos.
o Validar que los datos de edad y día son correctos al aplicar descuentos.
o Manejar excepciones para evitar reservas duplicadas o cancelaciones de
asientos no reservados.
4. Organización del Código:
o Todos los atributos deben ser privados y accesibles mediante getters y
setters.
o Los métodos deben ser modulares y seguir los principios de
encapsulamiento de POO.
o No se deben utilizar variables globales fuera de las clases.
