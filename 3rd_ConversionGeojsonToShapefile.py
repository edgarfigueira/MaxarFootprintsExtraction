import subprocess


def convert_geojson_to_shapefile(input_geojson, output_shapefile):
    command = f'ogr2ogr -f "ESRI Shapefile" {output_shapefile} {input_geojson}'
    subprocess.run(command, shell=True)

# Example usage:


if __name__ == "__main__":
    input_geojson = r'geojson_merged\\footprints.geojson'
    output_shapefile = r'shapefile_conversion\\maxar_footprints.shp'
    convert_geojson_to_shapefile(input_geojson, output_shapefile)
