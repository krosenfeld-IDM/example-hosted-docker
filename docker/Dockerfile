FROM almalinux:9.2-minimal
#
RUN microdnf upgrade -y
#
RUN microdnf -y install python3
RUN microdnf -y install python3-pip
RUN microdnf clean all
#
RUN pip install pip          --upgrade
RUN pip install cowsay

