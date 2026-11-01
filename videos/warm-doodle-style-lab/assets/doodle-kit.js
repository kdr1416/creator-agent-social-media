/* Original reusable SVG character kit. All motion belongs to the owning GSAP timeline. */
window.Doodle = {
  student(id, x, y, s = 1, color = '#78AEB0') {
    return `<g id="${id}" transform="translate(${x} ${y}) scale(${s})" stroke="#493D36" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round">
      <ellipse cx="75" cy="233" rx="65" ry="10" fill="#CBB9A2" stroke="none" opacity=".3"/>
      <g id="${id}-far-arm"><path d="M42 112 Q13 132 9 153" fill="none" stroke="${color}" stroke-width="20"/><path d="M9 153 Q4 168 17 176" fill="none" stroke="#EAB795" stroke-width="13"/></g>
      <path d="M112 100 Q139 95 138 139 L134 171 109 174Z" fill="#E5B858"/>
      <g id="${id}-left-leg"><path d="M59 173 Q48 201 43 223" fill="none" stroke="#747E96" stroke-width="22"/><path d="M43 224 L23 228 Q19 239 49 237 L58 231" fill="#F9F4E8"/></g>
      <g id="${id}-right-leg"><path d="M91 174 Q97 204 105 222" fill="none" stroke="#747E96" stroke-width="22"/><path d="M105 222 L120 229 Q130 240 98 238 L91 232" fill="#F9F4E8"/></g>
      <g id="${id}-body"><path d="M42 104 Q72 90 105 105 L115 178 Q73 189 35 178Z" fill="${color}"/><path d="M66 111 L74 131 84 110 M68 131 L67 148 M84 132 L86 147" fill="none" stroke="#F7F0DB" stroke-width="3"/><path d="M52 159 Q75 170 98 158" fill="none" stroke="#4F868B" stroke-width="2"/></g>
      <g id="${id}-head"><path d="M31 58 Q23 4 75 5 Q129 3 120 65 L113 97 101 84 43 90Z" fill="#6B4C3B"/><ellipse cx="76" cy="62" rx="40" ry="43" fill="#F0C5A5"/><path d="M36 50 Q32 11 74 15 Q111 13 117 45 Q92 43 82 29 Q63 49 36 50Z" fill="#6B4C3B"/><path d="M58 57 L62 56 M91 56 L96 57" fill="none"/><g id="${id}-eyes" fill="#493D36" stroke="none"><ellipse cx="61" cy="63" rx="3.5" ry="4.5"/><ellipse cx="94" cy="63" rx="3.5" ry="4.5"/></g><ellipse cx="48" cy="76" rx="8" ry="4" fill="#E99C8A" stroke="none" opacity=".7"/><ellipse cx="103" cy="76" rx="8" ry="4" fill="#E99C8A" stroke="none" opacity=".7"/><path d="M69 79 Q78 88 87 78" fill="none" stroke-width="2.5"/><path d="M112 28 L128 24 128 37 114 34Z" fill="#D16F4D" stroke-width="2"/></g>
      <g id="${id}-near-arm"><path d="M105 114 Q123 132 127 145" fill="none" stroke="${color}" stroke-width="20"/><path d="M127 145 Q137 149 144 137" fill="none" stroke="#EAB795" stroke-width="13"/><ellipse id="${id}-hand" cx="144" cy="137" rx="8" ry="7" fill="#F0C5A5" stroke-width="2"/></g>
    </g>`;
  },
  envelope(id, x, y, s = 1, color = '#FDF9EF') {
    return `<g id="${id}" transform="translate(${x} ${y}) scale(${s})" stroke="#493D36" stroke-width="3" stroke-linejoin="round"><path d="M-65-43L65-45 69 42-64 45Z" fill="${color}"/><path d="M-63-41L0 6 65-43M-63 43L-14 1M67 41L16 0" fill="none"/><circle cx="38" cy="20" r="12" fill="#94B598"/><path d="M31 20L36 25 45 14" fill="none" stroke="#365E4D" stroke-width="3"/></g>`;
  },
  sparkle(id, x, y, s = 1) {
    return `<g id="${id}" transform="translate(${x} ${y}) scale(${s})" fill="none" stroke="#B9763B" stroke-width="3" stroke-linecap="round"><path d="M0-13Q0 0 12 0Q0 0 0 13Q0 0-12 0Q0 0 0-13Z"/></g>`;
  }
};
