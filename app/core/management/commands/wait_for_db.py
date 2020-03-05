from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

import time


class Command(BaseCommand):
    """Django command to pause execution until db is available"""

    def handle(self, *args, **kwargs):
        self.stdout.write("waiting for dababase...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write("DB unavailable, waiting for 1 second....")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available !"))
