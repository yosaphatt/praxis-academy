if [ `find $1 -name "*.java" -type f` ]
    then
    	echo "Ada file Java pada direktori " `whereis `find $1 -name "*.java" -type f``
else
    echo "Tidak ada"

