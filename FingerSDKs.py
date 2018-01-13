import maya.cmds as cmds

DRIVER_VALUES = [0, 10, -10]
fingers = ["index", "pinky", "ring", "middle"]
finger_joints = ["proximal", "mid", "distal"]

prefixes = ["l", "r"]
separetor = "_"

def getDrivers():
    driversList = []
    for i in prefixes:
        for j in fingers:
            driversList.append((i + separetor + j))
    return driversList

def getDrivens(sort="flat"):
    if sort == "flat":
        driversList = []
        for p in prefixes:
            for finger in fingers:
                for joint in finger_joints:
                    driversList.append((p + separetor + finger + separetor + joint))
        return driversList

def getDriverDriven():
    drivenList = {}
    for p in prefixes:
        for finger in fingers:
            local_fingers = []
            for joint in finger_joints:
                local_fingers.append(p + separetor + finger + separetor + joint)
            drivenList[p + separetor + finger] = local_fingers

    return drivenList


def getBendDrivers():
    bendAttributes = ["bend_1", "bend_2", "bend_3"]
    list = []
    for prefix in prefixes:
        for finger in fingers:
            for attr in bendAttributes:
                list.append(prefix + separetor + finger + "." + attr)
    return list

def getBendDrivens():
    list = []
    for prefix in prefixes:
        for finger in fingers:
            for joint in finger_joints:
                list.append(prefix + separetor + finger + separetor + joint)
    return list

def getBendDriverDrivens():
    return zip(getBendDrivers(), getBendDrivens())

driverDrivens = getDriverDriven()

data = {
    "curl": {
        "attribute": "rotateZ",
        "drivenValues": [
            [0, -90, 75],
            [0, -90, 15],
            [0, -100, 5]
        ]
    },
    "scrunch": {
        "attribute": "rotateZ",
        "drivenValues": [
            [0, 45, -15],
            [0, -90, 11],
            [0, -100, 25]
        ]
    },
    "twist": {
        "attribute": "rotateX",
        "drivenValues": [
            [0, -50, 50]
        ]
    },
    "spread": {
        "attribute": "rotateY",
        "drivenValues": [
            [0, -50, 50]
        ]
    }
}


def setMultipleSDKs(driven, attr, drivenValus, driver, driverValues=DRIVER_VALUES):
        if(len(drivenValus) != len(driverValues)):
            print("Driver and driven value's length mismatch. ")
            return
        else:
            zippedDriverDrivenValus = zip(driverValues, drivenValus)
            for i in zippedDriverDrivenValus:
                cmds.setDrivenKeyframe(driven + "." + attr,
                                       currentDriver=driver,
                                       driverValue=i[0],
                                       value=i[1]
                                       )


def createFingerSDK(drivenJoints, driver, data):
    for i in zip(drivenJoints, data["drivenValues"]):
        setMultipleSDKs(i[0], data["attribute"], i[1], driver)


def createFingerSDKs():
    for key in data:
        for driver in driverDrivens:
            createFingerSDK(driverDrivens[driver][0: len(data[key]["drivenValues"])], driver + "." + key , data[key])


def setMultipleBendSDKs(driver, driven, drivenValues=[0,90,-90]):
    for (driverVal, drivenVal) in zip(DRIVER_VALUES, drivenValues):
        cmds.setDrivenKeyframe(driven + "." + "rotateZ",
                               currentDriver=driver,
                               driverValue=driverVal,
                               value=drivenVal
                               )


def createFingerBendSDKs():
    for (dr, dv) in getBendDriverDrivens():
        setMultipleBendSDKs(dr, dv)

def createAllFingerSDK():
    createFingerBendSDKs()
    createFingerSDKs()

createAllFingerSDK()