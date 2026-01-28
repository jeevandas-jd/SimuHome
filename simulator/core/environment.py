
class Room:

    def __init__(self,room_id,room_name):

        self.room_id=room_id
        self.room_name=room_name

        #environment variable setting

        self.state={
            "temperature":2000,
            "humidity":2000,
            "air_quality":2000,
            "illuminance":50
        }

        self.devices={}
    def get_state(self):
        return self.state


class MatterDevices:

    def __init__(self,device_id,device_type):
        self.device_id=device_id
        self.device_type=device_type

        self.endpoints={}

    def addEndPoint(self,endPoint_id):
        self.endpoints[endPoint_id]=Endpoint(endPoint_id)


class Endpoint:

    def __init__(self,endpoint_id):
        self.endpoint_id=endpoint_id
        self.cluster={}


class Cluster:

    def __init__(self,name):
        self.name=name

        self.attributes={}
        self.commanfs=[]

