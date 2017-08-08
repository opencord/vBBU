
# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import sys
from django.db.models import Q, F
from services.vbbu.models import MCORDService, VBBUComponent
from synchronizers.base.SyncInstanceUsingAnsible import SyncInstanceUsingAnsible

parentdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, parentdir)

class SyncVBBUComponent(SyncInstanceUsingAnsible):

    provides = [VBBUComponent]

    observes = VBBUComponent

    requested_interval = 0

    template_name = "sync_vbbu.yaml"

    service_key_name = "/opt/xos/configurations/mcord/mcord_private_key"

    def __init__(self, *args, **kwargs):
        super(SyncVBBUComponent, self).__init__(*args, **kwargs)

    def fetch_pending(self, deleted):

        if (not deleted):
            objs = VBBUComponent.get_tenant_objects().filter(
                Q(enacted__lt=F('updated')) | Q(enacted=None), Q(lazy_blocked=False))
        else:

            objs = VBBUComponent.get_deleted_tenant_objects()

        return objs

    def get_extra_attributes(self, o):
        return {"display_message": o.display_message, "s1u_tag": o.s1u_tag, "s1mme_tag": o.s1mme_tag, "rru_tag": o.rru_tag}
