from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from users.forms import RegistrationForm
from users.models import Utilizator


class Register(CreateView):
    model = Utilizator
    form_class = RegistrationForm
    template_name = "accounts/registration_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        user_kwdict = dict(username=self.object.email, email=self.object.email, first_name=self.object.first_name,
                           last_name=self.object.last_name, is_active=True)
        user = User.objects.create(**user_kwdict)
        user.set_password(form.cleaned_data['parola'])
        user.save()

        return super(Register, self).form_valid(form)

    def get_success_url(self):
        return reverse("badges:create_badge")