# Toon Maker
Convert a video into cartoon style.


## 사용자 입력

#### [TAB키] 모드 변환
- 모드 1: 카툰 스타일 뷰 (Cartoon Style)
- 모드 2: 엣지 검출 뷰 (Edge Detection)

#### [＋/－키] 스케일 확대 / 축소 (10%p)


## 실행 결과

### 사진

<모드 2: 흑백 | Canny엣지 | 엣지마스크>
<img width="1167" alt="toon_edges" src="https://github.com/illboi1/toon-maker/assets/88954347/8222f69d-dd87-4e9b-a9ee-8a3c81e729b0">

<모드 1: 원본 | 스무딩 | 카툰>
<img width="1167" alt="toon" src="https://github.com/illboi1/toon-maker/assets/88954347/bf0fe7d9-d83b-4cfb-9977-f77e8b5faeb5">


### 동영상

<동영상 1: 만화스러운 변환 성공>

<동영상 2: 만화스러운 변환 실패>

변환이 자연스러운 경우: 요소와 배경이 복잡할 때 테두리가 부각되면서 만화풍이 강조되는 효과가 있음
한계 논의: 요소간의 간격이 너무 짧거나 (ex. 노트북 키보드 자판), 평면적인 배경에서는 테두리가 덜 부각되면서 만화스러운 표현이 적게 나타남
