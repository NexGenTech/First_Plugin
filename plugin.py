class Plugin:
    """
    The most simple interface to be inherited when creating a plugin.
    """

    def __init__(self, id: str, active: bool, name: str, description: str, url: str, protocols: list, ports: list) -> None:
        self.id = id
        self.active = active 
        self.name = name
        self.description = description
        self.url = url
        self.protocols = protocols
        self.ports = ports

    def activate(self):
        """
        Called at plugin activation.
        """
        self.is_activated = True
        print("The " + self.__class__.__name__ + " has been activated")

    def deactivate(self):
        """
        Called when the plugin is disabled.
        """
        self.is_activated = False
        print("The " + self.__class__.__name__ + " has been deactivated")

    def run(self):
        """
        This function executes the plugin if it is activated
        """