import maya.cmds as cmds

currentDistanceNodeName = "Current_Arm_LengthShape";
SDKDriver = currentDistanceNodeName + ".distance"

upArmJointName = "R_Lowarm_IK_Joint"
lowArmJointName = "R_Hand_IK_Joint"

upArmLength = cmds.getAttr(upArmJointName + ".translateX")
lowArmLength = cmds.getAttr(lowArmJointName + ".translateX")

armMaxDistance = upArmLength + lowArmLength
currentDistance = cmds.getAttr(currentDistanceNodeName + ".distance")

cmds.setDrivenKeyframe(upArmJointName + ".tx",
                       currentDriver=SDKDriver,
                       driverValue=armMaxDistance,
                       value=upArmLength)

cmds.setDrivenKeyframe(lowArmJointName + ".tx",
                       currentDriver=SDKDriver,
                       driverValue=armMaxDistance,
                       value=lowArmLength)

cmds.setDrivenKeyframe(upArmJointName + ".tx",
                       currentDriver=SDKDriver,
                       driverValue=armMaxDistance * 10,
                       value=upArmLength * 10)

cmds.setDrivenKeyframe(lowArmJointName + ".tx",
                       currentDriver=SDKDriver,
                       driverValue=armMaxDistance * 10,
                       value=lowArmLength * 10)

cmds.setDrivenKeyframe(upArmJointName + ".tx",
                       currentDriver=SDKDriver,
                       driverValue=0,
                       value=upArmLength)

cmds.setDrivenKeyframe(lowArmJointName + ".tx",
                       currentDriver=SDKDriver,
                       driverValue=0,
                       value=lowArmLength)