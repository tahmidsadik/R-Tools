import maya.cmds as cmds


fkJoints = ['R_Uparm_FK_Joint', 'R_Lowarm_FK_Joint']
ikJoints = ['R_Uparm_IK_Joint', 'R_Lowarm_IK_Joint']

fkCtrls = ['R_Uparm_FK_Joint', 'R_Lowarm_FK_Joint']
ikHandCtrl = 'R_IK_Arm_Ctrl'
ikElbowCtrl = 'R_IK_Elbow_Ctrl'
ikfkSwitcherNode = 'R_IKFKCtrl'

# Put fk wrist and elbow locators here
fkLocators = ['R_FK_Hand_Position_Loc', 'R_FK_Elbow_Aim_Loc']

def matchObjects(fromObj, toObj):
    cmds.xform(toObj,
               translation=cmds.xform(fromObj, query=True, translation=True),
               rotation=cmds.xform(fromObj, query=True, rotation=True))


def RmatchFKtoIK():
    for fkCtrls_ikJointsPair in zip(ikJoints, fkCtrls):
        matchObjects(fkCtrls_ikJointsPair[0], fkCtrls_ikJointsPair[1])


def RmatchIKtoFK():
    fromCtrls = [ikHandCtrl, ikElbowCtrl]
    for i in zip(fkLocators, fromCtrls):
        matchObjects(i[0], i[1])

def RsnapIKFK():
    # the mode is an enum, 0 is ik and 1 ik fk

    if(cmds.getAttr(ikfkSwitcherNode + '.ik_fk_mode')):
        RmatchFKtoIK()
    else:
        RmatchIKtoFK()


cmds.scriptJob(runOnce=False, attributeChange=[ikfkSwitcherNode + '.ik_fk_mode', RsnapIKFK])
