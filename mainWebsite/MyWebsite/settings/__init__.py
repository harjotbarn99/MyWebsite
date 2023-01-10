import yaml
from pathlib import Path

src_path = Path(__file__).resolve().parent.parent.parent.parent
try : 
    with open(Path.joinpath(src_path, "config.yaml")) as f:
        config = yaml.safe_load(f)

    if config["App"]["prod"] :
        from .prod import *
    else :
        from .dev import *
except:
    from .dev import *