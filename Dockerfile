FROM continuumio/miniconda3

# paths are relative to context in compose file
COPY "requirements.txt" /
RUN ["pip", "install", "-r", "requirements.txt"]

COPY /src /src

RUN ["python", "-m", "src.pipeline"]

EXPOSE 8080
ENTRYPOINT ["python", "-m", "src.api"]
