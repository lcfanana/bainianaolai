import yaml
import os


def analyze_file(filename,datakey):
    list_data=list()
    with open("." + os.sep+"data" +os.sep + filename,"r",encoding="UTF-8")as f:
        data=yaml.load(f)
        data2=data[datakey]
        for i in data2.values():
            list_data.append(i)
    return list_data