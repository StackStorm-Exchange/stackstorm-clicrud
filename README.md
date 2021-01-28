# CLICRUD Integration Pack

This pack allows you to use [CLICRUD](https://github.com/DavidJohnGee/clicrud/) with StackStorm or Extreme Workflow Composer.

It can be used to run CLI commands against Extreme MLX and VDX devices, Arris ICX switches, and vRouter.

This pack contains two actions:

* `ops_command` - run 'show' commands and operational commands
* `config_command` - run a list of configuration commands - see more below

### config\_command

Allows you to run a comma separated LIST of configuration commands. The real world rarely leads to running a single command so this action allows you to create a list of them which will be pushed. This could also mean a comma separated template, with the comma allowing each input to be treated as a line.

## CLICRUD

If you are not familiar with CLICRUD, check out http://github.com/davidjohngee/clicrud for the latest or install using PyPi:

```bash
pip install clicrud
```

(NB This is automatically installed on StackStorm if you install this pack)

### Version 0.3.00 Update

With version 0.3.00 of this pack and version 0.3.00 of CLICRUD, it is possible to use different pre-configured credentials for different environments.

It is also possible to use base64 encoded passwords and enable passwords.

Finally, the vRouter is now also supported.

## Configuration

Copy `clicrud.yaml.example` to `/opt/stackstorm/configs/clicrud.yaml`

```yaml
  ---
  environment:
    default:  
      username: "admin"
      method:   "ssh"
      password: "password"
      enable:   "password"
      port: 22
    icx:
      username: "admin"
      method:   "telnet"
      b64password: "B64ENCODEDSTRING"
      b64enable: "B64ENCODEDSTRING"
      port: 7045
```

You can specify groups of configurations, as shown above. When running commands, you can specify the config group to use,
or it will use the `default` settings.

NB: `port:` is optional. It will use `22` by default for SSH, or `23` for Telnet. It is shown here as an example of over-riding
the defaults

It is possible to swap out password/b64password and enable/b64enable.

You can also use dynamic datastore values.

After modifying the configuration, tell StackStorm to load it into the database with `sudo st2ctl reload --register-configs`
