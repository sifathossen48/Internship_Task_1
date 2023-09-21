from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home-2', views.HomeView2.as_view(), name='home-2'),
    path('home-3/', views.HomeView3.as_view(), name='home-3'),
    path('newsLetter/', views.NewsLetterView.as_view(), name='newsLetter'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact-us/', views.ContactUsView.as_view(), name='contact-us'),
    path('team/', views.TeamView.as_view(), name='team'),
    path('team/details/<int:teamMember_id>/', views.TeamMemberDetailView.as_view(), name='team-details'),
    path('project/', views.ProjectView.as_view(), name='project'),
    path('project/details/<int:p_id>/', views.ProjectDetailView.as_view(), name='project-details'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('service/details/<int:service_id>/', views.ServiceDetailView.as_view(), name='service-details'),
    path('testimonial/', views.TestimonialView.as_view(), name='testimonial'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog-details/<int:ln_id>/', views.BlogDetailView.as_view(), name='blog-details'),
    path('blog-details/comment/<int:ln_id>/', views.CommentView.as_view(), name='blog-comment'),
    path('coming-soon/', views.ComingSoonView.as_view(), name='coming-soon'),
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    path('error/', views.ErrorView.as_view(), name='error'),
    path('error/email/', views.ErrorEmailView.as_view(), name='error-email'),
    path('search/', views.search_news, name='search_news'),
    path('all-search/', views.search, name='search')

]