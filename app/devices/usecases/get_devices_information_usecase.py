from app.devices.repositories.device_repository import DeviceRepository
from app.devices.services.mqtt_broker_services.get_device_datas_service import GetDeviceDatasService
class GetDevicesInformationUsecaseInput:
    def __init__(self,inputObj):
        self.inputObj = inputObj
class GetDevicesInformationUsecase:
    def __init__(self, input : GetDevicesInformationUsecaseInput, deviceRepository:DeviceRepository, getDeviceDatasService: GetDeviceDatasService):
        self.input = input
        self.deviceRepository = deviceRepository
        self.getDeviceDatasService = getDeviceDatasService

    def execute(self):
        devices = self.deviceRepository.getDevices()

        deviceDatas = self.getDeviceDatasService.execute()
        for device in devices:
            device["value"] = deviceDatas[device["deviceId"]] if device["deviceId"] in deviceDatas else None

        return devices