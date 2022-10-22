# Solar Prospecting Web App

## A personal project
![](/Images/Screenshot%202022-10-22%20172324.png)

### Goals
* V1: identify parcels of land for solar development given custom inputs for size, buffers, distance from power lines
* V2: identify rooftops for solar arrays given custom inputs for size, buffers

### TODO
* Port/embed webmap from mapbox export to React
* Host web map on cloud


### Tech Stack
* Mapped with QGIS
* Data stored in PostgreSQL/PostGIS db hosted on AWS RDS
* Scripts computed with Django - Python backend
* Published via web map with React, Typescript
* Front-end Hosted on GCP
* (v2) Utilizes satellite imagery