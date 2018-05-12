import filecmp
import imp
import time
import os
import sys
import shutil

from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.management.base import BaseCommand, CommandError

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler


def walk_django():
    paths = []
    for app_name in settings.INSTALLED_APPS:
        parts = app_name.split('.')
        mod = parts.pop(0)
        mod_path = imp.find_module(mod)[1]
        path = mod_path
        if parts:
            path += '/' + os.path.join(*parts)
        path += '/static'
        if os.path.isdir(path):
            for root, directories, filenames in os.walk(path):
                if 'pages' in directories:
                    paths.append(os.path.join(root, 'pages'))
    return paths

def run():
    if not os.path.isdir('pages'):
        os.makedirs('pages')

    for d in walk_django():
        report = filecmp.dircmp('pages', d)
        report.report()
        for missing in report.right_only:
            target = os.path.join('pages', missing)
            source = os.path.join(d, missing)
            print('CP', source, ' -> ', target)
            shutil.copyfile(source, target)

        for changed in report.diff_files:
            target = os.path.join('pages', changed)
            source = os.path.join(d, changed)
            print('!CP', source, ' -> ', target)
            shutil.copyfile(source, target)

    for root, directories, filenames in os.walk('pages'):
        for f in filenames:
            path = 'pages/' + f
            result = finders.find(path, all=True)
            if not result:
                print('RM', path)
                os.unlink(os.path.join(root, f))


class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        run()


class Command(BaseCommand):
    def handle(self, *args, **options):
        run()

        self.observers = {}
        for d in walk_django():
            self.observers[d] = Observer()
            self.observers[d].schedule(Handler(), d, recursive=True)
            self.observers[d].start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            for observer in self.observers.values():
                observer.stop()
        for observer in self.observers.values():
            observer.join()