import os


def create_directories(base_folder):
    # Define the directory names
    directories = ['MaxarFootprints', 'geojson_merged', 'shapefile_conversion']

    # Create the directories
    for directory in directories:
        dir_path = os.path.join(base_folder, directory)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")

    # Check if all directories are created
    all_created = all(os.path.exists(os.path.join(base_folder, directory)) for directory in directories)
    return all_created


# Usage
base_folder = 'path/to/your/base/folder'  # Replace with your desired base folder path
success = create_directories(base_folder)

if success:
    print("All directories created successfully!")
else:
    print("Failed to create one or more directories.")


