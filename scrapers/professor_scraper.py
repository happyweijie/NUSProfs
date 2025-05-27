import requests
import re
import json5
import os
import django
from helpers import reformat_name

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NUSProfs.settings")  # replace with your project name
django.setup()

from professors.models import Professor, Department, Faculty

DEPTS = {
    "Computer Science": "https://www.comp.nus.edu.sg/cs/people/",
    "Information Systems and Analytics": "https://www.comp.nus.edu.sg/disa/people/",
}

def main():
    soc, created = Faculty.objects.get_or_create(name="Computing")

    # Step 1: Fetch the HTML
    for dept_name, url in DEPTS.items():
        response = requests.get(url)
        html = response.text

        # Step 2: Extract the $scope.allStaffs JS variable
        pattern = r"\$scope\.allStaffs\s*=\s*(\[[\s\S]*?\]);"
        match = re.search(pattern, html)

        if not match:
            raise ValueError(f"Could not find staff data for {dept_name}.")

        staff_list = json5.loads(match.group(1))

        # Step 3: Get the department instance
        department = Department.objects.get(name=dept_name)
        if not department:
            department = Department(name=dept_name, faculty=soc)
            department.save()

        # Step 4: Create Professor objects
        for staff in staff_list:
            name = reformat_name(staff.get("name"))
            title = staff.get("title")
            office = staff.get("officetel") if staff.get("officetel") else None
            phone = staff.get("tel") if staff.get("tel") else None

            # Check if professor already exists
            if Professor.objects.filter(name=name, department=department).exists():
                print(f"Skipped existing: {name}")
                continue

            prof = Professor(
                name=name,
                title=title,
                office=office,
                phone=phone,
                department=department
            )
            prof.save()
            print(f"Added: {prof}")



if __name__ == "__main__":
    main()
    print("All professors have been added successfully.")