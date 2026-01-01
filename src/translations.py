"""
Configuración de idiomas y traducciones
"""

LANGUAGES = {
    'es': {
        'name': 'Español',
        'prompt_language': 'español',
        'sections': {
            'title': 'SECCIÓN D: DESCRIPCIÓN DEL ENFOQUE, METODOLOGÍA Y PLAN DE TRABAJO',
            'context': 'Comprensión del Contexto',
            'principles': 'Nuestros Principios Rectores',
            'approach': 'Enfoque Técnico y Metodología',
            'workplan': 'Plan de Trabajo',
            'team': 'Organización del Equipo',
            'risks': 'Gestión de Riesgos',
            'quality': 'Aseguramiento de Calidad',
        },
        'principles_intro': 'Los siguientes principios clave sustentan nuestra estrategia propuesta, y surgen de nuestro análisis del contexto local así como de las necesidades específicas expresadas en los TdR.',
    },
    'en': {
        'name': 'English',
        'prompt_language': 'English',
        'sections': {
            'title': 'SECTION D: DESCRIPTION OF APPROACH, METHODOLOGY AND WORK PLAN',
            'context': 'Understanding of the Context',
            'principles': 'Our Guiding Principles',
            'approach': 'Technical Approach and Methodology',
            'workplan': 'Work Plan',
            'team': 'Team Organization',
            'risks': 'Risk Management',
            'quality': 'Quality Assurance',
        },
        'principles_intro': 'The following key principles underpin our proposed strategy, and stem from our analysis of the local context as well as the specific needs expressed in the ToR.',
    },
    'fr': {
        'name': 'Français',
        'prompt_language': 'français',
        'sections': {
            'title': 'SECTION D: DESCRIPTION DE L\'APPROCHE, MÉTHODOLOGIE ET PLAN DE TRAVAIL',
            'context': 'Compréhension du Contexte',
            'principles': 'Nos Principes Directeurs',
            'approach': 'Approche Technique et Méthodologie',
            'workplan': 'Plan de Travail',
            'team': 'Organisation de l\'Équipe',
            'risks': 'Gestion des Risques',
            'quality': 'Assurance Qualité',
        },
        'principles_intro': 'Les principes clés suivants sous-tendent notre stratégie proposée et découlent de notre analyse du contexte local ainsi que des besoins spécifiques exprimés dans les TdR.',
    },
    'pt': {
        'name': 'Português',
        'prompt_language': 'português',
        'sections': {
            'title': 'SEÇÃO D: DESCRIÇÃO DA ABORDAGEM, METODOLOGIA E PLANO DE TRABALHO',
            'context': 'Compreensão do Contexto',
            'principles': 'Nossos Princípios Orientadores',
            'approach': 'Abordagem Técnica e Metodologia',
            'workplan': 'Plano de Trabalho',
            'team': 'Organização da Equipe',
            'risks': 'Gestão de Riscos',
            'quality': 'Garantia de Qualidade',
        },
        'principles_intro': 'Os seguintes princípios-chave sustentam nossa estratégia proposta e decorrem de nossa análise do contexto local, bem como das necessidades específicas expressas nos TdR.',
    }
}


def get_language_config(lang_code: str) -> dict:
    """Retorna la configuración para el idioma especificado"""
    return LANGUAGES.get(lang_code, LANGUAGES['es'])
