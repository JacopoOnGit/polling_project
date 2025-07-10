from django.contrib import admin
from .models import Poll, Vote, Choice

admin.site.register(Poll)
admin.site.register(Vote)
admin.site.register(Choice)