# SIBUME


Aplicación web de inventario de medicamentos construida con Django. Muestra un catálogo de medicamentos con nombre, concentración y cantidad disponible, permitiendo una búsqueda en tiempo real.

## Tecnologías Utilizadas
* Python 3
* Django
* HTML5 / CSS

## Cómo ejecutar el proyecto localmente

1. **Clonar el repositorio:**
   
   git clone [https://github.com/emelita12/SIBUME.git](https://github.com/emelita12/SIBUME.git)

 

2. **Crear y activar el entorno virtual**
 
 python -m venv venv
.\\venv\\Scripts\\activate 

3. **Instalar dependencias**
   pip install -r requirements.txt

4. **Iniciar el servidor**
   python manage.py runserver


## ESTRUCTURA DEL PROYECTO

Jorge/
├── manage.py                        # Punto de entrada de comandos Django
├── requirements.txt                 # Dependencias del proyecto
├── db.sqlite3                       # Base de datos SQLite
├── venv/                            # Entorno virtual de Python
└── farmacy/                         # Paquete principal de la aplicación
    ├── settings.py                  # Configuración global de Django
    ├── urls.py                      # Definición de rutas URL
    ├── views.py                     # Lógica de las vistas y motor de búsqueda
    ├── database.py                  # Base de datos en memoria (Catálogo de 50 medicamentos)
    └── templates/farmacy/
        └── index.html               # Plantilla HTML y CSS de la página principal



   
