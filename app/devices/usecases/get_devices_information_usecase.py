from app.devices.repositories.device_repository import DeviceRepository

class GetDevicesInformationUsecaseInput:
    def __init__(self,inputObj):
        self.inputObj = inputObj
class GetDevicesInformationUsecase:
    def __init__(self, input : GetDevicesInformationUsecaseInput, deviceRepository:DeviceRepository):
        self.input = input
        self.deviceRepository = deviceRepository

    def execute(self):
        devices = self.deviceRepository.getDevices()
        return devices