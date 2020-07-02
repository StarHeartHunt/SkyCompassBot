from GlobalConfig import *
from NetworkManager import *

def main():
    net_config = GlobalConfig()
    get_meta(net_config)
    get_weekly_schedule(net_config)
    
main()