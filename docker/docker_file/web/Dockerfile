FROM alpine:3.8

RUN apk update

RUN apk add --no-cache apache2 php7-apache2 php7

RUN apk add --no-cache openrc \
    && sed -i 's/#rc_sys=""/rc_sys="lxc"/g' /etc/rc.conf \
    && echo 'rc_provide="loopback net"' >> /etc/rc.conf \
    && sed -i 's/^#\(rc_logger="YES"\)$/\1/' /etc/rc.conf \
    && sed -i '/tty/d' /etc/inittab \
    && sed -i 's/hostname $opts/# hostname $opts/g' /etc/init.d/hostname \
    && sed -i 's/mount -t tmpfs/# mount -t tmpfs/g' /lib/rc/sh/init.sh \
    && sed -i 's/cgroup_add_service /# cgroup_add_service /g' /lib/rc/sh/openrc-run.sh \
    && mkdir /run/openrc \
    && touch /run/openrc/softlevel

COPY ./php.ini /etc/php7/php.ini

RUN mkdir /run/apache2

ENTRYPOINT ["httpd","-D","FOREGROUND"]

RUN apk add --no-cache php7-pdo php7-pdo_mysql php7-mysqli
