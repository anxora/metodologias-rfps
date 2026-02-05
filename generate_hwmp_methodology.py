#!/usr/bin/env python3
"""
Direct methodology generator for Palestine HWMP TOR
"""

import json
from src.document_writer import create_word_document
from src.translations import get_language_config

methodology = {
    "introduction": """Our consortium presents a comprehensive methodological approach for developing Palestine's National Hazardous Waste Management Plan (HWMP). Drawing on extensive international experience in environmental management and waste planning across developing countries and conflict-affected regions, we propose a participatory, evidence-based methodology that addresses the unique challenges facing the West Bank. Our approach integrates compliance with international conventions (Basel, Rotterdam, Stockholm, and Minamata) with practical, context-appropriate solutions that account for Palestine's geopolitical constraints, institutional capacity, and economic realities. The methodology prioritizes stakeholder engagement, capacity building, and the development of sustainable systems that can be effectively implemented within existing institutional frameworks while building toward long-term environmental protection goals.""",

    "context": """**Project Background and Institutional Framework**

The West Bank and Gaza face unprecedented challenges in environmental management due to their unique political context. The Palestinian Authority, through the Environment Quality Authority (EQA), has made significant strides in environmental governance, including accession to the Basel, Rotterdam, Stockholm, and Minamata (BRS-M) conventions. However, the implementation of comprehensive hazardous waste management remains constrained by several factors: isolated geography, lack of control over borders, ongoing conflict particularly affecting Gaza, and disruptions to waste management infrastructure.

The Municipal Development and Lending Fund (MDLF), operating on behalf of the Ministry of Local Government, has secured World Bank Group funding through the West Bank & Gaza Integrated Solid Waste Management Project (ISWMP-1). This strategic program aims to transition solid waste management toward a circular economy model, departing from traditional linear waste management approaches. The development of a national HWMP represents a critical component of this broader transformation.

**Stakeholder Landscape**

The hazardous waste management ecosystem in Palestine involves multiple stakeholders at various levels:

- **Governmental entities**: EQA serves as the primary regulatory authority, with critical roles played by the Ministry of Local Government (MoLG), Ministry of Agriculture (MoA), Ministry of Health, and Ministry of National Economy. Joint Service Councils (JSCs) provide regional coordination for waste management services.

- **Private sector actors**: Industrial facilities generating hazardous waste (manufacturing, automotive, healthcare), waste management service providers, and potential technology partners for treatment and disposal solutions.

- **International partners**: The World Bank provides financing and technical oversight, while UN agencies (UNEP, UNIDO) offer technical guidance on convention compliance.

- **Civil society and research institutions**: Universities, NGOs, and community organizations play vital roles in awareness raising and monitoring.

**Problem Statement and Challenges**

Palestine faces multiple hazardous waste challenges requiring immediate attention:

1. **Diverse waste streams**: Healthcare waste, industrial chemicals, e-waste, used oil, batteries, PCBs, pesticides, and pharmaceuticals are generated across the territory without adequate classification or tracking systems.

2. **Infrastructure gaps**: Limited treatment and disposal facilities exist, with most hazardous waste either mixed with municipal solid waste, stored indefinitely, or managed through informal channels.

3. **Regulatory gaps**: While legal frameworks exist, enforcement mechanisms and institutional capacity require strengthening to achieve effective compliance.

4. **Data deficiencies**: Baseline information on waste generation, composition, and current management practices remains incomplete.

5. **Financial constraints**: Economic challenges limit investment in infrastructure and operational systems.

6. **Geopolitical barriers**: Border restrictions impede the export of certain waste streams that cannot be treated locally.

**Project Objectives**

This assignment aims to develop a comprehensive, implementable HWMP that will:

- Establish a complete baseline inventory of hazardous waste streams across the West Bank
- Assess and strengthen legal, institutional, and financial frameworks
- Propose practical management approaches for collection, transport, treatment, storage, and disposal
- Develop stakeholder engagement and public awareness programs
- Recommend Best Available Technologies (BAT) and Best Environmental Practices (BEP)
- Create a monitoring, evaluation, and reporting framework
- Develop a realistic investment plan for implementation""",

    "principles": [
        {
            "name": "Compliance with International Standards",
            "description": "Our approach ensures full alignment with the Basel, Rotterdam, Stockholm, and Minamata conventions, as well as World Bank Environmental and Social Standards (ESS). All recommendations will be benchmarked against international best practices while remaining contextually appropriate for Palestine's unique circumstances. We will systematically review convention obligations and integrate them into the proposed legal and institutional frameworks."
        },
        {
            "name": "Participatory and Inclusive Engagement",
            "description": "Meaningful stakeholder participation forms the foundation of sustainable waste management systems. Our methodology prioritizes inclusive engagement with government agencies, private sector actors, civil society, research institutions, and affected communities. Special attention will be given to gender considerations, vulnerable populations, and informal sector workers who may be impacted by hazardous waste management reforms."
        },
        {
            "name": "Evidence-Based Decision Making",
            "description": "All recommendations will be grounded in rigorous data collection and analysis. We will conduct comprehensive field assessments, stakeholder interviews, and technical studies to establish an accurate baseline. Gap analyses will identify specific intervention needs, and proposed solutions will be validated through consultation with local experts and international benchmarking."
        },
        {
            "name": "Practical and Context-Appropriate Solutions",
            "description": "Recognizing Palestine's unique constraints, we will propose solutions that are technically feasible, financially viable, and institutionally manageable within the current context. Where local treatment capacity is unavailable, we will identify regional alternatives and develop contingency approaches. All recommendations will include realistic implementation pathways."
        },
        {
            "name": "Capacity Building and Knowledge Transfer",
            "description": "Sustainable hazardous waste management requires strong institutional capacity. Our approach integrates capacity building throughout all phases, including training programs for government officials, private sector operators, and enforcement personnel. We will develop comprehensive training materials and establish systems for ongoing knowledge development."
        },
        {
            "name": "Adaptive Management and Continuous Improvement",
            "description": "Environmental management in complex settings requires flexibility and adaptive approaches. Our methodology incorporates regular monitoring, evaluation, and feedback mechanisms that enable course corrections. The HWMP will include clear indicators, reporting protocols, and review processes to ensure continuous improvement over time."
        }
    ],

    "phases": [
        {
            "title": "Phase 1: Project Inception",
            "description": "The inception phase establishes the foundation for successful project implementation through comprehensive planning, stakeholder mapping, and methodology refinement. During this phase, we will mobilize our expert team, establish coordination mechanisms with EQA and MDLF, and develop detailed work plans that account for security considerations and logistical requirements in the West Bank. We will conduct initial stakeholder consultations to validate our approach and ensure alignment with client expectations and local needs.",
            "start_week": 1,
            "end_week": 2,
            "tasks": [
                {
                    "code": "1A",
                    "title": "Team Mobilization and Coordination Setup",
                    "description": "We will mobilize our multidisciplinary team comprising the Team Leader/Senior Environmental Management Expert, Hazardous Waste Management Specialist, Environmental Policy and Institutional Expert, and Social Development and Communication Specialist. Coordination mechanisms will be established with EQA, MDLF, and World Bank representatives. We will set up project management systems, communication protocols, and quality assurance procedures. A security management plan will be developed addressing field work requirements in the West Bank context.",
                    "items": [
                        "Mobilize key experts and establish team coordination structures",
                        "Conduct kick-off meeting with EQA, MDLF, and World Bank",
                        "Establish communication and reporting protocols",
                        "Develop security management plan for field activities",
                        "Set up document management and quality assurance systems"
                    ],
                    "start_week": 1,
                    "end_week": 1
                },
                {
                    "code": "1B",
                    "title": "Stakeholder Mapping and Work Plan Development",
                    "description": "A comprehensive stakeholder analysis will identify all actors relevant to hazardous waste management, including government agencies, private sector generators and service providers, research institutions, NGOs, and community representatives. We will assess each stakeholder's role, interest, influence, and potential contribution to HWMP development and implementation. The detailed work plan will be refined based on stakeholder input and logistics assessment, with specific attention to accessibility and security considerations.",
                    "items": [
                        "Conduct comprehensive stakeholder identification and mapping",
                        "Develop stakeholder engagement matrix with roles and interests",
                        "Refine detailed work plan and methodology",
                        "Prepare data collection instruments and interview guides",
                        "Develop document review framework and information requests"
                    ],
                    "start_week": 1,
                    "end_week": 2,
                    "deliverable_week": 2
                }
            ],
            "deliverables": [
                {"code": "D1", "name": "Inception Report with methodology, work plan, stakeholder mapping, and security management plan"}
            ]
        },
        {
            "title": "Phase 2: Situational Analysis",
            "description": "This comprehensive assessment phase will establish the baseline understanding of hazardous waste management in the West Bank through systematic data collection, field assessments, and stakeholder consultations. We will evaluate the legal, institutional, and financial frameworks governing hazardous waste, document current practices (both formal and informal), and prepare a detailed inventory of waste streams, infrastructure, and management gaps. This phase provides the evidence base for all subsequent recommendations.",
            "start_week": 3,
            "end_week": 8,
            "tasks": [
                {
                    "code": "2A",
                    "title": "Legal, Institutional, and Financial Framework Assessment",
                    "description": "We will conduct a thorough review of Palestine's legal framework for hazardous waste management, including the Palestinian Environmental Law, relevant bylaws, and regulatory instruments. The assessment will evaluate licensing and permitting procedures, enforcement mechanisms, and compliance monitoring systems. International treaty obligations under the Basel, Rotterdam, Stockholm, and Minamata conventions will be mapped against current national legislation to identify alignment gaps. The institutional analysis will examine the roles, capacities, and coordination mechanisms among EQA, MoLG, MoA, Ministry of Health, and other relevant agencies. Financial framework review will assess current funding sources, cost recovery mechanisms, and financial sustainability challenges.",
                    "items": [
                        "Review Palestinian Environmental Law and hazardous waste regulations",
                        "Analyze licensing, permitting, and enforcement procedures",
                        "Map BRS-M convention obligations against national legislation",
                        "Assess institutional roles, capacities, and coordination mechanisms",
                        "Evaluate financial framework including funding sources and cost recovery",
                        "Identify emerging issues: e-waste, used oil, pharmaceuticals, radioactive waste"
                    ],
                    "start_week": 3,
                    "end_week": 5
                },
                {
                    "code": "2B",
                    "title": "Current HWM Practices Assessment and Inventory Development",
                    "description": "Field assessments will document existing hazardous waste management practices across the West Bank, covering both formal and informal systems. We will identify and characterize major waste generators by sector (healthcare, manufacturing, agriculture, automotive), quantify waste streams where data exists, and document current handling, storage, transport, and disposal practices. Site visits to existing treatment facilities, storage sites, and disposal locations will assess infrastructure condition and capacity. The inventory will capture available assets, equipment, and human resources currently engaged in hazardous waste management.",
                    "items": [
                        "Conduct field assessments of major hazardous waste generators",
                        "Document formal and informal waste management practices",
                        "Quantify and characterize hazardous waste streams by type and source",
                        "Assess existing treatment, storage, and disposal infrastructure",
                        "Document current transport routes and handling procedures",
                        "Evaluate illegal traffic patterns and uncontrolled disposal sites"
                    ],
                    "start_week": 4,
                    "end_week": 7
                },
                {
                    "code": "2C",
                    "title": "Gap Analysis and Assessment Report Preparation",
                    "description": "Synthesis of all assessment findings into a comprehensive gap analysis identifying deficiencies in legal coverage, institutional capacity, infrastructure, financial resources, and operational practices. The gap analysis will prioritize issues by severity and urgency, providing the foundation for targeted recommendations. GIS mapping will visualize waste generation sources, transport routes, and disposal sites to support spatial planning. The Assessment Report will present all findings in a clear, actionable format for validation by EQA and stakeholders.",
                    "items": [
                        "Synthesize assessment findings into comprehensive gap analysis",
                        "Prioritize gaps by severity, urgency, and remediation feasibility",
                        "Develop GIS database and maps of HW sources and infrastructure",
                        "Prepare draft Assessment Report with findings and preliminary recommendations",
                        "Present assessment findings to EQA and key stakeholders for validation"
                    ],
                    "start_week": 7,
                    "end_week": 8,
                    "deliverable_week": 8
                }
            ],
            "deliverables": [
                {"code": "D2", "name": "Assessment Report on current HWM practices and legal, institutional, financial frameworks"}
            ]
        },
        {
            "title": "Phase 3: Strategy Development",
            "description": "Building on the assessment findings, this phase develops the strategic framework and technical recommendations for the HWMP. We will propose practical approaches for hazardous waste classification, collection, transport, treatment, storage, and disposal that are consistent with regulatory requirements and adapted to local conditions. Best Available Technologies (BAT) and Best Environmental Practices (BEP) will be evaluated and recommended based on technical suitability, financial viability, and institutional feasibility. Legal, institutional, and financial reform proposals will be developed to support effective implementation.",
            "start_week": 9,
            "end_week": 16,
            "tasks": [
                {
                    "code": "3A",
                    "title": "Development of Management Approaches",
                    "description": "We will develop practical, implementable approaches for each stage of the hazardous waste management chain. Classification systems based on international standards and national regulations will be proposed. Collection and segregation protocols will address different generator types and waste streams. Transport requirements including vehicle specifications, routing, documentation, and emergency response will be defined. Treatment options will be evaluated considering available local capacity and regional alternatives. Storage specifications for both temporary and long-term facilities will be developed. Disposal approaches will address final treatment requirements and potential export arrangements for wastes that cannot be managed locally.",
                    "items": [
                        "Develop hazardous waste classification system aligned with Basel Convention",
                        "Design collection and segregation protocols by generator type",
                        "Specify transport requirements, routing, and emergency procedures",
                        "Evaluate treatment options for major waste streams",
                        "Develop storage facility specifications and operational procedures",
                        "Propose disposal solutions including export arrangements where needed"
                    ],
                    "start_week": 9,
                    "end_week": 12
                },
                {
                    "code": "3B",
                    "title": "BAT/BEP Evaluation and Technology Assessment",
                    "description": "A systematic evaluation of Best Available Technologies and Best Environmental Practices suitable for Palestine's context will be conducted. Technologies for treating major waste streams (e-waste, batteries, PCBs, medical waste, used oil/chemicals) will be assessed against criteria including technical effectiveness, capital and operating costs, operational complexity, and local applicability. Interviews with technology providers operating in the West Bank and region will inform recommendations. Where BAT/BEP are not locally available, alternative options including regional treatment facilities and export arrangements will be identified. Success case studies from developing and developed countries will be compiled to inform recommendations.",
                    "items": [
                        "Establish technology evaluation criteria and assessment framework",
                        "Evaluate BAT/BEP for major hazardous waste streams",
                        "Conduct interviews with technology providers and operators",
                        "Assess regional treatment options and export possibilities",
                        "Compile international case studies for HWM systems",
                        "Develop technology recommendations with cost-benefit analysis"
                    ],
                    "start_week": 11,
                    "end_week": 14
                },
                {
                    "code": "3C",
                    "title": "Legal, Institutional, and Financial Reform Proposals",
                    "description": "Based on gap analysis findings, we will develop specific proposals for strengthening legal, institutional, and financial frameworks. Legal recommendations will include amendments to existing regulations and new regulatory instruments needed to address emerging issues (e-waste, pharmaceuticals, end-of-life vehicles). Institutional recommendations will clarify roles and responsibilities, propose coordination mechanisms, and identify capacity strengthening priorities. Financial recommendations will address cost recovery approaches, funding mechanisms, and incentive structures to promote compliance and sustainable operations.",
                    "items": [
                        "Draft proposed amendments to hazardous waste regulations",
                        "Develop new regulatory instruments for emerging waste streams",
                        "Design institutional framework with clear roles and responsibilities",
                        "Propose coordination mechanisms among government agencies",
                        "Develop financial framework including cost recovery approaches",
                        "Design incentive structures for compliance and private sector participation"
                    ],
                    "start_week": 13,
                    "end_week": 16
                }
            ],
            "deliverables": []
        },
        {
            "title": "Phase 4: Action Plan and Implementation",
            "description": "The final phase integrates all components into the comprehensive Hazardous Waste Management Plan, develops implementation instruments including the Public Awareness Program and investment plan, and validates the plan through stakeholder workshops. Monitoring and evaluation frameworks will ensure effective implementation tracking. The phase concludes with finalization of the HWMP incorporating all stakeholder feedback.",
            "start_week": 17,
            "end_week": 28,
            "tasks": [
                {
                    "code": "4A",
                    "title": "Public Awareness Program Development",
                    "description": "A comprehensive public awareness program will be designed targeting different stakeholder groups: general public, private sector generators, government officials, healthcare facilities, and educational institutions. The program will include communication strategies, key messages, delivery channels, and specific activities appropriate for each audience. Materials will be developed in Arabic with English versions as needed. Indicators for measuring awareness program effectiveness will be defined, including participatory indicators such as stakeholder surveys.",
                    "items": [
                        "Design awareness program strategy and target audience segmentation",
                        "Develop key messages and communication materials",
                        "Specify delivery channels and implementation methods",
                        "Create activity plans for different stakeholder groups",
                        "Define indicators for measuring awareness program effectiveness",
                        "Develop stakeholder engagement and feedback mechanisms"
                    ],
                    "start_week": 17,
                    "end_week": 19
                },
                {
                    "code": "4B",
                    "title": "Training Program and Capacity Building Design",
                    "description": "A comprehensive training program will be developed for government employees, private sector operators, and other stakeholders involved in hazardous waste management. Training modules will cover procedures, safety protocols, emergency response measures, regulatory compliance, and operational best practices. Training delivery approaches will include in-person workshops, train-the-trainer programs, and reference materials. Certification requirements and ongoing professional development pathways will be proposed.",
                    "items": [
                        "Develop training curriculum and module specifications",
                        "Design training materials for different target groups",
                        "Specify safety protocols and emergency response procedures",
                        "Develop train-the-trainer program approach",
                        "Create certification and competency assessment framework",
                        "Design ongoing professional development pathway"
                    ],
                    "start_week": 18,
                    "end_week": 20
                },
                {
                    "code": "4C",
                    "title": "Draft HWMP Compilation and Stakeholder Workshop",
                    "description": "All components will be integrated into the comprehensive Draft HWMP including: national hazardous waste profile with future projections, policy and action recommendations by sector and waste stream, infrastructure upgrading proposals, data systems improvements, strategies for legacy waste issues, institutional setup, and implementation indicators. The draft will include all annexes including the Public Awareness Program and case studies. A stakeholder workshop (up to 50 participants) will present the draft plan for discussion and feedback.",
                    "items": [
                        "Compile all components into Draft HWMP document",
                        "Develop national hazardous waste profile with projections",
                        "Prepare sector-specific action recommendations",
                        "Integrate infrastructure, technology, and data system proposals",
                        "Define institutional setup and implementation indicators",
                        "Organize and facilitate stakeholder workshop",
                        "Document workshop feedback and revision requirements"
                    ],
                    "start_week": 19,
                    "end_week": 22,
                    "deliverable_week": 22
                },
                {
                    "code": "4D",
                    "title": "Investment Plan and M&E Framework Development",
                    "description": "A comprehensive investment plan will be developed specifying human, technical, and financial resources required for HWMP implementation. Capital and operational cost estimates will be provided for infrastructure, equipment, capacity building, and awareness programs. Funding sources and financing mechanisms will be identified. The monitoring and evaluation framework will establish specific objectives, measurable targets, and performance indicators. Reporting schedules and monitoring approaches will enable progress tracking, accountability, and timely corrective actions.",
                    "items": [
                        "Develop detailed investment plan with cost estimates",
                        "Identify funding sources and financing mechanisms",
                        "Establish M&E objectives, targets, and performance indicators",
                        "Design monitoring and inspection processes",
                        "Develop reporting schedule and accountability mechanisms",
                        "Identify implications of non-implementation (environmental, health, legal)"
                    ],
                    "start_week": 21,
                    "end_week": 24
                },
                {
                    "code": "4E",
                    "title": "Final HWMP and Validation Workshop",
                    "description": "The Final HWMP will incorporate all feedback from the draft review process and stakeholder workshop. Final quality review will ensure consistency, completeness, and compliance with EQA requirements. A final validation workshop (up to 50 participants) will present the completed plan and associated implementation instruments. All documents will be finalized in both Arabic and English versions with professional quality formatting. Final deliverables will include editable formats (Word, Excel, PowerPoint) and PDF versions, along with GIS database outputs.",
                    "items": [
                        "Incorporate all stakeholder feedback into Final HWMP",
                        "Conduct final quality review and consistency check",
                        "Prepare Arabic and English versions of all documents",
                        "Organize and facilitate final validation workshop",
                        "Finalize all deliverables in required formats",
                        "Transfer GIS database and supporting materials to EQA"
                    ],
                    "start_week": 24,
                    "end_week": 28,
                    "deliverable_week": 28
                }
            ],
            "deliverables": [
                {"code": "D3", "name": "Draft HWMP with HWM Public Awareness Program"},
                {"code": "D4", "name": "Workshop 1: Draft Plan Discussion (up to 50 participants)"},
                {"code": "D5", "name": "Final HWMP incorporating stakeholder feedback"},
                {"code": "D6", "name": "Workshop 2: Final Plan Presentation (up to 50 participants)"}
            ]
        }
    ],

    "risks": """**Risk Management Framework**

Effective implementation of this assignment requires proactive identification and management of risks that could impact project delivery. Our risk management approach includes systematic risk identification, assessment, mitigation planning, and monitoring throughout the project lifecycle.

**Category 1: Operational and Access Risks**

The security and political situation in the West Bank may affect field work accessibility, stakeholder availability, and data collection activities. Mitigation measures include: development of a comprehensive security management plan in coordination with EQA and MDLF; flexible scheduling that allows for activity rescheduling; use of local team members with established relationships and access; and contingency protocols for remote engagement when physical access is constrained.

**Category 2: Data Availability and Quality Risks**

Baseline data on hazardous waste generation, composition, and management practices may be incomplete or inconsistent across sources. Mitigation approaches include: triangulation of data from multiple sources; use of estimation methodologies where primary data is unavailable; clear documentation of data limitations and assumptions; and validation workshops with knowledgeable stakeholders.

**Category 3: Stakeholder Engagement Risks**

Key stakeholders may have limited availability, competing priorities, or divergent interests that constrain effective engagement. Mitigation strategies include: early stakeholder mapping and relationship building; flexible scheduling of consultations; clear communication of project benefits and stakeholder roles; and escalation protocols through EQA for critical engagement needs.

**Category 4: Technical and Institutional Risks**

Proposed recommendations may face implementation challenges due to institutional capacity constraints, technology availability, or financial limitations. Mitigation approaches include: thorough assessment of existing capacity and realistic recommendation development; phased implementation approaches that build capacity progressively; identification of quick wins alongside longer-term initiatives; and clear specification of resource requirements for each recommendation.

**Category 5: Coordination and Approval Risks**

The requirement for clearance from multiple agencies (EQA, MoLG, MoA, World Bank) may create delays in deliverable approval. Mitigation measures include: proactive engagement with all review agencies from project inception; clear communication of review timelines and requirements; draft document sharing for informal feedback before formal submission; and regular progress updates to all stakeholders.

**Contingency Planning**

For each identified risk, specific contingency measures have been developed. These include alternative data collection approaches, remote engagement capabilities, phased deliverable submission options, and escalation procedures for critical issues. The project management approach includes regular risk monitoring and reporting to enable early identification of emerging issues and timely response.""",

    "quality": """**Quality Assurance Framework**

Our quality assurance approach ensures all deliverables meet the highest professional standards and comply with EQA requirements, World Bank standards, and international best practices.

**Quality Control Mechanisms**

All deliverables undergo a multi-stage review process: (1) Technical review by relevant subject matter experts on the team; (2) Editorial review for consistency, clarity, and formatting; (3) Team Leader quality verification ensuring compliance with ToR requirements; (4) Client review and feedback incorporation. Version control systems ensure all changes are tracked and documented.

**Key Performance Indicators**

The following KPIs will guide quality assurance:
- Timeliness: All deliverables submitted within specified deadlines
- Completeness: All ToR requirements fully addressed in deliverables
- Technical accuracy: Recommendations grounded in evidence and aligned with international standards
- Stakeholder satisfaction: Positive feedback from EQA, MDLF, and World Bank on deliverable quality
- Usability: HWMP documents practical and implementable by Palestinian institutions

**Monitoring and Reporting Protocols**

Weekly internal team meetings will monitor progress against work plan milestones. Monthly progress reports will be submitted to EQA and MDLF summarizing activities completed, issues encountered, and upcoming milestones. Regular coordination meetings (in-person and online) with client representatives will ensure alignment and enable timely feedback. All feedback will be systematically documented and addressed in subsequent deliverable versions.

**Document Quality Standards**

All reports and the HWMP will be produced in both Arabic and English to professional standards. Documents will be submitted in editable formats (MS Word, Excel, PowerPoint) and PDF format. GIS outputs will meet EQA technical specifications for integration with existing systems. Visual elements including maps, diagrams, and tables will be clear, accurate, and professionally formatted."""
}

# Generate Word document
lang_config = get_language_config('en')
output_path = "metodologia_hwmp_palestine.docx"

print("Creating Word document...")
create_word_document(methodology, output_path, lang_config)
print(f"Document created successfully: {output_path}")
