
from django.contrib import admin
from django.urls import path
from home import views
admin.site.site_header="Debayan Ray Django Website"
admin.site.site_title="Debayan Ray Django Website"
admin.site.index_title="Welcome to Debayan Ray Django Website"

urlpatterns = [
    
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact')

]
