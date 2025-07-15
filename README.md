# 🗂️ CRUD de Alumnos en Python + SQLite

Este proyecto es una aplicación de consola que permite realizar operaciones **CRUD** (Crear, Leer, Actualizar y Eliminar) sobre una base de datos de alumnos utilizando **Python** y **SQLite**.

## 📌 Funcionalidades

- Agregar nuevos alumnos.
- Listar todos los alumnos registrados.
- Modificar los datos de un alumno existente (por DNI).
- Eliminar un alumno (por DNI).
- Base de datos persistente con SQLite (`alumnos.db`).

## 🧰 Tecnologías utilizadas

- Python 3
- SQLite3 (base de datos local)
- `sqlite3` módulo nativo de Python

## 📁 Estructura del proyecto

```
📦 CRUD/
 ┣ 📄 main.py          # Archivo principal del programa
 ┣ 📄 alumnos.db       # Base de datos SQLite (se genera automáticamente)
```

## ▶️ Cómo usarlo

1. Cloná el repositorio:

```bash
git clone https://github.com/ezetaylor/CRUD.git
cd CRUD
```

2. Ejecutá el programa:

```bash
python main.py
```

3. Usá el menú interactivo para agregar, ver, modificar o eliminar alumnos.

> 💡 Si es la primera vez que lo ejecutás, el programa creará automáticamente la base de datos `alumnos.db` con la tabla correspondiente.

## 📝 Estructura de la tabla `Alumnos`

| Campo     | Tipo     | Descripción                     |
|-----------|----------|---------------------------------|
| nombre    | TEXT     | Nombre del alumno               |
| apellido  | TEXT     | Apellido del alumno             |
| edad      | INTEGER  | Edad del alumno                 |
| dni       | INTEGER  | DNI del alumno (clave primaria) |
| promedio  | REAL     | Promedio general                |

## 🧠 Autor

**Santiago Ezequiel Taylor**  
📧 [ezetaylor](https://github.com/ezetaylor)
