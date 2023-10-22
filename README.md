# MaxarFootprintsExtraction
Code repository for GIS-based python scripts

# Extraction of Buildings Footprints
1 - This repository was created to help in acquiring data from Maxar Sattelite Imagery.

2 - The main project is located here: https://blog.maxar.com/earth-intelligence/2018/gis-ready-building-footprint-shapefiles-for-accelerated-analysis
And you can search for the Microsoft official GitHub repository at this link: https://github.com/microsoft/GlobalMLBuildingFootprints

# Py Codes (What they have that others don't?)
The py codes are numbered sequentially, and they provide a programmatic solution for the extraction and geoprocessing of building footprints.
Sometimes, geospatial datasets can be very large and complex. Given that fact, programming approaches are very common to achieve the desired data.
the codes in this repository are made to extract, process, and convert shapefiles (polygons in this case).

# How to
1 - First, you should place these codes within the folder to where you want to extract your beautiful footprints;

2 - At 0_CreateDirs.py you should redifine the path to the 'base_folder' (Which should be the folder where you pasted the codes);

3 - At 1st_csv_zip_To_Geojson.py I recommend changing the 'location' variable according with the desired country;

4 - At the 2nd_mergeGeojsonDataset_ToOnlyfile.py the 'input_folder' and 'output_file' directories should be replaced as you pretend;

5 - Last but not least, the 3rd_ConversionGeojsonToShapefile.py file is using ogr2ogr (see documentation here: https://gdal.org/programs/ogr2ogr.html)
This approach allows to convert the data from GeoJson into shapefile with ease.

# Next steps
I think the whole code could be stored at a single .py file. For development, I find this step-by-step approach a great way to fix issues before merging all files.

If something pops-up, find me at edgarjunceiro@gmail.com

