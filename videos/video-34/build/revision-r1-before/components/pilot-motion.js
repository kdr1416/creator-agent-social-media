/* VIDEO-34 original scene choreography. GSAP 3.14.x, seek-driven, no clock callbacks. */
function groundedStride(tl, id, opts) {
  const {start, steps, period, swing, x, y, run = false} = opts;
  const back = `#${id}-leg-back`, front = `#${id}-leg-front`;
  const a = `#${id}-arm-back`, b = `#${id}-arm-front`;
  tl.set([back, front], {transformOrigin: '50% 0%'}, 0);
  tl.set([a,b], {transformOrigin: '50% 0%'}, 0);
  for (let i=0; i<steps; i++) {
    const t=start+i*period;
    for (const [target,sign] of [[back,1],[front,-1],[a,-0.6],[b,0.6]]) {
      tl.to(target,{rotation:swing*sign,duration:period/4,ease:'sine.inOut'},t);
      tl.to(target,{rotation:-swing*sign,duration:period/2,ease:'sine.inOut'},t+period/4);
      tl.to(target,{rotation:0,duration:period/4,ease:'sine.inOut'},t+period*3/4);
    }
  }
  // Translation is in each outer group's local SVG scale; authored placements remain intact.
  tl.to(`#${id}`,{x:`+=${x}`,y:`+=${y}`,duration:steps*period,ease:'none'},start);
}

function createPilotTimeline(id) {
  const tl=gsap.timeline({paused:true});
  if(id==='S03') {
    tl.set('#world',{svgOrigin:'360 850',scale:1.075,x:9,y:-20},0);
    groundedStride(tl,'walker-a',{start:.1,steps:3,period:.85,swing:12,x:29,y:-13});
    groundedStride(tl,'walker-b',{start:.2,steps:3,period:.85,swing:11,x:29,y:-13});
    groundedStride(tl,'runner',{start:2.05,steps:4,period:.47,swing:28,x:121,y:-66,run:true});
    // One slow opening-out reframe links the path, café and small square.
    tl.to('#world',{scale:1,x:0,y:0,duration:1.45,ease:'sine.inOut'},2.72);
    tl.set('#cafe-left-arm',{transformOrigin:'0% 0%'},0);
    tl.to('#cafe-left-arm',{rotation:-14,duration:.52,ease:'sine.inOut'},3.42);
    tl.to('#cafe-left-arm',{rotation:0,duration:.45,ease:'sine.inOut'},4.0);
    tl.to('#cafe-cup',{y:-7,x:-3,duration:.46,ease:'sine.inOut'},3.42);
    tl.to('#cafe-cup',{y:0,x:0,duration:.46,ease:'sine.inOut'},3.95);
    tl.set('#friend-a-arm-front',{transformOrigin:'50% 0%'},0);
    tl.to('#friend-a-arm-front',{rotation:-53,duration:.55,ease:'power2.inOut'},4.72);
    tl.to('#friend-a-arm-front',{rotation:-37,duration:.45,ease:'sine.inOut'},5.3);
    tl.set('#friend-b-head',{transformOrigin:'50% 80%'},0);
    tl.to('#friend-b-head',{rotation:-8,duration:.4,ease:'sine.inOut'},5.38);
    tl.to('#friend-b-head',{rotation:0,duration:.45,ease:'sine.inOut'},5.85);
    // Final attention change is modest: the café stays spatially present.
    tl.to('#world',{scale:1.035,x:-8,y:-17,duration:1.1,ease:'sine.inOut'},6.7);
    tl.set('#family-child-head',{transformOrigin:'50% 80%'},0);
    tl.to('#family-child-head',{rotation:-10,duration:.55,ease:'sine.inOut'},6.9);
    tl.set('#family-parent-head',{transformOrigin:'50% 80%'},0);
    tl.to('#family-parent-head',{rotation:9,duration:.65,ease:'sine.inOut'},7.3);
  } else if(id==='S08') {
    tl.set('#parent-head',{svgOrigin:'315 710',scale:.9,rotation:-16},0);
    tl.set('#child-head',{svgOrigin:'545 910',scale:.84,rotation:-3},0);
    tl.set('#parent-gaze',{x:-6,y:5},0);
    // A single purposeful final keystroke, then a pause: no perpetual typing loop.
    tl.to('#parent-hand',{y:-2,duration:.17,ease:'sine.inOut'},.22);
    tl.to('#parent-hand',{y:0,duration:.17,ease:'sine.inOut'},.39);
    tl.to('#parent-head',{rotation:-9,duration:.9,ease:'sine.inOut'},.65);
    tl.to('#parent-gaze',{x:1,y:1,duration:.8,ease:'sine.inOut'},1.15);
    // Hand clears the lid before it closes; hinge is fixed at (170,835).
    tl.to('#parent-near-arm',{attr:{d:'M340 757Q380 789 366 816L302 805'},duration:.5,ease:'sine.inOut'},1.85);
    tl.to('#parent-hand',{x:22,y:-29,duration:.5,ease:'sine.inOut'},1.85);
    tl.set('#laptop-position',{svgOrigin:'170 835'},0);
    tl.to('#laptop-position',{scaleY:.045,skewX:-8,duration:.38,ease:'power2.inOut'},2.37);
    tl.to('#parent-head',{rotation:9,duration:.8,ease:'sine.inOut'},2.95);
    tl.to('#parent-gaze',{x:4,y:0,duration:.7,ease:'sine.inOut'},3.02);
    tl.to('#parent-near-arm',{attr:{d:'M340 757Q390 811 411 864L468 924'},duration:1.52,ease:'power2.inOut'},3.15);
    tl.to('#parent-hand',{x:192,y:90,duration:1.52,ease:'power2.inOut'},3.15);
    tl.to('#parent-near-sleeve',{attr:{d:'M327 739Q351 732 369 774L341 794 311 758Z'},duration:.9,ease:'sine.inOut'},3.15);
    tl.to('#child-head',{rotation:-10,duration:.65,ease:'sine.inOut'},3.95);
    tl.to('#child-near-arm',{attr:{d:'M524 937Q502 950 490 943L468 924'},duration:.66,ease:'sine.inOut'},4.07);
    tl.to('#child-hand',{x:-7,y:-41,duration:.66,ease:'sine.inOut'},4.07);
    tl.to('#parent-smile',{attr:{d:'M320 680Q328 688 337 679'},duration:.45,ease:'sine.inOut'},4.68);
    tl.to('#child-smile',{attr:{d:'M530 886Q539 894 548 883'},duration:.45,ease:'sine.inOut'},4.68);
  }
  return tl;
}
