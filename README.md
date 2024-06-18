# Vulnerability Report API

Con esta API se podra consultar a demanda el consolidado de las vulnerabilidades encontradas en la aplicación http://192.168.1.6:5000, junto con el impacto que podria generar dentro de una orgnaizacion y sus posibles remedicaciones, y las técnicas y tácticas relevantes de la matriz MITRE ATT&CK.

## Endpoints

- `GET /vulnerabilities`: Muestra un listado de todas las vulnerabilidades.
- `GET /vulnerabilities/<int:id>`: Muestra solo la vunerabilidad consultada por el ID.
- `POST /vulnerabilities`: Agrega una nueva vulnerabilidad.
- `DELETE /vulnerabilities/<int:id>`: Elimina una vulnerabilidad por su ID.

## Ejecución

1. Clona el repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta la aplicación: `python app.py`

La aplicación estará disponible en `http://localhost:5000`.

## Ejemplo de Entrada para POST /vulnerabilities

```json
{
  "name": "Nueva Vulnerabilidad",
  "description": "Descripción de la vulnerabilidad",
  "impact": "Impacto de la vulnerabilidad",
  "remediation":"Paso 1,Paso 2,",
  "mitre": "tactic: Defense Evasion,technique: T1070, url: https://attack.mitre.org/techniques/T1070/"
}
