import React from 'react';
import {
  AbsoluteFill,
  Audio,
  Img,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';

export const Scene2: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // 1. Camera Zoom nhẹ (1.0x -> 1.05x)
  const bgScale = interpolate(frame, [0, 177], [1.0, 1.05], {
    extrapolateRight: 'clamp',
  });

  // 2. Top Banner Entrance (Frame 0 -> 15)
  const topBannerProgress = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.5, stiffness: 120 },
  });
  const topBannerY = interpolate(topBannerProgress, [0, 1], [-80, 55]);
  const topBannerOpacity = interpolate(topBannerProgress, [0, 1], [0, 1]);

  // 3. Card 1 Spring Physics: "THAY ĐỔI TÀI CHÍNH" (Frame 50 -> 115)
  const card1Spring = spring({
    frame: frame - 50,
    fps,
    config: { damping: 11, mass: 0.55, stiffness: 130 },
  });
  const card1Out = interpolate(frame, [105, 115], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const showCard1 = frame >= 50 && frame < 118;

  // 4. Card 2 Spring Physics: "TỪ NGÀY 01 THÁNG 09" (Frame 110 -> end)
  const card2Spring = spring({
    frame: frame - 110,
    fps,
    config: { damping: 11, mass: 0.55, stiffness: 130 },
  });
  const showCard2 = frame >= 110;

  // Vệt Highlight trượt mượt mà (Frame 118 -> 134)
  const highlightWidth = interpolate(frame, [118, 134], [0, 100], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#FFFFFF',
        overflow: 'hidden',
        fontFamily: "'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif",
      }}
    >
      <style>
        {`
          @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&display=swap');
        `}
      </style>

      {/* Voice Audio Track */}
      <Audio src={staticFile('audio.wav')} />

      {/* 2D Background với zoom nhẹ */}
      <AbsoluteFill style={{ transform: `scale(${bgScale})`, transformOrigin: 'center 40%' }}>
        <Img
          src={staticFile('bg.jpg')}
          style={{ width: '100%', height: '100%', objectFit: 'cover' }}
        />
      </AbsoluteFill>

      {/* ── TOP BADGE: DU HỌC CANADA ── */}
      <div
        style={{
          position: 'absolute',
          top: topBannerY,
          left: 0,
          right: 0,
          display: 'flex',
          justifyContent: 'center',
          opacity: topBannerOpacity,
          zIndex: 10,
        }}
      >
        <div
          style={{
            background: 'linear-gradient(135deg, #FF6B2B 0%, #FA5511 100%)',
            color: '#FFFFFF',
            padding: '10px 32px',
            borderRadius: 999,
            fontWeight: 900,
            fontSize: 22,
            letterSpacing: 2,
            border: '2px solid rgba(255, 255, 255, 0.95)',
            boxShadow: '0px 6px 0px #C73B00, 0px 14px 28px rgba(255, 107, 43, 0.35)',
            textTransform: 'uppercase',
            display: 'flex',
            alignItems: 'center',
            gap: 8,
          }}
        >
          <span style={{ fontSize: 18 }}>🍁</span>
          <span>DU HỌC CANADA</span>
        </div>
      </div>

      {/* ── POPUP CARD 1: THAY ĐỔI TÀI CHÍNH QUAN TRỌNG (Gọn gàng, không text thừa) ── */}
      {showCard1 && (
        <div
          style={{
            position: 'absolute',
            top: 210,
            left: 0,
            right: 0,
            display: 'flex',
            justifyContent: 'center',
            transform: `scale(${card1Spring})`,
            opacity: card1Out,
            zIndex: 20,
          }}
        >
          <div
            style={{
              backgroundColor: '#FFFFFF',
              border: '3px solid #0F172A',
              borderRadius: 22,
              padding: '24px 40px',
              width: 590,
              boxShadow: '0px 8px 0px #FF6B2B, 0px 20px 38px rgba(0, 0, 0, 0.09)',
              textAlign: 'center',
            }}
          >
            {/* Tag IRCC ngắn gọn */}
            <div
              style={{
                display: 'inline-block',
                backgroundColor: '#FFF4EE',
                color: '#FF6B2B',
                border: '1.5px solid #FFD8C4',
                padding: '4px 16px',
                borderRadius: 999,
                fontSize: 16,
                fontWeight: 900,
                letterSpacing: 1.5,
                textTransform: 'uppercase',
                marginBottom: 12,
              }}
            >
              THÔNG BÁO TỪ IRCC
            </div>

            {/* Dòng chữ chính cực đậm, dứt khoát */}
            <div
              style={{
                color: '#0F172A',
                fontSize: 38,
                fontWeight: 900,
                letterSpacing: -0.5,
                lineHeight: 1.25,
              }}
            >
              THAY ĐỔI{' '}
              <span style={{ color: '#FF6B2B' }}>TÀI CHÍNH</span>
              <br />QUAN TRỌNG
            </div>
          </div>
        </div>
      )}

      {/* ── POPUP CARD 2: TỪ NGÀY 01 THÁNG 09 (Tập trung 100% vào từ khóa chính) ── */}
      {showCard2 && (
        <div
          style={{
            position: 'absolute',
            top: 220,
            left: 0,
            right: 0,
            display: 'flex',
            justifyContent: 'center',
            transform: `scale(${card2Spring})`,
            zIndex: 20,
          }}
        >
          <div
            style={{
              backgroundColor: '#FFFFFF',
              border: '3.5px solid #0F172A',
              borderRadius: 24,
              padding: '26px 42px',
              boxShadow: '0px 10px 0px #FF6B2B, 0px 24px 44px rgba(255, 107, 43, 0.16)',
              textAlign: 'center',
              display: 'inline-flex',
              flexDirection: 'column',
              alignItems: 'center',
            }}
          >
            {/* Chỉ tập trung dòng Text chính: Font to, cực đậm (Weight 900), nổi bật */}
            <div
              style={{
                position: 'relative',
                display: 'inline-flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
            >
              {/* Vệt Highlight màu vàng pastel dẹt bo góc ôm khít chân chữ */}
              <div
                style={{
                  position: 'absolute',
                  left: -8,
                  bottom: 4,
                  height: '44%',
                  width: `${highlightWidth}%`,
                  maxWidth: 'calc(100% + 16px)',
                  background: 'linear-gradient(90deg, #FDE047 0%, #FACC15 100%)',
                  borderRadius: 6,
                  zIndex: 0,
                  opacity: 0.9,
                }}
              />

              <span
                style={{
                  position: 'relative',
                  zIndex: 1,
                  color: '#0F172A',
                  fontSize: 44,
                  fontWeight: 900,
                  letterSpacing: -0.5,
                  whiteSpace: 'nowrap',
                }}
              >
                TỪ NGÀY{' '}
                <span style={{ color: '#FF6B2B' }}>
                  01 THÁNG 09
                </span>
              </span>
            </div>
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};
