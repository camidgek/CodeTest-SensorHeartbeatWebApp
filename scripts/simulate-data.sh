set -e
DELAY=$1
HBCOUNT=$2

for (( ; ; ))
do 
	count=$RANDOM
	curl http://localhost:8000/sensors/ -X POST \
		-H "Content-Type: application/json" \
		--data "{\"serial_num\":\"${count}\"}"

	sleep ${DELAY} && echo ""

	for ((i=1;i<=${HBCOUNT};i++)); do
		curl http://localhost:8000/heartbeats/ -X POST \
			-H "Content-Type: application/json" \
			--data "{\"serial_num\":\"${count}\"}"
		sleep ${DELAY} && echo ""
	done
done
