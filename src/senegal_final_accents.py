# -*- coding: utf-8 -*-
"""
Metodología P2-P2RS Senegal - Versión con acentos UTF-8
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from document_writer import create_word_document
from translations import get_language_config


def generate_methodology():
    methodology = {
        "introduction": u"Notre consortium propose une approche méthodologique intégrée et participative pour l'accompagnement des communautés des 15 communes cibles du P2-P2RS au Sénégal. Forts de notre expérience dans les projets de gestion des ressources naturelles au Sahel, nous avons conçu une méthodologie qui s'ancre dans les réalités locales tout en répondant aux exigences de la Banque Africaine de Développement. Notre approche repose sur trois piliers fondamentaux : la participation communautaire, le renforcement des capacités locales et la durabilité des interventions. Nous mobiliserons une équipe pluridisciplinaire expérimentée dans les régions de Matam, Tambacounda et Fatick pour assurer un accompagnement de proximité efficace des Comités de Gestion Concertée des Ressources Naturelles (CGC/RN) et la mise en oeuvre réussie du Mécanisme de Gestion des Plaintes (MGP).",

        "context": u"""**Le Programme P2RS et son Contexte Régional**

Le Programme régional de résilience à l'insécurité alimentaire et nutritionnelle au Sahel (P2RS), initié par la Banque Africaine de Développement depuis 2014, constitue une réponse structurelle aux défis chroniques de sécurité alimentaire dans la région sahélienne. Le P2-P2RS (Projet 2) s'inscrit dans la continuité des acquis de la phase 1, avec un accent particulier sur la consolidation et l'élargissement des interventions dans 15 communes réparties dans les régions de Matam, Tambacounda et Fatick.

**Zones d'Intervention**

Le projet travaille autour de deux pôles de développement. Le Pôle Nord (Vallée du fleuve Sénégal) regroupe 12 communes : Matam (Agnam Civol, Dabia, Bokidiawé, Nguidjilone), Kanel (Aouré, Orkadjiéré, Sinthiou Bamambé, Ndendory) et Bakel (Bellé, Sinthiou Fissa, Gabou, Gathiary). Le Pôle Centre (Bassin arachidier) comprend 3 communes insulaires (Fimela, Bassoul, Djirnda) dans la région de Fatick, particulièrement vulnérables aux effets des changements climatiques.

**Cadre Institutionnel et Parties Prenantes**

Le projet s'inscrit dans le cadre de la politique nationale de décentralisation du Sénégal, avec les collectivités territoriales comme porte d'entrée principale. La stratégie d'intervention sera basée sur le « faire faire », impliquant fortement les services techniques nationaux. Les acteurs clés incluent : les services techniques déconcentrés (DRDR, IREF, SAED), les organisations de producteurs agricoles et pastoraux, les groupements de femmes, les autorités coutumières et religieuses, ainsi que les ONG locales.

**Problématique et Défis Majeurs**

Les communautés cibles font face à plusieurs défis interconnectés : (1) la dégradation continue des terres agricoles due à l'érosion hydrique et éolienne, la salinisation et la perte de fertilité ; (2) les conflits récurrents entre agriculteurs et éleveurs liés à la réduction des espaces pastoraux et à l'obstruction des couloirs de passage ; (3) la faible capacité organisationnelle des structures communautaires de gestion des ressources naturelles ; (4) l'insuffisance des connaissances en techniques de Gestion Durable des Terres (GDT) et d'agroécologie.

**Objectifs de la Mission**

L'objectif général est l'appui à l'opérationnalisation des Comités de Gestion Concertée des Ressources Naturelles (CGC/RN), la formation des acteurs à la gestion durable des ressources naturelles et des bonnes pratiques de GDT/agroécologie, et l'appui à la mise en oeuvre du Mécanisme de Gestion des Plaintes (MGP).""",

        "principles": [
            {
                "name": u"Approche Participative et Inclusive",
                "description": u"Toutes nos interventions seront fondées sur la participation effective des communautés à toutes les étapes : diagnostic, planification, mise en oeuvre et suivi. Nous accorderons une attention particulière à l'inclusion des groupes vulnérables, notamment les femmes et les jeunes, dans les instances de décision et les activités de renforcement des capacités."
            },
            {
                "name": u"Ancrage dans les Savoirs Locaux",
                "description": u"Notre méthodologie valorise et capitalise sur les connaissances endogènes des communautés en matière de gestion des ressources naturelles. Les pratiques traditionnelles validées seront intégrées aux innovations techniques proposées pour assurer une adaptation culturelle."
            },
            {
                "name": u"Adaptation au Contexte Local",
                "description": u"Reconnaissant la diversité des contextes agro-écologiques entre le Pôle Nord et le Pôle Centre, nous adapterons nos méthodes et contenus de formation aux spécificités de chaque zone. Les outils de communication seront développés dans les langues locales (Pulaar, Wolof, Sérère)."
            },
            {
                "name": u"Apprentissage par l'Action",
                "description": u"Notre programme de renforcement des capacités privilégie l'apprentissage pratique à travers les Champs Écoles Paysans (CEP) et les démonstrations sur le terrain, facilitant le transfert des connaissances et la démultiplication des pratiques."
            },
            {
                "name": u"Coordination et Synergie",
                "description": u"Nous assurerons une coordination étroite avec les services techniques déconcentrés, les autres partenaires du P2RS et les projets connexes intervenant dans les mêmes zones pour maximiser les complémentarités et mutualiser les ressources."
            },
            {
                "name": u"Équité Genre et Autonomisation",
                "description": u"L'intégration du genre sera transversale à toutes nos interventions. Les femmes représenteront au moins 40% des participants aux formations et au moins 30% des membres des instances de décision des CGC/RN."
            }
        ],

        "phases": [
            {
                "title": u"Phase 1 : Démarrage et Diagnostic Participatif",
                "description": u"Cette phase fondamentale de 4 mois permettra d'établir les bases solides de notre intervention à travers une compréhension approfondie du contexte socioéconomique et des dynamiques de gestion des ressources naturelles dans les 15 communes cibles. Nous procéderons à l'installation de nos équipes dans les trois régions (Matam, Tambacounda, Fatick) et établirons les premiers contacts avec les autorités locales et les communautés bénéficiaires. Le diagnostic participatif sera conduit selon une approche multi-acteurs intégrant les perceptions de tous les groupes d'intérêt.",
                "start_week": 1,
                "end_week": 16,
                "tasks": [
                    {
                        "code": "1A",
                        "title": u"Installation et cadrage méthodologique",
                        "description": u"L'activité de démarrage comprendra l'installation des bases opérationnelles dans les trois régions d'intervention. Nous procéderons au recrutement et à la formation de l'équipe locale (13 animateurs), à la mise en place des moyens logistiques et à l'établissement des protocoles de travail avec l'Unité de Coordination du Projet. Un atelier de lancement sera organisé avec les parties prenantes.",
                        "items": [
                            u"Installation des bases opérationnelles à Matam, Bakel et Fatick",
                            u"Recrutement et formation des 13 animateurs locaux",
                            u"Acquisition et déploiement des moyens logistiques",
                            u"Atelier de lancement avec les parties prenantes du P2RS",
                            u"Visites de courtoisie aux autorités des 15 communes"
                        ],
                        "start_week": 1,
                        "end_week": 4,
                        "deliverable_week": 4,
                        "deliverable_code": "L1"
                    },
                    {
                        "code": "1B",
                        "title": u"Études diagnostiques socioéconomiques",
                        "description": u"Le diagnostic socioéconomique sera conduit dans chacun des villages ciblés selon une méthodologie participative combinant : enquêtes ménages, focus groups différenciés (hommes, femmes, jeunes, éleveurs), entretiens avec les personnes ressources et observations directes. Nous analyserons les systèmes de production, les modes d'accès aux ressources naturelles et les dynamiques foncières.",
                        "items": [
                            u"Élaboration des outils de collecte de données",
                            u"Formation des enquêteurs sur les méthodologies participatives",
                            u"Réalisation des enquêtes ménages et focus groups dans les 15 communes",
                            u"Cartographie participative des ressources naturelles",
                            u"Analyse des données et rédaction des monographies communales"
                        ],
                        "start_week": 3,
                        "end_week": 12
                    },
                    {
                        "code": "1C",
                        "title": u"Inventaire des stratégies endogènes de GRN",
                        "description": u"Cette activité vise à documenter et valoriser les pratiques traditionnelles de gestion des ressources naturelles. Nous identifierons les règles coutumières de gestion des pâturages, des forêts et des points d'eau, les conventions locales existantes et les mécanismes traditionnels de résolution des conflits.",
                        "items": [
                            u"Recension des pratiques traditionnelles de GRN par zone",
                            u"Documentation des conventions locales existantes",
                            u"Identification des personnes ressources",
                            u"Analyse comparative des stratégies efficaces",
                            u"Élaboration d'un répertoire des bonnes pratiques"
                        ],
                        "start_week": 8,
                        "end_week": 14
                    },
                    {
                        "code": "1D",
                        "title": u"Restitution et validation du diagnostic",
                        "description": u"Les résultats du diagnostic seront restitués et validés lors d'ateliers participatifs organisés au niveau de chaque commune et au niveau régional. Ces ateliers permettront de confronter les analyses aux perceptions des acteurs locaux et de valider les orientations stratégiques.",
                        "items": [
                            u"Organisation de 15 ateliers communaux de restitution",
                            u"Organisation de 3 ateliers régionaux de validation",
                            u"Intégration des observations et corrections",
                            u"Finalisation des rapports de diagnostic par région",
                            u"Diffusion des résultats aux parties prenantes"
                        ],
                        "start_week": 13,
                        "end_week": 16,
                        "deliverable_week": 16,
                        "deliverable_code": "L2"
                    }
                ],
                "deliverables": [
                    {"code": "L1", "name": u"Rapport d'établissement avec recadrage méthodologique et planning actualisé"},
                    {"code": "L2", "name": u"Rapports de diagnostic socioéconomique et environnemental des 15 communes"}
                ]
            },
            {
                "title": u"Phase 2 : Mise en Place et Opérationnalisation des CGC/RN",
                "description": u"Cette phase de 6 mois constitue le coeur de notre intervention pour l'établissement d'un système durable de gestion concertée des ressources naturelles. Sur la base des résultats du diagnostic, nous procéderons à la mise en place ou à la redynamisation des Comités de Gestion Concertée des Ressources Naturelles (CGC/RN) dans chaque commune. Les règles de gestion concertée seront négociées et formalisées à travers des conventions locales.",
                "start_week": 17,
                "end_week": 40,
                "tasks": [
                    {
                        "code": "2A",
                        "title": u"Sensibilisation et mobilisation communautaire",
                        "description": u"Une vaste campagne d'information et de sensibilisation sera déployée dans les 15 communes pour expliquer les objectifs du projet et l'importance de la gestion concertée des ressources naturelles. Nous utiliserons des approches diversifiées : réunions villageoises, émissions radiophoniques, supports visuels et causeries thématiques.",
                        "items": [
                            u"Élaboration de la stratégie et des supports de communication",
                            u"Production d'émissions radiophoniques en Pulaar, Wolof et Sérère",
                            u"Organisation de réunions d'information dans chaque village",
                            u"Formation de relais communautaires",
                            u"Mise en place de panneaux d'information"
                        ],
                        "start_week": 17,
                        "end_week": 24
                    },
                    {
                        "code": "2B",
                        "title": u"Constitution et structuration des CGC/RN",
                        "description": u"Les CGC/RN seront mis en place ou redynamisés selon un processus transparent et participatif. Chaque CGC/RN comprendra des représentants des agriculteurs, éleveurs, exploitants forestiers, femmes, jeunes et autorités coutumières. Un bureau exécutif sera élu et les statuts seront élaborés de manière participative.",
                        "items": [
                            u"Évaluation des structures existantes de gestion des RN",
                            u"Facilitation des assemblées générales constitutives",
                            u"Élection des bureaux des CGC/RN (avec quota genre de 30%)",
                            u"Élaboration des statuts et règlements intérieurs",
                            u"Reconnaissance officielle des CGC/RN par les autorités"
                        ],
                        "start_week": 22,
                        "end_week": 32
                    },
                    {
                        "code": "2C",
                        "title": u"Négociation et élaboration des conventions locales",
                        "description": u"Les règles de gestion concertée seront négociées à travers des ateliers multi-acteurs. Ce processus portera sur : la délimitation des espaces, les règles d'accès et d'utilisation des ressources, les périodes de mise en défens, les sanctions et les mécanismes de surveillance.",
                        "items": [
                            u"Organisation d'ateliers de négociation multi-acteurs",
                            u"Facilitation des consensus sur les règles de gestion",
                            u"Rédaction des projets de conventions locales",
                            u"Validation participative des conventions",
                            u"Adoption des conventions par les conseils municipaux"
                        ],
                        "start_week": 28,
                        "end_week": 38
                    },
                    {
                        "code": "2D",
                        "title": u"Délimitation et matérialisation des espaces",
                        "description": u"Nous appuierons la délimitation et la matérialisation physique des espaces convenus : couloirs de passage du bétail, zones de pâturage, aires de repos, zones de mise en défens. Les cartes des terroirs seront produites et diffusées.",
                        "items": [
                            u"Cartographie participative des espaces par commune",
                            u"Identification et bornage des couloirs de passage",
                            u"Matérialisation des zones de pâturage et aires de repos",
                            u"Délimitation des zones de mise en défens",
                            u"Production et diffusion des cartes des terroirs"
                        ],
                        "start_week": 32,
                        "end_week": 40,
                        "deliverable_week": 40,
                        "deliverable_code": "L3"
                    }
                ],
                "deliverables": [
                    {"code": "L3", "name": u"15 CGC/RN opérationnels avec conventions locales adoptées et espaces délimités"}
                ]
            },
            {
                "title": u"Phase 3 : Formation et Renforcement des Capacités",
                "description": u"Cette phase de 12 mois est dédiée au renforcement des capacités des acteurs à tous les niveaux. Le programme couvrira les thématiques de la Gestion Durable des Terres (GDT), de l'agroécologie, de l'agroforesterie, de la Régénération Naturelle Assistée (RNA) et de la gestion des conflits. Notre approche privilégiera l'apprentissage par l'action à travers les Champs Écoles Paysans.",
                "start_week": 24,
                "end_week": 72,
                "tasks": [
                    {
                        "code": "3A",
                        "title": u"Élaboration du plan de renforcement des capacités",
                        "description": u"Sur la base des besoins identifiés lors du diagnostic, nous élaborerons un plan détaillé définissant les thématiques prioritaires, les approches pédagogiques, les contenus des modules et le calendrier des sessions.",
                        "items": [
                            u"Analyse des besoins de formation par groupe cible",
                            u"Définition des objectifs et contenus pédagogiques",
                            u"Identification des formateurs et personnes ressources",
                            u"Élaboration du calendrier de formation",
                            u"Validation du plan par l'UCP et les partenaires"
                        ],
                        "start_week": 24,
                        "end_week": 28,
                        "deliverable_week": 28,
                        "deliverable_code": "L4"
                    },
                    {
                        "code": "3B",
                        "title": u"Formation des formateurs et animateurs",
                        "description": u"Nous organiserons des sessions de formation des formateurs pour nos techniciens et animateurs ainsi que les agents des services techniques partenaires. Ces sessions couvriront les techniques de facilitation participative et les contenus techniques.",
                        "items": [
                            u"Session sur les techniques de facilitation (5 jours)",
                            u"Session technique sur la GDT et CES/DRS (5 jours)",
                            u"Session technique sur l'agroécologie et la RNA (5 jours)",
                            u"Session sur la production de plants agroforestiers (3 jours)",
                            u"Session sur la gestion des conflits et médiation (3 jours)"
                        ],
                        "start_week": 28,
                        "end_week": 36
                    },
                    {
                        "code": "3C",
                        "title": u"Formation des membres des CGC/RN",
                        "description": u"Les membres des 15 CGC/RN seront formés sur leurs rôles et responsabilités, les techniques de gouvernance locale, l'animation des réunions, la gestion des conflits et le suivi-évaluation participatif. Chaque CGC/RN bénéficiera d'au moins 10 jours de formation.",
                        "items": [
                            u"Module gouvernance et leadership (2 jours x 15 CGC/RN)",
                            u"Module techniques de GDT (3 jours x 15 CGC/RN)",
                            u"Module gestion des conflits (2 jours x 15 CGC/RN)",
                            u"Module suivi-évaluation participatif (2 jours x 15 CGC/RN)",
                            u"Visite d'échange inter-CGC/RN"
                        ],
                        "start_week": 36,
                        "end_week": 56
                    },
                    {
                        "code": "3D",
                        "title": u"Formation des producteurs via Champs Écoles Paysans",
                        "description": u"L'approche Champs Écoles Paysans (CEP) sera déployée pour former les producteurs aux techniques de GDT, d'agroécologie et d'agroforesterie. Chaque CEP regroupera 25 à 30 producteurs qui se réuniront régulièrement pendant une saison culturale complète.",
                        "items": [
                            u"Installation de 30 Champs Écoles Paysans (2 par commune)",
                            u"Sessions pratiques sur le compostage et la fertilité intégrée",
                            u"Sessions pratiques sur les ouvrages antiérosifs (cordons pierreux, zaï)",
                            u"Sessions pratiques sur la RNA et l'agroforesterie",
                            u"Évaluation participative des apprentissages"
                        ],
                        "start_week": 40,
                        "end_week": 72,
                        "deliverable_week": 72,
                        "deliverable_code": "L5"
                    }
                ],
                "deliverables": [
                    {"code": "L4", "name": u"Plan de renforcement des capacités validé avec modules de formation"},
                    {"code": "L5", "name": u"Rapport de formation avec 450 membres CGC/RN et 900 producteurs formés"}
                ]
            },
            {
                "title": u"Phase 4 : Accompagnement et Mise en Oeuvre du MGP",
                "description": u"Cette phase transversale de 20 mois est dédiée à l'accompagnement continu des CGC/RN dans la mise en oeuvre des conventions locales et l'opérationnalisation du Mécanisme de Gestion des Plaintes (MGP). Nos animateurs assureront un suivi de proximité régulier pour appuyer les comités dans l'application des règles négociées et la gestion des conflits.",
                "start_week": 20,
                "end_week": 96,
                "tasks": [
                    {
                        "code": "4A",
                        "title": u"Installation du dispositif MGP",
                        "description": u"Le Mécanisme de Gestion des Plaintes sera installé à trois niveaux : comités villageois, comités communaux et comité régional. Les organes seront dotés des outils nécessaires et les circuits de transmission des plaintes seront définis.",
                        "items": [
                            u"Identification des membres des comités de gestion des plaintes",
                            u"Organisation des assemblées d'installation des comités",
                            u"Dotation en matériels et outils de travail",
                            u"Mise en place des points de dépôt et du numéro vert",
                            u"Élaboration des procédures et circuits de traitement"
                        ],
                        "start_week": 20,
                        "end_week": 32
                    },
                    {
                        "code": "4B",
                        "title": u"Formation des membres des comités MGP",
                        "description": u"Les membres des comités de gestion des plaintes seront formés sur : la politique de gestion des plaintes, les procédures de réception et traitement, les techniques de médiation et de résolution amiable, et la documentation.",
                        "items": [
                            u"Formation sur la politique et les procédures du MGP (2 jours)",
                            u"Formation sur les techniques de médiation (2 jours)",
                            u"Formation sur la documentation et le rapportage (1 jour)",
                            u"Sessions de simulation et mise en situation",
                            u"Recyclage périodique des membres"
                        ],
                        "start_week": 28,
                        "end_week": 40,
                        "deliverable_week": 40,
                        "deliverable_code": "L6"
                    },
                    {
                        "code": "4C",
                        "title": u"Vulgarisation du MGP auprès des communautés",
                        "description": u"Une campagne intensive de vulgarisation sera déployée pour informer les populations sur l'existence du MGP, les types de plaintes recevables, les canaux de dépôt disponibles et les délais de traitement.",
                        "items": [
                            u"Production de spots radio sur le MGP en langues locales",
                            u"Conception et distribution d'affiches et dépliants illustrés",
                            u"Organisation de réunions d'information dans tous les villages",
                            u"Formation de relais communautaires pour la sensibilisation",
                            u"Rappels périodiques lors des activités du projet"
                        ],
                        "start_week": 36,
                        "end_week": 52
                    },
                    {
                        "code": "4D",
                        "title": u"Accompagnement des CGC/RN et suivi des conventions",
                        "description": u"Nos animateurs assureront un accompagnement régulier des CGC/RN : animation des réunions statutaires, application des conventions locales, gestion des infractions, mobilisation des ressources et reporting.",
                        "items": [
                            u"Visites hebdomadaires d'accompagnement des CGC/RN",
                            u"Appui à l'animation des réunions statutaires",
                            u"Suivi de l'application des conventions locales",
                            u"Facilitation de la résolution des conflits",
                            u"Appui à la mobilisation des ressources locales"
                        ],
                        "start_week": 40,
                        "end_week": 96
                    },
                    {
                        "code": "4E",
                        "title": u"Suivi-évaluation et capitalisation",
                        "description": u"Un dispositif de suivi-évaluation participatif sera mis en place pour mesurer les progrès et documenter les leçons apprises. Les rapports trimestriels synthétiseront les données et alimenteront les rapports à l'UCP.",
                        "items": [
                            u"Mise en place du système de suivi-évaluation",
                            u"Collecte et analyse des données de suivi",
                            u"Élaboration des rapports trimestriels d'activités",
                            u"Évaluations participatives avec les communautés",
                            u"Capitalisation et documentation des bonnes pratiques"
                        ],
                        "start_week": 12,
                        "end_week": 96,
                        "deliverable_week": 96,
                        "deliverable_code": "L7"
                    }
                ],
                "deliverables": [
                    {"code": "L6", "name": u"Dispositif MGP opérationnel avec comités formés et outils déployés"},
                    {"code": "L7", "name": u"8 rapports trimestriels d'activités et rapport final de capitalisation"}
                ]
            }
        ],

        "risks": u"""**Risques Contextuels**

- **Instabilité sécuritaire** : La région nord peut connaître des tensions liées aux mouvements transfrontaliers. Mesure d'atténuation : coordination étroite avec les autorités locales et adaptation des plannings de terrain.

- **Conditions climatiques défavorables** : Les aléas climatiques peuvent perturber les activités agricoles et les déplacements. Mesure d'atténuation : flexibilité du calendrier et priorisation des activités critiques.

- **Conflits intercommunautaires** : Les tensions agriculteurs-éleveurs peuvent s'intensifier. Mesure d'atténuation : renforcement de la médiation préventive et implication précoce des autorités coutumières.

**Risques Opérationnels**

- **Mobilisation insuffisante des communautés** : Les populations peuvent être réticentes à s'engager. Mesure d'atténuation : approche participative dès le diagnostic et communication intensive.

- **Turnover du personnel** : Le départ de membres clés peut affecter la continuité. Mesure d'atténuation : documentation systématique et partage des connaissances.

- **Difficultés logistiques** : L'enclavement de certaines communes peut compliquer les déplacements. Mesure d'atténuation : planification anticipée et moyens adaptés (pirogues pour les îles).

**Risques Institutionnels**

- **Faible appropriation par les autorités locales** : Les collectivités peuvent ne pas reconnaître les conventions locales. Mesure d'atténuation : implication dès le départ des maires et conseils municipaux.

- **Conflits de compétences** : Des chevauchements avec d'autres projets peuvent créer des tensions. Mesure d'atténuation : cartographie des acteurs et coordination régulière.

**Plan de Contingence**

En cas de survenance de risques majeurs, nous activerons notre plan de contingence comprenant : (1) réaffectation des ressources vers les zones accessibles ; (2) intensification des activités à distance ; (3) mobilisation de partenaires locaux relais ; (4) communication renforcée avec l'UCP pour adapter les cibles et le calendrier.""",

        "quality": u"""**Indicateurs Clés de Performance (KPIs)**

- Taux de fonctionnement des CGC/RN (réunions régulières, présence des membres) : cible 80%
- Taux de résolution des plaintes dans les délais : cible 90%
- Taux de satisfaction des bénéficiaires des formations : cible 85%
- Représentation des femmes dans les instances de décision : minimum 30%
- Taux d'application des conventions locales : cible 75%
- Nombre de producteurs formés via CEP : cible 900

**Mécanismes de Contrôle et Supervision**

- Supervision mensuelle du chef de mission dans chaque région
- Réunions hebdomadaires de coordination des techniciens
- Visites de terrain conjointes avec l'UCP (trimestrielles)
- Audits internes semestriels des activités
- Évaluations participatives semestrielles avec les communautés

**Protocoles de Reporting**

- Rapports hebdomadaires des animateurs (format standardisé)
- Rapports mensuels des techniciens avec données de suivi
- Rapports trimestriels consolidés à l'UCP (5 jours après fin trimestre)
- Base de données géoréférencée des interventions
- Photothèque et vidéothèque des activités

**Mesures Correctives**

En cas d'écarts constatés par rapport aux objectifs, nous mettrons en oeuvre des actions correctives immédiates : réaffectation des ressources, renforcement ciblé des capacités, adaptation des approches. Les non-conformités seront documentées et analysées pour amélioration continue."""
    }

    return methodology


if __name__ == "__main__":
    methodology = generate_methodology()
    lang_config = get_language_config('fr')
    output_path = "/Users/apple/metodologias-rfps/output/Methodologie_P2RS_Senegal.docx"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    create_word_document(methodology, output_path, lang_config)
    print(f"Document généré: {output_path}")
