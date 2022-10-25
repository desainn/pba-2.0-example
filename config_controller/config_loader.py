import dataclasses
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional, Any, DefaultDict, List, Dict

import hydra
import yaml
from hydra.core.config_store import ConfigStore
from omegaconf import OmegaConf, MISSING, SCMode, ValidationError

from modules.get_financing_package import GetFinancingPackageModule
from modules.get_merchant import GetMerchantModule
from modules.get_transfer_history import GetTransferHistoryModule
from modules.get_treasury_bank_account import GetTreasuryBankAccountModule


@dataclass
class UpdateMerchantConfig:
    get_merchant: GetMerchantModule = GetMerchantModule()
    get_financing_package: GetFinancingPackageModule = GetFinancingPackageModule()
    get_treasury_bank_account: GetTreasuryBankAccountModule = GetTreasuryBankAccountModule()
    get_transfer_history: GetTransferHistoryModule = GetTransferHistoryModule()


# @hydra.main(version_base=None, config_path="configs/update_merchant", config_name="shopify_usa")
def update_merchant_config_loader():
    custom_config = []
    with open("config_controller/configs/update_merchant/shopify_usa.yaml", "r") as stream:
        try:
            custom_config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    schema = OmegaConf.structured(UpdateMerchantConfig)  # load proper config schema
    merged_config = OmegaConf.merge(schema, custom_config)
    cfg = OmegaConf.to_container(merged_config, throw_on_missing=True)  # validate configuration against schema
    cfg: UpdateMerchantConfig = OmegaConf.structured(cfg)

    print(OmegaConf.to_yaml(cfg))

    return cfg