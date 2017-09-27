from django.contrib import admin
from demoApp.models import SnesGame

# this tells the admin to display the title rather than SnesGame Object
class GameAdmin(admin.ModelAdmin):
    list_display = ('gameName',)

# this registers the model
admin.site.register(SnesGame, GameAdmin)