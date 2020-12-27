import os
try:
    print("\n****")
    print(os.environ.get("PRODUCTION"))
    print("****\n")
except:
    print("\n****")
    print("failed os var")
    print("****\n")

if (os.environ.get("PRODUCTION") == "False"):
    print("this is development------------------------------------------ ")
    from .dev import *
else:
    print("this is production------------------------------------------- ")
    from .prod import *
# from .prod import *