from config_controller.config_loader import update_merchant_config_loader
from endpoint_controller.update_merchant import UpdateMerchant

endpoint = UpdateMerchant(update_merchant_config_loader())
endpoint.execute()
