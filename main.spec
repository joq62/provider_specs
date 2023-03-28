{appl_spec,"main",
 [
     {appl_name,"main"},
     {vsn,"0.1.0"},
     {dir,"main"},
     {tar_file,"main-0.1.0.tar.gz"},
     {NodeName,"main"},
     {clone_cmd,{os,cmd,["git clone https://github.com/joq62/main.git -C main"]}},
     {tar_cmd,{os,cmd,["tar -xvf main/main-0.1.0.tar.gz -C main "]}},
     {start_cmd,{os,cmd,["./main/bin/main daemon"]}},
     {affinity,["c201"]}       
 ]}.
