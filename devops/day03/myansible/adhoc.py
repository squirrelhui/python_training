import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# Options是在执行ansible临时命令时，提供的选项，需要了解的选项有
# connection是连接方式，有local表示在本机执行，ssh表示是ssh执行，smart表示自动选择
# forks指的是一次同事向多少台主机发送指令
Options = namedtuple('Options',
                     ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                  become_user=None, check=False, diff=False)

# Dataloader用于解析json/ini/yaml等文件，将其转换成python的数据类型
loader = DataLoader()  # Takes care of finding and reading yaml, json and ini files
# 设置密码
passwords = dict(vault_pass='secret')

# Instantiate our ResultCallback for handling results as they come in. Ansible expects this to be one of its main display outlets

# create inventory, use path to host config file as source or hosts in a comma separated string
# 主机清单文件，表示方式有两种
# 一种是将各个主机用冒号分隔，成为一个字符串
# 另外一中方式是使用主机路径清单列表
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources=['hosts'])

# 变量管理
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
play_source = dict(
    name="Ansible Play",
    hosts='webservers', # 在哪台主机上执行任务
    gather_facts='no',
    tasks=[
        dict(action=dict(module='shell', args='id root'), register='shell_out'),
        dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
    ]
)

# 创建play对象
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# 通过任务队列管理器执行play
tqm = None
try:
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=options,
        passwords=passwords,
    )
    result = tqm.run(play)  # most interesting data for a play is actually sent to the callback's methods
finally:
    # we always need to cleanup child procs and the structres we use to communicate with them
    if tqm is not None:
        tqm.cleanup()

    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
