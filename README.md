# Entorno. VS Code, LaTeX y Codex para programar documentos

## Proposito

Este modulo, llamado **Entorno**, introduce una nueva forma de trabajar con tecnologia para personas sin perfil informatico.

La idea principal coincide con la presentacion inicial: **programar sin ser informatico**. No se trata de aprender programacion clasica desde cero, sino de entender un metodo de trabajo: describir una tarea, preparar archivos, pedir ayuda a Codex, probar el resultado y revisar antes de aceptar nada.

En este modulo, VS Code funciona como **mesa de trabajo**. Todo ocurre dentro de una carpeta ordenada: archivos fuente, materiales de apoyo, resultados y checklists. LaTeX permite ver con claridad la relacion entre instrucciones y resultado: se escribe un archivo `.tex`, se compila con el icono de Play y se obtiene un PDF revisable.

Codex se presenta como apoyo tecnico. Puede explicar errores, proponer cambios y ayudar a entender codigo o documentos, pero no sustituye el criterio de la persona. La regla de trabajo del modulo es:

```text
Codex propone. La persona prueba, revisa y decide.
```

En este modulo se trabaja una idea central: **programar documentos**.

Programar documentos significa:

- crear una carpeta de proyecto;
- escribir un archivo fuente con instrucciones;
- compilar ese archivo;
- obtener un PDF;
- revisar el resultado;
- corregir el archivo fuente y volver a compilar.

Usaremos LaTeX porque permite ver con claridad esa relacion entre codigo y resultado. Al final del modulo tambien se prepara Python desde VS Code, no para automatizar todavia todo el proceso, sino para dejar listo el entorno que se usara despues en el modulo de Automatizacion.

## Duracion

Entorno dura **5 horas en total** y se organiza en cuatro sesiones de aproximadamente **1 hora y 15 minutos**.

Cada sesion es tambien una practica. El estudiante sigue el archivo de la sesion paso a paso.

## Sesiones

- [Sesion 1 - Preparar VS Code, LaTeX y Codex](sesiones/sesion-1-preparar-vscode.md)
- [Sesion 2 - Crear un documento municipal estructurado](sesiones/sesion-2-documento-municipal.md)
- [Sesion 3 - Usar Codex con un LaTeX de contexto legal](sesiones/sesion-3-codex-contexto.md)
- [Sesion 4 - Preparar Python en VS Code y ejecutar un programa](sesiones/sesion-4-python-vscode.md)

## Material de apoyo

- [Modulo 2.1 - Presentacion de la primera sesion](2.1%20entorno.pdf)
- [Carpeta de materiales](materiales/README.md)
- [LaTeX de contexto de la sesion 3: extracto formativo de la Ley 39/2015](materiales/ley%2039-2015/ley-39-2015-extracto-procedimiento-administrativo.tex)
- [Codigo de ejemplo de la sesion 4: tres en raya](materiales/3%20en%20raya/tres_en_raya.py)

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

Durante el modulo se recomienda crear una carpeta llamada:

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
  - Uso: editor principal del modulo.
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
  - Uso: se introduce solo en la ultima sesion para ejecutar un programa sencillo ya preparado.
  - Forma de uso en el curso: siempre desde VS Code, usando botones y menus.
  - Paquetes externos: la practica no requiere instalar paquetes adicionales de Python.
  - Enlace: <https://www.python.org/downloads/>

- Extension Python para VS Code:
  - Nombre exacto: Python
  - Creador oficial: Microsoft
  - Identificador: `ms-python.python`
  - Uso: permite a VS Code trabajar mejor con archivos `.py` y ejecutarlos con el boton **Run Python File**.

## Visor de PDF

No hace falta instalar otro visor de PDF para estas practicas si LaTeX Workshop funciona correctamente. La extension incluye un visor integrado.

Para evitar muchas ventanas abiertas, se abrira el PDF desde el explorador de archivos de VS Code y se trabajara dentro de la ventana principal.

No se pedira al alumnado crear archivos de configuracion de VS Code.

## Resultado esperado

Al terminar Entorno, cada participante deberia poder:

- abrir una carpeta de proyecto en VS Code;
- crear y editar archivos LaTeX;
- entender que el archivo `.tex` es el codigo fuente del documento;
- compilar con el icono de Play;
- reconocer el PDF como resultado;
- entender que LaTeX genera archivos auxiliares como `.aux`, `.log` o `.synctex.gz`;
- pedir ayuda a Codex sin aceptar automaticamente lo que proponga;
- distinguir entre Python instalado en el ordenador y la extension Python de VS Code;
- ejecutar un programa Python sencillo desde VS Code;
- revisar documentos antes de entregarlos.
