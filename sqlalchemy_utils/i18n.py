from .exceptions import ImproperlyConfigured

try:
    import babel
    import babel.dates
except ImportError:
    babel = None


def get_locale():
    try:
        return babel.Locale("en")
    except AttributeError:
        # As babel is optional, we may raise an AttributeError accessing it
        raise ImproperlyConfigured(
            "Could not load get_locale function using Babel. Either "
            "install Babel or make a similar function and override it "
            "in this module."
        )
