import json
import os

from click import command
from utils import exec_command

DAEMON = os.getenv('DAEMON')
RPC = os.getenv('RPC')
CHAINID = os.getenv('CHAINID')


def query_commission_rewards(validator_addr):
    try:
        command = f"{DAEMON} q distribution commission {validator_addr} --node {RPC} --chain-id {CHAINID} --output json"
        commission,commissionerr = exec_command(command)
        if len(commissionerr):
            return False, commissionerr
        return True,json.loads(commission)
    except Exception as e:
        return False,e

def query_community_pool():
    try:
        command = f"{DAEMON} q distribution community-pool --node {RPC} --chain-id {CHAINID} --output json"
        pool,poolerr = exec_command(command)
        if len(poolerr):
            return False,poolerr
        return True,json.loads(pool)
    except Exception as e:
        return False,e

def query_params():
    try:
        command = f"{DAEMON} q distribution params --node {RPC} --chain-id {CHAINID} --output json"
        params,paramserr = exec_command(command)
        if len(paramserr):
            return False,paramserr
        return True,json.loads(params)
    except Exception as e:
        return False,e

def query_rewards_singleval(delegator_addr,validator_addr):
    try:
        command = f"{DAEMON} q distribution rewards {delegator_addr} {validator_addr} --node {RPC} --chain-id {CHAINID} --output json"
        rewards,rewardserr = exec_command(command)
        if len(rewardserr):
            return False,rewardserr
        return True,json.loads(rewards)
    except Exception as e:
        return False,e

def query_rewards(delegator_addr):
    try:
        command = f"{DAEMON} q distribution rewards {delegator_addr} --node {RPC} --chain-id {CHAINID} --output json"
        rewards,rewardserr = exec_command(command)
        if len(rewardserr):
            return False,rewardserr
        return True,json.loads(rewards)
    except Exception as e:
        return False,e

def query_slashes(validator_addr,start_height,end_height):
    try:
        command = f"{DAEMON} q distribution slashes {validator_addr} {start_height} {end_height} --node {RPC} --chain-id {CHAINID} --output json"
        slashes,slasherr = exec_command(command)
        if len(slasherr):
            return False,slasherr
        return True,json.loads(slashes)
    except Exception as e:
        return False,e

def query_validator_rewards(validator_addr):
    try:
        command = f"{DAEMON} q distribution validator-outstanding-rewards {validator_addr} --node {RPC} --chain-id {CHAINID} --output json"
        valrewards,valrewardserr = exec_command(command)
        if len(valrewardserr):
            return False,valrewardserr
        return True,json.loads(valrewards)
    except Exception as e:
        return False,e

