from django.contrib import admin
from .models import Rating, Movie, Buch, Buchnumber, Character, Student, Author, Modul



@admin.register(Buch)
class BuchAdmin(admin.ModelAdmin):
    list_display=('title', 'completed', 'preis', 'cover', 'datum',
     'description', 'status', 'autor', 'number')
    list_filter=['datum']
    #bei suchen kann man nach igrendein eingenschat suchnen
    search_fields=['title']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('vorname', 'nachname', 'martikelnummer',
     'wohnort', 'geburtsdatum', 'datum', 'semester')


@admin.register(Modul)
class ModulStudentenAdmin(admin.ModelAdmin):
	list_display=('modulnummer', 'bezeichnung', 'prof')
#class ModulAdmin(admin.ModelAdmin):
#	list_display=('bezeichnung', 'prof')

admin.site.register(Buchnumber)
admin.site.register(Character)
admin.site.register(Author)
admin.site.register(Movie)
admin.site.register(Rating)
 #
# Register your models here.
