#Auto start pyspark in linux
cat ./bashrc
echo PATH=$PATH:$SPARK_HOME/bin/ >> ~/.bashrc
. ~/.bashrc
pyspark

## spark-shell exception and kill
ps -ef|grep -v grep|egrep "spark-sh|pyspark"|awk '{print $2}'|xargs kill -9

## Spark(Python) run
spark-submit Collaborative_Filtering_simple.py > result1.txt
cat result1.txt

## to use jupyter
```python
import pyspark
try:
    sc
except NameError:
    sc = pyspark.SparkContext('local[*]')

from pyspark.sql.context import SQLContext as sqlContext

```
