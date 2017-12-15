# yieldmo
Hi Jing,
Thanks for taking the time to do this data challenge. We have aquestion in programming (your language of choice, please mention the language) and SQL that we would like you to attempt in 2-3 hours. Note that we are primarily looking for your approach to the problem that said, we prefer if you can make sure that the code builds and it works.



Programming Question: (new_seg.py)

Given a collection of objects of a class with 2 integer fields , startTime and endTime (where startTime < endTime) , create a new collection such that the earliest startTime is preserved and the latest endTime is preserved , only if the difference between consecutive endTime and startTime is less than or equal to 5. In other words in the output collection , the difference between 2 consecutive endTime and startTime has to be greater than 5.


1------------12 18---------------33 

Difference = 6 ( > 5)



// Input

Segment s1 = new Segment(29, 33);
Segment s2 = new Segment(10, 12);
Segment s3 = new Segment(18, 20);
Segment s4 = new Segment(1, 8);
Segment s5 = new Segment(5, 7);
Segment s6 = new Segment(24,27);


//Output

Segment output2 = new Segment(1,12);

Segment output1 = new Segment(18, 33);

If needed, you can use any of the classes from the Java/Scala/Python collections framework that might simplify the problem.




SQL Questions: (see attached) (sql_answer.docx)


Lastly, we trust you to be ethical and honest in this take home test, and not copy the code or cheat in any form. We'd like to see 100% original work from you.

Other than that, feel free to be as creative as time permits!

To submit your work, feel free to host it on github and share it with us, or send over a dropbox/gdrive link. Make sure you add to the README at the root of the project, with a clear set of instructions on how to build and run the project as well as any additional information you’d like us to know.

I look forward to your response!

Best,

Indu
