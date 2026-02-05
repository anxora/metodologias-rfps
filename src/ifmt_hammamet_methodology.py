#!/usr/bin/env python3
"""
Methodology for UNIDO Project 240132 - Tunisie Professionnelle
Assessment of IFMT Hammamet - Conversion to Afro-Mediterranean Tourism Training Centre

UNIDO SAP Project ID: 240132
UNIDO RFQ No. 7000008282
Duration: 8 weeks
Language: English
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from document_writer import create_word_document
from translations import get_language_config


def get_ifmt_methodology():
    """
    Returns the complete methodology for:
    "Diagnostic and Roadmap for the Conversion of the Institut de Formation
    dans les Métiers de Tourisme de Hammamet (IFMTH) into an Afro-Mediterranean
    Centre for Training in Tourism Professions"

    UNIDO Project 240132 - Tunisie Professionnelle
    Funded by: Italian Agency for Development Cooperation (AICS)
    Duration: 8 weeks after contract signature
    """

    return {
        "introduction": """The team at Aninver Partners presents this comprehensive methodology for the delivery of consultancy services related to the **strategic diagnostic and roadmap for the transformation of the Institut de Formation dans les Métiers du Tourisme de Hammamet (IFMTH) into an Afro-Mediterranean Centre for Training in Tourism Professions**. Our approach is designed to provide UNIDO and its national partners with an evidence-based, participatory and actionable transformation strategy that positions the IFMTH as a **regional hub of excellence** in tourism vocational training. The consultants will employ an integrated methodology combining **institutional and strategic analysis**, pedagogical diagnostic, **international benchmarking**, governance reform design, and economic sustainability modelling. Our strategy ensures alignment with the broader objectives of the Tunisie Professionnelle project, funded by the **Italian Agency for Development Cooperation (AICS)**, which aims to strengthen the employability of young Tunisians through a revitalised vocational training system, with particular emphasis on **inclusive access for youth and women**, market-relevant curricula, and innovative pedagogical approaches including digital learning and dual training.""",

        "context": """**Understanding the Project Context**

The **Tunisie Professionnelle** project (UNIDO SAP ID 240132), funded by the Italian Agency for Development Cooperation (AICS), represents a strategic three-year intervention to strengthen the employability of young Tunisians by revitalising the national vocational training system. The project pursues a systemic transformation across two key outcomes: reinforcing the capacity of Tunisia's vocational training system to respond to labour market needs and youth aspirations, and improving training, reception and support mechanisms to foster the professional development and integration of young people, particularly women and vulnerable populations.

**The Tourism Training Opportunity**

Tunisia's tourism sector remains a cornerstone of the national economy, contributing significantly to GDP and employment. However, the sector faces critical challenges including the need to diversify beyond mass beach tourism, embrace sustainable and experiential tourism models, and upgrade the skills of its workforce to meet evolving international standards. The **IFMT Hammamet**, strategically located in one of Tunisia's premier tourism destinations, possesses significant untapped potential to serve as a **regional centre of excellence** for tourism vocational training. Its transformation into an Afro-Mediterranean Centre represents an opportunity to leverage Tunisia's geographic position, institutional expertise, and cultural assets to establish a hub that serves not only national needs but also regional demand across Africa and the Mediterranean basin.

**Institutional and Strategic Framework**

The intervention sits within a complex institutional landscape involving key actors of Tunisia's vocational training system, including the **AFMT (Agence de Formation dans les Métiers du Tourisme)**, the **ATFP**, **CENAFFIF**, professional federations, and the Ministry of Tourism. The project's four complementary outputs provide the framework for this mission: rehabilitation and modernisation of training structures (Output 1), introduction of innovative training mechanisms including dual training and digital tools (Output 2), strengthening the attractiveness and quality of centre services with attention to young women and disadvantaged territories (Output 3), and establishing structured public-private dialogue platforms for sustainability and scaling (Output 4).

**Regional and International Positioning**

The vision of transforming IFMTH into an Afro-Mediterranean Centre responds to growing demand for quality tourism training across the African continent and the Mediterranean region. South-South and triangular cooperation frameworks provide opportunities for student and trainer mobility, co-diplomation with recognised institutions in Africa and Europe, and regional certification programmes. Tunisia's established reputation in tourism, its proximity to both European and African markets, and its existing institutional infrastructure position the country as a potential **regional leader** in tourism vocational training, provided the necessary strategic, pedagogical, and governance reforms are implemented.""",

        "principles": [
            {
                "name": "Systemic and Strategic Approach",
                "description": "The consultants will adopt a holistic, systems-thinking perspective that addresses the interconnected dimensions of institutional transformation: strategic positioning, pedagogical innovation, governance reform, and economic sustainability. Rather than treating these as isolated components, our methodology ensures that recommendations across all domains are coherent, mutually reinforcing, and aligned with the overarching vision of the Afro-Mediterranean Centre."
            },
            {
                "name": "Participatory and Inclusive Process",
                "description": "All phases of the mission will be grounded in genuine stakeholder engagement, ensuring that the transformation roadmap reflects the perspectives and needs of all relevant actors: institutional leaders, trainers, students, industry professionals, public-private partners, and international cooperation stakeholders. We will pay particular attention to ensuring the voices of young women and vulnerable populations are heard in shaping the Centre's future direction."
            },
            {
                "name": "Evidence-Based Analysis",
                "description": "Our diagnostic and strategic recommendations will be anchored in rigorous data collection and analysis, including quantitative assessment of training programmes and labour market data, qualitative stakeholder interviews, institutional capacity evaluation, and targeted international benchmarking. This ensures that the transformation roadmap is grounded in empirical evidence rather than assumptions, enhancing its credibility and implementability."
            },
            {
                "name": "Innovation and Sustainability",
                "description": "The consultants will prioritise innovative and sustainable solutions across all dimensions of the transformation. This includes pedagogical innovations such as modularisation, active pedagogy, digital learning, and learning hotels, as well as governance innovations and sustainable economic models that diversify revenue sources and reduce dependency on public funding. All proposals will consider long-term viability and scalability."
            },
            {
                "name": "Regional Relevance and Cooperation",
                "description": "Given the ambition to establish an Afro-Mediterranean hub, our analysis and recommendations will consistently incorporate a regional perspective. We will assess opportunities for South-South and triangular cooperation, identify potential partner institutions across Africa and Europe, and propose mechanisms for student and trainer mobility, co-diplomation, and regional certification that position the Centre as a genuine regional reference."
            },
            {
                "name": "Sustainable Tourism Integration",
                "description": "In alignment with global trends and the TOR requirements, our approach will embed sustainable and responsible tourism principles throughout the transformation strategy. This includes mainstreaming environmental sustainability, ecotourism, natural and cultural resource preservation, waste management, energy efficiency, and short supply chains into curricula, institutional practices, and the Centre's strategic positioning."
            }
        ],

        "phases": [
            {
                "title": "Phase 1: Inception and Institutional Framing",
                "description": """The inception phase establishes the methodological foundation and institutional alignment necessary for the successful conduct of the diagnostic mission. The consultants will organise a **kick-off meeting with UNIDO and national partners** to frame the mission scope, confirm the work plan, agree on coordination modalities, and identify key stakeholders and documentation requirements. Simultaneously, the team will conduct comprehensive **documentary analysis and institutional framing**, reviewing existing strategic documents, training programme descriptions, institutional reports, labour market studies, and relevant policy frameworks governing Tunisia's vocational training system and the tourism sector. This phase ensures that the subsequent field work and diagnostic activities are built on a solid understanding of the institutional context, existing reform initiatives, and the specific positioning of IFMT Hammamet within the broader training ecosystem.""",
                "start_week": 1,
                "end_week": 2,
                "tasks": [
                    {
                        "code": "1A",
                        "title": "Kick-off Meeting and Mission Framing",
                        "description": """The mission begins with a structured kick-off session with UNIDO project management and national counterparts. Beyond the standard alignment on work plan and logistics, this meeting serves a more strategic purpose: it is the team's first opportunity to read the institutional landscape, understand unspoken expectations, and identify where political sensitivities may shape the diagnostic process. Who are the champions of this transformation? Where might resistance emerge? What previous reform attempts have shaped current attitudes? These are the questions that will guide not just the interview programme, but the tone and framing of the entire mission. The session will also confirm access to institutional documentation, agree on communication channels with UNIDO, and finalise the calendar of field visits to IFMT Hammamet and partner institutions across the vocational training ecosystem.""",
                        "items": [
                            "Facilitate kick-off meeting with UNIDO and national partners, capturing both formal requirements and informal institutional dynamics",
                            "Present and validate the detailed work plan, adapting as needed based on stakeholder input",
                            "Map the institutional landscape: identify champions, potential resistance, and key decision-making nodes",
                            "Confirm logistics and access arrangements for field visits to IFMT Hammamet"
                        ],
                        "start_week": 1,
                        "end_week": 1,
                        "deliverable_week": 1,
                        "deliverable_code": "E1",
                        "event_week": 1,
                        "event_code": "E1"
                    },
                    {
                        "code": "1B",
                        "title": "Documentary Analysis and Institutional Framing",
                        "description": """Before setting foot in Hammamet, the team needs to understand what has already been written, attempted, and debated. This desk phase involves a deep dive into IFMT Hammamet's institutional DNA: its founding mandate, the evolution of its training offer (CC, CAP, BTP, BTS, continuing education), performance data, staffing profiles, and any strategic planning documents that reveal how the institution sees itself. Equally important is the broader policy context, namely the orientations of AFMT, ATFP, CENAFFIF, and the Ministry of Tourism, which define the room for manoeuvre available for a transformation of this ambition. The team will also begin assembling regional labour market intelligence for the tourism sector at the national, African, and Mediterranean levels, as this data will anchor the relevance of any proposed new training tracks or pedagogical innovations. The phase concludes with a preliminary analytical framework that structures the diagnostic around six key dimensions: institutional positioning, pedagogical capacity, infrastructure and equipment, human resources, governance, and financial sustainability. This framework directly informs the design of interview guides and field visit protocols for Phase 2.""",
                        "start_week": 1,
                        "end_week": 2
                    }
                ],
                "deliverables": []
            },
            {
                "title": "Phase 2: Field Assessment and Comprehensive Diagnostic",
                "description": """This phase constitutes the core analytical effort of the mission, combining **institutional interviews, field visits, and in-depth diagnostic analysis** across all dimensions of the IFMT Hammamet transformation. The consultants will conduct extensive consultations with institutional stakeholders, industry professionals, trainers, students, and cooperation partners, complemented by on-site assessment of facilities, equipment, and pedagogical practices at IFMT Hammamet. The field assessment will be structured around the four analytical pillars defined in the TOR: strategic and institutional analysis, training offer and pedagogical capacity diagnostic, governance assessment, and economic model evaluation. The team will also conduct a **targeted international benchmark** of comparable tourism training institutions in Africa, the Mediterranean, and Asia to identify best practices and transformation models. All findings will be synthesised into the **comprehensive diagnostic report**, including a SWOT analysis and transformation scenarios.""",
                "start_week": 2,
                "end_week": 5,
                "tasks": [
                    {
                        "code": "2A",
                        "title": "Institutional Interviews and Stakeholder Consultations",
                        "description": """A diagnostic of this nature lives or dies by the quality of its stakeholder engagement. The consultants will conduct a carefully sequenced programme of interviews, beginning with senior institutional actors (AFMT, ATFP, CENAFFIF, Ministry of Tourism) to understand the strategic ceiling and floor for the proposed transformation, before moving to IFMT Hammamet itself, where conversations with management, trainers, administrative staff, and students will reveal the day-to-day realities that no official report can capture. A third layer of consultations will engage the demand side: hotel groups, professional federations, tourism industry associations, and employers who ultimately absorb the graduates this institution produces. Each conversation follows a tailored guide developed during Phase 1, but the team will remain alert to the unexpected, as the most valuable diagnostic insights often surface outside the prepared questions. We will ensure that women trainers and students have dedicated space to share their perspectives, and that voices from across the tourism value chain are represented, not just those closest to institutional power.""",
                        "start_week": 2,
                        "end_week": 4
                    },
                    {
                        "code": "2B",
                        "title": "On-site Assessment and Pedagogical Diagnostic",
                        "description": """The on-site visits to IFMT Hammamet represent the empirical backbone of this mission. The team will assess the full physical and pedagogical reality of the institution: classrooms, workshops, kitchens, accommodation facilities, laboratories, digital infrastructure, and the overall learning environment. But the physical assessment is only one layer. The deeper question is pedagogical: are the current training programmes (CC, CAP, BTP, BTS, and continuing education) actually producing the competencies that the evolving tourism sector demands? The team will evaluate this through direct observation of teaching sessions, review of curricula against industry benchmarks, and structured discussions with trainers about their methods, constraints, and aspirations.

The diagnostic will specifically assess the institution's readiness for a range of pedagogical innovations outlined in the TOR, namely modularisation, competency-based approaches, active pedagogy, soft skills development, project-based learning, and the learning hotel concept that bridges classroom instruction with real hospitality operations. The team will also map the digital learning infrastructure and evaluate the realistic potential for hybrid and online training delivery, distinguishing between what is technically possible and what is pedagogically meaningful given the current trainer capacity and student profile.""",
                        "start_week": 3,
                        "end_week": 4
                    },
                    {
                        "code": "2C",
                        "title": "International Benchmarking and SWOT Analysis",
                        "description": """Transformation does not happen in a vacuum. To define a credible vision for the Afro-Mediterranean Centre, the team needs to understand what similar ambitions have looked like elsewhere and what lessons they hold for Hammamet. The consultants will conduct a rapid but targeted benchmark of tourism training institutions that have undergone comparable transformations in Africa, the Mediterranean, and Asia, focusing on four dimensions: how they repositioned themselves strategically, what pedagogical innovations proved most impactful, how they structured governance for agility, and what economic models proved sustainable beyond initial donor investment.

This is not about copying models; it is about understanding what is transferable and what requires local adaptation. The benchmark will pay particular attention to institutions that have successfully positioned themselves as regional hubs, since the cooperation and mobility dimension is perhaps the most distinctive, and most ambitious, element of the IFMTH vision. Drawing together the documentary analysis, field assessment, stakeholder consultations, and international benchmark, the team will construct a comprehensive SWOT analysis that honestly confronts the institution's strengths and weaknesses alongside the opportunities and risks of transformation. This synthesis, along with preliminary transformation scenarios, will form the foundation of the detailed diagnostic report due at the end of Week 5.""",
                        "items": [
                            "Benchmark 4-6 comparable tourism training institutions across Africa, Mediterranean and Asia",
                            "Construct comprehensive SWOT analysis integrating all diagnostic findings",
                            "Develop transformation scenarios with realistic assessment of feasibility, investment needs, and expected impact"
                        ],
                        "start_week": 3,
                        "end_week": 5,
                        "deliverable_week": 5,
                        "deliverable_code": "D1"
                    }
                ],
                "deliverables": [
                    {"code": "D1", "name": "Detailed Diagnostic Report (institutional, organisational, pedagogical and operational assessment with SWOT analysis and benchmarking)"}
                ]
            },
            {
                "title": "Phase 3: Strategic Vision, Roadmap and Transformation Plans",
                "description": """Building on the diagnostic findings, this phase focuses on **elaborating the strategic vision, transformation roadmap, and detailed operational plans** for the conversion of IFMT Hammamet into the Afro-Mediterranean Centre. The consultants will define the Centre's strategic positioning and transformation axes structured around three pillars: **regional centre of pedagogical excellence** (specialised programmes, continuing education, trainer development), **Afro-Mediterranean cooperation and partnership hub** (South-South cooperation, co-diplomation, mobility programmes), and **pedagogical and digital innovation centre** (digital learning, innovation labs, digital content development). The team will also develop the **programme modernisation plan**, the **governance model**, and the **economic sustainability model** with partnership proposals, ensuring all components are coherent and mutually reinforcing.""",
                "start_week": 5,
                "end_week": 7,
                "tasks": [
                    {
                        "code": "3A",
                        "title": "Strategic Vision and Transformation Axes Definition",
                        "description": """With the diagnostic complete, the team shifts from analysis to design. The central task here is to articulate a strategic vision for the Afro-Mediterranean Centre that is simultaneously ambitious enough to justify the transformation and realistic enough to be credible with the institutional actors who must implement it.

The vision will be structured around the three axes defined in the TOR, but our treatment of each will be shaped by what the diagnostic has revealed. **Axis 1 (Regional Centre of Pedagogical Excellence)** will propose concrete new training tracks, for instance in sustainable tourism, gastronomy, experience management, cultural animation, and digital hospitality skills, alongside a revamped continuing education offer for working professionals and a dedicated trainer development programme. **Axis 2 (Afro-Mediterranean Cooperation Hub)** will move beyond generic aspirations to identify specific partnership opportunities: which African and European institutions are natural partners for co-diplomation? Where does demand for student and trainer mobility actually exist? What regional certification frameworks could the Centre anchor? **Axis 3 (Pedagogical and Digital Innovation)** will translate the pedagogical diagnostic into a concrete innovation roadmap, covering the digital learning pole, innovation laboratories, and a strategy for developing and curating digital educational content.

Critically, the team will define priority orientations at three time horizons, identifying what can be launched within the first year, what requires medium-term investment over two to three years, and what represents the long-term institutional aspiration.""",
                        "start_week": 5,
                        "end_week": 6,
                        "deliverable_week": 6,
                        "deliverable_code": "D2"
                    },
                    {
                        "code": "3B",
                        "title": "Strategic Transformation Roadmap Elaboration",
                        "description": """A vision without an operational plan is an aspiration. The roadmap translates the strategic axes into a sequenced, resourced, and accountable action plan. The team's approach to roadmap design distinguishes deliberately between **quick wins** that can generate visible momentum in the first months and signal institutional seriousness, and **deeper structural reforms** in governance, partnerships, and curricula that require sustained commitment and investment over several years.

Each action in the roadmap will be assigned to a responsible institutional actor, tagged with clear milestones and success indicators, and positioned within a realistic implementation timeline. The roadmap will also make explicit the critical dependencies between workstreams: for example, certain pedagogical innovations cannot be deployed until trainer capacity is developed, and the cooperation hub cannot function without the governance framework to manage international partnerships. Risk mitigation is embedded within the roadmap itself rather than treated as a separate exercise, ensuring that the plan is robust to the most likely implementation challenges.""",
                        "start_week": 6,
                        "end_week": 7,
                        "deliverable_week": 7,
                        "deliverable_code": "D3"
                    },
                    {
                        "code": "3C",
                        "title": "Modernisation Plan, Governance Model and Economic Model",
                        "description": """This task produces three interconnected deliverables that together define how the Centre will actually function.

The **programme and equipment modernisation plan** addresses the tangible dimension: what needs to change in the curricula, what new training tracks and modules should be introduced, what innovative pedagogical approaches should be adopted, and what this implies for equipment, workshops, laboratories, digital technologies, and physical infrastructure. The plan will be specific enough to serve as a basis for investment planning, with cost indications and prioritisation criteria.

The **governance model** tackles the institutional architecture. The current governance structure of IFMT Hammamet was designed for a national training centre, not for an Afro-Mediterranean hub managing international partnerships, multi-stakeholder coordination, and diversified revenue streams. The team will propose a modern, agile governance framework, potentially including a strategic council with external representation, an academic committee driving pedagogical quality, structured public-private partnership mechanisms, and integration into relevant professional networks. Roles, responsibilities, and coordination mechanisms will be defined with sufficient precision to guide implementation.

The **economic model** confronts what is perhaps the most critical question for sustainability: how will this Centre fund itself? The team will propose a diversified financing strategy combining own-resource generation through fee-based services and programmes, international project funding, partnerships with hotel groups and tourism operators, and continued institutional support. Each revenue stream will be assessed for its realistic potential and the conditions required to activate it, resulting in a financial projection model that national partners can use for planning and fundraising.""",
                        "start_week": 6,
                        "end_week": 7,
                        "deliverable_week": 7,
                        "deliverable_code": "D4"
                    }
                ],
                "deliverables": [
                    {"code": "D2", "name": "Strategic Transformation Axes and Priority Orientations"},
                    {"code": "D3", "name": "Strategic Transformation Roadmap (operational action plan with timeline, responsibilities and indicators)"},
                    {"code": "D4", "name": "Programme Modernisation Plan, Governance Model and Economic Model with Partnership Proposals"}
                ]
            },
            {
                "title": "Phase 4: Validation, Finalisation and Handover",
                "description": """The final phase ensures the quality, ownership, and institutional validation of all deliverables through a structured **validation workshop** and systematic incorporation of stakeholder feedback. The consultants will first transmit **draft versions of all deliverables** to UNIDO for initial review, then organise a multi-stakeholder restitution workshop before finalising all outputs and preparing the **executive summary note** for institutional dissemination. This phase is as much about building ownership as it is about quality control: a transformation roadmap that stakeholders have actively shaped and validated carries far more institutional weight than one handed down by external consultants.""",
                "start_week": 7,
                "end_week": 8,
                "tasks": [
                    {
                        "code": "4A",
                        "title": "Draft Deliverables Transmission and Validation Workshop",
                        "description": """Week 7 is the most intensive week of the mission. The team will first compile and transmit draft versions of all deliverables to UNIDO, giving the project team a window for initial review before the validation workshop. The **validation and restitution workshop** itself brings together the full spectrum of institutional stakeholders: UNIDO, AFMT, ATFP, CENAFFIF, professional federations, and other partners who have been engaged throughout the diagnostic process. The workshop is not a presentation; it is a structured deliberation. Each major component of the work, from diagnostic findings through strategic axes to governance and economic models, will be presented, discussed, challenged, and refined through facilitated working sessions. The team will use interactive methods that encourage genuine engagement rather than passive listening, because the quality of the feedback received here directly determines the quality and institutional acceptability of the final deliverables. All feedback will be systematically documented and tracked through to incorporation in the final versions.""",
                        "start_week": 7,
                        "end_week": 7,
                        "deliverable_week": 7,
                        "deliverable_code": "E2",
                        "event_week": 7,
                        "event_code": "E2"
                    },
                    {
                        "code": "4B",
                        "title": "Final Deliverables and Executive Summary",
                        "description": """The final week is dedicated to incorporating workshop feedback, conducting a final quality review across all seven deliverables, and producing the **executive summary note**: a concise 4-6 page document that distils the essential findings, strategic vision, transformation axes, and priority recommendations into a format designed for decision-makers and institutional dissemination. This note must stand alone, meaning it should communicate the core transformation narrative to a reader who will never open the detailed reports. All final deliverables will be transmitted in both Word and PDF formats, accompanied by a formal handover session with UNIDO and national partners that marks the transition from diagnostic to implementation.""",
                        "start_week": 8,
                        "end_week": 8,
                        "deliverable_week": 8,
                        "deliverable_code": "D5"
                    }
                ],
                "deliverables": [
                    {"code": "D5", "name": "Executive Summary Note (4-6 pages) with key findings, strategic vision and priority recommendations"},
                    {"code": "D6", "name": "Final versions of all deliverables (Diagnostic Report, Strategic Axes, Roadmap, Modernisation Plan, Governance Model, Economic Model)"}
                ]
            }
        ],

        "risks": """**Risk Management Framework**

The consultants have identified the key risks that could affect mission implementation and developed corresponding mitigation strategies to ensure delivery within the 8-week timeframe.

**Tight Timeline and Scope Complexity**
Eight weeks is a demanding timeline for a mission that spans institutional diagnosis, pedagogical assessment, governance design, economic modelling, and strategic planning. The risk of superficial analysis is real. We mitigate this through intensive pre-mission desk research, parallel workstreams across our expert team (tourism specialist, pedagogical engineer, governance expert), and a deliberate prioritisation of depth over breadth: the diagnostic will focus analytical firepower on the dimensions that matter most for the transformation, rather than attempting encyclopaedic coverage of every operational detail.

**Stakeholder Availability and Engagement**
Securing time with senior officials from AFMT, ATFP, CENAFFIF, the Ministry of Tourism, and industry leaders within a compressed timeline is inherently challenging. The inception phase will be used to confirm interview schedules early, leveraging UNIDO's institutional networks to facilitate access. Where in-person meetings prove impossible within the required timeframe, the team will propose virtual alternatives, while recognising that some conversations require face-to-face engagement.

**Institutional Sensitivity and Change Resistance**
Any diagnostic that implies transformation carries an implicit critique of the status quo, which can generate defensiveness among staff and institutional actors. Our approach deliberately positions stakeholders as co-designers of the transformation rather than subjects of external assessment. We will frame the narrative around opportunity and ambition, not deficiency, and ensure transparent communication about the mission's objectives at every stage.

**Data Availability and Quality**
Comprehensive institutional data on training outcomes, graduate employment rates, and financial performance may be incomplete or inconsistent. Rather than treating this as an obstacle, the team will triangulate across multiple sources, use qualitative methods to fill quantitative gaps, and be transparent about data limitations in the analysis. The international benchmark provides an additional reference layer where local data is thin.

**Political and Institutional Context**
Institutional leadership changes, shifting policy priorities, or funding uncertainties could affect the implementability of recommendations. The roadmap will therefore include phased implementation options that can adapt to changing circumstances, and the economic model will be stress-tested against different funding scenarios rather than built on a single optimistic assumption.

**Coherence Across Multiple Deliverables**
Seven interrelated deliverables produced in eight weeks must be internally consistent. The lead consultant maintains cross-cutting oversight and a unified analytical framework throughout, with regular internal coordination to ensure that what the governance model proposes is compatible with what the economic model assumes, and what the modernisation plan requires.""",

        "quality": """**Quality Assurance Framework**

The consultants will implement a rigorous quality assurance system ensuring all deliverables meet the highest professional standards within the 8-week timeline.

**Internal Review and Cross-Checking**
Every deliverable undergoes internal peer review before submission. Given the interconnected nature of the seven outputs, the lead consultant conducts a specific coherence review to verify that assumptions, recommendations, and timelines are consistent across the diagnostic report, strategic axes, roadmap, modernisation plan, governance model, and economic model.

**Stakeholder Validation as Quality Mechanism**
The validation workshop in Week 7 is not a formality. It is the most important quality assurance mechanism in the entire mission. When twenty institutional stakeholders challenge a finding, question an assumption, or flag a practical constraint the team has not considered, the resulting corrections produce a fundamentally better product than any amount of internal review alone. The team will systematically track all feedback received and document how it has been addressed in final deliverables.

**Timeline Discipline**
Internal deadlines are set 48 hours ahead of contractual deadlines to create a quality buffer. Weekly progress updates to UNIDO ensure early visibility of any risks to the delivery schedule. If a constraint emerges, we raise it immediately rather than allowing it to cascade into downstream deliverables.

**Compliance Tracking**
A simple but rigorous compliance matrix tracks every specific requirement in the TOR against the deliverable where it is addressed. This ensures nothing falls through the cracks: all four analytical dimensions (strategic, pedagogical, governance, economic), the three transformation axes, the sustainability requirements, and every deliverable component specified in the TOR are explicitly covered."""
    }


def main():
    lang_config = get_language_config('en')
    methodology = get_ifmt_methodology()

    # Ensure output directory exists
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, 'IFMT_Hammamet_Methodology_EN.docx')
    create_word_document(methodology, output_path, lang_config)
    print(f"Document generated: {output_path}")


if __name__ == "__main__":
    main()
