/* Scene-local voice cues. SVG opacity/transform state is fully seekable. */
function addTypography(tl,id) {
  const enter=(selector,at,vars={})=>tl.fromTo(selector,{opacity:0,...vars},{opacity:1,x:0,y:0,duration:.34,ease:'power2.out'},at);
  const exit=(selector,at)=>tl.to(selector,{opacity:0,y:-6,duration:.2,ease:'sine.in'},at);
  if(id==='S03') {
    enter('#ty-walk-a',.333917,{x:-14});
    enter('#ty-walk-b',.453917,{y:28});
    exit(['#ty-walk-a','#ty-walk-b'],1.95);
    // Type is in the world's coordinate system, travelling with the café fabric.
    enter('#ty-cafe',3.513917,{y:10});
    enter('#ty-outdoor',3.853917,{x:12});
    exit(['#ty-cafe','#ty-outdoor'],4.75);
    enter('#ty-family-a',7.373917,{x:-10});
    enter('#ty-family-b',7.573917,{y:12});
  } else {
    enter('#ty-work-a',2.41,{y:12});
    enter('#ty-work-b',2.53,{y:12});
    exit(['#ty-work-a','#ty-work-b'],2.97);
    enter('#ty-time-a',3.03,{x:-12});
    enter('#ty-time-b',3.19,{x:16});
    exit(['#ty-time-a','#ty-time-b'],4.5);
    enter('#ty-caption',4.62,{y:-8});
    enter('#ty-family-a',4.73,{x:-9});
    enter('#ty-family-b',4.89,{y:10});
  }
}
