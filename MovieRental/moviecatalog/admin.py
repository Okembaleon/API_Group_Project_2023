from django.contrib import admin

from moviecatalog.models import Customer
from moviecatalog.models import Genre
from moviecatalog.models import Movie
from moviecatalog.models import Rental

# Register your models here.
admin.site.register(Customer)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Rental)
