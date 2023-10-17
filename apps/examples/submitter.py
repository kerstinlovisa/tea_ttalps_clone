import argparse
import os
from SubmissionManager import SubmissionManager, SubmissionSystem

def get_args():
  parser = argparse.ArgumentParser(description="Submitter")

  parser.add_argument("--app", type=str, help="name of the app to run", required=True)
  parser.add_argument("--config", type=str, required=True, help="config to be executed by the app")
  
  parser.add_argument("--files_config", type=str, default=None, help="path to a python config with a list of input/output paths")
  
  parser.add_argument("--local", action="store_true", default=False, help="run locally")
  parser.add_argument("--condor", action="store_true", default=False, help="run on condor")
  
  parser.add_argument(
    "--job_flavour", 
    type=str, 
    default="espresso",
    help="condor job flavour: espresso (20 min), microcentury (1h), longlunch (2h), workday (8h), tomorrow (1d), testmatch (3d), nextweek (1w)"
  )
  parser.add_argument(
    "--resubmit_job", 
    type=int,
    default=None,
    help="use this option to resubmitt a specific job"
  )
  
  parser.add_argument("--dry", action="store_true", default=False, help="dry run, without submitting to condor")
  
  args = parser.parse_args()
  return args


def main():
  args = get_args()
  
  submission_system = SubmissionSystem.unknown
  if args.local:
    submission_system = SubmissionSystem.local
  if args.condor:
    submission_system = SubmissionSystem.condor
  
  if submission_system == SubmissionSystem.unknown:
    print("Please select either --local or --condor")
    exit()
    
  submission_manager = SubmissionManager(submission_system, args.app, args.config, args.files_config)

  if submission_system == SubmissionSystem.local:  
    submission_manager.run_locally()
  if submission_system == SubmissionSystem.condor:
    submission_manager.run_condor(args.job_flavour, args.resubmit_job, args.dry)
  
  
if __name__ == "__main__":
  main()
