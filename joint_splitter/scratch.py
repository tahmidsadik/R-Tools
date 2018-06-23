import pymel.core as pm

x = pm.listRelatives("joint1", ad=True)

# for i in range(1, len(x)):
#     pm.delete(x[i])

pm.parent(x[0], world=True)
pm.delete(x[-1])
pm.parent(x[0], "joint1")
