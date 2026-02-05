#!/usr/bin/env python3
"""
Generador de metodología para India H&S Platform Phase 2
World Bank - Consultancy Services for Developing Safety Manual Addendums
"""

import os
import json
from dotenv import load_dotenv
from src.document_writer import create_word_document
from src.translations import get_language_config

load_dotenv()


def generate_india_hs_methodology():
    """
    Genera la metodología para el proyecto India H&S Platform Phase 2

    El proyecto incluye:
    - Task 1: Update regulatory environment for H&S (Transport, Urban, Building)
    - Task 2: Develop Safety Manual Addendums for 3 sectors
    - Task 3: Prepare H&S Specifications for bidding documents
    - Task 4: Prepare training materials
    - Task 5: Deliver trainings (Delhi + 4 regional offices)
    - Task 6: Project specific H&S support (10 days)
    - Task 7: Train the Trainer workshop (Colombo, Sri Lanka)

    Deliverables:
    D1: Inception Report (D1+7)
    D2: Draft Safety Manual Addendums (D1+45)
    D3: Draft H&S Specifications (D1+60)
    D4: Final Safety Manual Addendums (D1+90)
    D5: Final Specifications (D1+105)
    D6: Training materials (D1+120)
    D7: Delhi & Train the Trainer trainings + report (D1+150)
    D8: Regional trainings + report
    D9: Project specific support
    """

    methodology = {
        "introduction": """Our consortium brings together specialized expertise in occupational health and safety (OHS), community health and safety (CHS), infrastructure project management, and capacity building across the Transport, Urban, and Building Construction sectors in India and South Asia. We have carefully reviewed the Terms of Reference for the India Health and Safety Platform Phase 2 and understand the World Bank's commitment to achieving zero fatality on Bank-financed projects through strengthening government agency and contractor capacity to manage H&S risks.

Our approach builds upon the successful Phase 1 Safety Manual for General High Energy Hazards, extending its practical application to sector-specific contexts. We recognize that effective H&S management requires not just technical documentation, but materials that are practical, accessible, and actionable for PIUs, contractors, and workers at construction sites across India's diverse regions. Our methodology emphasizes stakeholder engagement, real-world applicability, and sustainable capacity building through comprehensive training programs.""",

        "context": """**Project Background and Rationale**

The South Asian Region (SAR) Portfolio review of incidents and fatalities registered between 2010-2021 revealed critical gaps in health and safety management on World Bank-financed projects. In response, the World Bank established the Health and Safety (H&S) Platform for SAR, operational since FY22, with the objective of supporting Bank clients in implementing H&S requirements under the Environmental and Social Framework (ESF), specifically ESS2 (Labor and Working Conditions) and ESS4 (Community Health and Safety).

Phase 1 of the India H&S Platform successfully developed a Construction Safety Manual addressing general high-energy hazards including: work at heights, excavation and trenching, confined spaces, electrical hazards, lifting operations and crane safety, mobile vehicle incidents, hot works, demolition and structural instability, soil stability, working in congested areas, tree cutting, and sewer/sanitation works. This foundational manual established critical controls for high-energy hazards applicable across construction projects.

**Phase 2 Scope and Objectives**

Phase 2 focuses on extending this framework to sector-specific applications across three priority sectors that contribute most to fatalities in India Projects:

1. **Linear Infrastructure (Transport)**: Roads, rails, and power transmission lines
2. **Urban Sector Projects**: Water supply, sewerage, and waste management (solid, C&D, plastic, biomedical, e-waste, batteries, hazardous wastes)
3. **Large Building Construction**: Educational facilities, hospitals, disaster management infrastructure, and coastal infrastructure

The assignment encompasses seven interconnected tasks: regulatory review, Safety Manual Addendum development, H&S specification preparation, training material development, training delivery across India and Sri Lanka, project-specific technical support, and capacity building for SAR H&S Focal Points.

**Institutional Framework and Stakeholders**

The project operates within India's evolving occupational safety landscape, governed by the Occupational Safety, Health and Working Conditions Code 2020, Building and Other Construction Workers Act 1996, and various state-level regulations. Key stakeholders include:

- World Bank India Country Office and SAR H&S Focal Points
- Federal Ministry of Labour & Employment and State Labour Departments
- Project Implementation Units (PIUs) across Transport, Urban, and Building sectors
- Contractors, subcontractors, and workers on Bank-financed projects
- Local communities surrounding construction sites

**Geographic Context**

Training delivery will span five locations across India (New Delhi, North, South, East, and West regional offices) plus Colombo, Sri Lanka for the Train the Trainer workshop, requiring materials adaptable to diverse linguistic, climatic, and operational contexts.""",

        "principles": [
            {
                "name": "Zero Fatality Commitment",
                "description": "Every activity we undertake is guided by the World Bank's zero fatality objective. Our materials prioritize prevention of severe injuries and fatalities through clear identification of high-energy hazards, critical controls, and non-negotiable safety requirements. We design specifications with enforceable compliance mechanisms and penalties that incentivize contractors to prioritize worker and community safety."
            },
            {
                "name": "Practical Real-World Applicability",
                "description": "Safety guidelines are only effective when they can be readily understood and applied on construction sites. We develop materials using pictorial representations, dos and don'ts formats, and real-world examples from Indian construction contexts. Our approach ensures materials are accessible to workers with varying literacy levels and can be easily communicated to surrounding communities."
            },
            {
                "name": "Sector-Specific Expertise",
                "description": "Each sector presents unique H&S challenges requiring specialized knowledge. Our team includes dedicated sector experts for Transport (roads/rail), Urban (water/sewerage/waste), and Building Construction (power infrastructure/large buildings), ensuring addendums address specific hazards, equipment, and operational contexts while cross-referencing the Phase 1 Manual's foundational controls."
            },
            {
                "name": "Stakeholder-Centered Development",
                "description": "Effective H&S materials require input from those who will implement them. We engage PIU members, contractors, and workers through structured consultations during the inception phase and validation workshops during drafting. This ensures materials address real operational challenges and incorporate lessons learned from incident investigations."
            },
            {
                "name": "Sustainable Capacity Building",
                "description": "Training delivery extends beyond one-time events to create lasting institutional capacity. Our Train the Trainer approach equips SAR H&S Focal Points to deliver training across their respective countries, while regional trainings in India create networks of trained professionals who can cascade knowledge to contractors and workers throughout the project lifecycle."
            },
            {
                "name": "Compliance and Accountability",
                "description": "H&S specifications must be enforceable through clear contractual mechanisms. We develop detailed specifications aligned with WB ESF, EHS Guidelines, and Indian regulations, with specific non-compliance criteria and penalty structures that PIUs can incorporate into standard bidding documents. This creates accountability frameworks that translate safety requirements into contractor obligations."
            }
        ],

        "phases": [
            {
                "title": "Phase 1: Inception and Regulatory Review",
                "description": """This phase establishes the foundation for all subsequent deliverables through comprehensive project planning, stakeholder mapping, and regulatory analysis. We will conduct a thorough review of additional H&S regulations applicable specifically to Transport, Urban, and Building Construction sectors beyond those compiled in Phase 1. The inception phase includes mobilization of our expert team, establishment of coordination mechanisms with the World Bank India Country Office, and development of detailed work plans for each task stream.

Our regulatory review will identify sector-specific requirements from national legislation (Occupational Safety Code 2020, Building Workers Act, Motor Vehicles Act, Electricity Act), state-level regulations, and international Good International Industry Practices (GIIPs) including IFC EHS Guidelines. This compilation will serve as the normative foundation for Safety Manual Addendums and H&S Specifications.""",
                "start_week": 1,
                "end_week": 7,
                "tasks": [
                    {
                        "code": "1A",
                        "title": "Project Mobilization and Work Planning",
                        "description": """We will mobilize our full team including Team Leader, Sector Experts (Transport, Urban, Building/Electrical), Senior H&S Expert, India-based H&S Expert/Trainer, and CHS/Labour/Gender Expert. Initial activities include establishing project management protocols, communication channels with the World Bank, and internal quality assurance procedures.

A detailed work plan will be developed covering all seven tasks with specific milestones, responsibilities, and resource allocation. We will establish the document management system, stakeholder database, and training coordination mechanisms. The work plan will include contingency provisions for the project-specific support days (Task 6) to ensure flexible deployment throughout the contract period.""",
                        "items": [
                            "Mobilize expert team and establish roles and responsibilities",
                            "Set up project management systems and communication protocols",
                            "Develop detailed work plan with milestones for Tasks 1-7",
                            "Establish document templates for addendums and specifications",
                            "Create stakeholder database and engagement schedule"
                        ],
                        "start_week": 1,
                        "end_week": 2
                    },
                    {
                        "code": "1B",
                        "title": "Stakeholder Consultations and Document Review",
                        "description": """We will conduct comprehensive consultations with key stakeholders including PIU representatives, contractors operating on Bank-financed projects, and World Bank task teams. These consultations will gather input on practical challenges encountered in implementing Phase 1 Safety Manual, identify sector-specific hazards requiring attention, and understand operational contexts across different regions.

Simultaneously, we will review existing bidding and contract documents from Bank-supported projects to understand current H&S specification formats and identify gaps. This review will inform the proposed format and content structure for Safety Manual Addendums and H&S Specifications to be agreed with the World Bank.""",
                        "items": [
                            "Conduct consultations with PIU representatives from Transport, Urban, and Building sectors",
                            "Interview contractors and safety officers on Bank-financed projects",
                            "Review existing bidding documents and contract specifications",
                            "Analyze incident reports and lessons learned from Phase 1",
                            "Document stakeholder feedback and operational challenges"
                        ],
                        "start_week": 2,
                        "end_week": 5
                    },
                    {
                        "code": "1C",
                        "title": "Regulatory Review and Compilation",
                        "description": """Building upon Phase 1's general regulatory review, we will compile additional sector-specific regulations applicable to Transport (road construction safety, railway safety rules, power line proximity requirements), Urban (water supply and sewerage construction, waste handling and disposal, treatment plant construction), and Building Construction (high-rise safety, electrical installation codes, demolition regulations).

The compilation will cross-reference Phase 1 findings and identify any gaps or updates to national/state regulations. We will also review relevant international standards and GIIPs including ISO 45001, OSHA construction standards, and ILO guidance for construction safety. The output will be a comprehensive regulatory matrix by sector.""",
                        "items": [
                            "Review Transport sector regulations (roads, rail, power lines)",
                            "Review Urban sector regulations (water, sewerage, waste management)",
                            "Review Building Construction regulations (electrical, high-rise, demolition)",
                            "Compile international standards and GIIPs relevant to each sector",
                            "Prepare regulatory matrix cross-referenced with Phase 1 Manual"
                        ],
                        "start_week": 3,
                        "end_week": 6
                    },
                    {
                        "code": "1D",
                        "title": "Inception Report Preparation and Submission",
                        "description": """We will prepare a comprehensive Inception Report consolidating all Phase 1 findings including: preliminary list of additional regulations identified, detailed timeline for Tasks 1-7 with resource allocation, proposed format and contents for Safety Manual Addendums, and proposed format and contents for H&S Specifications.

The report will include stakeholder engagement findings, document review results, and recommendations for the structure of sector-specific materials. We will submit the draft report to the World Bank for review and incorporate feedback before finalization. The agreed formats will serve as templates for subsequent deliverables.""",
                        "items": [
                            "Compile findings from stakeholder consultations and document review",
                            "Develop proposed format and table of contents for Safety Manual Addendums",
                            "Develop proposed format and structure for H&S Specifications",
                            "Prepare detailed timeline and resource plan for remaining tasks",
                            "Submit Inception Report and incorporate World Bank feedback"
                        ],
                        "start_week": 5,
                        "end_week": 7,
                        "deliverable_week": 7
                    }
                ],
                "deliverables": [
                    {"code": "D1", "name": "Inception Report with regulatory compilation, proposed formats, and detailed timeline"}
                ]
            },
            {
                "title": "Phase 2: Development of Safety Manual Addendums",
                "description": """This phase focuses on developing sector-specific Safety Manual Addendums for Linear Infrastructure (Transport), Urban Sector Projects, and Large Building Construction. Following the approach established in Phase 1, each addendum will be structured as a "Sector Book" that cross-references the existing Safety Manual while providing detailed guidance on sector-specific hazards, critical controls, and practical applications.

Our Sector Experts will lead the technical content development for their respective domains, working closely with the Senior H&S Expert to ensure consistency with Phase 1 materials and international best practices. Materials will be developed in English with extensive use of pictorial representations showing dos and don'ts using real-world examples from Indian construction sites. All materials will be designed for easy comprehension by workers and for sharing with local communities surrounding construction sites.""",
                "start_week": 8,
                "end_week": 45,
                "tasks": [
                    {
                        "code": "2A",
                        "title": "Transport Sector Addendum Development (Roads, Rail, Power Lines)",
                        "description": """The Transport Sector Expert will develop comprehensive guidance for Linear Infrastructure covering road construction and rehabilitation, railway construction and maintenance, and power transmission line installation. Key hazards addressed will include: traffic management in live road environments, work near active rail corridors, electrical hazards from overhead and underground lines, heavy equipment operation in linear worksites, and slope stability on road embankments.

The addendum will include detailed critical controls, permit-to-work templates specific to transport infrastructure, and practical checklists for daily safety inspections. Pictorial guides will illustrate proper traffic management layouts, safe distances from rail operations, and exclusion zones for power line works. Information on smart tools and devices for safety monitoring will be provided.""",
                        "items": [
                            "Develop road construction/rehabilitation safety guidance with traffic management protocols",
                            "Prepare rail corridor safety controls and permit requirements",
                            "Document power line proximity hazards and electrical safety controls",
                            "Create pictorial dos and don'ts for transport sector activities",
                            "Compile smart tools and devices for transport sector safety monitoring"
                        ],
                        "start_week": 8,
                        "end_week": 35
                    },
                    {
                        "code": "2B",
                        "title": "Urban Sector Addendum Development (Water, Sewerage, Waste Management)",
                        "description": """The Urban Sector Expert will develop guidance covering water supply infrastructure (pipelines, pumping stations, treatment plants), sewerage systems (collection networks, pumping stations, treatment facilities), and comprehensive waste management including solid waste, C&D debris, plastic, biomedical waste, e-waste, batteries, and hazardous wastes. This includes construction of landfills, dumpsite rehabilitation, and recycling/treatment facilities.

Critical hazards addressed include confined space entry in manholes and tanks, exposure to hazardous gases (H2S, methane), handling of contaminated materials, trenching in urban environments with utility conflicts, and chemical hazards in treatment processes. The addendum will include specific protocols for manual scavenging prohibition compliance, biological hazard controls, and community safety during urban construction.""",
                        "items": [
                            "Develop water supply infrastructure safety guidance (pipelines, plants)",
                            "Prepare sewerage system construction and rehabilitation safety controls",
                            "Document waste management facility construction hazards (all waste types)",
                            "Address confined space, gas hazards, and biological exposure controls",
                            "Create pictorial guides for urban sector activities and community safety"
                        ],
                        "start_week": 8,
                        "end_week": 35
                    },
                    {
                        "code": "2C",
                        "title": "Building Construction Sector Addendum Development",
                        "description": """The Building/Electrical Sector Expert will develop guidance for large building construction including educational facilities, hospitals, disaster management infrastructure, and coastal infrastructure, as well as electrical/power infrastructure associated with transmission lines and metro projects.

Key hazards addressed include work at height in multi-story construction, electrical installation safety, structural stability during construction phases, demolition of existing structures, foundation work in challenging soil conditions, and specialized requirements for healthcare and coastal facilities. The addendum will integrate electrical safety protocols with general construction safety, addressing both occupational and community health impacts.""",
                        "items": [
                            "Develop high-rise building construction safety guidance",
                            "Prepare electrical infrastructure and installation safety controls",
                            "Document specialized requirements for hospitals, schools, coastal facilities",
                            "Address demolition safety and structural stability controls",
                            "Create pictorial guides for building construction activities"
                        ],
                        "start_week": 8,
                        "end_week": 35
                    },
                    {
                        "code": "2D",
                        "title": "Draft Addendums Compilation and Internal Review",
                        "description": """The three sector addendums will be compiled into a consistent format, ensuring cross-references to the Phase 1 Safety Manual are accurate and comprehensive. Our internal quality assurance team will review all materials for technical accuracy, regulatory compliance, practical applicability, and consistency of approach across sectors.

The Senior H&S Expert will ensure international best practices are appropriately adapted to the Indian context. The CHS, Labour and Gender Expert will review all materials to ensure community safety considerations, labour law compliance, and gender-sensitive approaches are integrated throughout. Draft materials will be prepared for submission to the World Bank.""",
                        "items": [
                            "Compile and format three sector addendums consistently",
                            "Ensure accurate cross-references to Phase 1 Safety Manual",
                            "Conduct technical review for accuracy and completeness",
                            "Review for CHS, labour law compliance, and gender considerations",
                            "Prepare draft addendums for World Bank submission"
                        ],
                        "start_week": 36,
                        "end_week": 45,
                        "deliverable_week": 45
                    }
                ],
                "deliverables": [
                    {"code": "D2", "name": "Draft Safety Manual Addendums for Transport, Urban, and Building Construction sectors"}
                ]
            },
            {
                "title": "Phase 3: Development of H&S Specifications",
                "description": """This phase develops detailed H&S specifications that PIUs can incorporate into standard bidding documents for each sector. Specifications will be structured by work component/activity (e.g., reconstruction of existing roads, new road laying, water pipeline installation, sewage treatment plant demolition) with both general specifications applicable across all operations and activity-specific requirements.

All specifications will align with the Safety Manual and Addendums, WB ESF requirements, EHS Guidelines, national regulations, and GIIPs. Critically, specifications will include enforceable non-compliance criteria with associated penalty structures, creating accountability mechanisms that incentivize contractor safety performance. The format will be practical for direct insertion into existing PIU bidding document templates.""",
                "start_week": 46,
                "end_week": 60,
                "tasks": [
                    {
                        "code": "3A",
                        "title": "General H&S Specifications Development",
                        "description": """We will develop a core set of general H&S specifications applicable across all sectors and operations, covering fundamental requirements for: contractor H&S management systems, competent person requirements, worker training and induction, PPE provision and usage, incident reporting and investigation, emergency preparedness, and worker welfare facilities.

General specifications will establish baseline H&S requirements that apply to all contracts regardless of sector or activity type, including requirements for H&S plans, organizational structure, safety officer qualifications, and documentation. These specifications will reference the Phase 1 Safety Manual's critical controls for high-energy hazards as mandatory requirements.""",
                        "items": [
                            "Develop contractor H&S management system specifications",
                            "Prepare competent person and safety officer requirements",
                            "Document worker training, induction, and certification requirements",
                            "Specify PPE standards, incident reporting, and emergency preparedness",
                            "Establish general penalty structure for H&S non-compliance"
                        ],
                        "start_week": 46,
                        "end_week": 50
                    },
                    {
                        "code": "3B",
                        "title": "Sector-Specific Specifications Development",
                        "description": """Building on general specifications, we will develop activity-specific H&S requirements for each sector. Transport specifications will cover road reconstruction, new road construction, rail works, and power line installation. Urban specifications will address water pipeline laying, pumping station construction, sewage treatment plant works (including demolition), and waste management facility construction. Building specifications will cover new construction, renovation, demolition, and electrical installations.

Each activity specification will include: specific hazard controls, permit requirements, equipment certifications, inspection frequencies, monitoring requirements, and performance indicators. Specifications will be formatted for direct insertion into relevant bidding document sections.""",
                        "items": [
                            "Develop Transport sector activity specifications (roads, rail, power)",
                            "Prepare Urban sector activity specifications (water, sewerage, waste)",
                            "Document Building sector activity specifications (construction, demolition, electrical)",
                            "Format specifications for insertion into standard bidding documents",
                            "Cross-reference with Safety Manual Addendums"
                        ],
                        "start_week": 48,
                        "end_week": 55
                    },
                    {
                        "code": "3C",
                        "title": "Non-Compliance Criteria and Penalty Framework",
                        "description": """We will develop a comprehensive non-compliance framework specifying clear criteria for identifying H&S violations, categorization of violations by severity (minor, major, critical), and associated penalty structures including financial penalties, work suspension triggers, and contract termination criteria.

The framework will provide PIUs with practical tools for enforcement including inspection checklists, violation documentation templates, and escalation procedures. Penalties will be graduated to incentivize prompt correction while creating meaningful consequences for persistent non-compliance. The framework will align with Indian contract law requirements for enforceability.""",
                        "items": [
                            "Develop violation categorization criteria (minor, major, critical)",
                            "Establish penalty structures aligned with Indian contract law",
                            "Create inspection checklists and violation documentation templates",
                            "Document escalation procedures and work suspension triggers",
                            "Prepare guidance for PIU specification insertion and enforcement"
                        ],
                        "start_week": 53,
                        "end_week": 58
                    },
                    {
                        "code": "3D",
                        "title": "Draft Specifications Compilation and Submission",
                        "description": """All specifications will be compiled into a comprehensive document organized by sector and activity type. The compilation will include guidance notes for PIUs on how to incorporate specifications into existing bidding document formats, how to apply penalty frameworks, and how to monitor contractor compliance during implementation.

Internal quality review will ensure specifications are complete, consistent with Safety Manual Addendums, and practically implementable. Draft specifications will be submitted to the World Bank for review alongside the draft Safety Manual Addendums to enable coordinated feedback.""",
                        "items": [
                            "Compile all specifications into comprehensive document",
                            "Prepare PIU guidance on specification incorporation",
                            "Conduct internal quality review for completeness and consistency",
                            "Format for World Bank submission",
                            "Prepare presentation materials for specification review meeting"
                        ],
                        "start_week": 56,
                        "end_week": 60,
                        "deliverable_week": 60
                    }
                ],
                "deliverables": [
                    {"code": "D3", "name": "Draft H&S Specifications for Transport, Urban, and Building sectors with penalty framework"}
                ]
            },
            {
                "title": "Phase 4: Finalization of Safety Manual Addendums and Specifications",
                "description": """This phase incorporates feedback from the World Bank and other stakeholders (PIUs, sector agencies) on draft Safety Manual Addendums and H&S Specifications. We will conduct validation workshops with PIU representatives to test the practical applicability of materials, gather final input on format and content, and ensure materials meet the operational needs of implementing agencies.

The finalization process will address all review comments systematically, document responses to feedback, and produce polished final versions ready for publication and dissemination. Final materials will be formatted for both print and digital distribution, with pictorial guides optimized for on-site use.""",
                "start_week": 61,
                "end_week": 105,
                "tasks": [
                    {
                        "code": "4A",
                        "title": "Stakeholder Validation Workshops",
                        "description": """We will organize validation workshops with PIU representatives, contractors, and World Bank sector teams to review draft Safety Manual Addendums and Specifications. Workshops will be structured by sector to allow focused discussion on sector-specific materials while also gathering cross-cutting feedback on general approaches.

Participants will include project managers, E&S specialists, and procurement specialists who will ultimately use these materials. Workshop activities will include hands-on review of pictorial guides, simulation of specification application in bidding contexts, and discussion of enforcement mechanisms. Feedback will be documented systematically for incorporation.""",
                        "items": [
                            "Organize Transport sector validation workshop",
                            "Organize Urban sector validation workshop",
                            "Organize Building Construction sector validation workshop",
                            "Document all feedback systematically with response matrix",
                            "Identify priority revisions based on stakeholder input"
                        ],
                        "start_week": 61,
                        "end_week": 70
                    },
                    {
                        "code": "4B",
                        "title": "Revision of Safety Manual Addendums",
                        "description": """Based on World Bank and stakeholder feedback, we will revise all three sector addendums to address comments, improve clarity, correct technical issues, and enhance practical applicability. Revisions will be tracked using change management protocols to document how each comment was addressed.

Particular attention will be paid to ensuring pictorial materials effectively communicate critical safety messages to the intended audience including workers with limited literacy. Additional real-world examples may be developed based on stakeholder input about common scenarios encountered on their projects.""",
                        "items": [
                            "Address World Bank review comments on all three addendums",
                            "Incorporate stakeholder workshop feedback",
                            "Enhance pictorial guides based on user testing feedback",
                            "Update regulatory references as needed",
                            "Prepare change log documenting all revisions"
                        ],
                        "start_week": 68,
                        "end_week": 85
                    },
                    {
                        "code": "4C",
                        "title": "Final Safety Manual Addendums Submission",
                        "description": """Final Safety Manual Addendums will be prepared incorporating all revisions and formatted for publication. Materials will be provided in both editable (Word) and final (PDF) formats suitable for print and digital distribution. High-resolution pictorial guides will be provided separately for potential poster printing for construction sites.

Final submission will include a summary of changes from draft to final versions and documentation of how all review comments were addressed. The addendums will be ready for use in training programs and for dissemination to PIUs across India.""",
                        "items": [
                            "Finalize all three sector addendums with professional formatting",
                            "Prepare print-ready and digital versions",
                            "Extract high-resolution pictorials for site poster use",
                            "Document all changes from draft to final",
                            "Submit final Safety Manual Addendums to World Bank"
                        ],
                        "start_week": 83,
                        "end_week": 90,
                        "deliverable_week": 90
                    },
                    {
                        "code": "4D",
                        "title": "Revision and Finalization of H&S Specifications",
                        "description": """Similarly, H&S Specifications will be revised based on World Bank and PIU feedback. Particular focus will be given to ensuring specifications are practical for incorporation into existing bidding document formats used by implementing agencies, and that penalty frameworks are enforceable under Indian contract law.

Final specifications will be formatted as ready-to-use modules that PIUs can directly insert into their standard bidding documents with minimal adaptation. Guidance materials for PIUs will be refined based on feedback about practical implementation challenges.""",
                        "items": [
                            "Address World Bank review comments on specifications",
                            "Incorporate PIU feedback on practical implementability",
                            "Refine penalty framework based on legal review feedback",
                            "Update PIU guidance materials",
                            "Submit final H&S Specifications to World Bank"
                        ],
                        "start_week": 90,
                        "end_week": 105,
                        "deliverable_week": 105
                    }
                ],
                "deliverables": [
                    {"code": "D4", "name": "Final Safety Manual Addendums for Transport, Urban, and Building sectors"},
                    {"code": "D5", "name": "Final H&S Specifications with penalty framework and PIU guidance"}
                ]
            },
            {
                "title": "Phase 5: Training Development and Delivery",
                "description": """This phase encompasses the development of training materials and delivery of comprehensive training programs across multiple locations. Training is designed to build sustainable capacity for H&S implementation, targeting PIU members (project managers, E&S specialists, procurement specialists), contractors, and ultimately creating a cadre of trainers who can cascade training across the South Asia Region.

Training programs will cover both the Safety Manual Addendums and H&S Specifications, with practical exercises enabling participants to apply concepts to real project scenarios. The India-based H&S Expert/Trainer will lead regional training delivery, ensuring materials are contextualized for local conditions while maintaining consistency with core content.""",
                "start_week": 106,
                "end_week": 150,
                "tasks": [
                    {
                        "code": "5A",
                        "title": "Training Materials Development",
                        "description": """We will develop comprehensive training materials (PowerPoint slides, facilitator guides, participant handbooks, and practical exercises) covering all Safety Manual Addendums and H&S Specifications. Materials will include sector-specific modules allowing trainings to be tailored for Transport, Urban, or Building sector audiences.

Training content will feature local pictures of good and bad practices from Indian construction sites, clear dos and don'ts, and case studies based on actual incidents. Interactive elements will include group exercises, role plays for specification enforcement scenarios, and site simulation activities. Materials will be developed in English with visual content designed for multilingual audiences.""",
                        "items": [
                            "Develop core training slides covering Safety Manual Addendums",
                            "Prepare sector-specific training modules",
                            "Create H&S Specifications training materials with enforcement exercises",
                            "Develop facilitator guides and participant handbooks",
                            "Prepare assessment tools and training evaluation forms"
                        ],
                        "start_week": 106,
                        "end_week": 115
                    },
                    {
                        "code": "5B",
                        "title": "New Delhi Training Delivery",
                        "description": """The Team Leader and Local H&S Expert will deliver training at a venue in New Delhi (World Bank office or nearby training venue) over four days (one day preparation, three days delivery). Training will target PIU members including project managers, E&S specialists, and procurement specialists from all three sectors.

Day 1 will cover Safety Manual overview and general H&S principles. Day 2 will focus on sector-specific addendums with breakout sessions by sector. Day 3 will cover H&S Specifications and enforcement mechanisms including practical exercises on applying specifications in procurement contexts. Training will include Q&A sessions and feedback collection for continuous improvement.""",
                        "items": [
                            "Conduct pre-training preparation and logistics coordination",
                            "Deliver Day 1: Safety Manual overview and H&S principles",
                            "Deliver Day 2: Sector-specific addendums with breakout sessions",
                            "Deliver Day 3: H&S Specifications and enforcement",
                            "Collect participant feedback and document lessons learned"
                        ],
                        "start_week": 125,
                        "end_week": 130
                    },
                    {
                        "code": "5C",
                        "title": "Train the Trainer Workshop (Colombo, Sri Lanka)",
                        "description": """Immediately following the Delhi training, the Team Leader and Senior H&S Expert will deliver a two-day Train the Trainer workshop in Colombo, Sri Lanka for SAR H&S Focal Points. This workshop will equip Focal Points to deliver Safety Manual, Addendum, and Specification training in their respective countries (Bangladesh, Nepal, Sri Lanka, Bhutan, Maldives).

The workshop will cover adult learning principles, facilitation techniques for H&S training, adaptation of materials for local contexts, and practical delivery sessions where participants practice delivering training modules. Focal Points will receive complete training packages and support materials for independent delivery.""",
                        "items": [
                            "Coordinate logistics with World Bank SAR team",
                            "Deliver Day 1: Training methodology and Safety Manual content",
                            "Deliver Day 2: Practical facilitation and country adaptation",
                            "Provide complete training packages to Focal Points",
                            "Prepare Train the Trainer workshop report"
                        ],
                        "start_week": 130,
                        "end_week": 135
                    },
                    {
                        "code": "5D",
                        "title": "Regional Training Delivery (4 Locations)",
                        "description": """The India-based H&S Expert(s) will deliver training at four regional PMU/PIU offices (North, South, East, West India) selected based on availability at time of training. Regional trainings will cover both the Safety Manual with Addendums and the Specifications, adapted for the predominant project types in each region.

Trainings will be staggered throughout the assignment period to allow lessons learned from earlier sessions to improve subsequent deliveries. Regional trainings will focus on practical application with site-specific examples relevant to local project contexts. Training reports will document attendance, content delivered, participant feedback, and recommendations.""",
                        "items": [
                            "Coordinate with regional PIU offices for training scheduling",
                            "Deliver training at North India regional office",
                            "Deliver training at South India regional office",
                            "Deliver training at East India regional office",
                            "Deliver training at West India regional office"
                        ],
                        "start_week": 135,
                        "end_week": 150,
                        "deliverable_week": 150
                    }
                ],
                "deliverables": [
                    {"code": "D6", "name": "Training materials for Safety Manual Addendums and H&S Specifications"},
                    {"code": "D7", "name": "New Delhi and Train the Trainer training delivery report"},
                    {"code": "D8", "name": "Regional trainings delivery report (4 locations)"}
                ]
            },
            {
                "title": "Phase 6: Project-Specific Support and Close-Out",
                "description": """This phase provides flexible project-specific H&S support (10 days allocated for the Local H&S Expert) available to any Bank-financed project in India throughout the contract period. Support may include targeted training delivery, inputs to bidding documents, site visits for H&S assessment, incident investigation support, or review of technical documents. Additionally, this phase includes preparation of the final project close-out report documenting all deliverables, lessons learned, and recommendations.

The flexible support days ensure the consultancy can respond to emerging needs while the close-out report provides comprehensive documentation of the assignment for institutional learning.""",
                "start_week": 1,
                "end_week": 150,
                "tasks": [
                    {
                        "code": "6A",
                        "title": "Project-Specific H&S Support",
                        "description": """Ten days are allocated for the Local H&S Expert to provide targeted support to specific projects as agreed between the World Bank and Consultant. Support may include: delivery of customized training sessions for specific project teams; inputs to bidding documents being prepared by PIUs; site visits to assess H&S conditions and provide recommendations; support for incident investigation and root cause analysis; and review of contractor H&S plans or technical documents.

Support requests will be coordinated through the World Bank India Country Office with advance notice to allow appropriate preparation. Each support activity will be documented with brief reports summarizing activities undertaken and recommendations provided.""",
                        "items": [
                            "Respond to project-specific training delivery requests",
                            "Provide inputs to bidding document preparation as requested",
                            "Conduct site visits for H&S assessment",
                            "Support incident investigation when requested",
                            "Review contractor H&S plans and technical documents"
                        ],
                        "start_week": 1,
                        "end_week": 150
                    },
                    {
                        "code": "6B",
                        "title": "Assignment Close-Out and Reporting",
                        "description": """Upon completion of all deliverables and training activities, we will prepare a comprehensive close-out report documenting the full assignment including: summary of all deliverables produced; training activities completed with participant numbers and feedback analysis; project-specific support provided; lessons learned during implementation; and recommendations for future H&S capacity building activities.

The close-out report will provide the World Bank with a complete record of the assignment and actionable recommendations for sustaining the capacity built through this consultancy. All final deliverable files will be organized and transferred to the World Bank in agreed formats.""",
                        "items": [
                            "Compile comprehensive summary of all deliverables",
                            "Analyze training feedback and document outcomes",
                            "Document lessons learned and best practices",
                            "Prepare recommendations for future H&S initiatives",
                            "Organize and transfer all deliverable files"
                        ],
                        "start_week": 145,
                        "end_week": 150,
                        "deliverable_week": 150
                    }
                ],
                "deliverables": [
                    {"code": "D9", "name": "Project-specific support documentation and close-out report"}
                ]
            }
        ],

        "risks": """**Risk Management Framework**

Our approach to risk management encompasses identification, assessment, mitigation, and monitoring of risks that could affect the successful delivery of this assignment. We have identified the following key risk categories and corresponding mitigation measures:

**Stakeholder Engagement Risks**

*Risk: Limited PIU availability for consultations and validation workshops*
Given the operational demands on PIU staff, there is a risk of limited availability for consultations during the inception phase and validation workshops during finalization. This could result in materials that do not fully address practical implementation challenges.

*Mitigation: Early engagement scheduling and flexible consultation formats*
We will identify key PIU contacts during the first week of mobilization and schedule consultations well in advance. We will offer flexible consultation formats including virtual sessions, written questionnaires, and site-based discussions to accommodate PIU schedules. For validation workshops, we will coordinate timing with the World Bank to align with other events that bring PIU representatives together.

**Technical Quality Risks**

*Risk: Inconsistency between Safety Manual Addendums and existing Phase 1 Manual*
Given that different sector experts will develop addendums in parallel, there is a risk of inconsistent approaches, terminology, or cross-referencing with the Phase 1 Safety Manual.

*Mitigation: Centralized quality assurance and editorial review*
The Senior H&S Expert will maintain oversight of all addendum development to ensure consistency with Phase 1 approaches and terminology. Editorial review will harmonize all materials before submission. Regular coordination meetings among sector experts will identify and resolve inconsistencies early.

*Risk: Specifications not practically implementable in existing PIU bidding systems*
H&S specifications may not align with existing bidding document formats or procurement systems used by implementing agencies, reducing their practical utility.

*Mitigation: Early review of existing bidding documents and PIU consultation*
Our inception phase includes comprehensive review of existing bidding documents to understand current formats. We will consult with PIU procurement specialists on practical insertion requirements. Draft specifications will be tested against actual bidding document templates during validation workshops.

**Training Delivery Risks**

*Risk: Variable participant engagement and knowledge retention across training locations*
Training effectiveness may vary across the five India locations plus Colombo due to differences in participant backgrounds, local project contexts, and language barriers.

*Mitigation: Standardized content with local adaptation and interactive delivery*
Core training content will be standardized while allowing for local adaptation of examples and case studies. Extensive use of visual materials reduces language barriers. Interactive exercises and practical applications reinforce learning. Post-training materials including participant handbooks support ongoing reference.

*Risk: Logistics challenges for regional training coordination*
Coordinating training at four regional PIU offices plus Delhi and Colombo involves significant logistics that could be disrupted by scheduling conflicts, venue availability, or travel restrictions.

*Mitigation: Advance scheduling with contingency planning*
Training schedules will be established early in the assignment with World Bank support for PIU coordination. Backup dates will be identified for each location. Virtual delivery contingency plans will be prepared in case of travel restrictions.

**Regulatory and Policy Risks**

*Risk: Changes to Indian H&S regulations during assignment period*
India's occupational safety regulatory framework is evolving with implementation of the Occupational Safety, Health and Working Conditions Code 2020. Regulatory changes during the assignment could affect the accuracy of compiled regulations and specifications.

*Mitigation: Continuous regulatory monitoring and update protocol*
We will monitor regulatory developments throughout the assignment and flag any significant changes to the World Bank. Materials will be designed to accommodate updates through modular formatting. The close-out report will identify any pending regulatory changes that may require future material updates.

**Contingency Measures**

For any identified risk that materializes, our response protocol includes: immediate notification to the World Bank Task Team Lead; assessment of impact on deliverable quality and timeline; proposal of mitigation actions; and implementation upon World Bank agreement. Our team structure with multiple experts per sector provides redundancy if individual team member availability is affected.""",

        "quality": """**Quality Assurance Framework**

Our quality assurance framework ensures all deliverables meet World Bank standards, align with ESF requirements, and provide practical value for implementing agencies. Quality assurance is integrated throughout the assignment lifecycle through the following mechanisms:

**Quality Control Procedures**

*Document Review Protocol*: All deliverables undergo a three-tier review process: (1) Technical review by the responsible Sector Expert; (2) Quality review by the Senior H&S Expert for consistency, accuracy, and international best practice alignment; (3) Editorial review for clarity, formatting, and accessibility. The Team Leader provides final sign-off before submission.

*Compliance Verification*: Each deliverable is verified against a compliance checklist ensuring alignment with: World Bank ESF requirements (ESS2, ESS4); IFC EHS Guidelines; Indian national and state regulations; Terms of Reference requirements; and agreed formats from the Inception Report.

*Stakeholder Feedback Integration*: Systematic processes for collecting, documenting, and addressing stakeholder feedback ensure materials reflect practical needs. All feedback will be logged in a response matrix documenting how each comment was addressed or explaining any deviation.

**Key Performance Indicators**

*Deliverable Quality*:
- 100% of deliverables submitted on or before agreed deadlines
- Zero resubmissions required due to non-compliance with agreed formats
- All World Bank review comments addressed within 10 working days of receipt

*Stakeholder Engagement*:
- Minimum 20 PIU representatives consulted during inception phase
- Validation workshop participation from all three target sectors
- Average training participant satisfaction rating of 4.0/5.0 or higher

*Training Effectiveness*:
- Minimum 50 PIU personnel trained across all Delhi and regional sessions
- Pre/post training assessment showing minimum 30% improvement in H&S knowledge
- SAR Focal Points demonstrate competency in training delivery during ToT workshop

*Material Accessibility*:
- Pictorial guides tested and validated as comprehensible by workers
- Materials formatted for both digital and print distribution
- Specifications compatible with existing PIU bidding document systems

**Monitoring and Reporting**

*Progress Monitoring*: Weekly internal team meetings track progress against work plan milestones. Monthly progress reports to the World Bank document activities completed, issues encountered, and upcoming milestones.

*Risk Monitoring*: Identified risks are tracked in a risk register updated monthly with status, probability/impact assessment, and mitigation progress. New risks identified during implementation are added and communicated to the World Bank.

*Deliverable Tracking*: A deliverable tracker monitors status of all nine deliverables from drafting through review and finalization. This ensures timely submission and systematic incorporation of feedback.

**Communication Protocols**

*World Bank Coordination*: Primary communication through the designated Task Team Lead with regular update meetings (suggested monthly or as agreed). Draft deliverables submitted via email with clear version numbering. Feedback tracked in shared review matrices.

*Team Coordination*: Team Leader maintains coordination among all experts. Weekly team calls during intensive work periods; bi-weekly during other periods. Shared document management system ensures version control and collaboration.

*Training Coordination*: Training scheduling coordinated through World Bank India Country Office for PIU locations. SAR coordination for Train the Trainer workshop through designated SAR focal point. Advance logistics confirmation minimum two weeks before each training event."""
    }

    return methodology


def main():
    """Genera el documento de metodología"""
    print("Generating India H&S Platform Phase 2 Methodology...")

    methodology = generate_india_hs_methodology()
    lang_config = get_language_config('en')

    output_path = "India_HS_Phase2_Methodology.docx"
    create_word_document(methodology, output_path, lang_config)

    print(f"\nDocument generated: {output_path}")
    print(f"Phases: {len(methodology['phases'])}")
    print(f"Principles: {len(methodology['principles'])}")

    # Summary of tasks
    total_tasks = sum(len(phase.get('tasks', [])) for phase in methodology['phases'])
    total_deliverables = sum(len(phase.get('deliverables', [])) for phase in methodology['phases'])
    print(f"Total tasks: {total_tasks}")
    print(f"Total deliverables: {total_deliverables}")


if __name__ == '__main__':
    main()
