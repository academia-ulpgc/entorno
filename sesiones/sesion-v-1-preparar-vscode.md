# Sesion V.1 - VS Code en español, LaTeX y Copilot

## Duracion

1 hora y 15 minutos.

## Objetivo

Configurar Visual Studio Code para trabajar con documentos LaTeX en español y usar Copilot como apoyo para entender, revisar y mejorar un documento.

Esta sesion introduce Visual Studio Code como herramienta de trabajo para las proximas sesiones del curso. El objetivo no es dominar todo VS Code, sino familiarizarse con lo basico: abrir una carpeta, crear archivos, instalar extensiones, escribir codigo LaTeX, compilar y revisar el resultado.

La idea de fondo es que LaTeX permite entender una forma sencilla de programar:

- se crea una carpeta de proyecto;
- se escribe un archivo con instrucciones, el "codigo";
- se compila ese archivo;
- se obtiene un resultado, normalmente un PDF;
- se revisa el resultado y se corrige el codigo si hace falta.

El foco esta en:

- poner VS Code en español;
- instalar LaTeX Workshop;
- crear un documento LaTeX sencillo;
- compilarlo a PDF;
- iniciar sesion en Copilot con SSO o cuenta autorizada;
- pedir a Copilot explicaciones y mejoras sobre el documento LaTeX.

## Practica paso a paso

### Paso 1. Abrir VS Code

Abre Visual Studio Code desde el menu de aplicaciones.

Si no esta instalado, usa:

```text
https://code.visualstudio.com/download
```

### Paso 2. Crear la carpeta de trabajo

Crea una carpeta llamada:

```text
curso-vscode
```

Abrela desde VS Code con **Archivo > Abrir carpeta...**.

Si VS Code pregunta si confias en la carpeta, acepta solo si la has creado tu o pertenece al material del curso.

Esta carpeta sera el proyecto. Dentro estara el codigo LaTeX y, despues de compilar, el PDF resultante.

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

Pulsa **Install** o **Instalar**.

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

### Paso 5. Crear `informe_prueba.tex`

En la carpeta `curso-vscode`, crea:

```text
informe_prueba.tex
```

Este archivo es el codigo fuente del documento. No es el PDF final: es el archivo que contiene las instrucciones que LaTeX va a procesar.

Pega:

```latex
\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
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

### Paso 6. Compilar el documento

Usa el boton de compilacion de LaTeX Workshop.

Compilar significa convertir el codigo LaTeX del archivo `.tex` en un PDF.

Si no lo encuentras:

1. Abre la paleta de comandos.
2. Busca:

```text
LaTeX Workshop: Build LaTeX project
```

3. Ejecuta el comando.

Comprueba que se genera un PDF.

Si algo falla, no borres el archivo. Lee el error con calma y pide ayuda a Copilot para entenderlo.

### Paso 7. Instalar y activar Copilot

En extensiones, busca:

```text
GitHub Copilot
```

Instala tambien Copilot Chat si no aparece automaticamente.

Datos de referencia:

- GitHub Copilot:
  - Creador: GitHub
  - Identificador: `GitHub.copilot`

- GitHub Copilot Chat:
  - Creador: GitHub
  - Identificador: `GitHub.copilot-chat`

Inicia sesion con la cuenta indicada.

Si aparece SSO:

1. elige la organizacion o proveedor indicado;
2. introduce tus credenciales institucionales;
3. completa la verificacion adicional si se solicita;
4. acepta volver a VS Code.

### Paso 8. Usar Copilot con LaTeX

Abre `informe_prueba.tex` y pregunta:

```text
Explicame la estructura de este documento LaTeX.
Indica que hacen documentclass, usepackage, title, section, itemize e item.
Explicame tambien la diferencia entre el archivo .tex como codigo fuente y el PDF como resultado compilado.
Explicame por que este ejemplo se parece a un informe municipal real, aunque use datos ficticios.
No cambies el archivo.
```

Despues pregunta:

```text
Propón una mejora pequeña para que el documento sea mas claro.
No inventes informacion.
Explica el cambio antes de proponer el texto.
```

No aceptes cambios automaticamente. Aplica manualmente solo lo que entiendas.

## Checklist final

- [ ] VS Code abre correctamente.
  - Observaciones:

- [ ] La interfaz esta en español.
  - Observaciones:

- [ ] LaTeX Workshop esta instalado.
  - Observaciones:

- [ ] `informe_prueba.tex` compila.
  - Observaciones:

- [ ] El PDF se puede visualizar.
  - Observaciones:

- [ ] Copilot Chat responde.
  - Observaciones:

- [ ] He iniciado sesion con SSO/cuenta autorizada o he documentado la incidencia.
  - Observaciones:

- [ ] Entiendo que no debo aceptar cambios sin revisar.
  - Observaciones:

## Producto de la sesion

- Archivo `informe_prueba.tex`.
- PDF generado desde LaTeX, si el equipo lo permite.
- Respuesta de Copilot explicando el documento LaTeX.
- Checklist final completada.
