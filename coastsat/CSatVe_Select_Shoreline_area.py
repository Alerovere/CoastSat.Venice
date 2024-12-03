import os
import folium
from folium import plugins
from IPython.display import display, Markdown

def create_shoreline_selection_map(tidal_point, sitename, base_dir="Data"):
    """
    Create an interactive map with a satellite background and tools to draw and export a GeoJSON region.

    Args:
        tidal_point (tuple): Latitude and longitude of the tidal point (e.g., (lat, lon)).
        sitename (str): Name of the site, used to organize outputs.
        base_dir (str, optional): Base directory for storing data and outputs. Defaults to "Data".

    Returns:
        folium.Map: The folium map with drawing and export functionalities.
    """
    # Create a map centered around the tidal point
    m = folium.Map(location=tidal_point, zoom_start=12)

    # Add a satellite tile layer
    folium.TileLayer(
        tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        attr="Esri",
        name="Satellite",
        overlay=False,
        control=True,
    ).add_to(m)

    # Add the tidal point to the map
    folium.CircleMarker(
        location=tidal_point,
        radius=5,
        color="black",
        fill=True,
        fill_color="black",
        fill_opacity=1,
        weight=2,
        opacity=1,
    ).add_to(m)

    folium.Marker(
        tidal_point,
        popup="Point of tidal data extraction",
        icon=folium.Icon(color="black", icon="info-sign"),
    ).add_to(m)

    # Add the drawing plugin to the map
    draw = plugins.Draw(export=True, filename="ROI_satellite.geojson", position="topleft")
    draw.add_to(m)

    # Display export instructions
    display(
        Markdown(
            f"After exporting the file, please move it to the directory: `{os.path.join(sitename, "Output", "data")}` "
            "and make sure its name is `ROI_satellite.geojson`."
        )
    )

    return m