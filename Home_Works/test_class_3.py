class Armaments:
    gun_exist = True
    transport_platform_exist = True

    def __init__(self) -> None:
        self.con_mission_arm = 'Fight against enemy'
        
class Tank(Armaments):
    gun = 1
    machine_gun = 3
    crew = 4

    def __init__(self) -> None:
        self.con_mission_tank = 'Fight on land against enemy'

class AirCraft (Armaments):
    wings = 2
    machine_gun = 2
    crew = 1

    def __init__(self) -> None:
        self.con_mission_aircraft = 'Fight in air against enemy'

# Test relations between Class and Instance (out of constructor)
air_craft_1 = AirCraft() # Resume_1: Changes in Class (including parental) out of constructor affect class Instance
armaments_1 = Armaments()
print("armaments_1.gun_exist", armaments_1.gun_exist)
print("air_craft_1.gun_exist", air_craft_1.gun_exist)
Armaments.gun_exist = False
print("armaments_1.gun_exist", armaments_1.gun_exist)
print("air_craft_1.gun_exist", air_craft_1.gun_exist)

print('')

#Res: air_craft_1.gun_exist True
#    air_craft_1.gun_exist False

"""
# Test relations between Class and Instance (in constructor)
air_craft_2 = AirCraft() 
print("air_craft_2.con_mission_aircraft", air_craft_2.con_mission_aircraft)
AirCraft.con_mission_aircraft = '' # Resume_2: We couldn`t change ver in constructor by code, except - Class Name(x..)  `
print("air_craft_2.con_mission_aircraft", air_craft_2.con_mission_aircraft)
print('') """

""" # Test relations between 2 Instance, Classes of which has inheritance
armaments_2  = Armaments()
tank_1 = Tank ()

armaments_2.gun_exist = False # Resume_3: Changes in Instances, Classes of which has inheritance  does not affect each other
print("armaments_2.gun_exist", armaments_1.gun_exist) 
print("tank_1.gun_exist", tank_1.gun_exist)

#Res: armaments_2.gun_exist False
#     tank_1.gun_exist True """











