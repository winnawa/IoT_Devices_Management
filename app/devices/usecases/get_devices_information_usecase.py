from app.devices.repositories.device_repository import DeviceRepository
from app.devices.services.mqtt_broker_services.get_device_data_service import GetDeviceDataService

class GetDevicesInformationUsecaseInput:
    def __init__(self,inputObj):
        self.inputObj = inputObj
class GetDevicesInformationUsecase:
    def __init__(self, input : GetDevicesInformationUsecaseInput, deviceRepository:DeviceRepository, getDeviceDataService: GetDeviceDataService):
        self.input = input
        self.deviceRepository = deviceRepository
        self.getDeviceDataService = getDeviceDataService

    def execute(self):
        devices = self.deviceRepository.getDevices()

        for device in devices:
            device["value"] = self.getDeviceDataService.execute(device["deviceId"])

        return devices