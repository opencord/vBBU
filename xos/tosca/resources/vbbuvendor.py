from xosresource import XOSResource
from core.models import Tenant
from services.vbbu.models import VBBUVendor

class XOSVBBUVendor(XOSResource):
    provides = "tosca.nodes.VBBUVendor"
    xos_model = VBBUVendor
    name_field = None
    copyin_props = ( "name",)

    def get_xos_args(self, throw_exception=True):
        args = super(XOSVBBUVendor, self).get_xos_args()

        tenant_name = self.get_requirement("tosca.relationships.VendorOfTenant", throw_exception=throw_exception)
        if tenant_name:
            args["provider_tenant"] = self.get_xos_object(Tenant, throw_exception=throw_exception, name=tenant_name)

        return args

    def get_existing_objs(self):
        args = self.get_xos_args(throw_exception=False)
        provider_tenant = args.get("provider", None)
        if provider_tenant:
            return [ self.get_xos_object(provider_tenant=provider_tenant) ]
        return []

    def postprocess(self, obj):
        pass

    def can_delete(self, obj):
        return super(XOSVBBUVendor, self).can_delete(obj)
