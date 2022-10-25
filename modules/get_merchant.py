from dataclasses import dataclass
from typing import Optional, List, Dict

from config_controller.defs.module_config import ModuleConfig
from modules.base import BaseModule


@dataclass
class GetMerchantModule(ModuleConfig):
    enabled: bool = True
    parameters: Optional[Dict] = None
    submodules: Optional[Dict] = None


class GetMerchant(BaseModule):
    def __init__(self, config):
        super(GetMerchant, self).__init__(config)

    def execute(self):
        self.__repr__()
        if not self.should_execute:
            print('Skip')
            return 'mocked merchant data'

        # invoke RPC calls and return
        print('Execute')
        return 'real merchant data'

