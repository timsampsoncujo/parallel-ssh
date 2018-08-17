"""
Example script for running multiple parallel commands on multiple hosts.

Ten five second sleeps are run in parallel on all five hosts, again in parallel.

Total time taken is a little over five seconds for all fifty (50) individual commands.
"""

from pssh.clients import ParallelSSHClient
import datetime

host = 'localhost'
hosts = [host for _ in range(5)]
client = ParallelSSHClient(hosts, pool_size=len(hosts))

# Run 10 five second sleeps
cmds = ['sleep 5' for _ in range(10)]
start = datetime.datetime.now()
output = [client.run_command(cmd, stop_on_errors=False)
          for cmd in cmds]
end = datetime.datetime.now()

print("Started %s commands on %s host(s) in %s" % (
    len(cmds), len(hosts), end-start,))
start = datetime.datetime.now()
for _output in output:
    client.join(_output)
    print(_output)
end = datetime.datetime.now()
print("All commands finished in %s" % (end-start,))
