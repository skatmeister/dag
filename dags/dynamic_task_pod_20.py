from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.decorators import task


with DAG(dag_id="dynamic_task_pod_n", start_date=datetime.utcnow()) as dag:

    @task
    def add_one(x: int):
        return x+1

    @task
    def sum_it(values):
        total = sum(values)
        print(f"Total was {total}")
        return total

    # mylist=createList(43)
    mylist = [i+1 for i in range(43)]
    added_values = add_one.expand(x=mylist)
    sum_it(added_values)
