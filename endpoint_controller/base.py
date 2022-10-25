class ControllerBase:
    def __init__(self, partner_config):
        # Config from ConfigController
        self.partner_config = partner_config

    def validate(self, args):
        pass

    def execute(self):
        pass

