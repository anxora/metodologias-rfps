"""
Generador de documentos Word
"""

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE


def create_word_document(methodology: dict, output_path: str, lang_config: dict):
    """
    Crea un documento Word con el enfoque metodológico

    Args:
        methodology: Diccionario con las secciones de la metodología
        output_path: Ruta del archivo de salida
        lang_config: Configuración de idioma
    """
    doc = Document()
    sections = lang_config['sections']

    # Configurar estilos
    _setup_styles(doc)

    # Título principal
    title = doc.add_heading(sections['title'], level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Agregar línea separadora
    doc.add_paragraph("_" * 50)

    # Secciones del documento
    section_mapping = [
        ('context', sections['context']),
        ('approach', sections['approach']),
        ('workplan', sections['workplan']),
        ('team', sections['team']),
        ('risks', sections['risks']),
        ('quality', sections['quality']),
    ]

    for key, title_text in section_mapping:
        content = methodology.get(key, '')
        if content:
            _add_section(doc, title_text, content)

    # Guardar documento
    doc.save(output_path)


def _setup_styles(doc: Document):
    """Configura los estilos del documento"""
    styles = doc.styles

    # Estilo para el cuerpo del texto
    style = styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)

    # Configurar márgenes
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1.25)
        section.right_margin = Inches(1.25)


def _add_section(doc: Document, title: str, content: str):
    """Agrega una sección al documento"""
    # Título de sección
    doc.add_heading(title, level=1)

    # Contenido - dividir en párrafos
    paragraphs = content.split('\n\n')
    for para_text in paragraphs:
        if para_text.strip():
            # Detectar si es una lista
            lines = para_text.strip().split('\n')
            for line in lines:
                line = line.strip()
                if line.startswith('- ') or line.startswith('• '):
                    # Es un elemento de lista
                    p = doc.add_paragraph(line[2:], style='List Bullet')
                elif line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
                    # Es una lista numerada
                    p = doc.add_paragraph(line[3:].strip(), style='List Number')
                else:
                    # Párrafo normal
                    p = doc.add_paragraph(line)
                    p.paragraph_format.space_after = Pt(6)

    # Espacio después de la sección
    doc.add_paragraph()
