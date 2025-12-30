"""
Generador de metodología usando Claude API
"""

import os
import json
from anthropic import Anthropic


def generate_methodology(tdr_content: str, lang_config: dict) -> dict:
    """
    Genera el enfoque metodológico basado en el TdR usando Claude

    Args:
        tdr_content: Contenido del TdR
        lang_config: Configuración de idioma

    Returns:
        Diccionario con las secciones de la metodología
    """
    client = Anthropic()

    sections = lang_config['sections']
    language = lang_config['prompt_language']

    prompt = f"""Analiza los siguientes Términos de Referencia (TdR) y genera un enfoque metodológico
completo para una propuesta de consultoría de ayuda al desarrollo.

IMPORTANTE: Genera todo el contenido en {language}.

TdR:
{tdr_content}

Genera un documento estructurado con las siguientes secciones. Para cada sección, proporciona
contenido detallado y profesional apropiado para una propuesta técnica:

1. {sections['context']}: Demuestra comprensión profunda del contexto, problemática y objetivos del proyecto.

2. {sections['approach']}: Describe la estrategia metodológica general, principios rectores y marco conceptual.

3. {sections['workplan']}: Detalla las fases, actividades principales, entregables y cronograma propuesto.

4. {sections['team']}: Describe la organización del equipo, roles clave y mecanismos de coordinación.

5. {sections['risks']}: Identifica riesgos potenciales y propone medidas de mitigación.

6. {sections['quality']}: Describe los mecanismos de aseguramiento de calidad y seguimiento.

Responde en formato JSON con la siguiente estructura:
{{
    "context": "contenido de la sección...",
    "approach": "contenido de la sección...",
    "workplan": "contenido de la sección...",
    "team": "contenido de la sección...",
    "risks": "contenido de la sección...",
    "quality": "contenido de la sección..."
}}

Asegúrate de que cada sección sea detallada, profesional y específica al proyecto descrito en el TdR.
"""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response_text = message.content[0].text

    # Extraer JSON de la respuesta
    try:
        # Buscar el JSON en la respuesta
        start = response_text.find('{')
        end = response_text.rfind('}') + 1
        json_str = response_text[start:end]
        methodology = json.loads(json_str)
    except (json.JSONDecodeError, ValueError):
        # Si falla el parsing, crear estructura básica
        methodology = {
            "context": response_text,
            "approach": "",
            "workplan": "",
            "team": "",
            "risks": "",
            "quality": ""
        }

    return methodology
