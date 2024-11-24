import os
from ipywidgets import Dropdown, Button, VBox, Output

def select_folder(data_folder_path="Data", create_additional_folders=False):
    """
    Displays a dropdown to select a folder and creates necessary subdirectories.

    Parameters:
        data_folder_path (str): Path to the main 'Data' folder.
        create_additional_folders (bool): Whether to create additional folders for Waves outputs.

    Returns:
        str: Name of the selected folder (sitename).
    """
    folders = [f for f in os.listdir(data_folder_path) if os.path.isdir(os.path.join(data_folder_path, f))]

    if not folders:
        print("No folders found in the 'Data' directory.")
        return None

    folder_dropdown = Dropdown(options=folders, description="Folder:", disabled=False)
    select_button = Button(description="Select Folder")
    output = Output()

    # Mutable container to capture the selected sitename
    sitename = {"value": None}

    def on_button_click(b):
        with output:
            output.clear_output()
            sitename["value"] = folder_dropdown.value
            print(f"Selected folder saved as sitename: {sitename['value']}")
            filepath = os.path.join(os.getcwd(), data_folder_path)
            create_directories(filepath, sitename["value"], create_additional_folders)

    select_button.on_click(on_button_click)

    display(VBox([folder_dropdown, select_button, output]))
    return sitename

def create_directories(filepath, sitename, create_additional_folders=False):
    """
    Creates the required directories for the selected site.

    Parameters:
        filepath (str): Base file path.
        sitename (str): Selected folder name.
        create_additional_folders (bool): Whether to create additional folders for Waves outputs.
    """
    directories = {
        "Slope Estimation": os.path.join(filepath, sitename, "slope_estimation"),
        "Tidal Data": os.path.join(filepath, sitename, "water_levels"),
        "Image Outputs": os.path.join(filepath, sitename, "Output/img"),
        "Data Outputs": os.path.join(filepath, sitename, "Output/data"),
        "Runup": os.path.join(filepath, sitename, "Output/Runup"),
        "Runup": os.path.join(filepath, sitename, "Output/Runup/data"),
        "Runup": os.path.join(filepath, sitename, "Output/Runup/img"),

    }

    # Add additional directories if requested
    if create_additional_folders:
        directories.update({
            "Waves": os.path.join(filepath, sitename, "Waves"),
            "Waves Images": os.path.join(filepath, sitename, "Waves", "img"),
            "Waves Data": os.path.join(filepath, sitename, "Waves", "data"),
            "Runup": os.path.join(filepath, sitename,"Runup"),
            "Runup Data": os.path.join(filepath, sitename,"Runup","data"),
            "Runup Images": os.path.join(filepath, sitename,"Runup","img"),
        })

    for name, path in directories.items():
        os.makedirs(path, exist_ok=True)
        print(f"Directory created or already exists: {path}")

