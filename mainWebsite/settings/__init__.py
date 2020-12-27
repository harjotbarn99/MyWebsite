import os
if (os.environ.get("PRODUCTION") == "True"):
    print("this is production------------------------------------------ ")
    from .prod import *
else:
    print("this is development------------------------------------------- ")
    from .prod import *
# from .prod import *