class Hotel:
    def __init__(self, nombre, ubicacion, habitaciones_disp):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.habitaciones_disp = habitaciones_disp
        self.reservas = []
    
    def reservar_habitacion(self, nombre_cliente, habitacion):
        if habitacion in self.habitaciones_disp:
            self.habitaciones_disp.remove(habitacion)
            self.reservas.append((nombre_cliente, habitacion))
            print(f'Habitacion {habitacion} reservada para {nombre_cliente}.')
        else:
            print('Lo sentimos, habitacion no esta disponible')


    def cancelar_reserva(self, nombre_cliente):
        reservas_actualizadas = []
        reserva_encontrada = False

        for reserva in self.reservas:
            if reserva[0] == nombre_cliente:
                self.habitaciones_disp.append(reserva[1])
                reserva_encontrada = True
            else:
                reservas_actualizadas.append(reserva)

        if reserva_encontrada:
            self.reservas = reservas_actualizadas
            print(f'Reserva cancelada para {nombre_cliente}')
        else:
            print(f'No se encontro ninguna reserva para {nombre_cliente}')


    def info_hotel(self):
        print(f'Hotel {self.nombre} 5 estrellas, que se encuentra en {self.ubicacion}')
        print(f'Habitaciones disponibles :{", ".join(self.habitaciones_disp)}')
        print('reservas:')
        if self.reservas:
            for reserva in self.reservas:
                print(f'Cliente: {reserva[0]}, Habitacion: {reserva[1]}')
        else:
            print('No hay reservas en el hotel')


# Ejemplo de uso
hotel = Hotel('Hotel AC', 'Quito', ['101', '102', '103', '104'])

hotel.reservar_habitacion('Arturo','101')
hotel.reservar_habitacion('Guerrero', '103')
hotel.reservar_habitacion('Meryuris', '105')  # Habitación no disponible

hotel.info_hotel()

hotel.cancelar_reserva('Guerrero')
hotel.cancelar_reserva('Jose')  # Reserva inexistente

hotel.info_hotel()
