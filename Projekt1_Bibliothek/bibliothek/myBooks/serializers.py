from rest_framework import serializers
from .models import Buch, Buchnumber, Character, Author, Student, Modul


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'name')


class BuchnumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buchnumber
        fields = ('id', 'isbin_1', 'isbin_2')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', )


class BuchSerializer(serializers.ModelSerializer):
    number = BuchnumberSerializer(many=False)
    characters = CharacterSerializer(many=True)
    authors=AuthorSerializer(many=True)

    class Meta:
        model = Buch
        fields = (
        'id', 'title', 'description', 'completed', 'preis', 'datum', 'status', 
        'cover', 'number', 'characters', 'authors')


class BuchMiniSerializer(serializers.ModelSerializer):


    class Meta:
        model = Buch
        fields = (
        'id', 'title')

##Studenten Serilizer now
"""
class ModulSerlizer(serializers.ModelSerializer):
    class Meta:
        mode=Student
        fields=("id","bezeichnung","prof")

"""

 

class ModulSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
        'id', 'bezeichnung',"prof")


class StudentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model=Student
        fields=('vorname', 'nachname', 'martikelnummer', "wohnort",
         "geburtsdatum", "datum" ,"semester")
    

class StudentMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
        'id', 'vorname')



 