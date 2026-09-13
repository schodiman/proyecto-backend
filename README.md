Plataforma de Noticias - Backend Django

Descripción del Proyecto
Este proyecto corresponde a la base técnica del backend para un medio digital. El sistema digitalizará la gestión de publicaciones periodísticas, permitiendo centralizar la información, manejar roles de usuario (Autores y Lectores) y controlar los estados de las publicaciones para futuras auditorías.

Actualmente, el proyecto cuenta con:
Núcleo de Django configurado.
Aplicación principal registrada.
Vista de bienvenida personalizada.
Manejo de error 404 personalizado.
Instrucciones de Instalación y Ejecución

Proyecto: 

1. Creación del Ambiente Virtual
Es una buena práctica mantener aislada toda la configuración de nuestro proyecto. Para crear el ambiente virtual, abre una terminal en la raíz del proyecto y ejecuta:
python -m venv nombre_ambiente

(Nota: La carpeta nombre_ambiente está excluida del repositorio mediante el archivo .gitignore).
2. Activación del Ambiente Virtual
Debemos activar el entorno antes de instalar las dependencias. Ejecuta el siguiente comando (en Windows):
.\nombre_ambiente\Scripts\activate


Si tienes problemas de restricciones de seguridad en PowerShell, ejecuta primero:
Set-ExecutionPolicy Bypass -Scope CurrentUser
3. Actualización de PIP e Instalación de Dependencias
Asegúrate de tener la última versión del gestor de paquetes:
python -m pip install --upgrade pip


Luego, instala todas las librerías necesarias (incluyendo Django) que están registradas en el archivo del proyecto:
pip install -r requirements.txt


4. Ejecución del Servidor Local
Una vez instaladas las dependencias, inicia el servidor de desarrollo de Django con el siguiente comando:
python manage.py runserver


El servidor se iniciará en http://127.0.0.1:8000/. Al ingresar a esta URL, podrás ver la página de bienvenida personalizada del proyecto.
5. Verificación de Error 404
El sistema está configurado para manejar errores 404 (recursos no encontrados). Puedes verificarlo intentando acceder a una ruta inexistente, por ejemplo:
http://127.0.0.1:8000/ruta-falsa/

