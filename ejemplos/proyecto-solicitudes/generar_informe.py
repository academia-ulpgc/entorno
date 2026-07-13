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
lineas.append(f"- Tiempo medio de respuesta: {media_dias:.1f} días")
lineas.append("")
lineas.append("## Solicitudes por estado")
lineas.append("")

for estado, cantidad in por_estado.items():
    lineas.append(f"- {estado}: {cantidad}")

lineas.append("")
lineas.append("## Solicitudes por área")
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
