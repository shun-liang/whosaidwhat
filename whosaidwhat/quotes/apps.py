from django.apps import AppConfig


class QuotesConfig(AppConfig):
    name = 'whosaidwhat.quotes'
    verbose_name = "Quotes"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
