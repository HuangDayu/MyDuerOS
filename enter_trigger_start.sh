# 通过"Enter"键来触发唤醒

WORK_PATH="${PWD}"
export PYTHONPATH=${WORK_PATH}:${PYTHONPATH}

sudo python ./mqtt/mymqtt.py -d

python ./app/enter_trigger_main.py