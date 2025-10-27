#funcion para mostramo el menu
def menu():
	print("MENU:")
	print("1. Crear_artículo")
	print("2. Listar_artículos")
	print("3. Buscar_artículo_por_id")
	print("4. Actualizar_artículo")
	print("5. Eliminar_artículo")
	print("6. Alternar_activo/inactivo")
	print("7. Salir")

#funcon para elegir una opcion del menu
def opcion():
	menu()
	elegir = input("eliga una la opción que desea realizar: ")
	while elegir != "7":
		match elegir:
			case "1":
				crear()

			case "2":
				for producto in inventario:
					print(producto)
			
			case "3":
				buscar()

			case "4":
				cambiar()

			case "5":
				eliminar()

			case "6":
				estado()

		menu()
		elegir = input("elija una la opción que desea realizar: ")
	print("Gracias por usar el programa vuelva pronto")

inventario = [
	{"id": 1, "nombre": "pan", "precio": 1.2, "stock": 20, "activo": True},
	{"id": 2, "nombre": "pollo", "precio": 2.5, "stock": 25, "activo": True},
	{"id": 3, "nombre": "ternera", "precio": 3.5, "stock": 21, "activo": True},
	{"id": 4, "nombre": "arroz", "precio": 1.5, "stock": 16, "activo": True}
]

#funcion para meter un producto nuevo en la lista
def crear():
	id_nuevo = int(input("introduzca el id del artículo: ") )
	for producto in inventario:
		if producto["id"] == id_nuevo:
			print("Error ya existe ese id")
			return
	nombre_nuevo = str(input("introduzca el nombre del artículo: "))
	precio_nuevo = float(input("introduzca el precio del artículo: "))
	stock_nuevo = int(input("introduzca el stock del artículo: "))
	activo_nuevo = input("introduzca si el producto esta activo o no (True/False): ").strip().lower() == "true"
	
	nuevo_producto = {
		"id": id_nuevo,
		"nombre": nombre_nuevo,
		"precio": precio_nuevo,
		"stock": stock_nuevo,
		"activo": activo_nuevo
	}
	inventario.append(nuevo_producto)
	print("producto agregado al inventario.")

#funcion para buscar un articulo por su id
def buscar():
	articulo = input("Introduzca el id del artículo que desea buscar: ")
	for producto in inventario:
		if producto["id"] == int(articulo):
			print(producto)
			return
	print("articulo no encontrado")

#funcion para cambiar valores de un diccionario
def cambiar():
	cambio = input("elige el id del producto que quieras cambiar: ")
	producto_a_cambiar = None
	for producto in inventario:
		if producto["id"] == int(cambio):
			producto_a_cambiar = producto
			break
	if producto_a_cambiar is None:
		print("error no existe ese producto") 
		return
	elegircambio = input("Elige que valor quiereres cambiar (nombre, precio o stock): ")
	if elegircambio == "nombre":
		cambiarnombre = input("elige el nuevo nombre: ")
		producto_a_cambiar["nombre"] = cambiarnombre
		
	elif elegircambio == "precio":
		cambiarprecio = input("elige el nuevo precio: ")
		producto_a_cambiar["precio"] = cambiarprecio
	
	elif elegircambio == "stock":
		cambiarstock = input("elige el nuevo stock: ")
		producto_a_cambiar["stock"] = cambiarstock
	print("el cambio ha sido realizado")


#funcion para eliminar un diccionario(articulo) de la lista
def eliminar():
	articulo_eliminar = input("introduzca el id del articulo que quiera eliminar: ")
	for producto in inventario:
		if producto["id"] == int(articulo_eliminar):
			inventario.remove(producto)
			print("articulo eliminado")
			return
	print("error no existe ese producto") 

#funcion para cambiar el estado de un producto (activo / no activo)
def estado():
	id_producto = int(input("Introduzca el ID del producto que desea activar/desactivar: "))
	for producto in inventario:
		if producto["id"] == id_producto:
			producto["activo"] = not producto["activo"]
			print(f"Se ha cambiado el estado del producto: '{producto['nombre']}'")
			return
	print("Error: no existe ese producto.")

#palabra para ejecutar la funcion que con tiene todo





def leer_int(mensaje):
	while True:
		return int(input(mensaje))


def leer_bool(mensaje):
    while True:
        valor = input(mensaje + " (True/False): ").strip().lower()
        if valor in ("true", "si"):
            return True
        elif valor in ("false", "no"):
            return False
        print("Error: introduzca True o False.")

def generar_id(lista):
    if not lista:
        return 1
    return max(item["id"] for item in lista) + 1

# Usuarios
usuarios = [
    {"id": 1, "nombre": "Ana", "email": "ana@gmail.com", "activo": True},
    {"id": 2, "nombre": "Luis", "email": "luis@gmaill.com", "activo": True}
]

def usuario_crear():
    id_nuevo = generar_id(usuarios)
    print(f"Creando nuevo usuario (ID asignado: {id_nuevo})")
    nombre = input("Nombre: ")
    while True:
        email = input("Email: ")
        if "@" in email and "." in email:
            break
        print("Email no válido, inténtelo de nuevo.")
    activo = leer_bool("¿Está activo?")
    usuarios.append({
        "id": id_nuevo,
        "nombre": nombre,
        "email": email,
        "activo": activo
    })
    print("Usuario creado correctamente.")

def usuario_listar():
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for usuario in usuarios:
        print(usuario)

def usuario_buscar_por_id(id_busqueda):
    for usuario in usuarios:
        if usuario["id"] == id_busqueda:
            return usuario
    return None

def usuario_buscar():
    id_buscado = leer_int("ID del usuario a buscar: ")
    usuario = usuario_buscar_por_id(id_buscado)
    print(usuario if usuario else "Usuario no encontrado.")

def usuario_actualizar():
    id_modificar = leer_int("ID del usuario a modificar: ")
    usuario = usuario_buscar_por_id(id_modificar)
    if not usuario:
        print("No existe ese usuario.")
        return
    campo = input("Campo a cambiar (nombre, email): ").lower()
    if campo == "nombre":
        usuario["nombre"] = input("Nuevo nombre: ")
    elif campo == "email":
        while True:
            nuevo_email = input("Nuevo email: ")
            if "@" in nuevo_email and "." in nuevo_email:
                usuario["email"] = nuevo_email
                break
            print("Email no válido.")
    else:
        print("Campo inválido.")
        return
    print("Usuario actualizado.")

def usuario_eliminar():
    id_eliminar = leer_int("ID del usuario a eliminar: ")
    usuario = usuario_buscar_por_id(id_eliminar)
    if usuario:
        usuarios.remove(usuario)
        print("Usuario eliminado.")
    else:
        print("No existe ese usuario.")

def usuario_alternar_activo():
    id_usuario = leer_int("ID del usuario a activar/desactivar: ")
    usuario = usuario_buscar_por_id(id_usuario)
    if usuario:
        usuario["activo"] = not usuario["activo"]
        print(f"Estado cambiado. Ahora está {'activo' if usuario['activo'] else 'inactivo'}.")
    else:
        print("No existe ese usuario.")

# Menú de usuarios
def menu_usuarios():
    opcion = ""
    while opcion != "7":
        print("\n=== GESTIÓN DE USUARIOS ===")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario por ID")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Alternar activo/inactivo")
        print("7. Volver")
        opcion = input("Elija una opción: ")
        match opcion:
            case "1": usuario_crear()
            case "2": usuario_listar()
            case "3": usuario_buscar()
            case "4": usuario_actualizar()
            case "5": usuario_eliminar()
            case "6": usuario_alternar_activo()
            case "7": print("Volviendo al menú principal...")
            case _: print("Opción no válida.")

# Menú principal
def menu_principal():
    opcion_menu = ""
    while opcion_menu != "3":
        print("MENÚ PRINCIPAL")
        print("1. Gestión de artículos")
        print("2. Gestión de usuarios")
        print("3. Salir")
        opcion_menu = input("Elija una opción: ")
        match opcion_menu:
            case "1":
                opcion()  # menú de artículos
            case "2":
                menu_usuarios()  # menú de usuarios
            case "3":
                print("Gracias por usar el programa.")
                break
            case _:
                print("Opción no válida.")

# Ejecutar programa
menu_principal()