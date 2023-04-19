{provider_spec,"test_appl",
 [
     {appl_name,"test_appl"},
     {vsn,"0.1.0"},
     {app_name,"test_appl"},
     {app,test_appl}, 
     {dir,"test_appl"},
     {tar_file,"test_appl-0.1.0.tar.gz"},
     {node_name,"test_appl"},
     {cookie,"a_cookie"},
     {pa_args," -pa test_appl/ebin -config test_appl/config/sys.config"},
     {git_path,"https://github.com/joq62/test_appl.git"},
     {tar_cmd,"tar -xvf test_appl/test_appl-0.1.0.tar.gz -C test_appl "},
     {start_cmd,{application,start,[test_appl],20000}},
     {num, 1},
     {affinity,[all_hosts]}
 ]
}.
