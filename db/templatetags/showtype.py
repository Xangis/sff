from django import template

register = template.Library()

@register.filter
def showtype(value):
    name = value.__class__.__name__
    if name is 'TVSeries':
        return 'show'
    if name is 'Episode':
        return 'episode'
    if name is 'Movie':
        return 'movie'
    if name is 'Show':
        try:
            if value.tvseries:
                return 'show'
        except:
            pass
        try:
            if value.episode:
                return 'episode'
        except:
            pass
        try:
            if value.movie:
                return 'movie'
        except:
            pass
    return name
