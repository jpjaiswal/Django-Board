import hashlib
import urllib
from django import template
from django.utils.safestring import mark_safe
from urllib.parse import urlencode
 
register = template.Library()
 
# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
#def gravatar_url(email, size=40):
def gravatar(user):
    email = user.email.lower().encode('utf-8')
    default = 'mm'
    size = 256
    url = 'https://www.gravatar.com/avatar/{md5}?{params}'.format(
        md5=hashlib.md5(email).hexdigest(),
        params=urllib.parse.urlencode({'d': default, 's': str(size)})
    )
    return url
   
   
   
   
    #default = "https://example.com/static/images/defaultavatar.jpg"
    
    
    #default = "c:/dev/myproject/venv/myproject/static/defaultavatar.jpg"
   # return "https://www.gravatar.com/avatar/%s?%s" % (hashlib.md5(email.encode()).hexdigest(), urllib.parse.urlencode({'d':default, 's':str(size)}))
 
# return an image tag with the gravatar
# TEMPLATE USE:  {{ email|gravatar:150 }}
#@register.filter
#def gravatar(email, size=40):
   # url = gravatar_url(email, size)
   # return mark_safe('<img src="%s" height="%d" width="%d">' % (url, size, size))

  