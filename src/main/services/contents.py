from django.db.models import F

from main.models import PageBlock


def inc_counter_by_page(page_id: int) -> None:
    """Увеличивает счетчик контента, связанного с страницей."""

    content_models = PageBlock.get_content_class_models()
    for model in content_models:
        model.objects.filter(blocks__page_id=page_id).distinct('pk').update(counter=F('counter') + 1)
