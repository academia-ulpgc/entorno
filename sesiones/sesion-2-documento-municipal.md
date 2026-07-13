# Sesion 2 - Crear un documento municipal estructurado

## Duracion

1 hora y 15 minutos.

## Objetivo

Crear un documento LaTeX mas completo a partir de un caso municipal ficticio, usando secciones, listas y una tabla sencilla.

La sesion refuerza la idea de que el documento se construye desde un archivo fuente y se obtiene mediante compilacion.

## Practica paso a paso

### Paso 1. Crear el proyecto e2

Dentro de `curso-entorno`, crea una carpeta llamada:

```text
e2
```

Abrela en VS Code con:

```text
Archivo > Abrir carpeta...
```

### Paso 2. Crear el archivo del informe

En `e2`, crea:

```text
informe_servicios.tex
```

Pega:

```latex
\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish]{babel}
\usepackage{array}

\title{Informe de seguimiento de servicios municipales}
\author{Area de Coordinacion Municipal}
\date{\today}

\begin{document}

\maketitle

\section{Finalidad del informe}

Este documento ficticio resume el estado de varias actuaciones municipales. Se utiliza solo como ejercicio de formacion.

\section{Datos revisados}

La informacion procede de una relacion inventada de actuaciones. No contiene datos personales ni expedientes reales.

\begin{itemize}
    \item Reposicion de luminarias.
    \item Reparacion de aceras.
    \item Limpieza de espacios publicos.
\end{itemize}

\section{Estado de las actuaciones}

\begin{center}
\begin{tabular}{|p{4cm}|p{3cm}|p{5cm}|}
\hline
Actuacion & Estado & Comentario \\
\hline
Alumbrado publico & En revision & Se revisaran avisos repetidos en una misma zona. \\
\hline
Aceras y pavimento & Pendiente & Se priorizaran puntos con riesgo para peatones. \\
\hline
Limpieza viaria & Programada & Se coordinara con el calendario ordinario del servicio. \\
\hline
\end{tabular}
\end{center}

\section{Recomendacion}

Antes de enviar este informe, el area responsable debe comprobar que los datos son correctos y que las actuaciones estan validadas.

\end{document}
```

Guarda el archivo.

### Paso 3. Compilar con Play

Con `informe_servicios.tex` abierto, pulsa el icono de **Play**.

Comprueba que se genera:

```text
informe_servicios.pdf
```

Si aparecen archivos `.aux`, `.log` o similares, no los borres durante la practica. Son parte normal del proceso de compilacion.

### Paso 4. Revisar el PDF

Abre el PDF en la ventana principal de VS Code.

Comprueba:

- que el titulo aparece correctamente;
- que las secciones estan separadas;
- que la lista se lee bien;
- que la tabla cabe en la pagina;
- que el informe no contiene datos personales reales.

### Paso 5. Hacer una primera modificacion controlada

En el archivo `.tex`, cambia el titulo por:

```latex
\title{Informe municipal de seguimiento operativo}
```

Guarda y vuelve a compilar con el icono de **Play**.

Comprueba que el cambio aparece en el PDF.

### Paso 6. Añadir una nueva seccion

Antes de `\end{document}`, añade:

```latex
\section{Comprobaciones finales}

Antes de firmar o remitir el informe se comprobara:

\begin{itemize}
    \item que la informacion procede de fuentes autorizadas;
    \item que no hay datos personales innecesarios;
    \item que el area competente ha revisado las recomendaciones.
\end{itemize}
```

Guarda y compila otra vez.

### Paso 7. Pedir una explicacion a Codex

Copia el contenido de `informe_servicios.tex` y pregunta a Codex:

```text
Explicame este documento LaTeX para una persona que esta empezando.
Quiero entender para que sirven section, itemize, tabular, hline y p{4cm}.
No modifiques el archivo.
```

Despues pregunta:

```text
Detecta si hay alguna parte confusa en el informe.
No inventes datos nuevos.
Propón solo una mejora de redaccion y explica por que ayuda.
```

Aplica manualmente solo el cambio que entiendas.

## Producto de la sesion

- Carpeta `curso-entorno/e2`.
- Archivo `informe_servicios.tex`.
- PDF generado desde LaTeX.
- Una modificacion realizada y compilada.
- Checklist de la sesion 2 compilado por el estudiante a partir de `checklists/checklist-sesion-2.tex`.

## Glosario de terminos

- **Comando LaTeX**: instruccion que empieza normalmente con barra invertida, como `\section`.
- **Entorno LaTeX**: bloque con inicio y fin, como `\begin{itemize}` y `\end{itemize}`.
- **`section`**: comando LaTeX que crea un apartado.
- **`itemize`**: entorno LaTeX que crea una lista con viñetas.
- **`item`**: comando que crea un elemento dentro de una lista.
- **`tabular`**: entorno LaTeX que crea una tabla.
- **`hline`**: comando que dibuja una linea horizontal en una tabla.
- **`p{4cm}`**: configuracion que fija el ancho de una columna.
- **Compilacion**: proceso que transforma el archivo `.tex` en PDF.
- **Recompilar**: volver a generar el PDF despues de modificar el codigo fuente.
- **Archivo fuente**: archivo original que se edita, como `informe_servicios.tex`.
- **Archivo generado**: archivo creado por una herramienta, como `informe_servicios.pdf`.
