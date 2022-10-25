import dataclasses
from dataclasses import dataclass
from typing import Optional, Dict, Any

from omegaconf import MISSING

from config_controller.defs.module_config import ModuleConfig
from modules.base import BaseModule


@dataclass
class GetTransferHistoryModule(ModuleConfig):
    enabled: bool = False
    parameters: Optional[Dict[str, str | int]] = dataclasses.field(default_factory=lambda: {
        'history_limit': 1
    })
    submodules: Optional[Dict] = None


class GetTransferHistory(BaseModule):
    def __init__(self, config):
        super(GetTransferHistory, self).__init__(config)

    def execute(self):
        self.__repr__()
        if not self.should_execute:
            print('Skip')
            return 'mocked merchant data'

        # invoke RPC calls and return
        print('Execute')

        return 'real merchant data'