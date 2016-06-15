while true;do

	echo 1 > /sys/class/gpio/gpio204/value;
	echo 0 > /sys/class/gpio/gpio205/value;
	echo 0 > /sys/class/gpio/gpio236/value;
	echo 0 > /sys/class/gpio/gpio237/value;
	sleep 0.0001;
	#echo 1;

	echo 0 > /sys/class/gpio/gpio204/value;
	echo 0 > /sys/class/gpio/gpio205/value;
	echo 0 > /sys/class/gpio/gpio236/value;
	echo 1 > /sys/class/gpio/gpio237/value;
	sleep 0.0001;
	#echo 2;


	echo 0 > /sys/class/gpio/gpio204/value;
	echo 0 > /sys/class/gpio/gpio205/value;
	echo 1 > /sys/class/gpio/gpio236/value;
	echo 0 > /sys/class/gpio/gpio237/value;
	sleep 0.0001;
	#echo 3;


	echo 0 > /sys/class/gpio/gpio204/value;
	echo 1 > /sys/class/gpio/gpio205/value;
	echo 0> /sys/class/gpio/gpio236/value;
	echo 0 > /sys/class/gpio/gpio237/value;
	sleep 0.0001;
	#echo 4;

done;

	echo 0 > /sys/class/gpio/gpio204/value;
	echo 0 > /sys/class/gpio/gpio205/value;
	echo 0 > /sys/class/gpio/gpio236/value;
	echo 0 > /sys/class/gpio/gpio237/value;
	echo finish;
