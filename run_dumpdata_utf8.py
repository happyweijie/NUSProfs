# run_dumpdata_utf8.py

import sys
import io
from django.core.management import call_command

with open("data/seed_data.json", "w", encoding="utf-8") as f:
    sys.stdout = io.TextIOWrapper(f.buffer, encoding='utf-8')
    call_command('dumpdata', 'professors.Faculty', 'professors.Department', 'professors.Professor', 'professors.Module', 'professors.Teaches', indent=2)
    sys.stdout = sys.__stdout__
