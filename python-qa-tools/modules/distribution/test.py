import os,logging,time
from unittest.mock import DEFAULT
from core.keys import keys_show

from modules.distribution.tx import (
    DEFAULT_GAS,
    tx_fund_communitypool,
    tx_withdraw_addr,
    tx_withdraw_allrewards,
    tx_withdraw_commisionRewards,
    tx_withdraw_rewards
)
from modules.distribution.query import (
    query_commission_rewards,
    query_community_pool,
    query_params,
    query_rewards,
    query_rewards_singleval,
    query_slashes,
    query_validator_rewards
)

HOME = os.getenv("HOME")
logging.basicConfig(format="%(message)s", level=logging.DEBUG)

validator = keys_show("validator1","val")[1]["address"]
delegator = keys_show("account1","acc")[1]["address"]
print(validator)
print(delegator)


# query validator rewards
status,before_claim = query_rewards_singleval(delegator,validator)
if not status:
    logging.error(f"error in querying rewards :: {before_claim}")
else:
    rewards = query_rewards_singleval(delegator,validator)[1]["rewards"][0]["amount"]
    logging.info(f"rewards :: {rewards}")

time.sleep(3)

status,rewards = tx_withdraw_rewards("account1",validator)
if not status:
    logging.error(f"error in tx withdraw rewards :: {rewards}")
else:
    logging.info(f"tx_hash  :: {rewards['txhash']}")

time.sleep(6)

status,all_rewards = tx_withdraw_allrewards("account1")
if not status:
    logging.error(f"error in tx withdraw all rewards :: {all_rewards}")
else:
    logging.info(f"tx_hash  :: {all_rewards['txhash']}")

