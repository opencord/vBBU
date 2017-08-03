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
            service_message:
                type: string
                required: false
            
    tosca.nodes.VBBUTenant:
        derived_from: tosca.nodes.Root
        description: >
            VBBU Tenant
        properties:
            xos_base_tenant_props
            tenant_message:
                type: string
                required: false

