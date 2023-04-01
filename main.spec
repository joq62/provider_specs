{provider_spec,"main",
 [
     {appl_name,"main"},
     {vsn,"0.1.0"},
     {dir,"main"},
     {tar_file,"main-0.1.0.tar.gz"},
     {node_name,"main"},
     {cookie,"main_cookie"},
     {clone_cmd,{os,cmd,["git clone https://github.com/joq62/main.git "]}},
     {tar_cmd,{os,cmd,["tar -xvf main/main-0.1.0.tar.gz -C main "]}},
     {start_cmd,{os,cmd,["./main/bin/main daemon"]}},
     {num, 1},
     {affinity,["c201"]}       
 ]}.
