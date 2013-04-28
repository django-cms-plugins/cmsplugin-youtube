
Name: Modified cmsplugin-youtube, support for templates
Description: YouTube embedding for django-cms

Original source code
Download: http://bitbucket.org/xenofox/cmsplugin-youtube/

Requirements:
- django-cms-2.0.0 final
- django: 1.1.1
+ requirements for django-cms-2.0

Last tested with:
- django-cms-2.4.0 final
- django: 1.4.2

Setup
- make sure requirements are installed and properly working
- add cmsplugin_youtube to python path
- add 'cmsplugin_youtube' to INSTALLED_APPS
- run 'python manage.py syncdb'

Settings
CMS_YOUTUBE_DEFAULT_AUTOPLAY    (Default False)
CMS_YOUTUBE_DEFAULT_WIDTH       (Default 425)
CMS_YOUTUBE_DEFAULT_HEIGHT      (Default 344)
CMS_YOUTUBE_DEFAULT_BORDER      (Default False)
CMS_YOUTUBE_DEFAULT_FULLSCREEN  (Default True)
CMS_YOUTUBE_DEFAULT_LOOP        (Default False)
CMS_YOUTUBE_DEFAULT_RELATED     (Default False)
CMS_YOUTUBE_DEFAULT_HIGHQUALITY (Default False)

TODO:
- Add tests
- Add translations

