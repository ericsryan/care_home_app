import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import pdfrw

from . import forms
from . import models
from profiles.models import Client


def fill_LIC624(request, client_pk):
    ANNOT_KEY = '/Annots'
    ANNOT_FIELD_KEY = '/T'
    ANNOT_VAL_KEY = '/V'
    ANNOT_RECT_KEY = '/Rect'
    SUBTYPE_KEY = '/Subtype'
    WIDGET_SUBTYPE_KEY = '/Widget'
    client = Client.objects.get(pk=client_pk)
    if request.method == 'POST':
        form = forms.LIC624Form(data=request.POST)
        if form.is_valid():
            data_dict = {
                'name_of_facility': 'Ryan Family Care Home',
                'facility_file_number': '317002780',
                'address': '12285 Rio Oso Rd.',
                'city_state_zip': 'Auburn, CA 95602',
                'telephone_number': '(530) 269-1892',
                'clients_involved_1': f'{client.first_name} {client.last_name}',
                'age_1': client.age,
                'sex_1': client.sex[0],
                'date_of_admission_1': client.admission_date.strftime('%m/%d/%Y'),
            }
            for field in form:
                data_dict[field.name] = form.cleaned_data[field.name]
                if form.cleaned_data[field.name] == True:
                    data_dict[field.name] = 'Yes'
                if type(form.cleaned_data[field.name]) == datetime.date:
                    data_dict[field.name] = form.cleaned_data[field.name].strftime('%m/%d/%Y')
            fillable_pdf = models.FillablePDF.objects.get(name='LIC624')
            template_pdf = pdfrw.PdfReader(fillable_pdf.file.url[1:])
            for page in template_pdf.pages:
                annotations = page[ANNOT_KEY]
                for annotation in annotations:
                    if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                        if annotation[ANNOT_FIELD_KEY]:
                            key = annotation[ANNOT_FIELD_KEY][1:-1]
                            if key in data_dict.keys():
                                if type(data_dict[key]) == bool:
                                    if data_dict[key] == True:
                                        annotation.update(pdfrw.PdfDict(
                                            AS=pdfrw.PdfName('Yes')))
                                else:
                                    annotation.update(
                                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                                    )
                                    annotation.update(pdfrw.PdfDict(AP=''))
            pdfrw.PdfWriter().write('media/fillable_pdfs/LIC624output.pdf', template_pdf)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = forms.LIC624Form()
    return render(request, 'pdf_filler/fill_LIC624.html', {'form': form})
