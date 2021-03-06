class SOL6ConfigDefault:
    """
    TOML can load a configutation file from a string using toml.loads, so instead of reworking
    a lot of the internal code, we're just going to copy the default config here and load it normally.
    """

    config = """
    # Sol6 Path configurations
[sol6]
    # **********
    # ** VNFD **
    # **********
    vnfd                        = "vnfd"
    vnfd_id                     = ["vnfd", "id"]
    vnfd_provider               = ["vnfd", "provider"]
    vnfd_product                = ["vnfd", "product-name"]
    vnfd_software_ver           = ["vnfd", "software-version"]
    vnfd_ver                    = ["vnfd", "version"]
    vnfd_info_name              = ["vnfd", "product-info-name"]
    vnfd_info_desc              = ["vnfd", "product-info-description"]
    vnfd_vnfm_info              = ["vnfd", "vnfm-info"]

    vnfd_config_props           = ["vnfd", "configurable-properties"]
    vnfd_config_autoheal        = ["vnfd_config_props", "is-auto-heal-enabled"]
    vnfd_config_autoscale       = ["vnfd_config_props", "is-auto-scalable-enabled"]
    vnfd_config_additional      = ["vnfd_config_props", "additional-configurable-property"]
    vnfd_config_add_elem        = ["vnfd_config_additional", "{}"]
    vnfd_config_add_key         = ["vnfd_config_add_elem", "key"]
    vnfd_config_add_value       = ["vnfd_config_add_elem", "value"]


    PROTOCOLS_PREFIX_VAL        = "etsi-nfv-descriptors:"
    VALID_PROTOCOLS_VAL         = ["ethernet", "ipv4", "ipv6", "mpls", "odu2", "pseudo-wire"]
    VALID_DISK_FORMATS_VAL      = ["qcow2", "raw", "vmdk"]
    VALID_CONTAINER_FORMATS_VAL = ["aki", "ami", "ari", "bare", "docker", "ova", "ovf"]
    VALID_AFF_SCOPES_VAL        = ["nfvi-node", "nfvi-pop", "zone", "zone-group"]
    VALID_STORAGE_TYPES_VAL     = ["ephemeral-storage", "root-storage", "swap-storage", "cisco-etsi-nfvo:volume-storage"]

    # ********************************
    # ** Virtual Compute Descriptor **
    # ********************************
    vnfd_virt_compute_desc_base = ["vnfd", "virtual-compute-desc"]
    vnfd_virt_compute_desc      = ["vnfd_virt_compute_desc_base", "{}"]
    vnfd_vcd_id                 = ["vnfd_virt_compute_desc", "id"]
    vnfd_vcd_flavor_name        = ["vnfd_virt_compute_desc", "cisco-etsi-nfvo-sol1-vnfd-extensions:flavour-name-variable"]
    vnfd_virtual_cpu            = ["vnfd_virt_compute_desc", "virtual-cpu"]
    vnfd_vcd_cpu_num            = ["vnfd_virtual_cpu", "num-virtual-cpu"]
    vnfd_vcd_cpu_clock          = ["vnfd_virtual_cpu", "clock"]
    vnfd_vcd_cpu_arch           = ["vnfd_virtual_cpu", "cpu-architecture"]
    vnfd_vcd_cpu_oversub        = ["vnfd_virtual_cpu", "oversubscription-policy"]
    vnfd_vcd_vdu_cpu_req        = ["vnfd_virtual_cpu", "vdu-cpu-requirements"]
    vnfd_vcd_mem                = ["vnfd_virt_compute_desc", "virtual-memory"]
    vnfd_vcd_mem_size           = ["vnfd_vcd_mem", "size"]

    # ********************************
    # ** Virtual Storage Descriptor **
    # ********************************
    vnfd_virt_storage_desc_base = ["vnfd", "virtual-storage-desc"]
    vnfd_virt_storage_desc      = ["vnfd_virt_storage_desc_base", "{}"]
    vnfd_virt_storage_id        = ["vnfd_virt_storage_desc", "id"]
    vnfd_virt_storage_type      = ["vnfd_virt_storage_desc", "type-of-storage"]
    VIRT_STORAGE_DEFAULT_VAL    = "root-storage"
    vnfd_virt_storage_size      = ["vnfd_virt_storage_desc", "size-of-storage"]
    vnfd_virt_storage_sw_image  = ["vnfd_virt_storage_desc", "sw-image-desc"]

    # ***********************
    # ** Deployment Flavor **
    # ***********************
    deployment_flavor           = ["vnfd", "df"]
    df_id                       = ["deployment_flavor", "id"]
    df_desc                     = ["deployment_flavor", "description"]
    df_inst_level_default       = ["deployment_flavor", "default-instantiation-level"]
    df_vdu_profile_list         = ["deployment_flavor", "vdu-profile"]
    df_vdu_profile              = ["df_vdu_profile_list", "{}"]
    df_vdu_prof_id              = ["df_vdu_profile", "id"]
    df_vdu_prof_inst_min        = ["df_vdu_profile", "min-number-of-instances"]
    df_vdu_prof_inst_max        = ["df_vdu_profile", "max-number-of-instances"]
    df_vdu_prof_aff_group_list  = ["df_vdu_profile", "affinity-or-anti-affinity-group"]
    df_vdu_prof_aff_group       = ["df_vdu_prof_aff_group_list", "{}"]
    df_vdu_prof_aff_group_id    = ["df_vdu_prof_aff_group", "id"]

    # -- Instantiation Level
    df_inst_level_base          = ["deployment_flavor", "instantiation-level"]
    df_inst_level               = ["df_inst_level_base", "{}"]
    df_inst_level_id            = ["df_inst_level", "id"]
    df_inst_level_desc          = ["df_inst_level", "description"]
    df_inst_level_vdu_level_lst = ["df_inst_level", "vdu-level"]
    df_inst_level_vdu_level     = ["df_inst_level_vdu_level_lst", "{}"]
    df_inst_level_vdu_vdu       = ["df_inst_level_vdu_level", "vdu-id"]
    df_inst_level_vdu_num       = ["df_inst_level_vdu_level", "number-of-instances"]
    # -- Scaling Info
    df_inst_scaling_info_list   = ["df_inst_level", "scaling-info"]
    df_inst_scaling_info        = ["df_inst_scaling_info_list", "{}"]
    df_inst_scaling_aspect      = ["df_inst_scaling_info", "id"]
    df_inst_scaling_level       = ["df_inst_scaling_info", "scale-level"]

    df_scale_aspect_list        = ["deployment_flavor", "scaling-aspect"]
    df_scale_aspect             = ["df_scale_aspect_list", "{}"]
    df_scale_aspect_id          = ["df_scale_aspect", "id"]
    df_scale_aspect_name        = ["df_scale_aspect", "name"]
    df_scale_aspect_desc        = ["df_scale_aspect", "description"]
    df_scale_aspect_max_level   = ["df_scale_aspect", "max-scale-level"]
    df_scale_aspect_delta_det   = ["df_scale_aspect", "aspect-delta-details"]
    df_scale_aspect_deltas_list = ["df_scale_aspect_delta_det", "deltas"]
    df_scale_aspect_deltas      = ["df_scale_aspect_deltas_list", "{}"]
    df_scale_aspect_deltas_id   = ["df_scale_aspect_deltas", "id"]
    df_scale_aspect_vdu_delta_lst = ["df_scale_aspect_deltas", "vdu-delta"]
    df_scale_aspect_vdu_delta   = ["df_scale_aspect_vdu_delta_lst", "{}"]
    df_scale_aspect_vdu_id      = ["df_scale_aspect_vdu_delta", "id"]
    df_scale_aspect_vdu_num     = ["df_scale_aspect_vdu_delta", "number-of-instances"]
    df_scale_aspect_no_delta_VAL = "unknown"

    df_affinity_group_list      = ["deployment_flavor", "affinity-or-anti-affinity-group"]
    df_affinity_group           = ["df_affinity_group_list", "{}"]
    df_affinity_id              = ["df_affinity_group", "id"]
    df_affinity_type            = ["df_affinity_group", "type"]
    df_affinity_scope           = ["df_affinity_group", "scope"]
    affinity_VAL                = "affinity"
    anti_affinity_VAL           = "anti-affinity"

    df_lcm_config               = ["deployment_flavor", "lcm-operations-configuration"]
    df_lcm_heal_config          = ["df_lcm_config", "heal-vnf-op-config"]
    df_heal_param_base          = ["df_lcm_heal_config", "parameter"]
    df_heal_param               = ["df_heal_param_base", "{}"]
    df_heal_param_key           = ["df_heal_param", "key"]
    df_heal_param_value         = ["df_heal_param", "value"]

    # ****************************
    # ** Virtual/External Links **
    # ****************************
    virt_link_desc_base         = ["vnfd", "int-virtual-link-desc"]
    virt_link_desc              = ["virt_link_desc_base", "{}"]
    virt_link_desc_id           = ["virt_link_desc", "id"]
    virt_link_desc_desc         = ["virt_link_desc", "description"]
    virt_link_desc_conn         = ["virt_link_desc", "connectivity-type"]
    virt_link_desc_protocol     = ["virt_link_desc_conn", "layer-protocol"]
    virt_link_desc_flow         = ["virt_link_desc_conn", "flow-pattern"]
    virt_link_desc_add_params   = ["virt_link_desc", "cisco-etsi-nfvo-sol1-vnfd-extensions:additional-sol1-parameters"]
    virt_link_desc_cidr         = ["virt_link_desc_add_params", "cidr-variable"]
    virt_link_desc_dhcp         = ["virt_link_desc_add_params", "dhcp-enabled-variable"]

    ext_cpd_base                = ["vnfd", "ext-cpd"]
    ext_cpd                     = ["ext_cpd_base", "{}"]
    ext_cpd_id                  = ["ext_cpd", "id"]
    ext_cpd_protocol            = ["ext_cpd", "layer-protocol"]
    ext_cpd_virt_link           = ["ext_cpd", "int-virtual-link-desc"]
    ext_cpd_role                = ["ext_cpd", "role"]
    ext_cpd_vdu                 = ["ext_cpd", "int-cpd"]
    ext_cpd_vdu_id              = ["ext_cpd_vdu", "vdu-id"]
    ext_cpd_int_cpd_id          = ["ext_cpd_vdu", "cpd"]


    #ext_cpd_int_cpd             = ["ext_cpd", "int-cpd"]
    #ext_cpd_icp_vdu             = ["ext_cpd_int_cpd", "vdu"]
    #ext_cpd_icp_cpd             = ["ext_cpd_int_cpd", "cpd"]


    # *********
    # ** VDU **
    # *********
    vdus                        = ["vnfd", "vdu"]
    vdu                         = ["vdus", "{}"]
    vdu_name                    = ["vdu", "name"]
    vdu_desc                    = ["vdu", "description"]
    vdu_id                      = ["vdu", "id"]
    vdu_boot_order_list         = ["vdu", "boot-order"]
    vdu_boot_order              = ["vdu_boot_order_list", "{}"]
    vdu_boot_key                = ["vdu_boot_order", "key"]
    vdu_boot_value              = ["vdu_boot_order", "value"]
    vdu_vc_desc_list            = ["vdu", "virtual-compute-desc"]
    vdu_vc_desc                 = ["vdu_vc_desc_list", "{}"]
    vdu_vs_desc_list            = ["vdu", "virtual-storage-desc"]
    vdu_vs_desc                 = ["vdu_vs_desc_list", "{}"]
    vdu_sw_image_desc_list      = ["vdu", "sw-image-desc"]
    vdu_sw_image_desc           = ["vdu_sw_image_desc_list", "{}"]

    vdu_artifact                = ["vdu", "cisco-etsi-nfvo:artifact"]

    # ********************************
    # ** Internal Connection Points **
    # ********************************
    int_cpd_list                = ["vdu", "int-cpd"]
    int_cpd                     = ["int_cpd_list", "{}"]
    int_cpd_id                  = ["int_cpd", "id"]
    int_cpd_layer_prot          = ["int_cpd", "layer-protocol"]
    int_cpd_virt_link_desc      = ["int_cpd", "int-virtual-link-desc"]
    int_cpd_role                = ["int_cpd", "role"]
    int_cpd_interface_id        = ["int_cpd", "cisco-etsi-nfvo:interface-id"]
    int_cpd_management          = ["int_cpd", "cisco-etsi-nfvo:management"]
    int_cpd_management_VAL      = "[null]"
    int_cpd_additional_params   = ["int_cpd", "cisco-etsi-nfvo-sol1-vnfd-extensions:additional-sol1-parameters"]
    int_cpd_allowed_addr        = ["int_cpd_additional_params", "allowed-address-variable"]
    int_cpd_ip_addr             = ["int_cpd_additional_params", "ip-address-variable"]
    int_cpd_security            = ["int_cpd_additional_params", "security-group-variable"]

    KEY_VIRT_LINK_MGMT_VAL      = "VIM_NETWORK_MANAGEMENT-VL"
    KEY_VIRT_LINK_MGMT_PROT_VAL = "etsi-nfv-descriptors:ipv4"
    KEY_VIRT_LINK_ORCH_VAL      = "VIM_NETWORK_ORCHESTRATION-VL"
    KEY_VIRT_LINK_ORCH_PROT_VAL = "etsi-nfv-descriptors:ipv4"
    KEY_EXT_CP_MGMT_VAL         = "VIM_NETWORK_MANAGEMENT"
    KEY_EXT_CP_MGMT_PROT_VAL    = "etsi-nfv-descriptors:ipv4"
    KEY_EXT_CP_ORCH_VAL         = "VIM_NETWORK_ORCHESTRATION"
    KEY_EXT_CP_ORCH_PROT_VAL    = "etsi-nfv-descriptors:ipv4"

    # *******************************
    # ** Software Image Descriptor **
    # *******************************
    sw_img_desc_base            = ["vnfd", "sw-image-desc"]
    sw_img_desc                 = ["sw_img_desc_base", "{}"]
    sw_id                       = ["sw_img_desc", "id"]
    sw_name                     = ["sw_img_desc", "name"]
    sw_image_name_var           = ["sw_img_desc", "cisco-etsi-nfvo-sol1-vnfd-extensions:image-name-variable"]
    sw_version                  = ["sw_img_desc", "version"]
    sw_checksum                 = ["sw_img_desc", "checksum"]
    sw_checksum_hash            = ["sw_checksum", "hash"]
    sw_checksum_algorithm       = ["sw_checksum", "algorithm"]
    sw_checksum_algorithm_VAL    = "sha-256"
    sw_container_format         = ["sw_img_desc", "container-format"]
    sw_disk_format              = ["sw_img_desc", "disk-format"]
    sw_min_disk                 = ["sw_img_desc", "min-disk"]
    sw_min_ram                  = ["sw_img_desc", "min-ram"]
    sw_size                     = ["sw_img_desc", "size"]
    sw_image                    = ["sw_img_desc", "image"]
    sw_operating_sys            = ["sw_img_desc", "operating-system"]
    sw_supp_virt_environ        = ["sw_img_desc", "supported-virtualization-environment"]

    # **************
    # ** Artifact **
    # **************
    artifact_base               = ["vnfd", "cisco-etsi-nfvo:artifact"]
    artifact                    = ["artifact_base", "{}"]
    artifact_id                 = ["artifact", "id"]
    artifact_dest               = ["artifact", "destination-name"]
    artifact_url                = ["artifact", "url"]
    artifact_variable_list      = ["artifact", "variable"]
    artifact_variable           = ["artifact_variable_list", "{}"]
    artifact_variable_id        = ["artifact_variable", "id"]
    artifact_variable_desc      = ["artifact_variable", "description"]
    artifact_checksum           = ["artifact", "checksum"]
    artifact_hash               = ["artifact_checksum", "hash"]
    artifact_algorithm          = ["artifact_checksum", "algorithm"]
    artifact_hash_DUMMY_VAL     = "9af30fce37a4c5c831e095745744d6d2"
    artifact_algorithm_DUMMY_VAL = "etsi-nfv-descriptors:sha-256"

    """
