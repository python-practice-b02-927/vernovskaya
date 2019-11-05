import math
import tkinter as tk
import time
from random import randrange as rnd, choice


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Ball():
    def __init__(self):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = -10
        self.y = -10
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 10

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.y > 550 or self.y < 0:
            if self.y > 550:
                self.y = 550

            elif self.y < 0:
                self.y = 1
            self.vx = (0.7) * self.vx
            self.vy = (-0.5) * self.vy
            self.live -= 1

        if self.x < 0 or self.x > 800:
            if self.x < 0:
                self.x = 1

            if self.x > 800:
                self.x = 799
            self.vx = -self.vx
            self.live -= 1

        self.x += self.vx
        self.y -= self.vy
        self.vy -= 2
        self.set_coords()

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 < (self.r + obj.r)**2:
            return True
        else:
            return False


class Gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x = 20
        self.y = 450
        self.id = canv.create_line(self.x, self.y, self.x+30, self.x-30, width=7)

    def fire2_start(self, event):
        print('button')
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet

        bullet += 1
        new_ball = Ball()
        new_ball.x = self.x
        new_ball.y = self.y
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))

        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')

        else:
            canv.itemconfig(self.id, fill='black')

        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1

            canv.itemconfig(self.id, fill='orange')

        else:
            canv.itemconfig(self.id, fill='black')

    def move_up(self, event):
        print('move up')
        self.y -= 10
        canv.coords(self.id, self.x, self.y, self.x+30, self.x-30)

    def move_down(self, event):
        print('move down')
        self.y += 10
        canv.coords(self.id, self.x, self.y, self.x+30, self.x-30)


class Target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.new_target()
        self.vtx = 0
        self.vty = 0
        self.color = 'red'

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        self.vtx = rnd(-3, 0)
        self.vty = rnd(-3, 3)
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        color = self.color = 'red'
        canv.itemconfig(self.id, fill=color, outline='black')

    def hit(self):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)

    def move(self):
        if self.y > 600 or self.y < 0:
            self.vty = (-1)*self.vty

            if self.y > 600:
                self.y = 590

            elif self.y < 0:
                self.y = 10

        if self.x < 0 or self.x > 800:
            self.vtx = (-1)*self.vtx
            if self.x < 0:
                self.x = 10

            if self.x > 800:
                self.x = 780

        self.x += self.vtx
        self.y += self.vty
        self.set_coords()


t1 = Target()
t2 = Target()
score = 0
scoretext = canv.create_text(30, 30, text=score, font='28')
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    print('new game')
    global Gun, t1, t2, screen1, balls, bullet, score
    t1.new_target()
    t2.new_target()
    bullet = 0
    balls = []
    canv.bind('<Up>', g1.move_up)
    canv.focus_set()
    canv.bind('<Down>', g1.move_down)
    canv.focus_set()
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    t1.live = 1
    t2.live = 1

    while g1.f2_on == 0:
        t1.move()
        t2.move()
        canv.update()
        time.sleep(0.03)

    while (t1.live or t2.live) or balls:
        canv.itemconfig(screen1, text='')
        canv.bind('<Button-1>', g1.fire2_start)
        canv.bind('<ButtonRelease-1>', g1.fire2_end)
        for b in balls:
            canv.update()
            canv.itemconfig(scoretext, text=score)
            b.move()
            if b.hittest(t2) and t2.live:
                score += 1
                t2.live = 0
                t2.hit()
                canv.itemconfig(t2.id, fill='white', outline='white')
                print('hit target 2')
                canv.bind('<Up>', g1.move_up)
                canv.focus_set()
                canv.bind('<Down>', g1.move_down)
                canv.focus_set()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')

            if b.hittest(t1) and t1.live:
                score += 1
                t1.live = 0
                t1.hit()
                canv.itemconfig(t1.id, fill='white', outline='white')
                print('hit target 1')
                canv.bind('<Up>', g1.move_up)
                canv.focus_set()
                canv.bind('<Down>', g1.move_down)
                canv.focus_set()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')

            if b.live == 0:
                canv.delete(b.id)
                balls.remove(b)

        canv.update()
        t1.move()
        t2.move()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()

    canv.itemconfig(
                    screen1,
                    text='Вы уничтожили цели за ' +
                    str(bullet) +
                    ' выстрелов')
    canv.delete(Gun)
    canv.update()
    canv.itemconfig(scoretext, text=score)
    print('new target')
    root.after(750, new_game)


new_game()

tk.mainloop()
