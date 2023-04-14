import json
my_dict = {'Number ' + str(x): x * x for x in range(10)}
print(json.dumps(my_dict, indent=2))