FROM maven:3-jdk-11 as build

WORKDIR /usr/src/app
RUN git clone https://github.com/OpenRefine/OpenRefine
WORKDIR /usr/src/app/OpenRefine

COPY muor-openrefine.patch .
RUN git apply muor-openrefine.patch

RUN ./refine clean
RUN ./refine build

FROM openjdk:11

WORKDIR /usr/app
COPY --from=build /usr/src/app/OpenRefine .

VOLUME /data
EXPOSE 3333

ENTRYPOINT ["/usr/app/refine", "-i", "0.0.0.0", "-d", "/data", "-m", "3G"]