from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponsePermanentRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from itertools import chain
from models import *
from forms import *

def index(request):
    shows = TVSeries.objects.all()
    movies = Movie.objects.all()
    persons = Person.objects.filter(score__gte=100)
    user = None
    if request.user.is_authenticated():
        user = request.user
    return render_to_response('index.htm', {'shows': shows, 'persons': persons, 'movies': movies, 'user': user })

def privacy(request):
    return render_to_response('privacy.htm')

def contact(request):
    return render_to_response('contact.htm')

def view_person(request, person_name):
    try:
        person = Person.objects.get(slug=person_name)
    except ObjectDoesNotExist:
        try:
            person = Person.objects.get(name=person_name)
            return HttpResponsePermanentRedirect('/person/' + person.slug + '/')
        except ObjectDoesNotExist:
            raise Http404
    recalculate_score(person)
    movies_directed = Movie.objects.filter(director=person)
    shows_directed = Episode.objects.filter(director=person)
    directed = list(chain(movies_directed, shows_directed))
    movies_produced = Movie.objects.filter(producer=person)
    shows_produced = Episode.objects.filter(producer=person)
    produced = list(chain(movies_produced, shows_produced))
    movies_wrote = Movie.objects.filter(writers=person)
    shows_wrote = Episode.objects.filter(writers=person)
    wrote = list(chain(movies_wrote, shows_wrote))
    movies_composed = Movie.objects.filter(music_by=person)
    shows_composed = TVSeries.objects.filter(theme_composer=person)
    composed = list(chain(movies_composed, shows_composed))
    created = TVSeries.objects.filter(creators=person)
    roles = Role.objects.filter(person=person).order_by('-show__year', '-show__name')
    return render_to_response('person.htm', {'person': person,
      'directed': directed, 'produced': produced, 'wrote': wrote,
      'composed': composed, 'created': created, 'roles': roles })

def view_show(request, show_name):
    try:
        show = TVSeries.objects.get(slug=show_name)
    except ObjectDoesNotExist:
        try:
            show = TVSeries.objects.get(name=show_name)
            return HttpResponsePermanentRedirect('/show/' + show.slug + '/')
        except ObjectDoesNotExist:
            raise Http404
    episodes = Episode.objects.filter(tvshow=show)
    roles = Role.objects.filter(show=show.id)
    return render_to_response('show.htm', {'show': show, 'episodes': episodes, 'roles': roles })

def view_movie(request, movie_name):
    try:
        movie = Movie.objects.get(slug=movie_name)
    except ObjectDoesNotExist:
        try:
            movie = Movie.objects.get(name=movie_name)
            return HttpResponsePermanentRedirect('/movie/' + movie.slug + '/')
        except ObjectDoesNotExist:
            raise Http404
    roles = Role.objects.filter(show=movie.id)
    user = None
    form = None
    my_rating = None
    if request.user.is_authenticated():
        user = request.user
        try:
            my_rating = Rating.objects.get(show=movie, user=request.user)
            my_rating = my_rating.rating
        except ObjectDoesNotExist:
            pass
    ratings = Rating.objects.filter(show=movie)
    total = 0
    rating = 0
    for item in ratings:
        total += item.rating
    if ratings.count() > 0:
        rating = total / ratings.count()
    return render_to_response('movie.htm', {'movie': movie, 'roles': roles, 'user': user, 'rating': rating,
        'num_ratings': ratings.count(), 'my_rating': my_rating  })

def view_episode(request, show_name, episode_name):
    try:
        show = TVSeries.objects.get(slug=show_name)
    except ObjectDoesNotExist:
        try:
            show = TVSeries.objects.get(name=show_name)
            return HttpResponsePermanentRedirect('/show/' + show.slug + '/episode/' + episode_name + '/')
        except ObjectDoesNotExist:
            raise Http404
    try:
        episode = Episode.objects.get(slug=episode_name, tvshow=show)
    except ObjectDoesNotExist:
        try:
            episode = Episode.objects.get(name=episode_name, tvshow=show)
            return HttpResponsePermanentRedirect('/show/' + show_name + '/episode/' + episode.slug + '/')
        except ObjectDoesNotExist:
            raise Http404
    regular_roles = Role.objects.filter(show=show.id)
    guest_roles = Role.objects.filter(show=episode.id)
    user = None
    form = None
    my_rating = None
    if request.user.is_authenticated():
        user = request.user
        try:
            my_rating = Rating.objects.get(show=episode, user=request.user)
            my_rating = my_rating.rating
        except ObjectDoesNotExist:
            pass
    ratings = Rating.objects.filter(show=episode)
    total = 0
    rating = 0
    for item in ratings:
        total += item.rating
    if ratings.count() > 0:
        rating = total / ratings.count()
    try:
        next = Episode.objects.get(season=episode.season, episode_num=(episode.episode_num+1), tvshow=show)
    except ObjectDoesNotExist:
        next = None
    try:
        prev = Episode.objects.get(season=episode.season, episode_num=(episode.episode_num-1), tvshow=show)
    except ObjectDoesNotExist:
        prev = None
    return render_to_response('episode.htm', {'show': show, 'episode': episode, 'regular_roles': regular_roles,
        'guest_roles': guest_roles, 'user': user, 'rating': rating, 'num_ratings': ratings.count(),
        'my_rating': my_rating, 'next': next, 'prev': prev })

def view_company(request, name):
    try:
        company = Company.objects.get(slug=name)
        shows = TVSeries.objects.filter(distribution_company=company)
        movies = Movie.objects.filter(distribution_company=company)
        return render_to_response('company.htm', {'shows': shows, 'movies': movies, 'company': company })
    except ObjectDoesNotExist:
        try:
            company = Company.objects.get(name=name)
            return HttpResponsePermanentRedirect('/company/' + company.slug + '/')
        except ObjectDoesNotExist:
            raise Http404

def view_subgenre(request, name):
    try:
        subgenre = Subgenre.objects.get(slug=name)
        shows = TVSeries.objects.filter(subgenre=subgenre)
        movies = Movie.objects.filter(subgenre=subgenre)
        return render_to_response('subgenre.htm', {'shows': shows, 'movies': movies, 'subgenre': subgenre })
    except ObjectDoesNotExist:
        try:
            subgenre = Subgenre.objects.get(name=name)
            return HttpResponsePermanentRedirect('/subgenre/' + subgenre.slug + '/')
        except:
            raise Http404

def subgenres(request):
    scifi = Subgenre.objects.filter(genre=0)
    fantasy = Subgenre.objects.filter(genre=1)
    horror = Subgenre.objects.filter(genre=2)
    return render_to_response('subgenres.htm', {'scifi': scifi, 'fantasy': fantasy, 'horror': horror } )

def view_people(request):
    persons = Person.objects.all()
    return render_to_response('people.htm', {'persons': persons})

def recalculate_score(person):
    score = 0
    roles = Role.objects.filter(person=person)
    for role in roles:
        try:
            if role.show.movie:
                score += 20
        except:
            pass
        try:
            if role.show.tvseries:
                score += role.show.tvseries.num_episodes
        except:
            pass
        try:
            if role.show.episode:
                score += 1
        except:
            pass
    score += Episode.objects.filter(director=person).count()
    score += Episode.objects.filter(writers=person).count()
    score += Episode.objects.filter(producer=person).count()
    score += TVSeries.objects.filter(creators=person).count()
    score += TVSeries.objects.filter(theme_composer=person).count()
    score += Movie.objects.filter(director=person).count()
    score += Movie.objects.filter(producer=person).count()
    score += Movie.objects.filter(writers=person).count()
    score += Movie.objects.filter(music_by=person).count()
    score += Book.objects.filter(authors=person).count()
    person.score = score
    person.save()

def register(request):
    user = User()
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST, instance=user)
        if user_form.is_valid():
            # Check for email address already used.
            email = request.POST['email']
            duplicate_email = User.objects.filter(email=email)
            if duplicate_email:
                return render_to_response('register.htm', {'user_form': user_form, 'error': 'Error: Email address is already in use.'}, context_instance=RequestContext(request))
            # Require both passswords to match.
            pwd1 = request.POST['password1']
            pwd2 = request.POST['password2']
            if pwd1 != pwd2:
                return render_to_response('register.htm', {'user_form': user_form, 'error': 'Error: Passwords do not match.'}, context_instance=RequestContext(request))
            user = user_form.save()
            user.set_password( request.POST['password1'] )
            user.save()
            return HttpResponseRedirect("/")
        else:
            return render_to_response('register.htm', {'user_form': user_form}, context_instance=RequestContext(request))
    else:
        user_form = RegistrationForm(instance=user)
        return render_to_response('register.htm', {'user_form': user_form }, context_instance=RequestContext(request))

def account(request):
    if not request.user.is_authenticated():
        return HttpResponseForbidden()
    ratings = Rating.objects.filter(user=request.user)
    return render_to_response('account.htm', {'user': request.user, 'ratings': ratings })

def rate_show(request, id, rating):
    user = None
    if not request.user.is_authenticated():
        return HttpResponseForbidden()
    user = request.user
    show = Show.objects.get(id=id)
    rating = int(rating)
    if rating < 1 or rating > 10:
        raise Http404
    my_rating = None
    try:
        my_rating = Rating.objects.get(show=show, user=request.user)
    except ObjectDoesNotExist:
        pass
    if my_rating:
        my_rating.rating = rating
        my_rating.ip_address = request.META['REMOTE_ADDR']
        my_rating.save()
    else:
        new_rating = Rating()
        new_rating.user = user
        new_rating.rating = rating
        new_rating.ip_address = request.META['REMOTE_ADDR']
        new_rating.show = show
        new_rating.save()

    try:
        if show.episode:
            return HttpResponseRedirect("/show/" + show.tvseries.name + "/episode/" + show.slug + "/")
    except:
        pass

    try:
        if show.movie:
            return HttpResponseRedirect("/movie/" + show.name + "/")
    except:
        pass

    return HttpResponseRedirect("/show/" + show.name + "/")

