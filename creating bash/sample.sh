#!/bin/bash

echo "starting at $(date)"
echo

echo "UPTIME"
UPTIME
echo

echo "FREE"
free
echo

echo "WHO"
who
echo

echo "Finished at $(date)"  

----------------
>> ./sample.sh

==== the above can be written as follows separeated by ; in single line ===
#!/bin/bash

echo "starting at $(date)";echo

echo "UPTIME";UPTIME;echo

echo "FREE";free;echo

echo "WHO";who;echo

echo "Finished at $(date)"  

============
>> bash sample.sh