from typing import Optional, Dict


class ModuleConfig:
    enabled: bool = True
    parameters: Optional[Dict] = None
    submodules: Optional[Dict] = None