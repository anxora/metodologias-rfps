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
        "max_tokens": 16000,
        "temperature": 0.7
    }

    response = requests.post(url, json=payload, headers=headers, timeout=300)
    response.raise_for_status()

    result = response.json()
    response_text = result['choices'][0]['message']['content']

    # Extraer JSON de la respuesta
    try:
        start = response_text.find('{')
        end = response_text.rfind('}') + 1
        json_str = response_text[start:end]
        methodology = json.loads(json_str)
    except (json.JSONDecodeError, ValueError):
        methodology = _create_fallback_structure(response_text)

    return methodology


def _build_prompt(tdr_content: str, template: dict, sections: dict, language: str, methodology_type: str) -> str:
    """Construye el prompt específico para el tipo de metodología"""

    phases_list = '\n'.join([f"   - {phase}" for phase in template['phases']])

    prompt = f"""You are an expert consultant writing a methodology proposal. Analyze the following Terms of Reference (ToR) and generate a COMPLETE and DETAILED methodology approach for a development consulting proposal.

METHODOLOGY TYPE: {methodology_type.upper()} - {template['description']}

CRITICAL REQUIREMENTS:
- Generate ALL content in {language}.
- The final document MUST have 15-25 pages (approximately 6,000-8,000 words MINIMUM).
- Each section must be EXTENSIVE, DETAILED and professional with MULTIPLE PARAGRAPHS.
- Follow EXACTLY the phase structure indicated below.
- ADAPT all content specifically to this ToR - mention specific deliverables, stakeholders, and objectives from the ToR.
- For the Nigeria iDICE project: include NFI upgrade details, PPP Film Studios (Lagos + 100 mini-studios), AfDB compliance, etc.

ToR:
{tdr_content}

=== REQUIRED STRUCTURE ===

Generate a JSON with this EXACT structure. EACH field must be VERY DETAILED:

{{
    "introduction": "Introductory paragraph of 150-200 words explaining the overall approach specifically for this ToR",

    "context": "Understanding of Context (1000+ words MINIMUM): detailed analysis of geographic context (Nigeria, Lagos, Jos), institutional framework (BOI, PCU, NFI, NFC, Ministry), sectoral analysis (Nollywood, creative industries), problem statement, key actors and stakeholders, specific objectives from ToR, and regulatory/normative framework (AfDB guidelines, Nigerian PPP laws)",

    "principles": [
        {{
            "name": "Short principle name 1",
            "description": "Description of 80-100 words explaining the principle and how it applies to this specific project"
        }},
        {{
            "name": "Short principle name 2",
            "description": "Description of 80-100 words"
        }},
        {{
            "name": "Short principle name 3",
            "description": "Description of 80-100 words"
        }},
        {{
            "name": "Short principle name 4",
            "description": "Description of 80-100 words"
        }},
        {{
            "name": "Short principle name 5",
            "description": "Description of 80-100 words"
        }},
        {{
            "name": "Short principle name 6",
            "description": "Description of 80-100 words"
        }}
    ],

    "phases": [
{_build_phases_structure(template['phases'], methodology_type)}
    ],

    "risks": "Risk Management (800+ words MINIMUM): identification of risks by category (political, technical, financial, regulatory, environmental/social, procurement), probability and impact analysis, specific mitigation measures for each risk, contingency plan, risk allocation in PPP structure",

    "quality": "Quality Assurance (600+ words MINIMUM): quality management system, specific KPIs and indicators, monitoring mechanisms, evaluation framework, reporting protocols, compliance verification processes"
}}

=== PHASE INSTRUCTIONS ===

The phases MUST follow this EXACT structure:
{phases_list}

For EACH phase, include:
- title: Exact phase title
- description: General description of 200-300 words (DETAILED, not generic)
- start_week: Start week number (use WEEKS not months, project is 46 weeks / 11 months)
- end_week: End week number
- tasks: List of 4-6 tasks with:
  - code: Task code (e.g., "1A", "1B", "2A")
  - title: Task title specific to this ToR
  - description: DETAILED description of 250-350 words explaining methodology, tools, stakeholders involved
  - items: List of 5-7 specific activities or deliverables
  - start_week: Start week
  - end_week: End week
  - deliverable_week: Week of deliverable (if applicable)
- deliverables: List of phase deliverables with code and name (MUST match ToR deliverables)

SPECIFIC DELIVERABLES FROM THIS ToR (use these exact names):
A. Nigeria Film Institute:
- D1: Validation and Stakeholder Engagement Report (Week 6)
- D2: Comprehensive and Costed Action Plan (Week 8)
- D3: Design and Procurement Support Package (Week 12)

B. PPP Film Studios:
- D4: Inception Report (Week 4)
- D5: Draft Study Report (Week 12)
- D6: Final Study and Investment Vehicle Structuring Report (Week 16)
- D7: Procurement Documentation and Technical Support (Week 44)
- D8: Close-out and Final Closure Report (Week 46)

{_get_type_specific_instructions(methodology_type)}

CRITICAL REMINDERS:
- Content MUST be professional and SPECIFIC to this Nigeria iDICE/NFI/PPP Studios project
- Use COMPLETE, DEVELOPED paragraphs (not bullet points for descriptions)
- Tasks must have consecutive codes (1A, 1B, 1C for Phase 1; 2A, 2B for Phase 2, etc.)
- Use WEEKS (1-46) consistent with the 11-month project duration
- MINIMUM 6,000 words total - each phase description and task must be VERY detailed
- Include **bold markers** around key terms that should be emphasized
- Reference specific stakeholders: BOI, PCU, NFI, NFC, Federal Ministry of Arts Culture and Creative Economy, AfDB
- Reference specific outputs: feasibility study, financial models, BOQs, RFPs, PPP agreements
"""
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
