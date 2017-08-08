from core.models.plcorebase import *
from models_decl import VBBUService_decl
from models_decl import VBBUTenant_decl

from core.models import Service, TenantWithContainer
from django.db import transaction
from django.db.models import *

class VBBUService(VBBUService_decl):
   class Meta:
        proxy = True 

class VBBUTenant(VBBUTenant_decl):
   class Meta:
        proxy = True 

   def __init__(self, *args, **kwargs):
       vbbuservice = VBBUService.get_service_objects().all()
       if vbbuservice:
           self._meta.get_field(
                   "provider_service").default = vbbuservice[0].id
       super(VBBUTenant, self).__init__(*args, **kwargs)

   def save(self, *args, **kwargs):
       super(VBBUTenant, self).save(*args, **kwargs)
       # This call needs to happen so that an instance is created for this
       # tenant is created in the slice. One instance is created per tenant.
       model_policy_vbbutenant(self.pk)

   def delete(self, *args, **kwargs):
       # Delete the instance that was created for this tenant
       self.cleanup_container()
       super(VBBUTenant, self).delete(*args, **kwargs)

def model_policy_vbbutenant(pk):
    # This section of code is atomic to prevent race conditions
    with transaction.atomic():
        # We find all of the tenants that are waiting to update
        tenant = VBBUTenant.objects.select_for_update().filter(pk=pk)
        if not tenant:
            return
        # Since this code is atomic it is safe to always use the first tenant
        tenant = tenant[0]
        tenant.manage_container()
