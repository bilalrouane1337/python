class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


errors = [PlantError(), WaterError()]

for error in errors:
    try:
        raise error
    except GardenError:
        print("Caught a garden error")                                               
