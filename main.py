#!/usr/bin/env python3
"""
Metodologías RFPs - Generador de enfoques metodológicos para consultoría
"""

import click
from pathlib import Path
from dotenv import load_dotenv

from src.tdr_parser import parse_tdr
from src.methodology_generator import generate_methodology, detect_methodology_type
from src.document_writer import create_word_document
from src.translations import get_language_config

load_dotenv()


@click.command()
@click.option('--tdr', required=True, type=click.Path(exists=True),
              help='Archivo de Términos de Referencia (PDF, DOCX, TXT)')
@click.option('--idioma', default='es', type=click.Choice(['es', 'en', 'fr', 'pt']),
              help='Idioma del documento de salida')
@click.option('--tipo', default='auto',
              type=click.Choice(['auto', 'general', 'feasibility', 'info_systems']),
              help='Tipo de metodología: auto (detectar), general, feasibility, info_systems')
@click.option('--output', default='metodologia.docx',
              help='Nombre del archivo de salida')
def main(tdr: str, idioma: str, tipo: str, output: str):
    """
    Genera un documento Word con enfoque metodológico basado en TdR.

    Tipos de metodología disponibles:

    \b
    - auto: Detecta automáticamente el tipo basado en el contenido del TdR
    - general: Metodología general para proyectos de estrategia, marketing, capacity building
    - feasibility: Estudios de factibilidad con análisis financiero y técnico
    - info_systems: Desarrollo de sistemas de información, websites, plataformas
    """
    click.echo(f"Procesando TdR: {tdr}")

    # Configurar idioma
    lang_config = get_language_config(idioma)
    click.echo(f"Idioma seleccionado: {lang_config['name']}")

    # Parsear TdR
    click.echo("Analizando Términos de Referencia...")
    tdr_content = parse_tdr(Path(tdr))

    # Detectar o usar tipo especificado
    if tipo == 'auto':
        methodology_type = detect_methodology_type(tdr_content)
        click.echo(f"Tipo de metodología detectado: {methodology_type}")
    else:
        methodology_type = tipo
        click.echo(f"Tipo de metodología seleccionado: {methodology_type}")

    # Generar metodología con Claude
    click.echo("Generando enfoque metodológico (esto puede tomar unos minutos)...")
    methodology = generate_methodology(tdr_content, lang_config, methodology_type)

    # Crear documento Word
    click.echo(f"Creando documento: {output}")
    create_word_document(methodology, output, lang_config)

    click.echo(f"\n✓ Documento generado exitosamente: {output}")
    click.echo(f"  Tipo de metodología: {methodology_type}")
    click.echo(f"  Idioma: {lang_config['name']}")


if __name__ == '__main__':
    main()
