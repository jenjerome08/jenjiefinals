from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Respondent)
admin.site.register(BinaryLogisticRegression)
admin.site.register(GeneralizedAnxietyDisorder)
admin.site.register(Assessment)
admin.site.register(Symptoms)