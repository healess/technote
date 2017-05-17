//gugu dan
//procedure method
// for (dan <- (2 to 9))
// 	for (r <- (1 to 9))
// 		printf("%d X %d = %d \n",dan,r,dan*r)

//functional 1 function
def gugu(dan:Int):String = (1 to 9).map(i => "%d X %d = %d \n".format(dan,i,dan*i)).reduce("%s%s".format(_,_) )

// println(gugu(3))
// println((2 to 9).map(gugu(_)))

//functional 1 line
// (2 to 9).map(gugu(_)).foreach(println)
(2 to 9).map( dan =>(1 to 9).map(i => "%d X %d = %d \n".format(dan,i,dan*i))
							.reduce("%s%s".format(_,_) )
	).foreach(println)