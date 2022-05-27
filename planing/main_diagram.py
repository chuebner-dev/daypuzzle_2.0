from diagrams import Diagram, Cluster, Edge
from diagrams.generic.os import Android
from diagrams.aws.integration import Appsync
from diagrams.aws.mobile import Amplify

with Diagram("Daypuzzle draft", show=False):
    
    appsync = Appsync("AppSync")
    
    with Cluster("Android Studio"):
        app = Android("app")
        amplify = Amplify("Amplify")
        amplify - Edge(color="grey", style="dashed") - app
    
    app >> appsync