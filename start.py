#
# AML Generic Launcher.
#
# Author: Philly Beijing Team <PhillyBJ@microsoft.com>
#
# This Python script works as the entry script of the AML job. Specifically,
# it will be uploaded by run.py, be executed on remote VM, set up necessary
# runtime environments, and then execute a designated user command.
#

import os
import argparse

import time

parser = argparse.ArgumentParser(description="AML Generic Launcher")
parser.add_argument('--environ', default="", help="The list of environment variables.")
parser.add_argument('--config', default="", help="config runing")
parser.add_argument('--workdir', default="", help="The working directory.")
# parser.add_argument('--command', default="/bin/true", help="The command to run.")
args, _ = parser.parse_known_args()

st = time.time()
# os.system("export %s WORKDIR=%s" % (args.environ, args.workdir))
os.environ.setdefault("WORKDIR",args.workdir)
os.system("nvidia-smi")
print('!'*100)
print(os.environ['WORKDIR'])

gpu = 8

print()
print('#'*10)
print(args.config)
print('#'*10)

root_path = os.path.join(os.environ['WORKDIR'], 'suyee')
# ----------------------------- Training -------------------------

cmd = "python train.py --outdir={}/training-runs/tiny-imagenet/ \
     --data={}/datasets/tiny-imagenet.zip \
     --gpus=8 \
     --cfg=auto ".format(root_path, root_path)

print(cmd)
# os.system('chmod 777 -R ./scripts')
os.system(cmd)


end = time.time()
print('end ..., job time: {:.1f} hours'.format((end - st)/3600))
