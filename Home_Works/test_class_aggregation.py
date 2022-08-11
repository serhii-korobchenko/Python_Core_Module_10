class Armaments:
    gun_exist = True
    transport_platform_exist = True

    def __init__(self, tank) -> None:
        self.con_mission_arm = 'Fight against enemy'
        self.obj_tank = tank
        
class Tank:
    gun = 1
    machine_gun = 3
    crew = 4

    def __init__(self) -> None:
        self.con_mission_tank = 'Fight on land against enemy'

class AirCraft:
    wings = 2
    machine_gun = 2
    crew = 1

    def __init__(self) -> None:
        self.con_mission_aircraft = 'Fight in air against enemy'



tank_1 = Tank()
armament_1 = Armaments(tank_1)

print("armament_1.obj_tank.crew", armament_1.obj_tank.crew)

Tank.crew = 3
print("armaments_1.obj_tank.crew", armament_1.obj_tank.crew)





