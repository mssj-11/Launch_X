#Ejercicio: Uso de funciones en Python
#Ejercicio 1: Trabajar con argumentos en funciones


# Función para leer 3 tanques de combustible y muestre el promedio
def informe(tanque_vacio, tanque_mediano, tanque_lleno):
    promedio_total = (tanque_vacio + tanque_mediano + tanque_lleno) / 3
    return f"""El Informe de combustible es:
    El Promedio Total : {promedio_total}%
    Tanque Vacio: {tanque_vacio}%
    Tanque Mediano: {tanque_mediano}%
    Tanque Lleno: {tanque_lleno}% 
    """

# Llamamos a la función que genera el reporte print(funcion(tanque1, tanque2, tanque3))
print(informe(0, 50, 100))


# Función promedio 
def promedio(values):
    total = sum(values)
    number_of_items = len(values)
    return total / number_of_items



# Actualiza la función
def informe(tanque_vacio, tanque_mediano, tanque_lleno):
    return f"""El Informe de combustible es:
    El Promedio Total : {promedio([tanque_vacio, tanque_mediano, tanque_lleno])}%
    Tanque Vacio: {tanque_vacio}%
    Tanque Mediano: {tanque_mediano}%
    Tanque Lleno: {tanque_lleno}% 
    """


# Volver a imprimir los datos actualizados
print(informe(0, 60, 100))


#*****************************************************************************************

#Ejercicio 2: Trabajo con argumentos de palabra clave
#Ejercicio : Trabajar con argumentos de palabras clave en funciones


# Función para leer 3 tanques de combustible y muestre el promedio
def segundo_informe(tanque_vacio, tanque_mediano, tanque_lleno):
    total_average = (tanque_vacio + tanque_mediano + tanque_lleno) / 3
    return f"""El Segundo Informe de combustible es:
    El Promedio Total : {total_average}%
    Tanque Vacio: {tanque_vacio}%
    Tanque Mediano: {tanque_mediano}%
    Tanque Lleno: {tanque_lleno}% 
    """


# Llamamos a la función que genera el reporte print(funcion(tanque1, tanque2, tanque3))
print(segundo_informe(0, 70, 100))



# Función promedio 
def seg_promedio(values):
    total = sum(values)
    number_of_items = len(values)
    return total / number_of_items

seg_promedio([1, 75, 100]) #agregando otros datos

# Actualiza la función
def generate_report(tanque_vacio, tanque_mediano, tanque_lleno):
    return f"""El Segundo Informe Actualizado de combustible es:
    El Promedio Total : {seg_promedio([tanque_vacio, tanque_mediano, tanque_lleno])}%
    Tanque Vacio: {tanque_vacio}%
    Tanque Mediano: {tanque_mediano}%
    Tanque Lleno: {tanque_lleno}% 
    """

# llamar los datos actualizados
print(generate_report(0, 80, 100))


