import ROOT
import os
import sys

sub_path = "skimmed_ttbarLike/histograms/"

def count_files(base_path):
    paths = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

    for path in paths:
        try:
            files = os.listdir(os.path.join(base_path, path, sub_path))
            print(f"{path}: {len(files)}")
        except:
            pass
    

if __name__ == "__main__":
    count_files("backgrounds2018")
    count_files("collision_data2018")
    count_files("signals")
    
