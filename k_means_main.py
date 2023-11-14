from k_means import *


# data_file = "set1a.txt"
# data_file = "set2a.txt"
# data_file = "set2b.txt"
data_file ="set2c.txt"

K = 2
#initialization = "random"
initialization = "round_robin"


k_means(data_file, K, initialization)
