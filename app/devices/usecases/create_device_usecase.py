from app.api_errors.bad_request_exception import BadRequestException
from app.devices.repositories.device_repository import DeviceRepository

class CreateDeviceUsecaseInput:
    def __init__(self,inputObj):
        self.inputObj = inputObj
class CreateDeviceUsecase:
    def __init__(self, input : CreateDeviceUsecaseInput, deviceRepository:DeviceRepository):
        self.input = input
        self.deviceRepository = deviceRepository

    def execute(self):
        createDeviceObj = self.input.inputObj

        newDeviceId = createDeviceObj["deviceId"]
        existingDevice = self.deviceRepository.getDevice(newDeviceId)
        if existingDevice is not None:
            raise BadRequestException('existed deviceId') 

        device = self.deviceRepository.createDevice(createDeviceObj)
        return device