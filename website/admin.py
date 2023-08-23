from django.contrib import admin

from website.models import Slider, Info, Service, Video, Project, Client, PreLoader, LatestNews, About, NewsLetter, \
    ContactUs, Contact, Testimonial, TeamMember, Skill, TopClients, ComingSoon, Subscribe, Comment, \
    ErrorEmail, ProjectItem, Gallery

# Register your models here.
admin.site.register(PreLoader)
admin.site.register(Slider)
admin.site.register(Info)
admin.site.register(Service)
admin.site.register(Video)
admin.site.register(Project)
admin.site.register(Client)
admin.site.register(LatestNews)
admin.site.register(About)
admin.site.register(NewsLetter)
admin.site.register(Contact)
admin.site.register(ContactUs)
admin.site.register(Testimonial)
admin.site.register(TeamMember)
admin.site.register(Skill)
admin.site.register(TopClients)
admin.site.register(ComingSoon)
admin.site.register(Subscribe)
admin.site.register(Comment)
admin.site.register(ProjectItem)
admin.site.register(ErrorEmail)
admin.site.register(Gallery)
