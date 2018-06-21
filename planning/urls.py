from django.conf.urls import url
from django.urls import path
# from . import views
from .views import AboutView, ComingView, HomeView

app_name='planning'
urlpatterns = [
    # url(r'^/$', TemplateView.as_view(template_name="about.html")),
    path('home/', HomeView.as_view()),
    path('about/', AboutView.as_view()),
    path('coming/', ComingView.as_view()),
]