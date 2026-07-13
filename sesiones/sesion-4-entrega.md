# Sesion 4 - Primer uso de Python para generar un documento LaTeX

## Duracion

1 hora y 15 minutos.

## Objetivo

Usar Python por primera vez en el bloque para generar automaticamente un archivo LaTeX sencillo y despues compilarlo a PDF con el icono de Play.

Hasta ahora se han escrito documentos LaTeX a mano. En esta sesion se introduce una idea nueva: una herramienta puede crear parte del archivo fuente por nosotros. Python no sustituye la revision humana; solo ayuda a repetir una tarea de forma ordenada.

## Practica paso a paso

### Paso 1. Crear el proyecto e4

Dentro de `curso-entorno`, crea una carpeta llamada:

```text
e4
```

Abrela en VS Code.

### Paso 2. Comprobar que Python esta disponible

Abre una terminal integrada en VS Code.

Escribe:

```text
python3 --version
```

Si en tu equipo se usa `python` en lugar de `python3`, escribe:

```text
python --version
```

Si no aparece una version de Python, anota la incidencia y sigue la explicacion del profesor.

### Paso 3. Crear el archivo de datos

En `e4`, crea:

```text
datos_incidencias.csv
```

Pega:

```csv
area,tipo,estado,cantidad
Alumbrado publico,Avisos revisados,En revision,8
Aceras y pavimento,Avisos prioritarios,Pendiente,5
Limpieza viaria,Avisos programados,Programado,6
```

Estos datos son ficticios. No uses datos personales ni expedientes reales.

### Paso 4. Crear el programa Python

En `e4`, crea:

```text
generar_informe.py
```

Pega:

```python
import csv

archivo_datos = "datos_incidencias.csv"
archivo_salida = "informe_generado.tex"

filas = []

with open(archivo_datos, newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        filas.append(fila)

lineas = []
lineas.append(r"\documentclass[a4paper,12pt]{article}")
lineas.append(r"\usepackage[utf8]{inputenc}")
lineas.append(r"\usepackage[T1]{fontenc}")
lineas.append(r"\usepackage[spanish]{babel}")
lineas.append(r"\usepackage{array}")
lineas.append("")
lineas.append(r"\title{Informe generado de incidencias municipales}")
lineas.append(r"\author{Area de Atencion Ciudadana}")
lineas.append(r"\date{\today}")
lineas.append("")
lineas.append(r"\begin{document}")
lineas.append("")
lineas.append(r"\maketitle")
lineas.append("")
lineas.append(r"\section{Objetivo}")
lineas.append("")
lineas.append("Este informe se ha generado automaticamente a partir de datos ficticios.")
lineas.append("")
lineas.append(r"\section{Resumen}")
lineas.append("")
lineas.append(r"\begin{center}")
lineas.append(r"\begin{tabular}{|p{4cm}|p{4cm}|p{3cm}|p{2cm}|}")
lineas.append(r"\hline")
lineas.append(r"Area & Tipo & Estado & Cantidad \\")
lineas.append(r"\hline")

for fila in filas:
    lineas.append(
        f"{fila['area']} & {fila['tipo']} & {fila['estado']} & {fila['cantidad']} \\\\"
    )
    lineas.append(r"\hline")

lineas.append(r"\end{tabular}")
lineas.append(r"\end{center}")
lineas.append("")
lineas.append(r"\section{Comprobaciones}")
lineas.append("")
lineas.append(r"\begin{itemize}")
lineas.append(r"    \item Los datos son ficticios.")
lineas.append(r"    \item El informe debe revisarse antes de usarse.")
lineas.append(r"    \item No se han incluido datos personales.")
lineas.append(r"\end{itemize}")
lineas.append("")
lineas.append(r"\end{document}")

with open(archivo_salida, "w", encoding="utf-8") as archivo:
    archivo.write("\n".join(lineas))

print(f"Archivo generado: {archivo_salida}")
```

Guarda el archivo.

### Paso 5. Ejecutar Python

En la terminal integrada, ejecuta:

```text
python3 generar_informe.py
```

Si tu equipo usa `python`, ejecuta:

```text
python generar_informe.py
```

Comprueba que aparece:

```text
Archivo generado: informe_generado.tex
```

### Paso 6. Abrir el LaTeX generado

Abre:

```text
informe_generado.tex
```

Este archivo ha sido creado por Python. Aun asi, debes revisarlo como cualquier otro documento.

Comprueba:

- que tiene titulo;
- que contiene una tabla;
- que los datos coinciden con `datos_incidencias.csv`;
- que no hay datos personales reales.

### Paso 7. Compilar con Play

Con `informe_generado.tex` abierto, pulsa el icono de **Play**.

Comprueba que se genera:

```text
informe_generado.pdf
```

Si aparecen archivos `.aux`, `.log`, `.synctex.gz`, `.fls` o `.fdb_latexmk`, recuerda que son archivos auxiliares normales de LaTeX.

### Paso 8. Pedir ayuda a Codex

Copia el programa `generar_informe.py` y pregunta a Codex:

```text
Explicame este programa Python para una persona que no sabe programar.
Quiero entender que hace csv.DictReader, la lista lineas y el archivo informe_generado.tex.
No cambies el codigo.
```

Despues pregunta:

```text
Propón una unica mejora pequeña para que el informe generado sea mas claro.
No inventes datos nuevos.
Explica primero la mejora y despues muestra el cambio.
```

Aplica manualmente solo lo que entiendas.

### Paso 9. Preparar la entrega

Dentro de `e4`, crea una carpeta llamada:

```text
entrega
```

Copia dentro de `entrega`:

```text
datos_incidencias.csv
generar_informe.py
informe_generado.tex
informe_generado.pdf
```

No es necesario copiar todos los archivos auxiliares. Pueden volver a generarse compilando el `.tex`.

## Producto de la sesion

- Carpeta `curso-entorno/e4`.
- Archivo `datos_incidencias.csv`.
- Programa `generar_informe.py`.
- Archivo `informe_generado.tex`.
- PDF `informe_generado.pdf`.
- Carpeta `entrega`.
- Checklist de la sesion 4 compilado por el estudiante a partir de `checklists/checklist-sesion-4.tex`.

## Glosario de terminos

- **Python**: lenguaje que puede ejecutar instrucciones y automatizar tareas.
- **Script**: archivo de codigo que ejecuta una tarea concreta.
- **CSV**: archivo de datos en texto, organizado por columnas separadas por comas.
- **`csv.DictReader`**: herramienta de Python que lee un CSV y trata cada fila como un conjunto de campos con nombre.
- **Variable**: nombre que guarda un valor dentro de un programa.
- **Lista**: estructura de Python que guarda varios elementos ordenados.
- **Bucle**: instruccion que repite una accion varias veces.
- **Archivo de entrada**: archivo que lee un programa, como `datos_incidencias.csv`.
- **Archivo de salida**: archivo creado por un programa, como `informe_generado.tex`.
- **`informe_generado.tex`**: documento LaTeX creado por Python.
- **Ejecutar**: poner en marcha un programa.
- **Terminal integrada**: zona de VS Code donde se escriben comandos.
- **Comando**: instruccion escrita en la terminal, como `python3 generar_informe.py`.
