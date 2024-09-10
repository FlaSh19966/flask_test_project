from . import celery, db
from .models import Company
import pandas as pd


@celery.task
def process_csv_task(filepath):
    try:
        chunk_size = 1000
        chunks = pd.read_csv(filepath, chunksize=chunk_size)

        for chunk in chunks:
            companies = [
                Company(
                    name=row['name'],
                    domain=row['domain'],
                    year_founded=row['year founded'],
                    industry=row['industry'],
                    size_range=row['size range'],
                    locality=row['locality'],
                    country=row['country'],
                    linkedin_url=row['linkedin url'],
                    current_employee_estimate=row['current employee estimate'],
                    total_employee_estimate=row['total employee estimate']
                ) for index, row in chunk.iterrows()
            ]
            db.session.bulk_save_objects(companies)
            db.session.commit()
        return {"status": "success", "message": "CSV processing completed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}