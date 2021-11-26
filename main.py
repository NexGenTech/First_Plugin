from Plugins.plugin import Plugin

class FirstPlugin(Plugin):

    def run(self):
        if self.is_activated:
            print("The First Plugin is being run")
        else:
            print("The First Plugin can not run because it is not activated")

# Inserts all the methods that their names do nopt start with a '_' into the globals() dictionary 
# so that they can be executed
import inspect
for name, member in inspect.getmembers(FirstPlugin(), inspect.ismethod):
    if not name.startswith('_'):
        globals()[name] = member