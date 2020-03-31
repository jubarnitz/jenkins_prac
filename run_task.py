# ======================================================================================================================
# === IMPORTS ==========================================================================================================
# ======================================================================================================================
# Standard Imports
import argparse
import logging

# ======================================================================================================================
# === CONSTANTS ========================================================================================================
# ======================================================================================================================
_JOB_START_URL = 'some_url'

# ======================================================================================================================
# === MAIN =============================================================================================================
# ======================================================================================================================
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--job_id', default=None, required=True, type=int, help='Job ID of rlated job')
    parser.add_argument('-t', '--task_id', dfault=None, required=True, type=int, help='Task ID of task being launched')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    job_id = args.job_id
    task_id = args.task_id
    verbose = args.verbose

    # Logging Setup
    if verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(filename='./test.log', level=level, format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info('job_id: *{}* *{}*'.format(job_id, task_id))
