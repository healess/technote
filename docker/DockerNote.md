# Docker Enviconment
 windows 10 Pro 유저는 : docker for windows
    * power shell에서 docker 명령을 실행
+ windows 10 Home or 7 유저는 : docker toolbox
    * docker Quick Start Terminal에서 실행
    * 단, docker에 ip로 접근할때는 hostMachine의 IP를 쓰지 말고, 
           "docker-machine ip"라고 쳤을때 나오는 IP(192.168.99.100)를 쓰셔야 합니다. 
    docker run  -it --rm  -p 8888:8888  -v /c/Users/userxx/work:/home/jovyan/work  --name=spark31  jupyter/pyspark-notebook

        (O) /c/Users/userxx/work
        (x) \c\Users\userxx\work
        (x) c:\Users\userxx\work
## Command
su - pi31 --command="cd /home/pi31/work; docker run  -it --rm  -p 8031:8888  -v /home/pi31/work:/home/jovyan/work  --name=spark31  nowage/pyspark-notebook >> /home/pi31/log.txt" &
## Document 
https://www.slideshare.net/pyrasis/docker-fordummies-44424016