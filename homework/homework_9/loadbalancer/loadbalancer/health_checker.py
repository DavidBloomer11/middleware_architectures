import requests
import time
import random


def check_health(instance):
    r = requests.get(instance)
    if r.status_code == 200:
        return True
    elif r.status_code == 500:
        return False
    
def health_checker(instances):
    
    while True:
        time.sleep(5)
        inst = []
        for i in instances:
            if check_health(i) == True:
                #Add instance to instance list
                inst.append(i + '\n')
        
        with open("instances.txt", "w") as f:
            f.writelines(inst)
        f.close()
        print('Available instances:')
        print(inst)

def get_instance():
    file = open('instances.txt')
    instances = file.readlines()
    length = len(instances)
    random_instance_number = random.randint(0,length-1)
    return instances[random_instance_number][:-1]


# Run the healthchecker
def run():
    instances = [
    'http://147.32.233.18:8888/MI-MDW-LastMinute1/list',
    'http://147.32.233.18:8888/MI-MDW-LastMinute2/list',
    'http://147.32.233.18:8888/MI-MDW-LastMinute3/list'
    ]   
    health_checker(instances)

