import sys
sys.path.append("D:\\akshay\\script")
import maya.cmds as cmds


'''
import listdiret as ld
ld.listdiret()
print 'listdiret executed'
'''


import createctrl as cc
reload (cc)

#create ik arm 
#first select root joint
#run following command
ik,jntList,ctrl,poleVCtrl=cc.makeIkArm(cmds.ls(sl=1),"right","arm")


#place arm controller at end joint and make frezee transformation
tmpCont = cmds.pointConstraint(jntList[-1],ctrl,maintainOffset=False)
cmds.delete(tmpCont)
cmds.makeIdentity(ctrl,apply=True,t=1,n=1,r=1,s=1)



#get the mid joint and place it behind the joint using getattar and setattar
mid=int(len(jntList)/2)
tmpCont = cmds.pointConstraint(jntList[mid],poleVCtrl,maintainOffset=False)
cmds.delete(tmpCont)
val=cmds.getAttr(poleVCtrl[0]+'.translateZ')
cmds.setAttr(poleVCtrl[0]+'.translateZ',val-5)
cmds.makeIdentity(poleVCtrl,apply=True,t=1,n=1,r=1,s=1)

#make parent constraint
cmds.parentConstraint(ctrl,ik,mo=0)

#make pole vector conatraint
cmds.poleVectorConstraint(poleVCtrl,ik,w=1)


