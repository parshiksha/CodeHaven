from django.contrib import admin

# Register your models here.

from .models import users
from problems.models import ProblemInfo,SubjectInfo, TestCaseInfo, UserProblemDeatils


admin.site.register(users)
admin.site.register(ProblemInfo)
admin.site.register(SubjectInfo)
admin.site.register(TestCaseInfo)
admin.site.register(UserProblemDeatils)
