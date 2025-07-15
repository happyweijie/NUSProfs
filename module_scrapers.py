import requests
from bs4 import BeautifulSoup
import os
import django
from helpers import reformat_name

# Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NUSProfs.settings")
django.setup()

from professors.models import Professor, Module, Teaches, Semester

URL = "https://web.archive.org/web/20240418052221/https://www.comp.nus.edu.sg/cug/soc-sched/"

ay = int(input("Enter academic year eg. 2024: ").strip())

SEMESTER_1, _ = Semester.objects.get_or_create(
    ay_start=int(ay),
    semester_number=1,
)
SEMESTER_2, _ = Semester.objects.get_or_create(
    ay_start=int(ay),
    semester_number=2,
)

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Get all table rows
rows = soup.select("table.newtab tbody tr")

for row in rows:
    cols = row.find_all("td")
    if len(cols) < 4:
        continue  # skip malformed rows

    # Extract module code and title
    code = cols[0].get_text(strip=True).upper()
    title_block = cols[1].get_text(separator="\n", strip=True)
    name = title_block.split("Units")[0].strip()

    # Create or get the Module
    module, created = Module.objects.get_or_create(module_code=code, defaults={"name": name})
    if module.name != name:
        module.name = name
        module.save()

    # Update module name if it changed
    if not created and module.name != name:
        module.name = name  
        module.save()

    # Process both semesters
    for i, semester_col in enumerate([cols[2], cols[3]]):
        semester = SEMESTER_1 if i == 0 else SEMESTER_2
        prof_links = semester_col.find_all("a")

        for a in prof_links:
            prof_name = reformat_name(a.get_text(strip=True))

            # Match or create professor by name
            prof = Professor.objects.filter_by(name_query=prof_name).first()
            if not prof:
                print(f"Skipping unregistered professor: {prof_name}")
                continue

            # Create the Teaches relationship if not already exists
            if not Teaches.objects.filter(prof=prof, module=module, semester=semester).exists():
                Teaches.objects.create(prof=prof, module=module, semester=semester)
                print(f"Linked {prof_name} → {code} ({semester})")