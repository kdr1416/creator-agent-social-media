"""Prepare the immutable audio, direction and scene packets for VIDEO-33.

Production utility kept with the handoff. Never writes into either input project.
"""
from pathlib import Path
import hashlib, json, shutil, wave, csv, math

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
SOURCE = REPO / 'videos/VIDEO-33'
REFERENCE = REPO / 'videos/tran-minh-nhat-director-handoff'

def save(name, value):
    path = ROOT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(value, (dict, list)):
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    else:
        path.write_text(value, encoding='utf-8')

def digest(path):
    return hashlib.file_digest(path.open('rb'), 'sha256').hexdigest()

def manifest():
    return {str(p.relative_to(REPO)): digest(p) for base in (SOURCE, REFERENCE)
            for p in sorted(base.rglob('*')) if p.is_file()}

# Every design is new. Source slice ranges remain immutable.
# fields: source ids, title, takeaway, composition, open, transformation, end,
# performance, visual family/verb, visible text, assets/layers, transition, risks.
DESIGNS = [
([1], 'Cuốn sách thành điểm tựa',
 'Việc học mở ra một kế hoạch dài hạn của gia đình, không chỉ một kỳ học.',
 'Cuốn sách xanh chiếm x=90–560, y=550–890; mascot ở phải, chân tại y=1020. Một mái nhà giấy nhỏ ở lớp trên, không phải tài sản đã được cấp quyền.',
 'Cận cuốn sách đang hé; mascot đưa tay tới mép bìa, mắt theo trang sách.',
 'Bìa mở và các trang gấp bung thành mặt đỡ; mái nhà giấy và nhóm gia đình hiện lên trên mặt đỡ sau cụm “mà còn”. Tay nắm mép sách trước khi trang đổi hình.',
 'Một cuốn sách vẫn nhận ra được làm nền cho nhà và gia đình; mascot ngước nhìn, không có dấu duyệt hay biểu tượng visa.',
 'Mở bìa → giữ mép trang → ngước nhìn mái nhà. Giữ mũ tím, túi xanh và thân cam bo góc.',
 'physical transformation', 'mở / nâng đỡ', ['HỌC TẬP', 'ĐIỂM TỰA DÀI LÂU'],
 ['book-back','book-pages','book-cover','folded-support','paper-house','family-silhouettes','mascot-body','mascot-far-arm','mascot-near-arm','mascot-eyes','mascot-cap','mascot-bag'],
 'Cắt theo ý sang cận vật liệu học phí; không kéo cùng căn nhà qua cảnh 02.',
 'Không biến sách thành chứng nhận cư trú; mái nhà là ẩn dụ điểm tựa.'),
([2], 'Chi phí có trọng lượng',
 'Gia đình đã dành nguồn lực đáng kể cho hành trình học tập.',
 'Cận bàn giấy đào: thước đo nằm chéo, chồng xu lớn và cuốn sổ chi phí mở. Mọi chi tiết ở y=350–1030, không dựng dashboard.',
 'Một chồng xu nằm trên góc trang sổ; chưa có con số.',
 'Các xu còn lại lăn vào cùng chồng làm giấy hơi võng; thước trượt qua chiều cao chồng xu theo cụm “hàng tỷ đồng”.',
 'Chồng xu cao nhưng không hiện giá của một trường/cá nhân cụ thể.',
 'Không mascot; trọng lượng và mép giấy là chủ thể.',
 'macro physical prop', 'tích / cân nhắc', ['CHI PHÍ DU HỌC'],
 ['ledger-left','ledger-right','coin-stack','rolling-coins','measuring-rule','paper-shadow'],
 'Mép sổ mở ra nhường màn hình cho kế hoạch dài hạn ở cảnh 03; cắt thẳng, không morph mọi đồ vật.',
 'Không tự thêm số tiền cụ thể hoặc khẳng định thống kê về số lượng phụ huynh.'),
([3], 'Một hành trình nhiều năm',
 'Học tập và sự nghiệp là một kế hoạch nối tiếp có khả năng thay đổi.',
 'Dải bản vẽ giấy uốn S qua khung, x=90–620/y=340–1010; một góc bàn học lớn ở gần, bàn làm việc ở xa. Không xếp bullet dọc.',
 'Mascot đặt cuốn vở lên đầu dải giấy còn gấp.',
 'Mascot mở nếp gấp; bàn học dựng lên trước, dụng cụ thực hành mở tiếp ở nửa sau, nhánh tương lai chỉ bằng nét đứt.',
 'Dải thời gian còn một đầu mở; không nhận bằng rồi lập tức có việc.',
 'Kéo nếp giấy, chuyển ánh nhìn từ vở tới bàn thực hành; chỉ một bước có mục đích.',
 'fold-out environment', 'trải / dự tính', ['NHIỀU NĂM'],
 ['folded-road','study-desk','practice-desk','open-ended-path','mascot-rig'],
 'Cắt từ đầu đường chưa định sang câu hỏi tài sản ở cảnh 04.',
 'Không gán mốc năm, nghề hay việc làm chắc chắn.'),
([4], 'Tập trung vào một nơi?',
 'Câu hỏi về mức độ tập trung tài sản, không phải yêu cầu bán tài sản Việt Nam.',
 'Một chiếc khay giấy thật lớn trên nền lilac; mọi nhà/xu nằm cùng một phía, không có khay quốc gia đối lập màu đỏ/xanh.',
 'Khay nằm gần giữa, toàn bộ khối tài sản tụ về một góc.',
 'Khay hơi nghiêng do tải lệch; dấu hỏi xuất hiện trong khoảng trống vừa mở. Không có đồ vật rơi hoặc cảnh khủng hoảng.',
 'Khay vẫn giữ mọi tài sản, dấu hỏi giữ lại câu cân nhắc.',
 'Không mascot để giữ câu hỏi đơn giản và tránh diễn cảm sợ hãi.',
 'concentration metaphor', 'nghiêng / đặt câu hỏi', ['MỘT NƠI?','Việt Nam'],
 ['paper-tray','house-token','coin-token','question-mark','location-label'],
 'Cắt sang mặt giấy mới mở ở Malta. Không cho xu tự bay khỏi Việt Nam.',
 'Không quy kết Việt Nam rủi ro hơn quốc gia khác; đây là câu hỏi biên tập.'),
([5], 'Mở thêm một địa điểm',
 'Malta là một địa điểm được đưa vào cân nhắc đa dạng hóa, không thay thế toàn bộ tài sản cũ.',
 'Một tờ bản đồ du lịch gấp trên nền kem. Ảnh thật Valletta chiếm x=100–620/y=350–720; phần dưới là mặt giấy với nhà nhỏ. Mascot đứng dưới phải, chạm góc gấp. Vật thể Việt Nam nhỏ ở mép trái vẫn còn.',
 'Tờ giấy gấp che gần hết ảnh, lộ chút bầu trời và mép ảnh; mascot chuẩn bị kéo mép.',
 'Tay kéo mép giấy, giấy xoay mở theo nếp làm lộ ảnh Valletta; ngôi nhà giấy dựng ở chân ảnh khi lời đọc tới bất động sản. Nhãn MALTA hiện cùng địa danh, không dán lên công trình cụ thể.',
 'Ảnh thật + giấy + nhà biểu tượng cùng một bề mặt, mascot giữ góc trang mở. Không có giá/lợi nhuận.',
 'Với tay → chạm giấy → giữ khi tờ giấy mở → nhìn ảnh và ngôi nhà.',
 'geographic mixed-media collage', 'mở / bổ sung', ['MALTA'],
 ['valletta-photo','photo-paper-edge','fold-left','fold-right','paper-crease','property-symbol','vietnam-keepsake','mascot-body','mascot-near-arm','mascot-eyes','mascot-cap','mascot-bag'],
 'Màu đá sáng nối sang không gian gia đình cảnh 06 bằng cắt ý; không dùng cùng căn nhà làm template.',
 'Ảnh Valletta chỉ định vị địa lý; không phải dự án bán hay căn nhà của khách hàng.'),
([6], 'Chỗ cho cả gia đình',
 'Một kế hoạch dài hạn được cân nhắc ở cấp gia đình.',
 'Bàn ăn hình oval lớn, nhìn nghiêng nhẹ trên nền peach; mascot và hai thành viên ở các phía. Mặt bàn sáng, chân bàn không đen nặng.',
 'Bàn có một phần lá gấp, các thành viên nhìn về chỗ còn thiếu.',
 'Mascot kéo lá bàn mở rộng; một chỗ ngồi mới vừa đủ hiện ra, mọi người xích lại chia sẻ bản kế hoạch không chữ.',
 'Một bàn chung với các chỗ ngồi, cảm giác cùng chuẩn bị thay vì tài sản tự tăng giá.',
 'Kéo bàn và kéo ghế cho người thân, không chỉ đứng cạnh nhà.',
 'family situation', 'mở rộng / cùng bàn', ['CẢ GIA ĐÌNH'],
 ['table-top','table-leaf','chairs','family-puppets','blank-plan','mascot-rig'],
 'Cắt cận mối kết nối ở cảnh 07, không dùng thêm thao tác mở đồ vật ngay đầu cảnh.',
 'Gia đình tượng trưng, không mô tả quyền lợi pháp lý tự phát sinh từ mua nhà.'),
([7], 'Giữ một điểm kết nối',
 'Gia đình có thể hoạch định kết nối với nơi con đang học.',
 'Bàn làm việc lilac, laptop thật về hình học ở x=150–560/y=440–790; dây nối uốn nhẹ xuống mascot tại y=920.',
 'Mascot cầm đầu dây, màn hình có khung ảnh gia đình chưa nối.',
 'Cắm đầu dây → màn hình sáng với người thân giơ tay chào; mascot nhìn vào mắt người trong màn hình, một nét nối sáng ngắn xuất hiện theo tiếp xúc.',
 'Hai phía cuộc gọi nhìn nhau. Không hiện giao diện thương hiệu, giấy phép hoặc “thẻ xanh EU”.',
 'Cắm dây, chào lại và theo dõi người thân trên màn hình.',
 'device interaction', 'cắm / kết nối', ['KẾT NỐI'],
 ['laptop-shell','screen-family','cable','plug','desk','mascot-rig'],
 'Lời chào dẫn bằng cắt cảnh sang cuộc gặp ngoài đời, không match cùng cánh tay.',
 'MPRP không tự cấp quyền cư trú/làm việc toàn EU; không mã hóa quyền đó trong UI.'),
([8], 'Đến gần những kế hoạch',
 'Thăm con và các dự định tương lai là những khả năng phải chuẩn bị riêng.',
 'Ga đến minh họa với vali phía trước, mascot đón phụ huynh ở y=800–1030; phía sau một vở học, chìa khóa và cặp làm việc ở các lớp sâu khác nhau, không ba card.',
 'Mascot nhìn sang vali ở mép khung, phụ huynh vừa đến.',
 'Vali dừng → hai người chạm tay chào; ánh nhìn chuyển qua các đạo cụ gợi học/sống/việc làm, chỉ một đạo cụ được nhấn ở mỗi nhịp.',
 'Cuộc gặp là hiện thực trong ẩn dụ; ba kế hoạch còn ở dạng nét phác mở, không dấu duyệt.',
 'Đón người thân và nhận tay kéo vali, tương tác có tiếp xúc.',
 'arrival / layered future', 'đón / dự định', ['KẾ HOẠCH TƯƠNG LAI'],
 ['arrival-floor','luggage','parent-puppet','study-prop','living-prop','work-prop','mascot-rig'],
 'Cắt sang cơ chế phân bổ tài sản cảnh 09 để đổi chủ thể và nhịp hình.',
 'Hồ sơ học tập, cư trú và lao động có điều kiện riêng; không diễn thành một thẻ mở mọi quyền.'),
([9,10], 'Phân bổ, không dồn một chỗ',
 'Đa dạng hóa là phân bổ mức tiếp xúc, không phải bảo đảm lợi nhuận hoặc xóa rủi ro.',
 'Bàn cơ khí mở trên nền lilac: một cụm tài sản chung tách ra ba vùng thị trường không đóng khung; ba bệ tròn vật lý lệch cao, liên hệ qua nhánh cong. Không dùng bản đồ giả.',
 'Ba đồng tài sản xếp chung tại một bệ, hai bệ còn trống.',
 'Các đồng trượt theo rãnh cong tới các bệ khác; camera giữ toàn cơ chế. Mỗi bệ vẫn có một dấu dao động ngắn riêng, không xuất hiện khiên/chốt bảo hiểm.',
 'Ba phần tài sản ở ba vùng, nét dao động vẫn còn. Nhãn một nơi biến mất trước nhãn nhiều thị trường xuất hiện.',
 'Không mascot: chủ thể là quan hệ phân bổ; tránh bàn tay thần kỳ bảo vệ mọi bệ.',
 'open allocation mechanism', 'chia / phân bổ', ['MỘT NƠI','NHIỀU THỊ TRƯỜNG'],
 ['allocation-track','market-a-platform','market-b-platform','market-c-platform','token-a','token-b','token-c','local-fluctuation-marks','caption-a','caption-b'],
 'Cắt từ ba phân bổ sang nhóm gia đình ở cảnh 10. Không biến ba thị trường thành bốn thế hệ.',
 'Không hiện %/đồ thị hiệu suất; cả ba vẫn có rủi ro. Phân bổ là ẩn dụ, không danh mục được khuyến nghị.'),
([11], 'Gia đình nhiều thế hệ — có điều kiện',
 'MPRP có thể bao gồm tới bốn thế hệ đủ điều kiện; âm thanh chi phí cần xử lý biên tập trước xuất bản.',
 'Một trang album gia đình thực sự, mở chéo trên nền cream, bốn thế hệ đặt theo quan hệ gia phả chứ không bốn trẻ kế tiếp; mascot đỡ góc album.',
 'Album hé với nhóm đương đơn và vợ/chồng; không hiện con số tiền.',
 'Các nhánh gia đình mở lần lượt tới con, cha mẹ, ông bà. Tới cụm “4 thế hệ” mới đủ bốn cấp; ghi ngắn “Theo điều kiện MPRP”, không đóng dấu thông qua.',
 'Bốn cấp quan hệ nối đúng, tất cả nằm trong một hồ sơ có điều kiện, không hộ chiếu quốc tịch.',
 'Mascot giữ album và hướng ánh nhìn theo nhánh, không trao thẻ cư trú.',
 'family album / genealogy', 'mở quan hệ', ['TỚI 4 THẾ HỆ','Theo điều kiện MPRP'],
 ['album-spread','applicant-couple','children','parents','grandparents','kinship-connectors','mascot-rig'],
 'Lật sang mặt sau album như vật liệu giấy để cắt sang chuẩn bị cho con.',
 'HOLD_PUBLICATION: “3,8 tỷ” chưa được xác nhận bằng cấu phần phí hiện tại. Không hiện giá, không tự sửa voice. Nếu render cảnh này trước duyệt số liệu phải gắn trạng thái review-only trong hồ sơ ngoài video.'),
([12,13], 'Chuẩn bị thay vì chỉ sở hữu',
 'Trọng tâm chuyển từ một bất động sản sang sự chuẩn bị cho tương lai của con.',
 'Cận chìa khóa nhà đặt trên bàn; camera nới ra lộ ba lô mở, vở và dụng cụ học. Không thêm hộ chiếu hay giấy trúng tuyển.',
 'Chìa khóa là tiêu điểm duy nhất, mascot ngoài mép hình.',
 'Mascot đặt chìa khóa xuống rồi sắp vở vào ba lô; trọng tâm ánh sáng chuyển từ chìa sang những thứ đã chuẩn bị.',
 'Ba lô đã sẵn sàng nhưng chưa tự bước tới kết quả nghề nghiệp.',
 'Sắp xếp đồ học đúng với ý chuẩn bị; không bắt chìa khóa biến thành bằng cấp.',
 'close-to-wide preparation', 'đặt / chuẩn bị', ['CHUẨN BỊ CHO TƯƠNG LAI'],
 ['house-key','table','backpack-open','notebook','study-tools','mascot-rig'],
 'Cắt từ vật liệu vở sang môi trường cơ hội cảnh 12; không kéo cùng ba lô qua từng bước chân.',
 'Audio “con gái/con cái” chưa giải quyết bằng nghe độc lập; text trung tính không chốt giới tính.'),
([14], 'Cơ hội có thể nắm bắt',
 'Thế hệ sau có thêm khả năng lựa chọn, vẫn cần nỗ lực và điều kiện.',
 'Một xưởng học nhỏ trên nền lilac, cánh tay mascot đưa tới dụng cụ thực hành treo ở nhiều cao độ; không bảng thống kê việc làm.',
 'Dụng cụ ở ngoài tầm tay, mascot nhìn thử khoảng cách.',
 'Mascot kéo ghế nhỏ đến gần rồi với lấy dụng cụ, bắt đầu thao tác ở bàn thực hành; nhấn hành động chủ động nắm cơ hội.',
 'Đã bắt đầu học/làm thử, không huy chương hoặc hợp đồng.',
 'Đưa ghế, với tay, cầm dụng cụ và tập thử.',
 'learning workshop', 'với / thử', ['CƠ HỘI'],
 ['workshop-table','stool','tool-hooks','chosen-tool','mascot-rig'],
 'Cắt sang quy mô thế giới cảnh 13; thay tỷ lệ để không lặp cảnh nhân vật đi đường.',
 'Không thêm ngành cụ thể hoặc lời hứa tuyển dụng.'),
([15], 'Cùng mở tầm nhìn',
 'Việc con học ở nước ngoài gợi gia đình cân nhắc phạm vi hoạch định tài sản rộng hơn.',
 'Địa cầu giấy lớn ở y=440–940; một đường học tập và một dấu tài sản bắt đầu từ hai vị trí lớp trước, không chạy theo cùng quỹ đạo.',
 'Mascot kéo quai vali cạnh địa cầu chỉ mở một nửa.',
 'Mascot xoay địa cầu để lộ phần còn lại; dấu học tập đi trước, dấu tài sản mở một hướng khác sau cụm “cũng có thể”.',
 'Hai phạm vi cùng mở nhưng độc lập, không chuyển toàn bộ tiền sang Malta.',
 'Xoay địa cầu và theo dõi hai hướng kế hoạch.',
 'paper globe / scale change', 'xoay / mở phạm vi', ['MỞ TẦM NHÌN'],
 ['globe-hemispheres','meridians','study-trace','asset-trace','luggage','mascot-rig'],
 'Dừng chuyển động lớn, cắt cận bàn tay chọn ở cảnh cuối để hạ nhịp.',
 'Địa cầu minh họa cần đường bờ có nguồn hoặc đơn giản không chi tiết; không vẽ biên giới sai.'),
([16,17], 'Có thêm một lựa chọn',
 'Giá trị kết luận là khả năng lựa chọn cho tương lai; không thêm lời kêu gọi mua.',
 'Nhà giấy ở trái, bên phải một bản kế hoạch gấp có hai lối mở. Mascot ở giữa cầm chìa khóa; bố cục rộng thay vì nhà đứng giữa.',
 'Mascot nhìn chìa khóa trên lòng bàn tay, căn nhà yên ở cạnh.',
 'Mascot xoay lòng bàn tay đặt chìa xuống; tay kia mở một nếp bản kế hoạch để lộ nhánh lựa chọn còn trống. Không bước hẳn vào một cánh cửa.',
 'Nhà vẫn có, thêm một hướng chưa chốt; text ngắn “THÊM MỘT LỰA CHỌN” giữ đến sample cuối, không CTA/QR/logo mới.',
 'Đặt chìa và tự mở kế hoạch; ánh nhìn dừng ở nhánh mới, phản ứng nhẹ.',
 'quiet choice / plan prop', 'đặt / chọn', ['THÊM MỘT LỰA CHỌN'],
 ['house-side','open-hand','key','folded-choice-plan','branch-a','branch-b','mascot-rig'],
 'Giữ kết quả tới 75.16s, không fade đen cắt đuôi voice.',
 'Không chọn thay khán giả, không guarantee tương lai, không tự thêm CTA.')
]

def main():
    if (ROOT/'STORYBOARD.json').exists():
        raise RuntimeError('Plan already exists; edit the authored files deliberately, do not reset them.')
    for d in ['inputs/audio','scratch','planning','scenes','pilots','assets/fonts','assets/runtime','qa','research','build']:
        (ROOT/d).mkdir(parents=True, exist_ok=True)
    save('qa/source-before.json',manifest())
    handoff=json.loads((SOURCE/'audio_handoff.json').read_text(encoding='utf-8-sig'))
    with wave.open(str(SOURCE/'inputs/source_audio.wav'),'rb') as w:
        pcm=w.readframes(w.getnframes()); rate=w.getframerate(); frames=w.getnframes()
    assert frames==1803840 and rate==24000
    assert hashlib.sha256(pcm).hexdigest()==handoff['source_pcm_sha256']
    slices=[]
    for seg in handoff['segments']:
        with wave.open(str(SOURCE/seg['audio_slice']),'rb') as w:
            data=w.readframes(w.getnframes())
        assert len(data)//2==seg['end_sample']-seg['start_sample']
        slices.append(data)
    assert b''.join(slices)==pcm
    save('qa/audio-source-verification.json',{'sample_rate':rate,'frames':frames,'duration':frames/rate,'contiguous':True,'pcm_reassembly_bit_exact':True,'pcm_sha256':hashlib.sha256(pcm).hexdigest(),'file_sha256':digest(SOURCE/'inputs/source_audio.wav'),'zero_crossings_independently_verified':False})
    # Routing is written before the detailed storyboard or asset production.
    scenes=[]; routes=[]; picture=[]; prior=0
    for n,des in enumerate(DESIGNS,1):
        ids,title,meaning,layout,opening,action,final,character,family,verb,text,layers,transition,risk=des
        segs=[handoff['segments'][i-1] for i in ids]
        start_sample=segs[0]['start_sample']; end_sample=segs[-1]['end_sample']
        start=start_sample/rate; end=end_sample/rate; duration=end-start
        sid=f'S{n:02d}'; present=n not in (2,4,9)
        reason=f'{title}: hành động chủ đạo là {verb} các lớp minh họa/giấy. HYBRID đã xét: diễn viên thật không giúp đọc quan hệ {family}, và sẽ thay mascot đã duyệt; cần giữ tiếp xúc và thay đổi lớp đúng nhịp. HF_ONLY vì cấu trúc hình mang nghĩa, không vì có chữ.'
        route={'scene_number':n,'scene_id':sid,'start':start,'end':end,'start_sample':start_sample,'end_sample':end_sample,'source_segments':ids,'raw_text':' '.join(s['raw_text'] for s in segs),'corrected_text':' '.join(s['corrected_text'] for s in segs),'semantic_type':family,'visual_center':title,'organic_motion_need':'Không cần diễn viên/plate hữu cơ; puppet vector có hành động chủ đích.' if present else 'Không cần; vật thể/quan hệ là chủ thể.','exact_graphics_need':'Tách lớp hình học và tiếp xúc, tiếng Việt native.','preferred_mode':'HF_ONLY','routing_confidence':'high','routing_reason':reason,'flow_contribution':'none','hf_contribution':action,'fallback_mode':None,'fallback_condition':'Dừng cảnh khi thiếu asset; không thay bằng card. Đổi engine cần override có lý do.','character':'yes' if present else 'no'}
        routes.append(route)
        pilot=n in (1,5,9)
        asset=[{'layer':layer,'source':'approved mascot derivative' if 'mascot' in layer else ('Wikimedia Commons: Skyline of Valletta.jpg / Juliana da Costa José / CC BY-SA 3.0' if layer=='valletta-photo' else 'new original layered vector; authored in this package for pilots, Antigravity for remaining scenes'),'status':'planned','required_separate_layer':True} for layer in layers]
        # Cue timing is a directing approximation, not forced word alignment.
        if n==1: beats=[(0,'Khi con du học Châu Âu','Mở cận sách, tay bắt đầu với'),(1.55,'đầu tư cho việc học','Bìa mở, chữ HỌC TẬP'),(3.05,'mà còn đầu tư','Trang gấp nâng mặt đỡ'),(4.25,'điểm tựa lâu dài','Nhà giấy rõ hình, đổi text và ngước nhìn'),(5.25,'đuôi câu','Giữ kết quả')]
        elif n==5: beats=[(0,'Đó là lý do','Bản đồ giấy còn gấp, tay với'),(.7,'ngày càng nhiều gia đình','Tay chạm góc giấy'),(1.5,'lựa chọn đa dạng hóa','Mở lá giấy, vẫn giữ vật thể cũ'),(3.1,'bất động sản','Nhà giấy dựng ở chân ảnh'),(4.1,'tại Malta','MALTA rõ, mascot nhìn ảnh'),(5.0,'khoảng nghỉ','Giữ collage')]
        elif n==9: beats=[(0,'Đồng thời, việc sở hữu','Ba đồng cùng một nơi'),(1.25,'ở nhiều thị trường','Mở hai rãnh phân bổ'),(2.55,'đa dạng hóa danh mục','Hai đồng theo rãnh tới vùng khác'),(4.907,'thay vì phụ thuộc','Bệ trung tâm còn một đồng; các vùng vẫn dao động'),(6.35,'một quốc gia','Nhãn nhiều thị trường; giữ phân bổ')]
        else: beats=[(0,'đầu lát nguồn',opening),(round(duration*.25,3),'cụm ý đầu — đối chiếu WAV',action.split(';')[0]),(round(duration*.60,3),'cụm ý sau — đối chiếu WAV',action),(round(duration*.83,3),'đuôi câu / nghỉ',final)]
        containers=[]
        if n in (1,2,3,5,6,7,10,11,14):
            object_name={1:'book',2:'ledger',3:'fold-out plan',5:'folded travel paper',6:'dining table',7:'laptop',10:'family album',11:'backpack',14:'choice plan'}[n]
            containers=[{'object_type':object_name,'bounds':'Trong vùng y=340–1040, theo staging cảnh','semantic_boundary':'Vật thể thật có mép/nếp/chức năng; không là khung chứa thông tin.','removal_consequence':'Mất hành động mở/giữ/đặt hoặc quan hệ trên bề mặt; Boundary Removal Test: giữ.'}]
        accent='blue short feature strip' if n in (1,7,11) else 'none'
        scene={**route,'title':title,'takeaway':meaning,'audio_source':[f'inputs/audio/seg_{i:02d}.wav' for i in ids],'duration':duration,'sample_frames':end_sample-start_sample,'raw_segments':segs,'render_mode':'HF_ONLY','style_candidates':[{'id':'hf_existing:warm-doodle-mixed-media','fit':'Bám brief đã duyệt; prop lớn, màu tươi, mascot gọn, collage có lý do.'},{'id':'kurzgesagt','fit':'Rõ lớp và biến đổi nhưng hình khối sạch/dày dễ xa nét mảnh và giấy của reference.'},{'id':'izometrik','fit':'Chỉ hữu ích khi cần cấu trúc không gian; cảnh này không cần hệ nhìn nghiêng toàn phần.'},{'id':'bauhaus','fit':'Nhịp hình học gọn nhưng không đủ hành động cụ thể của lời thoại.'}],'style_id':'hf_existing:warm-doodle-mixed-media','style_reference':'inputs/reference/DIRECTOR_BRIEF.md; approved reference scene 04/06/12 sources are external read-only','style_reason':'Ưu tiên cụ thể người dùng cao hơn mặc định style; giữ ngữ pháp hình, thiết kế nội dung mới.','visual_verb':verb,'composition':layout,'composition_reason':'Hình chủ đạo trải từ khoảng y=350 tới y=1040; footer y=1080–1280 chỉ có nền. Khoảng trống phục vụ thay đổi và đường mắt.','opening_state':opening,'transformation':action,'final_state':final,'protagonist_action':character,'mascot_role':character,'visual_family':family,'timed_beats':[{'local_seconds':t,'spoken_cue':cue,'action':act,'alignment':'approximate_directorial_cue_not_word_alignment'} for t,cue,act in beats],'motion_emphasis_sequence':[b[2] for b in beats],'hf_signature_motion':action,'flow_action':None,'flow_camera':None,'overlay_zone':'native typography y=150–330, content y=340–1060; subtitle reserve y=1080–1280','asset_contract':asset,'container_required':bool(containers),'container_inventory':containers,'container_semantics':containers,'visible_text_budget':{'max_simultaneous_words':max(len(t.split()) for t in text)+ (4 if n==10 else 0),'max_levels':2,'paragraphs':0},'visible_text_inventory':[{'text':t,'size_px':32 if n==10 and j==1 else (46 if len(t)>19 else 54),'role':'condition' if n==10 and j==1 else 'anchor','simultaneous':n in (4,10)} for j,t in enumerate(text)],'text_treatment':'Chữ native Segoe UI Black, dấu đầy đủ; đổi cụm thay vì tích lũy. '+('Một strip xanh ngắn có nghĩa nhấn ý.' if accent!='none' else 'Chữ trần trên nền sáng; không sweep.'),'accent_reason':'Nhấn sự chuyển trọng tâm của câu; không tô cả cảnh.' if accent!='none' else 'none','accent_treatment':accent,'mobile_legibility_plan':'720×1280 xuống 360×640; headline 46–54px; điều kiện 32px; text một–hai dòng ngắn, không dùng nhãn 18px; kiểm dấu ở bản raster.','dark_mass_strategy':'Nét #30313B 3–4px, màu đậm chỉ cho chữ/nét. Mặt bàn/nhà/túi dùng tint sáng và xanh, không nhiều khối navy.','handoff':transition,'continuity_risk':risk,'pilot':pilot,'status':'designed_not_produced','must_keep':[meaning,action,'voice/sample bounds','mascot identity, warm light palette, footer 200px','zero added CTA or documentary claims'],'flexible':['Toạ độ/kích thước trong safe area','easing/pose/chi tiết nét','dời cue nội cảnh sau đối chiếu voice; không đổi audio'],'reference_alignment':{axis:{'reference_evidence':ref,'candidate_evidence':f'{sid}: {evidence}','assessment':'pending_render_review','revision_needed':'Đối chiếu proof thực tế, không suy từ check.'} for axis,ref,evidence in [('colour_relationships','Brief: cream/peach/lilac + accents','warm ground and vivid orange/blue/purple'),('typography_treatment','Reference 06/12: Segoe UI Black Vietnamese','local shipped font, sparse native text'),('asset_mix','Reference 04/06: real campus plus drawing','Valletta photo where geographic evidence is needed; vector/physical paper elsewhere'),('composition','Reference 04: large prop; 12: shared meaningful surface',layout),('mascot_language','Reference 12: orange body, purple cap, blue backpack',character),('motion_rhythm','Reference 12: piece fits / cap worn / selection made',action)]}}
        scenes.append(scene)
        fs=(start_sample*30+rate//2)//rate; fe=(end_sample*30+rate//2)//rate
        assert fs==prior; prior=fe
        picture.append({'scene_id':sid,'start_sample':start_sample,'end_sample':end_sample,'global_start_frame':fs,'global_end_frame':fe,'picture_frames':fe-fs,'fps':30,'grid_error_ms':round((fs/30-start)*1000,5)})
    save('scratch/scene_routing.json',{'locked':True,'audit':{'HF_ONLY':14,'FLOW_ONLY':0,'HYBRID':0,'hf_ratio':1,'reconsidered_high_hf_ratio':True,'reason':'Từng cảnh đã xét HYBRID. Nghĩa nằm ở biến đổi cấu trúc giấy, phân bổ, puppet compact hoặc collage. Diễn viên thật sẽ đổi phong cách đã duyệt; không dùng Flow làm wallpaper. Không quota Flow.','protagonist_scenes':11,'total_scenes':14,'protagonist_ratio':11/14,'consecutive_hf_run':14,'repeat_treatment_review':'14 họ hành động/bối cảnh có phân biệt; lặp sách/nhà được giãn và đổi quan hệ, xem CONTINUITY.'},'scenes':routes})
    save('scratch/scene_routing.md','# Routing đã khóa\n\n100% HF_ONLY đã được xét lại vì vượt 60% và có nhiều cảnh liên tiếp. Lý do: quan hệ và biến đổi lớp là chủ thể; không cần diễn viên thật hay camera hữu cơ. Giữ mascot/collage đã duyệt, không dùng Flow nền.\n\n'+'\n'.join(f"- {s['scene_id']} {s['start']:.5f}–{s['end']:.5f}s · {s['visual_center']} · {s['routing_reason']}" for s in routes))
    save('STORYBOARD.json',{'project':'VIDEO-33-director-pilot','duration':frames/rate,'sample_rate':rate,'total_samples':frames,'canvas':[720,1280],'fps':30,'pilot_selection':{'method':'purposeful_directorial_selection_not_random','ids':['S01','S05','S09'],'rationale':['S01: biến đổi vật thể + tiếp xúc mascot','S05: ảnh thật/giấy/vector + mở nếp','S09: cơ chế phân bổ không người, giải thích quan hệ']},'cue_accuracy':'Mốc đạo diễn nội cảnh ước lượng; ranh giới sample nguồn chính xác. Không coi ASR/thiết kế là nghe kiểm chứng độc lập.','scenes':scenes})
    save('planning/picture_frame_plan.json',picture)
    with (ROOT/'planning/picture_frame_plan.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=picture[0]);w.writeheader();w.writerows(picture)
    md=['# Storyboard · Một điểm tựa, thêm lựa chọn','', 'Voice 75.16s / 1,803,840 samples / mono PCM16 24kHz. 17 lát gộp thành 14 cảnh, không mất/trùng sample. Pilot S01/S05/S09 là ba trích đoạn độc lập, không chứng minh seam toàn phim.','', '| Cảnh | Voice gốc | Ý & hình chủ đạo | Chuyển động | Chữ |','|---|---|---|---|---|']
    for s in scenes:
        md.append(f"| {s['scene_id']} {'PILOT' if s['pilot'] else ''} | {s['start']:.3f}–{s['end']:.3f}s / seg {s['source_segments']} | {s['title']} — {s['takeaway']} | {s['visual_verb']} | {' → '.join(t['text'] for t in s['visible_text_inventory'])} |")
        packet=f"# {s['scene_id']} · {s['title']}\n\n**Voice:** {s['start']:.8f}–{s['end']:.8f}s; samples [{s['start_sample']}, {s['end_sample']}); {s['duration']:.8f}s.\n\n**Raw, giữ nguyên:** {s['raw_text']}\n\n**Corrected text riêng:** {s['corrected_text']}\n\n**Ý chính:** {s['takeaway']}\n\n**Bố cục:** {s['composition']}\n\n**Đầu:** {s['opening_state']}\n\n**Hành động:** {s['transformation']}\n\n**Kết:** {s['final_state']}\n\n**Nhân vật:** {s['protagonist_action']}\n\n**Engine:** {s['render_mode']}. {s['routing_reason']}\n\n**Nhịp theo voice:** (ước lượng đạo diễn, không word-alignment)\n\n"+'\n'.join(f"- {b['local_seconds']:.3f}s · {b['spoken_cue']} → {b['action']}" for b in s['timed_beats'])+f"\n\n**Chữ:** {s['visible_text_inventory']}\n\n**Asset/layer:** "+', '.join(a['layer'] for a in s['asset_contract'])+f"\n\n**Container:** {s['container_inventory']}\n\n**Mobile:** {s['mobile_legibility_plan']}\n\n**Dark masses:** {s['dark_mass_strategy']}\n\n**Accent:** {s['accent_treatment']}\n\n**Sang cảnh sau:** {s['handoff']}\n\n**Giữ:** "+'; '.join(s['must_keep'])+"\n\n**Linh hoạt:** "+'; '.join(s['flexible'])+f"\n\n**Cần lưu ý:** {s['continuity_risk']}\n"
        save(f"scenes/{s['scene_id']}/PACKET.md",packet);save(f"scenes/{s['scene_id']}/packet.json",s)
    md+=['','Đọc packet từng cảnh để thi công; JSON lưu đủ asset/text/engine/style/mobile/continuity. Không triển khai 11 cảnh còn lại trong lượt này.']
    save('STORYBOARD.md','\n'.join(md))
    assets={'reused':[{'id':'mascot','source':str(REFERENCE/'reference_pilots/scene_12/assets/student.js'),'use':'Giữ hình nhận diện, tách arm/eyes/legs và pose mới. Không dùng bộ student human bị từ chối.'},{'id':'display-font','source':str(REFERENCE/'library/fonts/segoe-ui-black.ttf'),'use':'Local native Vietnamese glyphs'},{'id':'gsap','source':str(REFERENCE/'reference_pilots/scene_12/assets/gsap.min.js'),'use':'Offline seekable runtime'}],'new_pilot':[{'scene':s['scene_id'],'layers':s['asset_contract']} for s in scenes if s['pilot']],'remaining':[{'scene':s['scene_id'],'status':'DESIGN_ONLY / Antigravity creates after approval','layers':s['asset_contract']} for s in scenes if not s['pilot']],'photography':{'file':'assets/valletta.jpg','source':'https://commons.wikimedia.org/wiki/File:Skyline_of_Valletta.jpg','author':'Juliana da Costa José','license':'CC BY-SA 3.0','license_url':'https://creativecommons.org/licenses/by-sa/3.0/','modifications':'Framing/crop within the composition; no claims about ownership or sale.','purpose':'Geographic context, not property advertisement.'}}
    save('ASSET_PLAN.json',assets)
    save('ASSET_PLAN.md','# Asset plan\n\nGiữ mascot từ reference 12; làm pose/rig theo cảnh. Segoe UI Black và GSAP copy local. Không dùng kit human/muted của trial bị từ chối.\n\nPilot: S01 cuốn sách/trang gấp/mái nhà/nhóm gia đình; S05 ảnh Valletta + viền ảnh/giấy gấp/ngôi nhà/mascot; S09 cơ cấu rãnh cong/ba bệ/ba đồng tài sản/dấu dao động. Mỗi lớp điều khiển độc lập, không flatten video thành một ảnh.\n\n11 cảnh còn lại chỉ có kế hoạch, xem scenes/Sxx/packet.json. Antigravity cần tạo layer theo asset_contract; chưa có asset không được đổi sang card generic.\n\nẢnh Valletta: Juliana da Costa José, Wikimedia Commons, CC BY-SA 3.0. Dùng để nhận biết nơi chốn; không là dự án bất động sản, không coi cảnh chụp cũ là bằng chứng giá hiện tại. Credit và link license nằm trong ASSET_PLAN.json và CREDITS.md.\n\nTất cả asset pilot được đóng gói local; status final phải đối chiếu file thực tế, không suy từ bảng này.')
    # Only now freeze input copies, after planning/routing.
    for name in ['audio_handoff.json','transcript.json','transcript.md','whisper_raw.json','whisper_guided.json','HANDOFF_TO_CODEX.md']:
        shutil.copy2(SOURCE/name,ROOT/'inputs'/name)
    shutil.copy2(SOURCE/'inputs/source_audio.wav',ROOT/'inputs/source_audio.wav')
    for seg in handoff['segments']:
        shutil.copy2(SOURCE/seg['audio_slice'],ROOT/'inputs/audio'/Path(seg['audio_slice']).name)
    (ROOT/'inputs/reference').mkdir(exist_ok=True)
    shutil.copy2(REFERENCE/'DIRECTOR_BRIEF.md',ROOT/'inputs/reference/DIRECTOR_BRIEF.md')
    for font in ['segoe-ui-black.ttf','arial.ttf','arialbd.ttf']:
        shutil.copy2(REFERENCE/'library/fonts'/font,ROOT/'assets/fonts'/font)
    shutil.copy2(REFERENCE/'reference_pilots/scene_12/assets/gsap.min.js',ROOT/'assets/runtime/gsap.min.js')
    shutil.copy2(REFERENCE/'reference_pilots/scene_12/assets/student.js',ROOT/'assets/approved-student-source.js')
    save('BRIEF.md','---\nworkflow: general-video\nflow: companion\nstoryboard: yes\naspect: 9:16\nlanguage: vi\nlength: 75.16\n---\n\n# VIDEO-33 · Một điểm tựa, thêm lựa chọn\n\nScope người dùng: storyboard toàn phim và khoảng 3 pilot voice gốc; dừng để duyệt, chưa dựng full. Phong cách warm doodle theo brief đã duyệt, thiết kế mới từ voice. Cụ thể hóa thành 14 cảnh, pilot S01/S05/S09. Không nhạc/TTS/CTA/footage Flow thêm. Khung 720×1280 và 30fps theo reference là giả định thi công, không thay đổi nội dung audio.\n\nĐã đọc voice-to-scene-design và warm-doodle-video tại skills/ trước thiết kế. HyperFrames/fk-edu-motion-explainer cung cấp hợp đồng kỹ thuật và routing. User đã yêu cầu tạo MP4 pilot; không hỏi lại render approval.\n')
    save('DIRECTOR_BRIEF.md','# Đạo diễn · Một điểm tựa, thêm lựa chọn\n\nPhim 75.16s đặt việc học của con cạnh kế hoạch dài hạn của gia đình. Kể bằng các vật thể có chức năng: sách nâng đỡ, giấy mở nơi chốn, bàn mở chỗ, dây kết nối, rãnh phân bổ và kế hoạch mở nhánh. Mỗi hành động phải giúp hiểu quan hệ, không chỉ đưa các danh từ bay vào.\n\nGiữ nền cream #FFF8E9, peach #FFF0E5, lilac #F0EAFB; nét #30313B mảnh; cam #FFAA28, mũ #A990D5, túi #087BC1. Font local Segoe UI Black đầy đủ dấu; body Arial nếu cần trong tài liệu. Không Arial Black, không chữ Hình minh hoạ/Không gian minh hoạ trên video.\n\nGiữ nguyên toàn bộ WAV, raw transcript và sample timing; corrected_text riêng chỉ chuẩn ASR/tên Malta. Không sửa câu giá/rights trong voice. Có vấn đề fact-check phải giữ trạng thái chưa duyệt xuất bản (RESEARCH.md), không ngầm sửa hoặc khẳng định bằng đồ họa.\n\nBa pilot là S01 biến đổi sách/điểm tựa; S05 collage địa điểm thật và giấy gấp; S09 cơ chế phân bổ nhiều thị trường. Chọn có chủ đích để thử ba bài toán khác nhau. Không sản xuất các cảnh khác.\n\nBắt buộc giữ: ý nghĩa/quan hệ từng packet, identity mascot, voice/timing, visual chủ đạo và signature action, không hứa việc làm/quốc tịch/lợi nhuận. Linh hoạt: cân khung, pose, easing, nếp giấy, chi tiết nét và mốc cử động trong cùng lát voice sau khi nghe đối chiếu. Đổi visual chủ đạo/engine phải ghi override có lý do.\n\nĐây là bản đề xuất để người dùng duyệt, không phải phong cách mới đã được chấp nhận. Reference nguồn và workflow chính giữ read-only.\n')
    save('CONTINUITY.md','# Continuity & redundancy audit\n\n## Nhịp chuỗi\n\n01 sách/điểm tựa → 02 cận chi phí → 03 mở kế hoạch nhiều năm → 04 câu hỏi tập trung → 05 collage địa điểm → 06 bàn gia đình → 07 cuộc gọi → 08 gặp mặt → 09 cơ chế phân bổ → 10 album thế hệ → 11 sắp đồ → 12 thử dụng cụ → 13 xoay địa cầu → 14 lựa chọn tĩnh hơn.\n\nKhông ép mọi seam thành match cùng bước chân. Cắt theo ý, đổi tỷ lệ/bối cảnh khi nội dung đổi. S05 Malta không trùng cảnh S09 nhiều thị trường: một bên định vị thực, một bên quan hệ danh mục. S01/S06 đều nói nền tảng gia đình nhưng một bên vật thể nâng đỡ, một bên hành động chia sẻ bàn. S03/S14 dùng giấy gấp cách xa nhau: trước là trải thời gian, sau là mở khả năng chưa chọn. Nhà chỉ là motif phụ ở 05/14; không lặp bố cục nhà trung tâm.\n\n11/14 cảnh có protagonist (78.6%); 02/04/09 chủ động không thêm người. Mascot cam/mũ tím/túi xanh, không idle corner-filler. Các nhân vật gia đình cần quan hệ rõ, không biến mọi người thành bản sao mascot đội mũ.\n\n## Chữ và accent\n\nChỉ anchor ngắn, voice giải thích. HỌC TẬP rời trước ĐIỂM TỰA; MỘT NƠI rời trước NHIỀU THỊ TRƯỜNG. Không subtitle thứ hai. Footer y=1080–1280 trống. Strip xanh ngắn ở 01/07/11, không các cảnh liền nhau hay trong vòng 4 cảnh; không yellow sweep mặc định. S10 cần điều kiện MPRP thấy được, không footnote li ti.\n\n## Cần kiểm khi full production được duyệt\n\nMàu và tuyến mắt ở seam 04→05, density 08→09, hiểu đúng gia phả 10, không nhầm cơ hội thành đảm bảo ở 12→14. Ba pilot độc lập chưa chứng minh các seam này, chưa có full playback.\n')
    save('RESEARCH.md','# Xác minh nội dung · 26/10/2026\n\nNguồn chính thức đã mở: [Residency Malta — MPRP](https://residencymalta.gov.mt/legal-framework-mprp-2/), [S.L.217.26, sửa bởi LN146/2025](https://residencymalta.gov.mt/wp-content/uploads/2025/08/S.L.217.26-Amended-by-LN-310-of-2024_-LN-146-of-2025.pdf), [EU Immigration Portal — Malta](https://home-affairs.ec.europa.eu/policies/migration-and-asylum/eu-immigration-portal/international-service-provider-malta_en).\n\n- MPRP là thường trú Malta, khác quốc tịch. Mua tài sản không tự sinh quyền này. Không vẽ “nhà → hộ chiếu EU”.\n- Có thể đưa tới bốn thế hệ vào một hồ sơ, có điều kiện. S.L.217.26 p.2: con 18–dưới 29 phải chưa kết hôn và chủ yếu phụ thuộc; cha mẹ/ông bà không làm toàn thời gian và chủ yếu phụ thuộc. “4 thế hệ” không là bốn thế hệ con cháu kế tiếp hay mọi gia đình tự đủ.\n- Trang MPRP hiện nêu phí hành chính €60,000 + đóng góp €37,000 + từ thiện €2,000; thuê tối thiểu €14,000/năm hoặc mua từ €375,000, giữ 5 năm; có phí thành viên trưởng thành/thẻ, bảo hiểm, điều kiện tài sản. Phép cộng 5 năm thuê cơ bản: €60,000 + €37,000 + €2,000 + 5×€14,000 = €169,000, CHƯA phí thẻ/người phụ thuộc/đại lý/bảo hiểm. Đây là phép cộng từ nguồn, không báo giá. Phần giải thích €140–150k trong handoff không khớp cấu phần hiện tại.\n- Không có tỷ giá, báo giá và phạm vi dịch vụ để chứng thực “chỉ với khoảng 3,8 tỷ đồng”. Giữ audio, không dùng số ấy làm hero metric hoặc khẳng định đó là giá trọn gói. S10 đặt HOLD_PUBLICATION trước khi dựng/publish thương mại; cần chủ nội dung duyệt cơ sở chi phí/voice. Bỏ số trên hình không tự giải quyết câu nói trong audio.\n- MPRP không tự cấp quyền làm việc tại Malta hoặc các nước EU khác; EU Immigration Portal nói cần quyền lao động phù hợp. Quyền Schengen đi ngắn hạn 90/180 ngày không đồng nghĩa sinh sống/làm việc khắp châu Âu. S07/08 phải giữ nghĩa dự định, không thẻ mở tất cả quyền.\n- “Ngày càng nhiều gia đình”, lợi ích đầu tư và điểm tựa dài hạn là lời dẫn/quan điểm trong nguồn audio, chưa có thống kê chứng minh xu hướng/lợi nhuận. Không thêm chart tăng giá, % hay dấu an toàn.\n\nText ASR chuẩn hóa: Malta/bất động sản/danh mục/giá trị; giữ raw và uncertainties ở inputs/. Seg02 câu đầu chưa sửa ngữ pháp trong voice. Seg13 con gái/con cái giữ unresolved; hình và anchor không chốt giới tính. Không tuyên bố đã nghe xác nhận âm vị nếu công cụ chỉ đưa file phát lại.\n')
    save('production_status.json',{'project':'VIDEO-33-director-pilot','phase':'storyboard_complete_pilot_production_pending','user_approved':False,'source_read_only':True,'duration':75.16,'scenes_designed':14,'pilots_requested':['S01','S05','S09'],'full_film_rendered':False,'remaining_scenes_authorized_for_render':False,'publication_hold':['S10 source voice price claim needs factual approval'],'flow_health':'unreachable during preflight; no Flow generation required by locked HF_ONLY routing','hyperframes_usage':'unknown / usage_request_failed'})
    print(f'Created {len(scenes)} scene packets; audio bit-exact verified. Root: {ROOT}')

if __name__=='__main__': main()
