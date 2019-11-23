from tornado.web import RequestHandler

from celery_app.tasks import heavy_cpu_task


class CpuBoundController(RequestHandler):
    async def get(self):
        heavy_cpu_task.delay(130000)
        self.write("Task executing on Celery, returning a result without blocking")
