# Sesion 4 - Preparar Python en VS Code y ejecutar un programa

## Duracion

1 hora y 15 minutos.

## Objetivo

Dejar preparado VS Code para ejecutar Python y comprobarlo con un programa sencillo ya hecho.

En esta sesion no se programa desde cero. La idea es aprender el circuito basico:

- crear una carpeta de proyecto;
- crear o abrir un archivo `.py`;
- ejecutar el archivo desde VS Code con el boton **Run Python File**;
- observar el resultado;
- pedir a Codex que explique el codigo con palabras sencillas.

El ejemplo sera un pequeno juego de **tres en raya**. El objetivo no es dominar Python, sino perderle el miedo al entorno.

## Practica paso a paso

### Paso 1. Crear el proyecto e4

Dentro de `curso-entorno`, crea una carpeta llamada:

```text
e4
```

Abrela en VS Code.

Dentro de `e4`, crea esta estructura:

```text
e4/
  juegos/
```

Esta carpeta guardara el programa Python de la practica.

### Paso 2. Entender que hacen falta dos piezas

Para trabajar con Python en VS Code hacen falta dos cosas distintas:

- **Python instalado en el ordenador**: es el programa que ejecuta archivos `.py`.
- **Extension Python en VS Code**: es el complemento que ayuda a VS Code a reconocer y ejecutar Python.

La extension de VS Code no sustituye al programa Python. Puede ayudar a detectarlo y ejecutarlo, pero Python debe estar instalado en el equipo.

### Paso 3. Instalar la extension Python en VS Code

Abre la vista de extensiones de VS Code.

Busca:

```text
Python
```

Comprueba:

- Nombre exacto: Python
- Creador oficial: Microsoft
- Identificador unico: `ms-python.python`
- Funcion: permite trabajar mejor con archivos Python dentro de VS Code.

Pulsa **Instalar**.

### Paso 4. Comprobar Python desde VS Code

En `e4`, crea un archivo llamado:

```text
probar_python.py
```

Pega:

```python
print("Python funciona en VS Code")
```

Guarda el archivo.

Con `probar_python.py` abierto, pulsa el boton **Run Python File**.

El boton suele aparecer en la parte superior derecha del editor, con forma de triangulo de Play.

Comprueba que VS Code muestra el mensaje:

```text
Python funciona en VS Code
```

Si VS Code abre un panel inferior para mostrar el resultado, solo miralo: no hace falta escribir nada ahi.

Si VS Code pide seleccionar un interprete de Python, elige una opcion que diga Python 3.

Si VS Code indica que no encuentra Python, puede mostrar un boton o aviso para instalarlo o seleccionarlo. Sigue solo instrucciones que pertenezcan a VS Code y que entiendas.

### Paso 5. Pedir ayuda a Codex si Python no aparece

Si Python no aparece, no copies instrucciones al azar.

Abre Codex y pregunta:

```text
Estoy preparando VS Code para ejecutar un archivo Python sencillo.
Mi sistema operativo es: [Windows / macOS / Linux].

He instalado la extension Python de Microsoft en VS Code.
He creado un archivo probar_python.py con este contenido:

print("Python funciona en VS Code")

Al pulsar Run Python File, VS Code no encuentra Python o me pide seleccionar un interprete.

Dame instrucciones paso a paso usando la interfaz de VS Code, sin pedirme que escriba nada fuera del editor.
Si hay que instalar Python, explicame la forma mas segura de hacerlo.
No des por hecho que tengo permisos de administrador.
Antes de cada paso, explica que voy a comprobar.
```

Codex puede ayudarte a entender el problema y proponer pasos, pero la instalacion debe hacerla la persona, revisando cada accion.

### Paso 6. Crear el programa del juego

Dentro de `juegos`, crea un archivo llamado:

```text
juegos/tres_en_raya.py
```

Pega este codigo completo:

```python
import tkinter as tk
from tkinter import messagebox

turno = "X"
tablero = [""] * 9
botones = []

combinaciones_ganadoras = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def hay_ganador():
    for a, b, c in combinaciones_ganadoras:
        if tablero[a] and tablero[a] == tablero[b] == tablero[c]:
            return tablero[a]
    return ""


def tablero_lleno():
    return all(casilla != "" for casilla in tablero)


def jugar(posicion):
    global turno

    if tablero[posicion] != "":
        return

    tablero[posicion] = turno
    botones[posicion]["text"] = turno

    ganador = hay_ganador()

    if ganador:
        etiqueta_estado["text"] = f"Ha ganado {ganador}"
        messagebox.showinfo("Tres en raya", f"Ha ganado {ganador}")
        bloquear_tablero()
        return

    if tablero_lleno():
        etiqueta_estado["text"] = "Empate"
        messagebox.showinfo("Tres en raya", "La partida ha terminado en empate")
        return

    turno = "O" if turno == "X" else "X"
    etiqueta_estado["text"] = f"Turno de {turno}"


def bloquear_tablero():
    for boton in botones:
        boton["state"] = "disabled"


def nueva_partida():
    global turno, tablero

    turno = "X"
    tablero = [""] * 9
    etiqueta_estado["text"] = "Turno de X"

    for boton in botones:
        boton["text"] = ""
        boton["state"] = "normal"


ventana = tk.Tk()
ventana.title("Tres en raya")
ventana.geometry("360x430+200+120")
ventana.resizable(False, False)

etiqueta_estado = tk.Label(
    ventana,
    text="Turno de X",
    font=("Arial", 16),
    padx=10,
    pady=10,
)
etiqueta_estado.grid(row=0, column=0, columnspan=3)

for posicion in range(9):
    boton = tk.Button(
        ventana,
        text="",
        width=6,
        height=3,
        font=("Arial", 24),
        command=lambda p=posicion: jugar(p),
    )
    boton.grid(row=1 + posicion // 3, column=posicion % 3, padx=4, pady=4)
    botones.append(boton)

boton_nueva = tk.Button(
    ventana,
    text="Nueva partida",
    font=("Arial", 14),
    command=nueva_partida,
)
boton_nueva.grid(row=4, column=0, columnspan=3, sticky="ew", padx=4, pady=8)

print("Juego iniciado. Si no ves la ventana, mira detras de VS Code o en el Dock/barra de tareas.")

ventana.update_idletasks()
ventana.lift()
ventana.attributes("-topmost", True)
ventana.after(500, lambda: ventana.attributes("-topmost", False))

ventana.mainloop()
```

Guarda el archivo.

### Paso 7. Ejecutar el juego

Abre:

```text
juegos/tres_en_raya.py
```

Pulsa el boton **Run Python File**.

Debe abrirse una ventana con un tablero de tres en raya.

Si no ves la ventana:

- mira si esta detras de VS Code;
- mira el Dock o la barra de tareas;
- revisa el panel inferior de VS Code y busca el mensaje `Juego iniciado`;
- si aparece un mensaje de error, copialo y pegalo en Codex.

Juega una partida pulsando en las casillas.

Comprueba:

- que el turno cambia entre `X` y `O`;
- que el programa detecta cuando alguien gana;
- que el boton **Nueva partida** reinicia el tablero.

### Paso 8. Pedir a Codex que explique el programa

Copia el codigo de `juegos/tres_en_raya.py` y pregunta a Codex:

```text
Explicame este programa Python para una persona que no sabe programar.
No quiero una explicacion tecnica larga.

Quiero entender:
- que parte crea la ventana;
- que parte crea los botones;
- que parte comprueba si alguien gana;
- que ocurre cuando pulso una casilla.

No cambies el codigo.
```

Lee la respuesta y vuelve al archivo para localizar esas partes.

### Paso 9. Hacer un cambio pequeno

Haz solo un cambio sencillo en el codigo.

Por ejemplo, cambia el titulo de la ventana:

```python
ventana.title("Tres en raya")
```

por:

```python
ventana.title("Mi primer juego en Python")
```

Guarda el archivo y pulsa otra vez **Run Python File**.

Comprueba que la ventana se abre con el nuevo titulo.

### Paso 10. Pedir una mejora pequena a Codex

Pregunta a Codex:

```text
Tengo este programa Python de tres en raya.
Propón una unica mejora pequena y facil de entender.
No cambies la estructura completa.
Explica primero que hace la mejora.
Despues muestra solo las lineas que tendria que cambiar.
```

Aplica manualmente solo una mejora que entiendas.

Si Codex propone demasiados cambios, responde:

```text
Reduce la propuesta.
Quiero un unico cambio pequeno, adecuado para una persona que esta empezando.
```

### Paso 11. Preparar la entrega

Dentro de `e4`, crea una carpeta llamada:

```text
entrega
```

Copia dentro de `entrega`:

```text
probar_python.py
juegos/tres_en_raya.py
```

No hace falta entregar capturas salvo que se pidan expresamente.

## Producto de la sesion

- Carpeta `curso-entorno/e4`.
- Archivo `probar_python.py`.
- Carpeta `juegos`.
- Programa `juegos/tres_en_raya.py`.
- Juego ejecutado desde VS Code con **Run Python File**.
- Una pequena modificacion realizada y comprobada.
- Carpeta `entrega`.
- Checklist de la sesion 4 compilado por el estudiante a partir de `checklists/checklist-sesion-4.tex`.

## Glosario de terminos

- **Python**: lenguaje que puede ejecutar instrucciones y automatizar tareas.
- **Interprete de Python**: programa instalado en el ordenador que ejecuta archivos `.py`.
- **Extension Python**: complemento de VS Code que ayuda a editar y ejecutar archivos Python.
- **Archivo `.py`**: archivo que contiene codigo Python.
- **Run Python File**: boton de VS Code que ejecuta el archivo Python abierto.
- **Panel de salida**: zona inferior donde VS Code puede mostrar mensajes del programa.
- **Interfaz grafica**: ventana con botones y elementos visuales.
- **Tkinter**: herramienta incluida en Python para crear ventanas sencillas.
- **Funcion**: bloque de codigo que realiza una tarea concreta.
- **Variable**: nombre que guarda un valor dentro de un programa.
- **Condicion**: pregunta que el programa usa para decidir que hacer.
- **Evento**: accion del usuario que el programa recibe, por ejemplo pulsar un boton.
- **Ejecutar**: poner en marcha un programa.
