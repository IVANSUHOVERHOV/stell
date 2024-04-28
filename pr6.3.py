class BuildingError(Exception):
    def __str__(self):
        return f"With so much materials the house cannot build!"

def check_material(amount_of_material, limit_material):
    if amount_of_material > limit_material:
        return "enough material"
    else:
        raise BuildingError

material = 30381
check_material(material,300)