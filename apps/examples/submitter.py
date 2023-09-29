import argparse
import os
import importlib.util

def get_args():
  parser = argparse.ArgumentParser(description="Submitter")

  parser.add_argument("--app", type=str, help="name of the app to run", required=True)
  parser.add_argument("--config", type=str, default="", help="config to be executred by the app")
  
  parser.add_argument("--local", action="store_true", default=False, help="run locally")
  parser.add_argument("--condor", action="store_true", default=False, help="run on condor")
  
  parser.add_argument("--files_config", type=str, default="", help="path to a python config with a list of input/output paths")

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
    print("\n\nSubmitting to condor")
    command = f"condor_submit {app_name}.jdl"
    os.system(command)
  else:
    print("Please select either --local or --condor")
    exit()
  

if __name__ == "__main__":
  main()
