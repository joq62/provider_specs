{provider_spec,"adder",
 [
     {appl_name,"adder"},
     {vsn,"0.1.0"},
     {app_name,"adder"},
     {app,adder}, 
     {dir,"adder"},
     {tar_file,"adder-0.1.0.tar.gz"},
     {node_name,"adder"},
     {cookie,"a_cookie"},
     {pa_args," -pa adder/ebin -config adder/config/sys.config"},
     {git_path,"https://github.com/joq62/adder.git"},
     {tar_cmd,"tar -xvf adder/adder-0.1.0.tar.gz -C adder "},
     {start_cmd,{application,start,[adder],20000}},
     {num, 1},
     {affinity,[all_hosts]}
 ]
}.
