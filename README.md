# Entorno. VS Code, LaTeX y Codex para programar documentos

## Proposito

Este bloque, llamado **Entorno**, introduce Visual Studio Code como espacio de trabajo para personas sin perfil informatico.

La idea principal es sencilla: con apoyo de la IA, una persona puede desarrollar competencias para automatizar parte de su trabajo y preparar documentos mejor estructurados. No necesita convertirse en informatica. La IA actua como apoyo tecnico, y VS Code ofrece el espacio donde ordenar archivos, escribir instrucciones y revisar resultados.

En este bloque se trabaja una idea central: **programar documentos**.

Programar documentos significa:

- crear una carpeta de proyecto;
- escribir un archivo fuente con instrucciones;
- compilar ese archivo;
- obtener un PDF;
- revisar el resultado;
- corregir el archivo fuente y volver a compilar.

Usaremos LaTeX porque permite ver con claridad esa relacion entre codigo y resultado.

## Duracion

Entorno dura **5 horas en total** y se organiza en cuatro sesiones de aproximadamente **1 hora y 15 minutos**.

Cada sesion es tambien una practica. El estudiante sigue el archivo de la sesion paso a paso.

## Sesiones

- [Sesion 1 - Preparar VS Code, LaTeX y Codex](sesiones/sesion-1-preparar-vscode.md)
- [Sesion 2 - Crear un documento municipal estructurado](sesiones/sesion-2-documento-municipal.md)
- [Sesion 3 - Usar Codex con contexto y sin inventar informacion](sesiones/sesion-3-codex-contexto.md)
- [Sesion 4 - Primer uso de Python para generar un documento LaTeX](sesiones/sesion-4-entrega.md)

## Checklists

Los checklists no se entregan ya compilados en PDF. Cada estudiante debe generar su propio PDF a partir del archivo LaTeX correspondiente.

Archivos fuente:

- [Checklist sesion 1](checklists/checklist-sesion-1.tex)
- [Checklist sesion 2](checklists/checklist-sesion-2.tex)
- [Checklist sesion 3](checklists/checklist-sesion-3.tex)
- [Checklist sesion 4](checklists/checklist-sesion-4.tex)

Para generar el PDF de un checklist:

1. Abre el archivo `.tex` del checklist en VS Code.
2. Pulsa el icono de **Play** de LaTeX Workshop.
3. Comprueba que aparece el PDF correspondiente.
4. Abre el PDF en una pestaña de la ventana principal de VS Code.

Al compilar tambien pueden aparecer archivos auxiliares como `.aux`, `.log` o `.synctex.gz`. Es normal: forman parte del proceso de generacion del PDF.

## Estructura de carpetas recomendada para el alumnado

Durante el bloque se recomienda crear una carpeta llamada:

```text
curso-entorno
```

Dentro de ella, cada sesion tendra su propia carpeta:

```text
curso-entorno/
  e1/
  e2/
  e3/
  e4/
```

En la primera sesion, el proyecto se llama **e1**.

## Herramientas principales

- Visual Studio Code:
  - Uso: editor principal del bloque.
  - Enlace: <https://code.visualstudio.com/download>

- Spanish Language Pack for Visual Studio Code:
  - Creador oficial: Microsoft
  - Identificador: `MS-CEINTL.vscode-language-pack-es`
  - Uso: poner VS Code en español.

- LaTeX Workshop:
  - Creador oficial: James Yu
  - Identificador: `James-Yu.latex-workshop`
  - Uso: compilar documentos LaTeX con el icono de Play y abrir el PDF dentro de VS Code.

- Codex:
  - Uso: pedir ayuda para explicar, revisar y mejorar documentos y codigo.
  - Acceso: <https://chatgpt.com/> con la cuenta indicada para el curso.

- Python:
  - Uso: se introduce solo en la ultima sesion para generar automaticamente un archivo LaTeX sencillo.
  - Enlace: <https://www.python.org/downloads/>

## Visor de PDF

No hace falta instalar otro visor de PDF para estas practicas si LaTeX Workshop funciona correctamente. La extension incluye un visor integrado.

Para evitar muchas ventanas abiertas, se configurara LaTeX Workshop para abrir el PDF en una pestaña de la ventana principal de VS Code.

La configuracion recomendada es:

```json
{
  "latex-workshop.view.pdf.viewer": "tab"
}
```

## Resultado esperado

Al terminar Entorno, cada participante deberia poder:

- abrir una carpeta de proyecto en VS Code;
- crear y editar archivos LaTeX;
- entender que el archivo `.tex` es el codigo fuente del documento;
- compilar con el icono de Play;
- reconocer el PDF como resultado;
- entender que LaTeX genera archivos auxiliares como `.aux`, `.log` o `.synctex.gz`;
- pedir ayuda a Codex sin aceptar automaticamente lo que proponga;
- entender que Python puede crear archivos automaticamente;
- revisar documentos antes de entregarlos.
