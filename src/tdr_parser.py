"""
Parser de Términos de Referencia (TdR/TOR)
Soporta PDF, DOCX y TXT
"""

from pathlib import Path
from PyPDF2 import PdfReader
from docx import Document


def parse_tdr(file_path: Path) -> str:
    """
    Extrae el contenido de un archivo TdR

    Args:
        file_path: Ruta al archivo TdR

    Returns:
        Contenido del TdR como texto
    """
    suffix = file_path.suffix.lower()

    if suffix == '.pdf':
        return _parse_pdf(file_path)
    elif suffix == '.docx':
        return _parse_docx(file_path)
    elif suffix == '.txt':
        return _parse_txt(file_path)
    else:
        raise ValueError(f"Formato no soportado: {suffix}. Use PDF, DOCX o TXT.")


def _parse_pdf(file_path: Path) -> str:
    """Extrae texto de un PDF"""
    reader = PdfReader(str(file_path))
    text_parts = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            text_parts.append(text)

    return "\n\n".join(text_parts)


def _parse_docx(file_path: Path) -> str:
    """Extrae texto de un DOCX"""
    doc = Document(str(file_path))
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return "\n\n".join(paragraphs)


def _parse_txt(file_path: Path) -> str:
    """Lee un archivo de texto"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
