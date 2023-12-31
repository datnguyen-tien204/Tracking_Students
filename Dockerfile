FROM ubuntu:latest
WORKDIR /Tracking_Students
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential hdf5-tools libgl1 libgtk2.0-dev
COPY . /Tracking_Students
RUN pip3 install -r setup.txt
EXPOSE 8080
CMD ["python3","file_requirements.py"]
CMD ["python3", "app.py"]
