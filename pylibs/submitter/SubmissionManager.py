import os
import importlib.util
import uuid
from enum import Enum

from Logger import *

class SubmissionSystem(Enum):
  local = 1
  condor = 2
  unknown = 3

class SubmissionManager:
  def __init__(self, submission_system, app_name, config_path, files_config_path):
    self.app_name = app_name
    self.config_path = config_path
    self.files_config_path = files_config_path
    self.files_config = None
    
    info(f"Submission system: {submission_system.name}")
    
    self.__setup_files_config()

    self.applyMuonScaleFactors = None
    if hasattr(self.files_config, "applyMuonScaleFactors"):
      self.applyMuonScaleFactors = self.files_config.applyMuonScaleFactors
      
    self.applyMuonTriggerScaleFactors = None
    if hasattr(self.files_config, "applyMuonTriggerScaleFactors"):
      self.applyMuonTriggerScaleFactors = self.files_config.applyMuonTriggerScaleFactors

    if submission_system == SubmissionSystem.condor:
      self.__create_condor_directories()
  
  def run_locally(self):
    executor = f"python " if self.app_name[-3:] == ".py" else f"./"
    self.command = f"{executor}{self.app_name} {self.config_path}"
    
    if hasattr(self.files_config, "output_dir"): # option 1 & 3, 4, 5
      self.__run_local_with_output_dir()
    elif hasattr(self.files_config, "input_output_file_list"): # option 2
      self.__run_local_input_output_list()
    else:
      error("Unrecognized option")
  
  def run_condor(self, job_flavour, resubmit_job, dry):
    info("Running on condor")
    
    self.job_flavour = job_flavour
    self.resubmit_job = resubmit_job
    
    
    self.__setup_temp_file_paths()
    self.__copy_templates()
    
    input_files = self.__get_intput_file_list()
    self.__save_file_list_to_file(input_files)
    self.__set_condor_script_variables(len(input_files))
    self.__set_run_script_variables()
    
    command = f"condor_submit {self.condor_config_name}"
    info(f"Submitting to condor: {command}")
    
    if not dry:  
      os.system(command)
  
  def __create_dir_if_not_exists(self, dir_path):
    if not os.path.exists(dir_path):
      os.makedirs(dir_path)
  
  def __create_condor_directories(self):
    for path in ("error", "log", "output", "tmp"):
      self.__create_dir_if_not_exists(path)
    
  def __setup_files_config(self):
    if self.files_config_path is None:
      fatal("Please provide a files config")
      exit()
    
    info(f"Reading files config from path: {self.files_config_path}")
    spec = importlib.util.spec_from_file_location("files_module", self.files_config_path)
    self.files_config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(self.files_config)
  
  def __run_command(self, command):
    info(f"\n\nExecuting {command=}")
    os.system(command)
  
  def __get_das_files_list(self, dataset_name):
    das_command = f"dasgoclient -query='file dataset={dataset_name}'"
    info(f"\n\nExecuting {das_command=}")
    return os.popen(das_command).read().splitlines()
  
  def __get_intput_file_list(self):
    if hasattr(self.files_config, "dataset"):
      max_files = getattr(self.files_config, "max_files", -1)
      files = self.__get_das_files_list(self.files_config.dataset)
      if max_files > 0:
        return files[:max_files]
      return files
    
    if hasattr(self.files_config, "input_file_list"):
      return self.files_config.input_file_list
    
    if hasattr(self.files_config, "input_directory"):
      return os.popen(f"find {self.files_config.input_directory} -maxdepth 1 -name '*.root'").read().splitlines()
    
    fatal("Unrecognized option")
    exit()
  
  # option 1 & 3, 4, 5
  def __run_local_with_output_dir(self):
    
    input_file_list = self.__get_intput_file_list()
    
    if hasattr(self.files_config, "file_name"):
      file_name = self.files_config.file_name
      path = "/".join(input_file_list[0].strip().split("/")[:-1])
      input_file_list = [f"{path}/{file_name}"]
    
    max_files = -1
    if hasattr(self.files_config, "max_files"):
      max_files = self.files_config.max_files
    
    for i, input_file_path in enumerate(input_file_list):
      if max_files > 0 and i >= max_files:
        return
      
      input_file_name = input_file_path.strip().split("/")[-1]
      output_file_path = f"{self.files_config.output_dir}/{input_file_name}"
      command_for_file = f"{self.command} {input_file_path} {output_file_path}"
      if self.applyMuonScaleFactors is not None:
        command_for_file += f" {int(self.applyMuonScaleFactors)}"
      if self.applyMuonTriggerScaleFactors is not None:
        command_for_file += f" {int(self.applyMuonTriggerScaleFactors)}"
      
      self.__run_command(command_for_file)
  
  # option 2
  def __run_local_input_output_list(self):
    info("Running locally with input_output_file_list")
    for input_file_path, output_file_path in self.files_config.input_output_file_list:
      command_for_file = f"{self.command} {input_file_path} {output_file_path}"
      if self.applyMuonScaleFactors is not None:
        command_for_file += f" {int(self.applyMuonScaleFactors)}"
      if self.applyMuonTriggerScaleFactors is not None:
        command_for_file += f" {int(self.applyMuonTriggerScaleFactors)}"
        
      self.__run_command(command_for_file)
        
  def __setup_temp_file_paths(self):
    hash_string = str(uuid.uuid4().hex[:6])
    self.condor_config_name = f"tmp/condor_config_{hash_string}.sub"
    self.condor_run_script_name = f"tmp/condor_run_{hash_string}.sh"
    self.input_files_list_file_name = f"tmp/input_files_{hash_string}.txt"
    
  def __copy_templates(self):
    os.system(f"cp ../templates/condor_config.template.sub {self.condor_config_name}")
    os.system(f"cp ../templates/condor_run.template.sh {self.condor_run_script_name}")
    os.system(f"chmod 700 {self.condor_run_script_name}")
    info(f"Stored condor config at: {self.condor_config_name}")
    info(f"Stored run shell script at: {self.condor_run_script_name}")
    
  def __save_file_list_to_file(self, input_files):
    with open(self.input_files_list_file_name, "w") as file:
      for input_file_path in input_files:
        file.write(f"{input_file_path}\n")
  
  def __setup_voms_proxy(self):
    voms_proxy_path = os.popen("voms-proxy-info -path").read().strip().replace("/", "\/")    
    os.system(f"cp {voms_proxy_path} voms_proxy")
    os.system(f"sed -i 's/<voms_proxy>/{voms_proxy_path}/g' {self.condor_run_script_name}")
  
  def __set_python_executable(self):
    python_executable = os.popen("which python").read().strip()
    python_executable = python_executable.replace("/", "\/")
    os.system(f"sed -i 's/<python_path>/{python_executable}/g' {self.condor_run_script_name}")
  
  def __set_run_script_variables(self):
    self.__setup_voms_proxy()
    
    # set file name
    if hasattr(self.files_config, "file_name"):
      os.system(f"sed -i 's/<file_name>/--file_name {self.files_config.file_name}/g' {self.condor_run_script_name}")
    else:
      os.system(f"sed -i 's/<file_name>//g' {self.condor_run_script_name}")
    
    if self.applyMuonScaleFactors is None:
      os.system(f"sed -i 's/<muon_SFs>//g' {self.condor_run_script_name}")
    else:
      os.system(f"sed -i 's/<muon_SFs>/--apply_muon_SFs {int(self.applyMuonScaleFactors)}/g' {self.condor_run_script_name}")
    
    if self.applyMuonTriggerScaleFactors is None:
      os.system(f"sed -i 's/<muonTrigger_SFs>//g' {self.condor_run_script_name}")
    else:
      os.system(f"sed -i 's/<muonTrigger_SFs>/--apply_muon_trigger_SFs {int(self.applyMuonTriggerScaleFactors)}/g' {self.condor_run_script_name}")
    
    self.__set_python_executable()
    
    # set the app and app config to execute
    os.system(f"sed -i 's/<app>/{self.app_name}/g' {self.condor_run_script_name}")
    os.system(f"sed -i 's/<config>/{self.config_path}/g' {self.condor_run_script_name}")
    
    # set path to the list of input files
    input_files_list_file_name_escaped = self.input_files_list_file_name.replace("/", "\/")
    os.system(f"sed -i 's/<input_files_list_file_name>/{input_files_list_file_name_escaped}/g' {self.condor_run_script_name}")
    
    # set output directory
    output_dir = self.files_config.output_dir.replace("/", "\/")
    os.system(f"sed -i 's/<output_dir>/{output_dir}/g' {self.condor_run_script_name}")
    
  def __set_condor_script_variables(self, n_files):
    condor_run_script_name_escaped = self.condor_run_script_name.replace("/", "\/")
    os.system(f"sed -i 's/<executable>/{condor_run_script_name_escaped}/g' {self.condor_config_name}")
    os.system(f"sed -i 's/<job_flavour>/{self.job_flavour}/g' {self.condor_config_name}")
  
    if self.resubmit_job is not None:
      os.system(f"sed -i 's/$(ProcId)/{self.resubmit_job}/g' {self.condor_config_name}")
      os.system(f"sed -i 's/<n_jobs>/1/g' {self.condor_config_name}")
    elif hasattr(self.files_config, "file_name"):
      os.system(f"sed -i 's/<n_jobs>/1/g' {self.condor_config_name}")
    else:
      max_files = n_files
      if hasattr(self.files_config, "max_files"):
        max_files = self.files_config.max_files if self.files_config.max_files != -1 else n_files
      os.system(f"sed -i 's/<n_jobs>/{max_files}/g' {self.condor_config_name}")
    

