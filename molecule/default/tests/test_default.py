import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_prometheus_metrics(host):
    out = host.check_output('curl http://localhost:12345/metrics')
    assert 'process_cpu_seconds_total' in out
