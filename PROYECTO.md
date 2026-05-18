# Farmacy — Documentación del Proyecto

Aplicación web de inventario de medicamentos construida con Django 6. Muestra un catálogo de 50 medicamentos con nombre, concentración y cantidad disponible, con búsqueda en tiempo real.

---

## Cómo ejecutar el proyecto

### 1. Activar el entorno virtual

```bash
venv\Scripts\activate
```

Verás el prefijo `(venv)` en tu terminal indicando que el entorno está activo.

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

Solo es necesario la primera vez, o cuando el archivo `requirements.txt` cambie.

### 3. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

El servidor quedará corriendo en `http://127.0.0.1:8000/`.

### 4. Abrir la aplicación

Abre tu navegador y entra a:

- **Aplicación principal:** http://127.0.0.1:8000/
- **Panel de administración:** http://127.0.0.1:8000/admin/

Para detener el servidor presiona `Ctrl + C`.

---

## Estructura del proyecto

```
Jorge/
├── manage.py                        # Punto de entrada de comandos Django
├── requirements.txt                 # Dependencias del proyecto
├── db.sqlite3                       # Base de datos SQLite (generada automáticamente)
├── venv/                            # Entorno virtual de Python
└── farmacy/                         # Paquete principal de la aplicación
    ├── __init__.py
    ├── settings.py                  # Configuración global de Django
    ├── urls.py                      # Definición de rutas URL
    ├── views.py                     # Lógica de las vistas
    ├── apps.py                      # Configuración de la app
    ├── database.py                  # Datos de los medicamentos
    ├── wsgi.py                      # Entrada para servidores WSGI (producción)
    ├── asgi.py                      # Entrada para servidores ASGI (async)
    └── templates/
        └── farmacy/
            └── index.html           # Plantilla HTML de la página principal
```

---

## Explicación de cada archivo

### `manage.py`

Es el punto de entrada para todos los comandos administrativos de Django. No contiene lógica de negocio; su único rol es configurar el entorno y delegar comandos al framework.

Comandos más usados:

| Comando | Qué hace |
|---|---|
| `python manage.py runserver` | Inicia el servidor de desarrollo |
| `python manage.py migrate` | Aplica migraciones a la base de datos |
| `python manage.py createsuperuser` | Crea un usuario administrador |
| `python manage.py shell` | Abre una consola interactiva de Python con el contexto de Django |

---

### `requirements.txt`

Lista las dependencias exactas del proyecto con sus versiones. Garantiza que cualquier persona que clone el proyecto instale exactamente las mismas versiones.

| Paquete | Versión | Para qué sirve |
|---|---|---|
| Django | 6.0.4 | Framework web principal |
| asgiref | 3.11.1 | Soporte para servidores ASGI/async |
| sqlparse | 0.5.5 | Formateo de consultas SQL (usado internamente por Django) |
| colorama | 0.4.6 | Colores en la terminal (mensajes del servidor) |
| tzdata | 2026.1 | Base de datos de zonas horarias |

---

### `farmacy/settings.py`

Archivo central de configuración de Django. Controla el comportamiento de toda la aplicación.

**Puntos clave:**

- `DEBUG = True` — Activa el modo de desarrollo. Muestra errores detallados en el navegador. **Debe ser `False` en producción.**
- `SECRET_KEY` — Clave criptográfica usada para firmar sesiones y tokens. Debe mantenerse secreta y fuera del código en producción.
- `INSTALLED_APPS` — Lista las apps activas. Incluye las apps de Django (admin, auth, etc.) y la app propia `farmacy`.
- `DATABASES` — Configura SQLite como base de datos. En desarrollo es suficiente; en producción se usaría PostgreSQL o similar.
- `TEMPLATES` — Le indica a Django dónde buscar las plantillas HTML (`APP_DIRS = True` las busca dentro de cada app).
- `LANGUAGE_CODE = 'en-us'` y `TIME_ZONE = 'UTC'` — Configuración de idioma y zona horaria del sistema.

---

### `farmacy/urls.py`

Define el mapa de rutas de la aplicación: qué URL llama a qué vista.

```
/           →  views.index   (página principal con el catálogo)
/login/     →  views.login_view (página de acceso simulado)
/admin/     →  admin.site    (panel de administración de Django)
```

Cada vez que se agrega una nueva página a la aplicación, se registra aquí una nueva ruta.

---

### `farmacy/views.py`

Contiene la lógica que responde a las peticiones HTTP. Actualmente tiene estas funciones principales:

**`quitar_tildes(texto)`** — Función de apoyo que utiliza la librería `unicodedata` para limpiar los acentos y tildes del texto, permitiendo que las búsquedas sean más flexibles y fáciles para el usuario.

**`index(request)`** — Lee el parámetro `q` de la URL (ej. `/?q=amox`), filtra la lista de medicamentos cuyo nombre contenga ese texto ignorando mayúsculas y tildes, y envía los resultados a la plantilla. Si no hay búsqueda activa, envía todos los medicamentos. También pasa el total del catálogo y el término buscado para que la plantilla pueda mostrar el contador de resultados.

**`login_view(request)`** — Vista básica de inicio de sesión que valida si el usuario es `admin` y la contraseña `admin123`. Si son correctos, redirige al inicio; si no, muestra un error.

---

### `farmacy/database.py`

Almacena el inventario de medicamentos directamente en memoria como una lista de diccionarios Python. No usa una tabla en la base de datos.

Cada medicamento tiene tres campos:

| Campo | Descripción | Ejemplo |
|---|---|---|
| `nombre` | Nombre del medicamento | `"Amoxicilina"` |
| `concentracion` | Dosis o presentación | `"500 mg"` |
| `cantidad` | Unidades en existencia | `120` (o `0` si agotado) |

El catálogo tiene 50 medicamentos. Los que tienen `cantidad = 0` se muestran como **"Agotado"** en la interfaz.

> **Nota:** Al ser datos en memoria, cualquier cambio en este archivo requiere reiniciar el servidor para verse reflejado.

---

### `farmacy/apps.py`

Archivo de configuración de la app `farmacy` dentro del sistema de apps de Django. Define el nombre de la app y el tipo de campo de clave primaria por defecto (`BigAutoField`, un entero de 64 bits). Django lo usa internamente para registrar la app correctamente.

---

### `farmacy/wsgi.py`

Punto de entrada para servidores de producción que usen el protocolo **WSGI** (Web Server Gateway Interface), como Gunicorn o uWSGI. No se usa en desarrollo; `runserver` lo ignora.

---

### `farmacy/asgi.py`

Punto de entrada para servidores que usen el protocolo **ASGI** (Asynchronous Server Gateway Interface), como Daphne o Uvicorn. Permite manejar conexiones asíncronas (WebSockets, HTTP/2). No se usa en el desarrollo actual del proyecto.

---

### `farmacy/templates/farmacy/index.html`

Plantilla HTML de la única página de la aplicación. Combina HTML y CSS en un solo archivo, sin JavaScript.

**Qué hace cada parte:**

- **HTML** — Estructura la página: encabezado con título, formulario de búsqueda, cuadrícula de tarjetas de medicamentos. El formulario usa `method="get"` para enviar el término de búsqueda al servidor como parámetro en la URL (`?q=...`).
- **CSS (embebido)** — Estilos de la interfaz: diseño de tarjetas en cuadrícula responsiva, colores, badges de estado (verde = disponible, rojo = agotado).
- **Template tags de Django** — `{% for m in medicamentos %}` itera sobre los resultados ya filtrados por la vista; `{% if m.cantidad == 0 %}` decide si mostrar "Agotado" o la cantidad disponible; `{% if not medicamentos %}` muestra un mensaje cuando la búsqueda no arroja resultados.

---

## Cómo funciona la búsqueda

La búsqueda está manejada completamente por el servidor (backend). No hay JavaScript involucrado.

### Paso a paso

**1. El usuario escribe en el buscador y presiona Enter**

El formulario en `index.html` tiene `method="get"`, lo que significa que al enviarse, el navegador agrega el texto escrito a la URL:

```
http://127.0.0.1:8000/?q=amox
```

**2. El navegador hace una petición GET al servidor**

Django recibe esa petición con el parámetro `q` incluido en la URL.

**3. La vista lee el parámetro y filtra los datos (backend)**

En `views.py`:

```python
query = request.GET.get('q', '').strip()
query_norm = quitar_tildes(query.lower())
resultados = [m for m in medicamentos if query_norm in quitar_tildes(m['nombre'].lower())]
```

- `request.GET.get('q', '')` extrae el valor de `q` de la URL. Si no existe, usa `''`.
- A través de la función `quitar_tildes()` y `.lower()`, se eliminan los acentos y se pasa a minúscula tanto lo que busca el usuario como el nombre en la base de datos.
- La lista por comprensión recorre los 50 medicamentos y conserva solo los que coinciden con la búsqueda.
- Si no hay búsqueda activa (`q` vacío), devuelve todos los medicamentos.

**4. La vista envía los resultados a la plantilla**

```python
return render(request, 'farmacy/index.html', {
    'medicamentos': resultados,   # lista ya filtrada
    'total': len(medicamentos),   # total del catálogo (siempre 50)
    'query': query,               # texto buscado, para mostrarlo en el input
})
```

**5. La plantilla muestra los resultados (frontend)**

`index.html` recibe la lista ya filtrada y simplemente la dibuja:

```html
{% for m in medicamentos %}
  <!-- muestra cada tarjeta -->
{% endfor %}

{% if not medicamentos %}
  <div class="no-results">No se encontraron medicamentos.</div>
{% endif %}
```

El contador de resultados también se calcula en la plantilla con los datos que llegaron del servidor:

```html
{% if query %}
  {{ medicamentos|length }} de {{ total }} medicamentos
{% else %}
  {{ total }} medicamentos
{% endif %}
```

### Resumen visual

```
[Usuario escribe "amox" y presiona Enter]
             │
             ▼
    Navegador envía:  GET /?q=amox
             │
             ▼
    views.py filtra:  [m for m in medicamentos if "amox" in m['nombre'].lower()]
             │
             ▼
    Resultado:  [{"nombre": "Amoxicilina", ...}]
             │
             ▼
    index.html dibuja solo las tarjetas que llegaron del servidor
             │
             ▼
    [Usuario ve: "1 de 50 medicamentos"]
```

---

## Flujo de una petición

```
Navegador
   │
   │  GET http://127.0.0.1:8000/?q=amox
   ▼
urls.py          →  encuentra la ruta '/'  →  llama a views.index()
   │
views.py         →  lee el parámetro 'q', filtra medicamentos en database.py
   │
index.html       →  renderiza la plantilla con los resultados ya filtrados
   │
   ▼
Respuesta HTML enviada al navegador
```
