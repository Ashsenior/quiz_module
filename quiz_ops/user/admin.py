from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(UserQuizSummary)
class UserQuizSummary(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

@admin.register(UserQuizDetail)
class UserQuizDetail(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
