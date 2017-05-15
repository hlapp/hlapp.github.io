FROM python:3.5-alpine
MAINTAINER Hilmar Lapp <hilmar@lappland.io>

RUN apk update && \
    apk add bash make git

RUN pip install \
    pelican \
    Markdown

RUN git clone https://github.com/getpelican/pelican-plugins.git \
              /usr/local/share/pelican-plugins
    
RUN mkdir -p /srv/pelican

COPY serve.sh /usr/local/bin/serve.sh

WORKDIR /srv/pelican
ENTRYPOINT ["/usr/local/bin/serve.sh"]

EXPOSE 8000
