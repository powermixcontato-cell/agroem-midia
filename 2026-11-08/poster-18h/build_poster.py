from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path
import json
P=Path(__file__).resolve().parent
W,H=1080,1350
base=ImageOps.fit(Image.open(P/'background.jpg').convert('RGB'),(W,H),centering=(.35,.45)).convert('RGBA')
base=Image.alpha_composite(base,Image.new('RGBA',(W,H),(0,30,20,138)))
d=ImageDraw.Draw(base)
FONT='/usr/share/fonts/truetype/sand-box/google/'
def f(size,bold=True):return ImageFont.truetype(FONT+'Poppins/Poppins-'+('Bold' if bold else 'Regular')+'.ttf',size)
def condensed(size):return ImageFont.truetype(FONT+'Barlow Condensed/BarlowCondensed-ExtraBold.ttf',size)
cream='#FFF9E9';orange='#FF920B';green='#123E2E';red='#CE2027'
def txt(x,y,s,font,fill=cream,**kw):d.text((x,y),s,font=font,fill=fill,**kw)
def orange_icon(x,y,r=15):
 d.ellipse((x-r,y-r,x+r,y+r),fill=orange)
 d.ellipse((x-2,y-r-8,x+12,y-r+1),fill='#68AF3A')
# Branded header, same rounded green badge as reference.
d.rounded_rectangle((38,30,405,87),radius=27,fill=green)
orange_icon(66,60,15);txt(92,38,'@agroem.campo',f(29))
d.rounded_rectangle((805,37,1040,79),radius=10,fill=orange)
txt(825,46,'INVENTÁRIO 2026',f(19),green)
txt(46,103,'AS',f(31),orange)
txt(31,94,'12',condensed(270),orange)
for y,s,size in [(135,'REGIÕES DO',65),(215,'CINTURÃO',65),(295,'DA LARANJA',65)]:
 font=condensed(size);width=d.textlength(s,font=font)
 d.rounded_rectangle((322,y,322+width+30,y+73),radius=10,fill=red)
 txt(337,y-3,s,font)
txt(46,391,'POR ÁREA DE POMARES • SP E TRIÂNGULO/SUDOESTE MINEIRO',f(22))
txt(46,425,'400.260 hectares • principais variedades de laranja',f(21,False))
data=[('Avaré','SP',58959),('Duartina','SP',58600),('Bebedouro','SP',52171),('Matão','SP',37807),('Porto Ferreira','SP',37340),('Triângulo Mineiro','MG',35812),('Limeira','SP',26799),('Itapetininga','SP',25900),('Votuporanga','SP',22513),('São José do Rio Preto','SP',21120),('Altinópolis','SP',12815),('Brotas','SP',10424)]
assert sum(row[2] for row in data)==400260
assert sum(row[2] for row in data[:4])==207537
for i,(name,state,area) in enumerate(data):
 col=i%3;row=i//3;x=36+col*342;y=477+row*165;cw=326;ch=151
 d.rounded_rectangle((x,y,x+cw,y+ch),radius=13,fill=('#F8F5E8' if (col+row)%2==0 else '#E0EADD'))
 txt(x+14,y+6,f'{i+1}º',f(21),green)
 d.rounded_rectangle((x+cw-50,y+8,x+cw-10,y+36),radius=6,fill=green)
 txt(x+cw-45,y+8,state,f(17))
 size=23
 while d.textlength(name,font=f(size))>cw-30:size-=1
 txt(x+cw/2,y+37,name,f(size),green,anchor='mt')
 val=f'{area:,}'.replace(',','.')
 txt(x+cw/2,y+64,val,condensed(53),green,anchor='mt')
 txt(x+cw/2,y+118,'HECTARES',f(15),green,anchor='mt')
 # Orange underline signals visual family without misleading map or stock logo.
 d.rounded_rectangle((x+95,y+141,x+cw-95,y+145),radius=2,fill=orange)
# Legible criteria footer.
d.rounded_rectangle((30,1147,1050,1314),radius=14,fill='#0C2B21')
d.rectangle((48,1159,210,1163),fill=orange)
for y,s in [(1172,'Fonte: Fundecitrus • Inventário 2026 • tabela 44, p. 60.'),(1196,'Retrato: março/2026 • relatório: 10/06/2026 • consulta: 07/11/2026.'),(1220,'Critério: área total, pomares em formação + adultos. Regiões, não municípios.'),(1244,'Não é ranking nacional, de produção ou de produtividade.'),(1272,'Foto ilustrativa: Hans Braxmeier / Wikimedia Commons • CC0 • editada.')]:txt(48,y,s,f(18,False))
txt(41,1320,'AGRO EM CAMPO',f(15),cream)
txt(1039,1318,'@agroem.campo',f(19),cream,anchor='rt')
base.convert('RGB').save(P/'poster.jpg',quality=95,optimize=True)
(P/'data.json').write_text(json.dumps({'topic':'12 regiões do cinturão da laranja por área de pomares','reference':'Fundecitrus inventário março/2026, tabela 44 p.60','total_hectares':400260,'regions':[{'rank':i+1,'region':n,'state':s,'hectares':a} for i,(n,s,a) in enumerate(data)]},ensure_ascii=False,indent=2))
print(P/'poster.jpg')
