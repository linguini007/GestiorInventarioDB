import mysql.connector  # Libreria para conectar a nuestra DB
from tkinter import messagebox  #Importamos el modulo de messagebox para los indicadores de mensajes de Tkinter
import bcrypt #Importamos esta libreria para encriptar las credenciales del usuario que se registra

#Configuracion de la conexion mysql
config = {
        'host':'localhost', # Direccion a la que se va a conectar
        'port':'3307',   # Puerto por el que se va a conectar a la DB
        'user':'SET',   #Usuario de la DB que se va utulizar
        'password':'123456789', # contraseña que se utiliza para hacer la conexion
        'database':'tienda' # Nombre de la base de datos a la que se va a conectar
}

def crear_tabla_usuarios(): #Funcion para crear la tabla de los usuarios
    try:        
        conexion = mysql.connector.connect(**config) #  Instanciamos la conexion con nuestras configuraciones de config
        cursor=conexion.cursor() #Inicializamos nuestro cursor
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(  
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL,
                    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')#Con el cursor y (.execute) realizamos la instruccion SQL
        conexion.commit() # Despues hacemos un commit es para mandar las intrucciones SQL a la DB
    except mysql.connector.Error as err: # En caso de que no pueda hacer conexion  
       messagebox.showerror("Error",f"Ocurrio un error: {err}")# Mandara un mensaje emergente con el ERROR
    finally:    #Si la conexion fue exitosa, se desconectara de la DB 
        if 'conexion' in locals() and conexion.is_connected():  # si se esta conectado 
            cursor.close()      #se cerrara el curso
            conexion.close()    #y la conexion, para asegurar la integridad de la DB

def crear_tabla_productos(): # Funcion para crear la tabla de productos 
        try:
            conexion = mysql.connector.connect(**config)#  Instanciamos la conexion con nuestras configuraciones de config
            cursor=conexion.cursor()    #Inicializamos nuestro cursor
            cursor.execute('''CREATE TABLE IF NOT EXISTS productos(
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR(100) NOT NULL,
                        precio DECIMAL(10,2) NOT NULL,
                        stock INT NOT NULL,
                        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP);''')# Creamos la tabla de productos
            conexion.commit()   #Realizamos el commit para mandar la instrucciones SQL
        except mysql.connector.Error as err: #En caso de que no se realice la conexion
            messagebox.showerror("Error",f"Ocurrio un error: {err}") #Se abrira una ventana emergente diciendo el ERROR
        finally:
            if 'conexion' in locals() and conexion.is_connected(): #Despues Cerramos nuestro Cursor y 
                cursor.close()          #La conexion dentro de esta funcion
                conexion.close()

def crear_tablas_ventas(): #Funcion para crear la tabla de ventas
    try:
        conexion = mysql.connector.connect(**config)#  Instanciamos la conexion con nuestras configuraciones de config
        cursor=conexion.cursor()    #Inicializamos nuestro cursor
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS ventas (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        usuario_id INT NOT NULL,
                        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        total DECIMAL(10,2) NOT NULL,
                        FOREIGN KEY (usuario_id) REFERENCES usuarios(id))''') #Instrucciones para crear la tabla Ventas

        conexion.commit() # Realizamos nuestro commit para mandar la instruccion SQL
    except mysql.connector.Error as err: #En caso de que no se conecte a la DB
        messagebox.showerror("Error", f"Error al crear tablas de ventas: {err}") #Se abrira una ventana emergente con el ERROR
    finally:
        if 'conexion' in locals() and conexion.is_connected(): #Despues Cerramos nuestro Cursor y 
                cursor.close()  #La conexion dentro de esta funcion
                conexion.close() 

#En todas las funciones para las intrucciones de SQL, se repetira el proceso de hacer la conexion a la DB 
# 1.- Intanciamos la conexion con nuestras configuraciones de config
# 2.-Inicializamos nuestro cursor
# 3.- Intruccion SQL
# 4.- En caso de un error se abrira una ventana emergente con el ERROR
# 5.- Finalmente se cierra la conexion, cursor y conexion CLOSE()
# Lo unico que cambiara es la instrucciones SQL

def registrar_usuario(usuario, contraseña): #Funcion donde registramos los Usuarios Registrados
    if not usuario or not contraseña: #Si los campos de usuario y contraseña no estan completos, mandara un ERROR
        messagebox.showerror("Error", "Datos incompletos")
        return
    try:
        contraseña_bytes = contraseña.encode('utf-8')  # pasamos la contraseña y la encodeamos y decimos de que tipo es utf-8
                                #basicamente agrega caracteres especiales como los acentos y unifica las entradas de caracteres
                                # y lo asignamos a contraseña_bytes 
        hash_password = bcrypt.hashpw(contraseña_bytes, bcrypt.gensalt())# bcrypt.hashpw() le pasamos los bytes de la contraseña
                                                                    # y con bcrypt.gensalt() se genera un salt completo
                                                                    #$2b$12$DiN1dtgcupyeO........ algo asi
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO usuarios (username, password) VALUES (%s, %s)", #Mandamos la insercion de los datos
            (usuario, hash_password.decode('utf-8'))  # Decodificar el hash a string para almacenar en la DB
        )
        conexion.commit() 
        messagebox.showinfo("Éxito", "Usuario registrado correctamente")
    except mysql.connector.IntegrityError:  #en caso de que el usuario ya exista
        messagebox.showerror("Exito","El usuario ya existe")
    except Exception as e: #En caso de que la conexion no se realizo 
            messagebox.showerror("Error",f"Ocurrio un error:{e}")
    finally:
            if 'conexion' in locals() and conexion.is_connected():  #Desconectamos de la DB
                cursor.close()
                conexion.close()

def validar_login(usuario, contraseña): #Funcion para Validad el usuario registrado en la DB
    try:
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor(dictionary=True)#Crea un cursor que devuelva los resultado como diccionario para acceder 
                                                    #al campo de los usuarios['password']
        cursor.execute('SELECT password FROM usuarios WHERE username = %s',(usuario,)) # Buscsa en la DB que esta el usuario ya 
                                                                                        #registrado, ademas de evitar Inyecciones SQL
        resultado = cursor.fetchone()# Obtiene el usuario encontrado y lo almacena en resultado                                                      
        if resultado: #Verifica que el Cursor devolvio un resultado
            hash_almacenado = resultado['password'].encode('utf-8')  #Toma el valor del campo 'password' del resultado obtenido 
                                                                        #y lo convierte a bytes
            contraseña_bytes = contraseña.encode('utf-8')   #Toma la contraseña en texto plano y la pasa ta bytes para compararla con el hash
            if bcrypt.checkpw(contraseña_bytes, hash_almacenado):  # si verifica que contraseña_bytes sea igual al hast_almecenado
                messagebox.showinfo("Exito","Inicio de sesion exitoso")
                return True
        else:                                       #En caso de que no 
            messagebox.showerror("Error","Usuario o contraseña incorrecto") #Se abre una ventana emergene con el ERROR 
            return False
    except Exception as e:          #En caso de que la conexion no se realice a la DB
        messagebox.showerror("Error",f"Ocurrio un error:{e}")
        return False
    finally:                
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()                                      #CERRAMOS LA CONEXION A LA DB
            conexion.close()

def insertar_productos(nombre,precio,stock): # Funcion para la insercion de productos pasandoles el nombre,precio,stock
    if producto_existente(nombre):  #Si el nombre del producto ya existe 
        messagebox.showerror("Error","El producto ya existe o no se puedo verificar") # Abre una ventana emergente que el producto ya esta
        return False

    try:                                                
        conexion = mysql.connector.connect(**config)    
        cursor=conexion.cursor()
        cursor.execute('''INSERT INTO productos(nombre,precio,stock) VALUES(%s,%s,%s)''',
        (nombre,float(precio),int(stock)))#Realizamos la insercion del prodcuto a la tabla prodcutos
        conexion.commit() #Realizamos el commit a la DB
        return True
    except Exception as err:     #Cuando  la conexion no se realiza 
       messagebox.showerror("Error",f"Insercion de datos fallida: {err}")#Abre una ventana emergente 
       return False     
    finally:
        if 'conexion' in locals() and conexion.is_connected():  
            cursor.close()                      #CERRAMOS LA CONEXION Y EL CURSOR
            conexion.close()

def mostrar_todos_productos(): #Funcion para mostrar todos los productos
    try:
        conexion = mysql.connector.connect(**config)
        cursor=conexion.cursor(dictionary=True)
        cursor.execute('''SELECT * FROM productos''')   #Instruccion para mostrar todos los productos
        productos = cursor.fetchall() # TOma todos los valores y los almacena en productos
        return productos    #Regresa los productos
    except mysql.connector.Error as err: # En caso de que no haga una conexion
       messagebox.showerror("Error",f"Ocurrio un error: {err}")    #Se abre una ventana emergente con el ERROR
       return []    
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()                          #finalmente se cierra la conexion
            conexion.close()

def eliminar_producto(id_producto): #Funcion para eliminar un producto mediante el ID del producto
    try:
        conexion = mysql.connector.connect(**config)    #Hace la conexion
        cursor = conexion.cursor()

        cursor.execute("SELECT id FROM productos WHERE id = %s", (id_producto,)) #Instruccion SQL para buscar el ID del producto
        if not cursor.fetchone():    # Si el cursor no devuelve nada, eso segnifica que el ID del producto no esta registrado
            messagebox.showwarning("Advertencia", "ID de producto no encontrado") #Ventana emergente del error
            return False
        #En caso de que encuentra algo, eliminar ventas asociadas
        cursor.execute("DELETE FROM ventas WHERE producto_id = %s", (id_producto,)) # Busca el ID del producto vendido y lo borra de la tabla Ventas
        
        cursor.execute("DELETE FROM productos WHERE id = %s", (id_producto,)) #Busca el ID del producto en la tabla productos y lo borra 
        conexion.commit()       #Manda las intrucciones
        cursor.execute("SELECT id FROM productos WHERE id = %s", (id_producto,)) # Verificamos que el producto se borro correctamente
        if not cursor.fetchone(): #Si el cursor no devuelve nada, se significa que el producto se elimino 
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
            return True
        else:
            messagebox.showerror("Error", "No se pudo eliminar el producto")#En caso de que devuelva algo entonces aun existe el producto
            return False
            
    except mysql.connector.Error as err: # En caso de que la conexion no se establecio
        messagebox.showerror("Error", f"Error de base de datos: {err}")
        return False
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()                                  #Se cierra el cursor y la conexion a la DB                
            conexion.close()

def producto_existente(nombre): #Funcion que algun producto existe mediante el nombre
    try:
        conexio= mysql.connector.connect(**config)
        curso = conexio.cursor()                        
        curso.execute('SELECT COUNT(*) FROM productos WHERE nombre=%s',(nombre,))#Contamos todos los productos en busca del nombre a buscar
        return curso.fetchone()[0] > 0  #retorna True si existe, y lo retorna el valor
    except Exception as e:      #En caso de que la conexion no sea exitoza
        messagebox.showerror("Error",f"Error al verificar el producto: {e}")
        return True
    finally:            #Cierra secion con la DB y el cursor
        if 'conexion' in locals() and conexio.is_connected():
            curso.close()
            conexio.close()

def actualizar_producto(id_prodcuto,nuevo_precio,nuevo_stock): # Funcion para actualizar los productos con nuevos valores
    try:
        conexion= mysql.connector.connect(**config) 
        cursor = conexion.cursor()                      #SE HACE LA CONEXION A LA DB
        cursor.execute('SELECT COUNT(*) FROM productos WHERE id = %s', (id_prodcuto,)) #Instruccion SQL, 
                                                                                    #para buscar el id del producto a actualizar
        if cursor.fetchone()[0] == 0: #En caso de que no se encuentre que el valor sea NULL
            messagebox.showerror("Error","ID no encontrado")    #Se abrira un ventana emergente con el error
            return False
        cursor.execute('UPDATE productos SET precio=%s,stock=%s WHERE id=%s',(float(nuevo_precio),int(nuevo_stock),int(id_prodcuto))) #En caso 
                                                                                                                                #de que se encuentre
        conexion.commit()  #Hacemos la Actualizacion en la tabla productos y colocamos SET los 
                            #nuevos productos (precio,stock) de acuerdo al id del producto
        messagebox.showinfo("Exito","Se actualizo correctamente") #Se abre una ventana emergente exitozamente
        return True
    except ValueError:  #En caso de que los valores ingresados no sean los correctos
        messagebox.showerror("Error","Precio y Stock deben ser numeros validos")
        return False
    except Exception as e: #Si no se hizo conaxion a la DB 
         messagebox.showerror("Erro",f"Error al actualizar: {e}")
         return False
    finally:            #Se cierra la DB 
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def obtener_ventas():   #Funcion para obtener las ventas obtenidas de los productos
    try:
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor(dictionary=True)  #Devuelve el cursor como un diccionario
        
        cursor.execute("""
            SELECT 
                v.id,  
                u.username as usuario,                  
                p.nombre as producto,
                v.cantidad,
                v.precio_unitario,
                (v.cantidad * v.precio_unitario) as total,
                v.fecha 
            FROM ventas v
            JOIN usuarios u ON v.usuario_id = u.id
            JOIN productos p ON v.producto_id = p.id
            ORDER BY v.fecha DESC
        """)
        ventas = cursor.fetchall() # Al final obtenemos todas las ventas 
        # Formateamos las fechas con Python, al ser datatime, no apareceria bien la fecha 
        for venta in ventas: #Iterando en las ventas en el campo de las fechas 
            venta['fecha'] = venta['fecha'].strftime('%d/%m/%Y %H:%M')
        return ventas   #Retornamos la fecha 
    except Exception as e: #En caso de que la DB no se conecte 
        print(f"Error al obtener ventas: {e}")
        return []
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()              #SE DESCONECTA DE LA DB
            conexion.close()    
#SELECIONAMOS  id de la tabla Ventas, El nombre del usuario que hizo la venta y renombrado a usuario
        #El nombre de producto vendido y renombrado a producto
        #La cantidad de unidades de la venta
        #El precio por unidad del producto
        #Despues sacamos el total de la venta renombrado total
        # Y sacamos la fecha de la venta todo ESTO DE LA TABLA VENTAS renombrado v
        #JOIN usuarios u ON v.usuario_id= u.id ->Obtenemos los datos del usuario que hizo la venta
        #v.usuario_id (campo en la tabla ventas)
        #u.id (campo en la tabla usuarios)
        #JOIN productos p ON v.producto_id = p.id -> Obtenemos los productos vendidos
        #v.producto_id con p.id
        #ORDER BY v,fecha DESC -> Ordenamos las ventas de acuerdo a la fecha de forma descendente


def registrar_venta(usuario_id, producto_id, cantidad, precio_unitario): #Funcion para registrar las ventas pasando los datos de 
                                                                            #(usuario_id, producto_id, cantidad, precio_unitario)
    try:
        conexion = mysql.connector.connect(**config)    #Se conecta a la DB
        cursor = conexion.cursor()
        #Se verificar stock primero, para que el stock no quede en numeros negativos
        cursor.execute("SELECT stock FROM productos WHERE id = %s", (producto_id,)) #Buscamos el producto de acuerdo al ID  
                                                                                    #y seleccionamos el campo del STOCK
        stock_actual = cursor.fetchone()[0] #Retorna el stock
        if cantidad > stock_actual: #Si el stock es mayor que la cantidad que queremos vender, entonces no pasa, y regresa un false
            return False
        #Actualizar stock en caso de que la cantidad sea menor a la que tenemos almacenada
        cursor.execute("UPDATE productos SET stock = stock - %s WHERE id = %s", 
                      (cantidad, producto_id))  #Actualizamos el stock de acuerdo al ID del producto vendido
        #Registrar la venta con los campos obtenidos
        cursor.execute("""INSERT INTO ventas (usuario_id, producto_id, cantidad, precio_unitario)
                         VALUES (%s, %s, %s, %s)""",
                      (usuario_id, producto_id, cantidad, precio_unitario))#Registramos la venta del producto en la tabla de ventas
            #Con el Usuario que hizo la venta, el id del producto,cantidad vendida, y el precio unitario
        conexion.commit() #Mandamos las instrucciones
        return True
    except Exception as e:      #EN CASO DE QUE NO SE HAGA LA CONEXION A LA DB
        print(f"Error al registrar venta: {e}")
        return False
    finally:
        if conexion.is_connected(): #CERRAMOS LA CONEXION Y LOS CURSORES
            cursor.close()
            conexion.close()
