from django.apps import AppConfig


class CandidatesConfig(AppConfig):
    name = 'whosaidwhat.candidates'
    verbose_name = "Candidates"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
