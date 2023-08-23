from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import LatestNewsSearchForm
from .models import Skill, TeamMember, Gallery, Comment

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


class HomeView2(TemplateView):
    template_name = 'index-2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preLoader'] = PreLoader.objects.all()
        context['infos'] = Info.objects.last()
        context['sliders'] = Slider.objects.all()
        context['abouts'] = About.objects.last()
        context['services'] = Service.objects.filter(is_draft=False)
        context['videos'] = Video.objects.all()
        context['projects'] = Project.objects.all()
        context['topClients'] = TopClients.objects.all()
        context['professional'] = TeamMember.objects.all()
        context['clients'] = Client.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['latestNews'] = LatestNews.objects.all()
        return context


class HomeView3(TemplateView):
    template_name = 'index-3.html'

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
        context['photos'] = Gallery.objects.all()
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


class ErrorEmailView(View):
    def post(self, request):
        form = forms.ErrorEmailForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Done.')
        else:
            messages.error(request, 'Invalid! Please try again. ')
        return redirect('/home/')


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
        context['services'] = Service.objects.all()
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
        context['services'] = Service.objects.all()
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
        context['professional'] = TeamMember.objects.all()

        return context


def team(request):
    q = request.GET.get('q')
    professional = TeamMember.objects.filter(skill__name__icontains=q)
    skills = Skill.objects.all()
    context = {'skills': skills, 'professional': professional}
    return render(request, 'team.html', context)


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


class BlogDetailView(View):
    def get(self, request, ln_id):
        ln = LatestNews.objects.get(id=ln_id)
        context = {
            'ln': ln,
            'infos': Info.objects.last(),
            'services': Service.objects.all(),
            'abouts': About.objects.last(),
            'latestNews': LatestNews.objects.all()

        }
        return render(request, 'blog-details.html', context=context)


def search_items(request):
    form = LatestNewsSearchForm(request.GET)

    if form.is_valid():
        name = form.cleaned_data.get('name')
        category = form.cleaned_data.get('category')

        items = LatestNews.objects.all()

        if name:
            items = items.filter(name__icontains=name)

        if category:
            items = items.filter(category__icontains=category)

        context = {'form': form, 'items': items}
        return render(request, 'blog-details.html', context)

    context = {'form': form}
    return render(request, 'blog-details.html', context)


class ProjectView(TemplateView):
    template_name = 'project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preLoader'] = PreLoader.objects.all()
        context['infos'] = Info.objects.last()
        context['latestNews'] = LatestNews.objects.all()
        context['projects'] = Project.objects.all()
        context['abouts'] = About.objects.last()
        return context


class ProjectDetailView(View):
    def get(self, request, p_id):
        p = Project.objects.get(id=p_id)
        context = {
            'p': p,
            'infos': Info.objects.last(),
            'services': Service.objects.all(),
            'abouts': About.objects.last(),

        }
        return render(request, 'project-details.html', context=context)


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            password = form.data['password']
            user = form.save()
            user.set_password(password)
            user.save()
            messages.success(request, 'Registration successfully done')
            return redirect('/auth/login/')

        else:
            messages.error(request, 'Invalid data')

        context = {form: 'form'}
        return render(request, 'register.html', context=context)


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return redirect('/')
                messages.error(request, 'Password did not match')
            except ObjectDoesNotExist:
                messages.error(request, 'User not found')
        else:
            messages.error(request, 'Invalid data')
        context = {'form': form}
        return render(request, 'login.html', context=context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/auth/login/')


class ErrorView(TemplateView):
    template_name = 'error.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preLoader'] = PreLoader.objects.all()
        context['infos'] = Info.objects.last()
        context['abouts'] = About.objects.last()
        context['services'] = Service.objects.filter(is_draft=False)
        return context


class CommentView(View):
    def post(self, request, ln_id):
        form = forms.CommentForm(data=request.POST)
        if form.is_valid():
            Comment.objects.create(
                ln_id=ln_id
            ).save()
        else:
            messages.error(request, 'Invalid data.')
        return redirect(request, f"/blog-details/{ln_id}/")
