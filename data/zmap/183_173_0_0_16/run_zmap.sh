network="183.173.0.0/16"
list="$@"
if [ $# -eq 0 ]; then
	list="21 22 23 25 43 53 69 80 110 161 179 220 443 547 3306 3389 5432"
fi

echo
echo 端口列表:
echo ports: $list
echo

echo 是否跳过已有输出端口? Y/N
read pass_existed

echo 输出文件列表:

for i in $list; do
	pref="port$i"
	filename=${pref}.csv
	if [ ! -f $filename -o $pass_existed != "Y" ]; then
		now=0
		while [ -f $filename ]; do
			now=`expr $now + 1`
			filename=${pref}_${now}.csv 
		done
		echo ${filename}
	fi
done
echo

echo '确定开始吗? Y/N'
read choice

if [ $choice == "Y" ]; then
	for i in $list; do
		pref="port$i"
		filename=${pref}.csv
		if [ ! -f $filename -o $pass_existed != "Y" ]; then
			now=0
			while [ -f $filename ]; do
				now=`expr $now + 1`
				filename=${pref}_${now}.csv 
			done
			zmap -B 500kb -p $i -o $filename $network
		fi
	done
fi
