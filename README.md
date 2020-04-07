docker build -t iosbackup -f docker/Dockerfile .

docker volume switch-1

docker run -d --name=switch-1 -e IOS_HOST="192.168.1.10" -e IOS_USER="backusr" -e IOS_PASS="somesuperstrongpassword" -e IOS_ENABLE="true" -e IOS_SECRET="someotherpassword" --mount=src=switch-1,dst=/backup iosbackup:latest