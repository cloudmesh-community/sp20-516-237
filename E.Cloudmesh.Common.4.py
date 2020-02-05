from cloudmesh.common.Shell import Shell

my_pwd = Shell.execute('pwd')
print("My PWD: ", my_pwd)

#Below grep only works for rc = 0.  If for instance the grep pattern wasn't found the command would fail.
print("Grep output: ", Shell.execute('grep', '-c import {}/*.py'.format(my_pwd)))

#Couldn't do most of the direct Shell methods because they don't work on Windows