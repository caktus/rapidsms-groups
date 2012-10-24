from django.db import models

from rapidsms_groups.utils import format_number


class ContactExtra(models.Model):
    """ Abstract model to extend the RapidSMS Contact model """

    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=32, blank=True)
    title = models.CharField(max_length=64, blank=True)

    def save(self, **kwargs):
        if hasattr(self, 'patient_set') and not self.patient_set.all().exists():
            self.name = "%s %s" % (self.first_name, self.last_name)
        super(ContactExtra, self).save(**kwargs)

    class Meta:
        abstract = True

    @property
    def formatted_phone(self):
        return format_number(self.phone)
