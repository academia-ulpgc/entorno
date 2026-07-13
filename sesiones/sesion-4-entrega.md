# Sesion 4 - Usar Python para rellenar una plantilla LaTeX

## Duracion

1 hora y 15 minutos.

## Objetivo

Usar Python por primera vez en el bloque para generar varios documentos LaTeX a partir de una plantilla `.tex` y un archivo de datos `.tsv`.

Hasta ahora se han escrito documentos LaTeX a mano. En esta sesion se introduce una idea nueva: separar el documento en dos partes.

- La carpeta **plantillas** contiene el formato y los huecos.
- La carpeta **datos** contiene el archivo TSV.
- La carpeta **resultados** contiene los documentos generados.
- El **programa Python** abre la plantilla, lee los datos y sustituye cada hueco por el valor correspondiente.

Esta forma de trabajar es muy habitual en automatizacion documental.

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
  plantillas/
  datos/
  resultados/
```

La carpeta `resultados` tambien puede crearla Python automaticamente, pero conviene verla desde el principio para entender la organizacion del proyecto.

### Paso 2. Entender que hacen falta dos piezas

Para trabajar con Python en VS Code hacen falta dos cosas distintas:

- **Python instalado en el ordenador**: es el programa que ejecuta las instrucciones.
- **Extension Python en VS Code**: es el complemento que ayuda a VS Code a entender archivos `.py`.

La extension de VS Code no sustituye al programa Python. Puede ayudar a detectarlo, seleccionarlo y ejecutar archivos, pero Python debe estar instalado en el equipo.

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

### Paso 4. Comprobar que Python esta disponible

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

En algunos equipos, VS Code puede mostrar un aviso para instalar o seleccionar Python. Puedes seguir ese aviso si pertenece a VS Code y tienes permiso para instalar programas.

Si has instalado Python y la terminal sigue sin reconocerlo, cierra la terminal integrada y abre una nueva. Si sigue fallando, reinicia VS Code.

### Paso 5. Pedir ayuda a Codex si Python no aparece

Si Python no aparece, no copies comandos al azar.

Abre Codex y pregunta:

```text
Estoy preparando VS Code para ejecutar un script Python sencillo.
Mi sistema operativo es: [Windows / macOS / Linux].
Al escribir python3 --version o python --version no aparece una version de Python.

Explicame paso a paso como comprobar si Python esta instalado.
Si no lo esta, dime la forma mas segura de instalarlo.
No des por hecho que tengo permisos de administrador.
No ejecutes nada por mi.
Antes de proponer comandos, explicame que hace cada paso.
```

Codex puede ayudarte a entender el problema y proponer pasos, pero la instalacion debe hacerla la persona, revisando cada accion.

### Paso 6. Crear la plantilla LaTeX

Dentro de `plantillas`, crea:

```text
plantillas/plantilla_informe.tex
```

Pega:

```latex
\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish]{babel}

\title{Informe municipal de incidencia}
\author{Area de Atencion Ciudadana}
\date{\today}

\begin{document}

\maketitle

\section{Datos de la incidencia}

\begin{itemize}
    \item Expediente: {{expediente}}
    \item Area responsable: {{area}}
    \item Tipo de incidencia: {{tipo}}
    \item Estado: {{estado}}
    \item Avisos registrados: {{cantidad}}
\end{itemize}

\section{Resumen}

{{resumen}}

\section{Recomendacion}

{{recomendacion}}

\section{Comprobaciones}

\begin{itemize}
    \item Los datos usados en esta practica son ficticios.
    \item El documento debe revisarse antes de usarse en un caso real.
    \item No se han incluido datos personales.
\end{itemize}

\end{document}
```

Guarda el archivo.

Fijate en los textos entre dobles llaves:

```text
{{expediente}}
{{area}}
{{tipo}}
{{estado}}
{{cantidad}}
{{resumen}}
{{recomendacion}}
```

Esos textos son **marcadores**. Python los reemplazara por datos.

### Paso 7. Crear el archivo TSV

Dentro de `datos`, crea:

```text
datos/datos_incidencias.tsv
```

Pega exactamente:

```tsv
expediente	area	tipo	estado	cantidad	resumen	recomendacion
EXP-2026-001	Alumbrado publico	Avisos revisados	En revision	8	Se han recibido avisos ficticios relacionados con puntos de alumbrado en varias calles.	Revisar la concentracion de avisos y priorizar las zonas con mayor repeticion.
EXP-2026-002	Aceras y pavimento	Avisos prioritarios	Pendiente	5	Se han registrado avisos ficticios sobre desperfectos en aceras y pavimento.	Priorizar los puntos que puedan afectar a la accesibilidad peatonal.
EXP-2026-003	Limpieza viaria	Avisos programados	Programado	6	Se han agrupado avisos ficticios sobre limpieza en espacios publicos.	Coordinar la actuacion con el calendario ordinario del servicio.
```

Un archivo TSV es parecido a una hoja de calculo guardada como texto.

La primera linea contiene los nombres de las columnas:

```text
expediente, area, tipo, estado, cantidad, resumen, recomendacion
```

Cada fila posterior contiene los datos de un documento.

### Paso 8. Crear el programa Python

En `e4`, crea:

```text
generar_informes.py
```

Pega:

```python
import csv
from pathlib import Path

carpeta_plantillas = Path("plantillas")
carpeta_datos = Path("datos")
carpeta_resultados = Path("resultados")

archivo_plantilla = carpeta_plantillas / "plantilla_informe.tex"
archivo_datos = carpeta_datos / "datos_incidencias.tsv"

carpeta_resultados.mkdir(exist_ok=True)

with open(archivo_plantilla, encoding="utf-8") as archivo:
    plantilla = archivo.read()

with open(archivo_datos, newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo, delimiter="\t")

    for numero, fila in enumerate(lector, start=1):
        documento = plantilla

        for columna, valor in fila.items():
            marcador = "{{" + columna + "}}"
            documento = documento.replace(marcador, valor)

        archivo_salida = carpeta_resultados / f"informe_{numero:02d}.tex"

        with open(archivo_salida, "w", encoding="utf-8") as salida:
            salida.write(documento)

        print(f"Archivo generado: {archivo_salida}")
```

Guarda el archivo.

### Paso 9. Ejecutar Python

En la terminal integrada, ejecuta:

```text
python3 generar_informes.py
```

Si tu equipo usa `python`, ejecuta:

```text
python generar_informes.py
```

Comprueba que aparecen estos mensajes:

```text
Archivo generado: resultados/informe_01.tex
Archivo generado: resultados/informe_02.tex
Archivo generado: resultados/informe_03.tex
```

Los archivos se guardan dentro de:

```text
resultados/
```

### Paso 10. Abrir un LaTeX generado

Abre:

```text
resultados/informe_01.tex
```

Comprueba:

- que ya no aparecen marcadores como `{{area}}`;
- que los datos coinciden con la primera fila del TSV;
- que el formato general procede de `plantillas/plantilla_informe.tex`;
- que no hay datos personales reales.

### Paso 11. Compilar con Play

Con `resultados/informe_01.tex` abierto, pulsa el icono de **Play**.

Comprueba que se genera:

```text
resultados/informe_01.pdf
```

Si aparecen archivos `.aux`, `.log`, `.synctex.gz`, `.fls` o `.fdb_latexmk`, recuerda que son archivos auxiliares normales de LaTeX.

### Paso 12. Probar un cambio en los datos

Abre `datos/datos_incidencias.tsv`.

Cambia la cantidad de la primera fila:

```text
8
```

por:

```text
9
```

Guarda el TSV.

Vuelve a ejecutar:

```text
python3 generar_informes.py
```

Abre otra vez `resultados/informe_01.tex` y comprueba que el dato ha cambiado.

Despues compila de nuevo con el icono de **Play**.

### Paso 13. Pedir ayuda a Codex sobre el programa

Copia el programa `generar_informes.py` y pregunta a Codex:

```text
Explicame este programa Python para una persona que no sabe programar.
Quiero entender como abre la plantilla LaTeX, como lee el TSV y como reemplaza los marcadores.
No cambies el codigo.
```

Despues pregunta:

```text
Propón una unica mejora pequeña para que el programa sea mas claro.
No inventes datos nuevos.
Explica primero la mejora y despues muestra el cambio.
```

Aplica manualmente solo lo que entiendas.

### Paso 14. Preparar la entrega

Dentro de `e4`, crea una carpeta llamada:

```text
entrega
```

Copia dentro de `entrega`:

```text
plantillas/plantilla_informe.tex
datos/datos_incidencias.tsv
generar_informes.py
resultados/informe_01.tex
resultados/informe_01.pdf
```

Puedes mantener la misma organizacion dentro de `entrega`:

```text
entrega/
  plantillas/
  datos/
  resultados/
  generar_informes.py
```

No es necesario copiar todos los archivos auxiliares. Pueden volver a generarse compilando el `.tex`.

## Producto de la sesion

- Carpeta `curso-entorno/e4`.
- Carpeta `plantillas`.
- Plantilla `plantillas/plantilla_informe.tex`.
- Carpeta `datos`.
- Archivo de datos `datos/datos_incidencias.tsv`.
- Programa `generar_informes.py`.
- Carpeta `resultados`.
- Archivos generados `resultados/informe_01.tex`, `resultados/informe_02.tex` e `resultados/informe_03.tex`.
- PDF `resultados/informe_01.pdf`.
- Carpeta `entrega`.
- Checklist de la sesion 4 compilado por el estudiante a partir de `checklists/checklist-sesion-4.tex`.

## Glosario de terminos

- **Python**: lenguaje que puede ejecutar instrucciones y automatizar tareas.
- **Interprete de Python**: programa instalado en el ordenador que ejecuta archivos `.py`.
- **Extension Python**: complemento de VS Code que ayuda a editar, ejecutar y depurar archivos Python.
- **Script**: archivo de codigo que ejecuta una tarea concreta.
- **Plantilla**: archivo con una estructura fija y huecos que se rellenan despues.
- **Marcador**: texto temporal que sera reemplazado, como `{{area}}`.
- **TSV**: archivo de datos en texto, organizado por columnas separadas por tabuladores.
- **Columna**: campo de datos identificado por un nombre, como `area` o `estado`.
- **Fila**: conjunto de valores que pertenecen a un mismo registro.
- **`csv.DictReader`**: herramienta de Python que lee un archivo de datos y trata cada fila como campos con nombre.
- **Variable**: nombre que guarda un valor dentro de un programa.
- **Bucle**: instruccion que repite una accion varias veces.
- **Ruta**: ubicacion de un archivo o carpeta, como `plantillas/plantilla_informe.tex`.
- **Archivo de entrada**: archivo que lee un programa, como `datos/datos_incidencias.tsv`.
- **Archivo de salida**: archivo creado por un programa, como `resultados/informe_01.tex`.
- **Ejecutar**: poner en marcha un programa.
- **Terminal integrada**: zona de VS Code donde se escriben comandos.
- **Comando**: instruccion escrita en la terminal, como `python3 generar_informes.py`.
