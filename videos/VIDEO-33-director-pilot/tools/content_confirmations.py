"""Apply recorded owner confirmations without changing original audio/transcripts."""
import json, re
from prepare import ROOT, save

def apply():
    record=ROOT/'research/user-confirmations.json'
    if not record.exists():return
    confirmation=json.loads(record.read_text(encoding='utf-8'))
    old_takeaway='MPRP có thể bao gồm tới bốn thế hệ đủ điều kiện; âm thanh chi phí cần xử lý biên tập trước xuất bản.'
    takeaway='MPRP có thể bao gồm tới bốn thế hệ đủ điều kiện; con số khoảng 3,8 tỷ trong voice đã được chủ nội dung xác minh.'
    old_risk='HOLD_PUBLICATION: “3,8 tỷ” chưa được xác nhận bằng cấu phần phí hiện tại. Không hiện giá, không tự sửa voice. Nếu render cảnh này trước duyệt số liệu phải gắn trạng thái review-only trong hồ sơ ngoài video.'
    risk='OWNER_CONFIRMED: Chủ nội dung đã xác minh text “3.8 tỷ”. Giữ cách diễn đạt “khoảng 3,8 tỷ” trong voice. Không tự mở rộng thành giá mua nhà hoặc tổng phí trọn gói; bản thiết kế hiện tại vẫn tập trung gia phả và điều kiện MPRP.'
    def update(value):
        if isinstance(value,str):return value.replace(old_takeaway,takeaway).replace(old_risk,risk)
        if isinstance(value,list):return [update(x) for x in value]
        if isinstance(value,dict):return {k:update(v) for k,v in value.items()}
        return value
    for name in ['STORYBOARD.json','scenes/S10/packet.json']:
        data=update(json.loads((ROOT/name).read_text(encoding='utf-8')))
        scene=next(s for s in data['scenes'] if s['scene_id']=='S10') if name=='STORYBOARD.json' else data
        scene['price_confirmation']=confirmation
        save(name,data)
    for name in ['STORYBOARD.md','STORYBOARD.html','scenes/S10/PACKET.md']:
        save(name,update((ROOT/name).read_text(encoding='utf-8')))
    status=json.loads((ROOT/'production_status.json').read_text(encoding='utf-8'))
    status['publication_hold']=[]
    status['content_confirmations']=[confirmation]
    status['user_approved']=False
    status['approval_scope']='Price text only confirmed; storyboard/pilot approval and full-film production remain pending.'
    save('production_status.json',status)
    replacements={
        'RESEARCH.md':[(r'- Không có tỷ giá, báo giá.*?(?=\n)', '- Cập nhật từ chủ nội dung: người dùng xác minh text “3.8 tỷ” trong chat. Ghi nhận khoảng 3,8 tỷ là số liệu do chủ nội dung xác nhận cho dự án; điểm chờ xác minh này đã được gỡ. Chưa có bảng tính/tỷ giá/phạm vi phí bổ sung trong hồ sơ, nên không suy rộng thành giá mua nhà hay tổng phí trọn gói. Các kết quả tra cứu nguồn chính thức ở trên được giữ để phân biệt nguồn xác nhận.')],
        'REVIEW_GUIDE.md':[(r'S10 có claim “3,8 tỷ”.*?(?=\n\n)', 'S10: chủ nội dung đã xác minh text “3.8 tỷ” trong chat. Điểm chờ về số tiền đã được gỡ; giữ voice gốc với từ “khoảng”. Đây là xác nhận của chủ nội dung cho dự án; không tự suy rộng phạm vi chi phí. Việc duyệt storyboard/pilot vẫn đang chờ.')],
        'ANTIGRAVITY_PROMPT.md':[(r'Đặc biệt S10:.*?(?=\n\n)', 'S10: chủ nội dung đã xác minh text “3.8 tỷ”; gỡ điểm chờ xác minh về con số này và giữ voice gốc “khoảng 3,8 tỷ”. Xem research/user-confirmations.json để biết nguồn và phạm vi xác nhận. Không tự mở rộng thành giá mua nhà/tổng phí trọn gói hoặc đổi thiết kế sang hero metric. Các điều kiện MPRP về gia đình và quyền cư trú/lao động vẫn giữ theo packet. Xác nhận số liệu không đồng nghĩa đã duyệt storyboard/pilot hoặc cho phép dựng full.')],
        'START_HERE.md':[(r'S10 có vấn đề số tiền.*?(?=\n)', 'Người dùng đã xác minh text “3.8 tỷ” cho S10; điểm chờ số tiền đã được gỡ. Storyboard/pilot vẫn chờ duyệt.')],
        'REVIEW.html':[(r'<p class="note">.*?</p>', '<p class="note">Cập nhật: chủ nội dung đã xác minh text “3.8 tỷ” cho S10. Giữ voice gốc; storyboard và pilot vẫn đang chờ duyệt.</p>')],
    }
    for name,pairs in replacements.items():
        text=(ROOT/name).read_text(encoding='utf-8')
        for pattern,replacement in pairs:text=re.sub(pattern,lambda _:replacement,text,flags=re.S)
        save(name,text)
    brief=ROOT/'DIRECTOR_BRIEF.md'
    text=brief.read_text(encoding='utf-8')
    if '## Xác nhận nội dung từ người dùng' not in text:
        text+='\n## Xác nhận nội dung từ người dùng\n\nNgười dùng đã xác minh text “3.8 tỷ” trong chat. Gỡ điểm chờ xác minh con số ở S10; giữ voice gốc “khoảng 3,8 tỷ”. Xác nhận này chỉ áp dụng số liệu, chưa là duyệt storyboard/pilot hoặc lệnh dựng full. Nguồn xác nhận lưu tại research/user-confirmations.json.\n'
    save('DIRECTOR_BRIEF.md',text)

if __name__=='__main__':apply()
