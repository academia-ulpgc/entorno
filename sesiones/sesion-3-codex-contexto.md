# Sesion 3 - Usar Codex con contexto en LaTeX

## Duracion

1 hora y 15 minutos.

## Objetivo

Aprender a pedir ayuda a Codex usando un documento LaTeX como contexto y comprobando que la IA no inventa datos.

En esta sesion todo el material de trabajo se mantiene en LaTeX. El contexto sera un archivo `.tex` y el borrador tambien sera un archivo `.tex`.

## Practica paso a paso

### Paso 1. Crear el proyecto e3

Dentro de `curso-entorno`, crea una carpeta llamada:

```text
e3
```

Abrela en VS Code.

### Paso 2. Crear el documento de contexto en LaTeX

En `e3`, crea:

```text
fuentes_municipales.tex
```

Pega:

```latex
\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish]{babel}

\title{Fuentes para informe municipal}
\author{Material ficticio de practica}
\date{\today}

\begin{document}

\maketitle

\section{Situacion de partida}

El ayuntamiento quiere preparar un informe interno sobre avisos ciudadanos relacionados con mantenimiento urbano.

\section{Ambitos incluidos}

\begin{itemize}
    \item Alumbrado publico.
    \item Aceras y pavimento.
    \item Limpieza viaria.
\end{itemize}

\section{Reglas de uso}

\begin{itemize}
    \item No usar datos personales reales.
    \item No inventar expedientes.
    \item No citar normativa si no se ha proporcionado.
    \item Marcar como pendiente de verificacion cualquier dato dudoso.
\end{itemize}

\section{Advertencia}

Este documento contiene informacion ficticia para practicar. No debe utilizarse como fuente real.

\end{document}
```

Guarda el archivo.

### Paso 3. Compilar el documento de contexto

Con `fuentes_municipales.tex` abierto, pulsa el icono de **Play**.

Comprueba que se genera:

```text
fuentes_municipales.pdf
```

Este PDF sirve para comprobar que el contexto tambien es un documento LaTeX valido.

### Paso 4. Crear el borrador LaTeX

En `e3`, crea:

```text
borrador_informe.tex
```

Pega:

```latex
\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish]{babel}

\title{Borrador de informe interno}
\author{Area de Atencion Ciudadana}
\date{\today}

\begin{document}

\maketitle

\section{Contexto}

Pendiente de redactar.

\section{Alcance}

Pendiente de redactar.

\section{Recomendaciones}

Pendiente de redactar.

\section{Comprobaciones}

Pendiente de redactar.

\end{document}
```

Guarda el archivo.

### Paso 5. Hacer una pregunta demasiado vaga

Copia el contenido de `borrador_informe.tex` y pregunta a Codex:

```text
Completa este informe.
```

Lee la respuesta, pero no la pegues en el documento.

Comprueba si Codex ha inventado datos, expedientes, fechas, normativa o actuaciones que no estaban en `fuentes_municipales.tex`.

### Paso 6. Hacer una pregunta con contexto y limites

Pregunta ahora:

```text
Usa el archivo fuentes_municipales.tex como unica fuente de informacion.

Rellena las secciones del borrador LaTeX con texto breve y claro.

Condiciones:
- no inventes expedientes, fechas, importes ni normativa;
- no cites leyes si no aparecen en fuentes_municipales.tex;
- si falta informacion, escribe "pendiente de verificacion";
- manten el formato LaTeX;
- no cambies el titulo ni el autor.

Primero explica que vas a cambiar.
Despues muestra el texto propuesto.
```

Revisa la respuesta antes de copiar nada.

### Paso 7. Copiar solo lo que se entienda

Sustituye manualmente los textos `Pendiente de redactar.` por el contenido que consideres correcto.

No copies frases que:

- incluyan datos no presentes en `fuentes_municipales.tex`;
- parezcan demasiado concretas sin fuente;
- citen normas no proporcionadas;
- prometan actuaciones no validadas.

### Paso 8. Compilar el borrador con Play

Pulsa el icono de **Play**.

Comprueba que se genera:

```text
borrador_informe.pdf
```

Si aparece un error, pregunta a Codex:

```text
Tengo este error al compilar LaTeX.
Explicamelo en lenguaje sencillo y dime que linea debo revisar.
No reescribas todo el documento.
```

### Paso 9. Revisar el resultado

Abre el PDF en la ventana principal de VS Code.

Comprueba:

- que el texto procede del documento de contexto;
- que no aparecen datos inventados;
- que las dudas quedan marcadas como pendientes de verificacion;
- que no hay datos personales reales.

## Producto de la sesion

- Carpeta `curso-entorno/e3`.
- Archivo `fuentes_municipales.tex`.
- PDF `fuentes_municipales.pdf`.
- Archivo `borrador_informe.tex`.
- PDF `borrador_informe.pdf`.
- Comparacion entre una pregunta vaga y una pregunta con contexto.
- Checklist de la sesion 3 compilado por el estudiante a partir de `checklists/checklist-sesion-3.tex`.

## Glosario de terminos

- **IA generativa**: sistema capaz de producir texto, codigo u otros contenidos a partir de instrucciones.
- **Codex**: asistente de IA que ayuda a entender y modificar documentos o codigo.
- **Prompt**: instruccion o pregunta escrita a una IA.
- **Contexto**: informacion que se entrega a la IA para limitar y orientar la respuesta.
- **Fragmento copiado**: parte del archivo que se pega en Codex para pedir ayuda.
- **Alucinacion**: respuesta generada por una IA que contiene informacion inventada o no justificada.
- **Formato LaTeX**: estructura tecnica del documento, con comandos como `\section` o `\begin`.
- **Error de compilacion**: problema que impide generar el PDF.
- **Linea de error**: numero o zona del archivo donde LaTeX indica que puede estar el problema.
- **Salida**: resultado que produce una herramienta, como una respuesta de Codex o un PDF.
