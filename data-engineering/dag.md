# Directed Acrylic Graph

A `DAG` is a collection of all the tasks that need to be run, organised in a way that reflects their relationship and dependencies. They contain a set of nodes that are connected by directed edges and have no cycles, which means each job in the flow sees no node more than once.

These are similar to Databricks Workflows, Apache Airflow, etc.

![DAGs in Apache Airflow](/data-engineering/engineering-screenshots/dag-apache-spark-example.png)
