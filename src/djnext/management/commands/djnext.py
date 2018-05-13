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


def run_path(d, target):
    print('FOR ::::: ', d)
    report = filecmp.dircmp(target, d)
    for missing in report.right_only:
        source = os.path.join(d, missing)
        if source.split('/')[0].startswith('.'):
            continue
        target = os.path.join(target, missing)
        print('CP', source, ' -> ', target)
        if os.path.isfile(source):
            shutil.copyfile(source, target)
        elif os.path.isdir(source):
            shutil.copytree(source, target)
        else:
            print('WTF is', source, 'you poney?!')

    for changed in report.diff_files:
        target_file = os.path.join(target, changed)
        source = os.path.join(d, changed)
        print('!CP', source, ' -> ', target_file)
        shutil.copyfile(source, target_file)

    for e in report.common_dirs:
        run_path(
            os.path.join(d, e),
            os.path.join(target, e)
        )


def run():
    if not os.path.isdir('pages'):
        os.makedirs('pages')

    paths = walk_django()
    while paths:
        d = paths.pop()
        run_path(d, 'pages')

    for root, directories, filenames in os.walk('pages'):
        print('FOR :::', root)
        for f in filenames:
            path = os.path.join(root, f)
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
