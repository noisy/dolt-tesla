from django.db.models import TextField, Model, TextChoices, CharField


class InformationSource(Model):
    class Meta:
        db_table = "information_source"

    url = TextField()
    timestamp = TextField(null=True, default=None, blank=True)
    ipfs_mirror_url = TextField(null=True, default=None, blank=True)
    type = CharField(max_length=32, choices=TextChoices('source type', 'website video audio').choices)

    def __str__(self):
        return self.url
