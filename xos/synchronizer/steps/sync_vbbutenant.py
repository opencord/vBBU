import os
import sys
from django.db.models import Q, F
# from services.vbbu.models import MCORDService, VBBUTenant
from synchronizers.new_base.modelaccessor import *
from synchronizers.new_base.SyncInstanceUsingAnsible import SyncInstanceUsingAnsible

parentdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, parentdir)

class SyncVBBUTenant(SyncInstanceUsingAnsible):
    provides = [VBBUTenant]

    observes = VBBUTenant

    requested_interval = 0

    template_name = "vbbutenant_playbook.yaml"

    service_key_name = "/opt/xos/configurations/mcord/mcord_private_key"

    def __init__(self, *args, **kwargs):
        super(SyncVBBUTenant, self).__init__(*args, **kwargs)

    def fetch_pending(self, deleted):
        if (not deleted):
            objs = VBBUTenant.get_tenant_objects().filter(
                Q(enacted__lt=F('updated')) | Q(enacted=None), Q(lazy_blocked=False))
        else:
            objs = VBBUTenant.get_deleted_tenant_objects()

        return objs

