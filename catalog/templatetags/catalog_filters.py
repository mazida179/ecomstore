from django import template
import locale

#Creating custom filter
register = template.Library()

@register.filter(name='currency')
def currency(value):
    try:
        locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')
    except:
        locale.setlocale(locale.LC_ALL, '')
    loc = locale.localeconv()

    return locale.currency(value, loc['currency_symbol'], grouping=True)

    