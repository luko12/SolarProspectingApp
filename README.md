# Solar Prospecting Web App

## A personal project
![Day 1](/Images/Screenshot%202022-10-19%20174127.png)

### Goals
* V1: identify parcels of land for solar development given custom inputs for size, buffers, distance from power lines
* V2: identify rooftops for solar arrays given custom inputs for size, buffers

### TODO
* Migrate PostgreSQL DB to cloud (GCP)
* Upload raster files to DB
* Port/embed webmap from mapbox export to React
* Host web map on cloud


### Tech Stack
* Mapped with QGIS
* Data stored in PostGIS/PostgreSQL db
* Computed with Django - Python backend
* Published via web map with React, Typescript
* Hosted on GCP
* (v2) Utilizes satellite imagery