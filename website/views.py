from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader

from website import forms
from website.models import Slider, Info, Service, Video, Project, Client, PreLoader, LatestNews, About, Contact, \
    Testimonial, TeamMember, Skill, TopClients, ComingSoon


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preLoader'] = PreLoader.objects.all()
        context['infos'] = Info.objects.last()
        context['sliders'] = Slider.objects.all()
        context['abouts'] = About.objects.last()
        context['services'] = Service.objects.filter(is_draft=False)
        context['videos'] = Video.objects.all()
        context['projects'] = Project.objects.all()
        context['clients'] = Client.objects.all()
        context['latestNews'] = LatestNews.objects.all()
        return context


class NewsLetterView(View):
    def post(self, request):
        form = forms.NewsLetterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Done.')
        else:
            messages.error(request, 'Invalid! Please try again. ')
        return redirect('/')

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preLoader'] = PreLoader.objects.all()
        context['infos'] = Info.objects.last()
        context['contacts'] = Contact.objects.last()
        context['services'] = Service.objects.all()
        context['abouts'] = About.objects.last()
        return context

class ContactUsView(View):
    def post(self, request):
        form = forms.ContactUsForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully.')
        else:
            messages.error(request, 'Invalid! Please try again. ')
        return redirect('/contact/')

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preLoader'] = PreLoader.objects.all()
        context['infos'] = Info.objects.last()
        context['abouts'] = About.objects.last()
        context['clients'] = Client.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['professional'] = TeamMember.objects.all()
        context['services'] = Service.objects.all()
        context['skills'] = Skill.objects.all()
        return context

class TeamMemberDetailView(View):
    def get(self, request, teamMember_id):
        teamMember = TeamMember.objects.get(id=teamMember_id)
        context = {
            'teamMember': teamMember,
            'infos': Info.objects.last(),
            'services': Service.objects.all(),
            'abouts': About.objects.last(),
            'professional': TeamMember.objects.all(),
            'skills': Skill.objects.all()
        }
        return render(request, 'team-details.html', context=context)

class ServiceView(TemplateView):
    template_name = 'service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preLoader'] = PreLoader.objects.all()
        context['infos'] = Info.objects.last()
        context['abouts'] = About.objects.last()
        context['services_sol'] = Service.objects.filter(is_solution=True)
        context['services_include'] = Service.objects.filter(is_include=True)
        context['testimonials'] = Testimonial.objects.all()
        return context
class ServiceDetailView(View):
    def get(self, request, service_id):
        service = Service.objects.get(id=service_id)
        context = {
            'service': service,
            'infos': Info.objects.last(),
            'services': Service.objects.all(),
            'abouts': About.objects.last()

        }
        return render(request, 'service-details.html', context=context)

class TestimonialView(TemplateView):
    template_name = 'testimonial.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preLoader'] = PreLoader.objects.all()
        context['infos'] = Info.objects.last()
        context['topClients'] = TopClients.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        return context

class TeamView(TemplateView):
    template_name = 'team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preLoader'] = PreLoader.objects.all()
        context['infos'] = Info.objects.last()
        context['topClients'] = TopClients.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['skills'] = Skill.objects.all()
        return context

class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preLoader'] = PreLoader.objects.all()
        context['infos'] = Info.objects.last()
        context['latestNews'] = LatestNews.objects.all()
        context['abouts'] = About.objects.last()
        return context

class ComingSoonView(TemplateView):
    template_name = 'coming-soon.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preLoader'] = PreLoader.objects.all()
        context['infos'] = Info.objects.last()
        context['comingsoon'] = ComingSoon.objects.last()
        return context

class SubscribeView(View):
    def post(self, request):
        form = forms.SubscribeForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscribe Done.')
        else:
            messages.error(request, 'Invalid! Please try again. ')
        return redirect('/coming-soon/')
