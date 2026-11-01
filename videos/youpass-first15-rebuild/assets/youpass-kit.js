/* Reconstruction assets authored for the user-supplied 0–15s reference. */
window.YP={
 ink:'#30323B',
 mascot(id,x,y,s=1,color='#FFA000',headband=false,helmet=false){
 return `<g id="${id}" transform="translate(${x} ${y}) scale(${s})">
 <g id="${id}-far-arm" fill="none" stroke="#F68A3C" stroke-width="5" stroke-linecap="round"><path d="M24 79Q3 91-13 80"/><circle cx="-13" cy="80" r="4" fill="#F68A3C" stroke="none"/></g>
 <g id="${id}-legs" fill="none" stroke="#9F4B1F" stroke-width="5" stroke-linecap="round"><path id="${id}-leg1" d="M43 127Q36 144 29 154L21 153"/><path id="${id}-leg2" d="M73 127Q81 145 76 158L68 158"/></g>
 <g id="${id}-body"><path d="M50 17C81 2 103 25 103 59C104 87 88 119 66 131C43 145 14 130 16 104C14 77 27 29 50 17Z" fill="${color}"/>
 <path d="M61 10Q54-2 46 2Q49 12 61 10M63 10Q75-1 81 2Q76 12 63 10" fill="#69BE89"/>
 <g id="${id}-face" fill="#6F3A19"><path d="M44 49Q47 43 51 49M67 45Q71 40 74 46" fill="none" stroke="#6F3A19" stroke-width="3" stroke-linecap="round"/><path d="M53 64Q60 72 67 63Q58 58 53 64Z"/>
 <ellipse cx="40" cy="61" rx="6" ry="3" fill="#F58D3C"/><ellipse cx="78" cy="56" rx="6" ry="3" fill="#F58D3C"/></g>
 ${headband?'<path d="M30 31Q66 13 96 29L94 36Q63 22 31 39Z" fill="#C83A39"/><path d="M32 32L8 32 17 39 5 48 31 39Z" fill="#C83A39"/>':''}
 ${helmet?'<g stroke="#30323B" stroke-width="2"><path d="M24 32Q28-5 65-2Q97 0 105 30Z" fill="#F06D68"/><path d="M35 3Q57-3 70 7L67 15 38 12Z" fill="#FBEBDC" stroke="none"/><path d="M23 32L107 30 103 38 30 40Z" fill="#E7E7E9"/></g>':''}
 </g>
 <g id="${id}-near-arm" fill="none" stroke="#F68A3C" stroke-width="5" stroke-linecap="round"><path d="M77 87Q97 84 109 57"/><circle cx="109" cy="57" r="4" fill="#F68A3C" stroke="none"/></g>
 </g>`;
 },
 scooter(id,x,y,s=1,color='#FDFDFB',rider='#9EB1DE',helmet='#EEBC55'){
 return `<g id="${id}" transform="translate(${x} ${y}) scale(${s})" stroke="#30323B" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round">
 <circle cx="39" cy="108" r="19" fill="#30323B"/><circle cx="39" cy="108" r="8" fill="#9B9DA5" stroke="none"/>
 <circle cx="151" cy="106" r="19" fill="#30323B"/><circle cx="151" cy="106" r="8" fill="#9B9DA5" stroke="none"/>
 <path d="M48 58Q26 20 43-7Q51-22 64-13Q90 15 72 61Z" fill="${rider}" stroke-width="2.4"/>
 <path d="M41-7Q40-31 62-29Q82-29 85-10Z" fill="${helmet}" stroke-width="2.5"/><path d="M58-8L83-8" fill="none"/>
 <circle cx="68" cy="4" r="2" fill="#30323B" stroke="none"/><circle cx="76" cy="3" r="2" fill="#30323B" stroke="none"/>
 <path d="M63 37Q91 40 111 21" fill="none" stroke="${rider}" stroke-width="5"/>
 <path d="M18 61L82 59 95 89 120 89 119 39Q118 26 128 23L142 20 154 62 142 92 85 99 19 91Z" fill="${color}"/>
 <path d="M26 55Q40 49 75 53L84 61 26 65Z" fill="#30323B"/>
 <path d="M141 21L132-2 121-7M113-7L140-8" fill="none"/><circle cx="145" cy="27" r="6" fill="#FAD370" stroke-width="2"/>
 </g>`;
 },
 school(id,x,y,s=1,face=false){
 let windows='';for(let i=0;i<3;i++)for(let j=0;j<3;j++)windows+=`<rect x="${23+j*34}" y="${66+i*32}" width="22" height="21" rx="1" fill="#C8E9F9" stroke-width="2"/>`;
 return `<g id="${id}" transform="translate(${x} ${y}) scale(${s})" stroke="#30323B" stroke-width="3" stroke-linejoin="round">
 <path d="M10 20L140 20 137 207 13 207Z" fill="#FFFCEF"/><path d="M4 16L144 16 144 27 5 27Z" fill="#F18760"/>
 <path d="M49 16L49-22 74-45 98-23 98 16Z" fill="#FFFCEF"/><circle cx="73" cy="-10" r="17" fill="#FFFFFF" stroke-width="2"/><path d="M73-24L73-11 64-2" fill="none" stroke="#60636B" stroke-width="2"/>
 <rect x="22" y="37" width="110" height="20" rx="2" fill="#FFFFFF" stroke-width="1.5"/><text x="77" y="52" text-anchor="middle" font-size="12" fill="#30323B" stroke="none" class="yp-text">TRUNG TÂM</text>${windows}
 <path d="M57 207L57 173Q73 165 87 173L87 207Z" fill="#C79D63" stroke-width="2"/>
 ${face?'<path d="M40 171Q72 199 109 168Q108 206 75 205Q44 202 40 171Z" fill="#30323B"/><path d="M55 193Q77 185 92 195" fill="none" stroke="#F28C7E" stroke-width="7"/>':''}
 </g>`;
 },
 sparkle(id,x,y,s=1,color='#D6B65C'){return `<g id="${id}" transform="translate(${x} ${y}) scale(${s})" stroke="#30323B" stroke-width="1.8" fill="${color}"><path d="M0-11L3-3 10 0 3 3 0 12-3 3-11 0-3-3Z"/></g>`;},
 plant(id,x,y,s=1){return `<g id="${id}" transform="translate(${x} ${y}) scale(${s})" stroke="#6B7C69" stroke-width="2"><path d="M0 87L-35 8M0 87L0-11M0 87L29 13M0 87L36 55M0 87L-34 56" fill="none"/><ellipse cx="-35" cy="8" rx="15" ry="8" fill="#8ACB9C"/><ellipse cx="0" cy="-11" rx="15" ry="8" fill="#8ACB9C"/><ellipse cx="29" cy="13" rx="15" ry="8" fill="#8ACB9C"/><ellipse cx="36" cy="55" rx="15" ry="8" fill="#8ACB9C"/><ellipse cx="-34" cy="56" rx="15" ry="8" fill="#8ACB9C"/><path d="M-23 88L22 88 15 140-15 140Z" fill="#CF9F66" stroke="#30323B" stroke-width="3"/></g>`;}
};
