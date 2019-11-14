import pickle
import sys

# definition

work_path = '/home/kmj-labmen-007/Data1/Project/Code/HyperReco/groupActivity_GCN'
data_path = work_path + '/data'
volleyballdata_path = data_path + '/volleyball'

all_tracks = pickle.load(open(volleyballdata_path + '/tracks_normalized.pkl', 'rb'))

print(type(all_tracks))