from config_controller.defs import ModuleConfig


class BaseModule:
    def __init__(self, config: ModuleConfig):
        self.enabled = config.enabled
        self.parameters = config.parameters
        self.submodules = config.submodules
        self.should_execute = self.is_enabled()

    def __repr__(self):
        print('\n\n\n' + ('*' * 40))
        print('Module: {}'.format(self.__class__.__name__))
        print('Enabled: {}'.format(self.enabled))
        print('Parameters: {}'.format(self.parameters.__str__()))
        # print('Submodules: {}'.format(self.submodules.keys() if self.submodules else None))
        print('Submodules: {}'.format(self.submodules.__str__()))
        print(('*' * 40) + '\n')

    def is_enabled(self):
        if self.enabled:
            # call_logger_helper indicating the module will execute
            return True
        else:
            # call_logger_helper indicating the module will not execute
            return False
