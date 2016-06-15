while true;do

	echo 1 > /sys/class/gpio/gpio236/value;
	echo 0 > /sys/class/gpio/gpio237/value;
	sleep 0.2;
	echo 1;

	echo 0 > /sys/class/gpio/gpio236/value;
	echo 1 > /sys/class/gpio/gpio237/value;
	sleep 0.2;
	echo 2;

done;
