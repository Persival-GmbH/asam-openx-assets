# ASAM OpenX Data and Assets

This is a collection of data and assets demonstrating the connection between ASAM OpenDRIVE, ASAM OpenSCENARIO XML, ASAM OpenMATERIAL 3D and further ASAM OpenX standards.

## Folder Structure

- `xodr/`: Contains ASAM OpenDRIVE files defining road networks.
- `xosc/`: Contains ASAM OpenSCENARIO XML files defining driving scenarios.
- `models/`: Contains ASAM OpenMATERIAL 3D assets including material properties
    - `environments, vehicles, etc/`: Subfolders for different types of 3D assets.
    - `materials/`: Contains ASAM OpenMATERIAL 3D material property files and look-up tables.
      ⚠️ Note: The material files are placeholders to demonstrate how the material system works. They are not actual measurement data.

## How OpenDRIVE, OpenSCENARIO XML, and OpenMATERIAL 3D Work Together

ASAM OpenX standards form a unified framework for creating realistic and interoperable simulation environments.
Each standard addresses a distinct layer of the simulation stack, and together they ensure consistency between logical, dynamic, and physical representations.
For more information check out this [ASAM OpenX Video Tutorial](https://www.persival.de/post/tutorial-2-introduction-to-asam-openx-standards).

### ASAM OpenDRIVE

ASAM OpenDRIVE provides a detailed description of road networks, including geometry, topology, and semantic attributes such as lanes, markings, and traffic rules.
This serves as the foundation for any driving simulation.

### ASAM OpenSCENARIO XML

ASAM OpenSCENARIO XML defines dynamic content — traffic maneuvers, interactions between vehicles, pedestrians, and other entities.
It references the road network defined in OpenDRIVE through the `RoadNetwork` element, using the `LogicFile` property to link to an OpenDRIVE file.
This connection ensures that all scenario actions occur on a consistent road layout.
Furthermore, OpenSCENARIO does not just link the road network, it also uses lane and road definitions from ASAM OpenDRIVE to position entities accurately and execute maneuvers in context.

Check out this video tutorial on [how to create an ASAM OpenDRIVE map and an ASAM OpenSCENARIO XML file](https://www.persival.de/post/video-tutorial-3-creating-an-asam-opendrive-map-and-an-asam-openscenario-file).

### ASAM OpenMATERIAL 3D

While ASAM OpenDRIVE and ASAM OpenSCENARIO XML handle logical and behavioral aspects, ASAM OpenMATERIAL 3D adds 3D geometry and physical material properties.
It provides 3D asset files (.xoma) with metadata and references to 3D geometry and material mapping for environments and objects.

- Static environments are linked via the `SceneGraphFile` property in OpenSCENARIO XML.
- Individual objects such as vehicles are referenced using the `model3d` property, for example in a vehicle catalog.
- Paths to these assets must remain consistent and synchronized across distributed simulation components to maintain integrity.

Check out this introduction to [ASAM OpenMATERIAL 3D](https://www.youtube.com/watch?v=0PagWTJB3Y8) or further detailed tutorials for [different aspects of ASAM OpenMATERIAL 3D](https://www.persival.de/knowledge/tags/asam-openmaterial-3d).

The following ASAM OpenMATERIAL 3D assets are included in this repository including a comprehensive material mapping:

#### Vehicles

|                                                                                  |                                                                                        |                                                                                |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| ![vehicle_audi_q7_2015.png](doc/images/vehicle_audi_q7_2015.png)                 | ![vehicle_audi_tt_2014_roadster.png](doc/images/vehicle_audi_tt_2014_roadster.png)     | ![vehicle_dacia_duster_2010.png](doc/images/vehicle_dacia_duster_2010.png)     |
| ![vehicle_fiat_ducato_2014.png](doc/images/vehicle_fiat_ducato_2014.png)         | ![vehicle_gmc_hummer_2021_pickup.png](doc/images/vehicle_gmc_hummer_2021_pickup.png)   | ![vehicle_hyundai_tucson_2015.png](doc/images/vehicle_hyundai_tucson_2015.png) |
| ![vehicle_mini_countryman_2016.png](doc/images/vehicle_mini_countryman_2016.png) | ![vehicle_volvo_v60_polestar_2013.png](doc/images/vehicle_volvo_v60_polestar_2013.png) |                                                                                |

#### Environments

|                                                                                          | | |
|------------------------------------------------------------------------------------------|-|-|
| ![environment_german_highway_short.png](doc/images/environment_german_highway_short.png) | | |

## Usage

To utilize all standardized data and assets in a simulation, check out our [demo repository](https://github.com/Persival-GmbH/standardized-co-simulation-demo).

## Credits

- The vehicle models used in this repository were taken from public sources under the creative commons license and converted to the ASAM OpenMATERIAL 3D geometry format by https://github.com/bounverif/openx-assets.
We enhanced the models and added a comprehensive material mapping. Each asset contains authorship and copyright information in the metadata.
- The OpenDRIVE data was created with the [blender-driving-scenario-creator](https://github.com/johschmitz/blender-driving-scenario-creator).
