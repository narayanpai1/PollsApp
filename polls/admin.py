from django.contrib import admin
from .models import *


# register all the models to view and edit it through admin-page
admin.site.register(Question)
admin.site.register(Question_answer)
admin.site.register(Quiz)
