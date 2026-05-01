# Import qilish
from celery import Celery
import redis

# Redis uchun klon yaratish
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Celery uchun klon yaratish
app = Celery('tasks', broker='redis://localhost:6379/0')

# Background task yaratish
@app.task
def background_task(task_id, task_name, task_data):
    # Taskni Redisga yuklash
    redis_client.hset('tasks', task_id, task_name)
    redis_client.hset('tasks', f'{task_id}:data', task_data)

    # Taskni bajarganligini ko'rsatish
    print(f'Task {task_id} {task_name} bajarildi')

# Background taskni bajarganligini tekshirish
def check_task_status(task_id):
    # Task mavjudligini tekshirish
    if redis_client.hexists('tasks', task_id):
        # Task mavjud bo'lsa, uning holatini olish
        task_status = redis_client.hget('tasks', task_id)
        return task_status
    else:
        return None

# Background taskni bajarganligini tekshirish
def get_task_status(task_id):
    # Task mavjudligini tekshirish
    if redis_client.hexists('tasks', task_id):
        # Task mavjud bo'lsa, uning holatini olish
        task_status = redis_client.hget('tasks', task_id)
        return task_status
    else:
        return None

# Background taskni bajarganligini tekshirish
def get_task_data(task_id):
    # Task mavjudligini tekshirish
    if redis_client.hexists('tasks', task_id):
        # Task mavjud bo'lsa, uning ma'lumotlarini olish
        task_data = redis_client.hget(f'{task_id}:data')
        return task_data
    else:
        return None
```

Kodda quyidagilar mavjud:

1.  Redis uchun klon yaratish
2.  Celery uchun klon yaratish
3.  Background task yaratish
4.  Background taskni Redisga yuklash
5.  Background taskni bajarganligini ko'rsatish
6.  Background taskni bajarganligini tekshirish
7.  Background taskning holatini olish
8.  Background taskning ma'lumotlarini olish
