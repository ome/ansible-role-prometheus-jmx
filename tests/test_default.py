import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_prometheus_metrics(Command):
    out = Command.check_output('curl http://localhost:12345/metrics')
    assert 'process_cpu_seconds_total' in out
