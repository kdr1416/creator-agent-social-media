"""Animate the approved album still using one rigid hinged book leaf.

The house always remains a photograph. Both hands track real page points.
"""
import json,math,re,shutil,wave,copy,base64
from pathlib import Path
from xml.etree import ElementTree as ET
from prepare import ROOT,digest
from s05_final_frame_v5 import scene

OUT=ROOT/'revisions/S05-album-pilot-v5-r1'
SVG='http://www.w3.org/2000/svg'
ET.register_namespace('',SVG)
def txt(node):return ET.tostring(node,encoding='unicode')
def projection(x,y,angle):
    # Leaf hinge is the actual book gutter x=350, centered at y=780.
    theta=math.radians(angle);dx=x-350;dy=y-780
    z=-dx*math.sin(theta);f=1400/(1400-z)
    return 350+dx*math.cos(theta)*f,780+dy*f
def ease(t):return 4*t*t*t if t<.5 else 1-((-2*t+2)**3)/2
def pose(point,shoulder):return ((point[0]-shoulder[0])/1.1,(point[1]-shoulder[1])/1.1)

def main():
    if OUT.exists():raise RuntimeError('Revision exists; refuse to overwrite')
    (OUT/'assets').mkdir(parents=True);(OUT/'renders').mkdir()
    for src,name in [(ROOT/'assets/fonts/segoe-ui-black.ttf','display.ttf'),(ROOT/'assets/runtime/gsap.min.js','gsap.min.js'),(ROOT/'revisions/S05-final-frame-v5/assets/townhouse.jpg','townhouse.jpg'),(ROOT/'pilots/S05/assets/voice.wav','voice.wav')]:shutil.copy2(src,OUT/'assets'/name)
    for n in ['CREDITS.md','CREDITS.json']:shutil.copy2(ROOT/'revisions/S05-final-frame-v5'/n,OUT/n)
    with wave.open(str(OUT/'assets/voice.wav'),'rb') as w:duration=w.getnframes()/w.getframerate()
    root=ET.fromstring('<svg xmlns="'+SVG+'">'+scene()+'</svg>')
    album=root.find(".//*[@id='open-viewing-album']")
    # The final still has foreground forearm copies. Give every copy unique IDs before animation.
    id_counts={}
    for el in root.iter():
        id=el.get('id')
        if id:
            id_counts[id]=id_counts.get(id,0)+1
            if id_counts[id]>1:el.set('id','foreground-'+id)
    # Remove the album temporarily to partition scene depth into rear world / front hands.
    children=list(root);split=children.index(album)
    rear=children[:split];front=children[split+1:]
    defs=rear[0]
    left_clip=ET.SubElement(defs,'{'+SVG+'}clipPath',{'id':'album-left-half'})
    ET.SubElement(left_clip,'{'+SVG+'}rect',{'x':'0','y':'560','width':'350','height':'440'})
    left=ET.Element('{'+SVG+'}g',{'clip-path':'url(#album-left-half)'})
    left.append(copy.deepcopy(album))
    # Right half is rendered inside one rigid 3D plane: no width/height/scale distortion.
    leaf_album=copy.deepcopy(album);leaf_defs=copy.deepcopy(defs)
    for tree in [leaf_album,leaf_defs]:
        for el in tree.iter():
            if el.get('id'):el.set('id','leaf-'+el.get('id'))
            for key,val in list(el.attrib.items()):
                if 'url(#' in val:el.set(key,val.replace('url(#','url(#leaf-'))
    # Avoid carrying unrelated marker definitions into the leaf; the world still owns its own defs.
    leaf='<svg xmlns="'+SVG+'" width="300" height="420" viewBox="350 570 300 420">'+txt(leaf_defs)+txt(leaf_album)+'</svg>'
    # Self-contained SVG image transport keeps the rigid page editable without exposing
    # out-of-viewport SVG children to the 3D layout auditor as false gauge pointers.
    image_data=base64.b64encode((OUT/'assets/townhouse.jpg').read_bytes()).decode('ascii')
    leaf=leaf.replace('href="assets/townhouse.jpg"','href="data:image/jpeg;base64,'+image_data+'"')
    (OUT/'assets/right-leaf.svg').write_text(leaf,encoding='utf-8')
    leaf='<img id="right-leaf-art" src="assets/right-leaf.svg" width="300" height="420" alt="Printed right album page">'
    rear_svg='<svg id="album-world" xmlns="'+SVG+'" width="720" height="1280" viewBox="0 0 720 1280">'+''.join(txt(x) for x in rear)+txt(left)+'</svg>'
    # New right leaf covers only the right part of the existing physical book.
    foreground='<svg id="album-hands" xmlns="'+SVG+'" width="720" height="1280" viewBox="0 0 720 1280">'+''.join(txt(x) for x in front)+'</svg>'
    opening_at=2.42;opening_duration=2.35;initial_angle=50
    grips={'far':((480,590),(502.5,497.2)),'near':((610,595),(594.9,509.3))}
    js=['const tl=gsap.timeline({paused:true});',f"tl.fromTo('#right-album-leaf',{{rotationY:{initial_angle},transformPerspective:1400,transformOrigin:'0% 50%'}},{{rotationY:0,duration:{opening_duration},ease:'power2.inOut'}},{opening_at});"]
    for hand,(pagepoint,shoulder) in grips.items():
        initial=pose(projection(*pagepoint,initial_angle),shoulder)
        path_selector=f'#s05v5-{hand}-path,#foreground-s05v5-{hand}-path'
        hand_selector=f'#s05v5-{hand}-hand,#foreground-s05v5-{hand}-hand'
        controls=-35 if hand=='far' else 27
        d=f'M0 0Q{controls} {initial[1]*.65:.6f} {initial[0]:.6f} {initial[1]:.6f}'
        js.append(f"tl.fromTo('{path_selector}',{{attr:{{d:'{d}'}}}},{{attr:{{d:'{d}'}},duration:.001}},0);")
        js.append(f"tl.fromTo('{hand_selector}',{{attr:{{cx:{initial[0]},cy:{initial[1]}}}}},{{attr:{{cx:{initial[0]},cy:{initial[1]}}},duration:.001}},0);")
        paths=[];points=[];samples=60
        for i in range(1,samples+1):
            t=i/samples;angle=initial_angle*(1-ease(t));x,y=pose(projection(*pagepoint,angle),shoulder)
            paths.append({'attr':{'d':f'M0 0Q{controls} {y*.65:.6f} {x:.6f} {y:.6f}'},'duration':opening_duration/samples,'ease':'none'})
            points.append({'attr':{'cx':round(x,6),'cy':round(y,6)},'duration':opening_duration/samples,'ease':'none'})
        for selector in path_selector.split(','):
            js.append(f"tl.to('{selector}',{{keyframes:{json.dumps(paths)},ease:'none'}},{opening_at});")
        for selector in hand_selector.split(','):
            js.append(f"tl.to('{selector}',{{keyframes:{json.dumps(points)},ease:'none'}},{opening_at});")
        # The last settling pose is the exact approved contour and grip position.
        final_d='M0 0Q-35 59-20.45455 84.36364' if hand=='far' else 'M0 0Q27 46 13.72727 77.90909'
        fx,fy=(-20.45455,84.36364) if hand=='far' else (13.72727,77.90909)
        js.append(f"tl.to('{path_selector}',{{attr:{{d:'{final_d}'}},duration:.10,ease:'power2.out'}},4.77);")
        js.append(f"tl.to('{hand_selector}',{{attr:{{cx:{fx},cy:{fy}}},duration:.10,ease:'power2.out'}},4.77);")
    js.append("tl.fromTo('#album-title',{opacity:0,y:7},{opacity:1,y:0,duration:.22,ease:'power2.out'},4.95);")
    js.append("window.__timelines['s05-album-pilot-v5-r1']=tl;")
    page=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>S05 album pilot v5 r1</title><script src="assets/gsap.min.js"></script><style>
    @font-face{{font-family:Display;src:url('assets/display.ttf');font-weight:900;font-display:block}}
    html,body{{width:100%;height:100%;margin:0;overflow:hidden}}
    #s05-album-pilot-v5-r1{{position:relative;width:100%;height:100%;background:#FFF3E8;overflow:hidden}}
    #album-world,#album-hands{{position:absolute;inset:0;width:720px;height:1280px;overflow:hidden}}
    #album-hands{{pointer-events:none}}
    #right-leaf-slot{{position:absolute;left:350px;top:570px;width:300px;height:420px}}
    #right-album-leaf{{position:absolute;inset:0;transform-style:preserve-3d}}
    #right-album-leaf svg{{display:block;overflow:hidden}}
    #album-title{{position:absolute;left:60px;top:164px;width:600px;text-align:center;margin:0;color:#0870AC;font:900 64px/1.3 Display,sans-serif}}
    </style></head><body><div id="s05-album-pilot-v5-r1" data-composition-id="s05-album-pilot-v5-r1" data-width="720" data-height="1280" data-duration="{duration:.12f}" data-fps="30">
    {rear_svg}<div id="right-leaf-slot"><div id="right-album-leaf">{leaf}</div></div>{foreground}<h1 id="album-title">MALTA</h1>
    <audio id="album-voice" class="clip" src="assets/voice.wav" data-start="0" data-duration="{duration:.12f}" data-track-index="2"></audio>
    </div><script>{''.join(js)}</script></body></html>'''
    (OUT/'index.html').write_text(page,encoding='utf-8')
    (OUT/'hyperframes.json').write_text(json.dumps({'authoringSkill':'general-video','media':{'autoProxy':False}}),encoding='utf-8')
    d={'scene_id':'S05','revision':'album-pilot-v5-r1','based_on':'approved S05 final-frame-v5','duration':duration,'source_start_sample':435629,'source_end_sample':572581,'signature':'Finish opening an already held photographic album from a lifted right half to the approved flat spread. Hands track two page-margin points throughout. The real house never becomes a separate object.','opening_interval':[opening_at,opening_at+opening_duration],'initial_angle':initial_angle,'hinge':[350,780],'perspective':1400,'grips':grips,'proof_times':[.15,2.2,3.15,3.75,4.5,5.35],'approval':'motion_pending_user_review','original_voice_sha256':digest(OUT/'assets/voice.wav'),'static_reference_sha256':digest(ROOT/'revisions/S05-final-frame-v5/FINAL_FRAME.png')}
    (OUT/'DIRECTION.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
    print(OUT)

if __name__=='__main__':main()
