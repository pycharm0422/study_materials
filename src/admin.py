from django.contrib import admin
from .models import SubName, Branch, Note, Tutorial

# admin.site.register()
admin.site.register(SubName)
admin.site.register(Branch)
admin.site.register(Note)
# admin.site.register(PreviousYearQuestionPaper)
admin.site.register(Tutorial)