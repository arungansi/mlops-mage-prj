FROM mageai/mageai:alpha

ARG PROJECT_NAME=mlops
ARG MAGE_CODE_PATH=/home/src
ARG USER_CODE_PATH=${MAGE_CODE_PATH}/${PROJECT_NAME}

WORKDIR ${MAGE_CODE_PATH}

COPY ${PROJECT_NAME} ${PROJECT_NAME}

ENV USER_CODE_PATH=${USER_CODE_PATH}

#pl make sure you have the gh installed at the beginning
# RUN apt install gh
# do gh auth login in the container cmd line
# "trying thru wsl desparately"

# Install custom Python libraries and dependencies for your project.
RUN pip3 install -r ${USER_CODE_PATH}/requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:${MAGE_CODE_PATH}"

# Installing necessary utilities and Terraform.
# Uncomment the following lines if you want to use Terraform in Docker.
RUN apt-get update && \
  apt-get install -y wget unzip && \
  wget https://releases.hashicorp.com/terraform/1.8.3/terraform_1.8.3_linux_amd64.zip && \
  unzip terraform_1.8.3_linux_amd64.zip -d /usr/local/bin/ && \
  rm terraform_1.8.3_linux_amd64.zip

#It runs the shell command and -c is the argumet for sending the run_app.sh shell file
CMD ["/bin/sh", "-c", "/app/run_app.sh"]
