from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.analytics import Glue
from diagrams.aws.storage import S3
from diagrams.aws.database import Redshift
from diagrams.onprem.container import Docker
from diagrams.onprem.workflow import Airflow
from diagrams.onprem.iac import Terraform
from diagrams.onprem.analytics import Spark
from diagrams.custom import Custom
from diagrams import Node

with Diagram("AWS architecture", show=False, direction="LR"):
    source = Custom("Finn API", "./api.png")

    with Cluster("EC2 Instance"):
        extract = Lambda("Trigger Lambda")

        with Cluster("Docker Container"):

            with Cluster("Airflow"):
                S3 = S3("Extract")
                Red = Redshift("Load")

                with Cluster("Transform"):
                   transform =  [Glue("")- Spark("")]

            S3  >> transform >> Red


        source >> extract >> S3



    with Cluster("Infra & Orchestration"):
        terraform = Terraform("Manage Infrastructure")
        docker = Docker("Docker container")
        EC2 = EC2("EC2 Instance")
        airflow = Airflow("Schedule & Monitor ETL")

        terraform >> EC2 >> docker >> airflow





