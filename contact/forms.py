from django import forms
from django.contrib.auth import get_user_model
from .models import Contact

class ContactForm(forms.ModelForm):
	name = forms.CharField(
	        widget=forms.TextInput(
	                attrs={
	                    "id": "name"
	                }
	                )
	        )
	email    = forms.EmailField(
	        widget=forms.EmailInput(
	                attrs={
	                    "id": "email"
	                }
	                )
	        )
	message  = forms.CharField(
	        widget=forms.Textarea(
	            attrs={
	                'id': 'message',
	                "rows": '5',
			"style": 'resize: none;'
	                }
	            )
	)
	class Meta:
		model = Contact
		fields = ["name","email", "message"]
	def clean_name(self):
		name = self.cleaned_data.get('name')
		if name:
			if not name.strip():
				raise forms.ValidationError("Error")
		return name

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if email:
			if not email.strip():
				raise forms.ValidationError("Error")
		return email
	def clean_message(self):
		message = self.cleaned_data.get('message')
		if message:
			if not message.strip():
				raise forms.ValidationError("Error")
		return message

