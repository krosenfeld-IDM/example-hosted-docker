# example-hosted-docker
Example of how to generate and use a Docker container that gets hosted on the IDM artifactory that can be accessed by a SSMTWorkItem.

1. Run Jenkins pipeline:
    - Build with parameters on Jenkins ([link to pipeline](https://jenkins.apps.idmod.org/job/MobyJenkins_/build?delay=0sec])).
4. Access the Docker container
    - Look at `README.md` in `SSMTWorkItem/`

See also:
- [MobyJenkins](https://github.com/InstituteforDiseaseModeling/MobyJenkins)
- [Minimal example](https://github.com/InstituteforDiseaseModeling/example-container-build/tree/main/minimal)
- [EMOD-Generic-Scripts](https://github.com/InstituteforDiseaseModeling/EMOD-Generic-Scripts/blob/main/docker)
