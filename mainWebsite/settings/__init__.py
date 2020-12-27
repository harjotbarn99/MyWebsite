import os
if (os.environ.get("PRODUCTION") == "True"):
    from .prod import *
    print("this is production ")
else:
    from .dev import *
# from .prod import *