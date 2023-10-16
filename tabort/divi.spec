{provider_spec,"divi",
 [
     {appl_name,"divi"},
     {vsn,"0.1.0"},
     {app_name,"divi"},
     {app,divi}, 
     {dir,"divi"},
     {tar_file,"divi-0.1.0.tar.gz"},
     {node_name,"divi"},
     {cookie,"a_cookie"},
     {pa_args," -pa divi/ebin -config divi/config/sys.config"},
     {git_path,"https://github.com/joq62/divi.git"},
     {tar_cmd,"tar -xvf divi/divi-0.1.0.tar.gz -C divi "},
     {start_cmd,{application,start,[divi],20000}},
     {num, 1},
     {affinity,[all_hosts]}
 ]
}.
