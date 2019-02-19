"""
These are automatically used without having to update anything else.
The TOSCA variables are mapped to the SOL6 ones, they must have the same names.
The program does not attempt to map variables beginning with '_'
"""
from mapping_v2 import V2Mapping, MapElem
from dict_utils import *


class TOSCA:
    """
    The proper paths for the tosca values
    Variable names are in mostly-sol6 format. Their values are TOSCA yaml strings.
    """
    _top            = "topology_template"
    _nodes          = _top + ".node_templates"
    _vnf            = _nodes + ".vnf"
    _properties     = _vnf + ".properties"
    _policies       = "tosca.policies"
    _nfv_policies   = _policies + ".nvf"
    from_input      = "get_input"
    # --------------------------------
    # Deployment Flavor
    df_id                           = _properties + ".flavour_id"
    df_desc                         = _properties + ".flavour_description"

    # --------------------------------
    # Non-mapped variables
    inputs = "topology_template.inputs"

    # These all need to be formatted with the proper node before use
    vdu                         = _nodes + ".{}"
    vdu_cap_props               = vdu + ".capabilities.virtual_compute.properties"
    vdu_num_cpu                 = vdu_cap_props + ".virtual_cpu.num_virtual_cpu"
    vdu_mem_size                = vdu_cap_props + ".virtual_memory.virtual_mem_size"
    vdu_conf_props              = vdu + ".properties.configurable_properties"
    vdu_vim_flavor              = vdu_conf_props + ".additional_vnfc_configurable_properties" \
                                                   ".vim_flavor"
    vdu_type                    = "cisco.nodes.nfv.Vdu.Compute"

    vdu_profile                 = vdu + ".properties.vdu_profile"
    vdu_profile_min             = vdu_profile + ".min_number_of_instances"
    vdu_profile_max             = vdu_profile + ".max_number_of_instances"

    # These also need to be formatted before use
    virtual_block_storage       = _nodes + ".{}"
    vbs_props                   = virtual_block_storage + ".properties"
    vbs_size                    = vbs_props + ".virtual_block_storage_data.size_of_storage"
    vbs_type                    = "cisco.nodes.nfv.Vdu.VirtualBlockStorage"

    virtual_link_mapping        = _nodes + ".{}"
    _vlm_props                  = virtual_link_mapping + ".properties"
    vlm_desc                    = _vlm_props + ".description"
    vlm_protocols               = _vlm_props + ".connectivity_type.layer_protocols"
    vlm_type                    = "tosca.nodes.nfv.VnfVirtualLink"

    _instan_level               = "{}"
    _instan_level_properties    = _instan_level + ".properties"
    instan_level_nfv            = "{}.properties.levels"
    instan_level_nfv_desc       = instan_level_nfv + ".{}.description"
    instan_levels               = _instan_level_properties + ".levels"
    instan_level_num            = instan_levels + ".{}.number_of_instances"
    instan_level_targets        = _instan_level + ".targets"

    scaling_aspects             = "{}.properties.aspects"
    scaling_aspect              = scaling_aspects + ".{}"
    scaling_aspect_desc         = scaling_aspect + ".description"
    scaling_aspect_max_level    = scaling_aspect + ".max_scale_level"

    instan_level_type           = _nfv_policies + ".VduInstantiationLevels"
    instan_level_nfv_type       = _nfv_policies + ".InstantiationLevels"
    scaling_aspect_type         = _nfv_policies + ".ScalingAspects"
    anti_affinity_type          = _nfv_policies + ".AntiAffinityRule"
    sub_link_types              = ["virtual_link"]

    substitution_mappings       = _top + ".substitution_mappings.requirements"
    connection_point            = _nodes + ".{}"
    cp_properties               = connection_point + ".properties"
    cp_management               = cp_properties + ".management"
    cp_req                      = connection_point + ".requirements"
    cp_virt_binding             = cp_req + ".virtual_binding"
    cp_virt_link                = cp_req + ".virtual_link"
    cp_virt_link_id_key         = "id"
    cp_virt_link_desc_key       = "id"

    group_affinity_type         = "tosca.groups.nfv.PlacementGroup"
    # TODO: Handle Affinity as well
    group_aff_members_key       = "members"
    policy_aff_targets_key      = "targets"
    policy_aff_type_key         = "type"
    policy_aff_scope_key        = "properties.scope"
    cp_link_key                 = "link_type"


class SOL6:
    """
    The proper paths for SOL6 yang locations
    The values are SOL6 paths
    """
    _vnfd                           = "vnfd"
    vnfd                            = _vnfd
    # We build the VDUs out of place, then put in at the end, so we don't need the full path
    _vdu                            = "{}"

    # value_key is for if we have a default value we want to assign, the program can handle
    # assigning it automatically for basic keys
    # The variable must be postfixed with the value of 'value_key'
    value_key = "_VAL"
    # Deployment Flavor
    _deployment_flavor               = _vnfd + ".df"
    df_id                            = _deployment_flavor + ".id"
    df_desc                          = _deployment_flavor + ".description"
    df_affinity_group                = _deployment_flavor + ".affinity-or-anti-affinity-group"
    df_affinity_group_id             = df_affinity_group + ".id"
    df_affinity_group_type           = df_affinity_group + ".type"
    df_affinity_group_scope          = df_affinity_group + ".scope"

    # VDU profiles are a list and will be built then placed in
    df_vdu_profile                   = _deployment_flavor + ".vdu-profile"
    df_vdu_p_id                      = df_vdu_profile + ".id"
    df_vdu_p_min                     = df_vdu_profile + ".min-number-of-instances"
    df_vdu_p_max                     = df_vdu_profile + ".max-number-of-instances"

    df_vdu_p_affinity_group          = df_vdu_profile + ".affinity-or-anti-affinity-group"
    df_vdu_p_aff_id                  = df_vdu_p_affinity_group + ".id"

    df_inst_level                    = _deployment_flavor + ".instantiation-level"
    _df_inst_vdu_level               = df_inst_level + ".vdu-level"
    df_inst_level_id                 = df_inst_level + ".id"
    df_inst_level_desc               = df_inst_level + ".description"
    df_inst_level_vdu                = _df_inst_vdu_level + ".vdu"
    df_inst_level_num                = _df_inst_vdu_level + ".number-of-instances"
    df_inst_scale_info               = df_inst_level + ".scaling-info"
    df_inst_scale_aspect             = df_inst_scale_info + ".aspect"
    df_inst_scale_level              = df_inst_scale_info + ".scale-level"

    df_scaling_aspect                = _deployment_flavor + ".scaling-aspect"
    df_scaling_id                    = df_scaling_aspect + ".id"
    df_scaling_name                  = df_scaling_aspect + ".name"
    df_scaling_desc                  = df_scaling_aspect + ".description"
    df_scaling_max_scale             = df_scaling_aspect + ".max-scale-level"

    @staticmethod
    def df_anti_affinity_value(x):
        return "anti-affinity" if x == TOSCA.anti_affinity_type else "affinity"

    # --------------------------------

    inst_def_level                   = _deployment_flavor + ".default-instantiation-level"
    inst_def_level_VAL               = "default"

    # --------------------------------
    # Non-mapped variables
    # ** Virtual Compute Descriptors **
    # Note: these are relative paths, as they are built out of place, then put into the dict later
    virtual_comp_desc               = _vnfd + ".virtual-compute-descriptor"
    vcd_id                          = virtual_comp_desc + ".id"
    vcd_flavor_name                 = virtual_comp_desc + ".flavor-name-variable"
    flavor_name_key                 = "flavor-name"
    vcd_virtual_memory              = virtual_comp_desc + ".virtual-memory.size"
    vcd_virtual_cpu                 = virtual_comp_desc + ".virtual-cpu.num-virtual-cpus"

    virtual_storage_desc            = _vnfd + ".virtual-storage-descriptor"
    vsd_id                          = virtual_storage_desc + ".id"
    vsd_type_storage                = virtual_storage_desc + ".type-of-storage"
    vsd_type_storage_value          = "lvm"  # This can't be read from the yaml at this point
    vsd_size_storage                = virtual_storage_desc + ".size-of-storage"

    virtual_link_desc               = _vnfd + ".virtual-link-descriptor"
    vld_id                          = virtual_link_desc + ".id"
    vld_desc                        = virtual_link_desc + ".description"
    vld_protocol                    = virtual_link_desc + ".connectivity-type.layer-protocol"

    ext_cp                          = _vnfd + ".ext-cpd"
    ext_cp_id                       = ext_cp + ".id"
    ext_cp_int_cp                   = ext_cp + ".int-virtual-link-desc"
    ext_cp_layer_protocol           = ext_cp + ".layer_protocol"
    ext_cp_layer_protocol_value     = "etsi-nfv:Ethernet"

    int_cp                          = _vdu + ".int-cpd"
    int_cp_id                       = int_cp + ".id"
    int_cp_link_desc                = int_cp + ".int-virtual-link-desc"

    ext_cp_mgmt_id                  = "VIM_NETWORK_MANAGEMENT"
    ext_cp_orch_id                  = "VIM_NETWORK_ORCHESTRATION"

    # -- Internal --
    cp_mgmt_key                 = "vim_management"
    cp_vim_orch_key             = "vim_orchestration"


class TOSCAv2:
    """
    Second version of the definitions
    """
    topology_template               = "topology_template"
    node_template                   = topology_template + ".node_templates"
    desc                            = "description"
    policies                        = topology_template + ".policies"
    inputs                          = "topology_template.inputs"
    input_key                       = "get_input"

    # **************
    # ** Metadata **
    # **************
    vnf                             = node_template + ".vnf"
    vnf_prop                        = vnf + ".properties"
    vnf_desc_id                     = vnf_prop + ".descriptor_id"
    vnf_desc_ver                    = vnf_prop + ".descriptor_version"
    vnf_provider                    = vnf_prop + ".provider"
    vnf_product_name                = vnf_prop + ".product_name"
    vnf_software_ver                = vnf_prop + ".software_version"
    vnf_product_info_name           = vnf_prop + ".product_info_name"
    vnf_vnfm_info                   = vnf_prop + ".vnfm_info"

    # *********
    # ** VDU **
    # *********
    vdu                             = node_template + ".{}"
    vdu_identifier                  = ["type", "cisco.nodes.nfv.Vdu.Compute"]
    vdu_props                       = vdu + ".properties"
    vdu_name                        = vdu_props + ".name"
    vdu_boot                        = vdu_props + ".boot_order"
    vdu_desc                        = vdu_props + ".description"
    vdu_conf_props                  = vdu_props + ".configurable_properties." \
                                                  "additional_vnfc_configurable_properties"
    vdu_vim_flavor                  = vdu_conf_props + ".vim_flavor"
    vdu_cap_props                   = vdu + ".capabilities.virtual_compute.properties"
    vdu_virt_cpu_num                = vdu_cap_props + ".virtual_cpu.num_virtual_cpu"
    vdu_virt_mem_size               = vdu_cap_props + ".virtual_memory.virtual_mem_size"

    vdu_profile                     = vdu_props + ".vdu_profile"
    vdu_prof_inst_min               = vdu_profile + ".min_number_of_instances"
    vdu_prof_inst_max               = vdu_profile + ".max_number_of_instances"

    # *********************************
    # ** Internal Connectiion Points **
    # *********************************
    @staticmethod
    def int_cp_mgmt(item):
        """Return if the current cp is assigned to management or not"""
        return key_exists(item, "properties.management") and \
            get_path_value("properties.management", item[get_dict_key(item)], must_exist=False)

    int_cpd                         = node_template + ".{}"
    int_cpd_identifier              = ["type", "cisco.nodes.nfv.VduCp"]
    int_cpd_mgmt_identifier         = ["type", "cisco.nodes.nfv.VduCp", int_cp_mgmt.__func__]
    int_cpd_props                   = int_cpd + ".properties"
    int_cpd_virt_binding            = int_cpd + ".requirements.virtual_binding"
    int_cpd_virt_link               = int_cpd + ".requirements.virtual_link"
    int_cpd_layer_prot              = int_cpd_props + ".layer_protocols"

    @staticmethod
    def virt_filter(item):
        # Make sure that the virtual storage block we get has the {}.properties.sw_image_data field
        return key_exists(item, "properties.sw_image_data")

    virt_storage                    = node_template + ".{}"
    virt_storage_identifier         = ["type", "cisco.nodes.nfv.Vdu.VirtualBlockStorage",
                                       virt_filter.__func__]
    virt_props                      = virt_storage + ".properties"
    virt_artifacts                  = virt_storage + ".artifacts"
    virt_vsb                        = virt_props + ".virtual_block_storage_data"
    virt_size                       = virt_props + ".size_of_storage"
    sw_image_data                   = virt_props + ".sw_image_data"
    sw_name                         = sw_image_data + ".name"
    sw_version                      = sw_image_data + ".version"
    sw_checksum                     = sw_image_data + ".checksum"
    sw_container_fmt                = sw_image_data + ".container_format"
    sw_disk_fmt                     = sw_image_data + ".disk_format"
    sw_min_disk                     = sw_image_data + ".min_disk"
    sw_size                         = sw_image_data + ".size"
    sw_image_file                   = virt_artifacts + ".sw_image.file"

    # ** Deployment Flavor **

    df_id                           = vnf_prop + ".flavour_id"
    df_desc                         = vnf_prop + ".flavour_description"

    def_inst_level                  = policies + ".instantiation_levels"
    def_inst_key                    = "default"
    inst_level_identifier           = ["type", "tosca.policies.nfv.VduInstantiationLevels"]


class SOL6v2:
    """
    Second version of the definitions
    """
    # **********
    # ** VNFD **
    # **********
    vnfd                            = "vnfd"
    vnfd_id                         = vnfd + ".id"
    vnfd_provider                   = vnfd + ".provider"
    vnfd_product                    = vnfd + ".product-name"
    vnfd_software_ver               = vnfd + ".software-version"
    vnfd_ver                        = vnfd + ".version"
    vnfd_info_name                  = vnfd + ".product-info-name"
    vnfd_info_desc                  = vnfd + ".product-info-description"
    vnfd_vnfm_info                  = vnfd + ".vnfm-info"
    vnfd_virt_compute_desc          = vnfd + ".virtual-compute-descriptor.{}"
    vnfd_vcd_id                     = vnfd_virt_compute_desc + ".id"
    vnfd_vcd_flavor_name            = vnfd_virt_compute_desc + ".flavor-name-variable"
    vnfd_vcd_cpu_num                = vnfd_virt_compute_desc + ".virtual-cpu.num-virtual-cpu"
    vnfd_vcd_mem_size               = vnfd_virt_compute_desc + ".virtual-memory.virtual-memory-size"

    # ***********************
    # ** Deployment Flavor **
    # ***********************
    deployment_flavor               = vnfd + ".df"
    df_id                           = deployment_flavor + ".id"
    df_desc                         = deployment_flavor + ".description"
    df_vdu_profile                  = deployment_flavor + ".vdu-profile.{}"
    df_vdu_prof_id                  = df_vdu_profile + ".id"
    df_vdu_prof_inst_min            = df_vdu_profile + ".min-number-of-instances"
    df_vdu_prof_inst_max            = df_vdu_profile + ".max-number-of-instances"
    df_inst_level                   = deployment_flavor + ".instantiation-level"
    df_inst_id                      = df_inst_level + ".id"

    # ****************************
    # ** Virtual/External Links **
    # ****************************
    virt_link_desc_id               = vnfd + ".int-virtual-link-desc.{}.id"

    ext_cpd                         = vnfd + ".ext-cpd.{}"
    ext_cpd_id                      = ext_cpd + ".id"
    ext_cpd_virt_link               = ext_cpd + ".int-virtual-link-desc"

    # *********
    # ** VDU **
    # *********
    vdus                            = vnfd + ".vdu"
    vdu                             = vdus + ".{}"
    vdu_name                        = vdu + ".name"
    vdu_desc                        = vdu + ".description"
    vdu_id                          = vdu + ".id"
    vdu_boot_order                  = vdu + ".boot-order"
    vdu_boot_key                    = vdu_boot_order + ".key"
    vdu_boot_value                  = vdu_boot_order + ".value"
    vdu_vc_desc                     = vdu + ".virtual-compute-desc.{}"

    # *********************************
    # ** Internal Connection Points **
    # *********************************
    int_cpd                         = vdu + ".int-cpd.{}"
    int_cpd_id                      = int_cpd + ".id"
    int_cpd_layer_prot              = int_cpd + ".layer-protocol"
    int_cpd_virt_link_desc          = int_cpd + ".int-virtual-link-desc"

    KEY_VIRT_LINK_MGMT              = "CP_MGMT"
    KEY_VIRT_LINK_ORCH              = "CP_ORCH"
    KEY_EXT_CP_MGMT                 = "CP_EXT_MGMT"
    KEY_EXT_CP_ORCH                 = "CP_EXT_ORCH"

    # *******************************
    # ** Software Image Descriptor **
    # *******************************
    sw_img_desc                     = vnfd + ".sw-image-desc.{}"
    sw_id                           = sw_img_desc + ".id"
    sw_name                         = sw_img_desc + ".name"
    sw_image_name_var               = sw_img_desc + ".image_name_variable"
    sw_version                      = sw_img_desc + ".version"
    sw_checksum                     = sw_img_desc + ".checksum"
    sw_container_format             = sw_img_desc + ".container-format"
    sw_disk_format                  = sw_img_desc + ".disk-format"
    sw_min_disk                     = sw_img_desc + ".min-disk"
    sw_size                         = sw_img_desc + ".size"
    sw_image                        = sw_img_desc + ".image"


class V2Map(V2Mapping):
    """

    """
    FLAG_BLANK                      = ""
    # Pass this flag if you want to set the value with the key and not the value
    FLAG_KEY_SET_VALUE              = "KSV"
    # Will remove all non-numeric characters
    FLAG_ONLY_NUMBERS               = "NUMBERS"
    FLAG_ONLY_NUMBERS_FLOAT         = "NUMBERS_FLOAT"
    FLAG_APPEND_LIST                = "APPENDLIST"

    mapping = {}

    def __init__(self, dict_tosca, dict_sol6):
        super().__init__(dict_tosca, dict_sol6)

        T = TOSCAv2
        S = SOL6v2

        # Generate VDU map
        vdu_map = self.generate_map(T.node_template, T.vdu_identifier)

        sw_map = self.generate_map(T.node_template, T.virt_storage_identifier)

        # This list has the VDUs the flavors are attached to
        vdu_vim_flavors = self.get_items_from_map(T.vdu_vim_flavor, vdu_map, dict_tosca,
                                                  link_list=True)
        # *** VDU Flavors ***
        # vim_flavors = [VDU, {"get_input": FLAVOR_NAME}], so get the dicts
        vim_flavors = [x[1] for x in vdu_vim_flavors]
        vim_flavors = self.get_input_values(vim_flavors, T.inputs, dict_tosca)

        vim_flavors = [{vdu_vim_flavors[i][0]: get_dict_key(item)} for i, item in
                       enumerate(vim_flavors)]

        # We might have duplicate values in the dictionary. Use a reverse dict and get the unique
        # elements
        # Turn the resulting dict back into a list of dicts
        vim_flavors = remove_duplicates(vim_flavors, only_keys=False)
        vim_flavors_rev = reverse_dict(vim_flavors)
        vim_flavors = listify(vim_flavors)

        flavor_map = self.generate_map_from_list(vim_flavors,
                                                 map_args={"value_map": MapElem.basic_map_list(
                                                     len(vim_flavors))})

        # From the mapping      [c1 -> 0, parent=(0 -> 0, parent=(None))]
        # and the value_dict    {'VIM_FLAVOR_CF': 'c1'}
        # generate the mapping  [VIM_FLAVOR_CF -> 0, parent=(None)]
        vim_flavors_map = []
        for k, v in vim_flavors_rev.items():
            for m in flavor_map:
                if m.name == v:
                    vim_flavors_map.append(MapElem(k, m.cur_map))

        # *** End VDU Flavors ***

        # *** Connection Point mappings ***
        # Map internal connection points to their VDUs
        cps_map = self.generate_map(T.node_template, T.int_cpd_identifier,
                                    map_function=V2Map.int_cp_mapping,
                                    map_args={"vdu_map": vdu_map})
        # Filter internal connection points that are assigned to management
        mgmt_cps_map = self.generate_map(T.node_template, T.int_cpd_mgmt_identifier,
                                         map_function=V2Map.int_cp_mapping,
                                         map_args={"vdu_map": vdu_map})

        # These are not going to be correctly mapped, so get the mapping from cps_map where
        # the names are the same
        # Every int-cpd will have a virtual-link-desc field, just if it's MGMT or ORCH is the
        # difference
        mgmt_cps_map = [x for x in cps_map if any(x.name == i.name for i in mgmt_cps_map)]
        # Get the opposite set for the orch cps. Note: this can be sped up by putting both of these
        # in a single loop
        orch_cps_map = [x for x in cps_map if not any(x.name == i.name for i in mgmt_cps_map)]

        # *** End Connection Point mapping ***

        # Get the default instantiation level, if it exists
        def_inst = get_path_value(T.def_inst_level, self.dict_tosca)
        def_inst = get_roots_from_filter(def_inst, child_key=T.def_inst_key)
        if def_inst:
            def_inst_id = T.def_inst_key
        else:
            def_inst_id = None

        print(def_inst_id)

        vdu_inst_level_map = self.generate_map(T.policies, T.inst_level_identifier)
        print(vdu_inst_level_map)

        # If there is a mapping function needed, the second parameter is a list with the mapping
        # as the second parameter
        # The first parameteer is always a tuple
        # This now supports the same value mapped to different locations
        self.mapping = \
            [
             # -- Metadata --
             ((T.vnf_desc_id, self.FLAG_BLANK),                 S.vnfd_id),
             ((T.vnf_provider, self.FLAG_BLANK),                S.vnfd_provider),
             ((T.vnf_product_name, self.FLAG_BLANK),            S.vnfd_product),
             ((T.vnf_software_ver, self.FLAG_BLANK),            S.vnfd_software_ver),
             ((T.vnf_desc_ver, self.FLAG_BLANK),                S.vnfd_ver),
             ((T.vnf_product_info_name, self.FLAG_BLANK),       S.vnfd_info_name),
             ((T.desc, self.FLAG_BLANK),                        S.vnfd_info_desc),
             ((T.vnf_vnfm_info, self.FLAG_BLANK),               S.vnfd_vnfm_info),
             # -- End Metadata --

             ((T.vdu_name, self.FLAG_BLANK),                    [S.vdu_name, vdu_map]),
             ((T.vdu, self.FLAG_KEY_SET_VALUE),                 [S.vdu_id, vdu_map]),
             ((T.vdu_desc, self.FLAG_BLANK),                    [S.vdu_desc, vdu_map]),

             # ((T.vdu_boot, self.FLAG_BLANK),                    [S.vdu_boot_key, vdu_map]),
             ((T.vdu_boot, self.FLAG_BLANK),                    [S.vdu_boot_value, vdu_map]),

             # The first value in the map is what we want to set, so insert that into the 'key'
             (("{}", self.FLAG_KEY_SET_VALUE),                  [S.vnfd_vcd_id, vim_flavors_map]),
             ((T.vdu_virt_cpu_num, self.FLAG_ONLY_NUMBERS),     [S.vnfd_vcd_cpu_num, flavor_map]),
             ((T.vdu_virt_mem_size, self.FLAG_ONLY_NUMBERS),    [S.vnfd_vcd_mem_size, flavor_map]),

             ((T.int_cpd, self.FLAG_KEY_SET_VALUE),             [S.int_cpd_id, cps_map]),
             ((T.int_cpd_layer_prot, self.FLAG_BLANK),          [S.int_cpd_layer_prot, cps_map]),
             ((S.KEY_VIRT_LINK_MGMT, self.FLAG_KEY_SET_VALUE),  [S.int_cpd_virt_link_desc,
                                                                 mgmt_cps_map]),
             ((S.KEY_VIRT_LINK_ORCH, self.FLAG_KEY_SET_VALUE),  [S.int_cpd_virt_link_desc,
                                                                 orch_cps_map]),

             # -- Software Image --
             ((T.virt_storage, self.FLAG_KEY_SET_VALUE),        [S.sw_id, sw_map]),
             ((T.sw_name, self.FLAG_BLANK),                     [S.sw_name, sw_map]),
             ((T.sw_name, self.FLAG_BLANK),                     [S.sw_image_name_var, sw_map]),
             ((T.sw_version, self.FLAG_BLANK),                  [S.sw_version, sw_map]),
             ((T.sw_checksum, self.FLAG_BLANK),                 [S.sw_checksum, sw_map]),
             ((T.sw_container_fmt, self.FLAG_BLANK),            [S.sw_container_format, sw_map]),
             ((T.sw_disk_fmt, self.FLAG_BLANK),                 [S.sw_disk_format, sw_map]),
             ((T.sw_min_disk, self.FLAG_ONLY_NUMBERS),          [S.sw_min_disk, sw_map]),
             ((T.sw_size, self.FLAG_ONLY_NUMBERS),              [S.sw_size, sw_map]),
             ((T.sw_image_file, self.FLAG_BLANK),               [S.sw_image, sw_map]),
             # -- End Software Image --

             # -- Deployment Flavor --
             ((T.df_id, self.FLAG_BLANK),                       S.df_id),
             ((T.df_desc, self.FLAG_BLANK),                     S.df_desc),
             ((T.vdu, self.FLAG_KEY_SET_VALUE),                 [S.df_vdu_prof_id, vdu_map]),
             ((T.vdu_prof_inst_min, self.FLAG_BLANK),           [S.df_vdu_prof_inst_min, vdu_map]),
             ((T.vdu_prof_inst_max, self.FLAG_BLANK),           [S.df_vdu_prof_inst_max, vdu_map]),

             # -- End Deployment Flavor --

             # Setting specific values at specific indexes
             # These are currently only the two virtual links and external links
             (self.set_value(S.KEY_VIRT_LINK_MGMT, S.virt_link_desc_id, 0)),
             (self.set_value(S.KEY_VIRT_LINK_ORCH, S.virt_link_desc_id, 1)),

             (self.set_value(S.KEY_EXT_CP_MGMT, S.ext_cpd_id, 0)),
             (self.set_value(S.KEY_VIRT_LINK_MGMT, S.ext_cpd_virt_link, 0)),
             (self.set_value(S.KEY_VIRT_LINK_ORCH, S.ext_cpd_virt_link, 1)),
             (self.set_value(S.KEY_EXT_CP_ORCH, S.ext_cpd_id, 1)),

                (self.set_value(def_inst_id, ))
            ]

    def set_value(self, val, path, index):
        return (val, self.FLAG_KEY_SET_VALUE), [path, [MapElem(val, index)]]

    @staticmethod
    def int_cp_mapping(names, map_start, **kwargs):
        if "filtered" not in kwargs or "vdu_map" not in kwargs:
            raise KeyError("The proper arguments haven't been passed for this method")

        mapping = []
        filtered = kwargs["filtered"]
        vdu_mappings = list(kwargs["vdu_map"])
        cur_num = map_start
        last_vdu = None

        # Loop through the CP names
        for name in names:
            # Get the dict that's related to this name
            # There should only be one element in the list
            entry = [x for x in filtered if get_dict_key(x) == name].pop()

            # Get the virtual_binding for this element from the filtered list
            # Remove the beginning of the path since we aren't dealing with the entire dict here
            path_lvl = KeyUtils.remove_path_level(TOSCAv2.int_cpd_virt_binding,
                                                  TOSCAv2.node_template)
            vdu = get_path_value(path_lvl.format(name), entry)

            # We need to find the parent mapping so we can include it in the map definition
            cur_vdu_map = None
            for v_map in vdu_mappings:
                if v_map.name == vdu:
                    cur_vdu_map = v_map
                    break

            # Iterate the map number if we've seen this vdu before, otherwise start over from 0
            if last_vdu == vdu:
                cur_num += 1
            else:
                cur_num = map_start
                last_vdu = vdu

            # Build the MapElem object, this stores all the parent mappings as well
            mapping.append(MapElem(name, cur_num, cur_vdu_map))

        return mapping


class KeyUtils:
    """
    General utility methods to use on paths from this file
    
    """
    @staticmethod
    def get_path_last(path, n=1):
        """
        Get the n last elements of the path, with their separators between them
        """
        paths = path.split(".")
        if len(paths) > 0:
            return ".".join(paths[len(paths) - n:len(paths)])
        raise KeyError("Path {} is an invalid path to use in this method.".format(path))

    @staticmethod
    def remove_path_first(path, n=1):
        """ Get the string without the first n elements of the path """
        paths = path.split(".")
        if len(paths) > 0:
            return ".".join(paths[n:len(paths)])
        raise KeyError("Path {} is an invalid path to use in this method.".format(path))

    @staticmethod
    def remove_path_level(path, path_level):
        return KeyUtils.remove_path_first(path, KeyUtils.get_path_level(path_level))

    @staticmethod
    def remove_path_elem(path, elem):
        """
        Remove the given elem of the path, return the path string without that element
        """
        paths = path.split(".")
        del paths[elem]
        return ".".join(paths)

    @staticmethod
    def get_path_level(path):
        return path.count(".") + 1
