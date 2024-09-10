import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:password@localhost/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL') or 'amqp://guest:guest@localhost:5672/'
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND') or 'amqp://guest:guest@localhost:5672/'
    AES_BLOCK_SIZE = os.environ.get('AES_BLOCK_SIZE') or '32'
    AES_KEY = os.environ.get('AES_KEY') or 'dfeJ@NcRfTjWnZr4u7x!A%D*G-KaPksh'