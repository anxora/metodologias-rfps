#!/usr/bin/env python3
"""
Metodologías RFPs - Generador de enfoques metodológicos para consultoría
"""

import click
from pathlib import Path
from dotenv import load_dotenv

from src.tdr_parser import parse_tdr
from src.methodology_generator import generate_methodology
from src.document_writer import create_word_document
from src.translations import get_language_config

load_dotenv()


@click.command()
@click.option('--tdr', required=True, type=click.Path(exists=True),
              help='Archivo de Términos de Referencia (PDF, DOCX, TXT)')
@click.option('--idioma', default='es', type=click.Choice(['es', 'en', 'fr', 'pt']),
              help='Idioma del documento de salida')
@click.option('--output', default='metodologia.docx',
              help='Nombre del archivo de salida')
def main(tdr: str, idioma: str, output: str):
    """
    Genera un documento Word con enfoque metodológico basado en TdR.
    """
    click.echo(f"Procesando TdR: {tdr}")

    # Configurar idioma
    lang_config = get_language_config(idioma)
    click.echo(f"Idioma seleccionado: {lang_config['name']}")

    # Parsear TdR
    click.echo("Analizando Términos de Referencia...")
    tdr_content = parse_tdr(Path(tdr))

    # Generar metodología con Claude
    click.echo("Generando enfoque metodológico...")
    methodology = generate_methodology(tdr_content, lang_config)

    # Crear documento Word
    click.echo(f"Creando documento: {output}")
    create_word_document(methodology, output, lang_config)

    click.echo(f"Documento generado exitosamente: {output}")


if __name__ == '__main__':
    main()
