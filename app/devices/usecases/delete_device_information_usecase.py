from app.devices.repositories.device_repository import DeviceRepository

class DeleteDeviceInformationUsecaseInput:
    def __init__(self,deviceId,inputObj):
        self.inputObj = inputObj
        self.deviceId = deviceId
class DeleteDeviceInformationUsecase:
    def __init__(self, input : DeleteDeviceInformationUsecaseInput, deviceRepository:DeviceRepository):
        self.input = input
        self.deviceRepository = deviceRepository

    def execute(self):
        deviceId = self.input.deviceId
        device = self.deviceRepository.deleteDevice(deviceId)
        return device