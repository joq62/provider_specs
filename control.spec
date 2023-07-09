{provider_spec,"control",
 [
     {appl_name,"control"},
     {vsn,"0.1.0"},
     {app_name,"control"},
     {app,control}, 
     {dir,"control"},
     {tar_file,"control-0.1.0.tar.gz"},
     {node_name,"control"},
     {cookie,"a_cookie"},
     {pa_args," -pa control/ebin -config control/config/sys.config"},
     {git_path,"https://github.com/joq62/control.git"},
     {tar_cmd,"tar -xvf control/control-0.1.0.tar.gz -C control "},
     {start_cmd,{application,start,[control],20000}},
     {num, 1},
     {affinity,[all_hosts]}
 ]
}.
