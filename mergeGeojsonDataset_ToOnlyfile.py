import geopandas as gpd
import os

def merge_geojson(input_folder, output_file):
    # Get a list of all GeoJSON files in the folder
    geojson_files = [f for f in os.listdir(input_folder) if f.endswith('.geojson')]

    # Check if there are any GeoJSON files
    if not geojson_files:
        print("No GeoJSON files found in the folder.")
        return

    # Initialize an empty GeoDataFrame to store the merged data
    merged_gdf = gpd.GeoDataFrame()

    # Iterate through each GeoJSON file and merge it
    for file_name in geojson_files:
        file_path = os.path.join(input_folder, file_name)
        gdf = gpd.read_file(file_path)
        merged_gdf = merged_gdf.append(gdf, ignore_index=True)

    # Save the merged GeoDataFrame to a new GeoJSON file
    merged_gdf.to_file(output_file, driver='GeoJSON')
    print(f'Merged data saved to {output_file}')

# Usage example:
input_folder = '/path/to/your/input/folder'
output_file = '/path/to/your/output/merged.geojson'
merge_geojson(input_folder, output_file)
