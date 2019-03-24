FROM php:7.2.1-apache

RUN apt-get update
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y libzip-dev
RUN docker-php-ext-install mysqli
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
RUN a2enmod rewrite
RUN a2enmod http2
RUN a2enmod ssl

COPY armbook /var/www/html
COPY default.conf /etc/apache2/sites-enabled/default.conf
COPY server.crt /etc/apache2/ssl/server.crt
COPY server.key /etc/apache2/ssl/server.key

RUN service apache2 restart
EXPOSE 443
