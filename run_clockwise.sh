echo 204 > /sys/class/gpio/export
echo 205 > /sys/class/gpio/export
echo 236 > /sys/class/gpio/export
echo 237 > /sys/class/gpio/export

echo out > /sys/class/gpio/gpio204/direction
echo out > /sys/class/gpio/gpio205/direction
echo out > /sys/class/gpio/gpio236/direction
echo out > /sys/class/gpio/gpio237/direction

dur_time=$1
#speed=$2

start_time=`date +%s`
cur_time=0

while [ $cur_time -lt $dur_time ];do

	echo 1 > /sys/class/gpio/gpio204/value;
	echo 0 > /sys/class/gpio/gpio205/value;
	echo 0 > /sys/class/gpio/gpio236/value;
	echo 0 > /sys/class/gpio/gpio237/value;
	sleep 0.001;
	#echo 1;

	echo 0 > /sys/class/gpio/gpio204/value;
	echo 0 > /sys/class/gpio/gpio205/value;
	echo 0 > /sys/class/gpio/gpio236/value;
	echo 1 > /sys/class/gpio/gpio237/value;
	sleep 0.001;
	#echo 2;


	echo 0 > /sys/class/gpio/gpio204/value;
	echo 0 > /sys/class/gpio/gpio205/value;
	echo 1 > /sys/class/gpio/gpio236/value;
	echo 0 > /sys/class/gpio/gpio237/value;
	sleep 0.001;
	#echo 3;


	echo 0 > /sys/class/gpio/gpio204/value;
	echo 1 > /sys/class/gpio/gpio205/value;
	echo 0 > /sys/class/gpio/gpio236/value;
	echo 0 > /sys/class/gpio/gpio237/value;
	sleep 0.001;
	#echo 4;
	end_time=`date +%s`
	cur_time=$((end_time-start_time))
done;

echo 0 > /sys/class/gpio/gpio204/value;
echo 0 > /sys/class/gpio/gpio205/value;
echo 0 > /sys/class/gpio/gpio236/value;
echo 0 > /sys/class/gpio/gpio237/value;
echo finish;
