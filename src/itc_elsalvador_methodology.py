"""
Metodología específica para la Consultoría ITC - Mapeo de Polos de Innovación Social en El Salvador
EU-LAC Social Accelerator - febrero-abril 2026
"""

import os
import json
import requests
from document_writer import create_word_document
from translations import get_language_config


def generate_itc_methodology() -> dict:
    """
    Genera la metodología para la consultoría de mapeo de polos de innovación social en El Salvador
    basada en los TdR del ITC/EU-LAC Social Accelerator
    """

    methodology = {
        "introduction": """Aninver Development Partners presenta su propuesta metodológica para la realización del mapeo y diagnóstico participativo del ecosistema de innovación social en El Salvador, en el marco del proyecto EU-LAC Social Accelerator. Nuestro equipo de consultores fundamenta su aproximación en un enfoque sistémico que integra el análisis documental riguroso con metodologías participativas de investigación social, garantizando la aplicación transversal del enfoque transformador de género (GAP III), la interseccionalidad y los derechos humanos. Los consultores de Aninver combinan experiencia técnica en mapeo de ecosistemas de innovación, análisis de redes multiactor y diseño de instrumentos de investigación cuantitativa y cualitativa, con un profundo conocimiento del contexto centroamericano y de los marcos estratégicos de la Unión Europea, particularmente la Agenda Global Gateway. Esta propuesta responde de manera precisa a los seis objetivos específicos establecidos en los TdR, articulando un proceso metodológico en cuatro fases que permitirá identificar y caracterizar polos de innovación social, generar una base de datos estructurada, elaborar un diagnóstico participativo del ecosistema, y proveer insumos técnicos clave para la hoja de ruta nacional.""",

        "context": """**El Proyecto EU-LAC Social Accelerator y el Contexto Salvadoreño**

El proyecto EU-LAC Social Accelerator, financiado por la Comisión Europea en el marco de la Agenda Global Gateway, busca fortalecer los ecosistemas de innovación social en América Latina y el Caribe, promoviendo una transición verde y digital que sea justa, socialmente responsable e inclusiva. El consorcio implementador, conformado por CAINCO, Tecnalia, TEC de Monterrey, CACB, Caribbean Export y el Centro de Comercio Internacional (ITC), representa un modelo de cooperación UE-LAC orientado a la reducción de desigualdades y el fortalecimiento de la cohesión social, con especial énfasis en mujeres, jóvenes y grupos en situación de vulnerabilidad.

**El Salvador: Un Ecosistema de Innovación Social en Desarrollo**

El Salvador presenta un ecosistema de innovación social en etapa de consolidación, caracterizado por la presencia de diversos actores que incluyen organizaciones de la sociedad civil, empresas sociales, instituciones académicas, hubs de innovación y entidades gubernamentales. El país ha experimentado transformaciones significativas en su tejido social y económico, lo que genera tanto desafíos como oportunidades para el fortalecimiento de la innovación social. Las áreas temáticas prioritarias incluyen: empoderamiento económico de mujeres y juventudes, educación y formación técnica, sostenibilidad ambiental, inclusión financiera, tecnología y transformación digital, y emprendimiento social.

**Marco Normativo y Políticas Relevantes**

La consultoría se alinea con el Plan de Acción de Género III (GAP III) de la Unión Europea, incorporando los principios de interseccionalidad y derechos humanos. A nivel nacional, se articula con las políticas públicas salvadoreñas relacionadas con innovación, desarrollo social, juventud y género. El enfoque metodológico responde a los estándares del ePRAG 2025 y el Convenio de Subvención con la Comisión Europea.

**Objetivos del Mapeo y Diagnóstico**

Esta consultoría responde al Output 1.1 del Marco Lógico del proyecto: "Polos de innovación social desarrollados en ALC a partir de la experiencia de la UE". Los objetivos específicos incluyen: (OE1) identificar y mapear polos de innovación social activos o emergentes; (OE2) desarrollar una base de datos estructurada desagregada; (OE3) elaborar un diagnóstico participativo con análisis DAFO; (OE4) identificar necesidades, barreras y oportunidades; (OE5) proveer insumos técnicos para la hoja de ruta nacional; y (OE6) aportar a la línea de base para el monitoreo de impacto.

**Actores Clave del Ecosistema**

El mapeo abarcará la diversidad de actores que conforman el ecosistema: gobiernos (nacional y subnacionales), organizaciones de la sociedad civil (OSC, ONG, colectivos), sector privado (empresas, PyMEs, startups, empresas sociales), academia (universidades, centros de I+D), plataformas de innovación (hubs, aceleradoras), cámaras empresariales, agencias de cooperación e inversores de impacto. La identificación priorizará aquellos actores que han integrado la igualdad de género como objetivo explícito y que promueven cambios estructurales hacia una transformación social equitativa.

**Integración de la Agenda Global Gateway**

De manera transversal, el proceso incorporará las prioridades temáticas de la Agenda Global Gateway: transición verde, transformación digital, desarrollo humano y social, y conectividad sostenible. Las herramientas de investigación permitirán clasificar actores e iniciativas según su contribución a estos ejes, así como su potencial de vinculación con mecanismos de financiamiento de la Unión Europea.""",

        "principles": [
            {
                "name": "Enfoque Transformador de Género (GAP III)",
                "description": "El equipo de Aninver aplica el Plan de Acción de Género III de la UE como marco transversal, asegurando que todas las fases del mapeo integren la perspectiva de género, identifiquen brechas y barreras específicas que enfrentan las mujeres en el ecosistema de innovación social, y visibilicen liderazgos femeninos e iniciativas con enfoque de género explícito. Nuestros consultores desagregarán los datos por sexo y promoverán la participación equitativa en grupos focales y entrevistas."
            },
            {
                "name": "Interseccionalidad y Derechos Humanos",
                "description": "Nuestro equipo reconoce que las desigualdades se expresan de manera diferenciada según la intersección de múltiples factores (género, edad, etnia, condición socioeconómica, territorio). El enfoque metodológico de Aninver identifica cómo estas intersecciones afectan el acceso a oportunidades de innovación social, priorizando la inclusión de jóvenes, pueblos indígenas, comunidades rurales y otros grupos en situación de vulnerabilidad."
            },
            {
                "name": "Participación y Co-creación",
                "description": "Los consultores de Aninver construyen el mapeo y diagnóstico con los propios actores del ecosistema, no sobre ellos. Aplicamos metodologías participativas que reconocen los saberes locales, promueven el diálogo multiactor y generan apropiación de los resultados. Nuestros grupos focales, entrevistas y validaciones se diseñan para facilitar la participación activa de diversos tipos de actores, incluyendo aquellos tradicionalmente excluidos."
            },
            {
                "name": "Alineación con Global Gateway",
                "description": "El equipo de Aninver integra explícitamente las prioridades de la Agenda Global Gateway en el diseño metodológico, clasificando actores e iniciativas según su contribución a la transición verde, transformación digital, desarrollo humano y social, y conectividad sostenible. Este alineamiento facilita la identificación de oportunidades de inversión y articulación con programas de la UE."
            },
            {
                "name": "Rigor Metodológico y Evidencia",
                "description": "Nuestros consultores combinan métodos cuantitativos (encuestas digitales, matrices de datos) y cualitativos (entrevistas semiestructuradas, grupos focales, análisis DAFO) para triangular información y generar hallazgos robustos. El equipo de Aninver sigue protocolos de sistematización que garantizan la replicabilidad, comparabilidad y utilidad de los datos para el monitoreo de impacto del proyecto."
            },
            {
                "name": "Orientación a la Acción",
                "description": "Para Aninver, el mapeo y diagnóstico no son fines en sí mismos, sino insumos para la acción. Nuestro equipo prioriza la generación de recomendaciones prácticas, viables y priorizadas para la hoja de ruta nacional, identificando oportunidades concretas de articulación, inversión e incidencia política que fortalezcan el ecosistema de innovación social salvadoreño."
            }
        ],

        "phases": [
            {
                "title": "Fase 1: Revisión Documental y Diagnóstico Ex Ante",
                "description": """El equipo de consultores de Aninver iniciará esta fase con el propósito de comprender a profundidad el contexto nacional y regional de la innovación social en El Salvador. Nuestros especialistas analizarán el marco lógico del proyecto, documentos metodológicos del consorcio EU-LAC, políticas vinculadas al Global Gateway y GAP III, así como el estudio de mejores prácticas europeas sistematizadas por TECNALIA. Paralelamente, el equipo realizará investigación de fuentes secundarias sobre el ecosistema salvadoreño, incluyendo informes previos sobre innovación social, género, juventudes y grupos vulnerables. El producto de esta fase será el Diagnóstico Ex Ante del Contexto, que establecerá la línea base para las fases subsiguientes e incluirá la identificación preliminar de actores para el grupo semilla.""",
                "start_week": 1,
                "end_week": 2,
                "tasks": [
                    {
                        "code": "1A",
                        "title": "Elaboración del plan de trabajo y revisión documental inicial",
                        "description": """El equipo de Aninver elaborará el plan de trabajo detallado de la consultoría, definiendo el cronograma específico, el enfoque metodológico y la estrategia de validación con el ITC. Simultáneamente, nuestros consultores iniciarán el análisis sistemático de la documentación proporcionada por el ITC, incluyendo el marco lógico del proyecto EU-LAC Social Accelerator con sus indicadores y metas, los manuales técnicos y metodológicos del consorcio, las políticas marco del Global Gateway y el Plan de Acción de Género III, y el convenio de subvención con la Comisión Europea. Este análisis permitirá al equipo identificar los requisitos específicos de reporte y las expectativas de calidad que guiarán la ejecución de la consultoría.""",
                        "items": [
                            "Elaboración del cronograma detallado de actividades",
                            "Definición del enfoque metodológico específico",
                            "Revisión del marco lógico y matriz de indicadores del proyecto",
                            "Análisis de políticas Global Gateway y GAP III aplicables",
                            "Estudio de mejores prácticas europeas sistematizadas por TECNALIA"
                        ],
                        "start_week": 1,
                        "end_week": 1,
                        "deliverable_week": 1,
                        "deliverable_code": "P1"
                    },
                    {
                        "code": "1B",
                        "title": "Investigación de fuentes secundarias del contexto salvadoreño",
                        "description": """Nuestro equipo de investigadores conducirá una exhaustiva revisión de fuentes secundarias para construir una visión integral del ecosistema de innovación social salvadoreño. Los consultores de Aninver analizarán informes de organismos multilaterales como BID, PNUD y CEPAL, estudios académicos relevantes, y diagnósticos previos elaborados por organizaciones de la sociedad civil y agencias de cooperación internacional. El equipo también revisará el marco normativo nacional, incluyendo legislación sobre asociaciones, emprendimiento, juventud y género, así como los planes nacionales de desarrollo vigentes. Esta investigación permitirá a nuestros especialistas caracterizar la dimensión político-normativa e institucional del país, mapear programas existentes, e identificar tanto los desafíos estructurales como las oportunidades estratégicas para el fortalecimiento de la innovación social.""",
                        "items": [],
                        "start_week": 1,
                        "end_week": 2
                    },
                    {
                        "code": "1C",
                        "title": "Diagnóstico ex ante e identificación del grupo semilla",
                        "description": """A partir de los hallazgos de la revisión documental, el equipo de Aninver elaborará el Diagnóstico Ex Ante del Contexto y realizará el mapeo preliminar de actores clave del ecosistema de innovación social en El Salvador. Nuestros consultores aplicarán criterios de diversidad sectorial (OSC, academia, empresas, gobierno), cobertura territorial, balance de género y variedad de tipos de organización para conformar el grupo semilla inicial de 10-15 actores representativos. El equipo priorizará organizaciones con capacidad articuladora y trayectoria demostrada en innovación social, complementando este listado con la información de contactos proporcionada por el ITC. Este grupo semilla será fundamental para activar la técnica de bola de nieve en la fase de trabajo de campo.""",
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
                "description": """En esta fase, el equipo de Aninver se concentrará en la preparación metodológica rigurosa para el trabajo de campo. Nuestros especialistas trabajarán con los instrumentos base proporcionados por el ITC —la encuesta digital del Anexo B y la guía de entrevistas semiestructuradas del Anexo C— para adaptarlos al contexto específico salvadoreño y optimizar su eficacia. Los consultores realizarán una prueba piloto con un grupo reducido de actores para validar la claridad, pertinencia y funcionalidad de los instrumentos antes de su despliegue masivo. Todas las propuestas de ajuste serán coordinadas estrechamente con el equipo del ITC para asegurar la alineación con los estándares metodológicos del consorcio.""",
                "start_week": 2,
                "end_week": 3,
                "tasks": [
                    {
                        "code": "2A",
                        "title": "Revisión y adaptación de encuesta digital",
                        "description": """El equipo metodológico de Aninver realizará un análisis detallado de las siete secciones del formulario de encuesta digital (Anexo B), evaluando su pertinencia para el contexto salvadoreño. Nuestros consultores propondrán ajustes específicos basados en los hallazgos del diagnóstico ex ante: validarán que las categorías de actores reflejen la realidad del ecosistema local, verificarán que las opciones de áreas temáticas y poblaciones objetivo sean comprehensivas, y se asegurarán de que las preguntas sobre articulación capturen adecuadamente las dinámicas de colaboración existentes. El equipo incorporará preguntas que permitan clasificar a los actores según su alineación con los ejes del Global Gateway y el enfoque GAP III. La versión optimizada del instrumento será presentada al ITC para su validación y aprobación antes del lanzamiento.""",
                        "items": [],
                        "start_week": 2,
                        "end_week": 2
                    },
                    {
                        "code": "2B",
                        "title": "Prueba piloto del instrumento de encuesta",
                        "description": """Antes del despliegue masivo, el equipo de Aninver aplicará la encuesta a un grupo piloto de 5-8 actores seleccionados del grupo semilla. Esta prueba piloto tiene un doble propósito: por un lado, validar aspectos técnicos como el tiempo promedio de respuesta, la claridad de las preguntas, la completitud de las opciones y el correcto funcionamiento de la plataforma digital; por otro, evaluar la calidad de los datos obtenidos y su utilidad para los análisis previstos. Los consultores documentarán sistemáticamente las observaciones de los participantes piloto, identificarán puntos de confusión o fricción, y propondrán los ajustes finales necesarios. Este proceso iterativo garantizará que el instrumento esté completamente afinado antes de su aplicación a escala.""",
                        "items": [],
                        "start_week": 2,
                        "end_week": 3
                    },
                    {
                        "code": "2C",
                        "title": "Revisión de guía de entrevistas DAFO",
                        "description": """Los especialistas cualitativos de Aninver revisarán y adaptarán la Guía de Entrevistas Semiestructuradas (Anexo C) para el diagnóstico DAFO. El equipo asegurará que las preguntas capturen información relevante sobre las cinco dimensiones estratégicas: gobernanza y articulación interinstitucional, capacidades técnicas e institucionales, inclusión social y enfoque de género, sostenibilidad financiera y acceso a inversiones, e innovación tecnológica y transformación digital. Nuestros consultores definirán también los criterios de selección de actores a entrevistar, priorizando aquellos con alto nivel de articulación y representatividad sectorial, y diseñarán el protocolo de consentimiento informado que garantice el cumplimiento de las disposiciones éticas del proyecto.""",
                        "items": [],
                        "start_week": 2,
                        "end_week": 3
                    },
                    {
                        "code": "2D",
                        "title": "Preparación logística para trabajo de campo",
                        "description": """El equipo operativo de Aninver se encargará de toda la planificación logística necesaria para el trabajo de campo. Nuestros consultores configurarán la plataforma digital para la administración de encuestas, diseñarán la estrategia de difusión y convocatoria que maximice la tasa de respuesta, y prepararán los materiales de presentación del proyecto EU-LAC Social Accelerator. El equipo establecerá canales de comunicación directos con el grupo semilla y coordinará con el ITC para acceder a sus redes de contactos en El Salvador. Adicionalmente, los consultores definirán los protocolos de seguimiento —incluyendo frecuencia de recordatorios y canales alternativos de contacto— que aseguren alcanzar la meta de 60-100 encuestas completas.""",
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
                "description": """Esta fase representa el núcleo operativo de la consultoría, donde el equipo de Aninver desplegará las herramientas de mapeo y diagnóstico en terreno. Nuestros consultores iniciarán con la aplicación de encuestas al grupo semilla, expandiendo progresivamente el universo de actores mediante la técnica de bola de nieve. Toda la información cuantitativa será sistematizada en formato Excel según los estándares del ITC. De manera simultánea, el equipo conducirá entrevistas semiestructuradas a actores clave para alimentar el diagnóstico DAFO, y facilitará grupos focales por área temática que permitan profundizar en la comprensión del ecosistema. El objetivo es alcanzar un mínimo de 60-100 encuestas completas y generar información cualitativa robusta para caracterizar los polos de innovación social identificados.""",
                "start_week": 3,
                "end_week": 8,
                "tasks": [
                    {
                        "code": "3A",
                        "title": "Aplicación de encuestas al grupo semilla y expansión",
                        "description": """El equipo de campo de Aninver lanzará la encuesta digital al grupo semilla inicial proporcionado por el ITC, activando simultáneamente el mecanismo de bola de nieve: cada respondente nominará hasta tres instituciones con las que colabora regularmente, generando así nuevos contactos para encuestar. Nuestros consultores implementarán un sistema de seguimiento multicanal —correo electrónico, WhatsApp, llamadas telefónicas— para maximizar la tasa de respuesta y asegurar la completitud de los formularios. El equipo monitoreará continuamente la representatividad de la muestra por tipo de actor, territorio y género, realizando búsquedas activas complementarias cuando se identifiquen vacíos en la cobertura. La sistematización de datos en el formato Excel del ITC se realizará de manera progresiva, permitiendo ajustes tempranos en la estrategia de recolección.""",
                        "items": [],
                        "start_week": 3,
                        "end_week": 5,
                        "deliverable_week": 5,
                        "deliverable_code": "P3"
                    },
                    {
                        "code": "3B",
                        "title": "Sistematización de encuestas y análisis preliminar",
                        "description": """Una vez alcanzado el volumen crítico de respuestas, el equipo analítico de Aninver procesará los datos para generar el documento de sistematización (P3) y el reporte de análisis preliminar de actores (P4). Nuestros consultores realizarán la limpieza y validación de datos, aplicarán controles de consistencia, y ejecutarán la desagregación por las variables clave establecidas en los TdR: género, edad, tipo de actor, territorio, área temática, nivel de articulación, enfoque de género y poblaciones beneficiarias. El análisis clasificará a los actores identificando roles diferenciados —líderes, promotores, articuladores, implementadores— y construirá un mapa visual de las relaciones entre organizaciones que permita identificar clusters y patrones de colaboración en el ecosistema.""",
                        "items": [],
                        "start_week": 5,
                        "end_week": 6,
                        "deliverable_week": 6,
                        "deliverable_code": "P4"
                    },
                    {
                        "code": "3C",
                        "title": "Identificación y caracterización de polos de innovación",
                        "description": """Aplicando la metodología desarrollada por el Tecnológico de Monterrey —socio del consorcio EU-LAC—, el equipo de Aninver analizará la información recopilada para identificar polos de innovación social existentes o emergentes en El Salvador. Los criterios de identificación incluirán: densidad de articulación entre actores, concentración territorial, convergencia temática, capacidad demostrada de escalamiento, y potencial de atracción de inversiones. Nuestros consultores caracterizarán al menos tres polos, documentando para cada uno: los actores participantes y sus roles, el nivel de madurez institucional, la integración del enfoque de género, la alineación con los ejes del Global Gateway, y las necesidades específicas de fortalecimiento. Este análisis será insumo directo para las recomendaciones de la hoja de ruta nacional.""",
                        "items": [],
                        "start_week": 6,
                        "end_week": 7,
                        "deliverable_week": 7,
                        "deliverable_code": "P5"
                    },
                    {
                        "code": "3D",
                        "title": "Entrevistas semiestructuradas para diagnóstico DAFO",
                        "description": """El equipo cualitativo de Aninver conducirá entre 15 y 20 entrevistas a profundidad con actores clave identificados en las encuestas. Utilizando la guía del Anexo C, nuestros consultores explorarán las cinco dimensiones del diagnóstico DAFO: gobernanza y articulación interinstitucional, capacidades técnicas e institucionales, inclusión social y enfoque de género, sostenibilidad financiera y acceso a inversiones, e innovación tecnológica y transformación digital. La selección de entrevistados priorizará actores articuladores y representativos de cada polo identificado, asegurando diversidad de perspectivas sectoriales. El equipo continuará aplicando la técnica de bola de nieve durante las entrevistas para identificar informantes adicionales que enriquezcan el diagnóstico.""",
                        "items": [],
                        "start_week": 6,
                        "end_week": 8
                    },
                    {
                        "code": "3E",
                        "title": "Grupos focales de diagnóstico del ecosistema",
                        "description": """Los facilitadores de Aninver organizarán y conducirán grupos focales con actores del ecosistema, segmentados por área temática prioritaria. El equipo realizará entre tres y cuatro sesiones, cada una con participantes de diferentes tipos de organización (OSC, academia, empresas, gobierno) para asegurar la pluralidad de voces. La metodología de facilitación promoverá la construcción colectiva del análisis DAFO, permitiendo que los propios actores identifiquen y prioricen las fortalezas, debilidades, oportunidades y amenazas del ecosistema desde su experiencia directa. Nuestros consultores documentarán tanto los consensos como las divergencias de perspectivas, generando insumos valiosos para entender la complejidad del ecosistema salvadoreño. El informe de sistematización de grupos focales y entrevistas contextuales (P6) será entregado al finalizar esta fase.""",
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
                "description": """En esta fase conclusiva, el equipo de Aninver consolidará todos los resultados del trabajo de campo en los productos definitivos del proyecto. Nuestros consultores elaborarán el análisis DAFO integral del ecosistema, el diagnóstico ex post con enfoque GAP III, la línea de base nacional, y el informe final consolidado. Los documentos no solo describirán hallazgos, sino que formularán recomendaciones estratégicas priorizadas para fortalecer el ecosistema y proveerán insumos técnicos concretos para la construcción de la hoja de ruta nacional. El equipo mantendrá comunicación permanente con el ITC para la validación progresiva de productos y asegurar la alineación con los estándares y expectativas del proyecto.""",
                "start_week": 8,
                "end_week": 10,
                "tasks": [
                    {
                        "code": "4A",
                        "title": "Elaboración del análisis DAFO del ecosistema",
                        "description": """El equipo analítico de Aninver sintetizará toda la información cualitativa recopilada —entrevistas y grupos focales— para construir el diagnóstico DAFO integral del ecosistema de innovación social salvadoreño. Nuestros consultores abordarán las cinco dimensiones estratégicas definidas en los TdR, triangulando la información de fuentes primarias con los hallazgos de la revisión documental. El análisis cruzará el DAFO con el enfoque GAP III para identificar fortalezas, debilidades, oportunidades y amenazas específicas desde la perspectiva de género e interseccionalidad. El equipo priorizará los hallazgos según su relevancia estratégica para el fortalecimiento del ecosistema, y validará las conclusiones preliminares con actores clave antes de la entrega final.""",
                        "items": [],
                        "start_week": 8,
                        "end_week": 9,
                        "deliverable_week": 9,
                        "deliverable_code": "P7"
                    },
                    {
                        "code": "4B",
                        "title": "Diagnóstico ex post de oportunidades y brechas (GAP III)",
                        "description": """Los especialistas en género de Aninver elaborarán el diagnóstico ex post con foco específico en la inclusión de mujeres, jóvenes y grupos vulnerables en el ecosistema de innovación social. El análisis identificará las brechas de participación por género y edad, las barreras estructurales que limitan el acceso de poblaciones vulnerables, y las oportunidades concretas de empoderamiento económico. Nuestros consultores documentarán las buenas prácticas identificadas durante el trabajo de campo —iniciativas con enfoque de género explícito, liderazgos femeninos destacados, programas inclusivos exitosos— y formularán recomendaciones específicas para transversalizar el enfoque de género en las acciones futuras del proyecto. Este producto alimentará directamente la estrategia de la hoja de ruta nacional.""",
                        "items": [],
                        "start_week": 9,
                        "end_week": 9,
                        "deliverable_week": 9,
                        "deliverable_code": "P8"
                    },
                    {
                        "code": "4C",
                        "title": "Construcción de la línea de base del ecosistema",
                        "description": """El equipo de monitoreo y evaluación de Aninver elaborará el documento técnico de línea de base nacional, diseñado para ser compatible con el sistema de seguimiento e impacto del consorcio EU-LAC. La línea de base incluirá indicadores alineados con el Output 1.1 del marco lógico: número de polos de innovación social identificados y su nivel de madurez, instituciones con potencial de ser capacitadas, estimación de población beneficiaria directa e indirecta desagregada por sexo y edad, e inventario de iniciativas con potencial de pilotaje. Nuestros consultores documentarán la metodología de cálculo de cada indicador y entregarán el producto tanto en formato de documento técnico narrativo como en archivo Excel estructurado para facilitar su actualización futura.""",
                        "items": [],
                        "start_week": 9,
                        "end_week": 10,
                        "deliverable_week": 10,
                        "deliverable_code": "P9"
                    },
                    {
                        "code": "4D",
                        "title": "Elaboración del informe final consolidado",
                        "description": """El equipo de redacción de Aninver integrará todos los hallazgos, análisis y productos parciales en el Informe Final Consolidado de Mapeo y Diagnóstico del Ecosistema de Innovación Social de El Salvador. El documento incluirá una síntesis ejecutiva orientada a tomadores de decisión, la descripción detallada de la metodología aplicada, la caracterización integral del ecosistema y sus actores, el análisis de los polos identificados, el diagnóstico DAFO completo, el análisis desde el enfoque GAP III, los indicadores de línea de base, y —de manera central— las recomendaciones estratégicas para la construcción de la hoja de ruta nacional. Nuestros consultores incorporarán mapas, gráficos y visualizaciones que faciliten la comprensión de los hallazgos, y compilarán todos los anexos técnicos requeridos. El informe será sometido a validación final con el ITC antes de su entrega definitiva.""",
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

El equipo de Aninver ha identificado los principales riesgos asociados a la ejecución de esta consultoría y propone medidas de mitigación específicas para cada uno:

**Riesgos Metodológicos**

*Baja tasa de respuesta a encuestas*: Existe el riesgo de no alcanzar las 60-100 encuestas completas requeridas. Para mitigar este riesgo, nuestros consultores implementarán una estrategia de contacto multicanal (correo electrónico, WhatsApp, llamadas telefónicas), realizarán seguimiento sistemático con recordatorios escalonados, y activarán agresivamente la técnica bola de nieve desde el grupo semilla inicial. El equipo de Aninver coordinará con el ITC para acceder a sus redes de contactos en El Salvador y maximizar el alcance.

*Sesgos en la identificación de actores*: La técnica bola de nieve puede generar sesgos hacia redes preexistentes, subrepresentando actores aislados o emergentes. Nuestro equipo complementará esta técnica con búsqueda activa de actores a partir de fuentes secundarias, monitoreando continuamente la representatividad territorial y sectorial de la muestra para realizar ajustes correctivos cuando sea necesario.

*Información incompleta o de baja calidad*: Los actores pueden proporcionar información parcial o inexacta. Los consultores de Aninver triangularán información de múltiples fuentes, aplicarán validaciones cruzadas, y profundizarán mediante entrevistas cuando se identifiquen inconsistencias.

**Riesgos Operativos**

*Dificultades de acceso a actores en territorios remotos*: El Salvador presenta zonas con conectividad limitada. El equipo combinará modalidades virtuales y presenciales según el contexto de cada territorio, flexibilizando horarios y canales para facilitar la participación de actores en áreas rurales.

*Retrasos en validación de productos con ITC*: Los tiempos de revisión y aprobación podrían afectar el cronograma. Nuestros consultores establecerán canales de comunicación fluidos con el equipo ITC, entregarán versiones preliminares para retroalimentación temprana, y mantendrán flexibilidad en el cronograma interno para absorber eventuales ajustes.

**Riesgos de Contexto**

*Cambios en el contexto político-institucional*: Modificaciones en políticas públicas o cambios institucionales podrían afectar la relevancia de los hallazgos. El equipo de Aninver monitoreará activamente el contexto durante la consultoría, adaptará el análisis a la coyuntura, y formulará recomendaciones con horizontes temporales diferenciados (corto, mediano y largo plazo).

*Sensibilidades en temas de género y derechos humanos*: Algunos actores pueden mostrar resistencia al enfoque GAP III. Nuestros consultores comunicarán de manera clara el marco conceptual del proyecto, enfatizando su alineación con compromisos internacionales asumidos por El Salvador, y aplicarán sensibilidad cultural en el abordaje de estos temas.

**Plan de Contingencia**

En caso de materializarse riesgos críticos que afecten la entrega de productos, el equipo de Aninver activará: (1) comunicación inmediata con ITC para acordar ajustes, (2) reasignación de recursos del equipo consultor, (3) ajuste consensuado de alcance o cronograma, y (4) activación de redes alternativas de contactos.""",

        "quality": """**Aseguramiento de Calidad**

El equipo de Aninver implementará un sistema riguroso de aseguramiento de calidad para garantizar que todos los productos cumplan con los estándares técnicos del proyecto EU-LAC Social Accelerator y sean útiles para los fines del mapeo y diagnóstico.

**Indicadores Clave de Desempeño (KPIs)**

Nuestros consultores monitorearán los siguientes indicadores durante la ejecución:

- Tasa de respuesta de encuestas: mínimo 60 encuestas completas, meta 100
- Desagregación por género: mínimo 40% de respondentes mujeres
- Cobertura territorial: representación de al menos 10 de los 14 departamentos
- Diversidad de actores: mínimo 5 tipos de organizaciones representadas
- Tasa de completitud de datos: mínimo 90% de campos obligatorios completos
- Número de entrevistas a profundidad: mínimo 15-20 entrevistas
- Grupos focales realizados: mínimo 3 por área temática
- Polos identificados: mínimo 3 con caracterización completa

**Mecanismos de Control de Calidad**

*Revisión por pares*: Cada producto será revisado por al menos dos miembros del equipo de Aninver antes de su entrega, verificando consistencia metodológica, calidad de redacción y alineación con los TdR.

*Validación con actores*: Los hallazgos preliminares serán validados con actores clave del ecosistema para verificar su pertinencia, precisión y utilidad práctica.

*Verificación de datos*: El equipo implementará controles de consistencia en las bases de datos, validando rangos, formatos y coherencia de respuestas, con corrección de errores antes de los análisis.

*Alineación con TdR*: Cada producto será cotejado con los requisitos específicos de los términos de referencia y los formatos establecidos en los Anexos.

**Protocolo de Entregas**

El proceso de entrega de cada producto seguirá el siguiente protocolo: (1) autoevaluación de calidad por el equipo consultor; (2) envío de versión preliminar al ITC con 3 días de anticipación para comentarios; (3) incorporación de ajustes solicitados; (4) entrega de versión final; (5) documentación de observaciones y respuestas para trazabilidad.

**Protocolos de Confidencialidad y Protección de Datos**

El equipo de Aninver garantizará el cumplimiento del Reglamento General de Protección de Datos (RGPD) de la Unión Europea, obteniendo consentimiento informado de todos los participantes, anonimizando datos sensibles en informes públicos, implementando almacenamiento seguro con acceso restringido, y utilizando los datos exclusivamente para los fines de esta consultoría.

**Comunicación y Reporteo**

Nuestros consultores mantendrán comunicación fluida con el ITC mediante: reunión de inicio (kick-off) en Semana 1, reportes de avance semanales vía correo electrónico, reuniones virtuales de coordinación cada dos semanas, presentación de hallazgos preliminares en Semana 6, y presentación final de resultados en Semana 10."""
    }

    return methodology


def create_itc_document(output_path: str = None):
    """
    Crea el documento Word con la metodología para el ITC
    """
    if output_path is None:
        output_path = "output/metodologia_itc_elsalvador.docx"

    # Asegurar que existe el directorio de salida
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    methodology = generate_itc_methodology()
    lang_config = get_language_config('es')

    create_word_document(methodology, output_path, lang_config)
    print(f"Documento generado: {output_path}")

    return methodology


if __name__ == "__main__":
    create_itc_document()
