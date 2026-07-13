# Sesion 1 - Preparar VS Code, LaTeX y Codex

## Duracion

1 hora y 15 minutos.

## Objetivo

Preparar Visual Studio Code para trabajar con documentos LaTeX en español y empezar a usar Codex como apoyo.

En esta sesion se introduce una idea importante: **hacer documentos en LaTeX se parece a programar**.

La forma de trabajo sera:

- crear una carpeta de proyecto;
- escribir un archivo con instrucciones;
- compilarlo;
- obtener un PDF;
- revisar el resultado;
- corregir y volver a compilar si hace falta.

## Practica paso a paso

### Paso 1. Abrir Visual Studio Code

Abre Visual Studio Code desde el menu de aplicaciones.

Si no esta instalado, usa:

```text
https://code.visualstudio.com/download
```

### Paso 2. Crear la carpeta del curso y el proyecto e1

Crea una carpeta llamada:

```text
curso-entorno
```

Dentro de `curso-entorno`, crea otra carpeta llamada:

```text
e1
```

Abre la carpeta `e1` desde VS Code con:

```text
Archivo > Abrir carpeta...
```

Si VS Code pregunta si confias en la carpeta, acepta solo si la has creado tu o pertenece al material del curso.

La carpeta `e1` sera el primer proyecto. Dentro estaran el archivo LaTeX, el PDF y los archivos auxiliares que se generen al compilar.

### Paso 3. Instalar el idioma español

Abre la vista de extensiones.

Busca:

```text
Spanish Language Pack for Visual Studio Code
```

Comprueba:

- Nombre exacto: Spanish Language Pack for Visual Studio Code
- Creador oficial: Microsoft
- Identificador unico: `MS-CEINTL.vscode-language-pack-es`
- Funcion: traduce la interfaz, menus y configuraciones de VS Code al español.

Pulsa **Instalar**.

Si VS Code lo pide, reinicia y cambia el idioma a español.

### Paso 4. Instalar LaTeX Workshop

En extensiones, busca:

```text
LaTeX Workshop
```

Comprueba:

- Nombre exacto: LaTeX Workshop
- Creador oficial: James Yu
- Identificador unico: `James-Yu.latex-workshop`
- Funcion: permite compilar archivos LaTeX y ver el PDF integrado.

Pulsa **Instalar**.

No hace falta instalar otro visor de PDF para esta practica. LaTeX Workshop incluye un visor integrado dentro de VS Code.

### Paso 5. Configurar el PDF para que se abra en la ventana principal

Para evitar muchas ventanas, configura LaTeX Workshop para abrir el PDF como una pestaña dentro de VS Code.

En la carpeta `e1`, crea una carpeta llamada:

```text
.vscode
```

Dentro de `.vscode`, crea un archivo llamado:

```text
settings.json
```

Pega exactamente:

```json
{
  "latex-workshop.view.pdf.viewer": "tab"
}
```

Guarda el archivo.

### Paso 6. Crear el archivo LaTeX

En la carpeta `e1`, crea:

```text
informe_prueba.tex
```

Este archivo es el codigo fuente del documento. No es el PDF final: contiene las instrucciones que LaTeX va a procesar.

Pega:

```latex
\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish]{babel}

\title{Informe municipal de seguimiento de incidencias}
\author{Area de Atencion Ciudadana}
\date{\today}

\begin{document}

\maketitle

\section{Objetivo}

Este informe ficticio sirve para practicar la creacion de documentos estructurados con LaTeX en Visual Studio Code.

El documento resume incidencias comunicadas por la ciudadania sobre elementos de la via publica. Los datos son inventados y se usan solo con fines formativos.

\section{Resumen de incidencias}

Durante la semana analizada se han registrado incidencias en tres ambitos principales:

\begin{itemize}
    \item Alumbrado publico: 8 avisos.
    \item Aceras y pavimento: 5 avisos.
    \item Limpieza viaria: 6 avisos.
\end{itemize}

\section{Actuaciones previstas}

Las actuaciones se organizaran en funcion de la urgencia, la disponibilidad de medios y la concentracion de avisos en una misma zona.

\begin{itemize}
    \item Revisar los avisos de alumbrado en calles con mayor numero de incidencias.
    \item Priorizar reparaciones de pavimento que afecten a la accesibilidad peatonal.
    \item Coordinar la limpieza de zonas con avisos repetidos.
\end{itemize}

\section{Comprobaciones antes de enviar}

Antes de usar un informe de este tipo en un contexto real, una persona debe comprobar:

\begin{itemize}
    \item que los datos proceden de una fuente autorizada;
    \item que no se incluyen datos personales innecesarios;
    \item que las cifras son correctas;
    \item que las actuaciones propuestas han sido validadas por el area responsable.
\end{itemize}

\end{document}
```

Guarda el archivo.

### Paso 7. Compilar con el icono de Play

Con `informe_prueba.tex` abierto, pulsa el icono de **Play** de LaTeX Workshop.

El icono suele aparecer en la parte superior derecha del editor como un triangulo verde.

Compilar significa convertir el archivo `.tex` en un PDF.

Comprueba que aparece un archivo:

```text
informe_prueba.pdf
```

### Paso 8. Reconocer los archivos auxiliares

Despues de compilar, es normal que aparezcan varios archivos nuevos.

Puedes ver nombres como:

```text
informe_prueba.aux
informe_prueba.log
informe_prueba.synctex.gz
informe_prueba.fls
informe_prueba.fdb_latexmk
```

No son errores. Son archivos auxiliares que LaTeX usa para construir el PDF, guardar informacion de compilacion y ayudar a localizar problemas.

Para entregar un documento normalmente interesan sobre todo:

```text
informe_prueba.tex
informe_prueba.pdf
```

### Paso 9. Abrir el PDF en la ventana principal

Abre `informe_prueba.pdf` desde el explorador de VS Code.

Debe abrirse como una pestaña dentro de la ventana principal.

Si se abre en otra columna o resulta incomodo, cierra esa vista y vuelve a abrir el PDF desde el explorador. La idea es trabajar con una sola ventana principal para no perderse.

### Paso 10. Acceder a Codex

Abre en el navegador:

```text
https://chatgpt.com/
```

Inicia sesion con la cuenta indicada para el curso.

Selecciona **Codex**.

Si no aparece Codex, no continues con otra herramienta: anota la incidencia y avisa al responsable del curso.

No hace falta instalar ninguna extension adicional de IA en VS Code para esta practica.

La forma de trabajo sera:

- escribir y compilar el documento en VS Code;
- copiar a Codex solo el fragmento necesario;
- pedir explicaciones o mejoras concretas;
- revisar la respuesta antes de cambiar el archivo.

### Paso 11. Usar Codex para entender el documento

Abre `informe_prueba.tex`, copia su contenido y pregunta a Codex:

```text
Explicame la estructura de este documento LaTeX.
Indica que hacen documentclass, usepackage, title, section, itemize e item.
Explicame tambien la diferencia entre el archivo .tex como codigo fuente y el PDF como resultado compilado.
No cambies el archivo.
```

Despues pregunta:

```text
Propón una mejora pequeña para que el documento sea mas claro.
No inventes informacion.
Explica el cambio antes de proponer el texto.
```

No aceptes cambios automaticamente. Aplica manualmente en VS Code solo lo que entiendas.

## Producto de la sesion

- Carpeta `curso-entorno/e1`.
- Archivo `informe_prueba.tex`.
- PDF generado desde LaTeX.
- Archivos auxiliares creados por la compilacion.
- Respuesta de Codex explicando el documento.
- Checklist de la sesion 1 compilado por el estudiante a partir de `checklists/checklist-sesion-1.tex`.

## Glosario de terminos

- **VS Code**: editor de codigo que permite abrir carpetas, crear archivos y usar extensiones.
- **Extension**: complemento que añade funciones a VS Code.
- **Archivo `.tex`**: archivo de texto que contiene codigo LaTeX.
- **Codigo fuente**: instrucciones escritas en un archivo antes de generar el resultado final.
- **LaTeX**: lenguaje para crear documentos a partir de instrucciones.
- **Compilar**: convertir codigo fuente en un resultado, en este caso un PDF.
- **PDF**: archivo final generado tras compilar el documento.
- **LaTeX Workshop**: extension de VS Code para compilar LaTeX y visualizar PDFs.
- **Icono de Play**: boton que ejecuta la compilacion.
- **Archivo auxiliar**: archivo tecnico creado durante la compilacion, como `.aux`, `.log` o `.synctex.gz`.
- **`settings.json`**: archivo de configuracion de VS Code.
- **Codex**: asistente de IA que ayuda a entender y modificar documentos o codigo.
- **Prompt**: instruccion o pregunta escrita a una IA.
