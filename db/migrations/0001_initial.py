# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to=b'books', blank=True)),
                ('year', models.DateField(null=True, blank=True)),
                ('bestseller_rank', models.IntegerField()),
                ('slug', models.SlugField(max_length=240, null=True, blank=True)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name_plural': 'Books',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('alternate_name', models.CharField(max_length=120, null=True, blank=True)),
                ('bio', models.CharField(max_length=1000, null=True, blank=True)),
                ('born_date', models.DateField(null=True, blank=True)),
                ('died_date', models.DateField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'photos', blank=True)),
                ('birth_city', models.CharField(max_length=80, null=True, blank=True)),
                ('death_city', models.CharField(max_length=80, null=True, blank=True)),
                ('height', models.IntegerField(help_text=b'Height in inches.', null=True, blank=True)),
                ('score', models.IntegerField(null=True, blank=True)),
                ('slug', models.SlugField(max_length=240, null=True, blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Persons',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField()),
                ('ip_address', models.CharField(max_length=16)),
                ('rating_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('rating_date',),
                'verbose_name_plural': 'Ratings',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.CharField(max_length=120)),
                ('person', models.ForeignKey(to='db.Person')),
            ],
            options={
                'ordering': ('person',),
                'verbose_name_plural': 'Roles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=240)),
                ('slug', models.SlugField(max_length=240, null=True, blank=True)),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
                ('length', models.IntegerField(null=True, blank=True)),
                ('year', models.IntegerField()),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('show_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='db.Show')),
                ('budget', models.IntegerField(null=True, blank=True)),
                ('box_office', models.BigIntegerField(null=True, blank=True)),
                ('distribution_company', models.IntegerField(blank=True, null=True, choices=[(2, b'20th Century Fox'), (4, b'Alliance Atlantis'), (12, b'AMC'), (15, b'BBC One'), (10, b'Buena Vista'), (0, b'CBS Paramount'), (5, b'Columbia Pictures'), (8, b'Hallmark Entertainment'), (1, b'MGM'), (3, b'NBC Universal'), (13, b'New Line Cinema'), (11, b'Orion Pictures'), (14, b'Sony Pictures'), (6, b'TriStar Pictures'), (9, b'Walt Disney'), (7, b'Warner Brothers')])),
                ('genre', models.IntegerField(choices=[(0, b'Science Fiction'), (1, b'Fantasy'), (2, b'Horror')])),
                ('subgenre', models.IntegerField(choices=[(b'Science Fiction', ((1, b'Alien Invasion'), (2, b'Alien World'), (18, b'Alternate Dimension'), (3, b'Colonization'), (4, b'Comedy Sci-Fi'), (5, b'Computer World'), (19, b'Dystopian Future'), (6, b'Monster'), (7, b'Military'), (8, b'Police Drama'), (9, b'Post-Apocalyptic'), (10, b'Robots'), (17, b'Sci-Fi Drama'), (11, b'Sci-Horror'), (12, b'Space Opera'), (13, b'Space Western'), (14, b'Superhero'), (15, b'Time Travel'), (16, b'Viral Outbreak'))), (b'Fantasy', ((100, b'Comedy Fantasy'), (101, b'Historical Fiction'), (105, b'Modern Fairy Tale'), (102, b'Steampunk'), (103, b'Stone Age'), (104, b'Sword and Sorcery'))), (b'Horror', ((200, b'Comedy Horror'), (206, b'Demon'), (201, b'Lovecraftian'), (202, b'Murder'), (203, b'Vampire'), (204, b'Werewolf'), (205, b'Zombie')))])),
                ('director', models.ForeignKey(related_name='movie_director', blank=True, to='db.Person', null=True)),
                ('music_by', models.ForeignKey(related_name='movie_musicby', blank=True, to='db.Person', null=True)),
                ('producer', models.ManyToManyField(related_name='movie_producer', null=True, to='db.Person', blank=True)),
                ('writers', models.ManyToManyField(related_name='movie_writers', null=True, to='db.Person', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Movies',
            },
            bases=('db.show',),
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('show_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='db.Show')),
                ('season', models.IntegerField()),
                ('episode_num', models.IntegerField()),
                ('air_date', models.DateField(null=True, blank=True)),
                ('director', models.ForeignKey(related_name='episode_director', blank=True, to='db.Person', null=True)),
                ('producer', models.ForeignKey(related_name='episode_producer', blank=True, to='db.Person', null=True)),
            ],
            options={
                'ordering': ('year', 'season', 'episode_num'),
            },
            bases=('db.show',),
        ),
        migrations.CreateModel(
            name='TVSeries',
            fields=[
                ('show_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='db.Show')),
                ('num_seasons', models.IntegerField()),
                ('num_episodes', models.IntegerField(null=True, blank=True)),
                ('distribution_company', models.IntegerField(blank=True, null=True, choices=[(2, b'20th Century Fox'), (4, b'Alliance Atlantis'), (12, b'AMC'), (15, b'BBC One'), (10, b'Buena Vista'), (0, b'CBS Paramount'), (5, b'Columbia Pictures'), (8, b'Hallmark Entertainment'), (1, b'MGM'), (3, b'NBC Universal'), (13, b'New Line Cinema'), (11, b'Orion Pictures'), (14, b'Sony Pictures'), (6, b'TriStar Pictures'), (9, b'Walt Disney'), (7, b'Warner Brothers')])),
                ('genre', models.IntegerField(choices=[(0, b'Science Fiction'), (1, b'Fantasy'), (2, b'Horror')])),
                ('subgenre', models.IntegerField(choices=[(b'Science Fiction', ((1, b'Alien Invasion'), (2, b'Alien World'), (18, b'Alternate Dimension'), (3, b'Colonization'), (4, b'Comedy Sci-Fi'), (5, b'Computer World'), (19, b'Dystopian Future'), (6, b'Monster'), (7, b'Military'), (8, b'Police Drama'), (9, b'Post-Apocalyptic'), (10, b'Robots'), (17, b'Sci-Fi Drama'), (11, b'Sci-Horror'), (12, b'Space Opera'), (13, b'Space Western'), (14, b'Superhero'), (15, b'Time Travel'), (16, b'Viral Outbreak'))), (b'Fantasy', ((100, b'Comedy Fantasy'), (101, b'Historical Fiction'), (105, b'Modern Fairy Tale'), (102, b'Steampunk'), (103, b'Stone Age'), (104, b'Sword and Sorcery'))), (b'Horror', ((200, b'Comedy Horror'), (206, b'Demon'), (201, b'Lovecraftian'), (202, b'Murder'), (203, b'Vampire'), (204, b'Werewolf'), (205, b'Zombie')))])),
                ('creators', models.ManyToManyField(related_name='tvseries_creators', null=True, to='db.Person', blank=True)),
                ('theme_composer', models.ForeignKey(related_name='tvseries_themecomposer', blank=True, to='db.Person', null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': "TV Series'",
            },
            bases=('db.show',),
        ),
        migrations.AddField(
            model_name='role',
            name='show',
            field=models.ForeignKey(to='db.Show'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rating',
            name='show',
            field=models.ForeignKey(to='db.Show'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='episode',
            name='tvshow',
            field=models.ForeignKey(to='db.TVSeries'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='episode',
            name='writers',
            field=models.ManyToManyField(related_name='episode_writers', null=True, to='db.Person', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='book_authors', null=True, to='db.Person', blank=True),
            preserve_default=True,
        ),
    ]
