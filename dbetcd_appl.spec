{provider_spec,"dbetcd_appl",
 [
     {appl_name,"dbetcd_appl"},
     {vsn,"0.1.0"},
     {app_name,"dbetcd_appl"},
     {app,dbetcd},
     {dir,"dbetcd_appl"},
     {tar_file,"dbetcd_appl-0.1.0.tar.gz"},
     {node_name,"dbetcd_appl"},
     {cookie,"a_cookie"},
     {pa_args," -pa dbetcd_appl/ebin -config dbetcd_appl/config/sys.config"},
     {git_path,"https://github.com/joq62/dbetcd_appl.git"},
     {tar_cmd,"tar -xvf dbetcd_appl/dbetcd_appl-0.1.0.tar.gz -C dbetcd_appl "},
     {start_cmd,{application,start,[dbetcd_appl],20000}},
     {num, 1},
     {affinity,[all_hosts]}
 ]
}.
