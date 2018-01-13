import maya.cmds as cmds

fkJoints = ['L_Uparm_FK_Joint', 'L_Lowarm_FK_Joint']
ikJoints = ['L_Uparm_IK_Joint', 'L_Lowarm_IK_Joint']

fkCtrls = ['L_Uparm_FK_Joint', 'L_Lowarm_FK_Joint']
ikHandCtrl = 'L_IK_Hand_Ctrl'
ikElbowCtrl = 'L_IK_Elbow_Loc'
ikfkSwitcherNode = 'L_IKFKCtrl'

# Put fk wrist and elbow locators here
fkLocators = ['L_FK_Hand_Position_Loc', 'L_FK_Elbow_Aim_Loc']

def matchObjects(fromObj, toObj):
    cmds.xform(toObj,
               translation=cmds.xform(fromObj, query=True, translation=True),
               rotation=cmds.xform(fromObj, query=True, rotation=True))


def matchFKtoIK():
    for (ik, fk) in zip(ikJoints, fkCtrls):
        matchObjects(ik, fk)


def matchIKtoFK():
    fromCtrls = [ikHandCtrl, ikElbowCtrl]
    for (fkLoc, ikCtrl) in zip(fkLocators, fromCtrls):
        matchObjects(fkLoc, ikCtrl)

def snapIKFK():
    if(cmds.getAttr(ikfkSwitcherNode + '.ik_fk_mode')):
        matchFKtoIK()
    else:
        matchIKtoFK()

cmds.scriptJob(runOnce=False, attributeChange=[ikfkSwitcherNode + '.ik_fk_mode', snapIKFK])
