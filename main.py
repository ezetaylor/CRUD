import os
import sqlite3 as sql

def inicializar_db():
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Alumnos (
            nombre TEXT,
            apellido TEXT,
            edad INTEGER,
            dni INTEGER PRIMARY KEY,
            promedio REAL
        )"""
    )
    conn.commit()
    conn.close()

def guardar_alumno(alumno):
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor() 
    try:
        cursor.execute(
            """
            INSERT INTO Alumnos (nombre, apellido, edad, dni, promedio) VALUES (?, ?, ?, ?, ?)
        """, (alumno['nombre'], alumno['apellido'], alumno['edad'], alumno['DNI'], alumno['promedio'])
        )
        conn.commit()
    except sql.IntegrityError:
        print("Ya existe un alumno con ese DNI en la base de datos")
    finally:
        conn.close()

def cargar_alumnos_desde_db(db_path="alumnos.db"):
    alumnos = []
    try:
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT nombre, apellido, edad, DNI, promedio FROM alumnos")
        filas = cursor.fetchall()

        for fila in filas:
            alumno = {
                'nombre': fila[0],
                'apellido': fila[1],
                'edad': fila[2],
                'DNI': fila[3],
                'promedio': fila[4]
            }
            alumnos.append(alumno)

        conn.close()
    except sql.Error as e:
        print("❌ Error al cargar alumnos desde la base de datos:", e)

    return alumnos

def actualizar_sql(nombre, apellido, edad, nuevo_dni, promedio, dni_original, db_path="alumnos.db"):
    try:
        conn=sql.connect(db_path)
        cursor=conn.cursor()

        cursor.execute(
            """
            UPDATE Alumnos SET nombre=?, apellido=?, edad=?, DNI=?, promedio=?
            WHERE DNI = ?""",(nombre, apellido, edad, nuevo_dni, promedio, dni_original)
        )
        conn.commit()
        conn.close()
        return True
    except sql.Error as e:
        print("❌ Error al actualizar en la base de datos:", e)
        return False

def agregar_alumno(alumnos):
    nombre=input("Nombre de alumno: ")
    apellido=input("Apellido: ")

    try:
        edad=int(input("Edad: "))
        if edad<0:
            print("Edad invalida. Por favor ingrese una edad valida.")
            return
    except ValueError: 
        print("Edad invalida. Por favor ingrese una edad valida.")
        return

    try:
        dni = int(input("DNI: "))
        if any(alum['DNI'] == dni for alum in alumnos):
            print("⚠ Ya existe un alumno con ese DNI.")
            return
    except ValueError:
        print("⚠ DNI inválido. No se agregó el alumno.")
        return
    
    try:
        promedio=float(input("Promedio: "))
    except ValueError:
        print("Promedio ivalido.")
        return
    os.system('cls')
    
    alumno={
        "nombre":nombre,
        "apellido": apellido,
        "edad":edad,
        "DNI":dni,
        "promedio":promedio,
    }

    alumnos.append(alumno)
    guardar_alumno(alumno)

def mostrar_alumnos(alumnos):
    if not alumnos:
        os.system('cls')
        print("No se encuentran alumnos cargados.")
        return
    else:
        print("Lista de alumnos: \n")
        for alum in alumnos:
            print(f"Nombre: {alum['nombre']} - Apellido: {alum['apellido']} - Edad: {alum['edad']} - DNI: {alum['DNI']} - Promedio: {alum['promedio']}\n")

def modificar_alumno(alumnos):
    if not alumnos:
        os.system('cls')
        print("No se encuentran alumnos cargados.")
        return
    try:
        dni=int(input("Ingrese DNI del alumno a modificar: "))
    except ValueError:
        print("Error. Ingreso invalido.")
        return
    for alum in alumnos:
        if alum['DNI'] == dni:
            print(f"Alumno encontrado: {alum['nombre']}")
            nuevo_nombre = input("Ingrese el nuevo nombre (dejar vacío para no modificar): ").strip()
            nuevo_apellido = input("Ingrese el nuevo apellido (dejar vacío para no modificar): ").strip()
            nueva_edad = input("Ingrese la nueva edad (dejar vacío para no modificar): ").strip()
            nuevo_dni = input("Ingrese el nuevo DNI (dejar vacío para no modificar): ").strip()
            nuevo_promedio = input("Ingrese el nuevo promedio (dejar vacío para no modificar): ").strip()

            if nuevo_nombre:
                alum['nombre'] = nuevo_nombre
            if nuevo_apellido:
                alum['apellido'] = nuevo_apellido
            if nueva_edad.isdigit():
                alum['edad'] = int(nueva_edad)
            if nuevo_dni.isdigit():
                alum['DNI'] = int(nuevo_dni)
            if nuevo_promedio:
                alum['promedio']=float(nuevo_promedio)


            exito = actualizar_sql(
                alum['nombre'],
                alum['apellido'],
                alum['edad'],
                alum['DNI'],
                alum['promedio'],
                dni  # DNI original
            )

            if exito:
                print("✅ Alumno modificado con éxito.")
            return

    print("❌ No se encontró ningún alumno con ese DNI.")

def eliminar_alumno(alumnos):
    if not alumnos:
        os.system('cls')
        print("No se encuentran alumnos cargados.")
        return
    dni=int(input("Ingrese DNI del alumno a eliminar: "))
    for alum in alumnos:
        if alum['DNI'] == dni:
            alumnos.remove(alum)
        print("❌ Alumno eliminado con éxito.")
        return
    print("⚠ Alumno no encontrado.")

#PROGRAMA PRINCIPAL --------------------------------------------------------------------------------------------
inicializar_db()
alumnos=[]
alumnos = cargar_alumnos_desde_db()
eleccion=0
while eleccion != 5:
    print("1. Ingresar alumno")
    print("2. Mostrar alumnos")
    print("3. Modificar alumno")
    print("4. Eliminar alumno")
    print("5. Salir")

    try:
        eleccion=int(input("Elija su opcion: "))
        if eleccion < 1 or eleccion > 5:
            os.system('cls')
            print("Error. Elija una opcion correcta")
            continue
    except ValueError: 
        os.system('cls')
        print("Error. Elija una opcion correcta")
        continue


    if eleccion == 1:
        agregar_alumno(alumnos)
    elif eleccion == 2:
        mostrar_alumnos(alumnos)
    elif eleccion==3:
        modificar_alumno(alumnos)
    elif eleccion==4:
        eliminar_alumno(alumnos)
    else:
        break