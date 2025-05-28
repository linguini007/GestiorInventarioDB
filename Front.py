import tkinter as tk  #El as sirve como una forma de etiquetado o abreviacion de la libreria tk = tkinter
from tkinter import messagebox #El messagebox sirve para poder mandar mensajes de errores al usuario de forma de ventana
import Back as Back   #Referenciamos nuestro Backend para poder tener conexion a nuestra base de datos
from tkinter import ttk  #Para el Treeview que es para la tabla de mysql


#Creamos una fuente personalizada GRANDE,MEDIANA,PEQUEÑA  SON FORMATOS QUE PODEMOS USAR (podemos variar el todo)
fuente_normal_grande = ('Roboto', 35,'normal') #Normal
fuente_negritas_grande  =('Impact',35,'bold') # Negritas
fuente_cursiva_grande = ('Times', 35, 'italic') #Cursivas
fuente_subrayado_grande =('Calibri', 35, 'underliner') #Subrayado
fuente_tacahdo_grande =('Arial', 35,'overstrike') # Tachado
fuente_arial_grande =("Arial", 35,'normal')#Normal pequeña

fuente_normal_mediana = ('Roboto', 25,'normal') #Normal
fuente_negritas_mediana  =('Impact',25,'bold') # Negritas
fuente_cursiva_mediana = ('Times', 25, 'italic') #Cursivas
fuente_subrayado_mediana =('Calibri', 25, 'underliner') #Subrayado
fuente_tacahdo_mediana =('Arial', 25,'overstrike') # Tachado
fuente_arial_mediana =("Arial", 25,'normal')#Normal pequeñar

fuente_normal_pequeña= ('Roboto', 15,'normal') #Normal
fuente_negritas_pequeña  =('Impact',15,'bold') # Negritas
fuente_cursiva_pequeña = ('Times', 15, 'italic') #Cursivas
fuente_subrayado_pequeña=('Calibri', 15, 'underliner') #Subrayado
fuente_tacahdo_pequeña=('Arial', 15,'overstrike') # Tachado
fuente_arial_pequeña =("Arial", 15,'normal') #Normal pequeña
 #Etiqueta    bg= backgroud     fg= foreground bd=border    cursor(nos sirve para identificar un botton)

Azul_claro = "#392aa8" #Color azul_claro

#Utilizamos SELF para que en la memoria percista las modificaciones en diversas
#funiones a la vez, ademas de que, podemos llamar funciones dentro de otras funciones

#EJEMPLO

#   def crear_widgets():
#       boton = tk.Button(...., command=mostrar_productos)

#(SIN EL self el COMMAND no podria encontrar la funcion mostrar_productos())
#ESTO PUEDE AYUDAR A LA INTERACION DE LA INTERFAZ EN LOS BOTONES Y LAS ENTRADAS
#ADEMAS DE QUE LOS DATOS PERSISTEN ENTRE CLICKS EN LOS BOTONES

#Dentro de las Etiquetas de Texto y Botones el diseño sera muy parecido, en cuestiones de colores y tipo de letras,
# Omitire muchas caracteristicas del diseño de ellos, ya que se vuelve muy repetitivo. ejemplo
# etiqueta_titulo = tk.Label(self.ventana, text="LOGIN USER", font=fuente_negritas_grande, bg=Azul_claro)
#tk.Label ->Asignamos cadenas de texto a nuestra ventana, en este caso (self.ventana) con un texto (text="LOGIN USER") se colocara dentro de la ventana
#Con (font) establecemos un estilo de letras,color,tamaño de letra, con (bg) establecemos el color de fondo del texto

#tk.Entry -> Podemos colocar cajas para colocar texto, tambien se tiene el mismo tipo de diseñoasd

class LoginApp:             #VENTANA DEL LOGIN
    def __init__(self):
        self.ventana = tk.Tk()  #Creamos la ventana emergente llamada ventana
        self.ventana.title("Login") #Como titulo la llamamo "Login"
        self.ventana.geometry("750x500+300+150") # Sera la dimension de la Ventana + el posicionamiento Centrado
        self.ventana.configure(bg=Azul_claro)# BackGroud de color Azul_Claro, definido al inicio del codigo
        self.ventana.resizable(False, False)# No se podra redimensionar la ventana sera estatica y sin el boton de maximizar
        self.crear_widgets() #Crea las widgets de la ventana LoginApp
        Back.crear_tabla_usuarios() #Crea la tabla de los usuarios de la ventana LoginApp
        self.ventana.mainloop() #Cicla la ventana para que no se cierre nada mas ejecutar el programa
    def crear_widgets(self): #Funcion para crear los widgets de la ventana LOGIN
        # Etiquetas de texto dentro de la ventana LoginApp
        etiqueta_titulo = tk.Label(self.ventana, text="LOGIN USER", font=fuente_negritas_grande,bg=Azul_claro) #Texto dentro de la ventana del login con el fondo azul_claro
        etiqueta_usuario = tk.Label(self.ventana, text="Usuario", font=fuente_normal_pequeña,bg=Azul_claro) #Texto dentro de la ventana del login con el fondo azul_claro
        etiqueta_contraseña = tk.Label(self.ventana, text="Contraseña", font=fuente_normal_pequeña,bg=Azul_claro)#Texto dentro de la ventana del login con el fondo azul_claro
        # Entradas de texto dentro de la ventana LoginApp
        self.entrada_usuario = tk.Entry(self.ventana, font=fuente_arial_pequeña,bg='black') # Caja de entrada del nombre del usuario
        self.entrada_contraseña = tk.Entry(self.ventana, show="*", font=fuente_arial_pequeña,bg='black')# Caja de entrada para la constrasena 
        # Botones para interactuar con el Logeo de sesion y registrar el usuario
        boton_login = tk.Button(self.ventana, text="Iniciar Sesion", font=fuente_normal_pequeña,
                                activebackground="lightgreen", relief="raised", bd=5, command=self.on_login)# Boton de inicio con la funcionalidad de on_login
        boton_registro = tk.Button(self.ventana, text="Registrar", font=fuente_normal_pequeña,
                                activebackground="lightgreen", relief="raised", bd=5, command=self.on_registrar)#Boton de registro del usuario con la funcion on_registrar
        # Se usando grid para posicionar mejor los widgets
        etiqueta_titulo.grid(row=0, column=0, columnspan=2, pady=(40, 20), padx=10) # ya sea con pack o con grid podemos colocar en diferentes posiciones
        etiqueta_usuario.grid(row=1, column=0, sticky="e", pady=10, padx=(200, 10)) # pady = se mueve de forma de arriba y abajo
        self.entrada_usuario.grid(row=1, column=1, pady=10, padx=(0, 200)) # padx = se mueve de forma izquierda a derecha
        etiqueta_contraseña.grid(row=2, column=0, sticky="e", pady=10, padx=(200, 10)) # row = renglon y column = columna  sticky es asia donde se va apegar e = east "Este"
        self.entrada_contraseña.grid(row=2, column=1, pady=10, padx=(0, 200)) #Como si fuera una tabla 
        boton_login.grid(row=3, column=0, columnspan=2, pady=(50, 10))  #Solamente son las posiciones de los botones  y el orden 
        boton_registro.grid(row=4, column=0, columnspan=2, pady=10) # con columnspan = 2 toma 2 columnas a la vez 
    def on_registrar(self): # Funciones para el boton del  registro
        usuario = self.entrada_usuario.get()# Se toma la entrada del usuario y lo guarda en usuario
        contraseña = self.entrada_contraseña.get() #Se toma la contraseña y lo guarda en  contraseña
        Back.registrar_usuario(usuario,contraseña) #llamamos a la funcion de registrar_usuario del Backend y le pasamos las credenciales 
    def on_login(self):# Funcion para el boton del Login 
        usuario = self.entrada_usuario.get() # Se toma la entrada del usuario y lo guarda en usuario
        contraseña = self.entrada_contraseña.get() #Se toma la contraseña y lo guarda en  contraseña
        if Back.validar_login(usuario, contraseña): #En caso de que la validacion de la funcion del Backend sea correcta se cierra la ventana del login 
            self.ventana.destroy()          
            Consultas()                     #Y se abre la ventana de las consultas
class Consultas:                          #VENTANA DE LOS PRODUCTOS
    def __init__(self):
        self.ventana2 = tk.Tk()#Creamos la ventana de Consulta  donde gestionamos los producto
        self.ventana2.title("Gestor de Inventario") # Asi es como se llamara la ventana de las consultas
        self.ventana2.geometry("1366x768")   #Las dimensiones de la ventana
        self.ventana2.configure(bg=Azul_claro)  #El color de fondo sera color azul_claro
        self.ventana2.resizable(False, False)   #NO SE PODRA REDIMENSIONAR con los botones ni con el mous
        self.crear_widgets() # Crea todos los widgets declarados en la funcion
        Back.crear_tabla_productos() #Creamos la tabla de los productos 
        self.ventana2.mainloop()#Crea la ciclo para que la ventana no se cierre al momento
    def crear_widgets(self): #Funcion para crear los widgets dentro de la ventana2 o de la ventanta de Gestor de Inventario
        main_frame = tk.Frame(self.ventana2) #Creamos un FRAME dentro de la ventana2 o de consultas
        main_frame.grid(row=0, column=0, padx=100, pady=100, sticky="nsew") # Posiciona el FRAME gusto a x=100,y=100 pixels
        self.ventana2.grid_rowconfigure(0, weight=1) #Cambiamos las propiedades de la fila dentro del contenedor de la ventana2
        self.ventana2.grid_columnconfigure(0, weight=1) #Cambiamos la propiedades de la columna dentro del contenedor de la ventana2
        main_frame.grid_rowconfigure(2, weight=1)           
        main_frame.grid_columnconfigure(0, weight=1)    #Y hacemos lo mismo para el FRAME     (indice_de_la_fila , espacio adicional )
        tk.Label(main_frame, text="Gestión de Productos", font=fuente_negritas_grande).grid(row=0, column=0, columnspan=4, pady=10)  # Título Que tendra dentro de la ventana2 
        # Frame para controles (botones)
        control_frame = tk.Frame(main_frame) #Se crea un FRAME dentro del main_fram 
        control_frame.grid(row=1, column=0, columnspan=4, pady=10, sticky="ew")  #posicion del FREAME ( si esto los botones no se ordenan y no aparecen)
                                                                                    #Es como una tabla de una sola row pero con muchas columnas para los botones
        #LOS BOTONES SE ENCONTRARAN EN EL FRAME DEL CONTROL, PARA MANTENERLOS FIJOS AHI UNO TRAS OTRO
        ttk.Button(control_frame, text="Insertar Producto", command=self.abrir_formulario_insertar)\
            .grid(row=0, column=0, padx=5)# Boton para insertar productos con la funcion abrir_formulario_insertar
        ttk.Button(control_frame, text="Mostrar Productos", command=self.mostrar_todos_productos)\
            .grid(row=0, column=1, padx=5)# Boton para mostrar todos los productos con la funcion mostrar_todos_productos
        ttk.Button(control_frame, text="Eliminar Producto", command=self.abrir_formulario_eliminar)\
            .grid(row=0, column=2, padx=5) #Boton para eliminar un producto con la funcion abrir_formulario_eliminar
        ttk.Button(control_frame, text="Actualizar Producto", command=self.abrir_formulario_actualizar)\
            .grid(row=0, column=3, padx=5)#Boton para actualizar algun producto con la funcion abrir_formulario_actualizar
        ttk.Button(control_frame, text="Vender Productos", command=self.abrir_ventana_ventas)\
            .grid(row=0, column=4, padx=5)#Boton para abrir_ventana_ventas con la funcion abrir_ventana_ventas
        ttk.Button(control_frame, text="Mostrar Ventas", command=self.mostrar_ventas)\
            .grid(row=0, column=5, padx=5)  # Boton para mostrar las ventas que se hayan echo, con la funcion mostrar_ventas
        self.frame_tabla = tk.Frame(main_frame) #Se crea un FRAME para mostrar los productos
        self.frame_tabla.grid(row=2, column=0, columnspan=4, sticky="nsew", pady=10) # Posicionamiento de la tabla
    def mostrar_todos_productos(self): #Funcion para mostara todos los productos 
        for widget in self.frame_tabla.winfo_children(): # Limpiar el frame de tabla si  tiene contenido 
            widget.destroy()                              
        productos = Back.mostrar_todos_productos() #Obteneoms todos los productos de la DB y los vamos almacenando en productos
        if not productos: #SI AUN NO SE INGRESAN PRODUCTOS SE  LANAZRA ESTA VENTANA EMERGENTE
            messagebox.showinfo("Información", "No hay productos registrados")  #DICIENDO QUE NO HAY PRODUCTOS
            return
        # Crear Treeview que seria nuestra tabla que mostrar los productos insertados
        tree = ttk.Treeview(self.frame_tabla,columns=('ID', 'Nombre', 'Precio', 'Stock'),show='headings',style="Compact.Treeview",height=12)
        # Estara dentro del FRAME_TABLA con las columnas 'ID',NOMBRE,PRECIO,STOCK, y las mostraremos como cabeceras con el estilo de compact.Treeview y la separacion entre ellas
        tree.heading('ID', text='ID') #     # Configurar columnas
        tree.heading('ID', text='ID')  #Con .heading hacemos referencia a las cabeceras
        tree.heading('Nombre', text='Nombre')
        tree.heading('Precio', text='Precio (MX)')
        tree.heading('Stock', text='Stock')
        # Ajustar tamaño columnas 
        tree.column('ID', width=50, anchor=tk.CENTER, stretch=False, minwidth=40)
        tree.column('Nombre', width=500, stretch=False, minwidth=200) #EN el caso del nombre puede ser mas largo le damos mas espacio en width y minwidth
        tree.column('Precio', width=100, anchor=tk.CENTER, stretch=False, minwidth=70)
        tree.column('Stock', width=100, anchor=tk.CENTER, stretch=False, minwidth=50)
        # Ahora que tenemos la tabla INsertamos los valores desde el inicio '' hasta el final END iterando en los productos 
        for producto in productos: 
            tree.insert('', tk.END, values=(
                producto['id'],             #campos de producto[id], producto[nombre], ... .. ..
                producto['nombre'],
                f"${producto['precio']:.2f}",       #Solo tomamos valores flotantes de 2 decimales 10.00 o 10.01
                producto['stock']
            ))
        # Como pueden ser mucho productos para poder visualizar la tabla completa, agregamos un SCROLLBAR para subir y  bajar en la tabla
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL, command=tree.yview)#Se encontrara en el FRAME de la tabla orientaba de forma vertical en el tree.yview
        tree.configure(yscroll=scrollbar.set) #configuramos el tree para agregar el scrollbar a la tabla
        tree.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)   # Posicionamiento del Tree y del scrollbar
        scrollbar.grid(row=0, column=1, sticky="ns")# Orientamos el scrollbar
        self.frame_tabla.grid_rowconfigure(0, weight=1)  # Ajustar el posicionamiento del FRAM TABLA en las filas
        self.frame_tabla.grid_columnconfigure(0, weight=1) #COmo en las columnas
        btn_cerrar = tk.Button(self.frame_tabla, text="Cerrar Tabla", # Botón para cerrar la tabla
                               command=lambda: [w.destroy() for w in self.frame_tabla.winfo_children()])#Creamos el boton cerrar tabla con el mismo ciclo del inicio de esta funcion
        btn_cerrar.grid(row=1, column=0, columnspan=2, pady=10) # posicionamos el boton en la parte inferior del frame tabla
    def abrir_formulario_insertar(self): #Funcion para abrir formulario para insertar  nuevos productos
        formulario = tk.Toplevel(self.ventana2)# Se crea una ventana por encima de la ventana2 llamada formulario
        formulario.title("Agregar un nuevo Producto") # La ventana se llamara asi 
        formulario.grab_set()  #PARA MANTENER POR ENCIMA DE LA VENTANA
        self.ventana_insertar = formulario  #EVITAR MULTIPLES VENTANAS AL HACER CLICK
        tk.Label(formulario, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)#Se crea un texto que estara en el formulario 
        entry_nombre = tk.Entry(formulario)# se crea una caja para la insercion de los datos dentro del formulario
        entry_nombre.grid(row=0, column=1, padx=10, pady=5)# EL posicionamiento de la caja de entrada del nombre
        tk.Label(formulario, text="Precio:").grid(row=1, column=0, padx=10, pady=5)#Se crea un texto que estara en el formulario
        entry_precio = tk.Entry(formulario)#se crea una caja para la insercion de datos dentro del formulario
        entry_precio.grid(row=1, column=1, padx=10, pady=5)#EL posicionamiento de la caja
        tk.Label(formulario, text="Stock:").grid(row=2, column=0, padx=10, pady=5)#Se crea un texto que estara en el formulario
        entry_stock = tk.Entry(formulario)#se crea una caja para la insercion de datos dentro del formulario
        entry_stock.grid(row=2, column=1, padx=10, pady=5)#EL posicionamiento de la caja
        def confirmar():#Funcion para confirmar que los campos sea correctos y que esten completos
            nombre = entry_nombre.get() #LE  PASAMOS LO ALMACENADO DE LAS CAJAS nombre,precio,stock
            precio = entry_precio.get()
            stock = entry_stock.get()
            if not all([nombre, precio, stock]):#Validamos que todos los campos esten completos con los datos
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
            try:    #Si estan completos  se asegura que el precio y el stock sean positivos 
                precio = float(precio) 
                stock = int(stock)
                if precio <= 0 or stock < 0:
                    raise ValueError
            except ValueError:  #En caso de que uno de ellos no este bien, mandara una ventana emergente con el ERROR
                messagebox.showerror("Error", "Precio y stock deben ser números positivos")
                return
            if Back.insertar_productos(nombre, precio, stock): #Subimos los datos con la funcion del BACKEND de insertar_productos (nombre,precio,stock)
                messagebox.showinfo("Éxito", "Producto agregado correctamente") #Y se muestra una ventana emergente que fue realizada la accion
                self.mostrar_todos_productos()  #Actualiza la tabla
                formulario.destroy()    #Y cierra el formulario de insercion de nuevos productos
        ttk.Button(formulario, text="Guardar", command=confirmar).grid(row=3, columnspan=2, pady=10)#creamos un boton que estara en el formulario
        formulario.protocol("WM_DELETE_WINDOW", formulario.destroy)#Con la funcion de confirmar los valores y cuando se elimina cuando el formulario se destruye
    def abrir_formulario_eliminar(self):#Funcion para abrir el formulario de eliminar producto por ID
        formulario = tk.Toplevel(self.ventana2)# Ventana emergente para eliminar dentro de la ventana2
        formulario.title("Eliminar Producto")#Titulo de la ventana
        formulario.grab_set()  #PARA MANTENER POR ENCIMA DE LA VENTANA
        formulario.resizable(False, False)#No se puede redimensionar
        tk.Label(formulario, text="ID del Producto a Eliminar:").grid(row=0, column=0, padx=10, pady=5)#Se crea un texto  dentro del formulario
        entry_id = tk.Entry(formulario) #Se crea una caja para ingresar datos del ID
        entry_id.grid(row=0, column=1, padx=10, pady=5)#Posicionamiento de la caja para ingresar datos del ID

        def confirmar_eliminar(): #Funcion para confirmar que exista el ID que vamos a borrar
            id_producto = entry_id.get()# tomamos el dato de la caja osea el ID
            if not id_producto.isdigit(): #En caso de que NO sea un digito 
                messagebox.showerror("Error", "El ID debe ser un número") #Se abrira una ventana emergente
                return
            if messagebox.askyesno("Confirmar", f"¿Eliminar producto ID {id_producto} y sus ventas asociadas?"):#Muestra una ventana de SI o NO  antes de eliminar el producto
                Back.eliminar_producto(int(id_producto))  # Llamamos la funcion del Backend para eliminar el prodcuto
                self.mostrar_todos_productos()  # Y actualizamos los productos mostrando la nueva tabla sin el producto
                # formulario.destroy()
        # Botones (Aceptar/Cancelar)
        botones_frame = tk.Frame(formulario)#Creamos otro FRAME dentro de formulario para posicionar los botones de eliminar y Cancelar
        botones_frame.grid(row=1, column=0, columnspan=2, pady=10) #La posicion del FRAME

        btn_eliminar = tk.Button(botones_frame, text="Eliminar", font=fuente_normal_pequeña, command=confirmar_eliminar)#Creamos el boton eliminar con la accion confirmar_eliminar
        btn_eliminar.grid(row=0, column=0, padx=5)# el posicionamiento del boton

        btn_cancelar = tk.Button(botones_frame, text="Cancelar", font=fuente_normal_pequeña, command=formulario.destroy)#Creamos el boton eliminar con la accion  formulario.destroy
        btn_cancelar.grid(row=0, column=1, padx=5)#posicionamiento del boton
    def abrir_formulario_actualizar(self):#Funcion para Actualizar un producto por ID
        self.ventana_actualizar = tk.Toplevel(self.ventana2)#Creamos una ventana por encima de ventana2 para actualizar algun producto
        self.ventana_actualizar.title("Actualizar Producto") #Titulo de la ventana
        self.ventana_actualizar.resizable(False, False)#NO se puede redimensionar
        self.ventana_actualizar.geometry('500x250') #Tamano de la ventana
        self.ventana_actualizar.grab_set()# no se puede abrir mas de 1 vez (en caso de hacer muchos click en el boton)
        tk.Label(self.ventana_actualizar, text="ID del Producto:", font=fuente_normal_pequeña).grid(row=0, column=0, padx=10, pady=5)#Texto dentro de la ventana_actualizar
        entry_id = tk.Entry(self.ventana_actualizar, font=fuente_normal_pequeña)#caja de entrada de datos en la ventana de actualizar
        entry_id.grid(row=0, column=1, padx=10, pady=5)#posicionamiento de la caja
        tk.Label(self.ventana_actualizar, text="Nuevo Precio (MX):", font=fuente_normal_pequeña).grid(row=1, column=0, padx=10, pady=5)#Txto dentro de la ventana_actualizar
        entry_precio = tk.Entry(self.ventana_actualizar, font=fuente_normal_pequeña)#caja de entrada de datos en la ventana de actualizar
        entry_precio.grid(row=1, column=1, padx=10, pady=5)#posicionamiento de la caja
        tk.Label(self.ventana_actualizar, text="Nuevo Stock:", font=fuente_normal_pequeña).grid(row=2, column=0, padx=10, pady=5)#Texto dentro de la ventana_actualizar
        entry_stock = tk.Entry(self.ventana_actualizar, font=fuente_normal_pequeña)#caja de entrada de datos en la ventana de actualizar
        entry_stock.grid(row=2, column=1, padx=10, pady=5)#posicionamiento de la caja
        def confirmar_actualizacion():#Funcion para confirmar que todos los datos sean correctos
            id_producto = entry_id.get()
            nuevo_precio = entry_precio.get()# Le pasamos los valores id,precio,stock
            nuevo_stock = entry_stock.get()
            if not all([id_producto, nuevo_precio, nuevo_stock]): #Verificamos que todos los campos esten colocados
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
            try: #En caso de que si 
                nuevo_precio = float(nuevo_precio)
                nuevo_stock = int(nuevo_stock)
                if nuevo_precio <= 0 or nuevo_stock < 0:#Verificamos que el precio y el stock sean valores positivos
                    raise ValueError
            except ValueError:          #si alguno esta de forma negativa no se podra validar
                messagebox.showerror("Error", "Precio y stock deben ser números válidos")
                return
            if Back.actualizar_producto(id_producto, nuevo_precio, nuevo_stock):# Llamamos del Backend a actualizar_producto y le pasamos (id,precio,stock)
                self.mostrar_todos_productos() # Se actualizara 
                self.ventana_actualizar.destroy() # y se cerrara la ventana de actualizar
            else:
                messagebox.showerror("Error", "No se pudo actualizar el producto. Verifica el ID.") #EN caso de que no se encuentre el ID mostrara un error
        btn_frame = tk.Frame(self.ventana_actualizar) # Creamos un FRAME para los botones 
        btn_frame.grid(row=3, columnspan=2, pady=10)#Lo posicionamos 
        ttk.Button(btn_frame, text="Actualizar", command=confirmar_actualizacion).grid(row=0,column=0,padx=5)#Creamos el boton de actualizar con la funcion de confirmar
        ttk.Button(btn_frame, text="Cancelar", command=self.ventana_actualizar.destroy).grid(row=0,column=1,padx=5)#y otro para cancelar con la funcion del destroy
    def procesar_venta(self, tree, spin_cantidad): #Funcion para seleccionar el producto a vender del Tree
        seleccionado = tree.selection() # le pasamos el valor seleccionado del Tree osea de la tabla
        if not seleccionado: #Si queremos vender y no hemos seleccionado antes un producto
            messagebox.showerror("Error", "Selecciona un producto primero") #Mandara un ERROR
            return
        
        try: #En caso de que si seleccionemos un prodcutos 
            item = tree.item(seleccionado[0]) #obtenemos los items o los valores del producto seleccionado
            producto_id = int(item['values'][0]) #QUe serian el ID del prodcuto
            nombre = item['values'][1]          # EL nombre del prodcuto
            precio = float(item['values'][2].replace('$', ''))  # Convertir "$100.00" a 100.00
            cantidad = int(spin_cantidad.get()) # Se obtiene el valor seleccioando por el usuario osea lo que va a vender
            stock_actual = int(item['values'][3]) #y obtiene el stock

            if cantidad <= 0: #Si la cantidad es negativa de lo que va a vender es decir que venda  -1 producto NO
                messagebox.showerror("Error", "La cantidad debe ser mayor a 0")
                return
                
            if cantidad > stock_actual: #Si la cantidad a vender sobre pasa de cero manda un error
                messagebox.showerror("Error", f"No hay suficiente stock. Disponible: {stock_actual}")
                return
            if Back.registrar_venta(1, producto_id, cantidad, precio):  # Usuario_id hardcodeado como 1 por ahora porque no hay mas administadores mas que UNO
                messagebox.showinfo("Éxito", f"Venta registrada: {nombre} x {cantidad}")# registramos la venta y manda una ventana emergente
                tree.item(seleccionado[0], values=(   #Actualizamos la tabla de ventas 
                    producto_id,
                    nombre,
                    f"${precio:.2f}",
                    stock_actual - cantidad
                ))
            else:
                messagebox.showerror("Error", "No se pudo registrar la venta") #EN caso de que no se pueda realizar la venta
                
        except ValueError:
            messagebox.showerror("Error", "Cantidad inválida")# Si la canitdad es NULL
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}") #En caso de que definitivamente no se pueda realizar la accion
    def abrir_ventana_ventas(self): #Funcion para abrir_ventana_ventas
        ventana_ventas = tk.Toplevel(self.ventana2)#Creamos una ventana sobre la ventana2 para 
        ventana_ventas.title("Vender Productos")#titulo de la ventana
        ventana_ventas.geometry("900x600")#dimensiones de la ventana
        ventana_ventas.resizable(False, False) #Nose podra redimensionar
        ventana_ventas.grab_set() #No se abrira mas de 1 vez
        ventana_ventas.grid_rowconfigure(0, weight=1)  # Configuración de grid principal 
        ventana_ventas.grid_columnconfigure(0, weight=1)
        main_frame = tk.Frame(ventana_ventas)   # Frame principal  #Crea un FRAME dentro de la veentan de venta_ventas
        main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10) #Posicionamiento del FRAME
        main_frame.grid_rowconfigure(1, weight=1)  # Para que el treeview expanda por le misma ventana
        main_frame.grid_columnconfigure(0, weight=1)  # Tome la mayoria de la misma ventana
        tree_frame = tk.Frame(main_frame)   # Treeview con scrollbar #Creamos un FRAME dentro del MAIN_FRAME para almacenar la tabla de las ventas
        tree_frame.grid(row=1, column=0, sticky="nsew", pady=(0,10))# orientamos el FRAME 
        tree_frame.grid_rowconfigure(0, weight=1)#configuramos tanto los renglones como,las columnas 
        tree_frame.grid_columnconfigure(0, weight=1)#Del Tree_Frame
        scroll_y = tk.Scrollbar(tree_frame) #Creamos un scrollbar para el tree_frame
        scroll_y.grid(row=0, column=1, sticky="ns")# y lo orientamos a la derecha
        tree = ttk.Treeview(tree_frame,  
                        columns=('ID', 'Nombre', 'Precio', 'Stock'), 
                        yscrollcommand=scroll_y.set,
                        selectmode='browse') #Creamos la tabla dentro del tree_frame con los campos, y solo podemos selecionar un producto a la vez no todos juntos
        tree.heading('#0', text='', anchor='w')    # Configurar las cabeceras y renglones de la tabla# Eliminamos la primera cabecera la hacemos invisible basicamente
        tree.heading('ID', text='ID', anchor='center')
        tree.heading('Nombre', text='Nombre') # CREAMOS LAS CABECERAS PARA LA TABLA
        tree.heading('Precio', text='Precio (MXN)', anchor='e')
        tree.heading('Stock', text='Stock', anchor='center')
        tree.column('#0', width=0, stretch=False)#  Eliminamos la primera cabecera la hacemos invisible basicamente
        tree.column('ID', width=80, anchor='center')
        tree.column('Nombre', width=300) #CREAMOS LAS COLUMNAS PARA LOS DATOS
        tree.column('Precio', width=150, anchor='e')
        tree.column('Stock', width=100, anchor='center')
        scroll_y.config(command=tree.yview) # CONFIGURAMOS EL COMANDO DEL SCROLL para subir y bajar
        tree.grid(row=0, column=0, sticky="nsew") # Posicionamos el scroll
        try: # Obtener y mostrar productos
            productos = Back.mostrar_todos_productos() # le pasamos los productos a productos
            if not productos: #Si productos esta vacio
                tk.Label(main_frame, text="No hay productos registrados", fg='red').grid(row=0, column=0)# Muestra un error
                return
            for prod in productos: #si hay productos 
                tree.insert('', 'end', values=(
                    prod['id'],
                    prod['nombre'], #MUestra todo relacionado a los productos 
                    f"${prod['precio']:.2f}",
                    prod['stock']
                ))
        except Exception as e: # En caso de que no se puedan pasar los productos a la tabla
            messagebox.showerror("Error", f"No se pudieron cargar productos: {str(e)}")
            return
        controls_frame = tk.Frame(main_frame) # Controles de venta  dentro del MAIN FRAME
        controls_frame.grid(row=2, column=0, sticky="ew", pady=10)# posicionamineto del FRAME de los controles
        tk.Label(controls_frame, text="Cantidad:").grid(row=0, column=0, sticky="e") #TEXTO PARA EL FRAME CONTROLS
        spin_cantidad = tk.Spinbox(controls_frame, from_=1, to=100, width=5) #Selecciona el valor que quiere vender
        spin_cantidad.grid(row=0, column=1, padx=5)# El posicionamiento del spin_cantidad
        btn_vender = tk.Button(controls_frame, text="Vender", 
                            command=lambda:self.procesar_venta(tree, spin_cantidad))
        btn_vender.grid(row=0, column=2, padx=5) #CREAMOS UN BOTON vender y le pasamos la cantidad a vender ademas del posicionamiento
    def mostrar_ventas(self): #FUncion para mostrar venta
        for widget in self.frame_tabla.winfo_children():  # Limpiar el frame de tabla si tiene contenido
            widget.destroy()
        ventas = Back.obtener_ventas() # Llamamos el funcion obtener_ventas del Backend y lo vamos pasando a ventas
        if not ventas: # Si no hay ventas no mostramos nada
            messagebox.showinfo("Información", "No hay ventas registradas")
            return
        tree = ttk.Treeview(self.frame_tabla, columns=('ID', 'Usuario', 'Producto', 'Cantidad', 'P. Unitario', 'Total', 'Fecha'), show='headings')# Crear Treeview
        columnas = [
            ('ID', 50),
            ('Usuario', 120),
            ('Producto', 200),
            ('Cantidad', 80),        # Configurar columnas con la separacion una de la otra
            ('P. Unitario', 100),   
            ('Total', 100),
            ('Fecha', 150)
        ]
        for col, width in columnas: #Iteramos entre las columnas para crear la tabla
            tree.heading(col, text=col) 
            tree.column(col, width=width, anchor=tk.CENTER if col in ['ID', 'Cantidad'] else tk.W) #Ademas de ir cambiando el tamano del las columnas
        for venta in ventas:  #Iteramos en las ventas
            tree.insert('', tk.END, values=( # de inicio a final 
                venta['id'],
                venta['usuario'],
                venta['producto'],  #en todos los campos de venta
                venta['cantidad'],
                f"${venta['precio_unitario']:.2f}",     #ADEMAS DE AGREGAR EL PRECIO UNITARIO
                f"${venta['total']:.2f}", #Y EL TOTAL POR CADA PRODUCTO VENDIDO 
                venta['fecha']  # Usamos el campo 'fecha' directamente (ya que está formateado)
            ))
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL, command=tree.yview)#CREAMOS UN SCROLLBAR 
        tree.configure(yscroll=scrollbar.set)#Lo configuramos 
        tree.grid(row=0, column=0, sticky="nsew") # y lo posicionamos 
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.frame_tabla.grid_rowconfigure(0, weight=1) #Expandimos mas el frame de la tabla
        self.frame_tabla.grid_columnconfigure(0, weight=1)
        btn_cerrar = ttk.Button(self.frame_tabla, text="Cerrar",  command=lambda: [w.destroy() for w in self.frame_tabla.winfo_children()])
        btn_cerrar.grid(row=1, column=0, columnspan=2, pady=10) #Creamos el boton para cerrar el frame de la tabla 

class Main_tienda(): #Funcion MAIN  llamada Main_tienda() 
    def __init__(self): #Que contiene como inicializacion una funcion que manda
        LoginApp()      #a llamar a la funcion LoginApp() que es nuestro login al inicio del programa
                    #Dentro de esa funcionesta la llamada a la funcion consultas que es el resto del programa
Main_tienda() #INICIAMOS EL PROGRAMA