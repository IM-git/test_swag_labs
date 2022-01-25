FROM python:3.10

RUN mkdir -p /test_swag_labs/ &&  \
    mkdir /test_swag_labs/allureress

WORKDIR /test_swag_labs

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD pytest -s -v ./tests/ --alluredir=allureress
