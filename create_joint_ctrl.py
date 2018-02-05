import pymel.core as pm

TEMP_NAME = "__TEMPNAME__"

def get_selected_transforms_shape():
    selectedNodes = pm.general.selected()
    ## Maybe nothing is selected, and we might get empty list
    if not selectedNodes:
        return None
    else:
        shapes = []
        for node in selectedNodes:
            shapes.append(node.getShape())
        return shapes


def create_single_rotation_ctrl(joint_node):
    cc = pm.circle()[0]
    cc.rename(TEMP_NAME)
    cc.getShape().rename(joint_node.nodeName() + "Shape")
    pm.select(cc.getShape(), joint_node)
    pm.parent(shape=True, relative=True)
    pm.delete(cc.nodeName())


def create_rotation_ctrl():
    selected_objects = pm.ls(selection=True)
    if not selected_objects:
        print "No joint is selected to create control for."
        return

    for joint in pm.ls(selection=True):
        create_single_rotation_ctrl(joint)
