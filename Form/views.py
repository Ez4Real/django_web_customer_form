from re import template
from django.shortcuts import render
from .models import Form
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EditForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import datetime


class FormListView(generic.ListView):
    
    model = Form
    paginate_by = 25
    
    
class FormDetailView(generic.DetailView):
    
    model = Form


class FormCreate(CreateView):
    
    model = Form
    fields = '__all__'
    initial={'open_orded': datetime.datetime.now(),
             'password': 'Без паролю',
             'is_notified': 'NO',
             'is_repairable': 'NO'}

class FormDelete(DeleteView):
    model = Form
    success_url = reverse_lazy('forms')


def index(request):
    
    num_forms = Form.objects.all().count()
    num_forms_repairable = Form.objects.filter(is_repairable__exact='YES').count()
    num_asus = Form.objects.filter(manufacture__manufacture__iexact = 'asus').count()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    return render(
        request,
        'index.html',
        context={'num_forms':num_forms,
                 'num_forms_repairable':num_forms_repairable,
                 'num_asus': num_asus,
                 'num_visits': num_visits},
    )
   
    
def printing_form(request, pk):
    
    form = get_object_or_404(Form, pk=pk)
    
    return render(request, 'form/form_print.html', {'form': form})

def edit_form(request, pk):
    
    form = get_object_or_404(Form, pk=pk)
    
    if request.method == 'POST':
        
        edited_form = EditForm(request.POST)
        
        if edited_form.is_valid():
            
            form.last_name = edited_form.cleaned_data['last_name']
            form.first_name = edited_form.cleaned_data['first_name']
            form.phone = edited_form.cleaned_data['phone']
            form.model = edited_form.cleaned_data['model']
            form.password = edited_form.cleaned_data['password']
            form.reason = edited_form.cleaned_data['reason']
            form.serial_number = edited_form.cleaned_data['serial_number']
            form.is_repairable = edited_form.cleaned_data['is_repairable']
            form.price = edited_form.cleaned_data['price']
            form.is_notified = edited_form.cleaned_data['is_notified']
            form.took_the_order = edited_form.cleaned_data['took_the_order']
            # form.open_order = edited_form.cleaned_data['open_order']
            form.done_order = edited_form.cleaned_data['done_order']
            form.equipment = edited_form.cleaned_data['equipment']
            form.save()
            
            return HttpResponseRedirect(reverse('forms'))
        
    else: 
        edited_form = EditForm(initial={'last_name': form.last_name, 
                                        'first_name': form.first_name, 
                                        'phone': form.phone,
                                        'model': form.model,
                                        'password': form.password,
                                        'serial_number': form.serial_number,
                                        'is_repairable': form.is_repairable,
                                        'reason': form.reason,
                                        'price': form.price,
                                        'is_notified': form.is_notified,
                                        'took_the_order': form.took_the_order,
                                        # 'open_order': form.open_order,
                                        'done_order': form.done_order,
                                        'equipment': form.equipment,
                                        })
        
    return render(request, 'form/edit_form.html', {'form': form, 'editedform': edited_form})
    