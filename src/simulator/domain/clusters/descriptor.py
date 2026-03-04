from src.simulator.domain.clusters.base import Cluster


class DescriptorCluster(Cluster):
    

    def __init__(
        self,
        device_types=None,
        server_clusters=None,
        client_clusters=None,
        parts_list=None,
    ):
        super().__init__(cluster_id="Descriptor")


        default_device_types = (
            [{"DeviceType": 0x002D, "Revision": 1}]
            if device_types is None
            else device_types
        )
        default_server_clusters = (
            [0x001D, 0x0003, 0x0202] if server_clusters is None else server_clusters
        )
        default_client_clusters = [] if client_clusters is None else client_clusters
        default_parts_list = [] if parts_list is None else parts_list


        self.attributes = {
            "DeviceTypeList": default_device_types,
            "ServerList": default_server_clusters,
            "ClientList": default_client_clusters,
            "PartsList": default_parts_list,
            "TagList": [],
        }


        self.commands = {}

    def add_server_cluster(self, cluster_id):
        
        if cluster_id not in self.attributes["ServerList"]:
            self.attributes["ServerList"].append(cluster_id)
            return True
        return False

    def add_client_cluster(self, cluster_id):
        
        if cluster_id not in self.attributes["ClientList"]:
            self.attributes["ClientList"].append(cluster_id)
            return True
        return False

    def add_device_type(self, device_type, revision=1):
        
        new_device_type = {"DeviceType": device_type, "Revision": revision}
        if new_device_type not in self.attributes["DeviceTypeList"]:
            self.attributes["DeviceTypeList"].append(new_device_type)
            return True
        return False

    def add_tag(self, tag_name):
        
        if tag_name not in self.attributes["TagList"]:
            self.attributes["TagList"].append(tag_name)
            return True
        return False

    def remove_tag(self, tag_name):
        
        if tag_name in self.attributes["TagList"]:
            self.attributes["TagList"].remove(tag_name)
            return True
        return False
