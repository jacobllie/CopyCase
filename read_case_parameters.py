import json
import os

path = "C:\\temp\\tempexport"
files = os.listdir(path)

file = [f for f in files if "case_parameters" in f][0]

case_parameters = json.load(open(os.path.join(path,file)))
json_formatted_str = json.dumps(case_parameters, indent=2)
print(json_formatted_str)
#for k in case_parameters:
#    print(case_parameters[k])
