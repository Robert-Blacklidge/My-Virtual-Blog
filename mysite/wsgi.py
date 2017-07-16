





import os
import sys


path = os.path.expanduser('~/My-Virtual-Blog')
if path not in sys.path:
    sys.path.append(path)
<<<<<<< HEAD

#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
#application = get_wsgi_application()
=======

#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = get_wsgi_application()
#application = StaticFilesHandler(get_wsgi_application())

>>>>>>> 8bdc53b8d1924adb99b3916a986b7c31cd41ebcb
