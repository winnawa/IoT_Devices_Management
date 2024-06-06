from peewee import *
from datetime import datetime
from app.dataConnection import  Device

class DeviceRepositoryUtils:
    @staticmethod
    def createUpdateDeviceObj(updateDeviceInput):
        updateDeviceObj={}
        for key in updateDeviceInput:
            addOnObj = {Device[key]: updateDeviceInput[key]}
            updateDeviceInput.update(addOnObj)
        return updateDeviceObj

    def mapToDeviceDomainModel(devices : list):
        deviceDomainModels = []
        for device in devices:
            deviceDomainModels.append({
                'name': device.name,
                'deviceId': device.deviceId,
                'deviceType': device.deviceType,
                'createdDate': device.createdDate,
                'id': device.id
            })
        return deviceDomainModels
    
class DeviceRepository:
    def __init__(self):
        pass

    def createDevice(self,createDeviceInput):
        try:
            currentUtcTime = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            newDevice = Device(name=createDeviceInput["name"], deviceId = createDeviceInput["deviceId"], deviceType = createDeviceInput["deviceType"], createdDate = currentUtcTime, lastModifiedDate = currentUtcTime)
            if newDevice.save() > 0:
                print(createDeviceInput["deviceId"])
                deviceDataModel = Device.get(Device.deviceId == createDeviceInput["deviceId"])
                
                deviceDomainModel = DeviceRepositoryUtils.mapToDeviceDomainModel([deviceDataModel])[0]
                
                return deviceDomainModel
            return None
        except Exception as error:
            print(error, "inside create device deviceRepository")
    
    def updateDevice(self,deviceId,updateDeviceInput):
        try:
            currentUtcTime = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            
            updateObj = DeviceRepositoryUtils.createUpdateDeviceObj(updateDeviceInput)
            updateObj.update({
                Device.lastModifiedDate: currentUtcTime
            })

            q = (Device
                .update(updateObj)
                .where(Device.deviceId == deviceId))
            q.execute()

            deviceDataModel = Device.get(Device.deviceId == deviceId)
            deviceDomainModel = DeviceRepositoryUtils.mapToDeviceDomainModel([deviceDataModel])[0]
            return deviceDomainModel

        except Exception as error:
            print(error, "inside update device deviceRepository")

    def getDevice(self,deviceId):
        try:
            deviceDataModel = Device.get_or_none(Device.deviceId == deviceId)
            if deviceDataModel is not  None:
                deviceDomainModel = DeviceRepositoryUtils.mapToDeviceDomainModel([deviceDataModel])[0]
                return deviceDomainModel
            return None
        except Exception as error:
            print(error, "inside get device DeviceRepository")

    def getDevices(self):
        try:
            query = Device.select()
            deviceDataModels=[]
            for device in query:
                deviceDataModels.append(device)

            deviceDomainModels = DeviceRepositoryUtils.mapToDeviceDomainModel(deviceDataModels)
            return deviceDomainModels

        except Exception as error:
            print(error)

    def deleteDevice(self,deviceId):
        try:
            device = Device.get(Device.deviceId == deviceId)
            device.delete_instance()
        except Exception as error:
            print(error)
