#!/bin/bash

export X509_USER_PROXY=`pwd`/voms_proxy

job_number=$1
echo "Executing job number $job_number"
<python_path> condor_runner.py --app <app> --config <config> --input_files_file_name <input_files_list_file_name> --output_dir <output_dir> --file_index $job_number <file_name> <muon_SFs> <muonTrigger_SFs>
