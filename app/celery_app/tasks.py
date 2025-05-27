from celery import Celery

celery = Celery(__name__, config_source='celeryconfig')

@celery.task
def compute_response_score(response_id: int):
    print(f"Scoring response {response_id}...")
    # Imagine real scoring logic here