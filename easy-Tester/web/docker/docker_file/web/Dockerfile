FROM alpine:3.8

RUN apk update

RUN apk add --no-cache apache2

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

RUN mkdir /run/apache2

RUN mkdir /var/www/localhost/htdocs/web \
    && mkdir /var/www/localhost/htdocs/eT-test

ENTRYPOINT ["httpd","-D","FOREGROUND"]
