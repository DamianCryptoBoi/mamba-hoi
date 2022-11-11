#! /bin/bash
rm ~/.akachain/akc-mamba/mamba/config/.env
cat ./env-tmp/merchant.env-tmp >> ~/.akachain/akc-mamba/mamba/config/.env
# kubectl config use-context admin@cluster-mambabald.ap-southeast-1.eksctl.io 
# kubectl config current-context