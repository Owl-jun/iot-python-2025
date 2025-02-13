import pygame
import sys
import random
import os

# -------------------------------
# 상수 정의 (Constants)
# -------------------------------
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 800
GRID_SIZE = 80
FPS = 30

# 색상 정의
WHITE   = (255, 255, 255)
GREEN   = (0, 200, 0)
RED     = (250, 0, 0)
BLUE    = (100, 30, 150)
BLACK   = (0, 0, 0)
BROWN   = (165, 42, 42)
GRAY    = (50, 50, 50)

# -------------------------------
# 이미지 로딩 헬퍼 함수
# -------------------------------
def load_image(filename, colorkey=None):
    full_path = os.path.join('TOYPROJECT', filename)
    try:
        image = pygame.image.load(full_path)
    except pygame.error as message:
        print('Cannot load image:', full_path)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        image.set_colorkey(colorkey)
    return image

# -------------------------------
# 게임 상태 관리 클래스
# -------------------------------
class Game:
    def __init__(self):
        self.started = False
        self.player_turn = True
        self.shaking = False
        self.selecting_pawn = False
        self.selected_pawn = None

    def start(self):
        self.started = True
        self.shaking = False
        self.selecting_pawn = False

    def toggle_turn(self):
        self.player_turn = not self.player_turn

    def reset_pawn_selection(self):
        self.selecting_pawn = False
        self.selected_pawn = None

# -------------------------------
# 버튼 클래스
# -------------------------------
class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.font = pygame.font.SysFont('malgungothic', 30)
        self.pressed = False

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect, border_radius=10)
        label = self.font.render(self.text, True, WHITE)
        text_rect = label.get_rect(center=self.rect.center)
        screen.blit(label, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.pressed and self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()
            self.pressed = False

# -------------------------------
# 보드(발판) 클래스
# -------------------------------
class Board:
    def __init__(self):
        self.steps = []
        self.special_steps = {5: [6, 20], 10: [11, 25], 22: [23, 27]}
        self.bg_image = load_image('py96_bg.webp')
        self.bg_image.set_alpha(60)
        self.create_steps()
        # 메인 루트: 인덱스 0~19, 19 다음은 도착(-2)
        self.main_route = {i: i + 1 for i in range(19)}
        self.main_route[19] = -2
        # 분기 루트 매핑 (분기 선택 시 사용)
        # 예시: index 5에서 분기 선택(20)을 한 경우
        self.branch_routes = {
            20: {20: 21, 21: 22, 22: 23, 23: 24, 24: 15},  # 분기: 20 → 21 → 22 → 23 → 24 → 15
            25: {25: 26, 26: 27, 27: 15},                   # 분기: 25 → 26 → 27 → 15
            27: {27: 28, 28: 15}                            # 분기: 27 → 28 → 15
        }
    
    def create_steps(self):
        self.back_panel = pygame.Rect((SCREEN_WIDTH/2) - ((GRID_SIZE*5.5)/2)-30, 20, 500, 500)
        start_x = (SCREEN_WIDTH/2) - ((GRID_SIZE*5.5)/2)
        start_y = 50
        self.positions = [
            # 네모 발판 좌표 (인덱스 0~19)
            (5,5), (5,4), (5,3), (5,2), (5,1), (5,0),
            (4,0), (3,0), (2,0), (1,0), (0,0), (0,1),
            (0,2), (0,3), (0,4), (0,5), (1,5), (2,5),
            (3,5), (4,5), 
            # 대각선 발판 좌표 (인덱스 20~28)
            (4,1), (3.2,1.8), (2.5,2.5), (1.8,3.2), (1,4), (1,1), (1.8,1.8), (3.2,3.2), (4,4)
        ]
        for x, y in self.positions:
            rect = pygame.Rect(start_x + (x * GRID_SIZE), start_y + (y * GRID_SIZE), 40, 40)
            self.steps.append(rect)
    
    def calculate_main_move(self, start, steps):
        """ 메인 루트에서 start 위치부터 steps만큼 이동한 후의 위치를 반환 """
        pos = start
        for _ in range(steps):
            if pos == -2:
                return -2
            pos = self.main_route.get(pos, -2)
        return pos
    
    def calculate_branch_move(self, branch_start, steps):
        """ 분기 루트에서 branch_start 위치부터 steps만큼 이동한 후의 위치를 반환 """
        mapping = self.branch_routes.get(branch_start)
        if mapping is None:
            return -2
        pos = branch_start
        for _ in range(steps):
            if pos == -2:
                return -2
            pos = mapping.get(pos, -2)
        return pos
    
    def draw(self, screen):
        # 배경 패널 그리기 (원하는 색상이나 이미지로 수정 가능)
        pygame.draw.rect(screen, GRAY, self.back_panel)
        # 배경 이미지 그리기
        screen.blit(self.bg_image, (0, 0))
        # 각 스텝을 그리기
        for idx, rect in enumerate(self.steps):
            # 특별한 스텝은 다른 색상으로 표시 (예시)
            if idx in self.special_steps:
                color = BROWN
            else:
                color = WHITE
            pygame.draw.rect(screen, color, rect, 0)


# -------------------------------
# 플레이어 UI 클래스
# -------------------------------
class PlayerUI:
    def __init__(self):
        self.font = pygame.font.SysFont('NanumGothic', 36)
        self.player_surface = pygame.Surface((250, 400), pygame.SRCALPHA)
        self.player_surface.fill((RED[0], RED[1], RED[2], 128))
        self.computer_surface = pygame.Surface((250, 400), pygame.SRCALPHA)
        self.computer_surface.fill((BLUE[0], BLUE[1], BLUE[2], 128))

    def draw(self, screen):
        p_text = self.font.render('PLAYER', True, WHITE)
        c_text = self.font.render('COMPUTER', True, WHITE)
        self.player_surface.blit(p_text, (10, 0))
        self.computer_surface.blit(c_text, (10, 0))
        screen.blit(self.player_surface, (50, 100))
        screen.blit(self.computer_surface, (SCREEN_WIDTH - 300, 100))
        pygame.draw.rect(screen, WHITE, (50, 100, 250, 400), 3)
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 300, 100, 250, 400), 3)

# -------------------------------
# 말(Pawn) 클래스
# -------------------------------
class Pawn:
    def __init__(self, board):
        self.board = board
        self.p_positions = [-1] * 5  # -1: 필드, -2: 도착
        self.c_positions = [-1] * 5
        self.pawn_images = {
            'player': [load_image('py96_pPawn.png') for _ in range(5)],
            'computer': [load_image('py96_cPawn.png') for _ in range(5)]
        }
        # 각 말마다 분기 결정(방향) 정보를 기록 (None이면 아직 선택되지 않음)
        self.branch_choices = [None] * 5

    def draw(self, screen, is_player=True):
        positions = self.p_positions if is_player else self.c_positions
        pawns = self.pawn_images['player'] if is_player else self.pawn_images['computer']
        base_x = 100 if is_player else SCREEN_WIDTH - 250
        for idx, pos in enumerate(positions):
            if pos == -1:
                x, y = base_x, 150 + idx * 60
            elif pos == -2:
                continue
            else:
                if pos < len(self.board.steps):
                    rect = self.board.steps[pos]
                    x, y = rect.x, rect.y
                else:
                    continue
            screen.blit(pawns[idx], (x, y))
    
    def move_pawn(self, idx, result, is_player=True):
        """
        선택한 말(idx)를 윷 결과(result)에 따라 이동.
        만약 branch_choices에 분기 결정 값이 저장되어 있다면, 그 값을 기준으로 
        '효과적인 이동거리' = (윷 결과 이동거리 - 1) 만큼만 이동하도록 계산.
        """
        move_dict = {'백도!': -1, '도!': 1, '개!': 2, '걸!': 3, '윷!': 4, '모!': 5}
        move_steps = move_dict.get(result, 0)
        
        if is_player:
            # 분기 결정 값이 저장되어 있다면, 그 값을 새로운 기준(base)으로 사용
            if self.branch_choices[idx] is not None:
                base = self.branch_choices[idx]
                # 결과 이동이 양수이면 이미 분기 결정으로 진입한 효과가 있으므로 -1 보정
                effective_steps = move_steps - 1 if move_steps > 0 else move_steps
                new_pos = self.board.calculate_branch_move(base, effective_steps)
                # 사용 후 branch 결정 값 초기화 (한 번만 적용)
                self.branch_choices[idx] = None
            else:
                base = 0 if self.p_positions[idx] == -1 else self.p_positions[idx]
                new_pos = self.board.calculate_main_move(base, move_steps)
            self.p_positions[idx] = new_pos
        else:
            base = 0 if self.c_positions[idx] == -1 else self.c_positions[idx]
            new_pos = self.board.calculate_main_move(base, move_steps)
            self.c_positions[idx] = new_pos

        print(f'윷 결과: {result}, {"플레이어" if is_player else "컴퓨터"} 말[{idx}]의 새 위치: {new_pos}')
        return new_pos





# -------------------------------
# 윷 클래스
# -------------------------------
class Yut:
    def __init__(self):
        self.grid = 60
        self.start = 90
        self.font = pygame.font.SysFont('malgungothic', 24)
        self.create_yut_assets()
        self.result = []
        self.result_text = ''

    def create_yut_assets(self):
        self.back_plate = pygame.Surface((400, 150), pygame.SRCALPHA)
        self.back_plate.fill((150, 50, 150, 128))
        self.front_images = [load_image('yutFront.png') for _ in range(4)]
        self.back_images = [load_image('yutBack.png') for _ in range(3)]
        self.back_do_image = load_image('yutBackDo.png')

    def shake(self):
        temp = self.front_images + self.back_images + [self.back_do_image]
        random.shuffle(temp)
        self.result = temp[:4]
        self.back_plate.fill(BLACK)
        for i, img in enumerate(self.result):
            offset = random.randint(-20, 20)
            self.back_plate.blit(img, (self.start + i * self.grid, 37 + offset))

    def show_result(self):
        temp = self.front_images + self.back_images + [self.back_do_image]
        random.shuffle(temp)
        self.result = temp[:4]
        self.back_plate.fill(BLACK)
        front_count = 0
        back_count = 0
        is_back_do = False
        for i, img in enumerate(self.result):
            x = self.start + i * self.grid
            self.back_plate.blit(img, (x, 37))
            if img in self.front_images:
                front_count += 1
            elif img in self.back_images:
                back_count += 1
            elif img == self.back_do_image:
                back_count += 1
                is_back_do = True
        if back_count == 1 and is_back_do:
            self.result_text = '백도!'
        elif back_count == 1:
            self.result_text = '도!'
        elif back_count == 2:
            self.result_text = '개!'
        elif back_count == 3:
            self.result_text = '걸!'
        elif back_count == 4:
            self.result_text = '모!'
        elif front_count == 4:
            self.result_text = '윷!'
        text_surface = self.font.render(self.result_text, True, WHITE, BLACK)
        self.back_plate.blit(text_surface, (180, 0))

    def draw(self, screen):
        screen.blit(self.back_plate, (SCREEN_WIDTH//2 - 200, 520))

# -------------------------------
# 전체 게임 관리 클래스 (YutnoriGame)
# -------------------------------
class YutnoriGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("즐거운 윷놀이 게임")
        self.clock = pygame.time.Clock()
        self.game_state = Game()
        self.board = Board()
        self.ui = PlayerUI()
        self.pawn = Pawn(self.board)
        self.yut = Yut()
        self.setup_buttons()
        self.holding_throw = False

        # 분기 선택 상태 관련 변수
        self.branch_selection = False         # 분기 선택 UI 활성화 여부
        self.branch_options = []              # special_steps의 옵션 리스트 (예: [6, 20])
        self.branch_pawn_index = None         # 분기 선택 중인 말의 인덱스
        self.blink_counter = 0                # 깜빡임 효과를 위한 카운터

    def setup_buttons(self):
        self.start_button = Button(SCREEN_WIDTH//2 - 100, 700, 200, 50, "게임 시작", self.start_game)
        self.throw_button = Button(SCREEN_WIDTH//2 - 100, 700, 200, 50, "윷 던지기")

    def start_game(self):
        self.game_state.start()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 게임 시작 전: 시작 버튼 처리
            if not self.game_state.started:
                self.start_button.handle_event(event)
            else:
                self.throw_button.handle_event(event)
                if not self.game_state.selecting_pawn:
                    # 윷 던지기 버튼 클릭 이벤트 처리
                    if event.type == pygame.MOUSEBUTTONDOWN and self.throw_button.rect.collidepoint(event.pos):
                        self.holding_throw = True
                    elif event.type == pygame.MOUSEBUTTONUP and self.throw_button.rect.collidepoint(event.pos):
                        self.holding_throw = False
                        self.yut.show_result()
                        self.game_state.selecting_pawn = True


                # 분기 선택 UI가 활성화되어 있으면 우선 분기 옵션 클릭 처리
                if self.branch_selection and event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    for option in self.branch_options:
                        branch_rect = self.board.steps[option]
                        if branch_rect.collidepoint(mouse_x, mouse_y):
                            # 옵션을 클릭하면 pawn의 위치는 그대로 유지하고, 
                            # branch_choices에 선택한 분기 시작점(예: option)을 기록만 함.
                            self.pawn.branch_choices[self.branch_pawn_index] = option
                            print(f"분기 선택: 말[{self.branch_pawn_index}]가 {option} 방향을 선택 (다음 이동에 적용)")
                            self.branch_selection = False
                            self.branch_options = []
                            # 분기 선택 후에도 pawn 이동은 다음 윷 결과 시 진행되므로 selecting_pawn 상태는 유지
                            break



                # 일반 말 선택 처리 (분기 UI가 활성화되어 있지 않을 때)
                if self.game_state.selecting_pawn and not self.branch_selection and event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    for idx, pos in enumerate(self.pawn.p_positions):
                        if pos == -2:
                            continue  # 도착한 말은 제외
                        # 필드에 있는 말
                        if pos == -1:
                            pawn_rect = pygame.Rect(100, 150 + idx * 60, 40, 40)
                        else:
                            pawn_rect = self.board.steps[pos]
                        if pawn_rect.collidepoint(mouse_x, mouse_y):
                            new_pos = self.pawn.move_pawn(idx, self.yut.result_text, is_player=True)
                            # 만약 이동 후 special_steps에 도달하면 분기 선택 UI 활성화
                            if new_pos in self.board.special_steps:
                                self.branch_selection = True
                                self.branch_options = self.board.special_steps[new_pos]
                                self.branch_pawn_index = idx
                                print(f"분기 선택 활성화: 말[{idx}]가 {new_pos}에서 {self.branch_options} 중 선택해야 합니다.")
                            else:
                                self.game_state.selecting_pawn = False
                            break

    def update(self):
        if self.holding_throw:
            self.yut.shake()
        self.blink_counter = (self.blink_counter + 1) % 30

    def draw(self):
        self.screen.fill(BLACK)
        self.board.draw(self.screen)
        self.ui.draw(self.screen)
        self.pawn.draw(self.screen, is_player=True)
        self.pawn.draw(self.screen, is_player=False)
        self.yut.draw(self.screen)
        if not self.game_state.started:
            self.start_button.draw(self.screen)
        else:
            self.throw_button.draw(self.screen)
        if self.game_state.selecting_pawn:
            font = pygame.font.SysFont('malgungothic', 40)
            # 분기 선택 UI가 활성화되면 문구를 "어디로 움직일까요?"로 표시
            if self.branch_selection:
                text = font.render("어디로 움직일까요?", True, WHITE)
            else:
                text = font.render("내보낼 말을 선택하세요", True, WHITE)
            self.screen.blit(text, (SCREEN_WIDTH//2 - 150, 300))
        if self.branch_selection:
            for option in self.branch_options:
                branch_rect = self.board.steps[option]
                if self.blink_counter < 15:
                    pygame.draw.rect(self.screen, (255, 0, 0), branch_rect, 5)
        pygame.display.flip()



    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

# -------------------------------
# 메인 실행부
# -------------------------------
if __name__ == "__main__":
    game = YutnoriGame()
    game.run()
