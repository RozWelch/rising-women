from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form class for the contact form
    """
    class Meta:
        model = Contact
        fields = [
            'contact_fullname',
            'contact_email',
            'expertise_areas',
            'contact_website',
            'contact_linkedin',
            'contact_bio',
            'why_mentor',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
