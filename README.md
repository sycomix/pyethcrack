# pyethcrack
very (very) simple script to brute force a v3 ethereum wallet, mostly made to get familiar with git / github

###Credit
I'm really a n00b at this; I pulled this code directly from this stackexchange comment:
https://ethereum.stackexchange.com/questions/6845/how-to-apply-pyethrecover-py-on-v3-json-transfor-v3-json-to-v1

Which was, itself, more or less a stripped down and leaner version of the pyethrecover tool, which appears to only work on earlier versions of the ethereum wallets (from the presale)

##Installation
You'll need to first install pyethereum (I think? I actually have not tested without having pyethereum installed), which is best done through pip:
'#pip install ethereum'


##Usage
For right now the password grammar is embedded directly into the script. See password_spec.txt for a better explanation, and then crack open your editor to put it into the script. Run it, specifying the wallet file (UTC-\*\*\*) as the first argument. If you constructed your password rules well enough, it'll display the correct password after iterating through all the possible combos.

Good Luck!
