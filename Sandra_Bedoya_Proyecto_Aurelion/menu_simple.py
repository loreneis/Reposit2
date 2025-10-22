"""
menu_simple.py
Menú sencillo con 4 opciones para el usuario.

Cómo usar:
- Ejecuta: python menu_simple.py
- Selecciona una opción numérica y presiona Enter.
- 0 termina el programa.

Este script sigue el estilo "nivel pollito": funciones cortas, comentarios claros y pruebas simples.
"""

import sys

# Intentar forzar salida en UTF-8 para consolas que no lo detecten bien (Windows PowerShell)
try:
    # Disponible en Python 3.7+
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    # Si no está disponible, seguimos igual (no es crítico)
    pass


def opcion_texto_largo_1():
    """Devuelve un texto largo para la opción 1."""
    texto = """1 - Tema, Problema y Solución

Tema:
Utilizar los datos de la tienda para tomar decisiones que nos den más ventas.

Problema:
- 1- ¿Qué tipo de productos se venden más: Alimentos o Limpieza?
- 2- ¿En qué meses o días de la semana vendemos más?

Solución:
- 1- Agrupar las ventas por categoría de producto ("Alimentos" o "Limpieza") y sumar el total vendido en cada una, para identificar qué línea de productos genera mayores ingresos y enfocar estrategias de compra, inventario o promoción hacia esa categoría.
- 2- Analizar la fecha de cada venta y agrupar los datos según el mes y el día de la semana, para luego sumar los montos de venta en cada grupo para comparar los resultados.
    Este tipo de análisis permite:
    * Planificar mejor la disponibilidad de productos.
    * Organizar al personal según los días de mayor actividad.
    * Diseñar promociones específicas para los periodos de menor venta.
"""

    return texto


def opcion_texto_largo_2():
    """Devuelve un texto largo para la opción 2."""
    texto = """ ## 2. Dataset de referencia: fuente, definición, estructura, tipos y escala


--DATASET : Vamos a trabajar sobre una base de datos relacional que contiene los siguientes 4 archivos en tablas en texto plano :

### Clientes
- Id_Cliente : número único de cada cliente  
- Nombre_Cliente :  nombre de la persona o empresa  
- Email:
- Ciudad:   
- Fecha_Alta: fecha creacion

### Productos
- Id_Producto : número único de cada producto  
- Nombre_Producto: nombre  
- Categoria : tipo de producto  
- Precio_Unitario : cuánto cuesta

### Ventas
- Id_Venta: número único de cada venta  
- Fecha_Venta : día de la venta  
- Id_Cliente : quién compró
- Nombre_Cliente
- Email:  
- Medio_Pago: tarjeta, efectivo

### Detalle_Ventas
- Id_Venta : a qué venta pertenece  
- Id_Producto : qué producto es  
- Nombre_Producto : 
- Cantidad : cuántas unidades  
- Precio_Unitario : 
- Importe : subtotal 


--- Tipo_Datos / Escala de Medicion :

| Columna         | Tabla           | Descripción                          | Tipo de dato | Escala                  |
|-----------------|-----------------|--------------------------------------|--------------|-------------------------|
| Id_Cliente      | Clientes/Ventas | Número único de cada cliente         | int          | Nominal (identificador) |
| Nombre_Cliente  | Clientes/Ventas | Nombre de la persona o empresa       | str          | Nominal (categoría)     |
| Email           | Clientes/Ventas | Correo electrónico del cliente       | str          | Nominal                 |
| Ciudad          | Clientes        | Ciudad del cliente                   | str          | Nominal                 |
| Fecha_Alta      | Clientes        | Fecha de creación del cliente        | datetime     | Intervalo               |
| Id_Producto     | Productos/Detalle | Número único de cada producto      | int          | Nominal (identificador) |
| Nombre_Producto | Productos/Detalle | Nombre del producto                | str          | Nominal                 |
| Categoria       | Productos       | Tipo de producto                     | str          | Nominal                 |
| Precio_Unitario | Productos/Detalle | Precio por unidad del producto     | float        | Razón                   |
| Id_Venta        | Ventas/Detalle  | Número único de cada venta           | int          | Nominal (identificador) |
| Fecha_Venta     | Ventas          | Día de la venta                      | datetime     | Intervalo               |
| Medio_Pago      | Ventas          | Forma de pago (tarjeta, efectivo)    | str          | Nominal (categoría)     |
| Cantidad        | Detalle_Ventas  | Número de unidades vendidas          | int          | Razón                   |
| Importe         | Detalle_Ventas  | Subtotal (Cantidad * Precio_Unitario)| float        | Razón                   |
"""
    return texto


def opcion_texto_largo_3():
    """Devuelve un texto largo para la opción 3."""
    texto = """
### ***** Diagrama de flujo codigo ASCII:

  Inicio
    |
    v
 Mostrar menú
    |
    v
 Leer opción
    |
    +-- '0' --> Salir
    |
    +-- '1' --> Tema, Problema y Solución
    |
    +-- '2' --> Dataset de referencia: fuente, definición, estructura, tipos y escala
    |
    +-- '3' --> Pseudocódigo y diagrama del programa
    |
    +-- '4' --> Sugerencias y mejoras aplicadas con Copilot
    |
    +-- otra --> "Opción no válida"
    |
    v
 Volver a Mostrar menú (repetir)

Notas:
- Ctrl-C o EOF interrumpen y salen del programa.

    
### *******Pseudocodigo para MENU


Este archivo contiene pseudocódigo en español que describe la estructura y el flujo del script `menu_simple.py`.

## Resumen

Programa de consola con un menú sencillo que ofrece 3 opciones que muestran textos largos y una opción 0 para salir. Incluye pruebas simples ejecutadas al iniciar.

## Forma general

1. Definir funciones que devuelven textos largos para cada opción (1, 2, 3).
2. Definir función para mostrar el menú en la consola.
3. Definir función que maneja la opción ingresada y devuelve el texto correspondiente o None para salir.
4. Definir `main` que muestra el menú en un bucle, pide entrada al usuario, llama al manejador y actúa según la respuesta.
5. Definir pruebas sencillas que verifican la salida de las funciones y del manejador.
6. En `if __name__ == '__main__'`: ejecutar pruebas; si pasan, ejecutar `main()`.

## Pseudocódigo (detalle por función)

funcion opcion_texto_largo_1():
    # Devuelve un texto largo descriptivo para la opción 1
    texto = "Texto largo y explicativo para la opción 1"
    devolver texto

funcion opcion_texto_largo_2():
    # Devuelve un texto largo descriptivo para la opción 2
    texto = "Texto largo y explicativo para la opción 2"
    devolver texto

funcion opcion_texto_largo_3():
    # Devuelve un texto largo descriptivo para la opción 3
    texto = "Texto largo y explicativo para la opción 3"
    devolver texto

funcion mostrar_menu():
    imprimir "Menú principal:"
    imprimir "1 - Mostrar texto largo 1"
    imprimir "2 - Mostrar texto largo 2"
    imprimir "3 - Mostrar texto largo 3"
    imprimir "0 - Salir"

funcion manejar_opcion(opcion_string):
    opcion = opcion_string.trim()
    si opcion == '0':
        devolver None   # señal para salir
    si opcion == '1':
        devolver opcion_texto_largo_1()
    si opcion == '2':
        devolver opcion_texto_largo_2()
    si opcion == '3':
        devolver opcion_texto_largo_3()
    devolver "Opción no válida. Intenta de nuevo."

funcion main():
    mientras True:
        mostrar_menu()
        intentar:
            seleccion = leer entrada del usuario con prompt "Selecciona una opción: "
        excepto EntradaInterrumpida (EOF o Ctrl-C):
            imprimir "Entrada interrumpida. Saliendo..."
            salir del bucle

        resultado = manejar_opcion(seleccion)
        si resultado es None:
            imprimir "Saliendo del programa. ¡Hasta luego!"
            romper  # termina el bucle
        imprimir resultado

## Pruebas simples (nivel pollito)

funcion _run_tests():
    # Verifica que las funciones de texto devuelvan cadenas no vacías
    afirmar opcion_texto_largo_1() no esta vacio
    afirmar opcion_texto_largo_2() no esta vacio
    afirmar opcion_texto_largo_3() no esta vacio

    # Verifica el manejador de opciones
    afirmar manejar_opcion('1') empieza con 'Esta es'  # comprobación orientativa
    afirmar manejar_opcion('2') empieza con 'Opción 2'
    afirmar manejar_opcion('3') empieza con 'Opción 3'
    afirmar manejar_opcion('0') es None
    afirmar 'no válida' en manejar_opcion('x')

## Flujo al ejecutar el script

si __name__ == '__main__':
    intentar:
        _run_tests()
    excepto AssertionError como e:
        imprimir 'Fallo en pruebas internas:', e
        salir con codigo 1

    main()

## Notas

- El pseudocódigo mantiene el estilo "nivel pollito": claro, simple y con funciones cortas.
- Las pruebas son intencionalmente básicas y sirven como chequeo rápido al iniciar.
.
"""
    return texto


def opcion_texto_largo_4():
    """Devuelve un texto largo para la opción 4."""
    texto = """
Promts usados para generar el código con Copilot:

    1. "Desde ahora todo el código Python generado y documentado a nivel pollito"
    2. "Hacer un programa que tenga 4 opciones de los 4 puntos de la documentación, muestre texto de cada uno y si coloco 0 salga del programa."
    3. "Agrega comentarios claros y documentados en el código."
    4. "Hazlo más sencillo, nivel pollito."
    5. "quita las pruebas el programa básico."
    6. "Corrígelo que vuelva al menú después de cada opción."
    7. "Crea un mensaje de salida amigable."
    8. "Crea un md con el diagrama de flujo en codigo ascii y pseudocodigo."
    9. "Hazlo más fácil para entenderlo."
    10. "crea un archivo md con los principales prompts usados en copilot."



    """
    return texto


def mostrar_menu():
    """Muestra el menú y pide la opción al usuario."""
    print('\nMenú principal:')
    print('1 - Tema, Problema y Solucion')
    print('2 - Dataset de referencia: fuente, definición, estructura, tipos y escala')
    print('3 - Pseudocódigo y diagrama del programa')
    print('4 - Sugerencias y mejoras aplicadas con Copilot')
    print('0 - Salir')


def manejar_opcion(opcion):
    """Recibe la opción (string) y retorna el texto a mostrar o None para salir."""
    opcion = opcion.strip()
    if opcion == '0':
        return None
    if opcion == '1':
        return opcion_texto_largo_1()
    if opcion == '2':
        return opcion_texto_largo_2()
    if opcion == '3':
        return opcion_texto_largo_3()
    if opcion == '4':
        return opcion_texto_largo_4()
    return "Opción no válida. Intenta de nuevo."


def main():
    """Bucle principal del menú (versión simple).

    Pasos:
    1. Mostrar el menú
    2. Leer la selección del usuario
    3. Procesar la opción y mostrar resultado
    4. Repetir hasta que el usuario elija '0' o interrumpa la entrada
    """
    # Versión explícita del bucle para facilitar la comprensión:
    # - Usamos la variable `opcion` para controlar cuándo salir.
    # - El bucle continúa mientras `opcion` no sea '0'.
    # Estructura simple: leer, procesar, volver a leer
    mostrar_menu()
    opcion = input('Selecciona una opción: ')

    while opcion != '0':
        resultado = manejar_opcion(opcion)
        if resultado is None:
            print('Saliendo del programa. ¡Hasta luego!')
            return

        print('\n' + resultado + '\n')
        # Pausa simple para que el texto largo no desaparezca de la pantalla
        try:
            input('Presiona Enter para volver al menú...')
        except Exception:
            # En ejecución no interactiva puede fallar, ignoramos
            pass

        # Mostrar el menú y pedir otra opción
        mostrar_menu()
        opcion = input('Selecciona una opción: ')

    # Si salimos del bucle porque `opcion` es '0', mostrar mensaje de despedida
    print('Saliendo del programa. ¡Hasta luego!')


if __name__ == '__main__':
    # Ejecuta el programa principal
    main()
