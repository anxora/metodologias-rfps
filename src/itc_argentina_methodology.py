"""
Metodología específica para la Consultoría ITC - Mapeo de Polos de Innovación Social en Argentina
EU-LAC Social Accelerator - febrero-abril 2026
"""

import os
from document_writer import create_word_document
from translations import get_language_config


def generate_itc_argentina_methodology() -> dict:
    """
    Genera la metodología para la consultoría de mapeo de polos de innovación social en Argentina
    basada en los TdR del ITC/EU-LAC Social Accelerator
    """

    methodology = {
        "introduction": """Aninver Development Partners presenta su propuesta metodológica para la realización del mapeo y diagnóstico participativo del ecosistema de innovación social en Argentina, en el marco del proyecto EU-LAC Social Accelerator. Nuestro equipo de consultores fundamenta su aproximación en un enfoque sistémico que integra el análisis documental riguroso con metodologías participativas de investigación social, garantizando la aplicación transversal del enfoque transformador de género (GAP III), la interseccionalidad y los derechos humanos. Los consultores de Aninver combinan experiencia técnica en mapeo de ecosistemas de innovación, análisis de redes multiactor y diseño de instrumentos de investigación cuantitativa y cualitativa, con un profundo conocimiento del contexto latinoamericano y de los marcos estratégicos de la Unión Europea, particularmente la Agenda Global Gateway. Esta propuesta responde de manera precisa a los seis objetivos específicos establecidos en los TdR, articulando un proceso metodológico en cuatro fases que permitirá identificar y caracterizar polos de innovación social, generar una base de datos estructurada, elaborar un diagnóstico participativo del ecosistema, y proveer insumos técnicos clave para la hoja de ruta nacional.""",

        "context": """**El Proyecto EU-LAC Social Accelerator y el Contexto Argentino**

El proyecto EU-LAC Social Accelerator, financiado por la Comisión Europea en el marco de la Agenda Global Gateway, busca fortalecer los ecosistemas de innovación social en América Latina y el Caribe, promoviendo una transición verde y digital que sea justa, socialmente responsable e inclusiva. El consorcio implementador, conformado por CAINCO, Tecnalia, TEC de Monterrey, CACB, Caribbean Export y el Centro de Comercio Internacional (ITC), representa un modelo de cooperación UE-LAC orientado a la reducción de desigualdades y el fortalecimiento de la cohesión social, con especial énfasis en mujeres, jóvenes y grupos en situación de vulnerabilidad.

**Argentina: Un Ecosistema de Innovación Social Diverso y Maduro**

Argentina presenta uno de los ecosistemas de innovación social más desarrollados y diversos de América Latina, caracterizado por una sólida tradición de organizaciones de la sociedad civil, un sector académico de alto nivel, y un creciente movimiento de emprendimiento social e inversión de impacto. El país cuenta con una extensa red de universidades públicas y privadas con programas de investigación en innovación social, incubadoras y aceleradoras de impacto, y una economía social y solidaria con profundas raíces históricas. Las áreas temáticas prioritarias incluyen: empoderamiento económico de mujeres y juventudes, economía circular y sostenibilidad ambiental, inclusión financiera y microfinanzas, tecnología para el desarrollo social, educación y formación técnica, y agricultura familiar y soberanía alimentaria.

**Marco Normativo y Políticas Relevantes**

La consultoría se alinea con el Plan de Acción de Género III (GAP III) de la Unión Europea, incorporando los principios de interseccionalidad y derechos humanos. A nivel nacional, se articula con el marco normativo argentino en materia de economía social, incluyendo la Ley de Economía Social y Solidaria, las políticas de desarrollo productivo con inclusión, y los programas de apoyo al emprendedorismo social. El enfoque metodológico responde a los estándares del ePRAG 2025 y el Convenio de Subvención con la Comisión Europea.

**Objetivos del Mapeo y Diagnóstico**

Esta consultoría responde al Output 1.1 del Marco Lógico del proyecto: "Polos de innovación social desarrollados en ALC a partir de la experiencia de la UE". Los objetivos específicos incluyen: (OE1) identificar y mapear polos de innovación social activos o emergentes alineados con la Agenda Global Gateway; (OE2) desarrollar una base de datos estructurada desagregada por tipo de actor, enfoque, territorio y beneficiarios; (OE3) elaborar un diagnóstico participativo con análisis DAFO del ecosistema; (OE4) identificar necesidades, barreras y oportunidades de articulación, inversión e incidencia política; (OE5) proveer insumos técnicos para la hoja de ruta nacional; y (OE6) aportar a la línea de base para el monitoreo de impacto.

**Actores Clave del Ecosistema Argentino**

El mapeo abarcará la diversidad de actores que conforman el ecosistema: gobiernos (nacional, provinciales y municipales), organizaciones de la sociedad civil (fundaciones, asociaciones, cooperativas, mutuales, colectivos), sector privado (empresas, PyMEs, startups, empresas sociales, empresas B), academia (universidades públicas y privadas, centros de I+D, CONICET), plataformas de innovación (hubs, aceleradoras, incubadoras), cámaras empresariales, agencias de cooperación e inversores de impacto. La identificación priorizará aquellos actores que han integrado la igualdad de género como objetivo explícito y que promueven cambios estructurales hacia una transformación social equitativa.

**Integración de la Agenda Global Gateway**

De manera transversal, el proceso incorporará las prioridades temáticas de la Agenda Global Gateway: transición verde, transformación digital, desarrollo humano y social, y conectividad sostenible. Las herramientas de investigación permitirán clasificar actores e iniciativas según su contribución a estos ejes, así como su potencial de vinculación con mecanismos de financiamiento de la Unión Europea.""",

        "principles": [
            {
                "name": "Enfoque Transformador de Género (GAP III)",
                "description": "El equipo de Aninver aplica el Plan de Acción de Género III de la UE como marco transversal, asegurando que todas las fases del mapeo integren la perspectiva de género, identifiquen brechas y barreras específicas que enfrentan las mujeres en el ecosistema de innovación social argentino, y visibilicen liderazgos femeninos e iniciativas con enfoque de género explícito. Nuestros consultores desagregarán los datos por sexo y promoverán la participación equitativa en grupos focales y entrevistas."
            },
            {
                "name": "Interseccionalidad y Derechos Humanos",
                "description": "Nuestro equipo reconoce que las desigualdades se expresan de manera diferenciada según la intersección de múltiples factores (género, edad, origen étnico, condición socioeconómica, territorio). El enfoque metodológico de Aninver identifica cómo estas intersecciones afectan el acceso a oportunidades de innovación social en Argentina, priorizando la inclusión de jóvenes, pueblos originarios, comunidades rurales, poblaciones migrantes y otros grupos en situación de vulnerabilidad."
            },
            {
                "name": "Participación y Co-creación",
                "description": "Los consultores de Aninver construyen el mapeo y diagnóstico con los propios actores del ecosistema, no sobre ellos. Aplicamos metodologías participativas que reconocen los saberes locales, promueven el diálogo multiactor y generan apropiación de los resultados. Nuestros grupos focales, entrevistas y validaciones se diseñan para facilitar la participación activa de diversos tipos de actores, incluyendo aquellos tradicionalmente excluidos de los espacios de decisión."
            },
            {
                "name": "Alineación con Global Gateway",
                "description": "El equipo de Aninver integra explícitamente las prioridades de la Agenda Global Gateway en el diseño metodológico, clasificando actores e iniciativas según su contribución a la transición verde, transformación digital, desarrollo humano y social, y conectividad sostenible. Este alineamiento facilita la identificación de oportunidades de inversión y articulación con programas de la UE, potenciando el impacto del proyecto en Argentina."
            },
            {
                "name": "Rigor Metodológico y Evidencia",
                "description": "Nuestros consultores combinan métodos cuantitativos (encuestas digitales, matrices de datos) y cualitativos (entrevistas semiestructuradas, grupos focales, análisis DAFO) para triangular información y generar hallazgos robustos. El equipo de Aninver sigue protocolos de sistematización que garantizan la replicabilidad, comparabilidad y utilidad de los datos para el monitoreo de impacto del proyecto a lo largo del tiempo."
            },
            {
                "name": "Orientación a la Acción",
                "description": "Para Aninver, el mapeo y diagnóstico no son fines en sí mismos, sino insumos para la acción. Nuestro equipo prioriza la generación de recomendaciones prácticas, viables y priorizadas para la hoja de ruta nacional argentina, identificando oportunidades concretas de articulación, inversión e incidencia política que fortalezcan el ecosistema de innovación social del país."
            }
        ],

        "phases": [
            {
                "title": "Fase 1: Revisión Documental y Diagnóstico Ex Ante",
                "description": """El equipo de consultores de Aninver iniciará esta fase con el propósito de comprender a profundidad el contexto nacional y regional de la innovación social en Argentina. Nuestros especialistas analizarán el marco lógico del proyecto, documentos metodológicos del consorcio EU-LAC, políticas vinculadas al Global Gateway y GAP III, así como el estudio de mejores prácticas europeas sistematizadas por TECNALIA. Paralelamente, el equipo realizará investigación de fuentes secundarias sobre el ecosistema argentino, incluyendo informes previos sobre innovación social, economía social y solidaria, género, juventudes y grupos vulnerables. El producto de esta fase será el Diagnóstico Ex Ante del Contexto, que establecerá la línea base para las fases subsiguientes e incluirá la identificación preliminar de actores para el grupo semilla.""",
                "start_week": 1,
                "end_week": 2,
                "tasks": [
                    {
                        "code": "1A",
                        "title": "Elaboración del plan de trabajo y revisión documental inicial",
                        "description": """El equipo de Aninver elaborará el plan de trabajo detallado de la consultoría, definiendo el cronograma específico, el enfoque metodológico y la estrategia de validación con el ITC. Simultáneamente, nuestros consultores iniciarán el análisis sistemático de la documentación proporcionada por el ITC, incluyendo el marco lógico del proyecto EU-LAC Social Accelerator con sus indicadores y metas, los manuales técnicos y metodológicos del consorcio, las políticas marco del Global Gateway y el Plan de Acción de Género III, y el convenio de subvención con la Comisión Europea. Este análisis permitirá al equipo identificar los requisitos específicos de reporte y las expectativas de calidad que guiarán la ejecución de la consultoría.""",
                        "items": [],
                        "start_week": 1,
                        "end_week": 1,
                        "deliverable_week": 1,
                        "deliverable_code": "P1"
                    },
                    {
                        "code": "1B",
                        "title": "Investigación de fuentes secundarias del contexto argentino",
                        "description": """Nuestro equipo de investigadores conducirá una exhaustiva revisión de fuentes secundarias para construir una visión integral del ecosistema de innovación social argentino. Los consultores de Aninver analizarán informes de organismos multilaterales como BID, PNUD, CEPAL y CAF, estudios académicos de universidades argentinas, y diagnósticos previos elaborados por organizaciones como ACIJ, CIPPEC, Ashoka Argentina y la Red de Innovación Local. El equipo revisará el marco normativo nacional, incluyendo la Ley de Economía Social y Solidaria, legislación sobre cooperativas y mutuales, y las políticas provinciales de apoyo al emprendimiento social. Esta investigación permitirá caracterizar las particularidades del federalismo argentino y las diferencias regionales en el desarrollo de la innovación social.""",
                        "items": [],
                        "start_week": 1,
                        "end_week": 2
                    },
                    {
                        "code": "1C",
                        "title": "Diagnóstico ex ante e identificación del grupo semilla",
                        "description": """A partir de los hallazgos de la revisión documental, el equipo de Aninver elaborará el Diagnóstico Ex Ante del Contexto y realizará el mapeo preliminar de actores clave del ecosistema de innovación social en Argentina. Nuestros consultores aplicarán criterios de diversidad sectorial (OSC, academia, empresas, gobierno), cobertura territorial (considerando la estructura federal del país y las diferencias entre regiones), balance de género y variedad de tipos de organización para conformar el grupo semilla inicial de 10-15 actores representativos. El equipo priorizará organizaciones con capacidad articuladora y trayectoria demostrada, asegurando representación de distintas provincias y regiones del país.""",
                        "items": [],
                        "start_week": 2,
                        "end_week": 2,
                        "deliverable_week": 2,
                        "deliverable_code": "P2"
                    }
                ],
                "deliverables": [
                    {"code": "P1", "name": "Plan de trabajo detallado: cronograma, enfoque metodológico y estrategia de validación"},
                    {"code": "P2", "name": "Diagnóstico Ex Ante del Contexto y Herramientas de recolección validadas"}
                ]
            },
            {
                "title": "Fase 2: Diseño y Afinación de Herramientas",
                "description": """En esta fase, el equipo de Aninver se concentrará en la preparación metodológica rigurosa para el trabajo de campo en Argentina. Nuestros especialistas trabajarán con los instrumentos base proporcionados por el ITC —la encuesta digital del Anexo B y la guía de entrevistas semiestructuradas del Anexo C— para adaptarlos al contexto específico argentino, considerando las particularidades del federalismo, la diversidad regional y la terminología local. Los consultores realizarán una prueba piloto con un grupo reducido de actores para validar la claridad, pertinencia y funcionalidad de los instrumentos antes de su despliegue masivo.""",
                "start_week": 2,
                "end_week": 3,
                "tasks": [
                    {
                        "code": "2A",
                        "title": "Revisión y adaptación de encuesta digital al contexto argentino",
                        "description": """El equipo metodológico de Aninver realizará un análisis detallado de las siete secciones del formulario de encuesta digital (Anexo B), evaluando su pertinencia para el contexto argentino. Nuestros consultores propondrán ajustes específicos basados en los hallazgos del diagnóstico ex ante: adaptarán las categorías de actores para reflejar las particularidades del ecosistema local (incluyendo cooperativas, mutuales, empresas B, organizaciones de la economía popular), verificarán que las opciones territoriales contemplen la estructura federal del país, y asegurarán que las preguntas sobre articulación capturen las dinámicas de colaboración existentes entre distintos niveles de gobierno y sectores.""",
                        "items": [],
                        "start_week": 2,
                        "end_week": 2
                    },
                    {
                        "code": "2B",
                        "title": "Prueba piloto del instrumento de encuesta",
                        "description": """Antes del despliegue masivo, el equipo de Aninver aplicará la encuesta a un grupo piloto de 5-8 actores seleccionados del grupo semilla, asegurando diversidad geográfica y sectorial. Esta prueba piloto tiene un doble propósito: validar aspectos técnicos como el tiempo promedio de respuesta, la claridad de las preguntas y la completitud de las opciones; y evaluar la calidad de los datos obtenidos y su utilidad para los análisis previstos. Los consultores documentarán sistemáticamente las observaciones de los participantes piloto, identificarán puntos de confusión o fricción —particularmente en terminología y categorías de respuesta—, y propondrán los ajustes finales necesarios.""",
                        "items": [],
                        "start_week": 2,
                        "end_week": 3
                    },
                    {
                        "code": "2C",
                        "title": "Revisión de guía de entrevistas DAFO",
                        "description": """Los especialistas cualitativos de Aninver revisarán y adaptarán la Guía de Entrevistas Semiestructuradas (Anexo C) para el diagnóstico DAFO en el contexto argentino. El equipo asegurará que las preguntas capturen información relevante sobre las cinco dimensiones estratégicas: gobernanza y articulación interinstitucional (considerando el federalismo), capacidades técnicas e institucionales, inclusión social y enfoque de género, sostenibilidad financiera y acceso a inversiones, e innovación tecnológica y transformación digital. Nuestros consultores definirán los criterios de selección de actores a entrevistar, priorizando representatividad regional y sectorial.""",
                        "items": [],
                        "start_week": 2,
                        "end_week": 3
                    },
                    {
                        "code": "2D",
                        "title": "Preparación logística para trabajo de campo",
                        "description": """El equipo operativo de Aninver se encargará de toda la planificación logística necesaria para el trabajo de campo en un país de la extensión geográfica de Argentina. Nuestros consultores configurarán la plataforma digital para la administración de encuestas, diseñarán una estrategia de difusión diferenciada por región que maximice la tasa de respuesta, y prepararán los materiales de presentación del proyecto EU-LAC Social Accelerator adaptados al contexto local. El equipo establecerá canales de comunicación directos con el grupo semilla y coordinará con el ITC para acceder a sus redes de contactos en Argentina, incluyendo organizaciones en distintas provincias.""",
                        "items": [],
                        "start_week": 3,
                        "end_week": 3
                    }
                ],
                "deliverables": [
                    {"code": "P2", "name": "Herramientas de recolección validadas: encuesta digital revisada, guía de entrevistas DAFO, matriz de recolección"}
                ]
            },
            {
                "title": "Fase 3: Trabajo de Campo",
                "description": """Esta fase representa el núcleo operativo de la consultoría, donde el equipo de Aninver desplegará las herramientas de mapeo y diagnóstico en el territorio argentino. Nuestros consultores iniciarán con la aplicación de encuestas al grupo semilla, expandiendo progresivamente el universo de actores mediante la técnica de bola de nieve, con especial atención a lograr cobertura en distintas regiones del país. Toda la información cuantitativa será sistematizada en formato Excel según los estándares del ITC. De manera simultánea, el equipo conducirá entrevistas semiestructuradas a actores clave para alimentar el diagnóstico DAFO, y facilitará grupos focales por área temática que permitan profundizar en la comprensión del ecosistema.""",
                "start_week": 3,
                "end_week": 8,
                "tasks": [
                    {
                        "code": "3A",
                        "title": "Aplicación de encuestas al grupo semilla y expansión territorial",
                        "description": """El equipo de campo de Aninver lanzará la encuesta digital al grupo semilla inicial proporcionado por el ITC, activando simultáneamente el mecanismo de bola de nieve: cada respondente nominará hasta tres instituciones con las que colabora regularmente, generando así nuevos contactos para encuestar en distintas provincias y regiones. Nuestros consultores implementarán un sistema de seguimiento multicanal para maximizar la tasa de respuesta y asegurar la completitud de los formularios. El equipo monitoreará continuamente la representatividad de la muestra por tipo de actor, territorio (asegurando cobertura de múltiples provincias) y género, realizando búsquedas activas complementarias cuando se identifiquen vacíos en la cobertura regional.""",
                        "items": [],
                        "start_week": 3,
                        "end_week": 5,
                        "deliverable_week": 5,
                        "deliverable_code": "P3"
                    },
                    {
                        "code": "3B",
                        "title": "Sistematización de encuestas y análisis preliminar",
                        "description": """Una vez alcanzado el volumen crítico de respuestas (mínimo 60-100 encuestas completas), el equipo analítico de Aninver procesará los datos para generar el documento de sistematización (P3) y el reporte de análisis preliminar de actores (P4). Nuestros consultores realizarán la limpieza y validación de datos, aplicarán controles de consistencia, y ejecutarán la desagregación por las variables clave: género, edad, tipo de actor, provincia/región, área temática, nivel de articulación, enfoque de género y poblaciones beneficiarias. El análisis clasificará a los actores identificando roles diferenciados y construirá un mapa de relaciones que permita identificar clusters regionales y patrones de colaboración.""",
                        "items": [],
                        "start_week": 5,
                        "end_week": 6,
                        "deliverable_week": 6,
                        "deliverable_code": "P4"
                    },
                    {
                        "code": "3C",
                        "title": "Identificación y caracterización de polos de innovación",
                        "description": """Aplicando la metodología desarrollada por el Tecnológico de Monterrey —socio del consorcio EU-LAC—, el equipo de Aninver analizará la información recopilada para identificar polos de innovación social existentes o emergentes en Argentina, tanto territoriales como temáticos. Los criterios de identificación incluirán: densidad de articulación entre actores, concentración territorial (a nivel provincial o metropolitano), convergencia temática, capacidad demostrada de escalamiento, y potencial de atracción de inversiones. Nuestros consultores caracterizarán al menos tres polos, documentando para cada uno: los actores participantes, el nivel de madurez institucional, la integración del enfoque de género, y la alineación con los ejes del Global Gateway.""",
                        "items": [],
                        "start_week": 6,
                        "end_week": 7,
                        "deliverable_week": 7,
                        "deliverable_code": "P5"
                    },
                    {
                        "code": "3D",
                        "title": "Entrevistas semiestructuradas para diagnóstico DAFO",
                        "description": """El equipo cualitativo de Aninver conducirá entre 15 y 20 entrevistas a profundidad con actores clave identificados en las encuestas, asegurando diversidad regional y sectorial. Utilizando la guía del Anexo C, nuestros consultores explorarán las cinco dimensiones del diagnóstico DAFO: gobernanza y articulación interinstitucional (incluyendo dinámicas entre niveles de gobierno en el contexto federal), capacidades técnicas e institucionales, inclusión social y enfoque de género, sostenibilidad financiera y acceso a inversiones, e innovación tecnológica y transformación digital. La selección de entrevistados priorizará actores articuladores de cada polo identificado, asegurando representación de distintas regiones del país.""",
                        "items": [],
                        "start_week": 6,
                        "end_week": 8
                    },
                    {
                        "code": "3E",
                        "title": "Grupos focales de diagnóstico del ecosistema",
                        "description": """Los facilitadores de Aninver organizarán y conducirán grupos focales con actores del ecosistema argentino, segmentados por área temática prioritaria. El equipo realizará entre tres y cuatro sesiones virtuales o híbridas para facilitar la participación de actores de distintas provincias, cada una con participantes de diferentes tipos de organización (OSC, academia, empresas, gobierno) para asegurar la pluralidad de voces. La metodología de facilitación promoverá la construcción colectiva del análisis DAFO, permitiendo que los propios actores identifiquen y prioricen las fortalezas, debilidades, oportunidades y amenazas del ecosistema desde su experiencia directa, considerando las particularidades regionales.""",
                        "items": [],
                        "start_week": 7,
                        "end_week": 8,
                        "deliverable_week": 8,
                        "deliverable_code": "P6"
                    }
                ],
                "deliverables": [
                    {"code": "P3", "name": "Documento de sistematización de encuestas: archivo Excel con 60-100 encuestas completas desagregadas"},
                    {"code": "P4", "name": "Reporte de análisis preliminar de actores: clasificación, líderes, promotores y mapa de relaciones"},
                    {"code": "P5", "name": "Informe de identificación y caracterización de polos de innovación social (mínimo 3 polos)"},
                    {"code": "P6", "name": "Informe de sistematización de grupos focales y entrevistas contextuales"}
                ]
            },
            {
                "title": "Fase 4: Análisis, Informes y Productos Finales",
                "description": """En esta fase conclusiva, el equipo de Aninver consolidará todos los resultados del trabajo de campo en los productos definitivos del proyecto. Nuestros consultores elaborarán el análisis DAFO integral del ecosistema argentino, el diagnóstico ex post con enfoque GAP III, la línea de base nacional, y el informe final consolidado. Los documentos no solo describirán hallazgos, sino que formularán recomendaciones estratégicas priorizadas para fortalecer el ecosistema y proveerán insumos técnicos concretos para la construcción de la hoja de ruta nacional de Argentina.""",
                "start_week": 8,
                "end_week": 10,
                "tasks": [
                    {
                        "code": "4A",
                        "title": "Elaboración del análisis DAFO del ecosistema",
                        "description": """El equipo analítico de Aninver sintetizará toda la información cualitativa recopilada —entrevistas y grupos focales— para construir el diagnóstico DAFO integral del ecosistema de innovación social argentino. Nuestros consultores abordarán las cinco dimensiones estratégicas definidas en los TdR, triangulando la información de fuentes primarias con los hallazgos de la revisión documental. El análisis considerará las particularidades del federalismo argentino y las diferencias regionales, cruzando el DAFO con el enfoque GAP III para identificar fortalezas, debilidades, oportunidades y amenazas específicas desde la perspectiva de género e interseccionalidad.""",
                        "items": [],
                        "start_week": 8,
                        "end_week": 9,
                        "deliverable_week": 9,
                        "deliverable_code": "P7"
                    },
                    {
                        "code": "4B",
                        "title": "Diagnóstico ex post de oportunidades y brechas (GAP III)",
                        "description": """Los especialistas en género de Aninver elaborarán el diagnóstico ex post con foco específico en la inclusión de mujeres, jóvenes y grupos vulnerables en el ecosistema de innovación social argentino. El análisis identificará las brechas de participación por género y edad, las barreras estructurales que limitan el acceso de poblaciones vulnerables —incluyendo pueblos originarios, migrantes y población de zonas rurales—, y las oportunidades concretas de empoderamiento económico. Nuestros consultores documentarán las buenas prácticas identificadas durante el trabajo de campo y formularán recomendaciones específicas para transversalizar el enfoque de género en las acciones futuras del proyecto.""",
                        "items": [],
                        "start_week": 9,
                        "end_week": 9,
                        "deliverable_week": 9,
                        "deliverable_code": "P8"
                    },
                    {
                        "code": "4C",
                        "title": "Construcción de la línea de base del ecosistema",
                        "description": """El equipo de monitoreo y evaluación de Aninver elaborará el documento técnico de línea de base nacional, diseñado para ser compatible con el sistema de seguimiento e impacto del consorcio EU-LAC. La línea de base incluirá indicadores alineados con el Output 1.1 del marco lógico: número de polos de innovación social identificados y su nivel de madurez (desagregados por región), instituciones con potencial de ser capacitadas, estimación de población beneficiaria directa e indirecta desagregada por sexo y edad, e inventario de iniciativas con potencial de pilotaje. Nuestros consultores documentarán la metodología de cálculo de cada indicador y entregarán el producto en formato Word y Excel.""",
                        "items": [],
                        "start_week": 9,
                        "end_week": 10,
                        "deliverable_week": 10,
                        "deliverable_code": "P9"
                    },
                    {
                        "code": "4D",
                        "title": "Elaboración del informe final consolidado",
                        "description": """El equipo de redacción de Aninver integrará todos los hallazgos, análisis y productos parciales en el Informe Final Consolidado de Mapeo y Diagnóstico del Ecosistema de Innovación Social de Argentina. El documento incluirá una síntesis ejecutiva orientada a tomadores de decisión, la descripción detallada de la metodología aplicada, la caracterización integral del ecosistema y sus actores (con perspectiva regional), el análisis de los polos identificados, el diagnóstico DAFO completo, el análisis desde el enfoque GAP III, los indicadores de línea de base, y las recomendaciones estratégicas para la construcción de la hoja de ruta nacional. Nuestros consultores incorporarán mapas geográficos, gráficos y visualizaciones que faciliten la comprensión de los hallazgos.""",
                        "items": [],
                        "start_week": 10,
                        "end_week": 10,
                        "deliverable_week": 10,
                        "deliverable_code": "P10"
                    }
                ],
                "deliverables": [
                    {"code": "P7", "name": "Informe de análisis DAFO del ecosistema y diagnóstico de fuentes primarias"},
                    {"code": "P8", "name": "Diagnóstico ex post de oportunidades y brechas desde enfoque GAP III"},
                    {"code": "P9", "name": "Línea de base del ecosistema: documento técnico con variables e indicadores (Word y Excel)"},
                    {"code": "P10", "name": "Informe final consolidado: mapeo y diagnóstico del ecosistema con anexos técnicos"}
                ]
            }
        ],

        "risks": """**Identificación y Gestión de Riesgos**

El equipo de Aninver ha identificado los principales riesgos asociados a la ejecución de esta consultoría en el contexto argentino y propone medidas de mitigación específicas para cada uno:

**Riesgos Metodológicos**

*Baja tasa de respuesta a encuestas*: Existe el riesgo de no alcanzar las 60-100 encuestas completas requeridas, particularmente en regiones alejadas de los centros urbanos principales. Para mitigar este riesgo, nuestros consultores implementarán una estrategia de contacto multicanal, activarán redes de organizaciones paraguas con presencia federal, y realizarán seguimiento diferenciado por región. El equipo de Aninver coordinará con el ITC para acceder a sus redes de contactos en Argentina.

*Sesgos hacia Buenos Aires y grandes centros urbanos*: La técnica bola de nieve puede generar sesgos hacia actores concentrados en CABA y Buenos Aires, subrepresentando otras provincias. Nuestro equipo complementará esta técnica con búsqueda activa de actores en otras regiones, estableciendo cuotas mínimas de participación por macro-región y monitoreando continuamente la representatividad territorial.

*Información incompleta o de baja calidad*: Los actores pueden proporcionar información parcial o inexacta. Los consultores de Aninver triangularán información de múltiples fuentes, aplicarán validaciones cruzadas, y profundizarán mediante entrevistas cuando se identifiquen inconsistencias.

**Riesgos Operativos**

*Dificultades de acceso a actores en provincias alejadas*: Argentina presenta una extensa geografía con zonas de conectividad limitada. El equipo priorizará modalidades virtuales para actores de provincias distantes, flexibilizando horarios y canales para facilitar la participación de organizaciones en todas las regiones del país.

*Retrasos en validación de productos con ITC*: Los tiempos de revisión y aprobación podrían afectar el cronograma. Nuestros consultores establecerán canales de comunicación fluidos con el equipo ITC, entregarán versiones preliminares para retroalimentación temprana, y mantendrán flexibilidad en el cronograma interno.

**Riesgos de Contexto**

*Contexto económico volátil*: La situación económica argentina podría afectar la disponibilidad de actores para participar o la operatividad de organizaciones. El equipo monitoreará activamente el contexto durante la consultoría y adaptará las estrategias de contacto y participación según sea necesario.

*Sensibilidades en temas de género y derechos humanos*: Algunos actores pueden mostrar resistencia al enfoque GAP III. Nuestros consultores comunicarán de manera clara el marco conceptual del proyecto, enfatizando su alineación con compromisos internacionales y aplicando sensibilidad cultural en el abordaje de estos temas.

**Plan de Contingencia**

En caso de materializarse riesgos críticos que afecten la entrega de productos, el equipo de Aninver activará: (1) comunicación inmediata con ITC para acordar ajustes, (2) reasignación de recursos del equipo consultor, (3) ajuste consensuado de alcance o cronograma, y (4) activación de redes alternativas de contactos.""",

        "quality": """**Aseguramiento de Calidad**

El equipo de Aninver implementará un sistema riguroso de aseguramiento de calidad para garantizar que todos los productos cumplan con los estándares técnicos del proyecto EU-LAC Social Accelerator y sean útiles para los fines del mapeo y diagnóstico en Argentina.

**Indicadores Clave de Desempeño (KPIs)**

Nuestros consultores monitorearán los siguientes indicadores durante la ejecución:

- Tasa de respuesta de encuestas: mínimo 60 encuestas completas, meta 100
- Desagregación por género: mínimo 40% de respondentes mujeres
- Cobertura territorial: representación de al menos 10 provincias argentinas
- Diversidad de actores: mínimo 5 tipos de organizaciones representadas
- Tasa de completitud de datos: mínimo 90% de campos obligatorios completos
- Número de entrevistas a profundidad: mínimo 15-20 entrevistas
- Grupos focales realizados: mínimo 3 por área temática
- Polos identificados: mínimo 3 con caracterización completa

**Mecanismos de Control de Calidad**

*Revisión por pares*: Cada producto será revisado por al menos dos miembros del equipo de Aninver antes de su entrega, verificando consistencia metodológica, calidad de redacción y alineación con los TdR.

*Validación con actores*: Los hallazgos preliminares serán validados con actores clave del ecosistema argentino para verificar su pertinencia, precisión y utilidad práctica.

*Verificación de datos*: El equipo implementará controles de consistencia en las bases de datos, validando rangos, formatos y coherencia de respuestas, con corrección de errores antes de los análisis.

*Alineación con TdR*: Cada producto será cotejado con los requisitos específicos de los términos de referencia y los formatos establecidos en los Anexos.

**Protocolo de Entregas**

El proceso de entrega de cada producto seguirá el siguiente protocolo: (1) autoevaluación de calidad por el equipo consultor; (2) envío de versión preliminar al ITC con 3 días de anticipación para comentarios; (3) incorporación de ajustes solicitados; (4) entrega de versión final; (5) documentación de observaciones y respuestas para trazabilidad.

**Protocolos de Confidencialidad y Protección de Datos**

El equipo de Aninver garantizará el cumplimiento del Reglamento General de Protección de Datos (RGPD) de la Unión Europea y la normativa argentina de protección de datos personales, obteniendo consentimiento informado de todos los participantes, anonimizando datos sensibles en informes públicos, implementando almacenamiento seguro con acceso restringido, y utilizando los datos exclusivamente para los fines de esta consultoría.

**Comunicación y Reporteo**

Nuestros consultores mantendrán comunicación fluida con el ITC mediante: reunión de inicio (kick-off) en Semana 1, reportes de avance semanales vía correo electrónico, reuniones virtuales de coordinación cada dos semanas, presentación de hallazgos preliminares en Semana 6, y presentación final de resultados en Semana 10."""
    }

    return methodology


def create_itc_argentina_document(output_path: str = None):
    """
    Crea el documento Word con la metodología para el ITC Argentina
    """
    if output_path is None:
        output_path = "output/metodologia_itc_argentina.docx"

    # Asegurar que existe el directorio de salida
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    methodology = generate_itc_argentina_methodology()
    lang_config = get_language_config('es')

    create_word_document(methodology, output_path, lang_config)
    print(f"Documento generado: {output_path}")

    return methodology


if __name__ == "__main__":
    create_itc_argentina_document()
