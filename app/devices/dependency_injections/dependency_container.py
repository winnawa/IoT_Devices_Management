from app.devices.repositories.device_repository import DeviceRepository
from app.devices.services.mqtt_broker_services.get_device_data_service import GetDeviceDataService

deviceRepository = DeviceRepository()

getDeviceDataService = GetDeviceDataService()