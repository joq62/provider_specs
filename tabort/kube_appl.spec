{provider_spec,"kube_appl",
 [
     {appl_name,"kube_appl"},
     {vsn,"0.1.0"},
     {app_name,"kube_appl"},
     {app,kube_appl},
     {dir,"kube_appl"},
     {tar_file,"kube_appl-0.1.0.tar.gz"},
     {node_name,"kube_appl"},
     {cookie,"a_cookie"},
     {pa_args," -pa kube_appl/ebin -config kube_appl/config/sys.config"},
     {git_path,"https://github.com/joq62/kube_appl.git"},
     {tar_cmd,"tar -xvf kube_appl/kube_appl-0.1.0.tar.gz -C kube_appl "},
     {start_cmd,{application,start,[kube_appl],20000}},
     {num, 1},
     {affinity,[all_hosts]}
 ]
}.
