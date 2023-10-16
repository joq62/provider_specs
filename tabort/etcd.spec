{provider_spec,"etcd",
 [
     {appl_name,"etcd"},
     {vsn,"0.1.0"},
     {app_name,"etcd"},
     {app,etcd}, 
     {dir,"etcd"},
     {tar_file,"etcd-0.1.0.tar.gz"},
     {node_name,"etcd"},
     {cookie,"a_cookie"},
     {pa_args," -pa etcd/ebin -config etcd/config/sys.config"},
     {git_path,"https://github.com/joq62/etcd.git"},
     {tar_cmd,"tar -xvf etcd/etcd-0.1.0.tar.gz -C etcd "},
     {start_cmd,{application,start,[etcd],20000}},
     {num, 1},
     {affinity,[all_hosts]}
 ]
}.
