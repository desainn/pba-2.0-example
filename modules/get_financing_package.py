from dataclasses import dataclass
from typing import Optional, Dict

from config_controller.defs.module_config import ModuleConfig
from modules.base import BaseModule


@dataclass
class GetFinancingPackageModule(ModuleConfig):
    enabled: bool = False
    parameters: Optional[Dict] = None
    submodules: Optional[Dict] = None


class GetFinancingPackage(BaseModule):
    def __init__(self, config):
        super(GetFinancingPackage, self).__init__(config)

    def execute(self):
        self.__repr__()
        if not self.should_execute:
            print('Skip')
            return 'mocked merchant data'

        # invoke RPC calls and return
        print('Execute')
        return 'real merchant data'

