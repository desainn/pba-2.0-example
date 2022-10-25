from config_controller.config_loader import UpdateMerchantConfig, update_merchant_config_loader
from endpoint_controller.base import ControllerBase
from modules.defs import TreasuryBankAccountSubmodules, GetMerchantSubmodules
from modules.get_financing_package import GetFinancingPackage
from modules.get_merchant import GetMerchant
from modules.get_transfer_history import GetTransferHistory
from modules.get_treasury_bank_account import GetTreasuryBankAccount


class UpdateMerchant(ControllerBase):
    def __init__(self, cfg: UpdateMerchantConfig):
        super(UpdateMerchant, self).__init__(cfg)
        self.mod_get_merchant = GetMerchant(cfg.get_merchant)
        self.mod_get_financing_package = GetFinancingPackage(cfg.get_financing_package)
        self.mod_get_treasury_bank_account = GetTreasuryBankAccount(cfg.get_treasury_bank_account)
        self.mod_get_transfer_history = GetTransferHistory(cfg.get_transfer_history)

    def execute(self):
        # [MODULE] GET_MERCHANT
        existing_merchant = self.mod_get_merchant.execute(
            args=None,
            submodules=GetMerchantSubmodules()
        )

        # [MODULE] GET_FINANCING_PACKAGE
        financing_package = self.mod_get_financing_package.execute()

        # [MODULE] GET_TREASURY_BANK_ACCOUNT
        treasury_account = self.mod_get_treasury_bank_account.execute(
            args=None,
            submodules=TreasuryBankAccountSubmodules(
                self.mod_get_transfer_history
            )
        )


