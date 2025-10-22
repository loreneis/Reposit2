# Documentación del Proyecto_Aurelion
## 1. Tema, Problema, Solucion: 
Tema:
Utilizar los datos de la tienda para tomar decisiones que nos den mas ventas 

Problema:
- 1-  ¿Que tipo de productos se venden mas Alimentos o limpieza?
- 2-  ¿En qué meses o días de la semana vendemos más?

Solucion:

- 1- Agrupar las ventas por categoría de producto ( “Alimentos” o “Limpieza”) y sumar el total vendido en cada una, para identificar qué línea de productos genera mayores ingresos y enfocar estrategias de compra, inventario o promoción hacia esa categoría.
- 2- Analizar la fecha de cada venta y agrupar los datos según el mes y el día de la semana, para luego sumar los montos de venta en cada grupo para comparar los resultados. 
- - Este tipo de análisis permite:
        *Planificar mejor la disponibilidad de productos.
        *Organizar al personal según los días de mayor actividad.
        *Diseñar promociones específicas para los periodos de menor venta. 


## 2. Dataset de referencia: fuente, definición, estructura, tipos y escala


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





