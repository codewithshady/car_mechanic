from django.contrib import admin


from .models import *


class Services_detailsInline(admin.StackedInline):
    model = Services_details

class ServicesAdmin(admin.ModelAdmin):
    inlines = [Services_detailsInline]
    
    class Meta:
        model=Services




# Register your models here.
admin.site.register(Banner)
admin.site.register(About)
admin.site.register(Services,ServicesAdmin)
admin.site.register(Mission)
admin.site.register(Testimonial)
admin.site.register(Career)
admin.site.register(Enquiry)
admin.site.register(Gallery)





