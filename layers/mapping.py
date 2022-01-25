from django.contrib.gis.utils import LayerMapping

mannar_district_boundary_mapping = {
    'objectid': 'OBJECTID',
    'district_n': 'DISTRICT_N',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

mannar_ds_boundary_mapping = {
    'dsd_n': 'DSD_N',
    'geom': 'MULTIPOLYGON',
}

mannar_gn_boundary_mapping = {
    'gnd_n': 'GND_N',
    'gnd_no': 'GND_NO',
    'district_n': 'DISTRICT_N',
    'dsd_n': 'DSD_N',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

mannar_declared_forest_mapping = {
    'name': 'NAME',
    'con_status': 'Con_Status',
    'owner': 'Owner',
    'area': 'Area',
    'geom': 'MULTIPOLYGON',
}

mannar_forest_cover_mapping = {
    'district': 'District',
    'area_final': 'Area_final',
    'f_type': 'F_Type',
    'lc': 'LC',
    'forest_typ': 'Forest_Typ',
    'geom': 'MULTIPOLYGON',
}


mannar_landuse_mapping = {
    'mcode': 'MCode',
    'scode': 'SCode',
    'shape_area': 'Shape_Area',
    'main_land': 'Main_Land',
    'geom': 'MULTIPOLYGON25D',
}

mannar_major_irr_tank_mapping = {
    'tank_name': 'Tank_Name',
    'map_id': 'Map_id',
    'geom': 'MULTIPOLYGON',
}

mannar_other_state_forest_mapping = {
    'forest_typ': 'Forest_Typ',
    'geom': 'MULTIPOLYGON25D',
}

mannar_pa_cover_mapping = {
    'name': 'NAME',
    'con_status': 'Con_Status',
    'owner': 'Owner',
    'area': 'Area',
    'geom': 'MULTIPOLYGON',
}

mannar_place_mapping = {
    'place_id': 'id',
    'name': 'Name',
    'geom': 'MULTIPOINT',
}

mannar_river_basin_boundary_mapping = {
    'rb_id': 'RB_id',
    'name': 'Name',
    'basin_area': 'Basin_area',
    'geom': 'MULTIPOLYGON',
}

mannar_river_stream_mapping = {
    'objectid': 'OBJECTID',
    'shape_leng': 'Shape_Leng',
    'geom': 'MULTILINESTRING',
}

mannar_road_mapping = {
    'tl_nm_tran': 'TL_Nm_Tran',
    'road_class': 'Class',
    'type': 'Type',
    'start': 'Start',
    'end': 'End',
    'start_km_p': 'Start_km_p',
    'end_km_pos': 'End_km_pos',
    'tot_length': 'Tot_length',
    'geom': 'MULTILINESTRING',
}

mannar_slope_mapping = {
    'slope_id': 'ID',
    'gridcode': 'GRIDCODE',
    'sl_class': 'Sl_class',
    'geom': 'MULTIPOLYGON',
}

mannar_small_irr_tank_mapping = {
    'tank_name': 'Tank_Name',
    'map_id': 'Map_id',
    'geom': 'MULTIPOLYGON',
}

ampara_declared_forest_mapping = {
    'name': 'NAME',
    'con_status': 'Con_Status',
    'owner': 'Owner',
    'area': 'Area',
    'geom': 'MULTIPOLYGON',
}

ampara_disrict_boundary_mapping = {
    'district_n': 'DISTRICT_N',
    'geom': 'MULTIPOLYGON',
}

ampara_ds_boundary_mapping = {
    'dsd_n': 'DSD_N',
    'geom': 'MULTIPOLYGON',
}

ampara_forest_cover_mapping = {
    'forest_cover_id': 'Id',
    'lc': 'LC',
    'forest_typ': 'Forest_Typ',
    'geom': 'MULTIPOLYGON',
}

ampara_gn_boundary_mapping = {
    'gnd_n': 'GND_N',
    'gnd_no': 'GND_NO',
    'district_n': 'DISTRICT_N',
    'dsd_n': 'DSD_N',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

ampara_landuse_mapping = {
    'mcode': 'MCode',
    'scode': 'SCode',
    'shape_area': 'Shape_Area',
    'main_land': 'Main_Land',
    'geom': 'MULTIPOLYGON25D',
}

ampara_major_irr_tank_mapping = {
    'tank_name': 'Tank_Name',
    'map_id': 'Map_id',
    'geom': 'MULTIPOLYGON',
}

ampara_other_state_forest_mapping = {
    'fid_fc_201': 'FID_FC_201',
    'forest_typ': 'Forest_Typ',
    'name': 'Name',
    'geom': 'MULTIPOLYGON25D',
}

ampara_place_mapping = {
    'name': 'NAME',
    'geom': 'MULTIPOINT',
}

ampara_river_basin_boundary_mapping = {
    'rb_id': 'RB_id',
    'name': 'Name',
    'basin_area': 'Basin_area',
    'geom': 'MULTIPOLYGON',
}

ampara_river_stream_mapping = {
    'objectid': 'OBJECTID',
    'shape_leng': 'Shape_Leng',
    'geom': 'MULTILINESTRING',
}

ampara_road_mapping = {
    'tl_nm_tran': 'TL_Nm_Tran',
    'road_class': 'Class',
    'type': 'Type',
    'start': 'Start',
    'end': 'End',
    'tot_length': 'Tot_length',
    'geom': 'MULTILINESTRING',
}

ampara_slope_mapping = {
    'slope_id': 'ID',
    'gridcode': 'GRIDCODE',
    'sl_class': 'Sl_class',
    'geom': 'MULTIPOLYGON',
}


ampara_small_irr_tank_mapping = {
    'tank_name': 'Tank_Name',
    'map_id': 'Map_id',
    'district': 'District',
    'asc_field': 'ASC_',
    'gnd': 'GND',
    'river_b_na': 'River_B_na',
    'dsd': 'DSD',
    'ownership': 'Ownership',
    'geom': 'MULTIPOLYGON',
}



