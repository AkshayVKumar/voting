from django.contrib import admin
from voting.models import *
# Register your models here.
admin.site.register(Constituency)
admin.site.register(Candidate)
admin.site.register(Voter)