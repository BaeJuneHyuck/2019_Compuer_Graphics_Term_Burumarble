# 2019, PNU CSE, coputer graphics term project 부루마블

컴퓨터그래픽스 텀프로젝트 : 釜루마블


201424464 배준혁
201524479 변찬호
201524443 김재영

# 개요
 * 부산대학교를 배경으로 고전 보드게임 부루마블을 구현

# 특징
* Open GL API를 활용하여 입체적으로 시점을 구현
* 캐릭터에 각각 다른 모델을 적용하여 일반적인 부루마블의 ‘말’과 달리 캐릭터 마다 특성을 부여
* 캐릭터가 움직일 때 시점을 변경하여 역동적으로 움직임을 연출.
* 게임 지도의 가운데에 주사위를 3d 오브젝트로 구현하여 사용자가 실제로 주사위를 굴리는 느낌을 받을 수 있게 함.
* 부산대학교의 여러 건물과 장소들을 사용하여 친근감을 줌

# 구현할 기능
* 게임화면 만들기(시스템) : 게임판과 UI
* 주사위 버튼을 통해 주사위 굴리고 값을 시스템에 전달.
* 캐릭터 이동과 건물 배치 시 시점변경과 움직임 구현
* 화면에서 UI를 통해서 각 플레이어의 골드, 캐릭터 사진, 그리고 현재 순서 표시.

# 역할 분담
		공통 : 게임화면(시스템), UI 제작
		배준혁 : 캐릭터 애니메이션과 시점 변경, 기능 구현
		변찬호 : 건물 애니메이션과 시점 변경, 기능 구현
		김재영 : 주사위 애니메이션과 버튼구현

# 게임 실행
python을 통해 main.py를 실행한다.
 
![Preview](https://github.com/BaeJuneHyuck/2019_Compuer_Graphics_Term_Burumarble/blob/master/capture/capture1.png?raw=true)

<그림1 초기화면>

게임을 처음 실행하면 위와 같은 화면을 볼 수 있다. 각 화면의 모서리에 플레이어의 이름과, 그림, 가지고 있는 돈이 출력된다. 화면 중앙은 게임이 진행되는 지도와 캐릭터들이 출력된다. 또한 마우스 드래그와 마우스 휠을 통해 시점을 움직이거나 확대할 수 있다.
 
 이제 각 플레이어는 화면 중앙 아래에 있는 주사위 버튼을 클릭하여 자신의 캐릭터를 움직일 수 있다. 주사위가 굴려지면 그 값만큼 캐릭터가 이동한다.
 ![Preview](https://github.com/BaeJuneHyuck/2019_Compuer_Graphics_Term_Burumarble/blob/master/capture/capture2.png?raw=true)
 
<그림2 주사위 굴리기>
 
 ![Preview](https://github.com/BaeJuneHyuck/2019_Compuer_Graphics_Term_Burumarble/blob/master/capture/capture3.png?raw=true)
 
<그림3 주사위만큼 이동 후 건물 생성> 

![Preview](https://github.com/BaeJuneHyuck/2019_Compuer_Graphics_Term_Burumarble/blob/master/capture/capture4.png?raw=true)

<그림4 다른 플레이어가 산 건물에 이동, 파산>

이동시 다른 플레이어가 구입한 건물에 이동하면 자신의 골드가 줄어든다. 돈이 0원이되면 파산하여 플레이어 그림이 해골그림으로 바뀌며 자신의 집이 모두 사라진다.

# 클래스 개요

전체적인 클래스 구성은 아래와 같다.

* Game.py: 모든 게임 객체와 정보를 가지고 있는 최상위 객체이다.
* Board.py: 게임 보드, 각각의 인덱스, 위치좌표를 가지고 있으며 나타내는 부산대의 장소가 다르다.
* Dice.py : 주사위를 표현하는 클래스. 무작위 값에 대한 애니메이션을 재생한다.
* Character.py : 플레이어의 캐릭터. 플레이어 별 색깔이 다르며 주사위를 굴린 뒤 해당 값에 따라 보드를 이동한다.
* Building.py : 보드에 생성되는 건물, 플레이어 별로 색깔이 다르다. 
* Playstate.py : 게임중인 플레이어의 이름, 가지고 있는 돈을 출력

각 게임 객체들은 gameManager 클래스의 각 리스트에 의해 관리되며, display 함수 호출 시 각각의 draw()메소드를 통해 그려지게 된다.


