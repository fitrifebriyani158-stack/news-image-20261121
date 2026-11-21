import os
import shutil
import sys

MAKEFUN_OUTPUT_DIR = os.environ.get('MAKEFUN_OUTPUT_DIR') or '/output'
if os.name == 'nt':
    sys.exit(os.system('copy /y %s %s' % (os.path.join(os.path.dirname(__file__), 'entry.png'), os.path.join(MAKEFUN_OUTPUT_DIR, 'entry.png'))))
else:
    os.makedirs(MAKEFUN_OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(os.path.join(os.path.dirname(__file__), 'entry.png'), os.path.join(MAKEFUN_OUTPUT_DIR, 'entry.png'))