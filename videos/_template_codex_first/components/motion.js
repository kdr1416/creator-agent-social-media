// Optional GSAP utility. No default ease, style, pose, duration or automatic clock.
// Include as an ES module in a compatible scene, or adapt to the chosen renderer.
export function addMotion(timeline, target, from, to, at) {
  if (!timeline || typeof timeline.fromTo !== "function") throw new Error("Expected a seekable timeline");
  if (typeof to.duration !== "number" || !to.ease) throw new Error("Choose duration and ease per motion");
  return timeline.fromTo(target, from, to, at);
}
