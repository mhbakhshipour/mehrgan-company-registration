from django.contrib import admin

from consultant.models import Consultant, Skill, ContactForm, SkilledConsultant

admin.site.register(Consultant)
admin.site.register(SkilledConsultant)
admin.site.register(Skill)
admin.site.register(ContactForm)
