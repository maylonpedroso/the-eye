from django.contrib import admin

from .models import ClientCredential


@admin.register(ClientCredential)
class ClientCredentialAdmin(admin.ModelAdmin):
    fields = ('name', 'client_id', 'secret_key')
    readonly_fields = ('client_id', 'secret_key')
