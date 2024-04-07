import sys
input = sys.stdin.readline

# 입력 받기
N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 주사위의 상태를 저장하는 클래스
class Dice:
    def __init__(self):
        self.top = 0
        self.bottom = 0
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0

    # 주사위를 동쪽으로 굴리는 메소드
    def roll_east(self):
        self.top, self.west, self.bottom, self.east = self.west, self.bottom, self.east, self.top

    # 주사위를 서쪽으로 굴리는 메소드
    def roll_west(self):
        self.top, self.east, self.bottom, self.west = self.east, self.bottom, self.west, self.top

    # 주사위를 북쪽으로 굴리는 메소드
    def roll_north(self):
        self.top, self.south, self.bottom, self.north = self.south, self.bottom, self.north, self.top

    # 주사위를 남쪽으로 굴리는 메소드
    def roll_south(self):
        self.top, self.north, self.bottom, self.south = self.north, self.bottom, self.south, self.top

# 주사위 객체 생성
dice = Dice()

# 이동할 때마다의 좌표 변화와 주사위의 상태 업데이트
dx = [0, 0, -1, 1]  # 동, 서, 북, 남
dy = [1, -1, 0, 0]
for command in commands:
    nx, ny = x + dx[command - 1], y + dy[command - 1]
    if 0 <= nx < N and 0 <= ny < M:  # 지도를 벗어나지 않는 경우
        if command == 1:  # 동쪽으로 굴리기
            dice.roll_east()
        elif command == 2:  # 서쪽으로 굴리기
            dice.roll_west()
        elif command == 3:  # 북쪽으로 굴리기
            dice.roll_north()
        else:  # 남쪽으로 굴리기
            dice.roll_south()
        if board[nx][ny] == 0:  # 칸에 쓰여 있는 수가 0이면 주사위의 바닥면에 쓰여 있는 수를 칸에 복사
            board[nx][ny] = dice.bottom
        else:  # 칸에 쓰여 있는 수가 0이 아니면 칸에 쓰여 있는 수를 주사위의 바닥면에 복사하고, 칸에는 0을 쓴다.
            dice.bottom = board[nx][ny]
            board[nx][ny] = 0
        x, y = nx, ny  # 좌표 업데이트
        print(dice.top)  # 주사위의 윗 면에 쓰여 있는 값을 출력
