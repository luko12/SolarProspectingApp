# Solar Prospecting Web App

## A personal project
![](/Images/Screenshot%202022-11-01%20233518.png)

### Goals
* V1: identify parcels of land for solar development given custom inputs for size, buffers, distance from power lines
* V2: identify rooftops for solar arrays given custom inputs for size, buffers

### TODO
* create view or published map
* calculate slope from raster
* create raster in postgis
* Port/embed webmap from mapbox export to React
* Complete processing algorithm end to end as standalone script
* Explore repairing invalid geometries
* Host web map on cloud


### Tech Stack
* Mapped with QGIS
* Data stored in PostgreSQL/PostGIS db hosted on AWS RDS
* Scripts computed with Django - Python backend
* Published via web map with React, Typescript
* Front-end Hosted on GCP
* (v2) Utilizes satellite imagery


## How To
* Install QGIS with OSGEO4W Advanced Installation
* Configure filepaths in vscode.bat, run that batch file in order to open VSCode IDE with qgis.core module
* Now you can run processes in a standalone script