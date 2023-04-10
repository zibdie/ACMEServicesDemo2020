FROM nginx:1.23.4-alpine

# Remove the default nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Create and add a custom nginx configuration file
RUN echo 'server {'\
    '    listen       80;'\
    '    server_name  localhost;'\
    ''\
    '    location / {'\
    '        root   /usr/share/nginx/html;'\
    '        index  index.html;'\
    '        try_files $uri $uri/ =404;'\
    '    }'\
    ''\
    '    error_page   500 502 503 504  /50x.html;'\
    '    location = /50x.html {'\
    '        root   /usr/share/nginx/html;'\
    '    }'\
    '}' > /etc/nginx/conf.d/nginx.conf

# Copy your HTML and JS files into the nginx container
COPY /html_folder /usr/share/nginx/html

# The port you wish to connect, you can change it here
EXPOSE 80

# Start nginx with the custom configuration
CMD ["nginx", "-g", "daemon off;"]