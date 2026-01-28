
from core.environment import Room
from core.aggregator import Aggregator
import time



def Run_simulator(duration=60):
    
    my_Room=Room(room_id=1,room_name="my_Room")
    tick_rate=0.1
    current_tick=0

    total_tick=(duration*60)

    while(current_tick<total_tick):

        loop_start=time.time()

        Aggregator.update_room(my_Room)

        elapsed=time.time()-loop_start

        time.sleep(max(0,tick_rate-elapsed))
        current_tick+=tick_rate





Run_simulator(1)
