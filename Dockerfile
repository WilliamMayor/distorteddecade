FROM python:2.7-onbuild

EXPOSE 80

CMD ["gunicorn", "--bind=0.0.0.0:80", "wsgi:app", "--log-file", "-"]
