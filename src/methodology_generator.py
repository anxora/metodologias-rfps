"""
Generador de metodología usando Perplexity API
"""

import os
import json
import requests


# Plantillas de fases por tipo de metodología
METHODOLOGY_TEMPLATES = {
    'general': {
        'phases': [
            'Phase 1: Project inception',
            'Phase 2: Situational analysis',
            'Phase 3: Strategy development',
            'Phase 4: Action plan and implementation',
        ],
        'description': 'General consulting methodology for strategy, marketing, and capacity building projects'
    },
    'feasibility': {
        'phases': [
            'Phase 1: Project inception',
            'Phase 2: Market, value chain & regulatory assessment',
            'Phase 3: Technical assessment and proposal',
            'Phase 4: Financial analysis',
            'Phase 5: Roadmap & Validation of the Feasibility Study',
        ],
        'description': 'Feasibility study methodology for assessing viability of new ventures or investments'
    },
    'info_systems': {
        'phases': [
            'Phase 1: Inception Phase',
            'Phase 2: Analysis of platform requirements',
            'Phase 3: Design of Database and Mockups',
            'Phase 4: Development of the Platform',
            'Phase 5: Performance Testing',
            'Phase 6: Platform Documentation',
            'Phase 7: Platform Training',
            'Phase 8: Maintenance during warranty period',
        ],
        'description': 'Information systems methodology for web platforms, databases, and software development'
    }
}


def detect_methodology_type(tdr_content: str) -> str:
    """
    Detecta automáticamente el tipo de metodología basado en el contenido del TdR

    Returns:
        'general', 'feasibility', o 'info_systems'
    """
    content_lower = tdr_content.lower()

    # Palabras clave para cada tipo
    feasibility_keywords = [
        'feasibility study', 'feasibility assessment', 'estudio de factibilidad',
        'viability', 'financial analysis', 'market assessment', 'business case',
        'investment analysis', 'cost-benefit', 'npv', 'irr', 'roi',
        'análisis financiero', 'viabilidad'
    ]

    info_systems_keywords = [
        'website', 'web platform', 'portal', 'database', 'software',
        'information system', 'application', 'app development', 'ux/ui',
        'user interface', 'frontend', 'backend', 'api', 'sistema de información',
        'plataforma web', 'base de datos', 'desarrollo de software'
    ]

    # Contar coincidencias
    feasibility_score = sum(1 for kw in feasibility_keywords if kw in content_lower)
    info_systems_score = sum(1 for kw in info_systems_keywords if kw in content_lower)

    if feasibility_score > info_systems_score and feasibility_score >= 2:
        return 'feasibility'
    elif info_systems_score > feasibility_score and info_systems_score >= 2:
        return 'info_systems'
    else:
        return 'general'


def generate_methodology(tdr_content: str, lang_config: dict, methodology_type: str = None) -> dict:
    """
    Genera el enfoque metodológico basado en el TdR usando Perplexity API

    Args:
        tdr_content: Contenido del TdR
        lang_config: Configuración de idioma
        methodology_type: Tipo de metodología ('general', 'feasibility', 'info_systems') o None para auto-detectar

    Returns:
        Diccionario con las secciones de la metodología estructurada
    """
    api_key = os.getenv('PERPLEXITY_API_KEY')
    if not api_key:
        raise ValueError("PERPLEXITY_API_KEY environment variable not set")

    # Auto-detectar tipo si no se especifica
    if methodology_type is None:
        methodology_type = detect_methodology_type(tdr_content)

    template = METHODOLOGY_TEMPLATES.get(methodology_type, METHODOLOGY_TEMPLATES['general'])
    sections = lang_config['sections']
    language = lang_config['prompt_language']

    prompt = _build_prompt(tdr_content, template, sections, language, methodology_type)

    # Llamar a Perplexity API
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 32000,
        "temperature": 0.5
    }

    response = requests.post(url, json=payload, headers=headers, timeout=300)
    response.raise_for_status()

    result = response.json()
    response_text = result['choices'][0]['message']['content']

    # Extraer JSON de la respuesta
    methodology = _parse_json_response(response_text)

    return methodology


def _parse_json_response(response_text: str) -> dict:
    """
    Parsea la respuesta de Perplexity, manejando bloques markdown y JSON malformado
    """
    import re

    # Remover bloques de código markdown ```json ... ```
    json_block_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', response_text)
    if json_block_match:
        json_str = json_block_match.group(1).strip()
    else:
        # Buscar JSON directo entre { y }
        start = response_text.find('{')
        end = response_text.rfind('}') + 1
        if start >= 0 and end > start:
            json_str = response_text[start:end]
        else:
            return _create_fallback_structure(response_text)

    # Intentar parsear el JSON
    try:
        methodology = json.loads(json_str)

        # Validar estructura mínima
        if not isinstance(methodology, dict):
            return _create_fallback_structure(response_text)

        # Asegurar que las claves principales existan
        if 'phases' not in methodology or not methodology['phases']:
            methodology['phases'] = []
        if 'principles' not in methodology or not methodology['principles']:
            methodology['principles'] = []

        return methodology

    except json.JSONDecodeError as e:
        # Intentar reparar JSON truncado
        try:
            # Agregar llaves/corchetes faltantes
            repaired = _repair_truncated_json(json_str)
            methodology = json.loads(repaired)
            return methodology
        except:
            pass

        return _create_fallback_structure(response_text)


def _repair_truncated_json(json_str: str) -> str:
    """Intenta reparar JSON truncado agregando caracteres de cierre faltantes"""
    # Contar llaves y corchetes abiertos
    open_braces = json_str.count('{') - json_str.count('}')
    open_brackets = json_str.count('[') - json_str.count(']')

    # Agregar comillas faltantes si hay string sin cerrar
    if json_str.rstrip().endswith('"') is False:
        # Buscar última comilla
        last_quote = json_str.rfind('"')
        if last_quote > 0:
            before_quote = json_str[:last_quote].rfind('"')
            if before_quote >= 0:
                # Hay un string abierto, cerrarlo
                json_str = json_str.rstrip()
                if not json_str.endswith('"'):
                    json_str += '"'

    # Cerrar corchetes y llaves
    json_str += ']' * open_brackets
    json_str += '}' * open_braces

    return json_str


def _build_prompt(tdr_content: str, template: dict, sections: dict, language: str, methodology_type: str) -> str:
    """Construye el prompt específico para el tipo de metodología"""

    phases_list = '\n'.join([f"   - {phase}" for phase in template['phases']])
    num_phases = len(template['phases'])

    prompt = f"""You are a senior development consultant. Based on the Terms of Reference below, generate a methodology proposal in JSON format.

INSTRUCTIONS:
1. Read the ToR carefully and extract: objectives, deliverables, timeline, stakeholders, and location
2. Generate content in {language}
3. Adapt ALL content specifically to this ToR
4. Return ONLY valid JSON (no markdown, no explanation)

ToR CONTENT:
{tdr_content[:12000]}

REQUIRED JSON STRUCTURE:

{{
    "introduction": "150-200 word introduction explaining your approach to this specific project",

    "context": "800-1000 word analysis including: project background, geographic context, institutional framework, stakeholders, problem statement, and objectives from the ToR",

    "principles": [
        {{"name": "Principle 1 name", "description": "80-100 word description relevant to this project"}},
        {{"name": "Principle 2 name", "description": "80-100 word description"}},
        {{"name": "Principle 3 name", "description": "80-100 word description"}},
        {{"name": "Principle 4 name", "description": "80-100 word description"}},
        {{"name": "Principle 5 name", "description": "80-100 word description"}},
        {{"name": "Principle 6 name", "description": "80-100 word description"}}
    ],

    "phases": [
        {{
            "title": "{template['phases'][0]}",
            "description": "200-300 word phase description",
            "start_week": 1,
            "end_week": 4,
            "tasks": [
                {{
                    "code": "1A",
                    "title": "Task title from ToR",
                    "description": "200-300 word task description with methodology and tools",
                    "items": ["Activity 1", "Activity 2", "Activity 3", "Activity 4", "Activity 5"],
                    "start_week": 1,
                    "end_week": 2,
                    "deliverable_week": 2
                }},
                {{
                    "code": "1B",
                    "title": "Second task title",
                    "description": "200-300 word description",
                    "items": ["Activity 1", "Activity 2", "Activity 3", "Activity 4"],
                    "start_week": 2,
                    "end_week": 4
                }}
            ],
            "deliverables": [{{"code": "D1", "name": "Deliverable name from ToR"}}]
        }}
    ],

    "risks": "600-800 word risk management section covering: risk categories, mitigation measures, and contingency plans",

    "quality": "400-600 word quality assurance section with KPIs, monitoring mechanisms, and reporting protocols"
}}

PHASES TO INCLUDE (generate ALL {num_phases} phases with 3-5 tasks each):
{phases_list}

Extract deliverables and milestones from the ToR and assign them to the appropriate phases.

RETURN ONLY THE JSON OBJECT, NO OTHER TEXT."""

    return prompt


def _build_phases_structure(phases: list, methodology_type: str) -> str:
    """Construye la estructura JSON de ejemplo para las fases"""
    examples = []

    for i, phase in enumerate(phases[:2], 1):  # Solo mostrar ejemplo de primeras 2 fases
        start_week = (i - 1) * 4 + 1
        end_week = i * 4
        examples.append(f'''        {{
            "title": "{phase}",
            "description": "DETAILED description of 200-300 words explaining the phase objectives, methodology, key activities, stakeholders involved, and expected outcomes specific to this ToR...",
            "start_week": {start_week},
            "end_week": {end_week},
            "tasks": [
                {{
                    "code": "{i}A",
                    "title": "First task title specific to ToR",
                    "description": "DETAILED description of 250-350 words explaining the task methodology, tools used, stakeholders consulted, data sources, analysis approach...",
                    "items": ["Specific activity 1", "Specific activity 2", "Specific activity 3", "Specific activity 4", "Specific activity 5"],
                    "start_week": {start_week},
                    "end_week": {start_week + 1},
                    "deliverable_week": {start_week + 1}
                }},
                {{
                    "code": "{i}B",
                    "title": "Second task title specific to ToR",
                    "description": "DETAILED description...",
                    "items": ["Activity 1", "Activity 2", "Activity 3", "Activity 4"],
                    "start_week": {start_week + 1},
                    "end_week": {end_week}
                }}
            ],
            "deliverables": [
                {{"code": "D{i}", "name": "Deliverable name from ToR"}}
            ]
        }}''')

    examples.append('        // ... continue with ALL remaining phases with same level of detail')
    return ',\n'.join(examples)


def _get_type_specific_instructions(methodology_type: str) -> str:
    """Retorna instrucciones específicas según el tipo de metodología"""

    if methodology_type == 'feasibility':
        return """
=== SPECIFIC INSTRUCTIONS FOR THIS FEASIBILITY/TRANSACTION ADVISORY PROJECT ===

This is a DUAL-TRACK project with TWO workstreams running in parallel:

WORKSTREAM A - NIGERIA FILM INSTITUTE (NFI) UPGRADE:
- Phase 1: Validation with NFI, Federal Ministry, NFC, private sector stakeholders
- Phase 2: Develop comprehensive costed action plan (technology, infrastructure, human capacity, partnerships, financial sustainability)
- Phase 3: Technical Design, BOQs, and Procurement Documents for NFI upgrade

WORKSTREAM B - PPP FILM STUDIOS (Lagos State-of-Art Studio + 100 Regional Mini-Studios):
- Phase 1: Inception with stakeholder mapping, document review, engagement plan
- Phase 2: Comprehensive feasibility study with public sector comparator, PPP/investment reference models
  - Full project cycle costs, affordability limits, risks and costs
  - Value-for-money analysis, financial sustainability
  - Market analysis for creative sector in Nigeria
- Phase 3: Project structuring (PPP/SPV), financial models, governance frameworks
- Phase 4: Procurement documentation (RFPs, TORs, ITTs, evaluation criteria)
- Phase 5: Advisory for private partner procurement, contract negotiation, financial close
- Phase 6: Close-out report and PPP management plan

FINANCIAL ANALYSIS MUST INCLUDE:
- CAPEX and OPEX projections for studio infrastructure
- Revenue models (studio rentals, production services, training fees)
- NPV, IRR, payback period calculations
- Sensitivity analysis (±20% on key variables)
- Risk-adjusted returns and risk allocation matrix

COMPLIANCE REQUIREMENTS:
- AfDB procurement guidelines and eligibility criteria
- Nigerian PPP laws (ICRC Act 2005, National PPP Policy)
- Environmental and Social Impact Assessment (ESIA/ESMP)
- Gender equity and youth employment considerations
"""

    elif methodology_type == 'info_systems':
        return """
=== INSTRUCCIONES ESPECÍFICAS PARA INFORMATION SYSTEMS ===

- Phase 2 debe incluir: mapeo de stakeholders, consultas, análisis de requisitos funcionales y no funcionales
- Phase 3 debe cubrir: arquitectura del sistema, diseño de base de datos, wireframes, mockups, user journeys
- Phase 4 debe incluir: selección de tecnología, desarrollo frontend/backend, integración de APIs
- Phase 5 debe cubrir: UAT, pruebas de rendimiento, despliegue en producción
- Phase 6: documentación técnica y manuales de usuario
- Phase 7: materiales de capacitación, sesiones de training, informe de capacitación
- Phase 8: soporte post-implementación, corrección de bugs, mantenimiento
- Los entregables deben incluir: Inception Report, Requirements Document, Design Document, Platform/Website, Testing Report, Documentation, Training Materials
"""

    else:  # general
        return """
=== INSTRUCCIONES ESPECÍFICAS PARA METODOLOGÍA GENERAL ===

- Phase 2 (Situational Analysis) debe incluir: análisis de mercado, benchmark, investigación primaria y secundaria
- Phase 3 (Strategy Development) debe cubrir: talleres de visión, desarrollo de estrategia, validación
- Phase 4 (Action Plan) debe incluir: plan de acción detallado, presupuesto, responsabilidades, cronograma
- Incluir análisis FODA
- Los entregables deben incluir: Inception Report, Situational Analysis Report, Draft Strategy, Final Strategy and Action Plan
"""


def _create_fallback_structure(response_text: str) -> dict:
    """Crea una estructura básica si falla el parsing JSON"""
    return {
        "introduction": "",
        "context": response_text[:2000] if len(response_text) > 2000 else response_text,
        "principles": [
            {"name": "Principle 1", "description": ""},
            {"name": "Principle 2", "description": ""},
            {"name": "Principle 3", "description": ""}
        ],
        "phases": [],
        "risks": "",
        "quality": ""
    }
