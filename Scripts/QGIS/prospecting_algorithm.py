import utilities
"""
Prospecting steps:
1. Buffer powerlines X meters
2. Select parcels by location (if touching powerlines buffer)
3. Clip wetlands & floodplains to parcel selection to reduce working file size
4. Buffer wetlands & floodplains X meters
5. Difference? 
"""

buffered_powerlines = utilities.buffer(
        r"C:\Users\lukas\Documents\LukasProjects\SolarProspectingApp\Data\transmissionLines.shp",
        100,
        # output = r"C:\Users\lukas\Documents\LukasProjects\SolarProspectingApp\Data\transmissionBuffered1.shp",
    )
print("buffered_powerlines:", buffered_powerlines, 'id:', buffered_powerlines['OUTPUT'].id(), 'feature count:', buffered_powerlines['OUTPUT'].featureCount())


# parcels_electrical_selection = utilities.select_by_location()