
# -*- coding:utf-8 -*- 

import gammu 

# Initialisation 
sm = gammu.StateMachine() 
sm.ReadConfig()
sm.Init() 
# Entrer le code PIN si demande 
if sm.GetSecurityStatus() == ' PIN ' :
sm.EnterSecurityCode( ' PIN ' , ' XXXX ' )
# Donnees du message 
message = { 
' Text ' : ' Message avec gammu et python !  ' ,
' SMSC ' : { ' Location ' : 1 },
' Number ' : ' +33XXXXXXXXX ' 
}
# Envoi du message
sm.SendSMS(message) 
