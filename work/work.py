MODULE_DICT = {
    "Hanwha": {
         385: 21.5487,
         390: 21.5487,
         395: 21.5487,
         400: 21.5487,
         405: 21.5487,
         410: 21.5487,
         420: 21.3944,
         425: 21.3944,
         485: 25.3657
    },
    "REC": {
         400: 20.3476,
         410: 20.3476,
         420: 20.88
    }
}

def module_roof_percentage(brand: str, watt: int, panel_count: float, roof_size: float):
    panel_sqft = 0
    roof_percentage = 0

    if brand in MODULE_DICT:
        if watt in MODULE_DICT[brand]:
            panel_sqft = panel_count * MODULE_DICT[brand][watt]
            roof_percentage = (panel_sqft / roof_size) * 100
            return f"Module Percentage: {panel_sqft:.2f} sf (panels) / {roof_size} sf (roof) = {roof_percentage:.2f}%"
        else:
            return f"Wattage not found for {brand}."
    else:
        return "Brand not found."
