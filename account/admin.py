from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from account.models import Account
from socials.models import Social
from jobs.models import Job
from educations.models import Education


class AccountInline(admin.StackedInline):
    """Stacked account details in user model
    """

    model = Account


class SocialInline(admin.StackedInline):
    """Stacked social resources details in user model
    """

    model = Social
    extra = 1


class JobInline(admin.StackedInline):
    """Stacked jobs details in user model
    """

    model = Job
    extra = 1


class EducationInline(admin.StackedInline):
    """Stacked educations details in user model
    """

    model = Education
    extra = 1


class UserAdmin(BaseUserAdmin):
    """User admin section with account details
    """

    inlines = (AccountInline, SocialInline, JobInline, EducationInline)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
