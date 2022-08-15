import inspect


class Armaments:
    gun_exist = True
    transport_platform_exist = True

    def __init__(self) -> None:
        self.con_mission_arm = 'Fight against enemy'
        self.obj_tank = Tank()  # Bound tank to Armaments
        
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



armaments_1 = Armaments()
#print("armaments_1.obj_tank.crew", armaments_1.obj_tank.crew)

Tank.crew = 3
#print("armaments_1.obj_tank.crew", armaments_1.obj_tank.crew)


def inspect_class_obj (obj):

    if len(inspect.getmembers(obj)) > 0:

        print(len(inspect.getmembers(obj)))
    
        # Inspect Class atributes
        for i in inspect.getmembers(obj):
            
            # to remove private and protected
            # functions
            if not i[0].startswith('_'):
                
                # To remove other methods that
                # doesnot start with a underscore
                #if not inspect.ismethod(i[1]): 
                print(i)

    else:
        print(f'In {obj} is no avaliable elements')

inspect_class_obj (armaments_1.gun_exist)





