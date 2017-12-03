import octoprint.plugin

from .inkworks import InkworksPlugin

__plugin_implementation__ = InkworksPlugin()
__plugin_hooks__ = {
	"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
}
