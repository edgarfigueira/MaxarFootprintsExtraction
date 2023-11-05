import geopandas as gpd
import os
import pandas as pd

def merge_geojson(input_folder, output_file):
    # Get a list of all GeoJSON files in the folder
    geojson_files = [f for f in os.listdir(input_folder) if f.endswith('.geojson')]

    # Check if there are any GeoJSON files
    if not geojson_files:
        print("No GeoJSON files found in the folder.")
        return

    # Initialize an empty list to store GeoDataFrames
    gdf_list = []

    # Iterate through each GeoJSON file and merge it
    for file_name in geojson_files:
        file_path = os.path.join(input_folder, file_name)
        gdf = gpd.read_file(file_path)
        gdf_list.append(gdf)

    # Concatenate the list of GeoDataFrames
    merged_gdf = gpd.GeoDataFrame(pd.concat(gdf_list, ignore_index=True), crs=gdf_list[0].crs)

    # Save the merged GeoDataFrame to a new GeoJSON file
    merged_gdf.to_file(output_file, driver='GeoJSON')
    print(f'Merged data saved to {output_file}')


input_folder = r'MaxarFootprints'
output_file = r'geojson_merged\\footprints.geojson'

merge_geojson(input_folder, output_file)

