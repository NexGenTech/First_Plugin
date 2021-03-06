from plugin import Plugin
import requests

ip_address= "192.168.1.235"

class FirstPlugin(Plugin):

    def run(self):
        if self.is_activated:
            print("The First Plugin is being run..")
            x = requests.get("https://" + ip_address)
            print(x.text)
        else:
            print("The First Plugin can not run because it is not activated")
'''
# Inserts all the methods that their names do not start with a '_' into the globals() dictionary 
# so that they can be executed
import inspect
for name, member in inspect.getmembers(FirstPlugin(), inspect.ismethod):
    if not name.startswith('_'):
        globals()[name] = member
'''
import sys
import json

if __name__ == '__main__':
    pl = json.loads(sys.argv[1])
    plugin = FirstPlugin(pl['id'], pl['active'], pl['name'], pl['description'],
                         pl['url'], pl['protocols'], pl['ports'])
    plugin.activate()
    #plugin.run()
    plugin.deactivate()