import json,urllib.request
from pathlib import Path
T=Path('work/weblate/.token').read_text().strip()
M={143860869:'Återkallande av åtkomst är inte slutfört',143860907:'Hela perioden',143860962:'Banksynkronisering',143860963:'Banksynkronisering',143860964:'Banksynkronisering är frånkopplad',143860984:'Kan göra allt som grundläggande användare kan. Dessutom kan de lägga till nya användare i katalogen och få åtkomst till budgetfiler från alla användare.',143860993:'Kategorilärande',143860994:'Kategorilärande är inaktiverat',143860995:'Inställningar för kategorilärande',143861008:'Kontrollera mallar',143861010:'Kontrollerar inloggning med Header Token …',143861039:'Molnfil-ID saknas.',143861046:'Slutförd',143861091:'Dashboardwidgeten har sparats.',143861127:'Om OpenID inaktiveras stängs fleranvändarläget av.',143861128:'Visning',143861129:'Visningsnamn',143861151:'Redigera dashboard',143861154:'Redigera den här widgeten för att ändra innehållet i **markdown**.',143861169:'Rensning vid månadsslut',143861188:'Det gick inte att importera dashboardfilen.',143861195:'Det gick inte att uppdatera inloggningsmetoderna',143861196:'Det gick inte att spara dashboardwidgeten.',143861205:'Filternamn',143861206:'Filtrera betalningsmottagare …',143861207:'Filtrera regler …',143861208:'Filtrera scheman …',143861209:'Filtrera till de valda transaktionerna',143861211:'Filtrera användare …',143861212:'Filtrerat saldo:'}
for i,v in M.items():
 d=json.dumps({'target':[v],'state':20},ensure_ascii=False).encode();r=urllib.request.Request(f'https://hosted.weblate.org/api/units/{i}/',data=d,method='PATCH',headers={'Authorization':f'Token {T}','Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(r) as x: print(i,x.status)
 except Exception as e: print(i,'ERROR',e)
