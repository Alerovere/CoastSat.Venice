from ipyleaflet import Map, Marker, Output, TileLayer
from ipywidgets import VBox

def create_map():
    """
    Create and display an interactive map with a satellite background and
    functionality for selecting coordinates and getting map bounds.

    Returns:
        tuple: A tuple containing the map widget, output widget, and helper functions:
            - map_widget: The ipyleaflet Map widget.
            - output_widget: The output widget to display logs.
            - saved_variables: A dictionary to access `LAT` and `LON`.
            - get_map_bounds: Function to get the current map bounds.
    """
    # Satellite Tile Layer
    satellite_layer = TileLayer(
        url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        attribution="ESRI basemap",
    )

    # Create the Map
    m = Map(center=(0, 0), zoom=2, layers=(satellite_layer,))

    # Output Widget
    output = Output()

    # Dictionary to store LAT, LON, and map bounds
    saved_variables = {"LAT": None, "LON": None}
    map_bounds = []

    # Function to handle double-click events
    def handle_double_click(**kwargs):
        with output:
            output.clear_output()
            # Check if the event is a double-click and contains coordinates
            if kwargs.get("type") == "dblclick" and "coordinates" in kwargs:
                coords = kwargs["coordinates"]
                saved_variables["LAT"], saved_variables["LON"] = coords[0], coords[1]
                # Clear existing markers
                m.layers = m.layers[:1]  # Keep only the base map
                # Add a new marker at the double-clicked coordinates
                marker = Marker(location=coords)
                m.add_layer(marker)
                print(f"Coordinates saved: Latitude={saved_variables['LAT']}, Longitude={saved_variables['LON']}")

            # Save the current map bounds
            nonlocal map_bounds
            map_bounds = m.bounds
            print(f"Map bounds updated: {map_bounds}")

    # Add the double-click handler
    m.on_interaction(handle_double_click)

    # Function to get the map bounds
    def get_map_bounds():
        if map_bounds:
            extent = {
                "southwest": {"lat": map_bounds[0][0], "lon": map_bounds[0][1]},
                "northeast": {"lat": map_bounds[1][0], "lon": map_bounds[1][1]},
            }
            print(f"Current Map Bounds: {extent}")
            return extent
        else:
            print("Map bounds have not been recorded. Please interact with the map.")
            return None

    # Display the Map and Output
    display(VBox([m, output]))

    return m, output, saved_variables, get_map_bounds