from django.db import models
import datetime
 
 
class SnesGame(models.Model):
    gameName = models.CharField(max_length=200)
    releaseDate = models.DateField(default=datetime.date.today)
    rating = models.IntegerField(default = 0)
    description = models.TextField(default = "No description")
    # the model didn't work without this but the web seems to suggest that it's not required
    # The id field was created in the db without me specifying
    id = models.AutoField(primary_key=True)

# from _datetime import datetime
# 
# class SnesGame():
#  
#     def __init__(self, name = "No name", releaseDate=datetime.now(),
#                  rating = 0, description = "No description"):
#         self.name = name
#         self.releaseDate = releaseDate
#         self.rating = rating
#         self.description = description
#  
#     def __str__( self ) :
#         return "(" + str( self.name ) + ", " + str( self.releaseDate ) + ", " + str( self.rating ) + ", " + str( self.description )+ ")"
#  
#  
#  
#     def get_name(self):
#         return self.__name
#  
#  
#     def get_release_date(self):
#         return self.__releaseDate
#  
#  
#     def get_rating(self):
#         return self.__rating
#  
#  
#     def get_description(self):
#         return self.__description
#  
#  
#     def set_name(self, value):
#         self.__name = value
#  
#   
#     def set_release_date(self, value):
#         self.__releaseDate = value
#  
#  
#     def set_rating(self, value):
#         self.__rating = value
#  
#  
#     def set_description(self, value):
#         self.__description = value
#  
# # at some point run an experiment on how the del methods work
#     def del_name(self):
#         del self.__name
#  
#  
#     def del_release_date(self):
#         del self.__releaseDate
#  
#  
#     def del_rating(self):
#         del self.__rating
#  
#  
#     def del_description(self):
#         del self.__description

        
    