# LINK MAP
{
'world_link': <urdf_parser_py.urdf.Link object at 0x7ff7eb13e550>,
'calib_lwr_arm_base_link': <urdf_parser_py.urdf.Link object at 0x7ff7eb13e650>, 
'lwr_arm_1_link': <urdf_parser_py.urdf.Link object at 0x7ff7eb13e6d0>,
'lwr_arm_2_link': <urdf_parser_py.urdf.Link object at 0x7ff7eb13e750>, 
'lwr_arm_3_link': <urdf_parser_py.urdf.Link object at 0x7ff7eb15fa90>, 
'lwr_arm_4_link': <urdf_parser_py.urdf.Link object at 0x7ff7eb15fb90>,
'lwr_arm_5_link': <urdf_parser_py.urdf.Link object at 0x7ff7eb15aad0>,
'lwr_arm_6_link': <urdf_parser_py.urdf.Link object at 0x7ff7eb15abd0>,  
'lwr_arm_7_link': <urdf_parser_py.urdf.Link object at 0x7ff7eb144f50>
}


# PARENT MAP
{'lwr_arm_3_link': ('lwr_arm_2_joint', 'lwr_arm_2_link'), 'lwr_arm_4_link': ('lwr_arm_3_joint', 'lwr_arm_3_link'), 'calib_lwr_arm_base_link': ('world_link_lwr_arm_base_joint', 'world_link'), 'lwr_arm_2_link': ('lwr_arm_1_joint', 'lwr_arm_1_link'), 'lwr_arm_6_link': ('lwr_arm_5_joint', 'lwr_arm_5_link'), 'lwr_arm_5_link': ('lwr_arm_4_joint', 'lwr_arm_4_link'), 'lwr_arm_1_link': ('lwr_arm_0_joint', 'calib_lwr_arm_base_link'), 'lwr_arm_7_link': ('lwr_arm_6_joint', 'lwr_arm_6_link')}


# CHILD MAP
{'lwr_arm_3_link': ('lwr_arm_2_joint', 'lwr_arm_2_link'), 'lwr_arm_4_link': ('lwr_arm_3_joint', 'lwr_arm_3_link'), 'calib_lwr_arm_base_link': ('world_link_lwr_arm_base_joint', 'world_link'), 'lwr_arm_2_link': ('lwr_arm_1_joint', 'lwr_arm_1_link'), 'lwr_arm_6_link': ('lwr_arm_5_joint', 'lwr_arm_5_link'), 'lwr_arm_5_link': ('lwr_arm_4_joint', 'lwr_arm_4_link'), 'lwr_arm_1_link': ('lwr_arm_0_joint', 'calib_lwr_arm_base_link'), 'lwr_arm_7_link': ('lwr_arm_6_joint', 'lwr_arm_6_link')}
                # name,             type            axis         origin(transltn)   rot (rpy)
('Joints', [0], 'world_link_lwr_arm_base_joint', 'fixed', None, [0.0, 0.0, 0.2], [0.0, 0.0, 0.0])
('Joints', [1], 'lwr_arm_0_joint', 'revolute', [0.0, 0.0, 1.0], [0.0, 0.0, 0.11], [0.0, 0.0, 0.0])
('Joints', [2], 'lwr_arm_1_joint', 'revolute', [0.0, 1.0, 0.0], [0.0, 0.0, 0.2005], [0.0, 0.0, 0.0])
('Joints', [3], 'lwr_arm_2_joint', 'revolute', [0.0, 0.0, 1.0], [0.0, 0.0, 0.2], [0.0, 0.0, 0.0])
('Joints', [4], 'lwr_arm_3_joint', 'revolute', [0.0, -1.0, 0.0], [0.0, 0.0, 0.2], [0.0, 0.0, 0.0])
('Joints', [5], 'lwr_arm_4_joint', 'revolute', [0.0, 0.0, 1.0], [0.0, 0.0, 0.2], [0.0, 0.0, 0.0])
('Joints', [6], 'lwr_arm_5_joint', 'revolute', [0.0, 1.0, 0.0], [0.0, 0.0, 0.19], [0.0, 0.0, 0.0])
('Joints', [7], 'lwr_arm_6_joint', 'revolute', [0.0, 0.0, 1.0], [0.0, 0.0, 0.078], [0.0, 0.0, 0.0])


# Joint Values
header: 
  seq: 21517
  stamp: 
    secs: 1586321762
    nsecs: 649778120
  frame_id: ''
name: [lwr_arm_0_joint, lwr_arm_1_joint, lwr_arm_2_joint, lwr_arm_3_joint, lwr_arm_4_joint,
  lwr_arm_5_joint, lwr_arm_6_joint]
position: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
velocity: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
effort: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


# link names
calib_lwr_arm_base_link
lwr_arm_1_link
lwr_arm_2_link
lwr_arm_3_link
lwr_arm_4_link
lwr_arm_5_link
lwr_arm_6_link
lwr_arm_7_link
