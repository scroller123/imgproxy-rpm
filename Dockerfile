FROM jc21/rpmbuild-centos7

USER root

#RUN chmod 777 /srv/pkg
#USER rpmbuilder
#RUN ls -lah /srv
#RUN getent passwd 

RUN yum install libjpeg-turbo-devel -y;
RUN yum install libexif-devel -y;
RUN yum install giflib-devel -y;
RUN yum install librsvg2-devel -y;
RUN yum install libgsf-devel -y;
RUN yum install libtiff-devel -y;
RUN yum install fftw-devel -y;
RUN yum install lcms2 -y;
RUN yum install libpng-devel -y;
RUN yum install libimagequant -y;
RUN yum install ImageMagick ImageMagick-devel -y;
RUN yum install pango-devel -y;
RUN yum install orc -y;
RUN yum install matio-devel -y;
RUN yum install cfitsio -y;
RUN yum install libwebp -y;
RUN yum install OpenEXR-devel -y;
RUN yum install openslide -y;

COPY ./srv /srv
RUN chown -R 1000:1000 /srv


CMD /srv/pkg
