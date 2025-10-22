# Pseudocódigo para `menu_simple.py`

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
