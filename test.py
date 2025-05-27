# run_dumpdata_utf8.py


import os
import django
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nusprofs.settings")  # replace if needed
django.setup()

with open("data/seed_data.json", "w", encoding="utf-8") as f:
    call_command(
        'dumpdata',
        'professors.Faculty',
        'professors.Department',
        'professors.Professor',
        'professors.Module',
        'professors.Teaches',
        indent=2,
        stdout=f
    )
