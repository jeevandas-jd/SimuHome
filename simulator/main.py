
from core.environment import Room
from core.aggregator import Aggregator
import time



def Run_simulator(duration=60):
    my_Room=Room(room_id=1,room_name="my_Room")

    current_tick=0

    total_tick=(duration/0.1)

    while(current_tick<total_tick):

        Aggregator.update_room(my_Room)

        current_tick+=1




Run_simulator(300)
