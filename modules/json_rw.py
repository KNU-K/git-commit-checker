import json
#./json/user.json
class JsonRW:
    def __init__(self, path):
      self.path = path
    def read(self, target):
        with open(self.path[target],'r') as read_file:
           decoded_data = json.load(read_file)
           return decoded_data