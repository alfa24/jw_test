from main.services.contents import inc_counter_by_page
from project.celery import app as celery


@celery.task(queue="low")
def inc_counter_by_page_task(page_id: int) -> None:
    """Задача, увеличивающая счетчик контента, связанного с страницей."""
    inc_counter_by_page(page_id)
