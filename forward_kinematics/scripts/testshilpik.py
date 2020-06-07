import numpy 
import geometry_msgs.msg 
import rospy 
from sensor_msgs.msg import JointState 
import tf 
import tf.msg 
import tf2_ros 
from urdf_parser_py.urdf import URDF 

        #make broadcaster
        broadcaster = tf2_ros.TransformBroadcaster()

        #initialize
        joints_list = []
        links_list = []

        more_links = True

        #make a list of all the links and joints 
        link = self.robot.get_root()
        world = self.robot.get_root()

        while more_links == True:

            (next_joint_name, next_link) = self.robot.child_map[link][0]
            joints_list = joints_list + [next_joint_name]
            links_list = links_list + [next_link]

            link = next_link

            if link not in self.robot.child_map:
                more_links = False

        endeffector = next_link

        num_link = len(links_list)
        #initialize tfMat with identity
        tfMat = tf.transformations.identity_matrix()

        #initialize again for transformations
        link = self.robot.get_root()

        #loop through all frames in the child map
        for x in range(num_link):
 
            #name of the frame after root
            (next_joint_name, next_link) = self.robot.child_map[link][0]

            #pull out object to get attributes from it
            next_joint = self.robot.joint_map[next_joint_name]

            #look up joint type
            if next_joint.type == 'revolute':

                #look up index of joint_values with matching name. Link names are used. 
                i = joint_values.name.index(joints_list[x])
                joint_position = joint_values.position[i]

                #multiply 
                tfMat_Trans = numpy.dot(tfMat, tf.transformations.translation_matrix(next_joint.origin.xyz))
                tfMat_Rot = numpy.dot(tfMat_Trans, tf.transformations.euler_matrix(next_joint.origin.rpy[0],next_joint.origin.rpy[1],next_joint.origin.rpy[2])) #note, no axis defined. 
                tfMat_Final = numpy.dot(tfMat_Rot, tf.transformations.rotation_matrix(joint_position, next_joint.axis))
                message = convert_to_message(tfMat_Final,next_link,world)

            else: #aka 'fixed' joint type
                #set rotation to identity
                tfMat_Trans = numpy.dot(tfMat, tf.transformations.translation_matrix(next_joint.origin.xyz))
                tfMat_Rot = numpy.dot(tfMat_Trans, tf.transformations.euler_matrix(next_joint.origin.rpy[0],next_joint.origin.rpy[1],next_joint.origin.rpy[2])) #no axis defined. 

                tfMat_Final = tfMat_Rot
                message = convert_to_message(tfMat_Final,next_link,world) 