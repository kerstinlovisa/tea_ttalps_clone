import argparse
import os
import importlib.util
import uuid

def get_args():
  parser = argparse.ArgumentParser(description="Submitter")

  parser.add_argument("--app", type=str, help="name of the app to run", required=True)
  parser.add_argument("--config", type=str, default="", help="config to be executred by the app")
  
  parser.add_argument("--files_config", type=str, default="", help="path to a python config with a list of input/output paths")
  
  parser.add_argument("--local", action="store_true", default=False, help="run locally")
  parser.add_argument("--condor", action="store_true", default=False, help="run on condor")
  
  parser.add_argument(
    "--job_flavour", 
    type=str, 
    default="",
    help="condor job flavour: espresso (20 min), microcentury (1h), longlunch (2h), workday (8h), tomorrow (1d), testmatch (3d), nextweek (1w)"
  )
  parser.add_argument(
    "--resubmit_job", 
    type=int, 
    help="use this option to resubmitt a specific job"
  )
  
  parser.add_argument("--dry", action="store_true", default=False, help="dry run, without submitting to condor")
  
  args = parser.parse_args()
  return args

def run_locally_with_files_config(args, files_config):
  app_name = args.app
  executor = f"python " if app_name[-3:] == ".py" else f"./"
  command = f"{executor}{app_name} {args.config}"
  
  spec = importlib.util.spec_from_file_location("files_module", args.files_config)
  files_config = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(files_config)

  # check if files_config contains input_file_list variable
  if hasattr(files_config, "input_file_list"):
    print("Option 1")
    # option 1
    output_dir = files_config.output_dir
    input_file_list = files_config.input_file_list

    if not os.path.exists(output_dir):
      os.makedirs(output_dir)

    for input_file_path in input_file_list:
      input_file_name = input_file_path.strip().split("/")[-1]
      output_file_path = f"{output_dir}/{input_file_name}"
      command_for_file = f"{command} {input_file_path} {output_file_path}"
      
      print(f"\n\nExecuting {command_for_file=}")
      os.system(command_for_file)
  elif hasattr(files_config, "input_output_file_list"):
    print("Option 2")
    # option 2
    for input_file_path, output_file_path in files_config.input_output_file_list:
      command_for_file = f"{command} {input_file_path} {output_file_path}"
      print(f"\n\nExecuting {command_for_file=}")
      os.system(command_for_file)
  elif hasattr(files_config, "dataset"):
    print("Option 3")
    # option 3
    dataset_name = files_config.dataset
    output_dir = files_config.output_dir
    max_files = files_config.max_files
    
    # execute bash command and get output as a list of lines
    das_command = f"dasgoclient -query='file dataset={dataset_name}'"
    print(f"\n\nExecuting {das_command=}")
    input_files = os.popen(das_command).read().splitlines()
    
    for input_file_path in input_files[:max_files]:
      input_file_name = input_file_path.strip().split("/")[-1]
      output_file_path = f"{output_dir}/{input_file_name}"
      command_for_file = f"{command} {input_file_path} {output_file_path}"
      
      print(f"\n\nExecuting {command_for_file=}")
      os.system(command_for_file)
    
def create_condor_directories():
  if not os.path.exists("error"):
    os.makedirs("error")
  if not os.path.exists("log"):
    os.makedirs("log")
  if not os.path.exists("output"):
    os.makedirs("output")
  if not os.path.exists("tmp"):
    os.makedirs("tmp") 

def get_input_files(files_config):
  input_files = []
  
  if hasattr(files_config, "dataset"):
    dataset_name = files_config.dataset
    das_command = f"dasgoclient -query='file dataset={dataset_name}'"
    print(f"\n\nExecuting {das_command=}")
    input_files = os.popen(das_command).read().splitlines()
  elif hasattr(files_config, "input_directory"):
    input_directory = files_config.input_directory
    print(f"\n\nExecuting ls {input_directory}")
    # get list of all files in the input directory, together with their paths
    input_files = os.popen(f"find {input_directory} -name '*.root'").read().splitlines()
    
  return input_files

def main():
  args = get_args()
  
  app_name = args.app
  
  if args.local:
    print("Running locally")
    
    if args.files_config != "":
      run_locally_with_files_config(args, args.files_config)
    else:
      print(f"\n\nExecuting {command=}")
      os.system(command)
  elif args.condor:
    print("Running on condor")
    if args.job_flavour == "":
      print("Please provide a job flavour")
      exit()
    
    create_condor_directories()
    
    
    hash_string = str(uuid.uuid4().hex[:6])
    condor_config_name = f"tmp/condor_config_{hash_string}.sub"
    condor_run_script_name = f"tmp/condor_run_{hash_string}.sh"
    
    os.system(f"cp ../templates/condor_config.template.sub {condor_config_name}")
    os.system(f"cp ../templates/condor_run.template.sh {condor_run_script_name}")
    os.system(f"chmod 700 {condor_run_script_name}")
    
    print(f"Stored condor config at: {condor_config_name}")
    print(f"Stored run shell script at: {condor_run_script_name}")
    
    spec = importlib.util.spec_from_file_location("files_module", args.files_config)
    files_config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(files_config)
    
    input_files = get_input_files(files_config)
    
    # store input_files list in a file
    input_files_list_file_name = f"tmp/input_files_{hash_string}.txt"
    with open(input_files_list_file_name, "w") as file:
      for input_file_path in input_files:
        file.write(f"{input_file_path}\n")
    
    condor_run_script_name_escaped = condor_run_script_name.replace("/", "\/")
    
    voms_proxy_path = os.popen("voms-proxy-info -path").read().strip().replace("/", "\/")    
    os.system(f"cp {voms_proxy_path} voms_proxy")

    max_files = files_config.max_files if files_config.max_files != -1 else len(input_files)
    
    os.system(f"sed -i 's/<executable>/{condor_run_script_name_escaped}/g' {condor_config_name}")
    os.system(f"sed -i 's/<job_flavour>/{args.job_flavour}/g' {condor_config_name}")
    
    
    if args.resubmit_job is not None:
      os.system(f"sed -i 's/<$(ProcId)>/{args.resubmit_job}\/voms_proxy/g' {condor_config_name}")
      os.system(f"sed -i 's/<n_jobs>/{1}/g' {condor_config_name}")
      os.system(f"sed -i 's/<file_name>//g' {condor_run_script_name}")
    elif hasattr(files_config, "file_name"):
      file_name = files_config.file_name
      os.system(f"sed -i 's/<n_jobs>/{1}/g' {condor_config_name}")
      os.system(f"sed -i 's/<file_name>/--file_name {file_name}/g' {condor_run_script_name}")
    else:
      os.system(f"sed -i 's/<n_jobs>/{max_files}/g' {condor_config_name}")
      os.system(f"sed -i 's/<file_name>//g' {condor_run_script_name}")
    
    os.system(f"sed -i 's/<voms_proxy>/{voms_proxy_path}/g' {condor_run_script_name}")
    
    # set path to python executable
    python_executable = os.popen("which python").read().strip()
    python_executable = python_executable.replace("/", "\/")
    os.system(f"sed -i 's/<python_path>/{python_executable}/g' {condor_run_script_name}")
    
    # set the app and app config to execute
    os.system(f"sed -i 's/<app>/{app_name}/g' {condor_run_script_name}")
    os.system(f"sed -i 's/<config>/{args.config}/g' {condor_run_script_name}")
    
    # set path to the list of input files
    input_files_list_file_name_escaped = input_files_list_file_name.replace("/", "\/")
    os.system(f"sed -i 's/<input_files_list_file_name>/{input_files_list_file_name_escaped}/g' {condor_run_script_name}")
    
    # set output directory
    output_dir = files_config.output_dir.replace("/", "\/")
    os.system(f"sed -i 's/<output_dir>/{output_dir}/g' {condor_run_script_name}")
    
    if not args.dry:
      print("Submitting to condor")
      command = f"condor_submit {condor_config_name}"
      os.system(command)
    
  else:
    print("Please select either --local or --condor")
    exit()
  

if __name__ == "__main__":
  main()
