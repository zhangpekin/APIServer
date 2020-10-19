import os

from .common import Common
from .development import Development
from .production import Production

conf: Common = None

if os.environ.get('FLASK_ENV') == 'production':
    conf = Production
else:
    conf = Development
