from app.devices.repositories.device_repository import DeviceRepository

class GetDeviceInformationUsecaseInput:
    def __init__(self,deviceId,inputObj):
        self.inputObj = inputObj
        self.deviceId = deviceId
class GetDeviceInformationUsecase:
    def __init__(self, input : GetDeviceInformationUsecaseInput, deviceRepository:DeviceRepository):
        self.input = input
        self.deviceRepository = deviceRepository

    def execute(self):
        deviceId = self.input.deviceId
        device = self.deviceRepository.getDevice(deviceId)
        return device