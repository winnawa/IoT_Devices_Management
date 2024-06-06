import json
from flask import request
from app.api_errors.bad_request_exception import BadRequestException
from app.devices import bp
from app.devices.usecases.create_device_usecase import CreateDeviceUsecaseInput, CreateDeviceUsecase
from app.devices.usecases.delete_device_information_usecase import DeleteDeviceInformationUsecase, DeleteDeviceInformationUsecaseInput
from app.devices.usecases.get_device_information_usecase import GetDeviceInformationUsecase, GetDeviceInformationUsecaseInput
from app.devices.usecases.get_devices_information_usecase import GetDevicesInformationUsecaseInput, GetDevicesInformationUsecase
from app.devices.dependency_injections.dependency_container import deviceRepository

@bp.route('/', methods=['GET'])
def getDevices():
    # in the future, the query param can be pass to getDeviceQueryObj
    getDevicesQueryObj = {}
    getDevicesInformationUsecaseInput = GetDevicesInformationUsecaseInput(getDevicesQueryObj)
    getDevicesInformationUsecase = GetDevicesInformationUsecase(getDevicesInformationUsecaseInput, deviceRepository)

    devices = getDevicesInformationUsecase.execute()
    return json.dumps(
    {
        "message": "get devices success",
        "devices": devices
    }), 200, {'ContentType':'application/json'}

@bp.route('/<deviceId>', methods=['GET'])
def getDevice(deviceId):
    # in the future, the query param can be pass to getDeviceQueryObj
    getDeviceQueryObj = {}
    getDeviceInformationUsecaseInput = GetDeviceInformationUsecaseInput(deviceId,getDeviceQueryObj)
    getDeviceInformationUsecase = GetDeviceInformationUsecase(getDeviceInformationUsecaseInput, deviceRepository)

    device = getDeviceInformationUsecase.execute()
    return json.dumps(
    {
        "message": "get device success",
        "device": device
    }), 200, {'ContentType':'application/json'}

@bp.route('/<deviceId>', methods=['DELETE'])
def deleteDevice(deviceId):
    # in the future, the query param can be pass to getDeviceQueryObj
    deleteDeviceQueryObj = {}
    deleteDeviceInformationUsecaseInput = DeleteDeviceInformationUsecaseInput(deviceId,deleteDeviceQueryObj)
    deleteDeviceInformationUsecase = DeleteDeviceInformationUsecase(deleteDeviceInformationUsecaseInput, deviceRepository)

    device = deleteDeviceInformationUsecase.execute()
    return json.dumps(
    {
        "message": "delete device success",
        "device": device
    }), 200, {'ContentType':'application/json'}


@bp.route('/', methods=['POST'])
def createDevice():
    try:
        createDeviceObj = {}
        request_data = request.get_json()
        for key in request_data.keys():
            createDeviceObj[key] = request_data[key]

        createDeviceUsecaseInput = CreateDeviceUsecaseInput(createDeviceObj)
        createDeviceUsecase = CreateDeviceUsecase(createDeviceUsecaseInput, deviceRepository)

        device = createDeviceUsecase.execute()
        return json.dumps(
        {
            "message": "add device success",
            "device": device
        }), 200, {'ContentType':'application/json'}
    except BadRequestException as error:
        return json.dumps(
        {
            "message": error.message,
        }), error.statusCode, {'ContentType':'application/json'}
    except Exception as error:
        return json.dumps(
        {
            "message": error,
        }), 500, {'ContentType':'application/json'}