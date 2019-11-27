from django.shortcuts import render
from django.http import HttpResponse
from .caraDeCacaExpress.game import *
from .caraDeCacaExpress.Game.players import *
from .caraDeCacaExpress.Game.GameObjets import *


def home(request):
    return render(request,'careKKWeb/home.html')


realPlayer=player(hand([]),openField([]),closeField([]))
player2=goodDeterministicPlayerV2(hand([]),openField([]),closeField([]))
deck0=deck([card('2',2,2),card('2',2,2),card('2',2,2),card('2',2,2),card('3',3,3),card('3',3,3),card('7',7,7),card('7',7,7),card('7',7,7),card('7',7,7),card('10',10,10),card('10',10,10),card('10',10,10),card('10',10,10),card('11',11,11),card('11',11,11),card('11',11,11),card('11',11,11),card('13',13,13),card('13',13,13),card('13',13,13),card('13',13,13),card('14',14,14),card('14',14,14)])
gamePvIA0=gamePvIA([realPlayer,player2],deck0,4,4)

def PvsIA(request):
    gamePvIA0.repartirCartas()    
    
    return render(request,'careKKWeb/PvsIA.html',{'p2CloseFieldLen':player2.getCloseField().fieldLen(),'p1CloseFieldLen':realPlayer.getCloseField().fieldLen()})
