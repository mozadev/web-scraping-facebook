ve# Facebook Marketplace Scraper

Un script en Python para automatizar la extracción de datos de Facebook Marketplace usando Selenium.

## 🚀 Características

- Login automático en Facebook
- Búsqueda automática de productos
- Extracción de datos (título, precio, ubicación)
- Manejo de sesiones y cookies
- Sistema de logging
- Manejo de errores y reintentos
- Exportación de datos a CSV/JSON

## 📋 Requisitos Previos

- Python 3.8 o superior
- Google Chrome
- ChromeDriver (se instalará automáticamente)

## 🔧 Instalación

1. Clonar el repositorio:
``` Git bash
git clone https://github.com/yourusername/facebook-marketplace-scraper.git
cd facebook-marketplace-scraper
```

2. Crear un entorno virtual:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
```bash
# Copiar el archivo de ejemplo
cp .env.example .env

# Editar .env con tu editor preferido y agregar tus credenciales
FACEBOOK_EMAIL=tu_email@ejemplo.com
FACEBOOK_PASSWORD=tu_contraseña
```

## 📦 Estructura del Proyecto

```
facebook_marketplace_scraper/
│
├── src/
│   ├── scrapers/
│   │   ├── __init__.py
│   │   └── facebook_scraper.py
│   │
│   ├── browser/
│   │   ├── __init__.py
│   │   └── setup.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── input_utils.py
│       └── logging_utils.py
│
├── config/
│   ├── __init__.py
│   └── selectors.py
│
├── output/
│   ├── data/
│   └── logs/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── main.py
```

## 🚀 Uso

1. Ejecutar el scraper:
```bash
python main.py
```

2. Los resultados se guardarán en:
- CSV: `output/data/results_[timestamp].csv`
- JSON: `output/data/results_[timestamp].json`
- Logs: `output/logs/scraping_[timestamp].log`

## ⚙️ Configuración

### Términos de búsqueda
Modificar la lista de términos en `main.py`:
```python
search_terms = [
    "laptop",
    "smartphone",
    "headphones"
]
```

### Cantidad de resultados
Modificar el límite de productos en `src/scrapers/facebook_scraper.py`:
```python
# Cambiar el número en products[:10] para obtener más o menos resultados
for product in products[:10]:
```

## 📝 Logs

Los logs se guardan en `output/logs/` con la siguiente información:
- Inicio y fin de cada búsqueda
- Productos encontrados
- Errores y excepciones
- Estado del proceso

## 🛠️ Solución de Problemas

### Error de Login
- Verificar credenciales en `.env`
- Comprobar conexión a internet
- Revisar si hay verificación de seguridad de Facebook

### No se encuentran productos
- Verificar los selectores en `config/selectors.py`
- Aumentar los tiempos de espera
- Revisar los logs para más detalles

### Errores de ChromeDriver
- Eliminar la carpeta `.wdm/` y dejar que se reinstale
- Actualizar Chrome a la última versión
- Verificar la compatibilidad de versiones

## 🔒 Seguridad

- No compartir el archivo `.env`
- No commitear credenciales
- Usar un entorno virtual
- Mantener el ChromeDriver actualizado

## 🤝 Contribuir

1. Fork el proyecto
2. Crear una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Crear un Pull Request

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## ✨ Agradecimientos

- Selenium WebDriver
- Python Community
- Contribuidores del proyecto

## 📞 Soporte

Si encuentras algún problema o tienes sugerencias, por favor abre un issue en el repositorio.