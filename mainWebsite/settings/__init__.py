import os
if (os.environ.get("PRODUCTION") == "False"):
    print("this is development------------------------------------------ ")
    from .dev import *
else:
    print("this is production------------------------------------------- ")
    from .prod import *
