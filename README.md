# Proyecto Final - Sistemas Operativos

Este proyecto es parte de la materia **Sistemas Operativos** de la Universidad EIA. El objetivo del proyecto es crear un servicio usando **FastAPI** que reciba datos de un usuario, los almacene en archivos JSON, y luego respalde esos archivos en **AWS S3** de manera automatizada con cron jobs.

## Descripción

El servicio realizado en este proyecto incluye los siguientes componentes:

- **FastAPI**: Se creó un endpoint `POST` que recibe los siguientes datos:
  - **nombre**: El nombre del usuario.
  - **edad**: La edad del usuario.
  - **profesion**: La profesión del usuario.
  
  Los datos recibidos se almacenan en un archivo JSON en una carpeta específica en el sistema local.

- **AWS S3**: Los archivos JSON generados se respaldan automáticamente en un bucket de S3. Los archivos locales se eliminan después de ser respaldados.

- **Automatización con Cron**: Se configura un cron job que ejecuta el respaldo de los archivos JSON de manera diaria, usando AWS CLI para copiar los archivos al bucket de S3 y luego eliminar los archivos locales.

## Tecnologías

- **FastAPI**: Framework para crear APIs rápidas y eficientes en Python.
- **AWS S3**: Servicio de almacenamiento en la nube que se usa para respaldar los archivos generados.
- **Cron**: Herramienta de Linux para programar tareas de manera automática. En este caso, se usa para programar el respaldo diario de los archivos JSON.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

- **Python 3.8+**
- **pip** para gestionar dependencias.
- **AWS CLI** configurado con tus credenciales de AWS.
- Un bucket de **AWS S3** donde se subirán los archivos JSON.

## Instalación y Uso

1. **Clonar el repositorio**:
   
   Clona el repositorio a tu máquina local con el siguiente comando:

   ```bash
   git clone https://github.com/SantiagoPA712/Final-SO.git
2. **Instalar las dependencias**:

Accede a la carpeta del proyecto y crea un entorno virtual (opcional pero recomendado):

cd Final-SO
python3 -m venv venv
source venv/bin/activate
Instala las dependencias necesarias:


pip install fastapi uvicorn boto3

3. **Configurar AWS CLI**:

Si aún no lo has hecho, configura AWS CLI con tus credenciales de AWS (Access Key ID y Secret Access Key) y selecciona la región correcta:

aws configure
Ejecutar el servidor FastAPI:

4.**Levanta el servidor FastAPI con el siguiente comando**:

uvicorn main:app --reload
El servidor se ejecutará en http://127.0.0.1:8000.

5.**Probar el endpoint**:

Envía una solicitud POST al endpoint /store_data/ con un cuerpo JSON, como este:

json

{
  "nombre": "Juan Pérez",
  "edad": 30,
  "profesion": "Ingeniero"
}
Puedes probarlo con herramientas como Postman o Swagger UI (en http://127.0.0.1:8000/docs).

6.**Configuración de Cron**:

El script backup_to_s3.sh está diseñado para respaldar los archivos JSON diariamente en tu bucket de S3 y luego eliminarlos localmente.

Para configurar el cron job, edita el archivo crontab:


crontab -e
Añade la siguiente línea para ejecutar el script a medianoche todos los días:


0 0 * * * /path/to/Final-SO/backup_to_s3.sh
Autor
Santiago Pérez: GitHub


### Instrucciones para el uso del archivo:

1. **Clonar el repositorio**: El archivo explica cómo clonar el repositorio desde GitHub.
2. **Instalación de dependencias**: Detalla cómo instalar los paquetes necesarios en un entorno virtual.
3. **Configuración de AWS**: Se indica cómo configurar AWS CLI para autenticarte correctamente.
4. **Instrucciones de ejecución**: Explica cómo correr el servidor FastAPI y cómo probar el endpoint.
5. **Configuración del Cron Job**: Incluye las instrucciones para programar el cron job que realizará los respaldos diarios.
