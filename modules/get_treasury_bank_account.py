import dataclasses
from dataclasses import dataclass
from typing import Optional, Dict, List

from config_controller.defs import ModuleConfig
from modules.base import BaseModule
from modules.get_transfer_history import GetTransferHistoryModule, GetTransferHistory


# @dataclass
# class GetTreasuryBankAccountModule(ModuleConfig):
#     enabled: bool = False
#     parameters: Optional[Dict] = None
#     submodules: Optional[Dict[str, GetTransferHistoryModule]] = dataclasses.field(default_factory=lambda: {
#         'get_transfer_history': GetTransferHistoryModule
#     })

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
        # self.submodules: GetTransferHistoryModule

    def execute(self, get_transfer_history: GetTransferHistory):
        self.__repr__()
        if not self.should_execute:
            print('Skip')
            return 'mocked merchant data'

        # invoke RPC calls and return
        print('Execute')

        treasury_account = get_transfer_history.execute()

        return 'real merchant data'

