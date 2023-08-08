from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('newsLetter/', views.NewsLetterView.as_view(), name='newsLetter'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact-us/', views.ContactUsView.as_view(), name='contact-us'),
    path('team/', views.TeamView.as_view(), name='team'),
    path('team/details/<int:teamMember_id>/', views.TeamMemberDetailView.as_view(), name='team-details'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('service/details/<int:service_id>/', views.ServiceDetailView.as_view(), name='service-details'),
    path('testimonial/', views.TestimonialView.as_view(), name='testimonial'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('coming-soon/', views.ComingSoonView.as_view(), name='coming-soon'),
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe')
]