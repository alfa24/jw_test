import os

from kombu import Exchange, Queue

from .base import REDIS_URL, TIME_ZONE

CELERY_BROKER_URL = REDIS_URL
CELERY_BROKER_TRANSPORT_OPTIONS = {
    "is_secure": True,
}

CELERY_ACCEPT_CONTENT = {"json"}
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_ALWAYS_EAGER = os.getenv("CELERY_TASK_ALWAYS_EAGER", False) in [
    "true",
    "True",
]

CELERY_TASK_DEFAULT_QUEUE = "default"
CELERY_QUEUES = (
    Queue("low", Exchange("low"), routing_key="low"),
    Queue("default", Exchange("default"), routing_key="default"),
    Queue("high", Exchange("high"), routing_key="high"),
)

CELERY_BEAT_SCHEDULE = {}
