from service import XOSService
from services.vbbu.models import VBBUService

class XOSMVBBUService(XOSService):
    provides = "tosca.nodes.VBBUService"
    xos_model = VBBUService
    copyin_props = ["view_url", "icon_url", "enabled", "published", "public_key", "private_key_fn", "versionNumber"]

