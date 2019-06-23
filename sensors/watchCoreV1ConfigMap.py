from sensor_base import SensorBase
from os import sys, path
if __name__ == '__main__' and __package__ is None:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class watchCoreV1ConfigMap(SensorBase):

    def __init__(
            self,
            sensor_service,
            config=None,
            api_group="CoreV1Api",
            action="list_config_map_for_all_namespaces",
            trigger_ref="kubernetes.configmaps"):
        super(
            watchCoreV1ConfigMap,
            self).__init__(sensor_service, config, api_group, action, trigger_ref)
