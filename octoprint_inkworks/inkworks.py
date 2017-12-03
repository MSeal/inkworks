import octoprint.plugin

class InkworksPlugin(octoprint.plugin.SettingsPlugin, octoprint.plugin.StartupPlugin, octoprint.plugin.ShutdownPlugin):
    def on_startup(self, *args, **kwargs):
        self._logger.info("InkworksPlugin starting up")

    def on_after_startup(self, *args, **kwargs):
        self._logger.info("InkworksPlugin started up")

    def on_shutdown(self):
        pass

    def get_settings_defaults(self):
        return {}

    def get_update_information(self):
        return dict(
            inkworks=dict(
                displayName=self._plugin_name,
                displayVersion=self._plugin_version,

                type="github_release",
                current=self._plugin_version,
                user="MSeal",
                repo="inkworks",

                pip="https://github.com/MSeal/inkworks/archive/{target}.zip"
            )
        )