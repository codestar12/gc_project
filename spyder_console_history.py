#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:33:02 2017

@author: codyb
"""

# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

##---(Wed Nov 29 10:07:52 2017)---
import pandas as pd
import numpy as np
server_usage = pd.read_csv("/home/codyblakeney/private/personal_repo/gc_project/data/server_usage.csv")
container_usage = pd.read_csv("/home/codyblakeney/private/personal_repo/gc_project/data/container_usage.csv")
container_event = pd.read_csv("/home/codyblakeney/private/personal_repo/gc_project/data/container_event.csv")

##---(Wed Nov 29 13:37:22 2017)---
import pandas as pd
import numpy as np
container_event = pd.read_csv("/home/codyblakeney/private/personal_repo/gc_project/data/container_event.csv")
container_usage = pd.read_csv("/home/codyblakeney/private/personal_repo/gc_project/data/container_usage.csv")
server_usage = pd.read_csv("/home/codyblakeney/private/personal_repo/gc_project/data/server_usage.csv")
server_event = pd.read_csv("/home/codyblakeney/private/personal_repo/gc_project/data/server_event.csv")
server_event[server_event.timestamp != 0]
batch_instance = pd.read_csv("/home/codyblakeney/private/personal_repo/gc_project/data/batch_instance.csv")
sum(batch_instance.status == "Terminated")
sum(batch_instance.status == "Terminated") / len(batch_instance.status)
non_terminated = batch_instance[batch_instance.status != "Terminated"]

##---(Sat Dec  2 18:26:01 2017)---
import pandas as pd
import numpy as np

## ---(Sat Dec  2 19:07:15 2017)---
import pandas as pd
import numpy as np
service_containers = pd.read_csv("/home/codyblakeney/private/personal_repo/gc_project/data/container_event.csv")
service_cesinstan = pd.read_csv("/home/codyblakeney/private/personal_repo/gc_project/data/container_usage.csv.csv")
service_cesinstan = pd.read_csv("/home/codyblakeney/private/personal_repo/gc_project/data/container_usage.csv")
from service_machine.py import *
from service_machine import *
service_containers = pd.read_csv("/home/codyblakeney/private/personal_repo/gc_project/data/container_event.csv")
service_instance = pd.read_csv("/home/codyblakeney/private/personal_repo/gc_project/data/container_usage.csv")
machine_time_stamp = time_stamp_machine(39600,service_containers,service_instances)
machine_time_stamp = time_stamp_machine(39600,service_containers,service_instance)
machine_instance = pd.read_csv("/home/codyblakeney/private/personal_repo/gc_project/data/server_event.csv")
machine_instance = pd.read_csv("/home/codyblakeney/private/personal_repo/gc_project/data/server_usage.csv")
service_machine_usage = {}
for machine in machine_time_stamp:
    util = 0
    for instance in machine:
        util += instance["plan_cpu"] * instance["cpu_util]
    print(util / 64)
         
for machine in machine_time_stamp:
    util = 0
    for instance in machine:
        util += instance["plan_cpu"] * instance["cpu_util"]
    print(util / 64)
for machine in machine_time_stamp:
    util = 0
    for instance in machine_time_stamp[machine]:
        util += machine_time_stamp[instance]["plan_cpu"] * machine_time_stamp[instance]["cpu_util"]
    print(util / 64)
for machine in machine_time_stamp:
    util = 0
    for instance in machine_time_stamp[machine]:
        util += machine_time_stamp[machine][instance]["plan_cpu"] * machine_time_stamp[machine][instance]["cpu_util"]
    print(util / 64)
machine_util {}
machine_util = {}
for machine in machine_time_stamp:
    util = 0
    for instance in machine_time_stamp[machine]:
        util += machine_time_stamp[machine][instance]["plan_cpu"] * machine_time_stamp[machine][instance]["cpu_util"]
    machine_util[machine] = util / 64
machine_diff = {}
for machine in machine_util:
    machine_diff[machine] = machine_instance["machineId"].util_CPU - machine_util[machine]
for machine in machine_util:
    machine_diff[machine] = machine_instance["machineID"].util_CPU - machine_util[machine]
for machine in machine_util:
    machine_diff[machine] = machine_instance[np.logical_and(machine_instance.machineID==machine, timestamp==39600].util_CPU - machine_util[machine]
for machine in machine_util:
    machine_diff[machine] = machine_instance[np.logical_and(machine_instance.machineID==machine, timestamp==39600)].util_CPU - machine_util[machine]
for machine in machine_util:
    machine_diff[machine] = machine_instance[np.logical_and(machine_instance.machineID==machine, machine_instance.timestamp==39600)].util_CPU - machine_util[machine]
for machine in machine_util:
    machine_diff[machine] = flot(machine_instance[np.logical_and(machine_instance.machineID==machine, machine_instance.timestamp==39600)].util_CPU) - machine_util[machine]
for machine in machine_util:
    machine_diff[machine] = float(machine_instance[np.logical_and(machine_instance.machineID==machine, machine_instance.timestamp==39600)].util_CPU) - machine_util[machine]
import matplotlib.pyplot as plt
utils = machine_diff.values()
utils
p = plt.hist(utils)
utils
p = plt.hist(list(utils))
p = plt.hist(list(float(machine_instance[np.logical_and(machine_instance.machineID==machine, machine_instance.timestamp==39600)].util_CPU)))
p = plt.hist(machine_instance[machine_instance.timestamp==39600].util_CPU)
machine_service_totals = {}
p = plt.hist(machine_util.vale)
p = plt.hist(machine_util.values())
p = plt.hist(list(machine_util.values()))
sum(machine_util.values())
sum(machine_util.values()) / 13100
sum(machine_util.values())
p = plt.hist(list(machine_util.values()))
sum(machine_util.values())
sum(machine_util.values()) / 100
sum(machine_util.values()) / 100 / 1310
machine_util.values()[0]
list(machine_util.values())
list(machine_util.values())[0]
list(machine_util.values())[0] / 100
sum(machine_util.values())  / 1310
sum(machine_util.values())  / 13100
sum(machine_util.values())  / 1310
sum(machine_util.values())  
import statistics
statistics.median(machine_util.values())
max(machine_util.values())
min(machine_util.values())