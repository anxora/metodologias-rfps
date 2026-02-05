#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Metodología P2-P2RS Senegal - Version con formato párrafo como Uruguay
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from document_writer import create_word_document
from translations import get_language_config


def generate_methodology():
    methodology = {
        "introduction": "Notre consortium propose une approche méthodologique intégrée et participative pour l'accompagnement des communautés des 15 communes cibles du P2-P2RS au Sénégal. Forts de notre expérience dans les projets de gestion des ressources naturelles au Sahel, nous avons conçu une méthodologie qui s'ancre dans les réalités locales tout en répondant aux exigences de la Banque Africaine de Développement. Notre approche repose sur trois piliers fondamentaux : la participation communautaire, le renforcement des capacités locales et la durabilité des interventions. Nous mobiliserons une équipe pluridisciplinaire expérimentée dans les régions de Matam, Tambacounda et Fatick pour assurer un accompagnement de proximité efficace des Comités de Gestion Concertée des Ressources Naturelles (CGC/RN) et la mise en oeuvre réussie du Mécanisme de Gestion des Plaintes (MGP).",

        "context": """**Le Programme P2RS et son Contexte Régional**

Le Programme régional de résilience à l'insécurité alimentaire et nutritionnelle au Sahel (P2RS), initié par la Banque Africaine de Développement depuis 2014, constitue une réponse structurelle aux défis chroniques de sécurité alimentaire dans la région sahélienne. Le P2-P2RS (Projet 2) s'inscrit dans la continuité des acquis de la phase 1, avec un accent particulier sur la consolidation et l'élargissement des interventions dans 15 communes réparties dans les régions de Matam, Tambacounda et Fatick.

**Zones d'Intervention**

Le projet travaille autour de deux pôles de développement. Le Pôle Nord (Vallée du fleuve Sénégal) regroupe 12 communes : Matam (Agnam Civol, Dabia, Bokidiawé, Nguidjilone), Kanel (Aouré, Orkadjiéré, Sinthiou Bamambé, Ndendory) et Bakel (Bellé, Sinthiou Fissa, Gabou, Gathiary). Le Pôle Centre (Bassin arachidier) comprend 3 communes insulaires (Fimela, Bassoul, Djirnda) dans la région de Fatick, particulièrement vulnérables aux effets des changements climatiques.

**Cadre Institutionnel et Parties Prenantes**

Le projet s'inscrit dans le cadre de la politique nationale de décentralisation du Sénégal, avec les collectivités territoriales comme porte d'entrée principale. La stratégie d'intervention sera basée sur le « faire faire », impliquant fortement les services techniques nationaux. Les acteurs clés incluent : les services techniques déconcentrés (DRDR, IREF, SAED), les organisations de producteurs agricoles et pastoraux, les groupements de femmes, les autorités coutumières et religieuses, ainsi que les ONG locales.

**Problématique et Défis Majeurs**

Les communautés cibles font face à plusieurs défis interconnectés : la dégradation continue des terres agricoles due à l'érosion hydrique et éolienne, la salinisation et la perte de fertilité ; les conflits récurrents entre agriculteurs et éleveurs liés à la réduction des espaces pastoraux et à l'obstruction des couloirs de passage ; la faible capacité organisationnelle des structures communautaires de gestion des ressources naturelles ; et l'insuffisance des connaissances en techniques de Gestion Durable des Terres (GDT) et d'agroécologie.

**Objectifs de la Mission**

L'objectif général est l'appui à l'opérationnalisation des Comités de Gestion Concertée des Ressources Naturelles (CGC/RN), la formation des acteurs à la gestion durable des ressources naturelles et des bonnes pratiques de GDT/agroécologie, et l'appui à la mise en oeuvre du Mécanisme de Gestion des Plaintes (MGP).""",

        "principles": [
            {
                "name": "Approche Participative et Inclusive",
                "description": "Toutes nos interventions seront fondées sur la participation effective des communautés à toutes les étapes : diagnostic, planification, mise en oeuvre et suivi. Nous accorderons une attention particulière à l'inclusion des groupes vulnérables, notamment les femmes et les jeunes, dans les instances de décision et les activités de renforcement des capacités."
            },
            {
                "name": "Ancrage dans les Savoirs Locaux",
                "description": "Notre méthodologie valorise et capitalise sur les connaissances endogènes des communautés en matière de gestion des ressources naturelles. Les pratiques traditionnelles validées seront intégrées aux innovations techniques proposées pour assurer une adaptation culturelle et une appropriation durable."
            },
            {
                "name": "Adaptation au Contexte Local",
                "description": "Reconnaissant la diversité des contextes agro-écologiques entre le Pôle Nord et le Pôle Centre, nous adapterons nos méthodes et contenus de formation aux spécificités de chaque zone. Les outils de communication seront développés dans les langues locales (Pulaar, Wolof, Sérère)."
            },
            {
                "name": "Apprentissage par l'Action",
                "description": "Notre programme de renforcement des capacités privilégie l'apprentissage pratique à travers les Champs Écoles Paysans (CEP) et les démonstrations sur le terrain, facilitant le transfert des connaissances et la démultiplication des bonnes pratiques au sein des communautés."
            },
            {
                "name": "Coordination et Synergie",
                "description": "Nous assurerons une coordination étroite avec les services techniques déconcentrés, les autres partenaires du P2RS et les projets connexes intervenant dans les mêmes zones pour maximiser les complémentarités et mutualiser les ressources disponibles."
            },
            {
                "name": "Équité Genre et Autonomisation",
                "description": "L'intégration du genre sera transversale à toutes nos interventions. Les femmes représenteront au moins 40% des participants aux formations et au moins 30% des membres des instances de décision des CGC/RN, conformément aux objectifs du projet."
            }
        ],

        "phases": [
            {
                "title": "Phase 1 : Démarrage et Diagnostic Participatif",
                "description": "Cette phase fondamentale de 4 mois permettra d'établir les bases solides de notre intervention à travers une compréhension approfondie du contexte socioéconomique et des dynamiques de gestion des ressources naturelles dans les 15 communes cibles. Nous procéderons à l'installation de nos équipes dans les trois régions (Matam, Tambacounda, Fatick) et établirons les premiers contacts avec les autorités locales et les communautés bénéficiaires. Le diagnostic participatif sera conduit selon une approche multi-acteurs intégrant les perceptions de tous les groupes d'intérêt.",
                "start_week": 1,
                "end_week": 16,
                "tasks": [
                    {
                        "code": "1A",
                        "title": "Installation et cadrage méthodologique",
                        "description": "L'équipe de notre consortium procédera à l'installation des bases opérationnelles dans les trois régions d'intervention : Matam, Bakel et Fatick. Nous recruterons et formerons les 13 animateurs locaux qui constitueront l'ossature de notre dispositif de terrain, en veillant à leur ancrage communautaire et à leur maîtrise des langues locales. L'acquisition et le déploiement des moyens logistiques (véhicules, équipements de bureau, matériels de communication) seront finalisés durant cette période. Un atelier de lancement sera organisé avec l'ensemble des parties prenantes du P2RS pour présenter notre approche méthodologique et valider le planning détaillé des interventions. Des visites de courtoisie seront effectuées auprès des autorités administratives et coutumières des 15 communes pour établir les bases d'une collaboration fructueuse.",
                        "items": [],
                        "start_week": 1,
                        "end_week": 4,
                        "deliverable_week": 4,
                        "deliverable_code": "L1"
                    },
                    {
                        "code": "1B",
                        "title": "Études diagnostiques socioéconomiques",
                        "description": "Le diagnostic socioéconomique sera conduit dans chacun des villages ciblés selon une méthodologie participative rigoureuse combinant plusieurs outils complémentaires. Nous réaliserons des enquêtes ménages auprès d'un échantillon représentatif de la population, des focus groups différenciés (hommes, femmes, jeunes, éleveurs, agriculteurs) pour capturer les perceptions spécifiques de chaque groupe, et des entretiens approfondis avec les personnes ressources et les autorités coutumières. La cartographie participative des ressources naturelles permettra d'identifier les zones de tension, les couloirs de transhumance, les aires de pâturage et les espaces agricoles. L'analyse portera sur les systèmes de production, les modes d'accès aux ressources naturelles, les dynamiques foncières et les mécanismes existants de résolution des conflits.",
                        "items": [],
                        "start_week": 3,
                        "end_week": 12
                    },
                    {
                        "code": "1C",
                        "title": "Inventaire des stratégies endogènes de GRN",
                        "description": "Cette activité vise à documenter et valoriser les pratiques traditionnelles de gestion des ressources naturelles qui ont fait leurs preuves au fil des générations. Nos équipes recenseront les règles coutumières de gestion des pâturages, des forêts et des points d'eau, les conventions locales existantes entre communautés, et les mécanismes traditionnels de résolution des conflits entre agriculteurs et éleveurs. L'identification des personnes ressources (chefs coutumiers, sages, leaders d'opinion) permettra de constituer un réseau d'alliés pour la suite des interventions. Une analyse comparative des stratégies efficaces sera réalisée pour alimenter l'élaboration d'un répertoire des bonnes pratiques adaptées à chaque zone agro-écologique.",
                        "items": [],
                        "start_week": 8,
                        "end_week": 14
                    },
                    {
                        "code": "1D",
                        "title": "Restitution et validation du diagnostic",
                        "description": "Les résultats du diagnostic seront restitués et validés lors d'ateliers participatifs organisés à deux niveaux. Au niveau communal, 15 ateliers réuniront les représentants des différents villages, les élus locaux, les services techniques et les organisations communautaires pour présenter les résultats spécifiques à chaque commune et recueillir les observations. Au niveau régional, 3 ateliers de synthèse permettront de confronter les analyses aux perceptions des acteurs régionaux et de valider les orientations stratégiques pour la suite du projet. Les observations et corrections issues de ces restitutions seront intégrées dans les rapports finaux de diagnostic qui seront diffusés à l'ensemble des parties prenantes.",
                        "items": [],
                        "start_week": 13,
                        "end_week": 16,
                        "deliverable_week": 16,
                        "deliverable_code": "L2"
                    }
                ],
                "deliverables": [
                    {"code": "L1", "name": "Rapport d'établissement avec recadrage méthodologique et planning actualisé"},
                    {"code": "L2", "name": "Rapports de diagnostic socioéconomique et environnemental des 15 communes"}
                ]
            },
            {
                "title": "Phase 2 : Mise en Place et Opérationnalisation des CGC/RN",
                "description": "Cette phase de 6 mois constitue le coeur de notre intervention pour l'établissement d'un système durable de gestion concertée des ressources naturelles. Sur la base des résultats du diagnostic, nous procéderons à la mise en place ou à la redynamisation des Comités de Gestion Concertée des Ressources Naturelles (CGC/RN) dans chaque commune. Les règles de gestion concertée seront négociées et formalisées à travers des conventions locales adoptées par les conseils municipaux.",
                "start_week": 17,
                "end_week": 40,
                "tasks": [
                    {
                        "code": "2A",
                        "title": "Sensibilisation et mobilisation communautaire",
                        "description": "Une vaste campagne d'information et de sensibilisation sera déployée dans les 15 communes pour expliquer les objectifs du projet et l'importance de la gestion concertée des ressources naturelles. Notre stratégie de communication utilisera des approches diversifiées et adaptées aux contextes locaux : réunions villageoises animées dans les langues locales, émissions radiophoniques interactives en Pulaar, Wolof et Sérère sur les radios communautaires, supports visuels illustrés accessibles aux populations non alphabétisées, et causeries thématiques avec les différents groupes d'utilisateurs des ressources. Des relais communautaires seront formés pour assurer la continuité de la sensibilisation au-delà des interventions directes de nos équipes. Des panneaux d'information seront installés dans les lieux stratégiques de chaque commune.",
                        "items": [],
                        "start_week": 17,
                        "end_week": 24
                    },
                    {
                        "code": "2B",
                        "title": "Constitution et structuration des CGC/RN",
                        "description": "Les Comités de Gestion Concertée des Ressources Naturelles seront mis en place ou redynamisés selon un processus transparent et participatif respectant les équilibres sociaux locaux. Chaque CGC/RN comprendra des représentants de tous les groupes d'utilisateurs des ressources : agriculteurs, éleveurs transhumants et sédentaires, exploitants forestiers, femmes, jeunes, et autorités coutumières. Une évaluation préalable des structures existantes de gestion des ressources naturelles permettra d'identifier les acquis à capitaliser et les dysfonctionnements à corriger. Les assemblées générales constitutives seront facilitées par nos équipes en veillant à la représentativité et à l'inclusion. L'élection des bureaux respectera un quota genre de 30% minimum de femmes. Les statuts et règlements intérieurs seront élaborés de manière participative et la reconnaissance officielle des CGC/RN sera obtenue auprès des autorités compétentes.",
                        "items": [],
                        "start_week": 22,
                        "end_week": 32
                    },
                    {
                        "code": "2C",
                        "title": "Négociation et élaboration des conventions locales",
                        "description": "Les règles de gestion concertée des ressources naturelles seront négociées à travers des ateliers multi-acteurs réunissant l'ensemble des parties prenantes. Ce processus de négociation portera sur les points critiques identifiés lors du diagnostic : délimitation des espaces (zones agricoles, aires de pâturage, couloirs de transhumance, zones de mise en défens), règles d'accès et d'utilisation des ressources selon les saisons, périodes de mise en défens des pâturages et forêts, barème de sanctions pour les infractions, et mécanismes de surveillance et de contrôle. Les projets de conventions locales seront rédigés en tenant compte des réalités de chaque commune et soumis à validation participative avant leur adoption formelle par les conseils municipaux.",
                        "items": [],
                        "start_week": 28,
                        "end_week": 38
                    },
                    {
                        "code": "2D",
                        "title": "Délimitation et matérialisation des espaces",
                        "description": "Notre équipe appuiera la délimitation et la matérialisation physique des espaces convenus dans les conventions locales. La cartographie participative des terroirs sera finalisée avec l'appui de GPS et de systèmes d'information géographique pour produire des cartes précises et exploitables. Les couloirs de passage du bétail seront identifiés, bornés et sécurisés pour prévenir les conflits entre agriculteurs et éleveurs. Les zones de pâturage, les aires de repos du bétail et les points d'abreuvement seront clairement délimités. Les zones de mise en défens pour la régénération des ressources naturelles seront matérialisées. Les cartes des terroirs produites seront diffusées auprès de toutes les parties prenantes et affichées dans les lieux publics.",
                        "items": [],
                        "start_week": 32,
                        "end_week": 40,
                        "deliverable_week": 40,
                        "deliverable_code": "L3"
                    }
                ],
                "deliverables": [
                    {"code": "L3", "name": "15 CGC/RN opérationnels avec conventions locales adoptées et espaces délimités"}
                ]
            },
            {
                "title": "Phase 3 : Formation et Renforcement des Capacités",
                "description": "Cette phase de 12 mois est dédiée au renforcement des capacités des acteurs à tous les niveaux. Le programme couvrira les thématiques prioritaires de la Gestion Durable des Terres (GDT), de l'agroécologie, de l'agroforesterie, de la Régénération Naturelle Assistée (RNA) et de la gestion des conflits. Notre approche privilégiera l'apprentissage par l'action à travers les Champs Écoles Paysans, permettant aux producteurs d'expérimenter et d'adopter les techniques dans leurs propres conditions de production.",
                "start_week": 24,
                "end_week": 72,
                "tasks": [
                    {
                        "code": "3A",
                        "title": "Élaboration du plan de renforcement des capacités",
                        "description": "Sur la base des besoins identifiés lors du diagnostic participatif et des profils des bénéficiaires, notre équipe élaborera un plan détaillé de renforcement des capacités. Ce plan définira les thématiques prioritaires pour chaque catégorie d'acteurs (membres des CGC/RN, producteurs, femmes, jeunes), les approches pédagogiques adaptées aux contextes locaux et aux niveaux d'alphabétisation, les contenus détaillés des modules de formation, et le calendrier des sessions tenant compte du calendrier agricole. Les formateurs et personnes ressources seront identifiés parmi les techniciens des services déconcentrés, les ONG partenaires et les producteurs modèles. Le plan sera validé par l'Unité de Coordination du Projet et les partenaires techniques avant sa mise en oeuvre.",
                        "items": [],
                        "start_week": 24,
                        "end_week": 28,
                        "deliverable_week": 28,
                        "deliverable_code": "L4"
                    },
                    {
                        "code": "3B",
                        "title": "Formation des formateurs et animateurs",
                        "description": "Nous organiserons des sessions intensives de formation des formateurs pour nos techniciens et animateurs ainsi que pour les agents des services techniques partenaires qui seront impliqués dans le dispositif de formation. Ces sessions couvriront les techniques de facilitation participative et d'animation de groupes d'adultes, les contenus techniques sur la GDT et les techniques de Conservation des Eaux et des Sols/Défense et Restauration des Sols (CES/DRS), les pratiques agroécologiques et la Régénération Naturelle Assistée (RNA), la production de plants agroforestiers et les techniques de plantation, ainsi que la gestion des conflits liés aux ressources naturelles et les techniques de médiation. Chaque session durera entre 3 et 5 jours selon la complexité des thématiques.",
                        "items": [],
                        "start_week": 28,
                        "end_week": 36
                    },
                    {
                        "code": "3C",
                        "title": "Formation des membres des CGC/RN",
                        "description": "Les 450 membres des 15 CGC/RN bénéficieront d'un programme complet de formation sur leurs rôles et responsabilités. Les modules porteront sur la gouvernance locale et le leadership, l'animation des réunions et la prise de décision consensuelle, les techniques de gestion durable des ressources naturelles, la gestion des conflits et la médiation communautaire, le suivi-évaluation participatif des conventions locales, et la mobilisation des ressources locales pour le fonctionnement des comités. Chaque CGC/RN bénéficiera d'au moins 10 jours de formation répartis sur plusieurs sessions. Une visite d'échange inter-CGC/RN sera organisée pour faciliter le partage d'expériences entre communes.",
                        "items": [],
                        "start_week": 36,
                        "end_week": 56
                    },
                    {
                        "code": "3D",
                        "title": "Formation des producteurs via Champs Écoles Paysans",
                        "description": "L'approche Champs Écoles Paysans (CEP) sera déployée comme principal vecteur de formation des producteurs aux techniques de GDT, d'agroécologie et d'agroforesterie. Nous installerons 30 CEP (2 par commune) qui regrouperont chacun 25 à 30 producteurs se réunissant régulièrement pendant une saison culturale complète. Les sessions pratiques couvriront le compostage et la gestion intégrée de la fertilité des sols, la construction d'ouvrages antiérosifs (cordons pierreux, demi-lunes, zaï), les techniques de RNA et d'agroforesterie, et la production et utilisation de biopesticides. Au total, 900 producteurs seront formés directement, avec un objectif de 40% de femmes. L'évaluation participative des apprentissages permettra de mesurer l'adoption des pratiques et d'identifier les besoins de suivi.",
                        "items": [],
                        "start_week": 40,
                        "end_week": 72,
                        "deliverable_week": 72,
                        "deliverable_code": "L5"
                    }
                ],
                "deliverables": [
                    {"code": "L4", "name": "Plan de renforcement des capacités validé avec modules de formation"},
                    {"code": "L5", "name": "Rapport de formation avec 450 membres CGC/RN et 900 producteurs formés"}
                ]
            },
            {
                "title": "Phase 4 : Accompagnement et Mise en Oeuvre du MGP",
                "description": "Cette phase transversale de 20 mois est dédiée à l'accompagnement continu des CGC/RN dans la mise en oeuvre des conventions locales et l'opérationnalisation du Mécanisme de Gestion des Plaintes (MGP). Nos animateurs assureront un suivi de proximité régulier pour appuyer les comités dans l'application des règles négociées, la gestion des infractions et la résolution des conflits. Le dispositif MGP sera installé à trois niveaux pour garantir un traitement efficace et transparent des plaintes des communautés.",
                "start_week": 20,
                "end_week": 96,
                "tasks": [
                    {
                        "code": "4A",
                        "title": "Installation du dispositif MGP",
                        "description": "Le Mécanisme de Gestion des Plaintes sera installé à trois niveaux complémentaires pour assurer un traitement efficace et de proximité des doléances des communautés. Au niveau villageois, des points focaux seront désignés pour recevoir les plaintes et tenter une résolution à l'amiable. Au niveau communal, des comités de gestion des plaintes seront mis en place avec des représentants des différentes parties prenantes. Au niveau régional, un comité de recours traitera les cas non résolus aux niveaux inférieurs. Les organes seront dotés des outils nécessaires (registres, fiches de suivi, boîtes à suggestions) et les circuits de transmission des plaintes seront clairement définis. Un numéro vert sera mis en place pour faciliter le dépôt des plaintes.",
                        "items": [],
                        "start_week": 20,
                        "end_week": 32
                    },
                    {
                        "code": "4B",
                        "title": "Formation des membres des comités MGP",
                        "description": "Les membres des comités de gestion des plaintes à tous les niveaux bénéficieront d'une formation complète sur leurs rôles et responsabilités. Les modules couvriront la politique de gestion des plaintes du projet et les standards de la BAD, les procédures de réception, enregistrement et traitement des plaintes, les techniques de médiation et de résolution amiable des conflits, la documentation des cas et le rapportage, ainsi que la confidentialité et la protection des plaignants. Des sessions de simulation et de mise en situation permettront aux membres de s'exercer sur des cas concrets. Des recyclages périodiques seront organisés pour maintenir les compétences à jour.",
                        "items": [],
                        "start_week": 28,
                        "end_week": 40,
                        "deliverable_week": 40,
                        "deliverable_code": "L6"
                    },
                    {
                        "code": "4C",
                        "title": "Vulgarisation du MGP auprès des communautés",
                        "description": "Une campagne intensive de vulgarisation sera déployée pour informer les populations sur l'existence du MGP et ses modalités de fonctionnement. Les messages porteront sur les types de plaintes recevables, les canaux de dépôt disponibles (points focaux, boîtes à suggestions, numéro vert), les délais de traitement attendus, et les garanties de confidentialité et de non-représailles. Des spots radio seront produits et diffusés en langues locales sur les radios communautaires. Des affiches et dépliants illustrés seront conçus pour être accessibles aux populations non alphabétisées et distribués dans tous les villages. Des réunions d'information seront organisées dans chaque village et des relais communautaires seront formés pour assurer la sensibilisation continue.",
                        "items": [],
                        "start_week": 36,
                        "end_week": 52
                    },
                    {
                        "code": "4D",
                        "title": "Accompagnement des CGC/RN et suivi des conventions",
                        "description": "Nos animateurs assureront un accompagnement régulier et de proximité des CGC/RN tout au long du projet. Les visites hebdomadaires permettront d'appuyer les comités dans l'animation de leurs réunions statutaires, l'application effective des conventions locales, la gestion des infractions constatées, la mobilisation des ressources locales pour leur fonctionnement, et la documentation de leurs activités. Le suivi de l'application des conventions locales sera assuré à travers des indicateurs clés : respect des délimitations d'espaces, application des règles d'accès aux ressources, gestion des conflits signalés, et fonctionnement des mécanismes de surveillance. La facilitation de la résolution des conflits émergents sera assurée en coordination avec les autorités coutumières et administratives.",
                        "items": [],
                        "start_week": 40,
                        "end_week": 96
                    },
                    {
                        "code": "4E",
                        "title": "Suivi-évaluation et capitalisation",
                        "description": "Un dispositif de suivi-évaluation participatif sera mis en place pour mesurer les progrès réalisés et documenter les leçons apprises. Le système de collecte des données sera basé sur des indicateurs clés alignés sur le cadre logique du projet. Des évaluations participatives semestrielles seront conduites avec les communautés pour recueillir leurs perceptions sur l'évolution de la gestion des ressources naturelles et le fonctionnement des CGC/RN. Les rapports trimestriels d'activités synthétiseront les données collectées et alimenteront le reporting à l'Unité de Coordination du Projet. Un exercice de capitalisation finale permettra de documenter les bonnes pratiques, les innovations et les leçons apprises pour informer les futures interventions dans la région.",
                        "items": [],
                        "start_week": 12,
                        "end_week": 96,
                        "deliverable_week": 96,
                        "deliverable_code": "L7"
                    }
                ],
                "deliverables": [
                    {"code": "L6", "name": "Dispositif MGP opérationnel avec comités formés et outils déployés"},
                    {"code": "L7", "name": "8 rapports trimestriels d'activités et rapport final de capitalisation"}
                ]
            }
        ],

        "risks": """**Risques Contextuels**

- **Instabilité sécuritaire** : La région nord du Sénégal peut connaître des tensions liées aux mouvements transfrontaliers. Notre équipe maintiendra une coordination étroite avec les autorités locales et adaptera les plannings de terrain en fonction de l'évolution de la situation sécuritaire.

- **Conditions climatiques défavorables** : Les aléas climatiques (sécheresses, inondations) peuvent perturber les activités agricoles et les déplacements sur le terrain. Nous intégrerons une flexibilité dans le calendrier des interventions et prioriserons les activités critiques pendant les périodes favorables.

- **Conflits intercommunautaires** : Les tensions entre agriculteurs et éleveurs peuvent s'intensifier, notamment en période de soudure. Notre approche préventive basée sur le dialogue et la médiation, avec l'implication précoce des autorités coutumières, permettra d'anticiper et de désamorcer les conflits potentiels.

**Risques Opérationnels**

- **Mobilisation insuffisante des communautés** : Les populations peuvent être réticentes à s'engager dans de nouvelles structures de gestion. Notre approche participative dès le diagnostic et notre communication intensive en langues locales favoriseront l'appropriation du projet par les communautés.

- **Turnover du personnel** : Le départ de membres clés de l'équipe peut affecter la continuité des interventions. Nous mettrons en place une documentation systématique des activités et un partage régulier des connaissances au sein de l'équipe.

- **Difficultés logistiques** : L'enclavement de certaines communes, notamment les îles du Saloum, peut compliquer les déplacements. Nous planifierons les missions de terrain de manière anticipée et prévoirons des moyens adaptés (pirogues pour les îles).

**Risques Institutionnels**

- **Faible appropriation par les autorités locales** : Les collectivités territoriales peuvent ne pas reconnaître pleinement les conventions locales élaborées. Nous impliquerons les maires et conseils municipaux dès le départ du processus pour garantir leur engagement.

- **Conflits de compétences** : Des chevauchements avec d'autres projets peuvent créer des tensions ou des duplications. Une cartographie des acteurs et une coordination régulière avec les partenaires permettront d'optimiser les synergies.""",

        "quality": """**Indicateurs Clés de Performance (KPIs)**

- Taux de fonctionnement des CGC/RN (réunions régulières, présence des membres) : cible 80%
- Taux de résolution des plaintes dans les délais impartis : cible 90%
- Taux de satisfaction des bénéficiaires des formations : cible 85%
- Représentation des femmes dans les instances de décision des CGC/RN : minimum 30%
- Taux d'application effective des conventions locales : cible 75%
- Nombre de producteurs formés via les Champs Écoles Paysans : cible 900

**Mécanismes de Contrôle et Supervision**

- Supervision mensuelle du chef de mission dans chaque région d'intervention
- Réunions hebdomadaires de coordination des techniciens régionaux
- Visites de terrain conjointes avec l'Unité de Coordination du Projet (trimestrielles)
- Audits internes semestriels des activités et de la gestion financière
- Évaluations participatives semestrielles avec les communautés bénéficiaires

**Protocoles de Reporting**

- Rapports hebdomadaires des animateurs (format standardisé)
- Rapports mensuels des techniciens avec données de suivi des indicateurs
- Rapports trimestriels consolidés à l'UCP (5 jours après fin de trimestre)
- Base de données géoréférencée des interventions et des CGC/RN
- Photothèque et vidéothèque documentant les activités et les résultats"""
    }

    return methodology


if __name__ == "__main__":
    methodology = generate_methodology()
    lang_config = get_language_config('fr')
    output_path = "/Users/apple/metodologias-rfps/output/Methodologie_P2RS_Senegal.docx"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    create_word_document(methodology, output_path, lang_config)
    print(f"Document généré: {output_path}")
