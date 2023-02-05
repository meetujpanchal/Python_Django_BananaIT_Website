from cgitb import strong
from unicodedata import name
from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
from .models import TblTeam,Tblslider,Tblclient,Tblrecentwork,Tblcontact,Tbltestimonial,Tblenquiry,Category,Story

# Register your models here.

@admin.register(Tblenquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','description']

@admin.register(TblTeam)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','name','designation','qualification','profile_pic','fblink','inlink','twlink','linlink']

@admin.register(Tblslider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['id','slide_title','slide_description','slider_image']

@admin.register(Tblclient)
class clientAdmin(admin.ModelAdmin):
    list_display = ['id','c_name','client_img']    

@admin.register(Tblrecentwork)
class portAdmin(admin.ModelAdmin):
    list_display = ['id','title','portfol_img','navigatelink','description','category']    

@admin.register(Tblcontact)
class contactAdmin(admin.ModelAdmin):
    list_display = ['id','email','mobile']   

@admin.register(Tbltestimonial)
class testimonialAdmin(admin.ModelAdmin):    
    list_display = ['id','title','designation','description','testi_img']

# class EnquieyAdmin(ImportExportModelAdmin,admin.ModelAdmin):
#     list_display = ('id','name','email','description')

# admin.site.register(Tblenquiry , EnquieyAdmin)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','portfol_img','navigatelink','description','publish']    
