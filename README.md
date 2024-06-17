# Vulnerability Report API

Esta API permite consultar un consolidado de vulnerabilidades encontradas en una aplicación web, junto con las recomendaciones para mitigarlas, y las técnicas y tácticas relevantes de la matriz MITRE ATT&CK.

## Endpoints

- `GET /vulnerabilities`: Devuelve una lista de todas las vulnerabilidades.
- `GET /vulnerabilities/<int:id>`: Devuelve una vulnerabilidad específica por su ID.
- `POST /vulnerabilities`: Añade una nueva vulnerabilidad.
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