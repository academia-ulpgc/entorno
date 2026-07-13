# Sesion 3 - Usar Codex con un LaTeX de contexto legal

## Duracion

1 hora y 15 minutos.

## Objetivo

Aprender a pedir ayuda a Codex usando un archivo LaTeX de contexto normativo y comprobando que la IA no inventa legislacion, jurisprudencia, plazos ni conclusiones.

En esta sesion se trabajara con un extracto formativo de la **Ley 39/2015, de Procedimiento Administrativo Comun de las Administraciones Publicas**.

La idea principal es:

- dar a Codex un texto de contexto en LaTeX;
- pedirle que trabaje solo con ese texto;
- exigir que marque lo dudoso como pendiente de verificacion;
- pasar el resultado revisado a otro documento LaTeX.

## Practica paso a paso

### Paso 1. Crear el proyecto e3

Dentro de `curso-entorno`, crea una carpeta llamada:

```text
e3
```

Abrela en VS Code.

Dentro de `e3`, crea esta estructura:

```text
e3/
  contexto/
```

### Paso 2. Copiar el LaTeX de contexto

Desde el material del curso, localiza el archivo:

```text
materiales/ley 39-2015/ley-39-2015-extracto-procedimiento-administrativo.tex
```

Copialo dentro de la carpeta `contexto` de tu proyecto `e3`.

La estructura debe quedar asi:

```text
e3/
  contexto/
    ley-39-2015-extracto-procedimiento-administrativo.tex
```

Abre el archivo desde VS Code y lee las primeras secciones.

Comprueba:

- que el documento indica que es un extracto formativo;
- que remite al BOE como fuente oficial;
- que advierte que cualquier uso real exige verificacion juridica;
- que esta escrito en LaTeX.

### Paso 3. Compilar el contexto

Con `ley-39-2015-extracto-procedimiento-administrativo.tex` abierto, pulsa el icono de **Play**.

Comprueba que se genera:

```text
ley-39-2015-extracto-procedimiento-administrativo.pdf
```

Este PDF solo sirve para leer comodamente el contexto. La fuente que se usara con Codex sera el archivo `.tex`.

### Paso 4. Crear el borrador LaTeX

En `e3`, crea:

```text
informe_revision_procedimiento.tex
```

Pega:

```latex
\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish]{babel}

\title{Informe interno de revision procedimental}
\author{Area de Atencion Ciudadana}
\date{\today}

\begin{document}

\maketitle

\section{Situacion analizada}

Se ha recibido una solicitud ciudadana incompleta relacionada con una incidencia en la via publica.

El area responsable quiere preparar una respuesta inicial sin cerrar el expediente de forma indebida.

\section{Cautelas procedimentales}

Pendiente de redactar.

\section{Informacion que no debe darse por supuesta}

Pendiente de redactar.

\section{Puntos pendientes de verificacion juridica}

Pendiente de redactar.

\section{Comprobaciones antes de firmar}

Pendiente de redactar.

\end{document}
```

Guarda el archivo.

### Paso 5. Hacer una pregunta demasiado abierta

Antes de usar el contexto, pregunta a Codex:

```text
Tengo una solicitud ciudadana incompleta sobre una incidencia en la via publica.
Redacta un informe juridico-administrativo indicando que debe hacer el ayuntamiento.
```

Lee la respuesta, pero no la pegues en el documento.

Comprueba si Codex:

- cita articulos que no has proporcionado;
- habla de jurisprudencia sin fuente;
- inventa plazos concretos;
- da por cerrados tramites que no constan;
- usa un tono demasiado seguro.

El objetivo de este paso es ver el riesgo de trabajar sin contexto.

### Paso 6. Repetir la pregunta usando el LaTeX de contexto

Abre:

```text
contexto/ley-39-2015-extracto-procedimiento-administrativo.tex
```

Copia todo el contenido del archivo.

Abre Codex y escribe:

```text
Voy a darte un archivo LaTeX de contexto normativo.
Usalo como unica fuente normativa para la tarea siguiente.

CONTEXTO:

[pega aqui el contenido completo de ley-39-2015-extracto-procedimiento-administrativo.tex]

TAREA:

Estoy preparando un informe interno sobre una solicitud ciudadana incompleta relacionada con una incidencia en la via publica.

Necesito completar estas secciones de un documento LaTeX:
- Cautelas procedimentales
- Informacion que no debe darse por supuesta
- Puntos pendientes de verificacion juridica
- Comprobaciones antes de firmar

Condiciones:
- no inventes articulos que no aparezcan en el contexto;
- no cites jurisprudencia;
- no inventes plazos concretos;
- si el contexto no contiene detalle suficiente, escribe "pendiente de verificacion juridica";
- menciona entre parentesis el articulo del contexto que justifica cada recomendacion;
- manten un lenguaje claro para personal no juridico;
- no reescribas todo el documento, solo propone el contenido de las secciones pendientes.

Primero explica que informacion del contexto vas a usar.
Despues propone el texto para cada seccion.
```

### Paso 7. Revisar la respuesta antes de copiar

No copies la respuesta automaticamente.

Comprueba:

- que Codex se limita al LaTeX de contexto;
- que no aparecen leyes distintas;
- que no aparece jurisprudencia;
- que las recomendaciones mencionan articulos incluidos en el contexto;
- que las dudas quedan marcadas como `pendiente de verificacion juridica`.

Si Codex inventa informacion, responde:

```text
Rehaz la respuesta.
Has incluido informacion que no esta en el LaTeX de contexto.
Usa solo el contexto proporcionado y marca como pendiente de verificacion juridica lo que no puedas justificar.
```

### Paso 8. Completar el LaTeX manualmente

Vuelve a:

```text
informe_revision_procedimiento.tex
```

Sustituye los textos `Pendiente de redactar.` por el contenido revisado.

No pegues nada que no entiendas o que no puedas justificar con el LaTeX de contexto.

### Paso 9. Compilar con Play

Con `informe_revision_procedimiento.tex` abierto, pulsa el icono de **Play**.

Comprueba que se genera:

```text
informe_revision_procedimiento.pdf
```

Si aparece un error, pregunta a Codex:

```text
Tengo este error al compilar LaTeX.
Explicamelo en lenguaje sencillo y dime que linea debo revisar.
No reescribas todo el documento.
```

### Paso 10. Revisar el resultado final

Abre el PDF en la ventana principal de VS Code.

Comprueba:

- que el informe no dice ser una resolucion administrativa;
- que no cierra el expediente;
- que no inventa datos de la persona solicitante;
- que las referencias proceden del LaTeX de contexto;
- que cualquier duda juridica queda marcada para revision humana.

### Paso 11. Preparar la entrega

Dentro de `e3`, crea una carpeta llamada:

```text
entrega
```

Copia dentro:

```text
contexto/ley-39-2015-extracto-procedimiento-administrativo.tex
informe_revision_procedimiento.tex
informe_revision_procedimiento.pdf
```

No hace falta copiar los archivos auxiliares de LaTeX.

## Producto de la sesion

- Carpeta `curso-entorno/e3`.
- Carpeta `contexto`.
- Archivo `contexto/ley-39-2015-extracto-procedimiento-administrativo.tex`.
- Archivo `informe_revision_procedimiento.tex`.
- PDF `informe_revision_procedimiento.pdf`.
- Comparacion entre una pregunta sin contexto y una pregunta con LaTeX de contexto.
- Checklist de la sesion 3 compilado por el estudiante a partir de `checklists/checklist-sesion-3.tex`.

## Glosario de terminos

- **IA generativa**: sistema capaz de producir texto, codigo u otros contenidos a partir de instrucciones.
- **Codex**: asistente de IA que ayuda a entender y modificar documentos o codigo.
- **Prompt**: instruccion o pregunta escrita a una IA.
- **Contexto**: informacion que se entrega a la IA para limitar y orientar la respuesta.
- **LaTeX de contexto**: archivo `.tex` que Codex debe usar como fuente principal para responder.
- **Fuente normativa**: texto juridico o administrativo que sirve de base para una recomendacion.
- **Alucinacion**: respuesta generada por una IA que contiene informacion inventada o no justificada.
- **Verificacion juridica**: revision humana especializada antes de usar un texto en un caso real.
- **Formato LaTeX**: estructura tecnica del documento, con comandos como `\section` o `\begin`.
- **Error de compilacion**: problema que impide generar el PDF.
- **Archivo auxiliar**: archivo tecnico creado por LaTeX durante la compilacion.
