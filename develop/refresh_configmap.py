import os

os.environ['CONFIG_FILE_PATH'] = "/Users/varun.tomar/Documents/personal_github/monitoring/prometheus/config"
os.environ['RULES_FILE_PATH'] = "/Users/varun.tomar/Documents/personal_github/monitoring/prometheus/rules"
os.environ['STATIC_FILE_PATH'] = "/Users/varun.tomar/Documents/personal_github/monitoring/prometheus/static-files"

CONFIG_FILE_PATH = os.environ['CONFIG_FILE_PATH']
RULES_FILE_PATH = os.environ['RULES_FILE_PATH']
STATIC_FILE_PATH = os.environ['STATIC_FILE_PATH']

list_of_directories = [CONFIG_FILE_PATH, RULES_FILE_PATH, STATIC_FILE_PATH]


def get_files_of_files(extra: str) -> str:
    list_of_files = []
    for i in list_of_directories:
        for root, dirname, files in os.walk(i, followlinks=True):
            list_of_files.append(['--from-file=' + os.path.join(root, x) for x in files if x.endswith('.yaml')])
    flat_list = [item for sublist in list_of_files for item in sublist]
    return extra + ' '. join(flat_list)


print(get_files_of_files('kubectl create configmap prometheus-config -n devops '))
