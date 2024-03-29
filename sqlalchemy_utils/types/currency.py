import six
from sqlalchemy import types

from ..primitives import Currency
from .scalar_coercible import ScalarCoercible


class CurrencyType(ScalarCoercible, types.TypeDecorator):
    """
    Changes :class:`.Currency` objects to a string representation on the way in
    and changes them back to :class:`.Currency` objects on the way out.

    In order to use CurrencyType you need to install Babel_ first.

    .. _Babel: http://babel.pocoo.org/

    ::


        from sqlalchemy_utils import CurrencyType, Currency


        class User(Base):
            __tablename__ = 'user'
            id = sa.Column(sa.Integer, autoincrement=True)
            name = sa.Column(sa.Unicode(255))
            currency = sa.Column(CurrencyType)


        user = User()
        user.currency = Currency('USD')
        session.add(user)
        session.commit()

        user.currency  # Currency('USD')
        user.currency.name  # US Dollar

        str(user.currency)  # US Dollar
        user.currency.symbol  # $



    CurrencyType is scalar coercible::


        user.currency = 'US'
        user.currency  # Currency('US')
    """

    impl = types.String(3)
    python_type = Currency
    cache_ok = True

    def __init__(self, *args, **kwargs):
        super(CurrencyType, self).__init__(*args, **kwargs)

    def process_bind_param(self, value, dialect):
        if isinstance(value, Currency):
            return value.code
        elif isinstance(value, six.string_types):
            return value

    def process_result_value(self, value, dialect):
        if value is not None:
            return Currency(value)

    def _coerce(self, value):
        if value is not None and not isinstance(value, Currency):
            return Currency(value)
        return value
