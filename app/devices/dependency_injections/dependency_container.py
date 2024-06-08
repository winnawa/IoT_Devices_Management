from app.devices.repositories.device_repository import DeviceRepository
from app.devices.services.mqtt_broker_services.get_device_datas_service import GetDeviceDatasService

deviceRepository = DeviceRepository()

getDeviceDatasService = GetDeviceDatasService()