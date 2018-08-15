from django import forms
from . import models


class EditForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = [
            'first_name', 'last_name',
            'email', 'date_of_birth', 'bio', 'avatar'
        ]


class EditFormWithValidation(EditForm):
    confirm_email = forms.EmailField()

    def clean(self):
        cleaned_data = super(EditForm, self).clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")

        if email and confirm_email:
            if email != confirm_email:
                raise forms.ValidationError("Emails do not match.")

        return cleaned_data

    class Meta(EditForm.Meta):
        fields = EditForm.Meta.fields + ['confirm_email']
