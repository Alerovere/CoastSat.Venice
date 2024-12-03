import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def process_and_save_tides(calendar_dates, TIDE, LAT, LON, start_date, end_date, MODEL_NAME, sitename, folder_tides):
    """
    Process tide data and generate multiple outputs: CSV files and plots.

    Args:
        calendar_dates (pd.Series): Series of calendar dates.
        TIDE (pd.Series): Series of tide data.
        LAT (float): Latitude of the location.
        LON (float): Longitude of the location.
        start_date (datetime): Start date of the data.
        end_date (datetime): End date of the data.
        MODEL_NAME (str): Name of the tidal model.
        sitename (str): Name of the site.
        folder_tides (str): Directory where output files will be saved.

    Returns:
        None
    """
    # Ensure the folder exists
    os.makedirs(folder_tides, exist_ok=True)

    # Save the main tides DataFrame
    tides_df = pd.DataFrame({'Calendar Date (UTC)': calendar_dates, 'TIDE_data': TIDE.data})
    tides_df['dates'] = pd.to_datetime(tides_df['Calendar Date (UTC)']).dt.strftime('%Y-%m-%d %H:%M:%S.%f+00:00')
    tides_df['tide'] = tides_df['TIDE_data'].round(3)
    tides_df.drop(columns=['Calendar Date (UTC)', 'TIDE_data'], inplace=True)

    csvname = os.path.join(folder_tides, f'{MODEL_NAME}_tides_{sitename}.csv')
    tides_df.to_csv(csvname, index=False)
    print(f'Tide CSV file saved in {folder_tides}')

    # Save NOAA-compatible tides DataFrame
    tides_NOAA = pd.DataFrame({'Calendar Date (UTC)': calendar_dates, 'TIDE_data': TIDE.data})
    tides_NOAA['Calendar Date (UTC)'] = tides_NOAA['Calendar Date (UTC)'].dt.strftime('%m/%d/%Y %H:%M')
    csvname_noaa = os.path.join(folder_tides, f'{MODEL_NAME}_tides_NOAA_{sitename}.csv')
    tides_NOAA.to_csv(csvname_noaa, float_format='%.3f', index=False)
    print(f'Tide CSV file for NOAA saved in {folder_tides}')

    # Save metadata
    metadata_df = pd.DataFrame({
        "LAT": [LAT],
        "LON": [LON],
        "START_DATE": [start_date.isoformat()],
        "END_DATE": [end_date.isoformat()]
    })
    metadata_filepath = os.path.join(folder_tides, f'{MODEL_NAME}_location_date_{sitename}.csv')
    metadata_df.to_csv(metadata_filepath, index=False)
    print(f"Metadata saved to {metadata_filepath}")

    # Ensure 'Calendar Date (UTC)' is in datetime format
    tides_NOAA['Calendar Date (UTC)'] = pd.to_datetime(tides_NOAA['Calendar Date (UTC)'])

    # Create plots
    fig_size = (15, 5)
    fig, axs = plt.subplots(1, 2, figsize=fig_size, gridspec_kw={'width_ratios': [2, 1]})

    # Plot time series
    axs[0].plot(tides_NOAA['Calendar Date (UTC)'], tides_NOAA['TIDE_data'], color='black')
    axs[0].set_xlabel('Date', fontsize=14)
    axs[0].set_ylabel('Water level [m]', fontsize=14)
    axs[0].set_title(f'Water level from ({MODEL_NAME} tidal model)', fontsize=16)
    axs[0].tick_params(axis='both', which='major', labelsize=14)
    axs[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    axs[0].xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.setp(axs[0].xaxis.get_majorticklabels(), rotation=30, ha="right")
    axs[0].axhline(0, color='lightblue', linestyle='--', linewidth=1)

    # Plot histogram
    hist_data = tides_NOAA['TIDE_data']
    counts, bins = np.histogram(hist_data, bins=100)
    percentages = counts / counts.sum() * 100
    axs[1].barh(bins[:-1], percentages, height=np.diff(bins), color='black', edgecolor='black')
    axs[1].set_xlabel('Frequency (%)', fontsize=14)
    axs[1].set_title('Histogram of water levels', fontsize=16)
    axs[1].axhline(0, color='lightblue', linestyle='--', linewidth=1)
    axs[1].tick_params(axis='both', which='major', labelsize=14)

    # Adjust layout and save plot
    plt.tight_layout()
    plot_filepath = os.path.join(folder_tides, f'{sitename}_tide_timeseries.jpg')
    fig.savefig(plot_filepath, dpi=300)
    print(f"Plot saved to {plot_filepath}")
    plt.show()