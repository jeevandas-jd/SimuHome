from src.simulator.domain.clusters.base import Cluster

class BasicInformationCluster(Cluster):
    def __init__(self, vendor_name: str, vendor_id: int, product_name: str, product_id: int):
        super().__init__(cluster_id="BasicInformation")
        self.attributes = {
            'VendorName': vendor_name,
            'VendorID': vendor_id,
            'ProductName': product_name,
            'ProductID': product_id,
        }
        self.readonly_attributes = {"VendorName", "VendorID", "ProductName", "ProductID"}
