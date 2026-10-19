import importlib.util
import shutil
import sys
from pathlib import Path

WORK = Path(__file__).resolve().parent
SKILL = Path('C:/Users/ADMIN/.codex/plugins/cache/openai-primary-runtime/documents/26.1011.11113/skills/documents')
OUTPUT = WORK.parent / 'SE100_BaoCaoTienDo_Dot1_Scope_SRS.docx'
RENDER = WORK / 'render_final'
PDF = RENDER / 'SE100_BaoCaoTienDo_Dot1_Scope_SRS.pdf'
spec = importlib.util.spec_from_file_location('docx_renderer', SKILL / 'render_docx.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


def use_word_pdf(input_path, user_profile, convert_tmp_dir, stem, *, verbose=False):
    if not PDF.exists():
        raise FileNotFoundError(f'Word export not found: {PDF}')
    target = Path(convert_tmp_dir) / (stem + '.pdf')
    shutil.copyfile(PDF, target)
    return str(target), 'PDF exported by installed Microsoft Word because LibreOffice is unavailable.'


renderer.convert_to_pdf = use_word_pdf
sys.argv = ['render_docx.py', str(OUTPUT), '--output_dir', str(RENDER), '--emit_pdf', '--verbose']
renderer.main()
