# Metodologías RFPs

Generador de documentos Word con enfoques metodológicos para proyectos de consultoría de ayuda al desarrollo basados en Términos de Referencia (TdR/TOR).

## Descripción

Esta herramienta analiza Términos de Referencia (TdR) y genera automáticamente un documento Word con un enfoque metodológico estructurado para propuestas de consultoría en proyectos de cooperación al desarrollo.

## Características

- Análisis de TdR/TOR en múltiples formatos
- Generación automática de documentos Word
- Soporte multiidioma (Español, Inglés, Francés, Portugués)
- Estructura metodológica adaptable según tipo de proyecto

## Instalación

```bash
pip install -r requirements.txt
```

## Configuración

Crea un archivo `.env` con tu API key de Anthropic:

```
ANTHROPIC_API_KEY=tu_api_key_aqui
```

## Uso

```bash
python main.py --tdr archivo_tdr.pdf --idioma es --output metodologia.docx
```

### Opciones

- `--tdr`: Archivo de Términos de Referencia (PDF, DOCX, TXT)
- `--idioma`: Idioma del documento de salida (es, en, fr, pt)
- `--output`: Nombre del archivo de salida

## Estructura del Documento Generado

1. **Comprensión del Contexto** - Análisis del marco del proyecto
2. **Enfoque Metodológico** - Estrategia general de intervención
3. **Plan de Trabajo** - Fases y actividades
4. **Organización del Equipo** - Roles y responsabilidades
5. **Gestión de Riesgos** - Identificación y mitigación
6. **Aseguramiento de Calidad** - Mecanismos de control

## Licencia

MIT License
