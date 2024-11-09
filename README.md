# CoastSat.Venice

This is a fork of the CoastSat repository done by the Sea Level Changes group at Ca'Foscari University of Venice, for use with students and for research purposes. Please give credit to the original repository if you use this fork. We are just trying to build up on the exceptional work of K. Vos and his colleagues.

For extensive documentation, see the original repository [**here**](https://github.com/kvos/CoastSat.git) 

CoastSat is an open-source software toolkit written in Python that enables users to obtain time-series of shoreline position at any coastline worldwide from 40 years (and growing) of publicly available satellite imagery (Landsat and Sentinel-2).

 :point_right: Other repositories and extensions related to CoastSat: 

- [CoastSeg](https://github.com/dbuscombe-usgs/CoastSeg): an interactive toolbox for downloading satellite imagery, applying image segmentation models, mapping shoreline positions and more.
- [CoastSat.slope](https://github.com/kvos/CoastSat.slope): estimates the beach-face slope from the satellite-derived shorelines obtained with CoastSat.
- [CoastSat.PlanetScope](https://github.com/ydoherty/CoastSat.PlanetScope): shoreline extraction for PlanetScope Dove imagery (near-daily since 2017 at 3m resolution).
- [SDS_Benchmark](https://github.com/SatelliteShorelines/SDS_Benchmark): testbed for satellite-derived shorelines mapping algorithms and validation against benchmark datasets.
- [CoastSat.islands](https://github.com/mcuttler/CoastSat.islands): 2D planform measurements for small reef islands.
- [CoastSat.Maxar](https://github.com/kvos/CoastSat.Maxar): shoreline extraction on Maxar World-View images (in progress)
- [InletTracker](https://github.com/VHeimhuber/InletTracker): monitoring of intermittent open/close estuary entrances.
- [VedgeSat](https://github.com/fmemuir/COASTGUARD/tree/master): monitoring vegetation lines.

 :point_right: Publications describing the CoastSat satellite-derived shorelines:

- Shoreline detection algorithm: https://doi.org/10.1016/j.envsoft.2019.104528 (Open Access)
- Accuracy assessment: https://doi.org/10.1016/j.coastaleng.2019.04.004
- Challenges in meso-macrotidal environments: https://doi.org/10.1016/j.geomorph.2021.107707
- Basin-scale shoreline mapping (Paficic): https://www.nature.com/articles/s41561-022-01117-8 (The Conversation article [here](https://theconversation.com/millions-of-satellite-images-reveal-how-beaches-around-the-pacific-vanish-or-replenish-in-el-nino-and-la-nina-years-198505))
- Beach slope estimation: https://doi.org/10.1029/2020GL088365 (preprint [here](https://www.essoar.org/doi/10.1002/essoar.10502903.2))
- Beach slope dataset for Australia: https://doi.org/10.5194/essd-14-1345-2022
</details>

## Installation

<summary><strong> Create an environment with Anaconda:</strong></summary>

To run the toolbox you first need to install the required Python packages in an environment.You can do this with **Anaconda** . 

Once you have it installed on your PC, open the Miniforge Prompt (in Mac and Linux, open a terminal window) and run the following commands (one by one) to install the `coastsat` environment:

```
conda create -n coastsatVenice
conda activate coastsatVenice
conda install geopandas -y
conda install scikit-image matplotlib astropy notebook -y
pip install earthengine-api
pip install pyqt5 imageio-ffmpeg
conda install -c conda-forge pytmd
```

All the required packages have now been installed and are self-contained in an environment called `coastsatVenice`. Always make sure that the environment is activated with:

```
conda activate coastsat
```

To confirm that you have successfully activated CoastSat, your terminal command line prompt should now start with `(coastsatVenice)`.

:warning: **In case errors are raised** :warning:: clean things up with the following command before attempting to install `coastsat` again:
```
conda clean --all
conda update conda
```

<summary><strong>Activate Google Earth Engine Python API:</strong></summary>

First, create a Google Earth Engine project at https://signup.earthengine.google.com/. 
Then, go to https://cloud.google.com/sdk/docs/install and install the `gcloud CLI`. After you have installed it will automatically launch and let you authenticate with your GEE account (or personal gmail).

:warning: if you're finding that you're always asked to authenticate, open the gloud CLI and run this command: `gcloud auth application-default login` to set a default authentication on your machine.
</details>

:white_check_mark: If you completed those two steps you are ready to start using CoastSat!

## References and Datasets

This section provides a list of references that use the CoastSat toolbox as well as existing shoreline datasets extracted with CoastSat.

### Publications

- Vos K., Splinter K.D., Harley M.D., Simmons J.A., Turner I.L. (2019). CoastSat: a Google Earth Engine-enabled Python toolkit to extract shorelines from publicly available satellite imagery. *Environmental Modelling and Software*. 122, 104528. https://doi.org/10.1016/j.envsoft.2019.104528 (Open Access)

- Vos K., Harley M.D., Splinter K.D., Simmons J.A., Turner I.L. (2019). Sub-annual to multi-decadal shoreline variability from publicly available satellite imagery. *Coastal Engineering*. 150, 160–174. https://doi.org/10.1016/j.coastaleng.2019.04.004

- Vos K., Harley M.D., Splinter K.D., Walker A., Turner I.L. (2020). Beach slopes from satellite-derived shorelines. *Geophysical Research Letters*. 47(14). https://doi.org/10.1029/2020GL088365 (Open Access preprint [here](https://www.essoar.org/doi/10.1002/essoar.10502903.2))

- Vos, K. and Deng, W. and Harley, M. D. and Turner, I. L. and Splinter, K. D. M. (2022). Beach-face slope dataset for Australia. *Earth System Science Data*. volume 14, 3, p. 1345--1357. https://doi.org/10.5194/essd-14-1345-2022

- Vos, K., Harley, M.D., Turner, I.L. et al. Pacific shoreline erosion and accretion patterns controlled by El Niño/Southern Oscillation. *Nature Geosciences*. 16, 140–146 (2023). https://doi.org/10.1038/s41561-022-01117-8

- Castelle B., Masselink G., Scott T., Stokes C., Konstantinou A., Marieu V., Bujan S. (2021). Satellite-derived shoreline detection at a high-energy meso-macrotidal beach. *Geomorphology*. volume 383, 107707. https://doi.org/10.1016/j.geomorph.2021.107707

- Castelle, B., Ritz, A., Marieu, V., Lerma, A. N., & Vandenhove, M. (2022). Primary drivers of multidecadal spatial and temporal patterns of shoreline change derived from optical satellite imagery. Geomorphology, 413, 108360. https://doi.org/10.1016/j.geomorph.2022.10836

- Konstantinou, A., Scott, T., Masselink, G., Stokes, K., Conley, D., & Castelle, B. (2023). Satellite-based shoreline detection along high-energy macrotidal coasts and influence of beach state. Marine Geology, 107082. https://doi.org/10.1016/j.margeo.2023.107082

### Datasets

- Time-series of shoreline change along the Pacific Rim (v1.4) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7758183

- Time-series of shoreline change along the U.S. Atlantic coast: U.S. Geological Survey data release, https://doi.org/10.5066/P9BQQTCI.

- Time-series of shoreline change for the Klamath River Littoral Cell (California) (1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7641757

- Beach-face slope dataset for Australia (Version 2) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7272538

- Training dataset used for pixel-wise classification in CoastSat (initial version): https://doi.org/10.5281/zenodo.3334147
