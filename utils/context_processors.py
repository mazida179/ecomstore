from catalog.models import Category
from ecomstore import settings

def ecomstore(request):
    """context processor for makeing the following variables
    available everywhere.

    """
    return {
        'active_categories':Category.objects.filter(is_active=True),
        'site_name':settings.SITE_NAME,
        'meta_keywords':settings.META_KEYWORDS,
        'meta_description':settings.META_DESCRIPTION,
        'request':request
    }