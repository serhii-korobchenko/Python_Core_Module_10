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

control_level = 0
def inspect_class_obj (obj, level_in = 5):
    global control_level
    if len(inspect.getmembers(obj)) == 0: # base case
        print ('Zero elements in__')
    
    elif control_level >= level_in: # base case
        print ('Maximum depth level has been reached!')

    else:
        print(f'Object contains links for {len(inspect.getmembers(obj))} atributes')
    
        # Inspect Class atributes
        for i in inspect.getmembers(obj):
            
            # to remove private and protected
            # functions
            if not i[0].startswith('_'):
                
                # To remove other methods that
                # doesnot start with a underscore
                if not inspect.ismethod(i[1]): 
                    print(i)
                    control_level +=1
                    return inspect_class_obj (i)


inspect_class_obj (armaments_1.gun_exist)





