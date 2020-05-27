# diagram.py

import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Python37-32/Lib/site-packages/graphviz-2.38/release/bin'

'''from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Web Service", show=False):
    ELB("lb") >> EC2("web") >> RDS("userdb")'''

from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


with Diagram("Grouped Workers", filename="my_diagram", show=True, direction="TB"):
    ELB("lb") >> [EC2("worker1"),
                  EC2("worker2"),
                  EC2("worker3"),
                  EC2("worker4"),
                  EC2("worker5")] >> RDS("events")




"""from IPython.display import Image, display
im = Image(G.create_png())
display(im)"""