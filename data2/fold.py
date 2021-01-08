import os
import shutil

machines = os.listdir('./machines')

print(machines)

for machine in machines:
    os.mkdir("./machines/"+machine.replace(".pdf", ""))
    shutil.move('./machines/'+machine, './machines/' + machine.replace(".pdf", ""))
