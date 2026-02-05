# -*- coding: utf-8 -*-
"""
Metodología P2-P2RS Senegal - Debug version
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from document_writer import create_word_document
from translations import get_language_config


def generate_methodology():
    methodology = {
        "introduction": "Notre consortium propose une approche methodologique integree.",

        "context": """**Le Programme P2RS**

Le Programme regional de resilience au Sahel (P2RS), initie par la Banque Africaine de Developpement depuis 2014, constitue une reponse structurelle aux defis chroniques de securite alimentaire.

**Zones d'Intervention**

Le projet travaille autour de deux poles de developpement dans les regions de Matam, Tambacounda et Fatick.""",

        "principles": [
            {
                "name": "Approche Participative",
                "description": "Toutes nos interventions seront fondees sur la participation effective des communautes a toutes les etapes."
            },
            {
                "name": "Ancrage Local",
                "description": "Notre methodologie valorise les connaissances endogenes des communautes en matiere de gestion des ressources naturelles."
            },
            {
                "name": "Adaptation",
                "description": "Nous adapterons nos methodes aux specificites de chaque zone agro-ecologique."
            },
            {
                "name": "Apprentissage",
                "description": "Notre programme privilegie l'apprentissage pratique a travers les Champs Ecoles Paysans."
            },
            {
                "name": "Coordination",
                "description": "Nous assurerons une coordination etroite avec les services techniques."
            },
            {
                "name": "Equite Genre",
                "description": "L'integration du genre sera transversale a toutes nos interventions."
            }
        ],

        "phases": [
            {
                "title": "Phase 1 : Demarrage",
                "description": "Cette phase de 4 mois etablira les bases de notre intervention.",
                "start_week": 1,
                "end_week": 16,
                "tasks": [
                    {
                        "code": "1A",
                        "title": "Installation",
                        "description": "Installation des bases operationnelles.",
                        "items": [
                            "Installation des bases",
                            "Recrutement des animateurs"
                        ],
                        "start_week": 1,
                        "end_week": 4,
                        "deliverable_week": 4,
                        "deliverable_code": "L1"
                    }
                ],
                "deliverables": [
                    {"code": "L1", "name": "Rapport d'etablissement"}
                ]
            }
        ],

        "risks": """**Risques Contextuels**

- Instabilite securitaire : Coordination avec autorites locales.""",

        "quality": """**Indicateurs Cles**

- Taux de fonctionnement des CGC/RN : cible 80%"""
    }

    return methodology


if __name__ == "__main__":
    methodology = generate_methodology()
    lang_config = get_language_config('fr')
    output_path = "/Users/apple/metodologias-rfps/output/Methodologie_P2RS_Senegal_debug.docx"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    create_word_document(methodology, output_path, lang_config)
    print(f"Document genere: {output_path}")
