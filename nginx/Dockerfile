FROM nginx:latest

EXPOSE 80

COPY nginx.conf /etc/nginx/nginx.conf

CMD ["nginx"]

RUN echo "daemon off;" >> /etc/nginx/nginx.conf