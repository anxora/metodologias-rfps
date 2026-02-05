#!/usr/bin/env python3
"""
Generador de metodología para P2-P2RS Senegal - Versión 2
Con mejor manejo del parsing de respuesta de Perplexity
"""

import os
import sys
import json
import re
import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from document_writer import create_word_document
from translations import get_language_config


TDR_CONTENT = """
TERMES DE RÉFÉRENCE - PROJET P2-P2RS SÉNÉGAL
Opérateur de Proximité (OPP) pour l'Accompagnement des Comités de Gestion Concertée des Ressources Naturelles

I. CONTEXTE DU PROJET

La Banque Africaine de Développement (BAD) a initié depuis 2014 le Programme régional de résilience à l'insécurité alimentaire et nutritionnelle au Sahel (P2RS). Le Programme vise à:
- Contribuer à la réduction de la pauvreté et à l'amélioration de la sécurité alimentaire et nutritionnelle au Sahel
- Accroître, sur une base durable, la productivité et les productions agro-sylvo-pastorales et halieutiques

Le P2-P2RS intervient dans 15 communes situées dans 5 départements et 3 régions:
- Région de Tambacounda: Département de Bakel (Bellé, Sinthiou Fissa, Gabou, Gathiary)
- Région de Matam: Départements de Matam (Agnam Civol, Dabia, Bokidiawé, Nguidjilone) et Kanel (Aouré, Orkadjiéré, Sinthiou Bamambé, Ndendory)
- Région de Fatick: Départements de Fatick (Fimela) et Foundiougne (Bassoul, Djirnda)

II. COMPOSANTES DU PROJET
i. Renforcement de la résilience aux Changements Climatiques des productions agro-sylvo-pastorales
ii. Développement des chaînes de valeur agro-sylvo-pastorales et halieutiques
iii. Renforcement des capacités adaptatives aux changements climatiques
iv. Coordination et gestion du programme

III. OBJECTIFS DE LA MISSION

Objectif général: Appui à l'opérationnalisation des Comités de Gestion Concertée des Ressources Naturelles (CGC/RN), formation des acteurs à la gestion durable des ressources naturelles et des bonnes pratiques de GDT/agroécologie, et appui à la mise en œuvre du Mécanisme de Gestion des Plaintes (MGP).

Objectifs spécifiques:

Pour l'opérationnalisation des CGC/RN:
- Engager des études diagnostiques socioéconomiques des villages ciblés
- Identifier les principaux organismes exploitants (agriculture, élevage, foresterie)
- Analyser les perceptions des populations sur les ressources naturelles locales
- Inventorier les stratégies endogènes de gestion des ressources naturelles
- Négocier les règles de gestion concertées des ressources naturelles
- Appuyer l'élaboration et la mise en œuvre des conventions locales
- Mettre en place ou redynamiser les CGC/RN

Pour la formation des acteurs:
- Proposer un plan de renforcement des capacités (GDT, agroécologie, agroforesterie, RNA)
- Former les CGC sur les techniques de conservation et restauration des terres
- Accompagner les CGC sur la mise en œuvre des connaissances acquises

Pour le Mécanisme de Gestion des Plaintes:
- Informer et sensibiliser sur la politique de gestion des plaintes
- Aider à l'installation des comités de gestion des plaintes
- Vulgariser le MGP auprès des parties prenantes

IV. ÉQUIPE REQUISE
- Chef de mission/Superviseur (BAC+5, 15 ans d'expérience): 24 H/M
- Technicien GRN/agroécologie: 24 H/M
- Technicien GDT: 24 H/M
- Responsable MGP: 24 H/M
- Animateurs locaux: 13 personnes (6 Matam, 4 Tamba, 3 Fatick)

V. DURÉE: 24 mois
"""


def generate_methodology_v2(tdr_content: str, lang_config: dict) -> dict:
    """Genera metodología usando Perplexity API con mejor parsing"""

    api_key = os.environ.get('PERPLEXITY_API_KEY')
    if not api_key:
        raise ValueError("PERPLEXITY_API_KEY not set")

    language = lang_config['prompt_language']

    prompt = f"""Tu es un consultant senior en développement rural. Génère une méthodologie complète en français pour ce projet.

TERMES DE RÉFÉRENCE:
{tdr_content}

Génère UNIQUEMENT un objet JSON valide avec cette structure exacte (pas de texte avant ou après):

{{
    "introduction": "Introduction de 150-200 mots présentant l'approche globale pour ce projet P2-P2RS au Sénégal",

    "context": "Analyse de contexte de 800-1000 mots incluant: contexte du programme P2RS, zones d'intervention (Matam, Tambacounda, Fatick), cadre institutionnel, parties prenantes, problématique et objectifs",

    "principles": [
        {{"name": "Approche participative", "description": "Description de 80-100 mots sur la participation communautaire"}},
        {{"name": "Ancrage local", "description": "Description de 80-100 mots sur les savoirs endogènes"}},
        {{"name": "Équité genre", "description": "Description de 80-100 mots sur l'inclusion des femmes"}},
        {{"name": "Durabilité", "description": "Description de 80-100 mots sur la pérennité des actions"}},
        {{"name": "Coordination", "description": "Description de 80-100 mots sur les synergies"}},
        {{"name": "Apprentissage par l'action", "description": "Description de 80-100 mots sur les champs écoles"}}
    ],

    "phases": [
        {{
            "title": "Phase 1: Démarrage et Diagnostic Participatif",
            "description": "Description de 200-300 mots de cette phase de 4 mois",
            "start_week": 1,
            "end_week": 16,
            "tasks": [
                {{
                    "code": "1A",
                    "title": "Installation et cadrage méthodologique",
                    "description": "Description détaillée de 200 mots",
                    "items": ["Activité 1", "Activité 2", "Activité 3", "Activité 4", "Activité 5"],
                    "start_week": 1,
                    "end_week": 4,
                    "deliverable_week": 4,
                    "deliverable_code": "L1"
                }},
                {{
                    "code": "1B",
                    "title": "Études diagnostiques socioéconomiques",
                    "description": "Description détaillée de 200 mots",
                    "items": ["Activité 1", "Activité 2", "Activité 3", "Activité 4"],
                    "start_week": 3,
                    "end_week": 12
                }},
                {{
                    "code": "1C",
                    "title": "Restitution et validation",
                    "description": "Description détaillée de 150 mots",
                    "items": ["Activité 1", "Activité 2", "Activité 3"],
                    "start_week": 13,
                    "end_week": 16,
                    "deliverable_week": 16,
                    "deliverable_code": "L2"
                }}
            ],
            "deliverables": [
                {{"code": "L1", "name": "Rapport d'établissement"}},
                {{"code": "L2", "name": "Rapports de diagnostic des 15 communes"}}
            ]
        }},
        {{
            "title": "Phase 2: Mise en Place des CGC/RN",
            "description": "Description de 200-300 mots de cette phase de 6 mois",
            "start_week": 17,
            "end_week": 40,
            "tasks": [
                {{
                    "code": "2A",
                    "title": "Sensibilisation communautaire",
                    "description": "Description détaillée",
                    "items": ["Activité 1", "Activité 2", "Activité 3", "Activité 4"],
                    "start_week": 17,
                    "end_week": 24
                }},
                {{
                    "code": "2B",
                    "title": "Constitution des CGC/RN",
                    "description": "Description détaillée",
                    "items": ["Activité 1", "Activité 2", "Activité 3", "Activité 4"],
                    "start_week": 22,
                    "end_week": 32
                }},
                {{
                    "code": "2C",
                    "title": "Élaboration des conventions locales",
                    "description": "Description détaillée",
                    "items": ["Activité 1", "Activité 2", "Activité 3"],
                    "start_week": 28,
                    "end_week": 40,
                    "deliverable_week": 40,
                    "deliverable_code": "L3"
                }}
            ],
            "deliverables": [
                {{"code": "L3", "name": "15 CGC/RN opérationnels avec conventions locales"}}
            ]
        }},
        {{
            "title": "Phase 3: Formation et Renforcement des Capacités",
            "description": "Description de 200-300 mots",
            "start_week": 24,
            "end_week": 72,
            "tasks": [
                {{
                    "code": "3A",
                    "title": "Plan de renforcement des capacités",
                    "description": "Description détaillée",
                    "items": ["Activité 1", "Activité 2", "Activité 3"],
                    "start_week": 24,
                    "end_week": 28,
                    "deliverable_week": 28,
                    "deliverable_code": "L4"
                }},
                {{
                    "code": "3B",
                    "title": "Formation des formateurs",
                    "description": "Description détaillée",
                    "items": ["Activité 1", "Activité 2", "Activité 3", "Activité 4"],
                    "start_week": 28,
                    "end_week": 36
                }},
                {{
                    "code": "3C",
                    "title": "Formation des CGC/RN et producteurs",
                    "description": "Description détaillée",
                    "items": ["Activité 1", "Activité 2", "Activité 3", "Activité 4"],
                    "start_week": 36,
                    "end_week": 72,
                    "deliverable_week": 72,
                    "deliverable_code": "L5"
                }}
            ],
            "deliverables": [
                {{"code": "L4", "name": "Plan de renforcement des capacités"}},
                {{"code": "L5", "name": "Rapport de formation"}}
            ]
        }},
        {{
            "title": "Phase 4: Accompagnement et MGP",
            "description": "Description de 200-300 mots",
            "start_week": 20,
            "end_week": 96,
            "tasks": [
                {{
                    "code": "4A",
                    "title": "Installation du MGP",
                    "description": "Description détaillée",
                    "items": ["Activité 1", "Activité 2", "Activité 3", "Activité 4"],
                    "start_week": 20,
                    "end_week": 32
                }},
                {{
                    "code": "4B",
                    "title": "Formation comités MGP",
                    "description": "Description détaillée",
                    "items": ["Activité 1", "Activité 2", "Activité 3"],
                    "start_week": 28,
                    "end_week": 40,
                    "deliverable_week": 40,
                    "deliverable_code": "L6"
                }},
                {{
                    "code": "4C",
                    "title": "Accompagnement continu",
                    "description": "Description détaillée",
                    "items": ["Activité 1", "Activité 2", "Activité 3", "Activité 4"],
                    "start_week": 40,
                    "end_week": 96,
                    "deliverable_week": 96,
                    "deliverable_code": "L7"
                }}
            ],
            "deliverables": [
                {{"code": "L6", "name": "Dispositif MGP opérationnel"}},
                {{"code": "L7", "name": "Rapports trimestriels et rapport final"}}
            ]
        }}
    ],

    "risks": "Section de 600-800 mots sur la gestion des risques: risques contextuels (sécurité, climat, conflits), risques opérationnels (mobilisation, logistique), risques institutionnels, et mesures d'atténuation",

    "quality": "Section de 400-600 mots sur l'assurance qualité: KPIs, mécanismes de supervision, protocoles de reporting"
}}

IMPORTANT: Génère UNIQUEMENT le JSON, sans texte explicatif avant ou après. Assure-toi que le JSON est valide et complet."""

    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "sonar-pro",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 16000,
        "temperature": 0.3
    }

    print("Appelant Perplexity API...")
    response = requests.post(url, json=payload, headers=headers, timeout=300)
    response.raise_for_status()

    result = response.json()
    response_text = result['choices'][0]['message']['content']

    print(f"Réponse reçue ({len(response_text)} caractères)")

    # Parser le JSON
    methodology = parse_json_response(response_text)

    return methodology


def parse_json_response(response_text: str) -> dict:
    """Parse la réponse JSON de Perplexity"""

    # Nettoyer la réponse
    text = response_text.strip()

    # Enlever les blocs de code markdown
    if '```json' in text:
        match = re.search(r'```json\s*([\s\S]*?)\s*```', text)
        if match:
            text = match.group(1)
    elif '```' in text:
        match = re.search(r'```\s*([\s\S]*?)\s*```', text)
        if match:
            text = match.group(1)

    # Trouver le JSON entre { et }
    start = text.find('{')
    end = text.rfind('}')

    if start >= 0 and end > start:
        json_str = text[start:end+1]

        try:
            methodology = json.loads(json_str)
            print("JSON parsé avec succès")
            return methodology
        except json.JSONDecodeError as e:
            print(f"Erreur de parsing JSON: {e}")
            # Essayer de réparer
            json_str = repair_json(json_str)
            try:
                methodology = json.loads(json_str)
                print("JSON réparé et parsé")
                return methodology
            except:
                pass

    print("Échec du parsing, utilisation du fallback")
    return create_fallback_methodology()


def repair_json(json_str: str) -> str:
    """Tente de réparer un JSON malformé"""
    # Compter les accolades et crochets
    open_braces = json_str.count('{') - json_str.count('}')
    open_brackets = json_str.count('[') - json_str.count(']')

    # Fermer les structures ouvertes
    json_str = json_str.rstrip()

    # Ajouter les fermetures manquantes
    json_str += ']' * max(0, open_brackets)
    json_str += '}' * max(0, open_braces)

    return json_str


def create_fallback_methodology() -> dict:
    """Crée une méthodologie de fallback complète"""
    return {
        "introduction": """Notre consortium propose une approche méthodologique intégrée et participative pour l'accompagnement des communautés des 15 communes cibles du P2-P2RS au Sénégal. Forts de notre expérience dans les projets de gestion des ressources naturelles au Sahel, nous avons conçu une méthodologie qui s'ancre dans les réalités locales tout en répondant aux exigences de la Banque Africaine de Développement. Notre approche repose sur trois piliers fondamentaux : la participation communautaire, le renforcement des capacités locales et la durabilité des interventions.""",

        "context": """Le Programme régional de résilience à l'insécurité alimentaire et nutritionnelle au Sahel (P2RS), initié par la Banque Africaine de Développement depuis 2014, constitue une réponse structurelle aux défis chroniques de sécurité alimentaire dans la région sahélienne. Le P2-P2RS (Projet 2) s'inscrit dans la continuité des acquis de la phase 1, avec un accent particulier sur la consolidation et l'élargissement des interventions dans 15 communes réparties dans les régions de Matam, Tambacounda et Fatick.

**Zones d'intervention**

Le projet intervient dans deux pôles de développement distincts. Le Pôle Nord (Vallée du fleuve Sénégal) regroupe 12 communes dans les départements de Matam, Kanel et Bakel, caractérisé par des systèmes agropastoraux transhumants et des défis liés à la dégradation des terres. Le Pôle Centre (Bassin arachidier) comprend 3 communes insulaires (Fimela, Bassoul, Djirnda) dans la région de Fatick, vulnérables à la salinisation et aux changements climatiques.

**Cadre institutionnel**

Le projet s'inscrit dans la politique nationale de décentralisation, avec les collectivités territoriales comme porte d'entrée. Les acteurs clés incluent les services techniques déconcentrés (DRDR, IREF), les organisations de producteurs, les groupements de femmes et les autorités coutumières.

**Problématique**

Les communautés font face à plusieurs défis : dégradation des terres agricoles, conflits agriculteurs-éleveurs, faible capacité des structures communautaires, et insuffisance des connaissances en GDT et agroécologie.""",

        "principles": [
            {"name": "Approche participative et inclusive", "description": "Toutes nos interventions seront fondées sur la participation effective des communautés à toutes les étapes. Nous accorderons une attention particulière à l'inclusion des groupes vulnérables, notamment les femmes et les jeunes, dans les instances de décision."},
            {"name": "Ancrage dans les savoirs locaux", "description": "Notre méthodologie valorise les connaissances endogènes des communautés en matière de gestion des ressources naturelles. Les pratiques traditionnelles validées seront intégrées aux innovations techniques proposées."},
            {"name": "Adaptation au contexte local", "description": "Nous adapterons nos méthodes aux spécificités de chaque zone agro-écologique. Les outils de communication seront développés dans les langues locales (Pulaar, Wolof, Sérère)."},
            {"name": "Apprentissage par l'action", "description": "Notre programme privilégie l'apprentissage pratique à travers les Champs Écoles Paysans et les démonstrations sur le terrain pour faciliter le transfert des connaissances."},
            {"name": "Coordination et synergie", "description": "Nous assurerons une coordination étroite avec les services techniques, les partenaires du P2RS et les projets connexes pour maximiser les complémentarités."},
            {"name": "Équité genre", "description": "L'intégration du genre sera transversale. Les femmes représenteront au moins 40% des participants aux formations et 30% des membres des CGC/RN."}
        ],

        "phases": [
            {
                "title": "Phase 1: Démarrage et Diagnostic Participatif",
                "description": "Cette phase de 4 mois établira les bases de notre intervention à travers une compréhension approfondie du contexte socioéconomique des 15 communes. Nous installerons nos équipes, établirons les contacts avec les autorités et conduirons le diagnostic participatif selon une approche multi-acteurs.",
                "start_week": 1,
                "end_week": 16,
                "tasks": [
                    {
                        "code": "1A",
                        "title": "Installation et cadrage méthodologique",
                        "description": "Installation des bases opérationnelles dans les trois régions, recrutement et formation des animateurs, mise en place des moyens logistiques et établissement des protocoles de travail avec l'UCP.",
                        "items": ["Installation des bases à Matam, Bakel et Fatick", "Recrutement des 13 animateurs", "Atelier de lancement", "Visites aux autorités des 15 communes"],
                        "start_week": 1,
                        "end_week": 4,
                        "deliverable_week": 4,
                        "deliverable_code": "L1"
                    },
                    {
                        "code": "1B",
                        "title": "Études diagnostiques socioéconomiques",
                        "description": "Diagnostic participatif combinant enquêtes ménages, focus groups et cartographie des ressources naturelles dans chaque commune.",
                        "items": ["Élaboration des outils de collecte", "Enquêtes ménages et focus groups", "Cartographie participative", "Analyse des données"],
                        "start_week": 3,
                        "end_week": 12
                    },
                    {
                        "code": "1C",
                        "title": "Restitution et validation",
                        "description": "Restitution des résultats lors d'ateliers communaux et régionaux pour validation par les parties prenantes.",
                        "items": ["15 ateliers communaux", "3 ateliers régionaux", "Finalisation des rapports"],
                        "start_week": 13,
                        "end_week": 16,
                        "deliverable_week": 16,
                        "deliverable_code": "L2"
                    }
                ],
                "deliverables": [
                    {"code": "L1", "name": "Rapport d'établissement avec planning actualisé"},
                    {"code": "L2", "name": "Rapports de diagnostic des 15 communes"}
                ]
            },
            {
                "title": "Phase 2: Mise en Place des CGC/RN",
                "description": "Cette phase de 6 mois établira un système durable de gestion concertée des ressources naturelles à travers la mise en place ou redynamisation des CGC/RN, la négociation des conventions locales et la délimitation des espaces.",
                "start_week": 17,
                "end_week": 40,
                "tasks": [
                    {
                        "code": "2A",
                        "title": "Sensibilisation et mobilisation",
                        "description": "Campagne d'information dans les 15 communes utilisant réunions, radio et supports visuels pour expliquer l'importance de la gestion concertée.",
                        "items": ["Stratégie de communication", "Émissions radio en langues locales", "Réunions villageoises", "Panneaux d'information"],
                        "start_week": 17,
                        "end_week": 24
                    },
                    {
                        "code": "2B",
                        "title": "Constitution des CGC/RN",
                        "description": "Mise en place ou redynamisation des comités avec représentation inclusive de tous les groupes d'utilisateurs.",
                        "items": ["Évaluation des structures existantes", "Assemblées constitutives", "Élection des bureaux", "Élaboration des statuts"],
                        "start_week": 22,
                        "end_week": 32
                    },
                    {
                        "code": "2C",
                        "title": "Conventions locales et délimitation",
                        "description": "Négociation des règles de gestion et matérialisation des espaces (couloirs de passage, zones de pâturage).",
                        "items": ["Ateliers de négociation", "Rédaction des conventions", "Adoption par conseils municipaux", "Bornage des couloirs"],
                        "start_week": 28,
                        "end_week": 40,
                        "deliverable_week": 40,
                        "deliverable_code": "L3"
                    }
                ],
                "deliverables": [
                    {"code": "L3", "name": "15 CGC/RN opérationnels avec conventions locales"}
                ]
            },
            {
                "title": "Phase 3: Formation et Renforcement des Capacités",
                "description": "Phase de 12 mois dédiée au renforcement des capacités en GDT, agroécologie, agroforesterie et RNA à travers les Champs Écoles Paysans et formations des CGC/RN.",
                "start_week": 24,
                "end_week": 72,
                "tasks": [
                    {
                        "code": "3A",
                        "title": "Plan de renforcement des capacités",
                        "description": "Élaboration du plan détaillé définissant thématiques, approches pédagogiques et calendrier.",
                        "items": ["Analyse des besoins", "Définition des modules", "Calendrier de formation"],
                        "start_week": 24,
                        "end_week": 28,
                        "deliverable_week": 28,
                        "deliverable_code": "L4"
                    },
                    {
                        "code": "3B",
                        "title": "Formation des formateurs",
                        "description": "Sessions pour techniciens et animateurs sur facilitation, GDT, agroécologie et gestion des conflits.",
                        "items": ["Techniques de facilitation", "GDT et CES/DRS", "Agroécologie et RNA", "Gestion des conflits"],
                        "start_week": 28,
                        "end_week": 36
                    },
                    {
                        "code": "3C",
                        "title": "Formation des CGC/RN et producteurs",
                        "description": "Formation des membres des CGC/RN et déploiement de 30 Champs Écoles Paysans.",
                        "items": ["Modules CGC/RN (gouvernance, GDT)", "Installation 30 CEP", "Sessions pratiques", "Évaluation des acquis"],
                        "start_week": 36,
                        "end_week": 72,
                        "deliverable_week": 72,
                        "deliverable_code": "L5"
                    }
                ],
                "deliverables": [
                    {"code": "L4", "name": "Plan de renforcement des capacités"},
                    {"code": "L5", "name": "Rapport de formation (450 membres CGC/RN, 900 producteurs)"}
                ]
            },
            {
                "title": "Phase 4: Accompagnement et MGP",
                "description": "Phase transversale de 20 mois pour l'accompagnement continu des CGC/RN et l'opérationnalisation du Mécanisme de Gestion des Plaintes.",
                "start_week": 20,
                "end_week": 96,
                "tasks": [
                    {
                        "code": "4A",
                        "title": "Installation du MGP",
                        "description": "Mise en place des comités de gestion des plaintes aux niveaux villageois, communal et régional.",
                        "items": ["Identification des membres", "Installation des comités", "Points de dépôt et numéro vert", "Procédures de traitement"],
                        "start_week": 20,
                        "end_week": 32
                    },
                    {
                        "code": "4B",
                        "title": "Formation et vulgarisation MGP",
                        "description": "Formation des membres des comités et campagne de vulgarisation auprès des communautés.",
                        "items": ["Formation sur procédures MGP", "Techniques de médiation", "Spots radio", "Réunions d'information"],
                        "start_week": 28,
                        "end_week": 40,
                        "deliverable_week": 40,
                        "deliverable_code": "L6"
                    },
                    {
                        "code": "4C",
                        "title": "Accompagnement et suivi-évaluation",
                        "description": "Accompagnement continu des CGC/RN, suivi de l'application des conventions et capitalisation.",
                        "items": ["Visites hebdomadaires", "Suivi des conventions", "Rapports trimestriels", "Capitalisation finale"],
                        "start_week": 40,
                        "end_week": 96,
                        "deliverable_week": 96,
                        "deliverable_code": "L7"
                    }
                ],
                "deliverables": [
                    {"code": "L6", "name": "Dispositif MGP opérationnel"},
                    {"code": "L7", "name": "8 rapports trimestriels et rapport final"}
                ]
            }
        ],

        "risks": """**Risques contextuels**

- **Instabilité sécuritaire**: La région nord peut connaître des tensions. Mesure: coordination avec autorités locales et adaptation des plannings.
- **Conditions climatiques**: Les aléas peuvent perturber les activités. Mesure: flexibilité du calendrier.
- **Conflits intercommunautaires**: Tensions agriculteurs-éleveurs possibles. Mesure: médiation préventive.

**Risques opérationnels**

- **Mobilisation insuffisante**: Mesure: approche participative et communication intensive.
- **Turnover du personnel**: Mesure: documentation et partage des connaissances.
- **Difficultés logistiques**: Mesure: moyens adaptés (pirogues pour îles de Fatick).

**Risques institutionnels**

- **Faible appropriation locale**: Mesure: implication des maires dès le départ.
- **Conflits de compétences**: Mesure: coordination régulière avec partenaires.""",

        "quality": """**Indicateurs clés de performance**

- Taux de fonctionnement des CGC/RN: cible 80%
- Taux de résolution des plaintes: cible 90%
- Satisfaction des bénéficiaires: cible 85%
- Représentation des femmes: minimum 30%

**Mécanismes de contrôle**

- Supervision mensuelle du chef de mission
- Réunions hebdomadaires de coordination
- Visites conjointes avec l'UCP (trimestrielles)
- Évaluations participatives semestrielles

**Protocoles de reporting**

- Rapports hebdomadaires des animateurs
- Rapports mensuels des techniciens
- Rapports trimestriels à l'UCP"""
    }


def main():
    """Génère la méthodologie pour P2-P2RS Sénégal"""

    lang_config = get_language_config('fr')

    print("=" * 60)
    print("Génération de la méthodologie P2-P2RS Sénégal")
    print("=" * 60)

    try:
        methodology = generate_methodology_v2(TDR_CONTENT, lang_config)

        # Vérifier que la méthodologie est complète
        if not methodology.get('phases') or len(methodology['phases']) < 4:
            print("Méthodologie incomplète, utilisation du fallback")
            methodology = create_fallback_methodology()

        output_path = "/Users/apple/metodologias-rfps/output/Methodologie_P2RS_Senegal.docx"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        create_word_document(methodology, output_path, lang_config)

        print(f"\nDocument généré: {output_path}")

    except Exception as e:
        print(f"Erreur: {e}")
        print("Utilisation du fallback...")
        methodology = create_fallback_methodology()
        output_path = "/Users/apple/metodologias-rfps/output/Methodologie_P2RS_Senegal.docx"
        create_word_document(methodology, output_path, lang_config)
        print(f"Document généré avec fallback: {output_path}")


if __name__ == "__main__":
    main()
