from manim import *

# class Animation1(Scene):
#   def construct(self):
    
#     name = Text("Sheeesh", color=BLUE, font_size=100).to_edge(UL, buff=0.5)
#     circ = Circle(radius=1, color=BLUE).shift(LEFT * 3)
#     sq = Square(side_length=2, color=RED, fill_color=RED, fill_opacity=0.4).to_edge(DR, buff=0.2)
#     tri = Triangle(color=GREEN,fill_color = GREEN, fill_opacity=0.3).scale(1.45).shift(UP * 2.5 + RIGHT * 3.5)
    
#     self.play(Create(circ))
#     self.play(Write(name))
#     self.play(DrawBorderThenFill(sq), run_time=2)
#     self.play(DrawBorderThenFill(tri), run_time=1)
#     self.wait()

# class Animation2(Scene):
#   def construct(self):
    
#     name = Text("Helicopter Helicopter", color=RED, font_size=75).to_edge(UP, buff=0.5)
    
#     body = Rectangle(height=1.5, width=3, color=BLUE, fill_color=BLUE, fill_opacity=1)
    
#     prop1 = Circle(radius=0.5, color=DARK_BLUE, fill_color=DARK_BLUE, fill_opacity=1).shift(LEFT * 1.5 + UP * 0.75)
    
#     prop2 = Circle(radius=0.5, color=DARK_BLUE, fill_color=DARK_BLUE, fill_opacity=1).shift(RIGHT * 1.5 + UP * 0.75)
    
#     prop3 = Circle(radius=0.5, color=DARK_BLUE, fill_color=DARK_BLUE, fill_opacity=1).shift(LEFT * 1.5 + DOWN * 0.75)
    
#     prop4 = Circle(radius=0.5, color=DARK_BLUE, fill_color=DARK_BLUE, fill_opacity=1).shift(RIGHT * 1.5 + DOWN * 0.75)
    

    
#     self.play(Write(name), run_time=2)
#     self.play(DrawBorderThenFill(body), run_time=1)
#     self.play(DrawBorderThenFill(prop1), run_time=0.5)
#     self.play(DrawBorderThenFill(prop2), run_time=0.5)
#     self.play(DrawBorderThenFill(prop3), run_time=0.5)
#     self.play(DrawBorderThenFill(prop4), run_time=0.5)

    
#     self.play(
#       prop1.animate.shift(UP*2,RIGHT*4),
#       prop2.animate.shift(UP*2,RIGHT*4), 
#       prop3.animate.shift(UP*2,RIGHT*4), 
#       prop4.animate.shift(UP*2,RIGHT*4),
#       body.animate.shift(UP*2,RIGHT*4),
#       name.animate.shift(LEFT*4, UP*0.5).scale(0.65),
#       run_time=1)
    
#     # in order to create an active updating arrow, you need to use always_redraw (Updaters)
#     # You can also pass multiple arguments into the Create function to render multiple things without multiple lines
#     #buff is used to leave space
#     # the body.getleft and name.get_right are used to get the position of the objects (Getters)
#     sampleArrow = always_redraw(lambda: Line(end=body.get_left(), start=name.get_right(), buff=0.1, color=WHITE).add_tip())
#     self.play(Create(sampleArrow), run_time=1)
    
#     self.wait(0.35)
    
#     self.play(
#       prop1.animate.shift(DOWN*4),
#       prop2.animate.shift(DOWN*4), 
#       prop3.animate.shift(DOWN*4), 
#       prop4.animate.shift(DOWN*4),
#       body.animate.shift(DOWN*4),
#       run_time=1)
    
#     self.play(
#       body.animate.shift(UP*2),
#       prop1.animate.shift(UP*2),
#       prop2.animate.shift(UP*2),
#       prop3.animate.shift(UP*2),
#       prop4.animate.shift(UP*2),
#     )
    
#     self.wait(1)


# use surrounding rectangle to create a box around an object
# use always_redraw to update the box


# class Animation3(Scene):
#   def construct(self):
    
#     num = MathTex("y=mx+b")
#     box = always_redraw(lambda: 
#       SurroundingRectangle(
#         num, 
#         buff=0.3, 
#         color=WHITE, 
#         fill_color=ORANGE,
#         fill_opacity=0.5
#       )
#     )
#     name = always_redraw(lambda: 
#       Tex(
#         "Slope Intercept Form", 
#         color=BLUE, 
#         font_size=50
#       ).next_to(
#         box, 
#         DOWN, 
#         buff=0.3
#       )
#     )
#     self.play(Create(VGroup(num, box, name)))
#     self.play(num.animate.shift(RIGHT*2), run_time=2)
#     self.wait()
    
# class Animation4(Scene):
#   def construct(self):
    
#     k = ValueTracker(0)
#     num = always_redraw(lambda: DecimalNumber().set_value(k.get_value()))
    
#     self.play(FadeIn(num))
#     self.wait()
#     self.play(k.animate.set_value(10), run_time=4, rate_func=smooth)
    
#     #liner, smooth
#     self.wait()
  
class Animation5(Scene):

  
  def construct(self):
    
    plane = NumberPlane(x_range=[-4,4,2], x_length=7,y_range=[0.16,4],y_length=8).to_edge(DOWN).add_coordinates()
    
    #create a graph which takes in the plane and uses a lambda function and the plane to create a graph
    # the lambda function is used to create a function that takes in x and returns x^2
    # the plane is used to create the graph
    parab = always_redraw(lambda: plane.get_graph(lambda x: x**2))
  
    
    self.play(DrawBorderThenFill(plane), run_time=2)
    self.play(Create(parab))
    self.wait()