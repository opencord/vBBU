
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


from services.vbbu.models import VBBUComponent, MCORDService
from xosresource import XOSResource

class XOSVBBUComponent(XOSResource):
    provides = "tosca.nodes.VBBUComponent"
    xos_model = VBBUComponent
    copyin_props = ["s1u_tag", "s1mme_tag", "rru_tag", "display_message"]
    name_field = None

    def get_xos_args(self, throw_exception=True):
        args = super(XOSVBBUComponent, self).get_xos_args()

        provider_name = self.get_requirement("tosca.relationships.MemberOfService", throw_exception=throw_exception)
        if provider_name:
            args["provider_service"] = self.get_xos_object(MCORDService, throw_exception=throw_exception, name=provider_name)

        return args

    def get_existing_objs(self):
        args = self.get_xos_args(throw_exception=False)
        provider_service = args.get("provider", None)
        if provider_service:
            return [ self.get_xos_object(provider_service=provider_service) ]
        return []

    def postprocess(self, obj):
        pass

    def can_delete(self, obj):
        return super(XOSVBBUComponent, self).can_delete(obj)

