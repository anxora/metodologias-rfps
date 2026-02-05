#!/usr/bin/env python3
"""
Generador de metodología para el proyecto P2-P2RS Senegal
Versión manual sin API - Metodología completa predefinida
"""

import os
import sys

# Agregar el directorio src al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from document_writer import create_word_document
from translations import get_language_config


METHODOLOGY = {
    "introduction": """Notre consortium propose une approche méthodologique intégrée et participative pour l'accompagnement des communautés des 15 communes cibles du P2-P2RS au Sénégal. Forts de notre expérience dans les projets de gestion des ressources naturelles au Sahel, nous avons conçu une méthodologie qui s'ancre dans les réalités locales tout en répondant aux exigences de la Banque Africaine de Développement. Notre approche repose sur trois piliers fondamentaux : la participation communautaire, le renforcement des capacités locales et la durabilité des interventions. Nous mobiliserons une équipe pluridisciplinaire expérimentée dans les régions de Matam, Tambacounda et Fatick pour assurer un accompagnement de proximité efficace des Comités de Gestion Concertée des Ressources Naturelles (CGC/RN) et la mise en œuvre réussie du Mécanisme de Gestion des Plaintes (MGP).""",

    "context": """**Contexte du Programme P2RS**

Le Programme régional de résilience à l'insécurité alimentaire et nutritionnelle au Sahel (P2RS), initié par la Banque Africaine de Développement depuis 2014, constitue une réponse structurelle aux défis chroniques de sécurité alimentaire dans la région sahélienne. Le P2-P2RS (Projet 2) s'inscrit dans la continuité des acquis de la phase 1, avec un accent particulier sur la consolidation et l'élargissement des interventions dans 15 communes réparties dans les régions de Matam, Tambacounda et Fatick.

**Zones d'intervention et enjeux spécifiques**

Le projet intervient dans deux pôles de développement distincts aux caractéristiques contrastées. Le **Pôle Nord** (Vallée du fleuve Sénégal) regroupe 12 communes dans les départements de Matam, Kanel et Bakel. Cette zone agro-écologique se caractérise par des systèmes agropastoraux transhumants, une forte dépendance aux ressources hydriques du fleuve Sénégal, et des défis liés à la dégradation des terres et aux conflits agriculteurs-éleveurs. Le **Pôle Centre** (Bassin arachidier) comprend 3 communes insulaires (Fimela, Bassoul, Djirnda) dans la région de Fatick, particulièrement vulnérables aux effets des changements climatiques, notamment la salinisation des terres et l'élévation du niveau de la mer.

**Cadre institutionnel et parties prenantes**

Le projet s'inscrit dans le cadre de la politique nationale de décentralisation du Sénégal, avec les collectivités territoriales comme porte d'entrée principale. Les acteurs clés incluent : les services techniques déconcentrés (DRDR, IREF, Service de l'élevage), les organisations de producteurs agricoles et pastoraux, les groupements de femmes, les autorités coutumières et religieuses, ainsi que les ONG locales actives dans la gestion des ressources naturelles. La coordination avec la SAED est particulièrement importante pour la zone Nord.

**Problématique et défis majeurs**

Les communautés cibles font face à plusieurs défis interconnectés : (1) la dégradation continue des terres agricoles due à l'érosion hydrique et éolienne, la salinisation et la perte de fertilité ; (2) les conflits récurrents entre agriculteurs et éleveurs liés à la réduction des espaces pastoraux et à l'obstruction des couloirs de passage ; (3) la faible capacité organisationnelle des structures communautaires de gestion des ressources naturelles ; (4) l'insuffisance des connaissances en techniques de Gestion Durable des Terres (GDT) et d'agroécologie ; et (5) l'absence de mécanismes efficaces de résolution des conflits et de gestion des plaintes.

**Objectifs de la mission**

Notre mission d'Opérateur de Proximité vise à : (1) opérationnaliser les Comités de Gestion Concertée des Ressources Naturelles dans les 15 communes cibles ; (2) former les acteurs aux bonnes pratiques de GDT, d'agroécologie et d'agroforesterie ; et (3) appuyer la mise en œuvre effective du Mécanisme de Gestion des Plaintes. Ces interventions contribueront directement à l'objectif global du P2RS d'amélioration des conditions de vie et de la sécurité alimentaire et nutritionnelle des populations sahéliennes.""",

    "principles": [
        {
            "name": "Approche participative et inclusive",
            "description": "Toutes nos interventions seront fondées sur la participation effective des communautés à toutes les étapes : diagnostic, planification, mise en œuvre et suivi. Nous accorderons une attention particulière à l'inclusion des groupes vulnérables, notamment les femmes et les jeunes, dans les instances de décision et les activités de renforcement des capacités. Cette approche garantit l'appropriation locale des actions et leur durabilité au-delà de la période du projet."
        },
        {
            "name": "Ancrage dans les savoirs locaux",
            "description": "Notre méthodologie valorise et capitalise sur les connaissances endogènes des communautés en matière de gestion des ressources naturelles. Les pratiques traditionnelles validées seront intégrées aux innovations techniques proposées. Cette approche de co-construction facilite l'acceptation et l'adoption des nouvelles pratiques tout en renforçant le sentiment d'appropriation des bénéficiaires."
        },
        {
            "name": "Adaptation au contexte local",
            "description": "Reconnaissant la diversité des contextes agro-écologiques entre le Pôle Nord (vallée du fleuve) et le Pôle Centre (îles du Saloum), nous adapterons nos méthodes et contenus de formation aux spécificités de chaque zone. Les outils de communication seront développés dans les langues locales (Pulaar, Wolof, Sérère) pour garantir une compréhension optimale par toutes les parties prenantes."
        },
        {
            "name": "Apprentissage par l'action",
            "description": "Notre programme de renforcement des capacités privilégie l'apprentissage pratique à travers les Champs Écoles Paysans et les démonstrations sur le terrain. Cette approche permet aux producteurs d'expérimenter directement les techniques de GDT, d'agroforesterie et de RNA dans leurs propres parcelles, facilitant ainsi le transfert des connaissances et la démultiplication des pratiques au sein des communautés."
        },
        {
            "name": "Coordination et synergie",
            "description": "Nous assurerons une coordination étroite avec les services techniques déconcentrés, les autres partenaires du P2RS et les projets connexes intervenant dans les mêmes zones. Cette synergie permettra d'éviter les duplications, de maximiser les complémentarités et de mutualiser les ressources pour un impact optimal. Des réunions régulières de coordination seront organisées avec l'Unité de Coordination du Projet."
        },
        {
            "name": "Équité genre et autonomisation",
            "description": "L'intégration du genre sera transversale à toutes nos interventions. Nous veillerons à ce que les femmes représentent au moins 40% des participants aux formations et au moins 30% des membres des instances de décision des CGC/RN. Un accent particulier sera mis sur le renforcement de l'accès des femmes aux ressources foncières et forestières non ligneuses, conformément aux orientations du projet."
        }
    ],

    "phases": [
        {
            "title": "Phase 1 : Démarrage et Diagnostic Participatif",
            "description": """Cette phase fondamentale de 4 mois permettra d'établir les bases solides de notre intervention à travers une compréhension approfondie du contexte socioéconomique et des dynamiques de gestion des ressources naturelles dans les 15 communes cibles. Nous procéderons à l'installation de nos équipes dans les trois régions (Matam, Tambacounda, Fatick) et établirons les premiers contacts avec les autorités locales et les communautés bénéficiaires. Le diagnostic participatif sera conduit selon une approche multi-acteurs intégrant les perceptions de tous les groupes d'intérêt (agriculteurs, éleveurs, pêcheurs, femmes, jeunes, autorités coutumières). Cette phase aboutira à une cartographie détaillée des ressources naturelles, des contraintes et des potentialités de chaque commune, ainsi qu'à l'identification des structures organisationnelles existantes à renforcer ou à créer.""",
            "start_week": 1,
            "end_week": 16,
            "tasks": [
                {
                    "code": "1A",
                    "title": "Installation et cadrage méthodologique",
                    "description": """L'activité de démarrage comprendra l'installation des bases opérationnelles dans les trois régions d'intervention. Nous procéderons au recrutement et à la formation de l'équipe locale (animateurs), à la mise en place des moyens logistiques (véhicules, motos, équipements) et à l'établissement des protocoles de travail avec l'Unité de Coordination du Projet. Un atelier de lancement sera organisé avec les parties prenantes pour présenter l'équipe, valider le plan de travail détaillé et établir les mécanismes de coordination. Les premières visites de courtoisie aux autorités administratives, coutumières et religieuses des 15 communes seront effectuées pour officialiser le démarrage des activités et solliciter leur appui.""",
                    "items": [
                        "Installation des bases opérationnelles à Matam, Bakel et Fatick",
                        "Recrutement et formation des 13 animateurs locaux",
                        "Acquisition et déploiement des moyens logistiques",
                        "Atelier de lancement avec les parties prenantes du P2RS",
                        "Visites de courtoisie aux autorités des 15 communes"
                    ],
                    "start_week": 1,
                    "end_week": 4,
                    "deliverable_week": 4,
                    "deliverable_code": "L1"
                },
                {
                    "code": "1B",
                    "title": "Études diagnostiques socioéconomiques",
                    "description": """Le diagnostic socioéconomique sera conduit dans chacun des villages ciblés selon une méthodologie participative combinant : enquêtes ménages, focus groups différenciés (hommes, femmes, jeunes, éleveurs), entretiens avec les personnes ressources et observations directes. Nous analyserons les systèmes de production (agriculture, élevage, pêche, foresterie), les modes d'accès et d'utilisation des ressources naturelles, les dynamiques foncières, les structures organisationnelles existantes et les conflits potentiels. Une attention particulière sera portée à l'identification des groupes vulnérables et à l'analyse des inégalités de genre dans l'accès aux ressources.""",
                    "items": [
                        "Élaboration des outils de collecte de données (questionnaires, guides d'entretien)",
                        "Formation des enquêteurs sur les méthodologies participatives",
                        "Réalisation des enquêtes ménages et focus groups dans les 15 communes",
                        "Cartographie participative des ressources naturelles",
                        "Analyse des données et rédaction des monographies communales"
                    ],
                    "start_week": 3,
                    "end_week": 12
                },
                {
                    "code": "1C",
                    "title": "Inventaire des stratégies endogènes de GRN",
                    "description": """Cette activité vise à documenter et valoriser les pratiques traditionnelles de gestion des ressources naturelles qui ont fait leurs preuves dans les communautés. Nous identifierons les règles coutumières de gestion des pâturages, des forêts et des points d'eau, les conventions locales existantes, les mécanismes traditionnels de prévention et de résolution des conflits, ainsi que les techniques agricoles et pastorales adaptées au contexte local. Cette capitalisation permettra d'ancrer nos interventions dans les réalités socioculturelles et de favoriser l'appropriation des innovations par les communautés.""",
                    "items": [
                        "Recension des pratiques traditionnelles de GRN par zone agro-écologique",
                        "Documentation des conventions locales et règles coutumières existantes",
                        "Identification des personnes ressources et détenteurs de savoirs locaux",
                        "Analyse comparative des stratégies endogènes efficaces",
                        "Élaboration d'un répertoire des bonnes pratiques locales"
                    ],
                    "start_week": 8,
                    "end_week": 14
                },
                {
                    "code": "1D",
                    "title": "Restitution et validation du diagnostic",
                    "description": """Les résultats du diagnostic seront restitués et validés lors d'ateliers participatifs organisés au niveau de chaque commune et au niveau régional. Ces ateliers permettront de confronter les analyses aux perceptions des acteurs locaux, d'enrichir les résultats par leurs observations et de valider les orientations stratégiques pour la suite de l'intervention. Les rapports de diagnostic finalisés constitueront la base documentaire pour l'élaboration des plans de renforcement des capacités et la définition des règles de gestion concertée des ressources naturelles.""",
                    "items": [
                        "Organisation de 15 ateliers communaux de restitution",
                        "Organisation de 3 ateliers régionaux de validation",
                        "Intégration des observations et corrections",
                        "Finalisation des rapports de diagnostic par région",
                        "Diffusion des résultats aux parties prenantes"
                    ],
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
            "description": """Cette phase de 6 mois constitue le cœur de notre intervention pour l'établissement d'un système durable de gestion concertée des ressources naturelles. Sur la base des résultats du diagnostic, nous procéderons à la mise en place ou à la redynamisation des Comités de Gestion Concertée des Ressources Naturelles (CGC/RN) dans chaque commune. Ce processus sera conduit de manière participative et inclusive, en veillant à la représentation équilibrée de tous les groupes d'utilisateurs des ressources (agriculteurs, éleveurs, exploitants forestiers, pêcheurs, femmes, jeunes). Les règles de gestion concertée seront négociées et formalisées à travers des conventions locales reconnues par les autorités administratives et coutumières.""",
            "start_week": 17,
            "end_week": 40,
            "tasks": [
                {
                    "code": "2A",
                    "title": "Sensibilisation et mobilisation communautaire",
                    "description": """Une vaste campagne d'information et de sensibilisation sera déployée dans les 15 communes pour expliquer les objectifs du projet et l'importance de la gestion concertée des ressources naturelles. Nous utiliserons des approches de communication diversifiées : réunions villageoises, émissions radiophoniques dans les langues locales, supports visuels (affiches, dépliants), théâtre communautaire et causeries thématiques. Cette sensibilisation vise à créer une prise de conscience collective sur les enjeux de dégradation des ressources et à mobiliser les communautés autour de solutions concertées.""",
                    "items": [
                        "Élaboration de la stratégie et des supports de communication",
                        "Production d'émissions radiophoniques en Pulaar, Wolof et Sérère",
                        "Organisation de réunions d'information dans chaque village",
                        "Formation de relais communautaires pour la sensibilisation continue",
                        "Mise en place de panneaux d'information dans les communes"
                    ],
                    "start_week": 17,
                    "end_week": 24
                },
                {
                    "code": "2B",
                    "title": "Constitution et structuration des CGC/RN",
                    "description": """Les CGC/RN seront mis en place ou redynamisés selon un processus transparent et participatif. Là où des structures existent déjà, nous procéderons à leur évaluation organisationnelle et leur redynamisation. Là où elles sont inexistantes, nous faciliterons leur création en veillant à une représentation inclusive de tous les groupes d'intérêt. Chaque CGC/RN comprendra des représentants des agriculteurs, éleveurs, exploitants forestiers, femmes, jeunes et autorités coutumières. Un bureau exécutif sera élu et les statuts et règlement intérieur seront élaborés de manière participative.""",
                    "items": [
                        "Évaluation des structures existantes de gestion des RN",
                        "Facilitation des assemblées générales constitutives",
                        "Élection des bureaux des CGC/RN (avec quota genre)",
                        "Élaboration des statuts et règlements intérieurs",
                        "Reconnaissance officielle des CGC/RN par les autorités"
                    ],
                    "start_week": 22,
                    "end_week": 32
                },
                {
                    "code": "2C",
                    "title": "Négociation et élaboration des conventions locales",
                    "description": """Les règles de gestion concertée des ressources naturelles seront négociées à travers des ateliers multi-acteurs regroupant tous les groupes d'utilisateurs. Ce processus de négociation portera sur : la délimitation des espaces (zones agricoles, pastorales, forestières), les règles d'accès et d'utilisation des ressources, les périodes de mise en défens, les sanctions en cas de non-respect, et les mécanismes de surveillance et d'application. Les conventions locales ainsi négociées seront formalisées et soumises à l'approbation des conseils municipaux pour leur conférer une légitimité institutionnelle.""",
                    "items": [
                        "Organisation d'ateliers de négociation multi-acteurs par commune",
                        "Facilitation des consensus sur les règles de gestion",
                        "Rédaction des projets de conventions locales",
                        "Validation participative des conventions locales",
                        "Adoption des conventions par les conseils municipaux"
                    ],
                    "start_week": 28,
                    "end_week": 38
                },
                {
                    "code": "2D",
                    "title": "Délimitation et matérialisation des espaces",
                    "description": """En lien avec les POAS existants ou en cours d'élaboration, nous appuierons la délimitation et la matérialisation physique des espaces convenus : couloirs de passage du bétail, zones de pâturage, aires de repos, zones de mise en défens, périmètres agroforestiers. Cette matérialisation se fera par des bornes, des plantations d'alignement ou d'autres marqueurs reconnus localement. Les cartes des terroirs intégrant ces délimitations seront produites et diffusées auprès des communautés et des services techniques.""",
                    "items": [
                        "Cartographie participative des espaces par commune",
                        "Identification et bornage des couloirs de passage",
                        "Matérialisation des zones de pâturage et aires de repos",
                        "Délimitation des zones de mise en défens",
                        "Production et diffusion des cartes des terroirs"
                    ],
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
            "description": """Cette phase de 8 mois est dédiée au renforcement des capacités des acteurs à tous les niveaux : membres des CGC/RN, producteurs, animateurs et agents des services techniques. Le programme de formation couvrira les thématiques de la Gestion Durable des Terres (GDT), de l'agroécologie, de l'agroforesterie, de la Régénération Naturelle Assistée (RNA) et de la gestion des conflits. Notre approche pédagogique privilégiera l'apprentissage par l'action à travers les Champs Écoles Paysans, les visites d'échange et les démonstrations pratiques sur le terrain. Des modules spécifiques seront développés pour les femmes et les jeunes afin de répondre à leurs besoins particuliers.""",
            "start_week": 24,
            "end_week": 56,
            "tasks": [
                {
                    "code": "3A",
                    "title": "Élaboration du plan de renforcement des capacités",
                    "description": """Sur la base des besoins identifiés lors du diagnostic et des orientations des TdR, nous élaborerons un plan détaillé de renforcement des capacités. Ce plan définira : les thématiques prioritaires par groupe cible, les approches pédagogiques adaptées, les contenus des modules de formation, le calendrier des sessions, les formateurs et facilitateurs à mobiliser, ainsi que les indicateurs de suivi des acquis. Le plan sera validé par l'UCP et les services techniques concernés avant sa mise en œuvre.""",
                    "items": [
                        "Analyse des besoins de formation par groupe cible",
                        "Définition des objectifs et contenus pédagogiques",
                        "Identification des formateurs et personnes ressources",
                        "Élaboration du calendrier de formation",
                        "Validation du plan par l'UCP et les partenaires"
                    ],
                    "start_week": 24,
                    "end_week": 28,
                    "deliverable_week": 28,
                    "deliverable_code": "L4"
                },
                {
                    "code": "3B",
                    "title": "Formation des formateurs et animateurs",
                    "description": """Avant de former les producteurs, nous organiserons des sessions de formation des formateurs pour nos techniciens et animateurs ainsi que les agents des services techniques partenaires. Ces sessions couvriront les techniques de facilitation participative, les contenus techniques (GDT, agroécologie, agroforesterie, RNA) et les méthodes d'accompagnement post-formation. Cette approche en cascade garantira la qualité et l'homogénéité des formations dispensées dans les trois régions d'intervention.""",
                    "items": [
                        "Session de formation sur les techniques de facilitation (5 jours)",
                        "Session technique sur la GDT et CES/DRS (5 jours)",
                        "Session technique sur l'agroécologie et la RNA (5 jours)",
                        "Session sur la production de plants agroforestiers (3 jours)",
                        "Session sur la gestion des conflits et médiation (3 jours)"
                    ],
                    "start_week": 28,
                    "end_week": 34
                },
                {
                    "code": "3C",
                    "title": "Formation des membres des CGC/RN",
                    "description": """Les membres des 15 CGC/RN seront formés sur leurs rôles et responsabilités, les techniques de gouvernance locale, l'animation des réunions, la gestion des conflits, le suivi-évaluation participatif et la mobilisation des ressources. Des modules spécifiques porteront sur les techniques de conservation et restauration des terres, la gestion des couloirs de passage et la mise en application des conventions locales. Chaque CGC/RN bénéficiera d'au moins 10 jours de formation répartis sur plusieurs sessions.""",
                    "items": [
                        "Module gouvernance et leadership (2 jours x 15 CGC/RN)",
                        "Module techniques de GDT (3 jours x 15 CGC/RN)",
                        "Module gestion des conflits (2 jours x 15 CGC/RN)",
                        "Module suivi-évaluation participatif (2 jours x 15 CGC/RN)",
                        "Visite d'échange inter-CGC/RN (1 jour)"
                    ],
                    "start_week": 32,
                    "end_week": 48
                },
                {
                    "code": "3D",
                    "title": "Formation des producteurs via Champs Écoles",
                    "description": """L'approche Champs Écoles Paysans (CEP) sera déployée pour former les producteurs aux techniques de GDT, d'agroécologie et d'agroforesterie. Chaque CEP regroupera 25 à 30 producteurs qui se réuniront régulièrement (bimensuellement) pendant une saison culturale complète pour pratiquer et analyser ensemble les différentes techniques. Les thèmes couvriront : le compostage, la gestion intégrée de la fertilité, les ouvrages antiérosifs, les bandes enherbées, la RNA, les associations de cultures et les techniques agroforestières.""",
                    "items": [
                        "Installation de 30 Champs Écoles Paysans (2 par commune)",
                        "Sessions pratiques sur le compostage et la fertilité intégrée",
                        "Sessions pratiques sur les ouvrages antiérosifs (cordons pierreux, zaï)",
                        "Sessions pratiques sur la RNA et l'agroforesterie",
                        "Évaluation participative des apprentissages"
                    ],
                    "start_week": 36,
                    "end_week": 56,
                    "deliverable_week": 56,
                    "deliverable_code": "L5"
                }
            ],
            "deliverables": [
                {"code": "L4", "name": "Plan de renforcement des capacités validé avec modules de formation"},
                {"code": "L5", "name": "Rapport de formation avec 450 membres CGC/RN et 900 producteurs formés"}
            ]
        },
        {
            "title": "Phase 4 : Accompagnement et Mise en Œuvre du MGP",
            "description": """Cette phase transversale de 20 mois, démarrant dès le 5ème mois et se poursuivant jusqu'à la fin du projet, est dédiée à l'accompagnement continu des CGC/RN dans la mise en œuvre des conventions locales et l'opérationnalisation du Mécanisme de Gestion des Plaintes (MGP). Nos animateurs assureront un suivi de proximité régulier pour appuyer les comités dans l'application des règles négociées, la gestion des conflits émergents et la consolidation de leur fonctionnement organisationnel. Parallèlement, nous mettrons en place le dispositif complet du MGP avec ses organes à différents niveaux (village, commune, région) et formerons les membres sur les procédures de collecte, traitement et résolution des plaintes.""",
            "start_week": 20,
            "end_week": 96,
            "tasks": [
                {
                    "code": "4A",
                    "title": "Installation du dispositif MGP",
                    "description": """Le Mécanisme de Gestion des Plaintes sera installé à trois niveaux : comités villageois, comités communaux et comité régional. Nous faciliterons l'identification et l'installation des membres selon des critères d'intégrité, de représentativité et de disponibilité. Les organes seront dotés des outils nécessaires (registres, fiches de plainte, téléphones) et les circuits de transmission des plaintes seront définis et communiqués aux populations. Un numéro vert et des points de dépôt physiques seront mis en place dans chaque commune.""",
                    "items": [
                        "Identification des membres des comités de gestion des plaintes",
                        "Organisation des assemblées d'installation des comités",
                        "Dotation en matériels et outils de travail",
                        "Mise en place des points de dépôt et du numéro vert",
                        "Élaboration des procédures et circuits de traitement"
                    ],
                    "start_week": 20,
                    "end_week": 32
                },
                {
                    "code": "4B",
                    "title": "Formation des membres des comités MGP",
                    "description": """Les membres des comités de gestion des plaintes à tous les niveaux seront formés sur : la politique de gestion des plaintes du projet, les types de plaintes recevables, les procédures de réception et d'enregistrement, les délais et modalités de traitement, les techniques de médiation et de résolution amiable, la documentation et le rapportage. Des sessions de simulation permettront de tester la maîtrise des procédures avant la mise en opération effective du mécanisme.""",
                    "items": [
                        "Formation sur la politique et les procédures du MGP (2 jours)",
                        "Formation sur les techniques de médiation (2 jours)",
                        "Formation sur la documentation et le rapportage (1 jour)",
                        "Sessions de simulation et mise en situation",
                        "Recyclage périodique des membres"
                    ],
                    "start_week": 28,
                    "end_week": 40,
                    "deliverable_week": 40,
                    "deliverable_code": "L6"
                },
                {
                    "code": "4C",
                    "title": "Vulgarisation du MGP auprès des communautés",
                    "description": """Une campagne intensive de vulgarisation sera déployée pour informer les populations sur l'existence du MGP, les types de plaintes recevables, les canaux de dépôt disponibles et les délais de traitement. Nous utiliserons des supports adaptés aux différents publics : spots radio en langues locales, affiches illustrées, réunions villageoises, crieurs publics. Cette vulgarisation sera continue tout au long du projet pour maintenir le niveau d'information des communautés.""",
                    "items": [
                        "Production de spots radio sur le MGP en langues locales",
                        "Conception et distribution d'affiches et dépliants illustrés",
                        "Organisation de réunions d'information dans tous les villages",
                        "Formation de relais communautaires pour la sensibilisation",
                        "Rappels périodiques lors des activités du projet"
                    ],
                    "start_week": 32,
                    "end_week": 52
                },
                {
                    "code": "4D",
                    "title": "Accompagnement des CGC/RN et suivi des conventions",
                    "description": """Nos animateurs assureront un accompagnement régulier des CGC/RN dans l'exercice de leurs fonctions : animation des réunions statutaires, application des conventions locales, gestion des infractions, mobilisation des ressources et reporting. Des visites de terrain hebdomadaires permettront d'identifier les difficultés et d'apporter les appuis nécessaires. Les conflits émergents seront traités selon les procédures établies avec implication des autorités compétentes si nécessaire.""",
                    "items": [
                        "Visites hebdomadaires d'accompagnement des CGC/RN",
                        "Appui à l'animation des réunions statutaires",
                        "Suivi de l'application des conventions locales",
                        "Facilitation de la résolution des conflits",
                        "Appui à la mobilisation des ressources locales"
                    ],
                    "start_week": 40,
                    "end_week": 96
                },
                {
                    "code": "4E",
                    "title": "Suivi-évaluation et capitalisation",
                    "description": """Un dispositif de suivi-évaluation participatif sera mis en place pour mesurer les progrès et documenter les leçons apprises. Les indicateurs clés porteront sur : le fonctionnement des CGC/RN, l'application des conventions locales, les superficies sous pratiques de GDT, le nombre de plaintes reçues et résolues, et la satisfaction des bénéficiaires. Les rapports trimestriels d'activités synthétiseront ces données et alimenteront les rapports à l'UCP. Une capitalisation des expériences sera réalisée en fin de projet.""",
                    "items": [
                        "Mise en place du système de suivi-évaluation",
                        "Collecte et analyse des données de suivi",
                        "Élaboration des rapports trimestriels d'activités",
                        "Évaluations participatives avec les communautés",
                        "Capitalisation et documentation des bonnes pratiques"
                    ],
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

    "risks": """**Catégories de risques identifiés**

**Risques contextuels**
- **Instabilité sécuritaire** : La région nord (Matam, Tambacounda) peut connaître des tensions liées aux mouvements transfrontaliers. Mesure d'atténuation : coordination étroite avec les autorités locales et adaptation des plannings de terrain selon l'évolution de la situation.
- **Conditions climatiques défavorables** : Les aléas climatiques (sécheresses, inondations) peuvent perturber les activités agricoles et les déplacements. Mesure d'atténuation : flexibilité du calendrier et priorisation des activités critiques pendant les fenêtres favorables.
- **Conflits intercommunautaires** : Les tensions agriculteurs-éleveurs peuvent s'intensifier, surtout pendant les périodes de transhumance. Mesure d'atténuation : renforcement de la médiation préventive et implication précoce des autorités coutumières.

**Risques opérationnels**
- **Mobilisation insuffisante des communautés** : Les populations peuvent être réticentes à s'engager dans les structures de gestion. Mesure d'atténuation : approche participative dès le diagnostic, communication intensive et valorisation des bénéfices concrets.
- **Turnover du personnel** : Le départ de membres clés de l'équipe peut affecter la continuité. Mesure d'atténuation : documentation systématique, partage des connaissances et conditions de travail attractives.
- **Difficultés logistiques** : L'enclavement de certaines communes (îles de Fatick) peut compliquer les déplacements. Mesure d'atténuation : planification anticipée, moyens adaptés (pirogues) et prépositionnement de matériel.

**Risques institutionnels**
- **Faible appropriation par les autorités locales** : Les collectivités territoriales peuvent ne pas reconnaître les conventions locales. Mesure d'atténuation : implication dès le départ des maires et conseils municipaux dans le processus.
- **Conflits de compétences** : Des chevauchements avec d'autres projets ou services techniques peuvent créer des tensions. Mesure d'atténuation : cartographie des acteurs, coordination régulière et complémentarité des interventions.

**Plan de contingence**
En cas de survenance de risques majeurs, nous activerons notre plan de contingence comprenant : (1) réaffectation des ressources vers les zones accessibles ; (2) intensification des activités à distance (formations radio, téléaccompagnement) ; (3) mobilisation de partenaires locaux relais ; (4) communication renforcée avec l'UCP pour adapter les cibles et le calendrier. Des réunions mensuelles de revue des risques permettront d'anticiper et de réagir rapidement aux évolutions.""",

    "quality": """**Système d'assurance qualité**

Notre dispositif d'assurance qualité repose sur trois piliers complémentaires :

**1. Indicateurs clés de performance (KPIs)**
- Taux de fonctionnement des CGC/RN (réunions régulières, présence des membres) : cible 80%
- Taux de résolution des plaintes dans les délais : cible 90%
- Taux de satisfaction des bénéficiaires des formations : cible 85%
- Superficie sous pratiques de GDT promues : selon cibles du projet
- Représentation des femmes dans les instances de décision : minimum 30%
- Taux d'application des conventions locales : cible 75%

**2. Mécanismes de contrôle et supervision**
- Supervision mensuelle du chef de mission dans chaque région
- Réunions hebdomadaires de coordination des techniciens
- Visites de terrain conjointes avec l'UCP (trimestrielles)
- Audits externes annuels des activités
- Évaluations participatives semestrielles avec les communautés

**3. Protocoles de reporting et documentation**
- Rapports hebdomadaires des animateurs (format standardisé)
- Rapports mensuels des techniciens avec données de suivi
- Rapports trimestriels consolidés à l'UCP (5 jours après fin trimestre)
- Base de données géoréférencée des interventions
- Photothèque et vidéothèque des activités

**4. Mesures correctives**
En cas d'écarts constatés par rapport aux objectifs, nous mettrons en œuvre des actions correctives immédiates : réaffectation des ressources, renforcement ciblé des capacités, adaptation des approches. Les non-conformités seront documentées et analysées pour amélioration continue."""
}


def main():
    """Génère la méthodologie pour le projet P2-P2RS Sénégal"""

    # Configuration en français
    lang_config = get_language_config('fr')

    print("Génération de la méthodologie pour le P2-P2RS Sénégal...")
    print("Langue: Français")
    print("Type: Développement rural / Gestion des ressources naturelles")

    # Créer le document Word
    output_path = "/Users/apple/metodologias-rfps/output/Methodologie_P2RS_Senegal.docx"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    create_word_document(METHODOLOGY, output_path, lang_config)

    print(f"\nDocument généré avec succès: {output_path}")


if __name__ == "__main__":
    main()
