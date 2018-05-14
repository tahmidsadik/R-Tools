import pymel.core as pm
import pymel.core.datatypes as dt


class JointSplitter:
    def __init__(self):
        pass

    error_messages = {
        "emptySelection": "You must select two joints to use this command. Currently Nothing is selected",
        "exceedSelection": "Exactly two joints must be selected to use this command. Currently more than two objects are selected",
        "incorrectObjectSelection": "Your selection contains objects that are not joints. You need to select joints to use this command.",
        "notEnoughJoint": "This command requires two joints to be selected. Currently only one object is selected"
    }

    @staticmethod
    def validate_for_split_joint(sl):
        if not sl:
            pm.windows.confirmDialog(message=JointSplitter.error_messages["emptySelection"], button=["Okay"])
            return False
        elif len(sl) > 2:
            pm.windows.confirmDialog(message=JointSplitter.error_messages["exceedSelection"], button=["Okay"])
            return False
        elif len(sl) == 1:
            pm.windows.confirmDialog(message=JointSplitter.error_messages["notEnoughJoint"], button=["Okay"])
            return False
        elif pm.objectType(sl[0], isType="joint") and pm.objectType(sl[1], isType="joint"):
            return True
        else:
            pm.windows.confirmDialog(message=JointSplitter.error_messages["incorrectObjectSelection"], button=["Okay"])
            return False

    @staticmethod
    def split_joints(first_joint, second_joint, n=5):
        if not (first_joint or second_joint):
            return -1
        JointSplitter.flatten_joints(first_joint, second_joint)
        fj = pm.joint(first_joint, query=True, position=True)
        lj = pm.joint(second_joint, query=True, position=True)
        fj_vector = dt.Vector(fj[0], fj[1], fj[2])
        lj_vector = dt.Vector(lj[0], lj[1], lj[2])
        new_joint = None
        pm.select(deselect=True)
        for i in range(0, n - 1):
            split_point = fj_vector.__mul__((n - i - 1.0) / n).__add__(lj_vector.__mul__(i + 1.0) / n)
            new_joint = pm.insertJoint(new_joint if i > 0 else first_joint)
            pm.joint(new_joint, edit=True, component=True, position=split_point)
        pm.select(d=True)

    @staticmethod
    def flatten_joints(parent_joint, child_joint):
        """ deletes all joints between parent and child joints"""
        pm.parent(child_joint, world=True)
        x = pm.listRelatives(parent_joint, children=True)
        for i in x:
            print(i)
            pm.delete(i)
        pm.parent(child_joint, parent_joint)
