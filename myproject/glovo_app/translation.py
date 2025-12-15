from .models import  (Category, Store, Contact,
                       Address, StoreMenu,Product)
from modeltranslation.translator import TranslationOptions,register



@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Store)
class ProductTranslationOptions(TranslationOptions):
    fields = ('store_name','description',)


@register(Contact)
class ProductTranslationOptions(TranslationOptions):
    fields = ('contact_name',)


@register(Address)
class ProductTranslationOptions(TranslationOptions):
    fields = ('address_name',)

@register(StoreMenu)
class ProductTranslationOptions(TranslationOptions):
    fields = ('menu_name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name','product_description')
