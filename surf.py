import json

def read_surfboards(file_path):
    with open (file_path,"r", encoding= 'utf-8') as file: 
        boards=json.load(file)
    return boards


def users_data(): #customer 
    users_name = input("Ingresa tu nombre: ")
    while True:
        try:
            users_phone_number = int(input("Ingrese su numero de telefono: "))
            break
        except ValueError:
            print("El numero ingresado es de formato no valido")
        
    users_email = input("Ingrse su correo electronico: ")
    return {
    "Nombre": users_name,
    "Telefono": users_phone_number,
    "Correo": users_email
}


def surfboard_shape(): #board
    Model= input("Ingrese que modelo de tabla deseas: ")
    brand= input("Ingrese la marca de dicha tabla: ")

    board_type = int(input(
    "Digite:\n"
    "1. Shortboard\n"
    "2. Longboard\n"
    "3. Fish\n"
    "4. Funboard\n"
    "5. Gun\n"
    "6. Soft Top\n"
    "Seleccione una opción: "
))

    if board_type == 1:
        board_type = "Shortboard"
        print("Has seleccionado una Shortboard")
    elif board_type == 2:
        board_type = "Longboard"
        print("Has seleccionado una Longboard")
    elif board_type == 3:
        board_type = "Fish"
        print("Has seleccionado una Fish")
    elif board_type == 4:
        board_type = "Funboard"
        print("Has seleccionado una Funboard")
    elif board_type == 5:
        board_type = "Gun"
        print("Has seleccionado una Gun")
    elif board_type == 6:
        board_type = "Soft Top"
        print("Has seleccionado una Soft Top")
    else:
        print("Opción no válida.")
    
    return {
        "Modelo": Model,
        "Marca": brand,
        "Tipo": board_type
    }


def surfboard_dimensions(): #dimensions
    while True:
        try:
            length = float(input("Ingrese el largo que deseas en tu tabla: "))
            width = float(input("Ingresa el ancho del que la deseas: "))
            thickness = float(input("Ingrese el espesor: "))
            volume= float(input("Ingrese el volumen de la tabla: "))
            break
        except ValueError:
            print("Debe ingresar un número válido.")
    return {
        "Length": length,
        "Width": width,
        "Thickness": thickness,
        "Volume": volume
    }


def Board_specifications(): #specifications
    Material= input("Ingrese el material con el que quieres la tabla (PU/EPS/Epoxy): ")
    personalized= input("Deseas un diseño personalizado (si/no): ").lower()
    if personalized == "si":
        print("Ingrese las especificaciones que deseas en la tabla: ")
    
    fins_number = int(input("Ingrese la cantidad de quillas quieres en tu tabla: "))

    while True:
        try:
            fins_system = int(input(
                "Seleccione que sistema de quillas quieres:\n" 
                "1. FCS II\n" 
                "2. Futures\n"
                "Opcion:"
            ))
            if fins_system == 1:
                fins_system = "FCS II"
                break
            elif fins_system == 2:
                fins_system = "Futures"
                break
        except ValueError:
            print("Ingrese una opcion valida")
    return {
    "Material": Material,
    "Diseño personalizado": personalized,
    "Numero de quillas": fins_number,
    "Sistema de quillas": fins_system
}


def order(): #purchase  
    while True:
        try:  
            quantity = int(input("Ingrese la cantidad de tablas que desea: "))

            if quantity>0:
                break
            else:
                print("Lacantidad debe ser mayor a 0")
        
        except ValueError:
            print("Debe ingresar únicamente números.")
    
    cover = input("Desea una funda para las/la tabla?(si/no): ").lower() == "si"
    if cover:
        print("Has agregado una funda a tu orden")
    else:
        print("Tu orden no tendra funda incluida")
        
    leash = input("Deseas que tu orden tenga un leash? (si/no): ").lower() =="si"
    if leash:
        print("Se le ah agregado un leash a su orden")
    else:
        print("Tu orden no tendra leash incluido") 
        
    wax = input("Ingrese si quieres wax incluido en tu pedido (si/no):").lower() == "si"
    if wax:
        print("Se le ah agregado un wax a tu orden")
    else:
        print("Tu orden no tendra wax incluido")
    
    return {
    "Cantidad": quantity,
    "Funda": cover,
    "Leash": leash,
    "Wax": wax
}


def new_order():

    customer = users_data()
    board = surfboard_shape()
    dimensions = surfboard_dimensions()
    specifications = Board_specifications()
    purchase = order()
    
    order_data={
        "Cliente": customer,
        "Tabla": board,
        "Dimensiones": dimensions,
        "Especificaciones": specifications,
        "Pedido":purchase
    }
    return order_data


def main():
    # Ruta del archivo JSON
    file_path = "board.json"

    # Lee los pedidos existentes
    boards = read_surfboards(file_path)

    # Crea un nuevo pedido
    new_board_order = new_order()

    # Agrega el nuevo pedido a la lista
    boards.append(new_board_order)

    # Guarda nuevamente el archivo
    save_files(file_path, boards)

    print("¡Pedido agregado correctamente!")


def save_files(file_path, boards):
    """
    Guarda la lista de pedidos en un archivo JSON.
    """

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(boards, file, indent=4,)


if __name__ == "__main__":
    main()