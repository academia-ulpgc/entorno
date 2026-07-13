# Sesion V.4 - Automatizacion sencilla y entrega del trabajo

## Duracion

1 hora y 15 minutos.

## Objetivo

Automatizar una tarea sencilla con Python y preparar una entrega ordenada mediante carpetas, checklist y revision manual.

## Practica paso a paso

### Paso 1. Crear la carpeta

Crea:

```text
practica-v5
```

Dentro, crea:

```text
solicitudes.csv
generar_informe.py
notas-validacion.md
```

### Paso 2. Crear `solicitudes.csv`

Pega:

```csv
id,area,tipo,estado,dias_respuesta
1,Urbanismo,Licencia,Resuelta,12
2,Servicios Sociales,Ayuda,Pendiente,8
3,Urbanismo,Consulta,Resuelta,5
4,Medio Ambiente,Queja,Pendiente,15
5,Servicios Sociales,Ayuda,Resuelta,20
6,Medio Ambiente,Consulta,Resuelta,4
7,Urbanismo,Licencia,Pendiente,18
8,Atención Ciudadana,Consulta,Resuelta,2
```

Estos datos son ficticios. No uses expedientes reales ni datos personales.

### Paso 3. Crear `generar_informe.py`

Pega:

```python
import csv
from collections import Counter

archivo_datos = "solicitudes.csv"
archivo_informe = "informe_solicitudes.md"

solicitudes = []

with open(archivo_datos, newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        fila["dias_respuesta"] = int(fila["dias_respuesta"])
        solicitudes.append(fila)

total = len(solicitudes)
por_estado = Counter(s["estado"] for s in solicitudes)
por_area = Counter(s["area"] for s in solicitudes)
media_dias = sum(s["dias_respuesta"] for s in solicitudes) / total

lineas = []
lineas.append("# Informe de solicitudes")
lineas.append("")
lineas.append("## Resumen general")
lineas.append("")
lineas.append(f"- Total de solicitudes: {total}")
lineas.append(f"- Tiempo medio de respuesta: {media_dias:.1f} dias")
lineas.append("")
lineas.append("## Solicitudes por estado")
lineas.append("")

for estado, cantidad in por_estado.items():
    lineas.append(f"- {estado}: {cantidad}")

lineas.append("")
lineas.append("## Solicitudes por area")
lineas.append("")

for area, cantidad in por_area.items():
    lineas.append(f"- {area}: {cantidad}")

lineas.append("")
lineas.append("## Observaciones")
lineas.append("")
lineas.append("- Este informe se ha generado a partir de datos ficticios.")
lineas.append("- Las conclusiones deben revisarse antes de usarse en un documento real.")

with open(archivo_informe, "w", encoding="utf-8") as archivo:
    archivo.write("\n".join(lineas))

print(f"Informe generado: {archivo_informe}")
```

### Paso 4. Ejecutar el script

Ejecuta `generar_informe.py`.

Resultado esperado:

```text
Informe generado: informe_solicitudes.md
```

Abre `informe_solicitudes.md`.

### Paso 5. Validar los resultados

En `notas-validacion.md`, pega y completa:

```markdown
# Validacion humana

## Comprobaciones

- Total de filas de datos revisado:
- Estados detectados:
- Areas detectadas:
- El informe contiene solo datos ficticios:

## Dudas o errores encontrados

-
```

### Paso 6. Pedir ayuda a Copilot

Pregunta:

```text
Explica este script Python paso a paso para una persona no tecnica.
No propongas cambios todavia.
```

Despues pregunta:

```text
Propón una unica mejora pequeña para que el informe generado sea mas util.
Antes de dar codigo, explica por que esa mejora ayuda.
```

Revisa la propuesta antes de aplicarla.

### Paso 7. Preparar la entrega

Crea:

```text
entrega-bloque-v
```

Dentro, crea:

```text
ENTREGA.md
incidencias-acceso.md
```

En `ENTREGA.md`, pega:

```markdown
# Entrega del Bloque V

## Participante

Nombre:

## Sesiones incluidas

- [ ] Sesion V.1 - VS Code, LaTeX y Copilot.
- [ ] Sesion V.2 - Primer proyecto con LaTeX, Markdown y Python.
- [ ] Sesion V.3 - Copilot con contexto e instrucciones.
- [ ] Sesion V.4 - Automatizacion y entrega.

## Estado del acceso

- [ ] Copilot funciona.
- [ ] Copilot no funciona, pero la incidencia esta documentada.
- [ ] He usado SSO o cuenta autorizada.

## Confirmacion

- [ ] He revisado que no hay datos personales reales.
- [ ] He revisado que no hay contraseñas.
- [ ] He abierto los archivos antes de entregar.
- [ ] He comprobado que los scripts funcionan o he documentado el problema.
```

En `incidencias-acceso.md`, anota cualquier problema con SSO, Copilot o permisos.

## Checklist final

- [ ] He creado el CSV con datos ficticios.
  - Observaciones:

- [ ] He ejecutado el script Python.
  - Observaciones:

- [ ] Se ha generado `informe_solicitudes.md`.
  - Observaciones:

- [ ] He revisado manualmente los resultados.
  - Observaciones:

- [ ] He preparado `entrega-bloque-v`.
  - Observaciones:

- [ ] No hay datos personales reales ni contraseñas.
  - Observaciones:

## Producto de la sesion

- `solicitudes.csv`.
- `generar_informe.py`.
- `informe_solicitudes.md`.
- `notas-validacion.md`.
- Carpeta `entrega-bloque-v`.
- `ENTREGA.md`.
- `incidencias-acceso.md`, si hace falta.
