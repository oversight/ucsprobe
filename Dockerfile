FROM ghcr.io/oversight/netappprobe:latest

ENV PROBE_VERSION 1.0.4
ENV PROBE_REPOSITORY unstable
ENV PROBE_NAME osucsprobe

COPY code /code
WORKDIR /code

ENTRYPOINT [ "/opt/OsNetAppProbe/bin/python", "ucsProbe.py" ]
