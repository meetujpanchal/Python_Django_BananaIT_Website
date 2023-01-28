from django.contrib import admin
from django.urls import path
from . import views
app_name = 'enroll'

urlpatterns = [
    path('',views.show_page,name="showpage"),
    path('ourteam/',views.team,name="ourteam"),
    path('aboutbanana/',views.about,name="aboutbananit"),
    path('events/',views.testi,name="testimonial"),
    path('Sevice/',views.services,name="service"),
    path('Contact_us/',views.contactus,name="contact"),
    path('career/',views.careerpg,name="careerp"),
    path('pricing/',views.price,name="pricp"),
    path('potfolio/',views.story_list,name="story_list"),
    path('potfolio/<slug:category_slug>',views.story_list,name="story_category"),
    path('client/',views.clnt,name="cnt"),
    path('export/',views.export_csv,name="export-csv"),
]
