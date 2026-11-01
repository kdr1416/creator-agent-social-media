import wave
import numpy as np
import sys

sys.stdout.reconfigure(encoding="utf-8")

audio_path = "videos/VIDEO-33/inputs/source_audio.wav"
with wave.open(audio_path, "rb") as w:
    sr = w.getframerate()
    ch = w.getnchannels()
    width = w.getsampwidth()
    total_frames = w.getnframes()
    pcm = w.readframes(total_frames)

data = np.frombuffer(pcm, dtype=np.int16)

def find_best_cut(center_s, search_radius_s=0.25):
    """Find sample with minimum absolute amplitude and zero-crossing near center_s"""
    c_idx = int(center_s * sr)
    r_idx = int(search_radius_s * sr)
    st = max(0, c_idx - r_idx)
    en = min(total_frames, c_idx + r_idx)
    
    sub = data[st:en]
    abs_sub = np.abs(sub)
    
    # Prefer exact zero crossing with lowest absolute amplitude
    zero_crossings = np.where(np.diff(np.signbit(sub)))[0]
    if len(zero_crossings) > 0:
        # Among zero crossings, pick one with smallest amplitude
        zc_amps = abs_sub[zero_crossings]
        best_zc = zero_crossings[np.argmin(zc_amps)]
        best_idx = st + best_zc
    else:
        best_idx = st + np.argmin(abs_sub)
    
    best_s = best_idx / sr
    amp = data[best_idx]
    print(f"Target {center_s:6.3f}s -> Best cut: sample {best_idx:7d} ({best_s:6.3f}s), amp={amp}")
    return best_idx

# Candidate cut points based on silence intervals:
cuts = [
    6.25,   # Between S1 & S2 (Hook -> "Trước nhiều phụ huynh...")
    10.05,  # Between S2 & S3 ("...du học của con," -> "nhưng nếu con có kế hoạch...")
    14.35,  # Between S3 & S4 ("...trong nhiều năm." -> "Liệu toàn bộ tài sản...")
    18.40,  # Between S4 & S5 ("...ở Việt Nam." -> "Đó là lý do...")
    24.10,  # Between S5 & S6 ("...bất động sản tại Malta." -> "Không chỉ là sở hữu...")
    29.90,  # Between S6 & S7 ("...cho cả gia đình." -> "Khi có một tài sản tại Malta...")
    34.50,  # Between S7 & S8 ("...điểm kết nối với Châu Âu," -> "thuận tiện hơn cho những...")
    40.05,  # Between S8 & S9 ("...trong tương lai." -> "Đồng thời...")
    44.95,  # Between S9a & S9b ("...danh mục đầu tư" -> "thay vì phụ thuộc...")
    47.50,  # Between S9 & S10 ("...vào một quốc gia." -> "Chỉ với khoảng 3,8 tỷ đồng...")
    53.65,  # Between S10 & S11 ("...định cư cho 4 thế hệ." -> "Đây không chỉ là...")
    56.85,  # Between S11 & S12 ("...vào một bất động sản," -> "mà còn là quyết định...")
    60.38,  # Between S12a & S12b ("...tương lai của con cái" -> "và những cơ hội...")
    64.00,  # Between S12 & S13 ("...tại Châu Âu." -> "Khi con đã bước ra thế giới...")
    68.55,  # Between S13 & S14 ("...bước ra thế giới." -> "Bởi đôi khi...")
    72.50   # Between S14 & S15 ("...thêm một căn nhà," -> "mà là sở hữu thêm một lựa chọn...")
]

print(f"Total frames: {total_frames} ({total_frames/sr:.4f}s)")
cut_samples = [0]
for c in cuts:
    cut_samples.append(find_best_cut(c))
cut_samples.append(total_frames)

print(f"\nFinal cuts list ({len(cut_samples)} points, {len(cut_samples)-1} segments):")
for i in range(len(cut_samples)-1):
    s_st = cut_samples[i]
    s_en = cut_samples[i+1]
    dur = (s_en - s_st) / sr
    print(f"Seg {i+1:02d}: {s_st:7d} -> {s_en:7d} ({dur:5.3f}s)")
