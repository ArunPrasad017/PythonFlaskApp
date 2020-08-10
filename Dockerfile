FROM ubuntu:20.04
# Upgrade installed packages
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Python package management and basic dependencies
RUN apt-get install -y curl python3.8 python3.8-dev python3.8-distutils

# Register the version in alternatives
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1

# Set python 3 as the default python
RUN update-alternatives --set python /usr/bin/python3.8

# Upgrade pip to latest version
RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py --force-reinstall && \
    rm get-pip.py

COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install -r /tmp/requirements.txt
EXPOSE 5000

CMD [ "python","-m","flask_project" ]
