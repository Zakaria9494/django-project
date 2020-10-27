from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# hier bauen wir relationship to buch mit Buchnumber

class Buchnumber(models.Model):
    isbin_1 = models.CharField(max_length=10, blank=True)
    isbin_2 = models.CharField(max_length=13, blank=True)


class Buch(models.Model):
    Status = {
        ("verfügbar", "verfügbar"),
        ("ausgeliehen", "ausgeliehen"),
        ("nicht verfügbar", "nicht verfügbar"),
        ("nicht existiert", "nicht existiert")
    }
    title = models.CharField(max_length=120)
    description = models.TextField()
    preis = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    datum = models.DateField(blank=True, null=True, default=None)
    autor = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=30, null=True, blank=False, unique=True, default="", choices=Status)
    cover = models.ImageField(upload_to='covers/', blank=True)
    completed = models.BooleanField(default=False)
    number = models.OneToOneField(Buchnumber, null=True, blank=True, on_delete=models.CASCADE)


    def _str_(self):
        return self.title


## jetzt one to many

class Character(models.Model):
    name = models.CharField(max_length=300)
    book = models.ForeignKey(Buch, on_delete=models.CASCADE, related_name='characters')

# hier machen wir many to many

class Author(models.Model):
    name=models.CharField(max_length=30)
    books=models.ManyToManyField(Buch, related_name="authors")

# hier bau ich Studentmodel

class Modul(models.Model):
    modulnummer=models.IntegerField()
    bezeichnung=models.CharField(max_length=40)
    prof=models.CharField(max_length=30)



class Student(models.Model):
    Semesters = {
        ("erstes Semester", "erstes Semester"),
        ("zweites Semester", "zweites Semester"),
        ("drittes Semester", "drittes Semester"),
        ("viertes Semester", "viertes Semester"),
        ("fünftes Semester", "fünftes Semester"),
        ("sechstes Semester", "sechstes Semester")
    }
    vorname = models.CharField(max_length=200, blank=False)
    nachname = models.CharField(max_length=200, blank=False)
    martikelnummer = models.CharField(max_length=120, blank=True)
    wohnort = models.CharField(max_length=200, blank=False)
    geburtsdatum = models.DateField(blank=True, null=True, default=None)
    datum = models.DateField(blank=True, null=True, default=None)
    semester = models.CharField(max_length=50, null=True, blank=False, unique=True, default="", choices=Semesters)
    modul_name = models.ManyToManyField(Modul, related_name="studetenmodule")

    def _str_(self):
        return self.vorname

## Movie Projekt realiesieren

class Movie(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=100)

    def no_of_ratings(self):
        ratings=Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        sum=0
        ratings=Rating.objects.filter(movie=self)
        for rating in ratings:
            sum+=rating.stars
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0

class Rating(models.Model):
    # refrenz zu Moive
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),
    MaxValueValidator(5)])
    class Meta:
        unique_together=(('user', 'movie'),)
        index_together=(('user', 'movie'),)


    #wenn ich die movie remove we have remove the rating und umgekehrt
