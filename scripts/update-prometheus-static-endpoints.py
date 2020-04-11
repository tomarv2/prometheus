import yaml
import in_place
import sys
from shutil import copyfile

job_name = sys.argv[1]
new_end_point = sys.argv[2]
sourcefile = '/mnt/monitoring/prometheus/static_files/' + job_name + '.yaml'

old_targets = []
new_targets = []
clean_list = []

print("taking backup of file...")
copyfile(sourcefile, sourcefile + '.bak')


def get_value(file_to_update, end_point):
    with open(file_to_update, 'r') as stream:
        out = yaml.load(stream)
        print("output as json: %s", out)
        if (out[0]['labels']['job']) == job_name:
            old_targets.append(out[0]['targets'])
            new_targets.append(end_point)


def update_values(file_to_update, old, new):
        with in_place.InPlace(file_to_update) as file:
            for line in file:
                line = line.replace(old, new)
                file.write(line)


get_value(sourcefile, new_end_point)
print("old targets: ", old_targets)
print("new targets: ", new_targets)
str2 = " ".join(str(x) for x in new_targets)
print(str2)
for i in old_targets:
    for j in i:
        clean_list.append(j)

print("".join(str(clean) for clean in clean_list))

print ("replacing values...")
update_values(sourcefile, ("".join(str(clean) for clean in clean_list)), str2)

