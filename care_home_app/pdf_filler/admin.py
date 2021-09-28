from django.contrib import admin

from pdf_filler.models import FillablePDF


class FillablePDFInline(admin.StackedInline):
    model = FillablePDF
    can_delete = False


admin.site.register(FillablePDF)
