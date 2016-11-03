from services.vbbu.models import MCORDService
from service import XOSService

class XOSMCORDService(XOSService):
    provides = "tosca.nodes.MCORDService"
    xos_model = MCORDService
    copyin_props = ["view_url", "icon_url", "enabled", "published", "public_key",
                    "private_key_fn", "versionNumber",
                    ]

