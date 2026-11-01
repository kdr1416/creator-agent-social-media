"""Typography from reviewed static studies, integrated into editable SVG surfaces."""
import re
N='#092e4d';W='#fffdf6'
def text(id,x,y,size,word,fill=N,font='Display',extra=''):
 return f'<text class="type-word" id="{id}" x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{fill}" {extra}>{word}</text>'

def design(sid,art):
 if sid=='S03':
  # Solid fabric matches the café study, retaining the same physical awning.
  art=art.replace('fill="#ff7053"','fill="#dc5943"')
  art=re.sub(r'(<path[^>]*d="M34 574L282 503 337 602 35 690Z"[^>]*fill=")[^"]+',r'\g<1>#dc5943',art)
  # SVG from the R1 drawing uses XML attribute order d,fill.
  cafe='<g transform="matrix(.724637681 0 0 .724637681 8.55072464 226.8115942)">'+'<g transform="rotate(-16 103 560)">'+text('ty-cafe',103,560,82,'cà phê',W,'Editorial')+'</g>'+text('ty-outdoor',172,662,28,'NGOÀI TRỜI',N,extra='letter-spacing="3"')+'</g>'
  end=art.rfind('</g>');art=art[:end]+cafe+art[end:]
  layer=text('ty-walk-a',85,1040,66,'đi',N,'Editorial')+text('ty-walk-b',82,1205,158,'BỘ',N,extra='letter-spacing="-6"')
  layer+=text('ty-family-a',50,650,106,'gia',N,'Editorial')+text('ty-family-b',64,760,119,'đình',N,'Editorial')
 else:
  art=re.sub(r'<path\b[^>]*d="(?:M46 306|M58 318|M58 491)[^"]*"[^>]*/>','',art)
  art=re.sub(r'<ellipse cx="190" cy="365"[^>]*/>','',art)
  layer=text('ty-work-a',57,292,83,'CÔNG',N,extra='letter-spacing="-3"')+text('ty-work-b',58,390,91,'VIỆC',N,extra='letter-spacing="-3"')
  layer+=text('ty-time-a',405,415,72,'thời',N,'Editorial')+text('ty-time-b',400,516,101,'GIAN',N,extra='letter-spacing="-4"')
  layer+=text('ty-caption',420,480,27,'THỜI GIAN',N,extra='letter-spacing="3"')
  layer+=text('ty-family-a',408,586,101,'gia',N,'Editorial')+text('ty-family-b',410,700,110,'đình',N,'Editorial')
 return art.replace('</svg>',layer+'</svg>')

CSS='''@font-face{font-family:Display;src:url('assets/display.ttf')}@font-face{font-family:Editorial;src:url('assets/editorial-italic.ttf')}.type-word{opacity:0;font-kerning:normal;text-rendering:geometricPrecision}text[font-family="Display"]{font-weight:750;font-variation-settings:"wght" 750,"wdth" 85}'''
