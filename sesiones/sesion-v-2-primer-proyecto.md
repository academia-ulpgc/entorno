# Sesion V.2 - Primer proyecto con LaTeX, Markdown y Python

## Duracion

1 hora y 15 minutos.

## Objetivo

Crear un primer proyecto completo en VS Code con varios archivos: un `README.md`, un documento LaTeX, un script Python y un archivo de resultados.

## Practica paso a paso

### Paso 1. Crear la carpeta del proyecto

En tu carpeta de trabajo, crea:

```text
practica-v2
```

Dentro, crea:

```text
README.md
informe.tex
analisis.py
resultados.txt
```

### Paso 2. Escribir `README.md`

Pega:

```markdown
# Practica V.2

## Objetivo

Comprobar que puedo trabajar en VS Code con documentos LaTeX y scripts Python.

## Archivos

- `informe.tex`: documento LaTeX de prueba.
- `analisis.py`: script Python con calculos sencillos.
- `resultados.txt`: salida obtenida al ejecutar Python.

## Comprobaciones

- [ ] El documento LaTeX compila.
- [ ] El script Python se ejecuta.
- [ ] He revisado los resultados antes de entregarlos.
```

Abre la vista previa con:

```text
Markdown: Open Preview to the Side
```

### Paso 3. Crear `informe.tex`

Pega:

```latex
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage{hyperref}

\title{Informe de prueba con VS Code}
\author{Nombre del participante}
\date{\today}

\begin{document}

\maketitle

\section{Introduccion}
Este documento muestra como generar un PDF con LaTeX desde VS Code.

\section{Entorno de trabajo}

Durante la practica se han usado:

\begin{itemize}
    \item Visual Studio Code.
    \item LaTeX Workshop.
    \item Python.
    \item GitHub Copilot Chat como apoyo.
\end{itemize}

\section{Resultados}
La compilacion produce un archivo PDF visible en el visor integrado de VS Code.

\section{Conclusion}
La carpeta del proyecto permite reunir documentos, codigo y resultados en un unico lugar.

\end{document}
```

Compila con LaTeX Workshop.

### Paso 4. Crear `analisis.py`

Pega:

```python
nombre = "Participante"
print(f"Hola, {nombre}! Esto es una prueba de Python.")

valores = [10, 20, 30, 40, 50]
media = sum(valores) / len(valores)
maximo = max(valores)
minimo = min(valores)

print(f"Valores: {valores}")
print(f"Media de los valores: {media}")
print(f"Valor minimo: {minimo}")
print(f"Valor maximo: {maximo}")
```

Ejecuta el archivo.

### Paso 5. Guardar resultados

Copia la salida del terminal en `resultados.txt`.

Añade al principio:

```text
Resultados de la sesion V.2
Fecha:
```

### Paso 6. Pedir ayuda a Copilot

Abre `analisis.py` y pregunta:

```text
Explica este script Python para una persona que no sabe programar.
No cambies el archivo. Usa frases breves.
```

Revisa que la respuesta coincide con el codigo.

## Checklist final

- [ ] La carpeta `practica-v2` esta ordenada.
  - Observaciones:

- [ ] `README.md` se ve correctamente en vista previa.
  - Observaciones:

- [ ] `informe.tex` compila a PDF.
  - Observaciones:

- [ ] `analisis.py` se ejecuta.
  - Observaciones:

- [ ] `resultados.txt` contiene la salida del script.
  - Observaciones:

- [ ] He revisado la respuesta de Copilot antes de usarla.
  - Observaciones:

## Producto de la sesion

- Carpeta `practica-v2`.
- `README.md`.
- `informe.tex` y PDF generado.
- `analisis.py`.
- `resultados.txt`.
- Checklist final completada.
