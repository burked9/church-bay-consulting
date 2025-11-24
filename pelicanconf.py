AUTHOR = 'Daniel Burke'
SITENAME = 'Church Bay Consulting'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Navigation
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Home', '/'),
    ('About', '/pages/about-us.html'),
    ('Projects', '/pages/projects.html'),
    ('Contact', '/pages/contact.html'),
)

# Theme
THEME = 'theme'

# Contact Details (Custom variables)
EMAIL = 'burked9@gmail.com'
PHONE = '+353 871933409'
ADDRESS = 'Clonrush Whitegate Co. Clare, Ireland'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Static paths
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
