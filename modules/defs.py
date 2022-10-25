from typing import Optional

from modules.get_transfer_history import GetTransferHistory


class GetMerchantSubmodules:
    def __init__(self):
        pass


class TreasuryBankAccountSubmodules:
    def __init__(self, get_transfer_history=None):
        self.get_transfer_history: Optional[GetTransferHistory] = get_transfer_history
