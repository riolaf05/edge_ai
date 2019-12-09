FROM raspbian/stretch:latest

#Workdir
RUN mkdir /home/scripts
WORKDIR /home/scripts

#Updating packet manager
RUN apt-get update

#Install Python3
RUN apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
RUN wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz \
&& tar xf Python-3.6.5.tar.xz \
&& cd Python-3.6.5 \
&& ./configure \
&& make \
&& make altinstall

#Cleaning python installation junk
RUN cd ..
RUN rm -r Python-3.6.5 
RUN rm Python-3.6.5.tar.xz 

#Install pip3
RUN apt-get install python3-pip -y

#Update pip3
RUN pip3 install --upgrade pip

#Tensorflow Lite installing
RUN wget 'https://dl.google.com/coral/python/tflite_runtime-1.14.0-cp35-cp35m-linux_armv7l.whl'
RUN pip3 install tflite_runtime-1.14.0-cp35-cp35m-linux_armv7l.whl

#Installing models folder
RUN mkdir /home/scripts/models

#Install pip packages dependencies
RUN apt-get install libjpeg-dev -y \
&& apt-get install zlib1g-dev -y \
&& apt-get install libfreetype6-dev -y \
&& apt-get install liblcms1-dev -y \
&& apt-get install libopenjp2-7 -y \
&& apt-get install libtiff5 -y \
&& apt-get install -y libraspberrypi0 libraspberrypi-dev libraspberrypi-doc libraspberrypi-bin

#Installing picamera, jupyter and other pip packages
RUN pip3 install numpy --user
RUN pip3 install imutils --user
RUN pip3 install argparse --user 
RUN pip3 install Pillow --user  
RUN pip3 install picamera --user
#RUN pip3 install jupyter --user   #problem: Package 'ipython' requires a different Python: 3.5.3 not in '>=3.6'
#RUN pip install pyarrow --user 
#RUN pip install python-opencv  --user #TODO: problem..unable to find python-opencv on Debian buster repositories!

#Cleaning pip packages junk
RUN apt-get --purge remove -y build-essential tk-dev
RUN apt-get --purge remove -y libncurses5-dev libncursesw5-dev libreadline6-dev
RUN apt-get --purge remove -y libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev 
RUN apt-get --purge remove -y libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev 
RUN apt-get autoremove -y 
RUN apt-get clean

# Installing Miniconda dependencies
RUN apt-get install -y libatlas-base-dev \ 
#&& apt-get install -y libjasper-dev \ #is it needed for opencv?
&& apt-get install -y libqtgui4 \
&& apt-get install -y python3-pyqt5

# Miniconda installing
RUN wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
RUN md5sum Miniconda3-latest-Linux-armv7l.sh
RUN bash Miniconda3-latest-Linux-armv7l.sh -b
RUN rm Miniconda3-latest-Linux-armv7l.sh

# Set path to conda
ENV PATH /root/miniconda3/bin:$PATH

# Updating Miniconda packages
RUN conda update conda -y
RUN conda update --all

#Install models and labels
COPY download.sh /home/scripts/models
RUN chmod +x /home/scripts/models/download.sh
RUN /home/scripts/models/download.sh

#Copy demo file
RUN mkdir /home/scripts/samples
COPY /tflite/pi_image_classifier_tflite_demo.py /home/scripts

# Configuring access to Jupyter
#RUN mkdir /root/notebooks
#ENV PATH /root/.local/bin/:$PATH
#RUN jupyter notebook --generate-config --allow-root
#RUN echo "c.NotebookApp.password = u'sha1:dfffed19ed8c:a177ca4460cfec9f5064ed5fc21c4bd7f490943a'" >> /home/scripts/.jupyter/jupyter_notebook_config.py

# Jupyter listens port: 8888
#EXPOSE 8888

# Run Jupytewr notebook as Docker main process
#CMD ["jupyter", "notebook", "--allow-root", "--notebook-dir=/home/scripts/notebooks", "--ip='*'", "--port=8888", "--no-browser"]

