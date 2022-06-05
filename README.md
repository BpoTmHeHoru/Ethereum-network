# Ethereum-network
Ethereum network

Windows:

Создадим каталог, в котором будем хранить нашу сеть:
                EthereumNet
                            network
                            contract
                
Запустим PowerShell в папке network
             puppeth
             Придумываем имя нашей сети
             у меня это будет ethereumnet
             
              2. Configure new genesis
              
              1. Create new genesis from scratch

              1. Ethash - proof-of-work Будем майнить =)
              
              оставляем без изменений

              выберем yes
              
              попросят выбрать ID network оставим по умолчанию
              
               2. Manage existing genesis

               2. Export genesis configurations
               
               создадим каталог bnode
               
               geth --datadir bnode init .\ethereumnet.json
              
               
               заходим в консоль, для этого нам понадобятся bnode и ChainId
               geth --datadir ethereumnet --port 30301 --networkid 63691  --nodiscover console
               
               admin.nodeInfo получаем "enode" прописываем его в конфиг
               
                создадим 2 аккаунта:
	             $ personal.newAccount("password")


	             $ miner.setEtherbase(eth.accounts[0]) 
               

               $ geth --datadir .\node3\ init .\ethereumnet.json
               $ geth --datadir .\node4\ init .\ethereumnet.json  
	          
               
        
	       $ bootnode -genkey boot.key 	и копируем в папку bnode

               
               $ miner.start()
               

    
