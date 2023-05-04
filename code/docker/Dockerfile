FROM ubuntu:latest
MAINTAINER transceptor-technology "support@transceptor.technology"
ENV PROBE_VERSION 1.0.4
ENV PROBE_REPOSITORY unstable
ENV PROBE_NAME osucsprobe
RUN \
  apt-get update && \
  apt-get install --yes --force-yes wget supervisor libffi-dev && \
  cd /root/ && \
  wget https://storage.googleapis.com/oversight_repository/compiled/linux/debian/dists/${PROBE_REPOSITORY}/main/binary-amd64/${PROBE_NAME}_${PROBE_VERSION}_amd64.deb && \
  dpkg -i /root/${PROBE_NAME}_${PROBE_VERSION}_amd64.deb && \
  rm /root/${PROBE_NAME}_${PROBE_VERSION}_amd64.deb
# Remove var and etc as we mount then during compose
RUN \
  rm -rf /opt/OsUcsProbe/var && \
  rm -rf /opt/OsUcsProbe/etc
#Startup Script
COPY  /includes/startup.py /opt/OsUcsProbe/startup.py
RUN chmod +x /opt/OsUcsProbe/startup.py
ENTRYPOINT ["/opt/OsUcsProbe/startup.py"]
