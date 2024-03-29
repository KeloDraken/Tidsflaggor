from config.settings.base import DEBUG

if DEBUG:
    from config.settings.development import *
else:
    from config.settings.production import *