from django.contrib.gis.utils import LayerMapping

mannar_district_boundary_mapping = {
    'name':'DISTRICT_N',
    'geom':'POLYGON'
}

mannar_dsd_mapping = {
    'name':'DSD_N',
    'geom':'POLYGON'
}

mannar_gnd_mapping = {
    'name':'GND_N',
    'num': 'GND_NO',
    'geom':'POLYGON'
}

mannar_forest_cover_mapping  = {
    'forest_type': 'Forest_Typ',
    'geom':'POLYGON'
}

mannar_irrigation_tank_mapping  = {
    'name': 'Tank_Name',
    'geom':'POLYGON'
}

mannar_landuse_mapping  = {
    'mcode': 'MCode',
    'scode': 'SCode',
    'main_category': 'Main_Categ',
    'sub_category': 'Sub_Catego',
    'year_of_update': 'Year_of_Up',
    'geom':'POLYGON'
}

mannar_national_roads_mapping  = {
    'name': 'TL_Nm_Tran',
    'road_class': 'Class',
    'road_type': 'Type',
    'starts_at': 'Start',
    'ends_at': 'End',
    'geom': 'LINESTRING'
}

mannar_pa_cover_mapping  = {
    'name': 'NAME',
    'con_status': 'Con_Status',
    'owner': 'Owner',
    'gaz_no': 'GAZ_NO',
    'date_of_gaz': 'DATE_GAZ',
    'category': 'CATEGORY',
    'remarke': 'REMARKES',
    'geom':'POLYGON'
}

mannar_places_mapping  = {
    'name': 'Name',
    'geom': 'POINT'
}

mannar_remaining_forest_mapping  = {
    'forest_type': 'Forest_Typ',
    'geom':'POLYGON'
}

mannar_river_basin_mapping  = {
    'name': 'Name',
    'geom':'POLYGON'
}

mannar_small_irrigation_tank_point_mapping  = {
    'name': 'Tank_name',
    'river_b_na': 'River_B_na',
    'ownership': 'Tank_owner',
    'functional': 'Functional',
    'remarke': 'Remark',
    'geom': 'POINT'
}

mannar_small_irrigation_tank_poly_mapping  = {
    'name': 'Tank_Name',
    'river_b_na': 'River_B_na',
    'ownership': 'Ownership',
    'geom':'POLYGON'
}

mannar_stream_network_mapping  = {
    'object_id': 'OBJECTID',
    'from_node': 'FROM_NODE',
    'to_node': 'TO_NODE',
    'geom': 'LINESTRING'
}