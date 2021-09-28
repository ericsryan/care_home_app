from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import pdfrw

from . import models


def fill_pdf(request):
    ANNOT_KEY = '/Annots'
    ANNOT_FIELD_KEY = '/T'
    ANNOT_VAL_KEY = '/V'
    ANNOT_RECT_KEY = '/Rect'
    SUBTYPE_KEY = '/Subtype'
    WIDGET_SUBTYPE_KEY = '/Widget'
    data_dict = {
        'name_of_facility': 'Ryan Family Care Home',
        'facility_file_number': '123456789',
        'address': '12285 Rio Oso Rd.',
        'city_state_zip': 'Auburn, CA 95602',
        'telephone_number': '(530) 613-4535',
        'clients_involved_1': 'Goober Fish',
        'date_occured_1': '12/12/2021',
        'age_1': 34,
        'sex_1': 'M',
        'date_of_admission_1': '01/01/2020',
        'describe_incident': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum',
        'medical_treatment_necessary_checkbox_yes': 'Yes',
        'agencies_aps_cps_checkbox': 'Yes',
        'unauthorized_absence': 'Yes',
        'aca_other': 'Yes'
    }
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
