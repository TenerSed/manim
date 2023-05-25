from manim import *
from scipy.integrate import odeint
import numpy as np
import scipy as sp

def line(mob1, mob2, text, color=WHITE):
  l = Line(mob1.get_right(), mob2.get_left(), color=color)
  t = Text(text, font_size=25, color=color).next_to(l, UP)
  group = VGroup(l, t)
  return group
    
def free_line(position1, position2, text, color=WHITE, font_size=25):
  l = Line(position1, position2, color=color)
  t = Text(text, font_size=font_size, color=color).next_to(l, UP)
  group = VGroup(l, t)
  return group
    
def boxsh(mob1, text, color):
  b = Rectangle(height=1, width=2, color=WHITE, fill_color=color, fill_opacity=0.45).next_to(mob1, RIGHT*7)
  t = Text(text, font_size=25).move_to(b.get_center())
  group = VGroup(b, t)
  return group
    
def node(mob1):
  c = Circle(radius=0.35, color=WHITE, fill_color=WHITE, fill_opacity=0.35).next_to(mob1, RIGHT, buff=0)
  group = VGroup(c)
  return group

def free_line_fix(position1, position2, color=WHITE):
  l = Line(position1, position2, color=color)
  group = l
  return group

class page1(Scene):
  def construct(self):
    
    title = Text("PID Controller", color=BLUE,font_size=100)
    self.play(Write(title), run_time=7)
    self.wait()

#----------------------------BREAK----------------------------#

class PController(Scene):
  def construct(self):
    
    
    input_line = free_line(LEFT*6.75, LEFT*5.75, "Input", WHITE).shift(UP)
    node1 = node(input_line[0])
    
    prop_box = boxsh(node1, "Proportional", RED).shift(LEFT*0.5)
    error_line1 = line(node1[0], prop_box[0], "Error")
    act_box = boxsh(prop_box[0], "Plant", YELLOW).shift(RIGHT*0.5)
    prop_line = line(prop_box[0], act_box[0], "Prop Output")
    node3 = Circle(radius=0.35, color=WHITE, fill_color=WHITE, fill_opacity=0.35).next_to(act_box[0], RIGHT*4).shift(RIGHT)
    act_line = line(act_box[0], node3, "Result")
    final_out_line = free_line(node3, RIGHT*7+UP, "")
    
    down_line1= free_line(node3.get_bottom()+DOWN*2, node3, "")
    down_line2= free_line(node1.get_bottom()+DOWN*2, node1, "")
    loop_line = free_line(down_line1, down_line2, "LoopBack")
    
    self.play(Create(VGroup(input_line[0], node1, error_line1[0], prop_box[0], prop_line[0], act_box[0], act_line[0], node3, final_out_line[0], down_line1, down_line2, loop_line[0]), run_time=10))
    
    self.play(Create(VGroup(input_line[1], error_line1[1], prop_box[1], act_box[1], prop_line[1], act_line[1], final_out_line[1], loop_line[1]), run_time=10))
    
    proportion_eq = MathTex("R", "=", "K_p", "\\times", "e(t)").move_to(DOWN*2)
    
    self.play(Create(proportion_eq), run_time=3)
    
    self.wait(13)
    
#----------------------------BREAK----------------------------#

class PIController(Scene):
  def construct(self):
      
      input_line = free_line(LEFT*6.75, LEFT*5.75, "Input").shift(UP)
      node1 = node(input_line[0])
      
      prop_box = boxsh(node1, "Proportional", RED).shift(LEFT*0.5)
      integral_box = boxsh(node1, "Integral", GREEN).shift(LEFT*0.5+UP*1.5)
      
      error_line1 = line(node1[0], prop_box[0], "Error")
      error_line1[1] = error_line1[1].shift(LEFT*0.16)
      error_line2 = free_line(error_line1[0].get_center()+RIGHT*0.35, error_line1[0].get_center()+RIGHT*0.35+UP*1.5, "")
      error_line21 = free_line(error_line2[0].get_top(), integral_box[0].get_left(), "")
      
      integral_line1 = free_line(integral_box[0].get_right(), integral_box[0].get_right()+RIGHT*0.7, "")
      
      node2 = node(prop_box[0]).shift(RIGHT*0.35)
      integral_line2 = free_line(integral_line1[0].get_right(), node2[0].get_top(), "")
      
      act_box = boxsh(prop_box[0], "Plant", YELLOW).shift(RIGHT*1)
      
      prop_line = line(prop_box[0], node2, "")
      output_line = line(node2, act_box[0], "Output")
      node3 = Circle(radius=0.35, color=WHITE, fill_color=WHITE, fill_opacity=0.35).next_to(act_box[0], RIGHT*4).shift(RIGHT)
      act_line = line(act_box[0], node3, "Result")
      final_out_line = free_line(node3, RIGHT*7+UP, "")
      
      
      down_line1= free_line(node3.get_bottom()+DOWN*3, node3, "")
      down_line2= free_line(node1.get_bottom()+DOWN*3, node1, "")
      loop_line = free_line(down_line1, down_line2, "LoopBack")
      
      integration_eq = MathTex("R", "=", "K_p", "\\times", "e(t)", "+","K_i","\\times", r"\int_{0}^{t} e(\tau) d\tau").move_to(DOWN)
      
      self.add(VGroup(input_line, node1, error_line1,  prop_box, prop_line, node2, output_line, act_box, act_line, node3, final_out_line, down_line1, down_line2, loop_line))
      
      self.play(Create(VGroup(error_line2[0], error_line21[0], integral_box[0], integral_line1[0], integral_line2[0]), run_time=5))
      
      self.play(Create( integral_box[1]), run_time=2)
      
      self.play(Create(integration_eq), run_time=5)
      
      self.wait(5)
    
#----------------------------BREAK----------------------------#

class PIDController(Scene):
  def construct(self):
      input_line = free_line(LEFT*6.75, LEFT*5.75, "Input").shift(UP)
      node1 = node(input_line[0])
      
      prop_box = boxsh(node1, "Proportional", RED).shift(LEFT*0.5)
      integral_box = boxsh(node1, "Integral", GREEN).shift(LEFT*0.5+UP*1.5)
      
      derivative_box = boxsh(node1, "Derivative", BLUE).shift(LEFT*0.5+DOWN*1.5)
      
      error_line1 = line(node1[0], prop_box[0], "Error")
      error_line1[1] = error_line1[1].shift(LEFT*0.16)
      error_line2 = free_line(error_line1[0].get_center()+RIGHT*0.35, error_line1[0].get_center()+RIGHT*0.35+UP*1.5, "")
      error_line3 = free_line(error_line1[0].get_center()+RIGHT*0.35, error_line1[0].get_center()+RIGHT*0.35+DOWN*1.5, "")
      error_line21 = free_line(error_line2[0].get_top(), integral_box[0].get_left(), "")
      error_line31 = free_line(error_line3[0].get_bottom(), derivative_box[0].get_left(), "") 
      
      integral_line1 = free_line(integral_box[0].get_right(), integral_box[0].get_right()+RIGHT*0.7, "")
      derivative_line1 = free_line(derivative_box[0].get_right(), derivative_box[0].get_right()+RIGHT*0.7, "")
      
      node2 = node(prop_box[0]).shift(RIGHT*0.35)
      integral_line2 = free_line(integral_line1[0].get_right(), node2[0].get_top(), "")
      derivative_line2 = free_line(derivative_line1[0].get_right(), node2[0].get_bottom(), "")
      
      act_box = boxsh(prop_box[0], "Plant", YELLOW).shift(RIGHT*1)
      
      prop_line = line(prop_box[0], node2, "")
      output_line = line(node2, act_box[0], "Output")
      node3 = Circle(radius=0.35, color=WHITE, fill_color=WHITE, fill_opacity=0.35).next_to(act_box[0], RIGHT*4).shift(RIGHT)
      act_line = line(act_box[0], node3, "Result")
      final_out_line = free_line(node3, RIGHT*7+UP, "")
      
      
      down_line1= free_line(node3.get_bottom()+DOWN*4, node3, "")
      down_line2= free_line(node1.get_bottom()+DOWN*4, node1, "")
      loop_line = free_line(down_line1, down_line2, "LoopBack")
      
      derivative_eq = MathTex("R", "=", "K_p", "\\times", "e(t)", "+", "K_i","\\times", r"\int_{0}^{t} e(\tau) d\tau", "+", "K_d", "\\times", r"\frac{d}{dt}e(t)").move_to(DOWN*2)
      
      self.add(VGroup(input_line, node1, error_line1, error_line2,error_line21, prop_box, integral_box,  prop_line, node2,integral_line1,  integral_line2,  output_line, act_box, act_line, node3, final_out_line, down_line1, down_line2, loop_line))
      
  
      
      self.play(Create(VGroup(error_line3, error_line31, derivative_box[0] ,derivative_line1[0], derivative_line2[0]), run_time=5))
      self.play(Create(VGroup(derivative_box[1] ,derivative_line1[1], derivative_line2[1]), run_time=5))
      
      
      self.play(Create(derivative_eq), run_time=5)
      
      self.wait(14)
    
#----------------------------BREAK----------------------------#

class FootballField(Scene):
  def construct(self):
    field = Rectangle(height=5, width=12, color=GREEN, fill_color=GREEN, fill_opacity=0.35).shift(UP)
    vert_lines = VGroup()
    for i in range(0, 6):
      vert_lines.add(Line(field.get_bottom(), field.get_top(), color=WHITE).shift(LEFT*i*6/5))
      
    for i in range(1, 6):
      vert_lines.add(Line(field.get_bottom(), field.get_top(), color=WHITE).shift(RIGHT*i*6/5))
    
# Create the head
    head = Circle(radius=0.25, color=WHITE)
    head.move_to(UP)

    # Create the body
    body = Line(head.get_bottom(), DOWN*0.5)

        # Create the arms
    left_arm = Line(UP*0.6, LEFT * 0.7)
    right_arm = Line(UP*0.6, RIGHT * 0.7)

        # Create the legs
    left_leg = Line(body.get_bottom(), LEFT * 0.5+DOWN*1.5)
    right_leg = Line(body.get_bottom(), RIGHT * 0.5+DOWN*1.5)

        # Group all the parts together
    stick_figure = VGroup(head, body, left_arm, right_arm, left_leg, right_leg)
        # Position the stick figure
    stick_figure.scale(0.6)
    stick_figure.move_to(field.get_bottom()+DOWN*2.3+field.get_left())
    
    dist_err = always_redraw(lambda: free_line_fix(stick_figure.get_right(), field.get_right()+RIGHT*0.45+DOWN*3.8, YELLOW))
    
    left_tick = always_redraw(lambda: free_line_fix(dist_err[0].get_left()+UP*0.3, dist_err[0].get_left()+DOWN*0.3, YELLOW))
    
    right_tick =  free_line_fix(dist_err[0].get_right()+UP*0.3, dist_err[0].get_right()+DOWN*0.3, YELLOW)
    

        # Add the stick figure to the scene
    self.add(stick_figure)
    self.add(VGroup(field, dist_err, left_tick, right_tick))
    self.add(VGroup(vert_lines))
    self.wait(11)
    self.play(stick_figure.animate.shift(RIGHT*12),rate_func=rate_functions.smooth, run_time=7)
    self.wait(1)
   
    field_demo = VGroup(field, dist_err, left_tick, right_tick, stick_figure, vert_lines)
    
    self.play(FadeOut(VGroup(field_demo)))
    field_demo = field_demo.scale(0.5).shift(LEFT*4)
    
    field_demo[4] = field_demo[4].shift(LEFT*6)
    field_demo[1] = always_redraw(lambda: free_line_fix(stick_figure.get_right(), right_tick.get_left(), YELLOW))
    field_demo[2] = always_redraw(lambda: free_line_fix(field_demo[1].get_left()+UP*0.15, field_demo[1].get_left()+DOWN*0.15, YELLOW))
    
    #Begin Graph Creation
    pos_ax=Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1, .5],
            tips=False,
        ).scale(0.5).next_to(field_demo.get_center(),RIGHT,buff=3.5).shift(1.5*UP)
    vel_ax=Axes(
            x_range=[0, 10, 1],
            y_range=[0, 0.25, .125],
            tips=False,
        ).scale(0.5).next_to(pos_ax,DOWN)
       
    
    pos_func=lambda x: 1/(1+np.exp(5-x))
    vel_func=lambda x: 1/(1+np.exp(5-x))*(1-1/(1+np.exp(5-x)))

    time=ValueTracker(0)
    pos_curve=always_redraw(lambda:
                            pos_ax.plot(pos_func,x_range=[0,time.get_value()],color=YELLOW)
    )
    vel_curve=always_redraw(lambda:
                            vel_ax.plot(vel_func,
                          x_range=[0,time.get_value()],color=YELLOW)
    )
    
    pos_dot=always_redraw(lambda:
                          Dot(pos_ax.c2p(time.get_value(),pos_func(time.get_value())))
                          )
    vel_dot=always_redraw(lambda:
                          Dot(vel_ax.c2p(time.get_value(),vel_func(time.get_value())))
                          )
    pos_line=always_redraw(lambda:
      DashedLine(pos_ax.c2p(time.get_value(),0), 
                 pos_ax.c2p(time.get_value(),pos_func(time.get_value())))
    )
    vel_line=always_redraw(lambda:
      DashedLine(vel_ax.c2p(time.get_value(),0), 
                 vel_ax.c2p(time.get_value(),vel_func(time.get_value())))
    )

    target_line=DashedLine(pos_ax.c2p(0,1),pos_ax.c2p(10,1),color=RED)

    target_text=Tex("target",font_size=40,color=RED).next_to(target_line.get_center(),DOWN+3*LEFT)
    pos_text=always_redraw(lambda:
      Tex("position",font_size=30).next_to(pos_dot,0.5*RIGHT+0.2*UP)
    )
    vel_text=always_redraw(lambda:
      Tex("velocity",font_size=30).next_to(vel_dot,UP)
    )

    self.play(FadeIn(VGroup(field_demo)),
              *[Write(mob) for mob in 
                [pos_ax,vel_ax,pos_dot,vel_dot,target_line,pos_text,vel_text,target_text]])
    self.add(pos_curve,vel_curve,pos_line,vel_line)
    self.wait(3)
    self.play(stick_figure.animate.shift(RIGHT*6),
              time.animate.set_value(10),
              rate_func=rate_functions.smooth,run_time=4)
    self.wait(7)

#----------------------------BREAK----------------------------#

class DroneDemonstration(Scene):
  def construct(self):
# Create the body
        body = Rectangle(width=2, height=0.5, color=BLUE)

        # Create the arms
        arm1 = Rectangle(width=0.1, height=1.6, color=BLUE).shift(UP * 0.4 + LEFT * 1., )
        arm2 = Rectangle(width=0.1, height=1.6, color=BLUE).shift(UP * 0.4 + RIGHT * 1.)
        arm3 = Rectangle(width=0.1, height=1.6, color=BLUE).shift(DOWN * 0.4 + LEFT * 1.)
        arm4 = Rectangle(width=0.1, height=1.6, color=BLUE).shift(DOWN * 0.4 + RIGHT * 1.)
        
        # Create the propellers
        propeller1 = Circle(radius=0.3, color=RED, fill_opacity=1, fill_color=BLACK).shift(UP * 0.8 + LEFT * 1)
        propeller2 = Circle(radius=0.3, color=RED, fill_opacity=1, fill_color=BLACK).shift(UP * 0.8 + RIGHT * 1)
        propeller3 = Circle(radius=0.3, color=RED, fill_opacity=1, fill_color=BLACK).shift(DOWN * 0.8 + LEFT * 1)
        propeller4 = Circle(radius=0.3, color=RED, fill_opacity=1, fill_color=BLACK).shift(DOWN * 0.8 + RIGHT * 1)

        # Group all the parts together
        drone = VGroup(body, arm1, arm2, arm3, arm4, propeller1, propeller2, propeller3, propeller4).scale(0.6)

        height_line=free_line(UP*3.5+LEFT*6.75, UP*3.5+LEFT*3.75, "", YELLOW)
        h_text = Text("h", color=YELLOW, font_size= 35, slant=ITALIC).next_to(height_line, RIGHT).shift(LEFT*0.15)
        
        # Position the drone
        drone.move_to(LEFT*5.75+DOWN*3)
        
        # Add the drone to the scene
        self.add(VGroup(height_line, drone, h_text))
        
        #Graph Creation
        pos_ax=Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.179, .5],
            tips=False,
        ).scale(0.55).next_to(drone.get_center(),RIGHT*1.3,buff=3.5).shift(4.75*UP)
        vol_ax=Axes(
            x_range=[0.01, 10, 1],
            y_range=[0, 1.217, .5],
            tips=False,
        ).scale(0.55).next_to(pos_ax,DOWN*1.2)
        
        pos_func=lambda x: (sp.special.sic(1.6*x)[0])*(1/1.6)
    #si(1.6x)/1.6
        vol_func = lambda x: np.sin((1.6)*x)/((1.6)*x)+0.217
        

        time=ValueTracker(0.01)
        pos_curve=always_redraw(lambda:
          pos_ax.plot(pos_func, x_range=[0,time.get_value()],color=YELLOW))
        
        vol_curve=always_redraw(lambda:
          vol_ax.plot(vol_func, x_range=[0.01,time.get_value()],color=YELLOW))
    
        pos_dot=always_redraw(lambda:
          Dot(pos_ax.c2p(time.get_value(),pos_func(time.get_value())))
        )
        vol_dot=always_redraw(lambda:
          Dot(vol_ax.c2p(time.get_value(),vol_func(time.get_value()))))
        pos_line=always_redraw(lambda:
      DashedLine(pos_ax.c2p(time.get_value(),0), 
                 pos_ax.c2p(time.get_value(),pos_func(time.get_value())))
    )
        vol_line=always_redraw(lambda:
      DashedLine(vol_ax.c2p(time.get_value(),0), 
                 vol_ax.c2p(time.get_value(),vol_func(time.get_value())))
    )

        target_line=DashedLine(pos_ax.c2p(0,1.179),pos_ax.c2p(10,1.179),color=RED)

        target_text=Tex("target",font_size=40,color=RED).next_to(target_line.get_center(),DOWN+3*LEFT)
        pos_text=always_redraw(lambda:
      Tex("position",font_size=30).next_to(pos_dot,0.5*RIGHT+0.2*UP))
        vol_text=always_redraw(lambda:
      Tex("voltage",font_size=30).next_to(vol_dot,UP*0.6+RIGHT*0.7))
        
        self.add(VGroup(pos_ax,vol_ax,pos_dot,vol_dot,target_line,pos_text,vol_text,target_text, pos_line, vol_line, pos_curve, vol_curve))
      
        #Graph END
        
        self.wait(15)
        self.play(drone.animate.shift(UP*5.75), time.animate.set_value(1.6), rate_func=rate_functions.smooth, run_time=4)
        
        
        g_arrow = always_redraw(lambda: Arrow(start=drone.get_bottom(), end=drone.get_bottom()+DOWN*1.5, color=WHITE))
        
        g_text = always_redraw(lambda: Text("g", color=WHITE, font_size= 35, slant=ITALIC).next_to(g_arrow, RIGHT).shift(LEFT*0.15))
        self.play(FadeIn(VGroup(g_arrow,g_text)))
        
        
        self.play(drone.animate.shift(DOWN*1.75), time.animate.set_value(3), rate_func=rate_functions.ease_in_cubic, run_time=2)
        self.play(drone.animate.shift(DOWN*2), time.animate.set_value(4), rate_func=rate_functions.ease_out_cubic, run_time=2)
        
        p_arrow = always_redraw(lambda: Arrow(start=drone.get_top(), end=drone.get_top()+UP*1.5, color=RED))
        p_text = always_redraw(lambda: Text("Pp", color=RED, font_size= 35, slant=ITALIC).next_to(p_arrow, RIGHT).shift(LEFT*0.15))
        
        self.play(FadeIn(VGroup(p_arrow,p_text)))
        self.play(drone.animate.shift(UP*1.5), time.animate.set_value(6),rate_func=rate_functions.smooth, run_time=2)
        self.play(drone.animate.shift(DOWN*1), time.animate.set_value(7),rate_func=rate_functions.smooth, run_time=2)
        self.play(drone.animate.shift(UP*0.5), time.animate.set_value(8),rate_func=rate_functions.smooth, run_time=2)
        self.play(drone.animate.shift(DOWN*.25), time.animate.set_value(10),rate_func=rate_functions.smooth, run_time=2)
        
        steady_state = free_line(drone.get_top()+UP*0.4+LEFT, drone.get_top()+RIGHT*3+UP*0.4, "Steady State Error", RED, 30)
        
        
        self.play(FadeOut(VGroup(g_arrow,g_text,p_arrow,p_text)))
        self.play(FadeIn(steady_state), run_time=2)
        self.wait(16)
        
        err_line = free_line(UP*0.95, UP*1.7, "").shift(RIGHT*1.45+UP*1.7)
        err_line_text = Tex("Error", font_size=30).next_to(err_line, DOWN)
        self.play(FadeIn(VGroup(err_line, err_line_text)), FadeOut(target_text))
        self.wait(2)
        
        proportion_eq = MathTex("R", "=", "K_p", "\\times", "e(t)").move_to(DOWN+RIGHT*1.5)
        integration_portion = MathTex("+", "K_i", "\\int_0^t", "e(\\tau)", "d\\tau").next_to(proportion_eq, RIGHT)
        self.play(Create(proportion_eq), FadeOut(VGroup(err_line, err_line_text)), run_time=2)
        
        anti_area = pos_ax.get_area(pos_curve, x_range=(0,time.get_value()), color=BLACK, opacity=1)
        
        area = Rectangle(height=3.25, width=6.5, color=YELLOW, fill_opacity=0.3).move_to(UP*1.75+RIGHT*2.15)
        
        self.play(FadeIn(area, anti_area), run_time=2)
        self.wait(3)
        
        
        self.play(Create(integration_portion),FadeOut(VGroup( area, anti_area)), run_time=2)
        
        self.wait(3)
        
        p_arrow = always_redraw(lambda: Arrow(start=drone.get_top()+LEFT*0.5, end=height_line.get_bottom()+LEFT*1, color=RED))
        p_text = always_redraw(lambda: Text("Pp", color=RED, font_size= 35, slant=ITALIC).next_to(p_arrow, RIGHT).shift(LEFT*0.15))
        
        self.play(FadeOut(VGroup(proportion_eq, steady_state)),FadeIn(VGroup(p_arrow, p_text, g_arrow, g_text)), run_time=2)
        
        pi_arrow = always_redraw(lambda: Arrow(start=drone.get_top()+RIGHT*0.5, end=drone.get_top()+UP*1.5+RIGHT*0.5, color=PURPLE))
        pi_text = always_redraw(lambda: Text("Pi", color=PURPLE, font_size= 35, slant=ITALIC).next_to(pi_arrow, RIGHT).shift(LEFT*0.15)) 
        
        self.play(FadeOut(integration_portion), FadeIn(VGroup(pi_arrow, pi_text)), run_time=3)
        
        self.play(drone.animate.shift(UP*1.5),height_line.animate.shift(DOWN*1.5), h_text.animate.shift(DOWN*1.5) , run_time=6)
        
        self.remove(p_arrow, p_text)
        
        self.wait(1)
        

#----------------------------BREAK----------------------------#

class DroneDemoDerivative(Scene):
  def construct(self):
    body = Rectangle(width=2, height=0.5, color=BLUE)

    # Create the arms
    arm1 = Rectangle(width=0.1, height=1.6, color=BLUE).shift(UP * 0.4 + LEFT * 1., )
    arm2 = Rectangle(width=0.1, height=1.6, color=BLUE).shift(UP * 0.4 + RIGHT * 1.)
    arm3 = Rectangle(width=0.1, height=1.6, color=BLUE).shift(DOWN * 0.4 + LEFT * 1.)
    arm4 = Rectangle(width=0.1, height=1.6, color=BLUE).shift(DOWN * 0.4 + RIGHT * 1.)
        
        # Create the propellers
    propeller1 = Circle(radius=0.3, color=RED, fill_opacity=1, fill_color=BLACK).shift(UP * 0.8 + LEFT * 1)
    propeller2 = Circle(radius=0.3, color=RED, fill_opacity=1, fill_color=BLACK).shift(UP * 0.8 + RIGHT * 1)
    propeller3 = Circle(radius=0.3, color=RED, fill_opacity=1, fill_color=BLACK).shift(DOWN * 0.8 + LEFT * 1)
    propeller4 = Circle(radius=0.3, color=RED, fill_opacity=1, fill_color=BLACK).shift(DOWN * 0.8 + RIGHT * 1)

        # Group all the parts together
    drone = VGroup(body, arm1, arm2, arm3, arm4, propeller1, propeller2, propeller3, propeller4).scale(0.6)

    height_line=free_line(UP*3.5+LEFT*6.75, UP*3.5+LEFT*3.75, "", YELLOW)
    h_text = Text("h", color=YELLOW, font_size= 35, slant=ITALIC).next_to(height_line, RIGHT).shift(LEFT*0.15)
    
    height = VGroup(height_line, h_text)
        
        # Position the drone
    drone.move_to(LEFT*5.75+DOWN*3)
        
        # Add the drone to the scene
    self.add(VGroup(height_line, drone, h_text))
 
    pos_ax=Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.5, .5],
            tips=False,
        ).scale(0.55).next_to(drone.get_center(),RIGHT*1.3,buff=3.5).shift(4.75*UP)
    vol_ax=Axes(
            x_range=[0.01, 10, 1],
            y_range=[0, 1.434, .5],
            tips=False,
        ).scale(0.55).next_to(pos_ax,DOWN*1.2)
        
    pos_func= lambda x: (sp.special.sici(1.6*x)[0])*(1/1.6)
        
    vol_func = lambda x: np.sin((1.6)*x)/((1.6)*x)+0.434
        

    time=ValueTracker(0.01)
    pos_curve=always_redraw(lambda:
      pos_ax.plot(pos_func, x_range=[0,time.get_value()],color=YELLOW))
        
    vol_curve=always_redraw(lambda:
      vol_ax.plot(vol_func, x_range=[0.01,time.get_value()],color=BLUE))
    
    pos_dot=always_redraw(lambda:
          Dot(pos_ax.c2p(time.get_value(),pos_func(time.get_value())))
        )
    vol_dot=always_redraw(lambda:
          Dot(vol_ax.c2p(time.get_value(),vol_func(time.get_value()))))
    pos_line=always_redraw(lambda:
      DashedLine(pos_ax.c2p(time.get_value(),0), 
                 pos_ax.c2p(time.get_value(),pos_func(time.get_value())))
    )
    vol_line=always_redraw(lambda:
      DashedLine(vol_ax.c2p(time.get_value(),0), 
                 vol_ax.c2p(time.get_value(),vol_func(time.get_value())))
    )

    target_line=DashedLine(pos_ax.c2p(0,1),pos_ax.c2p(10,1),color=RED)

    tangent_line=always_redraw(lambda: TangentLine(pos_curve, alpha=time.get_value()/10, d_alpha=0.01, length=1.5, color=BLUE))
    integral_eq = MathTex("R", "=", "K_p", "\\times", "e(t)", "+", "K_i","\\times", r"\int_{0}^{t} e(\tau) d\tau").scale(0.7).move_to(LEFT*4.5+DOWN*2)
    derivative_portion = MathTex("+", "K_d", "\\times", r"\frac{d}{dt}e(t)").scale(0.7).move_to(RIGHT*3.5+UP)

    target_text=Tex("target",font_size=40,color=RED).next_to(target_line.get_center(),DOWN+3*LEFT)
    pos_text=always_redraw(lambda:
      Tex("position",font_size=30).next_to(pos_dot,0.5*RIGHT+0.2*UP))
    vol_text=always_redraw(lambda:
      Tex("voltage",font_size=30).next_to(vol_dot,UP*0.6+RIGHT*0.7))
        
    slope_explain = MathTex(r"\frac{de(t)}{dt} = - \frac{dp(t)}{dt}", color=WHITE).scale(0.8).shift(RIGHT*3.5+UP*1)
        
    self.add(VGroup(pos_ax,vol_ax,pos_dot,vol_dot,target_line,pos_text,vol_text,target_text.shift(LEFT*0.4), pos_line, vol_line, pos_curve, vol_curve, tangent_line)) 
    
    self.wait(4)
    self.play(drone.animate.shift(UP*5.25), height.animate.shift(DOWN*2), time.animate.set_value(1.8), run_time = 4)
    self.play(drone.animate.shift(DOWN*1.5), time.animate.set_value(3.9),rate_func=rate_functions.smooth, run_time=2)
    self.play(drone.animate.shift(UP*1), time.animate.set_value(5.7),rate_func=rate_functions.smooth, run_time=2)
    self.play(drone.animate.shift(DOWN*0.5), time.animate.set_value(7.5),rate_func=rate_functions.smooth, run_time=2)
    self.play(drone.animate.shift(UP*0.25), time.animate.set_value(10),rate_func=rate_functions.smooth, run_time=2)
    self.wait(7)
    self.play(Create(slope_explain), run_time=2)
    self.wait(7)
    self.play(Uncreate(slope_explain), Create(integral_eq),  run_time=2)
    self.play(Create(derivative_portion), run_time=2)
    self.wait(2)
    self.play(derivative_portion.animate.move_to(integral_eq).shift(DOWN*0.6))
    self.wait(3)
    
    self.play(FadeOut(VGroup(pos_dot,vol_dot,pos_text,vol_text, pos_line, vol_line, pos_curve, vol_curve, tangent_line)))
    self.wait(2)
    
    total_equation = VGroup(integral_eq, derivative_portion)
    
    pos_func=lambda x: 1/(1+np.exp(5-x))
    vol_func=lambda x: 1-np.exp(-x)
    time=ValueTracker(0.01)
    self.play(FadeOut(total_equation),drone.animate.shift(DOWN*3.75), height.animate.shift(UP*2), run_time=2)
    self.wait(0.2)
    
    self.add(VGroup(pos_dot,vol_dot,vol_text, pos_line, vol_line, pos_curve, vol_curve, tangent_line)) 
    
    self.play(drone.animate.shift(UP*5), time.animate.set_value(10), run_time=5)
    self.wait(22)

#----------------------------BREAK----------------------------#

class IntegralWindup(Scene):
  def construct(self):
    body = Rectangle(width=2, height=0.5, color=BLUE)

    # Create the arms
    arm1 = Rectangle(width=0.1, height=1.6, color=BLUE).shift(UP * 0.4 + LEFT * 1., )
    arm2 = Rectangle(width=0.1, height=1.6, color=BLUE).shift(UP * 0.4 + RIGHT * 1.)
    arm3 = Rectangle(width=0.1, height=1.6, color=BLUE).shift(DOWN * 0.4 + LEFT * 1.)
    arm4 = Rectangle(width=0.1, height=1.6, color=BLUE).shift(DOWN * 0.4 + RIGHT * 1.)
        
        # Create the propellers
    propeller1 = Circle(radius=0.3, color=RED, fill_opacity=1, fill_color=BLACK).shift(UP * 0.8 + LEFT * 1)
    propeller2 = Circle(radius=0.3, color=RED, fill_opacity=1, fill_color=BLACK).shift(UP * 0.8 + RIGHT * 1)
    propeller3 = Circle(radius=0.3, color=RED, fill_opacity=1, fill_color=BLACK).shift(DOWN * 0.8 + LEFT * 1)
    propeller4 = Circle(radius=0.3, color=RED, fill_opacity=1, fill_color=BLACK).shift(DOWN * 0.8 + RIGHT * 1)

        # Group all the parts together
    drone = VGroup(body, arm1, arm2, arm3, arm4, propeller1, propeller2, propeller3, propeller4).scale(0.6)

    height_line=free_line(UP*3.5+LEFT*6.75, UP*3.5+LEFT*3.75, "", YELLOW)
    h_text = Text("h", color=YELLOW, font_size= 35, slant=ITALIC).next_to(height_line, RIGHT).shift(LEFT*0.15)
    
    height = VGroup(height_line, h_text)
        
        # Position the drone
    drone.move_to(LEFT*5.75+DOWN*3)
        
        # Add the drone to the scene
    
    
    # Create the head
    head = Circle(radius=0.25, color=WHITE)
    head.move_to(UP)

    # Create the body
    body = Line(head.get_bottom(), DOWN*0.5)

        # Create the arms
    left_arm = Line(UP*0.4, LEFT * 0.9+UP*0.4)
    right_arm = Line(UP*0.4, RIGHT * 0.7)

        # Create the legs
    left_leg = Line(body.get_bottom(), LEFT * 0.5+DOWN*1.5)
    right_leg = Line(body.get_bottom(), RIGHT * 0.5+DOWN*1.5)

        # Group all the parts together
    stick_figure = VGroup(head, body, left_arm, right_arm, left_leg, right_leg)
        # Position the stick figure
    stick_figure.scale(0.6)
    stick_figure.move_to(LEFT+DOWN)
    stick_figure = stick_figure.scale(1.2).shift(LEFT*3.4+DOWN*1.5)

    self.add(VGroup(height_line, drone, h_text))
    p_arrow = always_redraw(lambda: Arrow(start=drone.get_top(), end=drone.get_top()+UP*1.5, color=RED))
    p_text = always_redraw(lambda: Text("P", color=RED, font_size= 35, slant=ITALIC).next_to(p_arrow, RIGHT).shift(LEFT*0.15))
    p_unit = VGroup(p_arrow, p_text)
    g_arrow = always_redraw(lambda: Arrow(start=drone.get_bottom(), end=drone.get_bottom()+DOWN*1.5, color=WHITE))
    g_text = always_redraw(lambda: Text("g", color=WHITE, font_size= 35, slant=ITALIC).next_to(g_arrow, RIGHT).shift(LEFT*0.15))
    g_unit = VGroup(g_arrow, g_text)
    c_arrow = Arrow(start=stick_figure[2].get_left(), end=stick_figure.get_left()+DOWN*1., color=YELLOW)
    c_text = Text("s", color=YELLOW, font_size= 35, slant=ITALIC).next_to(c_arrow, RIGHT).shift(LEFT*0.15+UP*0.1)
    c_unit = VGroup(c_arrow, c_text)
    
    pos_ax=Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.5, .5],
            tips=False,
        ).scale(0.55).next_to(drone.get_center(),RIGHT*1.3,buff=3.5).shift(4.75*UP)
    vol_ax=Axes(
            x_range=[0.01, 10, 0.5],
            y_range=[0, 1.434, .5],
            tips=False,
        ).scale(0.55).next_to(pos_ax,DOWN*1.2)
        
    pos_func= lambda x: (sp.special.sici(1.6*(x-2))[0])*(1/1.6)*np.heaviside(x-2,1)
        
    vol_func = lambda x: np.exp(-1*((5-x)/3)**(10))
       
    def rec(x, start, end):
      return (np.heaviside(x-start,1)-np.heaviside(x-end,1))
    
    ip = [0,1,2,2.8,3.383,3.783,4,4.1,5]
    y_intceps = [0,2,-2,3.6,-3.166,4.4,-3.6,0.5]
    
    def vol_func_line_gay(x):
      result = 0
      s = 1
      for i in range(0,len(ip)-2):
        result += (y_intceps[i]+s*x)*rec(x,ip[i],ip[i+1])
        s = -s
      result += y_intceps[-1]*rec(x,ip[-2],ip[-1])
      return result 

    zigger = lambda x: vol_func_line_gay(x/2.001) + 0.2

    time=ValueTracker(0.01)
    pos_curve=always_redraw(lambda:
      pos_ax.plot(pos_func, x_range=[0,time.get_value()],color=YELLOW))
    
    
        
    vol_curve=always_redraw(lambda:
      vol_ax.plot(zigger, x_range=[0.01,time.get_value()],color=BLUE))
    
    pos_dot=always_redraw(lambda:
          Dot(pos_ax.c2p(time.get_value(),pos_func(time.get_value())))
        )
    vol_dot=always_redraw(lambda:
          Dot(vol_ax.c2p(time.get_value(),zigger(time.get_value()))))
    pos_line=always_redraw(lambda:
      DashedLine(pos_ax.c2p(time.get_value(),0), 
                 pos_ax.c2p(time.get_value(),pos_func(time.get_value())))
    )
    vol_line=always_redraw(lambda:
      DashedLine(vol_ax.c2p(time.get_value(),0), 
                 vol_ax.c2p(time.get_value(),zigger(time.get_value())))
    )
    
    target_line=DashedLine(pos_ax.c2p(0,1),pos_ax.c2p(10,1),color=RED)
    max_volts = DashedLine(vol_ax.c2p(0,0.8),vol_ax.c2p(10,0.8),color=GREEN)
    vol_text=always_redraw(lambda:
      Tex("voltage",font_size=30).next_to(vol_dot,UP*0.6+RIGHT*0.7))
    target_text=Tex("target",font_size=40,color=RED).next_to(target_line.get_center(),DOWN+3*LEFT)
    
    max_volts_text=MathTex("V max",font_size=40,color=GREEN).next_to(max_volts.get_center(),DOWN+3*LEFT)
    pos_text=always_redraw(lambda:
      Tex("position",font_size=30).next_to(pos_dot,0.5*RIGHT+0.2*UP))

    self.add(VGroup(pos_ax,vol_ax,pos_dot,vol_dot,target_line,max_volts, max_volts_text,pos_text,vol_text,target_text.shift(LEFT*0.4), pos_line, vol_line, pos_curve, vol_curve))
    
    self.wait(12)
    
    self.play(FadeIn(VGroup(p_arrow,p_text,g_arrow,g_text)),run_time=2)
    self.play(drone.animate.shift(UP*1.3), run_time=2)
    self.play(FadeIn(stick_figure), run_time=0.5)
    self.play(Create(VGroup(c_arrow, c_text)), time.animate.set_value(2), run_time=2)
    
    self.play(FadeOut(VGroup(p_arrow,p_text)))
    
    p_arrow = always_redraw(lambda: Arrow(start=drone.get_top(), end=drone.get_top()+UP*2, color=RED))
    p_text = always_redraw(lambda: Text("P", color=RED, font_size= 40, slant=ITALIC).next_to(p_arrow, RIGHT).shift(LEFT*0.15)) 
    
    
    self.play(FadeIn(VGroup(p_arrow,p_text)))
    
    self.wait(2)
    
    self.play(FadeOut(VGroup(stick_figure, c_arrow, c_text)))
    
    self.play(height.animate.scale(0.75).shift(DOWN*2), drone.animate.scale(0.75).shift(UP*4.5), time.animate.set_value(4),run_time=2)
    self.wait()
    self.play(drone.animate.shift(DOWN*2), time.animate.set_value(5.7),rate_func=rate_functions.smooth, run_time=2)
    self.play(drone.animate.shift(UP*1), time.animate.set_value(7.5),rate_func=rate_functions.smooth, run_time=2)
    self.play(drone.animate.shift(DOWN*0.3), time.animate.set_value(10),rate_func=rate_functions.smooth, run_time=2)
    self.wait(2)
    
    self.play(FadeOut(VGroup(p_arrow,p_text)))
    p_arrow = always_redraw(lambda: Arrow(start=drone.get_top(), end=drone.get_top()+UP*1.5, color=RED))
    p_text = always_redraw(lambda: Text("P", color=RED, font_size= 35, slant=ITALIC).next_to(p_arrow, RIGHT).shift(LEFT*0.15)) 
    self.play(FadeIn(VGroup(p_arrow,p_text)))
    
    target_func = lambda x: 1
    target_curve = always_redraw(lambda: pos_ax.plot(target_func, x_range=[0,time.get_value()],color=RED))
    
    
    area1 = pos_ax.get_area(pos_curve, x_range=(0,time.get_value()), color=ORANGE, opacity=0.3, bounded_graph=target_curve)
    area_text = Text("Area", font_size=30, color = ORANGE).next_to(area1, LEFT).shift(RIGHT*1.55)
    
    integral_point1 = Arrow(start=LEFT*3+DOWN*3, end=DOWN*1.2+RIGHT*0.35, color=WHITE)
    integral_point2 = Arrow(start=LEFT*3+DOWN*3, end=DOWN*1.5+RIGHT*2.75, color=WHITE)
    
    self.play(FadeIn(area1), FadeIn(area_text), FadeOut(target_text))
    self.play(FadeIn(VGroup(integral_point1, integral_point2)), FadeOut(max_volts_text))
    
    int_wind_description1 = Text("Integral Windup: These areas", font_size=20).move_to(DOWN*3+LEFT*4.7)
    int_wind_description2 = Text("describe Voltages higher than possible", font_size=20).next_to(int_wind_description1, DOWN) 
    
    self.play(Write(VGroup(int_wind_description1,int_wind_description2)), run_time=2)
    
    self.wait(29)
    