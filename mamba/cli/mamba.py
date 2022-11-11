@click.group(invoke_without_command=True)
@click.option('-config', default=expanduser('~/.akachain/akc-mamba/mamba/config/.env'))
@click.option('--set-default/--no-default', default=False)

def mamba(config, set_default):
    # Setup all shared global utilities in settings module
    settings.init(config, set_default)
    if mamba.invoke_without_command:
       hiss.rattle('Initialize mamba')
       hiss.echo('Successfully with \'%s\' on the %s!' % (config, settings.EKS_CLUSTER_NAME))

mamba.add_command(environment)
mamba.add_command(vpn)
mamba.add_command(copyscripts)
mamba.add_command(reg_orgs)
mamba.add_command(reg_orderers)
mamba.add_command(reg_peers)
mamba.add_command(enroll_orderers)
mamba.add_command(enroll_peers)
mamba.add_command(rca)
mamba.add_command(ica)
mamba.add_command(zookeeper)
mamba.add_command(kafka)
mamba.add_command(orderer)
mamba.add_command(updatefolder)
mamba.add_command(peer)
mamba.add_command(gen_artifact)
mamba.add_command(channel_artifact)
mamba.add_command(admin)
mamba.add_command(secret)
mamba.add_command(bootstrap)
mamba.add_command(start)
mamba.add_command(delete)
mamba.add_command(terminate)
mamba.add_command(explorer)
mamba.add_command(prometheus)
mamba.add_command(grafana)
mamba.add_command(create_org)
mamba.add_command(channel_config)

if __name__ == '__main__':
    mamba()