import pandas as pd
import numpy as np

def time_stamp_machine(ts, service_containers, service_instances):
    ids_at_ts = np.array(service_instances[service_instances.ts == ts].instance_id)
    machines = {}
    for ids in ids_at_ts:
        container = service_containers[service_containers.instance_id == ids]
        instance = service_instances[np.logical_and(service_instances.instance_id == ids, service_instances.ts==ts)]
        
        for machine in container.machine_id:
        	if machine not in machines:
        		machines[machine] = {}
	        	machines[machine][ids] = {
	        							"plan_cpu": int(np.array(container.plan_cpu)[0]),
	        							"plan_mem": float(np.array(container.plan_mem)[0]),
	        							"plan_disk": float(np.array(container.plan_disk)[0]),
	        							"cpu_set": str(np.array(container.cpuset)[0]).split("|"),
	        							"cpu_util": float(np.array(instance.cpu_util)[0]),
	        							"mem_util": float(np.array(instance.mem_util)[0]),
	        							"disk_util": float(np.array(instance.disk_util)[0]),
	        							"load1": float(np.array(instance.load1)[0]),
	        							"load5" : float(np.array(instance.load5)[0])
	        							
	        						}
	        else:
	        	machines[machine][ids] = {
	        							"plan_cpu": int(np.array(container.plan_cpu)[0]),
	        							"plan_mem": float(np.array(container.plan_mem)[0]),
	        							"plan_disk": float(np.array(container.plan_disk)[0]),
	        							"cpu_set": str(np.array(container.cpuset)[0]).split("|"),
	        							"cpu_util": float(np.array(instance.cpu_util)[0]),
	        							"mem_util": float(np.array(instance.mem_util)[0]),
	        							"disk_util": float(np.array(instance.disk_util)[0]),
	        							"load1": float(np.array(instance.load1)[0]),
	        							"load5" : float(np.array(instance.load5)[0])
	        							
	        						}

        
    return machines
        
    