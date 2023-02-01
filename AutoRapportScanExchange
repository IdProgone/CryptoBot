@echo off
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"
echo Le Téléchargement est en cours ...
echo Durée du Téléchargement 45 secondes
echo ... ... ... 
echo ... ...
echo ...  
echo      ::::::::::: :::::::::  :::::::::  :::::::::   ::::::::   ::::::::   ::::::::  ::::    ::: :::::::::: 
echo         :+:     :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:+:   :+: :+:         
echo        +:+     +:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ +:+        +:+    +:+ :+:+:+  +:+ +:+          
echo       +#+     +#+    +:+ +#++:++#+  +#++:++#:  +#+    +:+ :#:        +#+    +:+ +#+ +:+ +#+ +#++:++#      
echo      +#+     +#+    +#+ +#+        +#+    +#+ +#+    +#+ +#+   +#+# +#+    +#+ +#+  +#+#+# +#+            
echo     #+#     #+#    #+# #+#        #+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#   #+#+# #+#             
echo ########### #########  ###        ###    ###  ########   ########   ########  ###    #### ##########  
python ScanExchange-BTC_BRL.py > output_%YYYY%%MM%%DD%_%HH%h%Min%.txt
start output_%YYYY%%MM%%DD%_%HH%h%Min%.txt
@echo off
timeout /t 5
exit

