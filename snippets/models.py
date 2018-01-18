from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)



class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=100, blank=True, default='123')
    email = models.CharField(max_length=100, blank=True, default='email')

    class Meta:
        ordering = ('created',)

    # owner = models.ForeignKey('auth.User', related_name='users', on_delete=models.CASCADE)
    # highlighted = models.TextField()

    # def save(self, *args, **kwargs):
    #     """
    #     Use the `pygments` library to create a highlighted HTML
    #     representation of the code snippet.
    #     """
    #     lexer = get_lexer_by_name(self.language)
    #     linenos = self.linenos and 'table' or False
    #     options = self.username and {'username': self.username} or {}
    #     formatter = HtmlFormatter(style=self.style, linenos=linenos,
    #                               full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)
    #     super(User, self).save(*args, **kwargs)

class Map(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    lat = models.CharField(max_length=100, blank=True, default='')
    lon = models.CharField(max_length=100, blank=True, default='')
    addr = models.CharField(max_length=100, blank=True, default='')
    amenity = models.CharField(max_length=100, blank=True, default='')
    cuisine = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    opening_hours = models.CharField(max_length=100, blank=True, default='')
    website = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)


class LocationInfo(models.Model):
    latitude = models.IntegerField(blank=True, default='')
    longitude = models.IntegerField(blank=True, default='')
    name = models.IntegerField(blank=True, default='')