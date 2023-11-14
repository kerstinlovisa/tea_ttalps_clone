import ROOT
import os
import sys

base_path = "/nfs/dust/cms/user/jniedzie/ttalps_cms"

# sub_path = "skimmed_ttbarLike/histograms/"
sub_path = "skimmed_looseSemimuonic_tightMuon/"
# sub_path = "skimmed_ttbarSemimuonicCR_tightMuon/"
# sub_path = "skimmed_ttZSemimuonicCR_tightMuon_noLooseMuonIso/"

def count_events_in_files(files):
    n_events = 0
    
    for file in files:
        f = ROOT.TFile(file)
        t = f.Get("Events")
        n_events += t.GetEntries()
        f.Close()
    
    return n_events

def get_total_size_of_files(files):
    size = 0
    
    for file in files:
        size += os.path.getsize(file)
    
    return size

def count_files(input_path):
    paths = [d for d in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, d))]
    paths = sorted(paths)

    for path in paths:
        try:
            files = os.listdir(os.path.join(input_path, path, sub_path))
            
            # remove from files entries which are not files but directories
            files = [file for file in files if os.path.isfile(os.path.join(input_path, path, sub_path, file))]
            
            n_events = count_events_in_files([os.path.join(input_path, path, sub_path, file) for file in files])
            total_size = get_total_size_of_files([os.path.join(input_path, path, sub_path, file) for file in files])
            print(f"{path}: N files: {len(files)}, N events: {n_events}, size: {total_size/1024/1024/1024:.3f} GB".replace(".", ","))
        except:
            pass
    

if __name__ == "__main__":
    count_files(f"{base_path}/backgrounds2018")
    count_files(f"{base_path}/collision_data2018")
    count_files(f"{base_path}/signals")
    
