FROM php:8.4.1-fpm

# Install tools and extensions
RUN apt-get update && apt-get install -y \
    nginx supervisor git curl zip unzip libzip-dev libonig-dev libxml2-dev \
    && docker-php-ext-install pdo pdo_mysql zip mbstring \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Make PHP-FPM listen on TCP 9000
RUN echo "listen = 9000" >> /usr/local/etc/php-fpm.d/zz-docker.conf

# Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Copy configs
COPY docker/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY docker/app/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Remove default Nginx config
RUN rm /etc/nginx/sites-enabled/default

# Set working directory
WORKDIR /var/www

# Expose port 80
EXPOSE 80

CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/conf.d/supervisord.conf"]