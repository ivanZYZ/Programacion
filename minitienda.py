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




#funciones para ayudar

#por ejemplo: funcion para meteer un input con int
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
	while opcion_menu != "4":
		print("MENÚ PRINCIPAL")
		print("1. Gestión de artículos")
		print("2. Gestión de usuarios")
		print("3. Menu de ventas" )
		print("4. Salir")
		opcion_menu = input("Elija una opción: ")
		match opcion_menu:
			case "1":
				opcion()  # menú de artículos
			case "2":
				menu_usuarios()  # menú de usuarios
			case "3":
				menu_ventas() #menu de ventas
			case "4":
				print("Gracias por usar el programa.")
				break
			case _:
				print("Opción no válida.")



ventas = []  
carrito_actual = []  
usuario_activo = None  


def seleccionar_usuario_activo():
    global usuario_activo
    usuario_listar()
    id_usuario = leer_int("Ingrese el ID del usuario activo: ")
    usuario = usuario_buscar_por_id(id_usuario)
    if usuario and usuario["activo"]:
        usuario_activo = id_usuario
        print(f"Usuario '{usuario['nombre']}' seleccionado como activo.")
    else:
        print("Usuario no válido o inactivo.")
        usuario_activo = None

def añadir_al_carrito():
    if usuario_activo is None:
        print("Debe seleccionar un usuario activo antes de añadir artículos.")
        return
    id_articulo = leer_int("Ingrese ID del artículo a añadir: ")
    producto = buscar_articulo_por_id(id_articulo)
    if not producto or not producto["activo"]:
        print("Artículo no válido o inactivo.")
        return
    cantidad = leer_int("Ingrese cantidad: ")
    if cantidad < 1:
        print("La cantidad debe ser al menos 1.")
        return
    if cantidad > producto["stock"]:
        print("No hay stock suficiente.")
        return


   
    for i, (art_id, cant) in enumerate(carrito_actual):
        if art_id == id_articulo:
            carrito_actual[i] = (art_id, cant + cantidad)
            print(f"Cantidad actualizada en el carrito: {cant + cantidad}")
            return
    carrito_actual.append((id_articulo, cantidad))
    print(f"Artículo '{producto['nombre']}' añadido al carrito.")

def quitar_del_carrito():
    if not carrito_actual:
        print("El carrito está vacío.")
        return
    id_articulo = leer_int("Ingrese ID del artículo a quitar del carrito: ")
    for i, (art_id, _) in enumerate(carrito_actual):
        if art_id == id_articulo:
            carrito_actual.pop(i)
            print("Artículo eliminado del carrito.")
            return
    print("El artículo no estaba en el carrito.")


def ver_carrito():
    if not carrito_actual:
        print("El carrito está vacío.")
        return 0 

    total = 0
    print("Carrito de compras")

    for articulo_id, cantidad in carrito_actual:
        articulo = buscar_articulo_por_id(articulo_id)
        if articulo:
            subtotal = articulo["precio"] * cantidad
            total += subtotal
            print(f"ID: {articulo['id']}, Nombre: {articulo['nombre']}, Cantidad: {cantidad}, "
                  f"Precio unitario: {articulo['precio']}, Subtotal: {subtotal}")

    print(f"Total del carrito: {total}")
    return total


def confirmar_compra():
    global carrito_actual
    if usuario_activo is None:
        print("Debe seleccionar un usuario activo antes de comprar.")
        return
    if not carrito_actual:
        print("El carrito está vacío.")
        return
   

    for art_id, cantidad in carrito_actual:
        producto = buscar_articulo_por_id(art_id)
        if cantidad > producto["stock"]:
            print(f"No hay stock suficiente para '{producto['nombre']}'. Compra cancelada.")
            return
  

    items_venta = []
    total = 0
    for art_id, cantidad in carrito_actual:
        producto = buscar_articulo_por_id(art_id)
        producto["stock"] -= cantidad
        subtotal = producto["precio"] * cantidad
        total += subtotal
        items_venta.append((art_id, cantidad, producto["precio"]))
    id_venta = len(ventas) + 1
    ventas.append({
        "id_venta": id_venta,
        "usuario_id": usuario_activo,
        "items": items_venta,
        "total": total
    })
    print(f"Compra confirmada. Total: {total}")
    carrito_actual = []

def historial_ventas_por_usuario():
    if usuario_activo is None:
        print("Seleccione un usuario activo primero.")
        return
    print(f"\n--- Historial de ventas del usuario {usuario_activo} ---")
    usuario = usuario_buscar_por_id(usuario_activo)
    for venta in ventas:
        if venta["usuario_id"] == usuario_activo:
            print(f"Venta ID: {venta['id_venta']}, Total: {venta['total']}")
            for art_id, cant, precio in venta["items"]:
                producto = buscar_articulo_por_id(art_id)
                print(f"  {producto['nombre']}: {cant} x {precio} = {cant * precio}")


def vaciar_carrito():
    global carrito_actual
    carrito_actual = []
    print("Carrito vaciado.")


def buscar_articulo_por_id(id_busqueda):
    for producto in inventario:
        if producto["id"] == id_busqueda:
            return producto
    return None

# Menú de ventas 
def menu_ventas():
    opcion = ""
    while opcion != "8":
        print("VENTAS")
        print("1. Seleccionar usuario activo")
        print("2. Añadir artículo al carrito")
        print("3. Quitar artículo del carrito")
        print("4. Ver carrito")
        print("5. Confirmar compra")
        print("6. Historial de ventas por usuario")
        print("7. Vaciar carrito")
        print("8. Volver")
        opcion = input("Elija una opción: ")
        match opcion:
            case "1": seleccionar_usuario_activo()
            case "2": añadir_al_carrito()
            case "3": quitar_del_carrito()
            case "4": ver_carrito()
            case "5": confirmar_compra()
            case "6": historial_ventas_por_usuario()
            case "7": vaciar_carrito()
            case "8": print("Volviendo al menú principal")
            case _: print("Opción no válida.")



# Ejecutar programa
menu_principal()

