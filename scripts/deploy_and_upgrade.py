from scripts.helpful_scripts import encode_function_data, get_account, encode_function_data, upgrade
from brownie import Box, network, ProxyAdmin,TransparentUpgradeableProxy, Contract, BoxV2

def main():
    account = get_account()
    print(f"deploying Box to {network.show_active()}")
    box = Box.deploy({"from": account}, publish_source=True)
    value = box.returnValue()
    print(f"value returned: {value}")
    
    proxy_admin = ProxyAdmin.deploy({"from": account},publish_source=True)
    # initializer = box.store, 1

    box_encoded_initializer_function = encode_function_data()

    proxy = TransparentUpgradeableProxy.deploy(
      box.address,
      proxy_admin.address,
      box_encoded_initializer_function,
      {"from": account, "gas_limit": 1000000},
      publish_source=True
    )
    print(f'proxy deployed to {proxy} you can now upgrade to v2!')

    # calling proxy address and delegating the call to Box
    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)
    proxy_box.storeValue(2, {"from":account})
    print(proxy_box.returnValue())

    # upgrade
    box_v2 = BoxV2.deploy({"from":account},publish_source=True)
    # 
    upgrade_txn = upgrade(account, proxy, box_v2.address,
      proxy_admin_contract=proxy_admin
    )
    upgrade_txn.wait(1)
    print("Proxy has been upgraded!!")
    proxy_box = Contract.from_abi("BoxV2", proxy.address, BoxV2.abi)
    proxy_box.increment({"from":account})
    print(proxy_box.returnValue())