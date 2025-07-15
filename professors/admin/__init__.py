# Import managers
from .faculty_admin import *
from .department_admin import *
from .module_admin import *
from .professor_admin import *  
from .semester_admin import *
from .teaches_admin import *

# Change site header and title
from django.contrib import admin

admin.site.site_header = "NUSProfs Admin"
admin.site.site_title = "NUSProfs Admin Portal"