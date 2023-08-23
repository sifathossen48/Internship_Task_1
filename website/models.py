from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class PreLoader(models.Model):
    letter = models.CharField(max_length=1)

    def __str__(self):
        return self.letter


class Slider(models.Model):
    image = models.ImageField(upload_to='slider/')
    title = models.CharField(max_length=35)
    title2 = models.CharField(max_length=60)
    year = models.CharField(max_length=6)
    land = models.CharField(max_length=20)
    banner = models.ImageField(upload_to='banner/')
    item_name = models.CharField(max_length=20, null=True)
    item_image = models.ImageField(upload_to='slider/', null=True)
    item_desc = models.TextField(max_length=400, null=True)
    item_location = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title


class Info(models.Model):
    company = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='logo/')
    favicon = models.ImageField(upload_to='favicon/')
    header_shape = models.ImageField(upload_to='shape/', null=True)
    slider_shape = models.ImageField(upload_to='shape/', null=True)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    youtube = models.CharField(max_length=50)
    pinterest = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    location = models.CharField(max_length=100)
    designer = models.CharField(max_length=50)
    designer_profile = models.CharField(max_length=100)
    designs_year = models.CharField(max_length=10)
    project_title = models.CharField(max_length=30)
    project_subtitle = models.CharField(max_length=20)
    project_background = models.ImageField(upload_to='background/')
    contact_title = models.CharField(max_length=30)
    contact_subtitle = models.CharField(max_length=20)
    latestNews_title = models.CharField(max_length=30, null=True)
    about_page_title = models.CharField(max_length=20, null=True)
    about_title_background = models.ImageField(upload_to='background/', null=True)
    contact_page_title = models.CharField(max_length=20, null=True)
    service_page_title = models.CharField(max_length=40, null=True)
    service_page_title_background = models.ImageField(upload_to='background/', null=True)
    service_page_section_background = models.ImageField(upload_to='background/', null=True)
    service_about_title = models.CharField(max_length=50, null=True)
    service_about_background = models.ImageField(upload_to='background/', null=True)
    service_about_desc = models.TextField(max_length=400, null=True)
    service_about_image = models.ImageField(upload_to='about/', null=True)
    service_about_image2 = models.ImageField(upload_to='about/', null=True)
    service_about_icon = models.ImageField(upload_to='about/', null=True)
    project_page_title = models.CharField(max_length=30, null=True)
    project_page_title_background = models.ImageField(upload_to='projects/', null=True)
    project_page_about_title = models.CharField(max_length=30, null=True)
    project_details_page_title = models.CharField(max_length=30, null=True)
    project_details_page_title_background = models.ImageField(upload_to='background/', null=True)
    blog_page_title = models.CharField(max_length=20, null=True)
    blog_page_title_background = models.ImageField(upload_to='background/', null=True)
    blog_details_page_title = models.CharField(max_length=20, null=True)
    blog_details_page_title_background = models.ImageField(upload_to='background/', null=True)
    team_page_title = models.CharField(max_length=30, null=True)
    team_page_title_background = models.ImageField(upload_to='background/', null=True)
    team_details_page_title = models.CharField(max_length=30, null=True)
    team_details_page_title_background = models.ImageField(upload_to='background/', null=True)
    testimonial_background = models.ImageField(upload_to='background/', null=True)
    testimonial_page_title = models.CharField(max_length=30, null=True)
    testimonial_page_title_background = models.ImageField(upload_to='background/', null=True)
    top_client_icon = models.ImageField(upload_to='icon/')
    footer_image = models.ImageField(upload_to='footer/', null=True)
    footer_image2 = models.ImageField(upload_to='footer/', null=True)
    footer_image3 = models.ImageField(upload_to='footer/', null=True)
    footer_background = models.ImageField(upload_to='background/', null=True)
    error_head = models.CharField(max_length=3, null=True)
    error_page_title = models.CharField(max_length=30, null=True)
    error_page_subtitle = models.CharField(max_length=100, null=True)
    error_page_title_background = models.ImageField(upload_to='background/', null=True)

    def __str__(self):
        return self.company


class About(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to='abouts/')
    author_name = models.CharField(max_length=30)
    author_title = models.CharField(max_length=20, null=True)
    author_details = models.TextField(null=True, blank=True)
    author_image = models.ImageField(upload_to='ceo/')
    button_text = models.CharField(max_length=30)
    item_name = models.CharField(max_length=30)
    item_location = models.CharField(max_length=30)
    background_image = models.ImageField(upload_to='background/', null=True)
    about_quote_icon = models.ImageField(upload_to='icon/', null=True)
    work_sample_picture = models.ImageField(upload_to='abouts/', null=True)
    year_of_company_experience = models.CharField(max_length=3, null=True)
    circle_title_of_experience = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=50)
    title_background = models.ImageField(upload_to='background/', null=True)
    desc = models.TextField(null=True, blank=True)
    service_logo = models.ImageField(upload_to='service/', null=True)
    sample_image = models.ImageField(upload_to='service/', null=True)
    sample_image2 = models.ImageField(upload_to='service/', null=True)
    sample_image3 = models.ImageField(upload_to='service/', null=True)
    is_draft = models.BooleanField(default=True, null=True)
    is_solution = models.BooleanField(default=False, null=True)
    is_include = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title

class ProjectItem(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=40)
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=70, null=True)
    image = models.ImageField(upload_to='projects/', null=True)
    location = models.CharField(max_length=40, null=True)
    image2 = models.ImageField(upload_to='projects/', null=True)
    image3 = models.ImageField(upload_to='projects/', null=True)
    desc = models.TextField(null=True)
    desc2 = models.TextField(null=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    website_link = models.CharField(max_length=100)
    company_logo = models.ImageField('clients/')

    def __str__(self):
        return self.website_link


class LatestNews(models.Model):
    author = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=30, null=True)
    title = models.CharField(max_length=60)
    image1 = models.ImageField(upload_to='blog/', null=True)
    image2 = models.ImageField(upload_to='blog/', null=True)
    image3 = models.ImageField(upload_to='blog/', null=True)
    desc = models.TextField(null=True, blank=True)
    desc2 = models.TextField(null=True, blank=True)
    quote = models.TextField(max_length=200, null=True)
    author_of_quote = models.CharField(max_length=30, null=True)
    quote_icon = models.ImageField(upload_to='icon/', null=True)

    @property
    def get_short_desc(self):
        return self.desc[:100]

    def get_short_desc2(self):
        return self.desc[:250]

    def get_comment(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title


class NewsLetter(models.Model):
    email = models.EmailField(max_length=30, unique=True)
    def __str__(self):
        return self.email


class Contact(models.Model):
    title_background = models.ImageField(upload_to='background/')
    page_background = models.ImageField(upload_to='background/')
    contact_title = models.CharField(max_length=40)
    contact_desc = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.contact_title


class ContactUs(models.Model):
    username = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.username


class Testimonial(models.Model):
    author_name = models.CharField(max_length=40)
    author_title = models.CharField(max_length=30)
    quote = models.TextField(null=True, blank=True)
    author_image = models.ImageField(upload_to='author/')
    def __str__(self):
        return self.author_name
class Video(models.Model):
    thumbnail = models.ImageField(upload_to='thumbnail/')
    title = models.CharField(max_length=50)
    title2 = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    video_link = models.CharField(max_length=100)
    quotes = models.ForeignKey(Testimonial, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    @property
    def author_name(self):
        return self.quotes.author_name
    def author_title(self):
        return self.quotes.author_title
    def quote(self):
        return self.quotes.quote
    def author_image(self):
        return self.quotes.author_image

class Skill(models.Model):
    skill_name = models.CharField(max_length=20)

    def __str__(self):
        return self.skill_name


class TeamMember(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=70)
    profile = models.ImageField(upload_to='team_member/')
    age = models.CharField(max_length=10)
    experience = models.CharField(max_length=20)
    desc = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    facebook = models.CharField(max_length=60)
    instagram = models.CharField(max_length=60)
    twitter = models.CharField(max_length=60)
    skill = models.ManyToManyField(Skill)

    @property
    def get_other_member(self):
        return TeamMember.objects.filter(skill__in=self.skill.all())[:3]
    def get_skill_member(self):
        return TeamMember.objects.filter(skill__in=self.skill.all())

    def __str__(self):
        return self.name


class TopClients(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name

class ComingSoon(models.Model):
    page_subtitle = models.CharField(max_length=50)
    page_title = models.CharField(max_length=20)
    page_background = models.ImageField(upload_to='background')
    date = models.DateTimeField(null=True)
    form_title = models.CharField(max_length=50)
    def __str__(self):
        return self.page_title


class Subscribe(models.Model):
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        return self.email

class Comment(models.Model):
    name = models.CharField(max_length=20)
    news = models.ForeignKey(LatestNews, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=50)
    comment = models.TextField()
    def __str__(self):
        return f"{self.name}:{self.id}"

class ErrorEmail(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    def __str__(self):
        return self.email

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    link = models.CharField(max_length=60)
    def __str__(self):
        return self.link