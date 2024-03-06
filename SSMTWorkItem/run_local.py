import os
from idmtools.core.platform_factory                           import  Platform
from idmtools.assets                                          import  Asset
from idmtools_models.python.python_task                       import  PythonTask
from idmtools_platform_comps.ssmt_work_items.comps_workitems  import  SSMTWorkItem

DOCK_PACK   = r'docker-staging-public.packages.idmod.org/example_hosted_docker:b03f37e'
FILENAME_PY =  'run_remote.py'
FILENAME_ID =  'COMPS_ID.id'
COMPS_URL   =  'https://comps.idmod.org'


# Runs locally
def launch_example(exp_id='', LOCAL_PATH=''):

    # Connect to COMPS
    plat = Platform(block        = 'COMPS',
                    endpoint     = COMPS_URL,
                    environment  = 'Calculon')

    # Create python task for SSMT work item
    task_obj = PythonTask(python_path = 'python3',
                            script_path = FILENAME_PY)

    # Add script for python task and exp id file to assets
    asset01 = Asset(filename=FILENAME_ID, content=exp_id)
    asset02 = Asset(filename=os.path.join(LOCAL_PATH,FILENAME_PY))
    task_obj.common_assets.add_asset(asset01)
    task_obj.common_assets.add_asset(asset02)

    # Reduce experiment output to single file
    wi_obj = SSMTWorkItem(name            = 'Docker-Example:its-a-moo-world',
                            task          = task_obj,
                            docker_image  = DOCK_PACK)
    wi_obj.run(wait_on_done=True)

    # Download stdout.txt delete work item
    resp_dict = plat.get_files(wi_obj,['stdout.txt'])
    with open("output.txt", "wb") as fid:
       fid.write(resp_dict['stdout.txt'])
    plat_obj  = wi_obj.get_platform_object()
    plat_obj.delete()

    return resp_dict

#*******************************************************************************

if (__name__ == "__main__"):

  resp_dict = launch_example()