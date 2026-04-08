AUTHOR = 'Roberto Aguilera'
SITENAME = "Roberto Aguilera's Blog"
SITEURL = ""
THEME = './themes/robert_theme'

PATH = "content"

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

AUTHOR_ABOUT = "Soy un ingeniero en desarrollo de software al que le apasiona compartir conocimiento y crear soluciones digitales. Cuento con amplia experiencia en el desarrollo de aplicaciones móviles, páginas web, aplicaciones de escritorio y todo tipo de soluciones de software que se adapten e impulsen tu negocio."



# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True

SUMMARY_MAX_PARAGRAPHS = 1

# Enable Pygments for syntax highlighting
PYGMENTS_RST_OPTIONS = {'class': 'highlight'}
# Optional: Use CSS classes instead of inline styles
PYGMENTS_USE_CLASSES = True

LIQUID_TAGS = ["img", "literal", "video", "youtube",
               "vimeo", "include_code"]

STATIC_PATHS = ['images', 'code']
CODE_DIR = 'code'


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

