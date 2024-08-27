#! /usr/bin/env python
import rospy
# Importa el servicio adecuado utilizado por /execute_trajectory
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest
import rospkg
rospack = rospkg.RosPack()
# Obtiene la ruta completa del archivo de trayectoria
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"
# Inicializa un nodo ROS llamado 'service_client'
rospy.init_node('service_client')
# Espera a que el servicio /execute_trajectory esté disponible
rospy.wait_for_service('/execute_trajectory')
# Crea la conexión al servicio /execute_trajectory
traj_by_trajectory_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj)
# Crea un objeto de tipo ExecTrajRequest
traj_by_trajectory_object = ExecTrajRequest()
# Asigna la ruta de la trayectoria al campo adecuado en la solicitud
traj_by_trajectory_object.file = traj
# Llama al servicio y envía la solicitud
result = traj_by_trajectory_service(traj_by_trajectory_object)
# Imprime el resultado devuelto por el servicio
print(result)