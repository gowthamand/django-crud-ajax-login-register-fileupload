FROM python AS builder
EXPOSE 8000
WORKDIR /mysite
COPY requirements.txt /mysite
RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
COPY . /mysite
ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]