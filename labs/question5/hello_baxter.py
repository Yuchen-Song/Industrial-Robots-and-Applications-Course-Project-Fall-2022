
import rospy

import baxter_interface 

rospy.init_node('Hello_Baxter')

limb=baxter_interface.Limb('right')
l_limb=baxter_interface.Limb('left')
angles=limb.joint_angles()
l_angles=l_limb.joint_angles()
#print(angles)
#print(l_angles)
angles['right_s0']=0.0 
angles['right_s1']=0.0 
angles['right_e0']=0.0 
angles['right_e1']=0.0 
angles['right_w0']=0.0 
angles['right_w1']=0.0 
angles['right_w2']=0.0

l_angles['left_s0']=0.0 
l_angles['left_s1']=0.0 
l_angles['left_e0']=0.0 
l_angles['left_e1']=0.0 
l_angles['left_w0']=0.0 
l_angles['left_w1']=0.0 
l_angles['left_w2']=0.0

#print(angles)
#print(l_angles)
limb.move_to_joint_positions(angles)
l_limb.move_to_joint_positions(l_angles)

wave_1={'right_s0': -0.459,'right_s1': -0.202,'right_e0': 1.807,'right_e1': 1.714,'right_w0': -0.906,'right_w1': -1.545,'right_w2': -0.276}

wave_2={'right_s0': -0.395,'right_s1': -0.202,'right_e0': 1.831,'right_e1': 1.981,'right_w0': -1.979,'right_w1': -1.100,'right_w2': -0.448}

l_wave_1={'left_s0': 0.459,'left_s1': -0.202,'left_e0': -1.807,'left_e1': 1.714,'left_w0': 0.906,'left_w1': -1.545,'left_w2': 0.276}

l_wave_2={'left_s0': 0.395,'left_s1': -0.202,'left_e0': -1.831,'left_e1': 1.981,'left_w0': 1.979,'left_w1': -1.100,'left_w2': 0.448}
for _move in range(3): 
    limb.move_to_joint_positions(wave_1)
    l_limb.move_to_joint_positions(l_wave_1)  
    limb.move_to_joint_positions(wave_2)
    l_limb.move_to_joint_positions(l_wave_2) 
    

quit()
