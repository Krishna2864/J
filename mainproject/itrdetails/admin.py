from django.contrib import admin
from .models import *






admin.site.register(personal_info)
admin.site.register(itr_type)
admin.site.register(itrform)

admin.site.register(exempted_income)
admin.site.register(professional_income)


