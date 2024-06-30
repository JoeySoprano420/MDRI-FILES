class Plugin:
    def execute(self, lines):
        raise NotImplementedError

class PluginManager:
    def __init__(self):
        self.plugins = []

    def register_plugin(self, plugin):
        self.plugins.append(plugin)

    def execute_plugins(self, lines):
        for plugin in self.plugins:
            plugin.execute(lines)

# Example plugin
class PrintPlugin(Plugin):
    def execute(self, lines):
        for line in lines:
            if line.startswith('|=|'):
                print(line[3:].strip())

plugin_manager = PluginManager()
plugin_manager.register_plugin(PrintPlugin())
