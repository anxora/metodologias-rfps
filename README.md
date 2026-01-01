# Metodologías RFPs

Generador de documentos Word con enfoques metodológicos para proyectos de consultoría de ayuda al desarrollo basados en Términos de Referencia (TdR/TOR).

## Descripción

Esta herramienta analiza Términos de Referencia (TdR) y genera automáticamente un documento Word con un enfoque metodológico estructurado para propuestas de consultoría en proyectos de cooperación al desarrollo.

El documento generado sigue el formato Aninver con:
- Estilos profesionales predefinidos
- Tablas de principios rectores con colores corporativos
- Tablas de actividades y timeline por fase
- Diagramas Gantt con colores de marca
- Cajas de entregables destacadas

## Características

- Análisis de TdR/TOR en múltiples formatos (PDF, DOCX, TXT)
- Generación automática de documentos Word de 15-25 páginas
- Soporte multiidioma (Español, Inglés, Francés, Portugués)
- **Tres tipos de metodología:**
  - **General**: Proyectos de estrategia, marketing, capacity building
  - **Feasibility**: Estudios de factibilidad con análisis financiero
  - **Info Systems**: Desarrollo de plataformas web, bases de datos, software
- Detección automática del tipo de metodología
- Formato Aninver con colores y estilos corporativos

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
# Detección automática del tipo de metodología
python main.py --tdr archivo_tdr.pdf --idioma en --output metodologia.docx

# Especificar tipo de metodología
python main.py --tdr archivo_tdr.pdf --tipo feasibility --idioma es --output estudio.docx

# Metodología de sistemas de información
python main.py --tdr archivo_tdr.pdf --tipo info_systems --idioma en --output platform.docx
```

### Opciones

| Opción | Descripción | Valores |
|--------|-------------|---------|
| `--tdr` | Archivo de Términos de Referencia | PDF, DOCX, TXT |
| `--idioma` | Idioma del documento de salida | `es`, `en`, `fr`, `pt` |
| `--tipo` | Tipo de metodología | `auto`, `general`, `feasibility`, `info_systems` |
| `--output` | Nombre del archivo de salida | *.docx |

## Tipos de Metodología

### General
Para proyectos de estrategia, marketing y capacity building:
- Phase 1: Project inception
- Phase 2: Situational analysis
- Phase 3: Strategy development
- Phase 4: Action plan and implementation

### Feasibility (Estudios de Factibilidad)
Para análisis de viabilidad de nuevas inversiones:
- Phase 1: Project inception
- Phase 2: Market, value chain & regulatory assessment
- Phase 3: Technical assessment and proposal
- Phase 4: Financial analysis
- Phase 5: Roadmap & Validation

### Info Systems (Sistemas de Información)
Para desarrollo de plataformas web y software:
- Phase 1: Inception Phase
- Phase 2: Analysis of platform requirements
- Phase 3: Design of Database and Mockups
- Phase 4: Development of the Platform
- Phase 5: Performance Testing
- Phase 6: Platform Documentation
- Phase 7: Platform Training
- Phase 8: Maintenance during warranty period

## Estructura del Documento Generado

1. **Título de Sección** - "SECTION D: DESCRIPTION OF APPROACH, METHODOLOGY AND WORK PLAN"
2. **Comprensión del Contexto** - Análisis del marco del proyecto
3. **Principios Rectores** - Tabla con 3-6 principios con colores corporativos
4. **Enfoque Técnico y Metodología** - Fases con:
   - Descripción de la fase
   - Tabla de Activities/Timeline
   - Detalle de cada tarea (código, descripción, items)
   - Tabla Gantt con cronograma
   - Cajas de entregables
5. **Gestión de Riesgos** - Identificación y mitigación
6. **Aseguramiento de Calidad** - Mecanismos de control

## Colores del Formato Aninver

| Elemento | Color | Hex |
|----------|-------|-----|
| Header Principios | Azul claro | #BDD6EE |
| Título Principio | Azul oscuro | #2E74B5 |
| Header Activities | Azul | #5B83DF |
| Body Activities | Gris claro | #F2F2F2 |
| Timeline | Verde/Teal | #00A798 |
| Gantt Activo | Amarillo | #FFC000 |
| Entregables | Amarillo claro | #FFF2CC |

## Licencia

MIT License
