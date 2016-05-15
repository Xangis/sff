from django.forms import SelectMultiple
from django.contrib import admin
from django.db import models
from models import *

class PersonAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class MovieAdmin(admin.ModelAdmin):
    formfield_overrides = { models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'10'})}, }
    list_display = ('name', 'subgenre', 'year')
    search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
    formfield_overrides = { models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'10'})}, }
    list_display = ('title',)
    search_fields = ('title',)

class EpisodeAdmin(admin.ModelAdmin):
    formfield_overrides = { models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'16'})}, }
    fieldsets = (
        (None, {
            'fields': (('name', 'slug'), ('tvshow', 'season', 'episode_num'),
            ('year', 'air_date'),
            ('director', 'producer'), 'writers',
            ('description', 'length'),
            )
         }),
    )
    list_display = ('name', 'tvshow', 'season', 'episode_num')
    search_fields = ('name', 'tvshow__name')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('person', 'character', 'show')
    search_fields = ('person__name', 'character', 'show__name')

class TVSeriesAdmin(admin.ModelAdmin):
    formfield_overrides = { models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'12'})}, }
    list_display = ('name', 'subgenre', 'year')
    search_fields = ('name',)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('show', 'rating')
    search_fields = ('show__name',)
    ordering = ('-rating_date',)

class SubgenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')

admin.site.register(Movie, MovieAdmin)
admin.site.register(TVSeries, TVSeriesAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Subgenre, SubgenreAdmin)
admin.site.register(Company, CompanyAdmin)
