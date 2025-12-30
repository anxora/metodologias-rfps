"""
Configuraciones de idioma y traducciones
"""

LANGUAGES = {
    'es': {
        'code': 'es',
        'name': 'Español',
        'sections': {
            'title': 'Enfoque Metodológico',
            'context': 'Comprensión del Contexto',
            'approach': 'Enfoque Metodológico',
            'workplan': 'Plan de Trabajo',
            'team': 'Organización del Equipo',
            'risks': 'Gestión de Riesgos',
            'quality': 'Aseguramiento de Calidad',
        },
        'prompt_language': 'español'
    },
    'en': {
        'code': 'en',
        'name': 'English',
        'sections': {
            'title': 'Methodological Approach',
            'context': 'Context Understanding',
            'approach': 'Methodological Approach',
            'workplan': 'Work Plan',
            'team': 'Team Organization',
            'risks': 'Risk Management',
            'quality': 'Quality Assurance',
        },
        'prompt_language': 'English'
    },
    'fr': {
        'code': 'fr',
        'name': 'Français',
        'sections': {
            'title': 'Approche Méthodologique',
            'context': 'Compréhension du Contexte',
            'approach': 'Approche Méthodologique',
            'workplan': 'Plan de Travail',
            'team': 'Organisation de l\'Équipe',
            'risks': 'Gestion des Risques',
            'quality': 'Assurance Qualité',
        },
        'prompt_language': 'français'
    },
    'pt': {
        'code': 'pt',
        'name': 'Português',
        'sections': {
            'title': 'Abordagem Metodológica',
            'context': 'Compreensão do Contexto',
            'approach': 'Abordagem Metodológica',
            'workplan': 'Plano de Trabalho',
            'team': 'Organização da Equipe',
            'risks': 'Gestão de Riscos',
            'quality': 'Garantia de Qualidade',
        },
        'prompt_language': 'português'
    }
}


def get_language_config(code: str) -> dict:
    """Obtiene la configuración de idioma"""
    return LANGUAGES.get(code, LANGUAGES['es'])


def get_available_languages() -> list:
    """Retorna lista de idiomas disponibles"""
    return [(code, lang['name']) for code, lang in LANGUAGES.items()]
