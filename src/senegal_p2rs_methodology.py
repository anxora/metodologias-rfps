#!/usr/bin/env python3
"""
Generador de metodología para el proyecto P2-P2RS Senegal
Operador de Proximidad (OPP) - Gestión de Recursos Naturales
"""

import os
import sys

# Agregar el directorio src al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from methodology_generator import generate_methodology, METHODOLOGY_TEMPLATES
from document_writer import create_word_document
from translations import get_language_config


# Definir template específico para este proyecto de desarrollo rural/GRN
METHODOLOGY_TEMPLATES['rural_development'] = {
    'phases': [
        'Phase 1: Démarrage et Diagnostic Participatif',
        'Phase 2: Mise en Place et Renforcement des Comités de Gestion',
        'Phase 3: Formation et Renforcement des Capacités',
        'Phase 4: Accompagnement et Mise en Œuvre du MGP',
    ],
    'description': 'Méthodologie pour les projets de développement rural, gestion des ressources naturelles et renforcement des capacités communautaires'
}


TDR_CONTENT = """
TERMES DE RÉFÉRENCE - PROJET P2-P2RS SÉNÉGAL
Opérateur de Proximité (OPP) pour l'Accompagnement des Comités de Gestion Concertée des Ressources Naturelles

I. CONTEXTE DU PROJET

La Banque Africaine de Développement (BAD) a initié depuis 2014 le Programme régional de résilience à l'insécurité alimentaire et nutritionnelle au Sahel (P2RS). Le Programme de renforcement de la résilience à l'insécurité alimentaire et nutritionnelle au Sahel (P2RS) vise à:
- Contribuer à la réduction de la pauvreté et à l'amélioration de la sécurité alimentaire et nutritionnelle au Sahel
- Accroître, sur une base durable, la productivité et les productions agro-sylvo-pastorales et halieutiques

Le P2-P2RS (Projet 2 du P2RS) intervient dans 15 communes situées dans 5 départements et 3 régions:
- Région de Tambacounda: Département de Bakel (Bellé, Sinthiou Fissa, Gabou, Gathiary)
- Région de Matam: Départements de Matam (Agnam Civol, Dabia, Bokidiawé, Nguidjilone) et Kanel (Aouré, Orkadjiéré, Sinthiou Bamambé, Ndendory)
- Région de Fatick: Départements de Fatick (Fimela) et Foundiougne (Bassoul, Djirnda)

Le projet travaille autour de 2 pôles de développement:
1. Pôle Nord (Vallée du fleuve Sénégal): 12 communes dans les régions de Matam et Tambacounda
2. Pôle Centre (Bassin arachidier): 3 communes insulaires dans la région de Fatick

II. COMPOSANTES DU PROJET

i. Renforcement de la résilience aux Changements Climatiques des productions agro-sylvo-pastorales
ii. Développement des chaînes de valeur agro-sylvo-pastorales et halieutiques et promotion de l'entreprenariat
iii. Renforcement des capacités adaptatives aux changements climatiques
iv. Coordination et gestion du programme

III. OBJECTIFS DE LA MISSION

Objectif général: Appui à l'opérationnalisation des Comités de Gestion Concertée des Ressources Naturelles (CGC/RN), formation des acteurs à la gestion durable des ressources naturelles et des bonnes pratiques de GDT/agroécologie, et appui à la mise en œuvre du Mécanisme de Gestion des Plaintes (MGP).

Objectifs spécifiques:

Pour l'opérationnalisation des CGC/RN:
- Engager des études diagnostiques socioéconomiques des villages ciblés
- Identifier les principaux organismes exploitants (agriculture, élevage, foresterie)
- Identifier les principales contraintes et potentialités des zones ciblées
- Analyser les perceptions des populations sur les ressources naturelles locales
- Inventorier les stratégies endogènes de gestion des ressources naturelles
- Organiser des réunions d'information et de sensibilisation
- Négocier les règles de gestion concertées des ressources naturelles
- Appuyer l'élaboration et la mise en œuvre des conventions locales
- Mettre en place ou redynamiser les CGC/RN

Pour la formation des acteurs:
- Organiser des séances de restitution et validation des résultats
- Proposer un plan de renforcement des capacités (GDT, agroécologie, agroforesterie, RNA)
- Renforcer les capacités techniques des animateurs
- Former les CGC sur les techniques de conservation et restauration des terres
- Accompagner les CGC sur la mise en œuvre des connaissances acquises

Pour le Mécanisme de Gestion des Plaintes:
- Informer et sensibiliser sur la politique de gestion des plaintes
- Aider à l'installation des comités de gestion des plaintes
- Renforcer les capacités des membres des comités
- Vulgariser le MGP auprès des parties prenantes
- Appuyer le dispositif de collecte et transmission des plaintes

IV. PRINCIPES DIRECTEURS

2.1. Gestion durable des terres agricoles
- Maintenir la productivité à long terme des fonctions d'écosystème
- Accroître la productivité des biens et services
- Réalisation d'ouvrages antiérosifs et technologies de restauration

2.2. Restauration biologique des terres agricoles dégradées
- Compostage, gestion intégrée de la fertilité
- Micro-fertilisation, engrais verts, rotations avec légumineuses
- Jachères améliorées, paillage, gestion des résidus de récolte

2.3. Promotion de l'agroforesterie communautaire et de l'agroécologie
- Techniques agroforestières pour améliorer les rendements
- Régénération naturelle assistée (RNA)
- Plantation d'espèces à fonctions spécifiques

2.4. Aménagement de couloirs de passage
- Délimitation de couloirs pour le bétail
- Négociation entre parties prenantes
- Mise en place de comités de gestion

2.5. Plans d'occupation et d'affectation des sols (POAS)
- Planification de l'utilisation des terres
- Amélioration de la gestion foncière
- Intégration des activités productives

2.6. Sécurisation foncière et GRN
- Appui aux bureaux locaux de gestion foncière
- Cartographie et enregistrement des terres
- Droits d'accès des femmes aux ressources

2.7. Formation des acteurs
- Approche champs écoles pour les producteurs
- Formation des formateurs et facilitateurs
- Apprentissage par action

2.8. Mécanisme de Gestion des Plaintes
- Processus transparent et accessible
- Gratuit et sans représailles
- Approprié sur le plan culturel

V. ACTIVITÉS PRÉVUES

4.1. Information et sensibilisation
- Réunions au niveau des communes et villages
- Émissions radiophoniques
- Dépliants, affiches, panneaux

4.2. Mise en place et renforcement des CGC et CG-MGP
- Diagnostic socioéconomique
- Élaboration des plans de renforcement des capacités
- Formation des membres des comités

4.3. Appui à la mise en œuvre du MGP
- Organisation des ateliers
- Sensibilisation sur le mécanisme
- Accompagnement de la résolution des plaintes

VI. ÉQUIPE REQUISE

- Chef de mission/Superviseur (BAC+5, 15 ans d'expérience): 24 H/M
- Technicien GRN/agroécologie (Bac/Technicien supérieur, 5 ans): 24 H/M
- Technicien GDT (Bac/Technicien supérieur, 5 ans): 24 H/M
- Responsable MGP (Maîtrise/Master 2 sociologie, 5 ans): 24 H/M
- Animateurs locaux (Bac/Technicien, 5 ans): 24 H/M chacun
  - Matam: 6 animateurs
  - Tambacounda: 4 animateurs
  - Fatick: 3 animateurs

VII. MOYENS MATÉRIELS
- 1 véhicule de liaison par zone
- Motos 125 pour techniciens et animateurs
- Matériel informatique et bureautique

VIII. LIVRABLES
- Rapport d'établissement (1 mois après démarrage)
- Rapports trimestriels d'activités
- Rapports de performances des organisations appuyées

IX. DURÉE
La durée totale de la mission est de 24 mois.

X. ZONES D'INTERVENTION

Région Matam (8 communes):
- Département Matam: Agnam Civol, Dabia, Bokidiawé, Nguidjilone
- Département Kanel: Aouré, Orkadjiéré, Sinthiou Bamambé, Ndendory

Région Tambacounda (4 communes):
- Département Bakel: Bellé, Sinthiou Fissa, Gabou, Gathiary

Région Fatick (3 communes):
- Département Fatick: Fimela
- Département Foundiougne: Bassoul, Djirnda
"""


def main():
    """Genera la metodología para el proyecto P2-P2RS Senegal"""

    # Configuración en francés
    lang_config = get_language_config('fr')

    print("Generando metodología para P2-P2RS Senegal...")
    print("Idioma: Français")
    print("Tipo: Desarrollo rural / Gestión de recursos naturales")

    # Generar metodología usando Perplexity
    try:
        methodology = generate_methodology(
            tdr_content=TDR_CONTENT,
            lang_config=lang_config,
            methodology_type='general'  # Usamos general que tiene 4 fases como necesitamos
        )

        # Crear documento Word
        output_path = "/Users/apple/metodologias-rfps/output/Methodologie_P2RS_Senegal.docx"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        create_word_document(methodology, output_path, lang_config)

        print(f"\nDocumento generado exitosamente: {output_path}")

    except Exception as e:
        print(f"Error generando metodología: {e}")
        raise


if __name__ == "__main__":
    main()
