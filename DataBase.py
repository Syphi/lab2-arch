#import json
# import pickle
# import yaml
operation_0 = {'sign': '+',
               'summary': 200,
               'dd': 16, 'mm': 1, 'yy': 2016,
               'comment': "salary"}
operation_1 = {'sign': '+',
               'summary': 35,
               'dd': 8, 'mm': 3, 'yy': 2016,
               'comment': "debt"}
operation_2 = {'sign': '-',
               'summary': 1500,
               'dd': 16, 'mm': 5, 'yy': 2016,
               'comment': "B'day"}

Operation_History = [operation_0, operation_1, operation_2]

# with open('ser.yaml', 'w') as f:
#     yaml.dump(Operation_History, f)

# with open('ser.pickle', 'wb') as f:
#     pickle.dump(Operation_History, f)

#with open('ser.json', 'w') as f:
#     json.dump(Operation_History, f)