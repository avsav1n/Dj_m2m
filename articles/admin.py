from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Article


class ArticleInlineFormset(BaseInlineFormSet):
    def clean(self) -> None:
        main_flag = False
        for form in self.forms:
            if form.cleaned_data.get('DELETE'):
                continue
            if (form_flag := form.cleaned_data.get('is_main')) and main_flag:
                raise ValidationError('Основным может быть только один раздел')
            main_flag = main_flag or form_flag
        return super().clean()

class ArticleInline(admin.TabularInline):
    model = Article.tags.through
    extra = 0
    formset = ArticleInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text_column', 'published_at']
    inlines = [ArticleInline]

    @admin.display(description='Содержание', ordering='text')
    def text_column(self, obj):
        return obj.text[:100] + '...' if len(obj.text) > 100 else ''

    
