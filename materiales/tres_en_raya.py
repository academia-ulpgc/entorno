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
