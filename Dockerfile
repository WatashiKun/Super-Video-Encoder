# New release 
# Support with libfdk_aac 

FROM python:3.9.2-slim-buster
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev mediainfo
# Change repo 
RUN echo deb http://http.us.debian.org/debian/ testing non-free contrib main > /etc/apt/sources.list && \
    apt -qq update
# Install other dependencies
# Install AOM
# Compile and install fresh ffmpeg from sources:
# See: https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu
RUN wget https://ffmpeg.org/releases/ffmpeg-4.2.1.tar.bz2  && \
tar -xf ffmpeg-4.2.1.tar.bz2  && \
rm ffmpeg-4.2.1.tar.bz2  && \
cd ffmpeg-4.2.1  && \
RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev ffmpeg mediainfo
COPY . .
RUN pip3 install -r requirements.txt
CMD ["bash","run.sh"]
