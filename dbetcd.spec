{provider_spec,"dbetcd",
 [
     {appl_name,"dbetcd"},
     {vsn,"0.1.0"},
     {app_name,"dbetcd"},
     {app,dbetcd},
     {dir,"dbetcd"},
     {tar_file,"dbetcd-0.1.0.tar.gz"},
     {node_name,"dbetcd"},
     {cookie,"a_cookie"},
     {pa_args," -pa dbetcd/lib/*/ebin "},
     {git_path,"https://github.com/joq62/dbetcd.git"},
     {tar_cmd,"tar -xvf dbetcd/dbetcd-0.1.0.tar.gz -C dbetcd "},
     {start_cmd,{application,start,[dbetcd],20000}},
     {num, 1},
     {affinity,[all_hosts]}
 ]
}.
