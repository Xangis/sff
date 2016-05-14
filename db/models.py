from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

COMPANY_CHOICES = (
  (2, '20th Century Fox'),
  (4, 'Alliance Atlantis'),
  (12, 'AMC'),
  (15, 'BBC One'),
  (10, 'Buena Vista'),
  (0, 'CBS Paramount'),
  (5, 'Columbia Pictures'),
  (8, 'Hallmark Entertainment'),
  (1, 'MGM'),
  (3, 'NBC Universal'),
  (13, 'New Line Cinema'),
  (11, 'Orion Pictures'),
  (14, 'Sony Pictures'),
  (6, 'TriStar Pictures'),
  (9, 'Walt Disney'),
  (7, 'Warner Brothers'),
)

GENRE_CHOICES = (
  (0, 'Science Fiction'),
  (1, 'Fantasy'),
  (2, 'Horror'),
)

SUBGENRE_CHOICES = (
('Science Fiction',(
  (1, 'Alien Invasion'),
  (2, 'Alien World'),
  (18, 'Alternate Dimension'),
  (3, 'Colonization'),
  (4, 'Comedy Sci-Fi'),
  (5, 'Computer World'),
  (19, 'Dystopian Future'),
  (6, 'Monster'),
  (7, 'Military'),
  (8, 'Police Drama'),
  (9, 'Post-Apocalyptic'),
  (10, 'Robots'),
  (17, 'Sci-Fi Drama'),
  (11, 'Sci-Horror'),
  (12, 'Space Opera'),
  (13, 'Space Western'),
  (14, 'Superhero'),
  (15, 'Time Travel'),
  (16, 'Viral Outbreak'),
)),
('Fantasy', (
  (100, 'Comedy Fantasy'),
  (101, 'Historical Fiction'),
  (105, 'Modern Fairy Tale'),
  (102, 'Steampunk'),
  (103, 'Stone Age'),
  (104, 'Sword and Sorcery'),
)),
('Horror', (
  (200, 'Comedy Horror'),
  (206, 'Demon'),
  (201, 'Lovecraftian'),
  (202, 'Murder'),
  (203, 'Vampire'),
  (204, 'Werewolf'),
  (205, 'Zombie'),
)),
)

SUBGENRE_SLUG_MAP = (
# Sci-fi
('alien-invasion', 1),
('alien-world', 2),
('alternate-dimension', 18),
('colonization', 3),
('comedy-sci-fi', 4),
('computer-world', 5),
('dystopian-future', 19),
('monster', 6),
('military', 7),
('police-drama', 8),
('post-apocalyptic', 9),
('robots', 10),
('sci-fi-drama', 17),
('sci-horror', 11),
('space-opera', 12),
('space-western', 13),
('superhero', 14),
('time-travel', 15),
('viral-outbreak', 16),
# Fantasy
('comedy-fantasy', 100),
('historical-fiction', 101),
('modern-fairy-tale', 105),
('steampunk', 102),
('stone-age', 103),
('sword-and-sorcery', 104),
# Horror
('comedy-horror', 200),
('demon', 206),
('lovecraftian', 201),
('murder', 202),
('vampire', 203),
('werewolf', 204),
('zombie', 205),
)

class Subgenre(models.Model):
    genre = models.IntegerField(choices=GENRE_CHOICES)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    slug = models.CharField(max_length=60, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Subgenre, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('genre', 'name', )

class Show(models.Model):
    name = models.CharField(max_length=240, null=False, blank=False)
    slug = models.SlugField(max_length=240, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    year = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Show, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )

class Movie(Show):
    director = models.ForeignKey('Person', null=True, blank=True, related_name='movie_director')
    producer = models.ManyToManyField('Person', null=True, blank=True, related_name='movie_producer')
    writers = models.ManyToManyField('Person', null=True, blank=True, related_name='movie_writers')
    music_by = models.ForeignKey('Person', null=True, blank=True, related_name='movie_musicby')
    budget = models.IntegerField(null=True, blank=True)
    box_office = models.BigIntegerField(null=True, blank=True)
    distribution_company = models.IntegerField(choices=COMPANY_CHOICES, null=True, blank=True)
    genre = models.IntegerField(choices=GENRE_CHOICES)
    subgenre = models.ForeignKey('Subgenre', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Show, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Movies'

class TVSeries(Show):
    num_seasons = models.IntegerField()
    num_episodes = models.IntegerField(null=True, blank=True)
    distribution_company = models.IntegerField(choices=COMPANY_CHOICES, null=True, blank=True)
    genre = models.IntegerField(choices=GENRE_CHOICES)
    subgenre = models.ForeignKey('Subgenre', null=True, blank=True)
    creators = models.ManyToManyField('Person', null=True, blank=True, related_name='tvseries_creators')
    theme_composer = models.ForeignKey('Person', null=True, blank=True, related_name='tvseries_themecomposer')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Show, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name_plural = "TV Series'"

class Episode(Show):
    tvshow = models.ForeignKey('TVSeries', null=False, blank=False)
    season = models.IntegerField()
    episode_num = models.IntegerField()
    director = models.ForeignKey('Person', null=True, blank=True, related_name='episode_director')
    producer = models.ForeignKey('Person', null=True, blank=True, related_name='episode_producer')
    writers = models.ManyToManyField('Person', null=True, blank=True, related_name='episode_writers')
    air_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Show, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.tvshow) + ' S' + str(self.season) + 'E' + str(self.episode_num) + ' - ' + self.name

    class Meta:
        ordering = ('year', 'season', 'episode_num')

class Person(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    alternate_name = models.CharField(max_length=120, null=True, blank=True)
    bio = models.CharField(max_length=1000, null=True, blank=True)
    born_date = models.DateField(null=True, blank=True)
    died_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='photos', null=True, blank=True)
    birth_city = models.CharField(max_length=80, null=True, blank=True)
    death_city = models.CharField(max_length=80, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True, help_text='Height in inches.') # Height in inches.
    score = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(max_length=240, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Person, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Persons'

class Role(models.Model):
    person = models.ForeignKey('Person', null=False, blank=False)
    character = models.CharField(max_length=120, null=False, blank=False)
    show = models.ForeignKey('Show', null=False, blank=False)

    def __unicode__(self):
        return self.person.name + ' as ' + self.character + ' in ' + self.show.name

    class Meta:
        ordering = ('person',)
        verbose_name_plural = 'Roles'

class Book(models.Model):
    authors = models.ManyToManyField('Person', null=True, blank=True, related_name='book_authors')
    title = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to='books', null=True, blank=True)
    year = models.DateField(null=True, blank=True)
    bestseller_rank = models.IntegerField(null=False, blank=False)
    slug = models.SlugField(max_length=240, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(models.Model, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title + ' by ' + self.authors

    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Books'

class Rating(models.Model):
    show = models.ForeignKey('Show', null=False, blank=False)
    rating = models.IntegerField(null=False, blank=False)
    ip_address = models.CharField(max_length=16, null=False, blank=False)
    rating_date = models.DateField(null=False, blank=False, auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.show.name + ' rating'

    class Meta:
        ordering = ('rating_date', )
        verbose_name_plural = 'Ratings'

#class Comment(models.Model):
#    beer = models.ForeignKey('Beer', null=False, blank=False)
#    text = models.CharField(max_length=1000, null=False, blank=False)
#    ip_address = models.CharField(max_length=16, null=False, blank=False)
#    post_date = models.DateField(null=False, blank=False, auto_now_add=True)##
#
#    def __unicode__(self):
#        return self.beer + ' comment'#
#
#    class Meta:
#        ordering = ('post_date', )
#        verbose_name_plural = 'Comments'

