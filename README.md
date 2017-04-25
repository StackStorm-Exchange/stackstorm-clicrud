## Readme

This pack allows you to use CLICRUD effectively within StackStorm or the Brocade Workflow Composer.


This pack contains two actions below. The 'ops_command' allows you to run show commands and operational commands. 'config_command' allows you to list a set of configuration commands.

```text
- ops_command
- config_command
```

####ops_command

Allows you to run an operational command on a Brocade ICX, MLX or VDX using CLI.

####config_command

Allows you to run a comma separated LIST of configuration commands. The real world rarely leads to running a single command so this action allows you to create a list of them which will be pushed. This could also mean a comma separated template, with the comma allowing each input to be treated as a line.


#### CLICRUD

If you are not familiar with CLICRUD, check out http://github.com/davidjohngee/clicrud for the latest or install using PyPi:

#### Version 0.3.00 Update
With version 0.3.00 of this pack and version 0.3.00 of CLICRUD, it is possible to use different pre-configured credentials for different environments.
It is also possible to use base64 encoded passwords and enable passwords.

Finally, the Brocade vRouter is now also supported.

```bash
pip install clicrud
```

This dependency will automatically be installed on ST2/BWC so don't worry about that! You do not have to install this to get the clicrudST2 integration working.

#### Configuration file/s

`clicrud.yaml`

This file hides the connectivity method and credentials from the actual composer itself. This is to limit what can change in the workflows/rules.

Currently the connectivity method is also in the configuration file. This in the future may change. Everyone uses SSH right? (Just nod).

You can create the configuration manually or use the 'st2 pack config' command to generate it.


```
  ---
  environment:
    default:  
      username: "admin"
      method:   "ssh"
      password: "password"
      enable:   "password"
    icx:
      username: "admin"
      method:   "telnet"
      b64password: "B64ENCODEDSTRING"
      b64enable: "B64ENCODEDSTRING"
```

It is possible to swap out password/b64password and enable/b64enable.
You can also use dynamic datastore values.
