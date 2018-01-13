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


