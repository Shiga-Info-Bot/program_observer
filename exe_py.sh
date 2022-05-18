start_dt=`date`
cd $1
pyResult=`python3 $2 2>&1`
if [ $? -gt 0 ]; then
    cd $3
    python3 send_discord.py $1 $2 "$start_dt" "$pyResult"
fi