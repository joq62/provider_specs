-module(provider_spec).

-export([
	 start/0,
	 %% Support
	 all_files/0,
	 all_info/0
	]).


-define(Dir,".").
-define(FileExt,".spec").

%% --------------------------------------------------------------------
%% Function: available_hosts()
%% Description: Based on hosts.config file checks which hosts are avaible
%% Returns: List({HostId,Ip,SshPort,Uid,Pwd}
%% --------------------------------------------------------------------
start()->
    
    check(all_info()),
    init:stop(),
    ok.

check([])->
    io:format("Success, OK ! ~n");
check([{ok,[{provider_spec,_Id,Info}]}|T])->
    io:format("Checking ~p~n",[Info]),
  
    true=proplists:is_defined(appl_name,Info),
    true=proplists:is_defined(vsn,Info),
    true=proplists:is_defined(dir,Info),
    true=proplists:is_defined(tar_file,Info),
    true=proplists:is_defined(node_name,Info),
    true=proplists:is_defined(cookie,Info),
    true=proplists:is_defined(clone_cmd,Info),
    true=proplists:is_defined(tar_cmd,Info),
    true=proplists:is_defined(start_cmd,Info),
    true=proplists:is_defined(num,Info),
    true=proplists:is_defined(affinity,Info),


    check(T).

   

%% --------------------------------------------------------------------
%% Function: available_hosts()
%% Description: Based on hosts.config file checks which hosts are avaible
%% Returns: List({HostId,Ip,SshPort,Uid,Pwd}
%% --------------------------------------------------------------------
all_files()->
    {ok,Files}=file:list_dir(?Dir),
    FileNames=[filename:join(?Dir,Filename)||Filename<-Files,
					     ?FileExt=:=filename:extension(Filename)],
    FileNames.    
all_info()->
    [file:consult(File)||File<-all_files()].
	    
    
