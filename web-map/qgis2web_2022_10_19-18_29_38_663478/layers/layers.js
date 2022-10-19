var wms_layers = [];


var format_floodzones_2 = new ol.format.GeoJSON();
var features_floodzones_2 = format_floodzones_2.readFeatures(json_floodzones_2, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_floodzones_2 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_floodzones_2.addFeatures(features_floodzones_2);
var lyr_floodzones_2 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_floodzones_2, 
                style: style_floodzones_2,
                interactive: false,
                title: '<img src="styles/legend/floodzones_2.png" /> floodzones'
            });
var format_USStates_3 = new ol.format.GeoJSON();
var features_USStates_3 = format_USStates_3.readFeatures(json_USStates_3, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_USStates_3 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_USStates_3.addFeatures(features_USStates_3);
var lyr_USStates_3 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_USStates_3, 
                style: style_USStates_3,
                interactive: true,
                title: '<img src="styles/legend/USStates_3.png" /> US States'
            });
var format_Colorado_County_Boundaries_4 = new ol.format.GeoJSON();
var features_Colorado_County_Boundaries_4 = format_Colorado_County_Boundaries_4.readFeatures(json_Colorado_County_Boundaries_4, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_Colorado_County_Boundaries_4 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_Colorado_County_Boundaries_4.addFeatures(features_Colorado_County_Boundaries_4);
var lyr_Colorado_County_Boundaries_4 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_Colorado_County_Boundaries_4, 
                style: style_Colorado_County_Boundaries_4,
                interactive: true,
                title: '<img src="styles/legend/Colorado_County_Boundaries_4.png" /> Colorado_County_Boundaries'
            });

        var lyr_GoogleMaps_6 = new ol.layer.Tile({
            'title': 'Google Maps',
            'type': 'base',
            'opacity': 0.500000,
            
            
            source: new ol.source.XYZ({
    attributions: ' ',
                url: 'https://mt1.google.com/vt/lyrs=r&x={x}&y={y}&z={z}'
            })
        });
var group_Borders = new ol.layer.Group({
                                layers: [lyr_USStates_3,lyr_Colorado_County_Boundaries_4],
                                title: "Borders"});
var group_Environmental = new ol.layer.Group({
                                layers: [lyr_floodzones_2,],
                                title: "Environmental"});

lyr_floodzones_2.setVisible(false);lyr_USStates_3.setVisible(true);lyr_Colorado_County_Boundaries_4.setVisible(true);lyr_GoogleMaps_6.setVisible(true);
var layersList = [group_Environmental,group_Borders,lyr_GoogleMaps_6];
lyr_floodzones_2.set('fieldAliases', {'id': 'id', 'dfirm_id': 'dfirm_id', 'version_id': 'version_id', 'fld_ar_id': 'fld_ar_id', 'study_typ': 'study_typ', 'fld_zone': 'fld_zone', 'zone_subty': 'zone_subty', 'sfha_tf': 'sfha_tf', 'static_bfe': 'static_bfe', 'v_datum': 'v_datum', 'depth': 'depth', 'len_unit': 'len_unit', 'velocity': 'velocity', 'vel_unit': 'vel_unit', 'ar_revert': 'ar_revert', 'ar_subtrv': 'ar_subtrv', 'bfe_revert': 'bfe_revert', 'dep_revert': 'dep_revert', 'dual_zone': 'dual_zone', 'source_cit': 'source_cit', 'layer': 'layer', 'path': 'path', });
lyr_USStates_3.set('fieldAliases', {'id': 'id', 'region': 'region', 'division': 'division', 'statefp': 'statefp', 'statens': 'statens', 'geoid': 'geoid', 'stusps': 'stusps', 'name': 'name', 'lsad': 'lsad', 'mtfcc': 'mtfcc', 'funcstat': 'funcstat', 'aland': 'aland', 'awater': 'awater', 'intptlat': 'intptlat', 'intptlon': 'intptlon', });
lyr_Colorado_County_Boundaries_4.set('fieldAliases', {'id': 'id', 'objectid': 'objectid', 'county': 'county', 'full': 'full', 'label': 'label', 'cnty_fips': 'cnty_fips', 'num_fips': 'num_fips', 'cent_lat': 'cent_lat', 'cent_long': 'cent_long', 'us_fips': 'us_fips', });
lyr_floodzones_2.set('fieldImages', {'id': 'TextEdit', 'dfirm_id': 'TextEdit', 'version_id': 'TextEdit', 'fld_ar_id': 'TextEdit', 'study_typ': 'TextEdit', 'fld_zone': 'TextEdit', 'zone_subty': 'TextEdit', 'sfha_tf': 'TextEdit', 'static_bfe': 'TextEdit', 'v_datum': 'TextEdit', 'depth': 'TextEdit', 'len_unit': 'TextEdit', 'velocity': 'TextEdit', 'vel_unit': 'TextEdit', 'ar_revert': 'TextEdit', 'ar_subtrv': 'TextEdit', 'bfe_revert': 'TextEdit', 'dep_revert': 'TextEdit', 'dual_zone': 'TextEdit', 'source_cit': 'TextEdit', 'layer': 'TextEdit', 'path': 'TextEdit', });
lyr_USStates_3.set('fieldImages', {'id': 'TextEdit', 'region': 'TextEdit', 'division': 'TextEdit', 'statefp': 'TextEdit', 'statens': 'TextEdit', 'geoid': 'TextEdit', 'stusps': 'TextEdit', 'name': 'TextEdit', 'lsad': 'TextEdit', 'mtfcc': 'TextEdit', 'funcstat': 'TextEdit', 'aland': 'TextEdit', 'awater': 'TextEdit', 'intptlat': 'TextEdit', 'intptlon': 'TextEdit', });
lyr_Colorado_County_Boundaries_4.set('fieldImages', {'id': 'TextEdit', 'objectid': 'Range', 'county': 'TextEdit', 'full': 'TextEdit', 'label': 'TextEdit', 'cnty_fips': 'TextEdit', 'num_fips': 'Range', 'cent_lat': 'TextEdit', 'cent_long': 'TextEdit', 'us_fips': 'TextEdit', });
lyr_floodzones_2.set('fieldLabels', {});
lyr_USStates_3.set('fieldLabels', {});
lyr_Colorado_County_Boundaries_4.set('fieldLabels', {});