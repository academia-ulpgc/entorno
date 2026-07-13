# Sesion V.3 - Copilot con contexto e instrucciones

## Duracion

1 hora y 15 minutos.

## Objetivo

Usar Copilot Chat con mas precision: redactar, revisar, aportar contexto y comprobar que la respuesta no inventa informacion.

## Practica paso a paso

### Paso 1. Crear la carpeta

Crea:

```text
practica-v3
```

Dentro, crea:

```text
texto-copilot.md
esquema-informe.md
documentacion-proceso.md
revision-respuestas.md
contexto-del-proyecto.md
.github/copilot-instructions.md
```

### Paso 2. Crear un texto para revisar

En `texto-copilot.md`, pega:

```markdown
Este bloque enseña utilizar herramientas de IA en un entorno de trabajo con VS Code, LaTeX y Python. El objetivo es que se pueda hacer documentos y automatizaciones sencillas sin ser informático. También se va a usar Copilot para que ayude a explicar errores y mejorar documentos, pero hay que tener cuidado porque no todo lo que dice una IA tiene que estar bien.
```

### Paso 3. Comparar una pregunta vaga y una precisa

Primero pregunta a Copilot:

```text
Mejora esto.
```

Despues pregunta:

```text
Revisa el texto del archivo abierto.
Propón una version mas clara y breve para empleados publicos sin perfil tecnico.
Mantén el sentido original.
No añadas ideas nuevas.
Antes de dar la version final, dime que problemas has detectado.
```

En `revision-respuestas.md`, anota:

```markdown
# Comparacion de respuestas

## Respuesta vaga


## Respuesta precisa


## Cambios que acepto

-

## Cambios que no acepto

-
```

### Paso 4. Generar un esquema de informe

Abre `esquema-informe.md` y pregunta:

```text
Crea un esquema para un informe de practica sobre como configurar VS Code, compilar un documento LaTeX y ejecutar un script Python.

Condiciones:
- maximo 6 apartados;
- pensado para una persona no tecnica;
- incluir un apartado final de comprobaciones;
- no escribas el informe completo, solo el esquema.
```

Pega el resultado y revisalo.

### Paso 5. Documentar un proceso a partir de hechos

En `documentacion-proceso.md`, escribe:

```markdown
# Hechos de la practica

- He abierto VS Code.
- He creado una carpeta de trabajo.
- He creado un archivo LaTeX.
- He compilado el documento a PDF.
- He creado un script Python.
- He ejecutado el script y he revisado la salida.
- He usado Copilot para pedir explicaciones y mejoras.
```

Pregunta:

```text
Redacta un resumen de la practica a partir de estos hechos.
Usa primera persona.
No inventes pasos que no esten en la lista.
Maximo 180 palabras.
```

### Paso 6. Crear contexto del proyecto

En `contexto-del-proyecto.md`, pega:

```markdown
# Contexto del proyecto

Este proyecto forma parte de un curso para personas sin perfil tecnico.

El objetivo es aprender a usar VS Code, LaTeX, Python y Copilot en tareas administrativas sencillas.

El tono debe ser claro, directo y practico.

No deben incluirse datos personales reales.

Cuando se generen ejemplos, deben ser ficticios y faciles de revisar.
```

### Paso 7. Crear instrucciones para Copilot

En `.github/copilot-instructions.md`, pega:

```markdown
# Instrucciones para Copilot

Este proyecto es material de curso para alumnado sin perfil tecnico.

Cuando ayudes en este proyecto:

- usa español claro;
- evita jerga informatica si no la explicas;
- divide las tareas en pasos;
- no inventes leyes, datos personales, expedientes ni resultados;
- si falta informacion, indicalo;
- propone cambios pequeños y revisables.
```

### Paso 8. Probar contexto

Pregunta:

```text
Usa contexto-del-proyecto.md.
Redacta una introduccion para un informe de practica sobre VS Code.
Debe ser clara para personas sin perfil tecnico.
Maximo 120 palabras.
```

Comprueba que la respuesta no inventa informacion.

## Checklist final

- [ ] He creado los archivos de la sesion.
  - Observaciones:

- [ ] He comparado una pregunta vaga y una pregunta precisa.
  - Observaciones:

- [ ] He generado un esquema de informe.
  - Observaciones:

- [ ] He documentado un proceso a partir de hechos.
  - Observaciones:

- [ ] He creado contexto e instrucciones para Copilot.
  - Observaciones:

- [ ] He revisado que Copilot no invente informacion.
  - Observaciones:

## Producto de la sesion

- `texto-copilot.md`.
- `esquema-informe.md`.
- `documentacion-proceso.md`.
- `revision-respuestas.md`.
- `contexto-del-proyecto.md`.
- `.github/copilot-instructions.md`.
