import dataclasses
from dataclasses import dataclass
from typing import Optional, Dict, List

from config_controller.defs import ModuleConfig
from modules.base import BaseModule
from modules.defs import TreasuryBankAccountSubmodules
from modules.get_transfer_history import GetTransferHistoryModule, GetTransferHistory


@dataclass
class GetTreasuryBankAccountModule(ModuleConfig):
    enabled: bool = False
    parameters: Optional[Dict] = None
    submodules: Optional[List] = dataclasses.field(default_factory=lambda: [
        GetTransferHistoryModule
    ])


class GetTreasuryBankAccount(BaseModule):
    def __init__(self, config):
        super(GetTreasuryBankAccount, self).__init__(config)

    def execute(self, args, submodules: TreasuryBankAccountSubmodules):
        self.__repr__()
        if not self.should_execute:
            print('Skip')
            return 'mocked merchant data'

        # invoke RPC calls and return
        print('Execute')
        print(self.submodules)

        # [MODULE] GET_TRANSFER_HISTORY
        transfer_history = submodules.get_transfer_history.execute()

        return 'real merchant data'