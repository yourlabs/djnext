from appwatch.management.commands.appwatch import Command


class Command(Command):
    def handle(self, *args, **options):
        args = ['pages:./pages', 'components:./pages/components']
        super().handle(*args, **options)
