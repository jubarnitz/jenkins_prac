# ======================================================================================================================
# === IMPORTS ==========================================================================================================
# ======================================================================================================================
# Standard Imports
import argparse
import time


# ======================================================================================================================
# === CONSTANTS ========================================================================================================
# ======================================================================================================================
_JOB_START_URL = 'some_url'

# ======================================================================================================================
# === MAIN =============================================================================================================
# ======================================================================================================================
if __name__ == "__main__":
    """
    Manage Command Line Arguements
    """

    # Parse Args
    parser = argparse.ArgumentParser()
    parser.add_argument('--plan_id', default=None, type=int, required=True)
    parser.add_argument('--type', default=None, type=str, required=True)
    parser.add_argument('--url', default=None, type=str, required=True)
    args = parser.parse_args()

    # Update DB and create job_id here

    # Create Fake Job ID for now
    epoch = str(int(time.time()))
    api_job_id = '{}_{}'.format(args.plan_id, epoch)

    print(api_job_id)
