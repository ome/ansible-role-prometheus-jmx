import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_prometheus_metrics(File):
    assert File('/opt/prometheus/jars/jmx_prometheus_javaagent.jar').exists
