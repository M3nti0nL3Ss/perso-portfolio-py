from django.shortcuts import render,redirect
from .models import Project
from skills.models import Skill
from django.views.generic.base import TemplateView
from contact.forms import ContactForm


class Home(TemplateView):
	template_name = "portfolio/home.html"
	projects = Project.objects.all()
	skills = Skill.objects.all()
	form = ContactForm()
	msg_sent = False
	def get(self, request, *args, **kwargs):
	    if 'sent' in request.session:
	    	self.msg_sent = True
	    	del request.session['sent']
	    	request.session.modified = True
	    else:
	    	self.msg_sent = False
	    return render(request, self.template_name, {'projects': self.projects, 
	    	'skills':self.skills, 
	    	'skills':self.skills, 
	    	'form': self.form , 
	    	'msg_sent':self.msg_sent})
	def post(self, request, *args, **kwargs):
		contact_form = ContactForm(request.POST or None)
		if contact_form.is_valid():
			contact = contact_form.save()
			context = {'projects': self.projects, 
	    	'skills':self.skills, 
	    	'skills':self.skills, 
	    	'form': self.form , 
	    	'msg_sent':self.msg_sent}
			request.session['sent'] = 'msg_sent'
			return redirect("home")
		return self.render_to_response(context)