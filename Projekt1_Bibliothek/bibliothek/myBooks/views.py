from .models import Buch
from .serializers import BuchMiniSerializer, BuchSerializer,StudentMiniSerializer
from rest_framework import viewsets, status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer, StudentSerializer ,MovieSerializer, RatingSerializer
from .models import Student , Movie, Rating
from rest_framework.decorators import action
from django.contrib.auth.models import User




         # add this



class BuchView(viewsets.ModelViewSet):
    serializer_class=BuchMiniSerializer
    queryset=Buch.objects.all()
    authentication_classes=(TokenAuthentication,)



    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=BuchSerializer(instance)
        return Response(serializer.data)



def first(request):
    books=Buch.objects.all()
    return render(request, 'index.html', {"books": books})



## das ist the view für studenten
"""
class StudentView(viewsets.ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
"""




class StudentView(viewsets.ModelViewSet):
    serializer_class=StudentMiniSerializer
    queryset=Student.objects.all()
    authentication_classes=(TokenAuthentication,)



    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=StudentSerializer(instance)
        return Response(serializer.data)


## noew für Projekt Moive


class UserView(viewsets.ModelViewSet):
     queryset=User.objects.all()
     serializer_class=UserSerializer





class MovieView(viewsets.ModelViewSet):
     queryset=Movie.objects.all()
     serializer_class=MovieSerializer
     authentication_classes=(TokenAuthentication,)





     @action(detail=True, methods=['POST'])
     def rat_movie(self, request, pk=None):
         if 'stars' in request.data:
             movie=Movie.objects.get(id=pk)
             stars=request.data['stars']
             #user=request.user
             user=User.objects.get(id=1)

             try:
                 rating=Rating.objects.get(user=user.id, movie=movie.id)
                 rating.stars=stars
                 rating.save()
                 serializer=RatingSerializer(rating, many=False)
                 response={'message': 'Rating akualisiert', 'Ergbnis': serializer.data}
                 return Response(response, status=status.HTTP_200_OK)
             except:
                  rating=Rating.objects.create(user=user, movie=movie, stars=stars)
                  serializer=RatingSerializer(rating, many=False)
                  response={'message': 'Rating erstellt', 'Ergbnis': serializer.data}
                  return Response(response, status=status.HTTP_200_OK)


             print('user', user.username)
             print('user', user)
             print('movie title: ', movie.title)
             response={'message':'ists work'}
             return Response(response, status=status.HTTP_200_OK)
         else:
            response={'message':'you nend to provide data'}
            return Response(response, status=status.HTTP_400_BAD_RQUEST)





class RatingView(viewsets.ModelViewSet):
     queryset=Rating.objects.all()
     serializer_class=RatingSerializer
     authentication_classes=(TokenAuthentication,)
 
