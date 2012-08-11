from django.utils.translation import ungettext_lazy, ugettext as _
from django.http import HttpResponse
from demo.forms import DemoForm
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    message = "DEMO"
    string_count = 2
    plural_message = ungettext_lazy("This is %d string",
            "These are %d strings", string_count)  % string_count
    form = DemoForm()
    return render_to_response('home.html',
            {
                'message': message,
                'plural_message': plural_message,
                'greetings': _("Greetings from view."),
                'form': form
            },
            context_instance=RequestContext(request)
    )

