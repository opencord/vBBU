tosca_definitions_version: tosca_simple_yaml_1_0

# compile this with "m4 vbbu.m4 > vbbu.yaml"

# include macros
include(macros.m4)

node_types:
    tosca.nodes.VBBUService:
        derived_from: tosca.nodes.Root
        description: >
            VBBU Service
        capabilities:
            xos_base_service_caps
        properties:
            xos_base_props
            xos_base_service_props
            
    tosca.nodes.VBBUTenant:
        derived_from: tosca.nodes.Root
        description: >
            VBBU Tenant
        properties:
            xos_base_tenant_props

    tosca.nodes.VBBUVendor:
        derived_from: tosca.nodes.Root
        description: >
            VBBU Vendor
        properties:
            name:
                type: string
                required: true

    tosca.relationships.VendorOfTenant:
           derived_from: tosca.relationships.Root
           valid_target_types: [ tosca.capabilities.xos.VBBUTenant ]

