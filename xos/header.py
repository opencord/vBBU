# models.py -  vBBU Models

from core.models import Service, TenantWithContainer
from django.db import transaction
from django.db.models import *

SERVICE_NAME = 'vbbuservice'
SERVICE_NAME_VERBOSE = 'vBBU Service'
SERVICE_NAME_VERBOSE_PLURAL = 'vBBU Services'
TENANT_NAME_VERBOSE = 'vBBU Tenant'
TENANT_NAME_VERBOSE_PLURAL = 'vBBU Tenants'
