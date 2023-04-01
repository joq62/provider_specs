{provider_spec,"kube",
 [
     {appl_name,"kube"},
     {vsn,"0.1.0"},
     {dir,"kube"},
     {tar_file,"kube-0.1.0.tar.gz"},
     {node_name,"kube"},
     {cookie,"a_cookie"},
     {clone_cmd,{os,cmd,["git clone https://github.com/joq62/kube.git"]}},
     {tar_cmd,{os,cmd,["tar -xvf kube/kube-0.1.0.tar.gz -C kube "]}},
     {start_cmd,{os,cmd,["nohup erl -pa kube/lib/*/* -run application  start kube -setcookie a_cookie & exit"]}},
     {num, 1},
     {affinity,[all_hosts]} 
 ]}.
