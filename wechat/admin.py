from django.contrib import admin
from .models import Magnet, NodeSs

class magnetAdmin(admin.ModelAdmin):
    list_display = ('mgTitle', 'mgLable')
    search_fields = ['mgTitle', 'mgLable', 'id']

class nodessAdmin(admin.ModelAdmin):
    list_display = ('node_name', 'node_server', 'node_method', 'node_info', 'node_status')

admin.site.register(Magnet, magnetAdmin)
admin.site.register(NodeSs, nodessAdmin)