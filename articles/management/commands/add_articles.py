from typing import Any
from django.core.management import BaseCommand

from articles.models import Tag


class Command(BaseCommand):
    help = 'Заполняет таблицу Tag'

    def handle(self, *args: Any, **options: Any) -> str | None:
        tags = [
            'Культура',
            'Город',
            'Здоровье',
            'Наука',
            'Космос',
            'Международные отношения',
        ]
        tag_objects = [Tag(name=tag) for tag in tags]
        Tag.objects.bulk_create(tag_objects)