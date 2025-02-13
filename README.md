Givven string that is a path that represent files structur that we need to understand and to build: 
---------------------------------------------------------------------------------------------------

Exp: 

Givven a path: r"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

I came to this task by first splitin by r'\n':
---------------------------------
dir             (n=0, t=0)    : dir\  	                         
\tsubdir1       (n=1, t=1)    : dir\subdir1                       
\t\tfile1.ext   (n=1, t=2)    : dir\subdir1\file1.txt             
\t\tsubsubdir1  (n=1, t=2)    : dir\subdir1\subsubdir1\	         
\tsubdir2	    (n=1, t=1)    : dir\subdir2\				         
\t\tsubsubdir2  (n=1, t=2)    : dir\subdir2\subsubdir2\           
\t\t\tfile2.ext (n=1, t=3)    : dir\subdir2\subsubdir2\file2.ext  

we see that n = 0, 1 has no effect, only value of t has effect

dir              (n=0, t=0)    : dir\  	                          #(t=0 means: only current item)                                item_path: dir\                              root_path: dir\       
\t subdir1       (n=1, t=1)    : dir\subdir1                      #(t=1 means: root_path + current item (which here is subdir1)) item_path: dir\subdir1\,                     prev_path: dir\subdir1\              
\t\t file1.ext   (n=1, t=2)    : dir\subdir1\file1.txt            #(t=2 means: prev_path + current item which is file1.txt)      item_path: dir\subdir1\file1.txt,            prev_path: dir\subdir1\
\t\t subsubdir1  (n=1, t=2)    : dir\subdir1\subsubdir1\	        #(t=2 means: prev_path + current item which is subsubdir1)     item_path: dir\subdir1\subsubdir1,           prev_path: dir\subdir1\subsubdir1\  
\t subdir2	     (n=1, t=1)    : dir\subdir2\				              #(t=1 means  root_path + current item (which here is subdir2)) item_path: dir\subdir2,                      prev_path: dir\subdir2\
\t\t subsubdir2  (n=1, t=2)    : dir\subdir2\subsubdir2\          #(t=2 means: prev_path + current item which is subsubdir2)     item_path: dir\subdir2\subsubdir2,           prev_path: dir\subdir2\subsubdir2\
\t\t\t file2.ext (n=1, t=3)    : dir\subdir2\subsubdir2\file2.ext #(t=3 means: prev_path + current item which is file2.ext)      item_path: dir\subdir2\subsubdir2\file2.ext, prev_path: dir\subdir2\subsubdir2\

we see that in this exp the longest path to a file is: dir\subdir2\subsubdir2\file2.ext
length = 32 characters
