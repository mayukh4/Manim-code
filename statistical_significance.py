from manim import *
import numpy as np
from scipy import stats

class StatisticalSignificance(Scene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        
        # Introduction
        self.introduction()
        
        # Explain normal distribution
        self.explain_normal_distribution()
        
        # Explain sigma levels with areas
        self.explain_sigma_levels()
        
        # Real-world examples
        self.real_world_examples()
        
        # Conclusion
        self.conclusion()

    def introduction(self):
        title = Text("Understanding Statistical Significance", font="Arial", color=BLUE_C, font_size=40)
        title.scale(1.0)
        subtitle = Text("The meaning of σ (sigma) in scientific observations", font="Arial", color=LIGHT_GRAY, font_size=24)
        subtitle.scale(0.8)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        
        group = VGroup(title, subtitle)
        self.play(FadeOut(group))

    def explain_normal_distribution(self):
        title = Text("The Normal Distribution", font="Arial", color=BLUE_C, font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create axes for the normal distribution
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.45, 0.1],
            x_length=10,
            y_length=5,
            axis_config={"color": LIGHT_GRAY},
        )
        
        # Add labels to axes with reduced font size
        x_label = Text("Value", font_size=20, color=LIGHT_GRAY).next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = Text("Probability Density", font_size=20, color=LIGHT_GRAY).next_to(axes.y_axis, LEFT, buff=0.3).rotate(90 * DEGREES)
        axes_labels = VGroup(x_label, y_label)
        
        # Plot the normal distribution
        normal_dist = axes.plot(lambda x: stats.norm.pdf(x, 0, 1), color=BLUE_C)
        
        # Mean line
        mean_line = DashedLine(
            axes.c2p(0, 0), 
            axes.c2p(0, stats.norm.pdf(0, 0, 1)),
            color=RED_C,
            stroke_width=3
        )
        # Smaller font size for mean label
        mean_label = Text("Mean (μ)", font="Arial", color=RED_C, font_size=20)
        mean_label.next_to(mean_line, UP, buff=0.1)
        
        self.play(Create(axes), Create(axes_labels))
        self.play(Create(normal_dist))
        self.wait(1)
        self.play(Create(mean_line), Write(mean_label))
        
        # Explanation text with reduced font size
        explanation = Text(
            "In scientific measurements, data often follows a normal distribution",
            font="Arial", font_size=20, color=LIGHT_GRAY
        )
        explanation.to_edge(DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(2)
        
        self.play(FadeOut(explanation))
        
        # Standard deviation explanation with reduced font size
        sd_explanation = Text(
            "Standard deviation (σ) measures the spread of data",
            font="Arial", font_size=20, color=LIGHT_GRAY
        )
        sd_explanation.to_edge(DOWN, buff=0.5)
        
        # Highlight 1 sigma
        area_1sigma = axes.get_area(
            normal_dist,
            x_range=[-1, 1],
            color=BLUE_C,
            opacity=0.3
        )
        
        sigma_braces = []
        sigma_labels = []
        
        # 1 sigma with adjusted positioning and smaller font
        brace_1sigma = BraceBetweenPoints(axes.c2p(-1, 0), axes.c2p(1, 0), color=YELLOW_D)
        brace_1sigma.shift(DOWN * 0.1)  # Move down slightly to avoid overlap
        label_1sigma = Text("1σ", font="Arial", color=YELLOW_D, font_size=20)
        label_1sigma.next_to(brace_1sigma, DOWN, buff=0.1)
        sigma_braces.append(brace_1sigma)
        sigma_labels.append(label_1sigma)
        
        self.play(Write(sd_explanation))
        self.play(Create(area_1sigma), Create(brace_1sigma), Write(label_1sigma))
        self.wait(2)
        
        # Clear for the next section
        all_objects = VGroup(
            title, axes, axes_labels, normal_dist, mean_line, mean_label,
            sd_explanation, area_1sigma, brace_1sigma, label_1sigma
        )
        self.play(FadeOut(all_objects))

    def explain_sigma_levels(self):
        title = Text("Sigma (σ) Levels and Confidence", font="Arial", color=BLUE_C, font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create axes for the normal distribution with sigma regions
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 0.45, 0.1],
            x_length=12,
            y_length=5,
            axis_config={"color": LIGHT_GRAY},
        )
        
        # Reduced font size for axis labels
        x_label = Text("Standard Deviations from Mean (σ)", font_size=20, color=LIGHT_GRAY).next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = Text("Probability Density", font_size=20, color=LIGHT_GRAY).next_to(axes.y_axis, LEFT, buff=0.3).rotate(90 * DEGREES)
        axes_labels = VGroup(x_label, y_label)
        
        # Plot the normal distribution
        normal_dist = axes.plot(lambda x: stats.norm.pdf(x, 0, 1), color=WHITE)
        
        self.play(Create(axes), Create(axes_labels), Create(normal_dist))
        
        # Mean line
        mean_line = DashedLine(
            axes.c2p(0, 0), 
            axes.c2p(0, stats.norm.pdf(0, 0, 1)),
            color=RED_C,
            stroke_width=3
        )
        mean_label = Text("Mean", font="Arial", color=RED_C, font_size=20)
        mean_label.next_to(mean_line, UP, buff=0.1)
        
        self.play(Create(mean_line), Write(mean_label))
        self.wait(1)
        
        # Create sigma regions
        sigma_colors = {
            1: BLUE_D,
            2: GREEN_D,
            3: YELLOW_D,
            5: PURPLE_D
        }
        
        sigma_regions = {}
        sigma_braces = {}
        sigma_labels = {}
        sigma_info = {}
        
        # Confidence levels text - reduced font size
        confidence_text = {
            1: "1σ: 68% confidence (1-in-3 chance of random fluctuation)",
            2: "2σ: 95% confidence (1-in-20 chance of random fluctuation)",
            3: "3σ: 99.7% confidence (1-in-370 chance of random fluctuation)",
            5: "5σ: 99.9999% confidence (1-in-3.5 million chance of random fluctuation)"
        }
        
        # First, show all regions
        for sigma, color in sigma_colors.items():
            region = axes.get_area(
                normal_dist,
                x_range=[-sigma, sigma],
                color=color,
                opacity=0.3
            )
            sigma_regions[sigma] = region
        
        self.play(*[Create(region) for region in sigma_regions.values()])
        self.wait(1)
        
        # Then focus on each region one by one
        for sigma, color in sigma_colors.items():
            # Hide other regions temporarily
            other_regions = [r for s, r in sigma_regions.items() if s != sigma]
            self.play(
                *[FadeOut(r) for r in other_regions],
                run_time=0.7
            )
            
            # Add brace and label
            brace = BraceBetweenPoints(
                axes.c2p(-sigma, 0),
                axes.c2p(sigma, 0),
                color=color
            )
            
            # Adjust vertical position of brace to avoid overlap with axis
            brace.shift(DOWN * 0.1 * sigma)
            
            # Reduced font size for sigma labels
            label = Text(f"{sigma}σ", font="Arial", color=color, font_size=22)
            label.next_to(brace, DOWN, buff=0.1)
            
            sigma_braces[sigma] = brace
            sigma_labels[sigma] = label
            
            # Create info text with smaller font
            info = Text(
                confidence_text[sigma],
                font="Arial", font_size=20, color=LIGHT_GRAY
            )
            info.to_edge(DOWN, buff=0.5)
            sigma_info[sigma] = info
            
            self.play(
                Create(brace),
                Write(label),
                Write(info)
            )
            self.wait(2)
            
            # Clean up for next sigma level
            self.play(
                FadeOut(brace),
                FadeOut(label),
                FadeOut(info)
            )
            
            # Bring back all regions
            self.play(
                *[FadeIn(r) for r in other_regions],
                run_time=0.7
            )
        
        # Show all braces together with adjusted positions
        all_braces = []
        all_labels = []
        
        for sigma, color in sigma_colors.items():
            brace = BraceBetweenPoints(
                axes.c2p(-sigma, 0),
                axes.c2p(sigma, 0),
                color=color
            )
            
            # Adjust vertical position to avoid overlap - more spacing
            brace.shift(DOWN * (sigma - 1) * 0.4)
            
            label = Text(f"{sigma}σ", font="Arial", color=color, font_size=22)
            label.next_to(brace, DOWN, buff=0.1)
            
            all_braces.append(brace)
            all_labels.append(label)
        
        self.play(
            *[Create(brace) for brace in all_braces],
            *[Write(label) for label in all_labels]
        )
        
        # Summary text with reduced font size
        summary = Text(
            "Higher sigma values = stronger statistical significance",
            font="Arial", font_size=24, color=LIGHT_GRAY
        )
        summary.to_edge(DOWN, buff=0.5)
        
        self.play(Write(summary))
        self.wait(2)
        
        # Clean up
        self.play(
            FadeOut(VGroup(
                title, axes, axes_labels, normal_dist, mean_line, mean_label,
                *sigma_regions.values(), *all_braces, *all_labels, summary
            ))
        )

    def real_world_examples(self):
        title = Text("Scientific Standards for Discovery", font="Arial", color=BLUE_C, font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create titles for columns with reduced font size
        field_title = Text("Field", font_size=22, color=YELLOW_D)
        standard_title = Text("Standard", font_size=22, color=YELLOW_D)
        chance_title = Text("Random Chance", font_size=22, color=YELLOW_D)
        application_title = Text("Application", font_size=22, color=YELLOW_D)
        
        # Position titles with more spacing
        field_title.to_corner(UL).shift(DOWN * 1.2 + RIGHT * 2)
        standard_title.next_to(field_title, RIGHT, buff=1.7)
        chance_title.next_to(standard_title, RIGHT, buff=1.7)
        application_title.next_to(chance_title, RIGHT, buff=1.7)
        
        # Create header row
        header_row = VGroup(field_title, standard_title, chance_title, application_title)
        
        # Create data for rows
        fields = ["Physics", "Astronomy", "Medicine", "Social Science"]
        standards = ["5σ", "3σ - 5σ", "2σ", "2σ"]
        chances = ["1 in 3.5 million", "1 in 370 - 3.5 million", "1 in 20", "1 in 20"]
        applications = ["Particle discovery (Higgs Boson)", "New celestial object detection", "Clinical trial results", "Statistical hypothesis testing"]
        
        # Create text objects for each cell with reduced font size
        all_rows = []
        for i in range(4):
            field = Text(fields[i], font_size=18)
            standard = Text(standards[i], font_size=18)
            chance = Text(chances[i], font_size=18)
            application = Text(applications[i], font_size=18)
            
            field.move_to(field_title.get_center() + DOWN * (i + 1) * 0.8)
            standard.move_to(standard_title.get_center() + DOWN * (i + 1) * 0.8)
            chance.move_to(chance_title.get_center() + DOWN * (i + 1) * 0.8)
            application.move_to(application_title.get_center() + DOWN * (i + 1) * 0.8)
            
            row = VGroup(field, standard, chance, application)
            all_rows.append(row)
        
        # Create the table
        table_content = VGroup(*all_rows)
        table = VGroup(header_row, table_content)
        
        self.play(Create(table))
        self.wait(2)
        
        # Highlight physics row for emphasis (5σ standard)
        physics_row = all_rows[0]  # Physics row
        self.play(physics_row.animate.set_color(PURPLE_D))
        
        # Add explanation with reduced font size
        explanation = Text(
            "For extraordinary claims like new particle discovery,\na 5σ threshold is required",
            font="Arial", font_size=20, color=LIGHT_GRAY,
            line_spacing=1.5
        )
        explanation.to_edge(DOWN, buff=0.5)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # Clean up
        self.play(FadeOut(VGroup(title, table, explanation)))

    def conclusion(self):
        title = Text("When is a Discovery Real?", font="Arial", color=BLUE_C, font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create axes for simplified visualization
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 0.45, 0.1],
            x_length=10,
            y_length=5,
            axis_config={"color": LIGHT_GRAY},
        )
        
        # Plot the normal distribution
        normal_dist = axes.plot(lambda x: stats.norm.pdf(x, 0, 1), color=WHITE)
        
        self.play(Create(axes), Create(normal_dist))
        
        # Add vertical lines for different sigma levels
        sigma_lines = {}
        sigma_labels = {}
        sigma_texts = {}
        
        descriptions = {
            1: "1σ (68%): Likely noise",
            2: "2σ (95%): Possibly real",
            3: "3σ (99.7%): Probably real",
            5: "5σ (99.9999%): Definitely real"
        }
        
        colors = {
            1: BLUE_D,
            2: GREEN_D,
            3: YELLOW_D,
            5: PURPLE_D
        }
        
        # Create lines for each sigma level with reduced font size and better spacing
        for sigma, color in colors.items():
            # Right side line
            line = DashedLine(
                axes.c2p(sigma, 0),
                axes.c2p(sigma, stats.norm.pdf(sigma, 0, 1)),
                color=color,
                stroke_width=3
            )
            
            label = Text(f"{sigma}σ", font="Arial", color=color, font_size=18)
            label.next_to(line, UP, buff=0.1)
            
            # Position text at different vertical levels to avoid overlap
            text = Text(
                descriptions[sigma],
                font="Arial", font_size=18, color=color
            )
            # Stagger text positions to avoid overlap
            text.to_edge(RIGHT, buff=1.5).shift(LEFT * 1.5 + UP * (2.5 - sigma * 0.7))
            
            sigma_lines[sigma] = line
            sigma_labels[sigma] = label
            sigma_texts[sigma] = text
            
        # Show all simultaneously
        self.play(
            *[Create(line) for line in sigma_lines.values()],
            *[Write(label) for label in sigma_labels.values()],
            *[Write(text) for text in sigma_texts.values()]
        )
        
        # Add final conclusion text with reduced font size
        conclusion_text = Text(
            "3σ means \"interesting enough to investigate further\"\n5σ means \"conclusive evidence\"",
            font="Arial", font_size=20, color=LIGHT_GRAY,
            line_spacing=1.5
        )
        conclusion_text.to_edge(DOWN, buff=0.4)
        
        self.play(Write(conclusion_text))
        self.wait(3)
        
        # Final fade out
        self.play(FadeOut(VGroup(
            title, axes, normal_dist,
            *sigma_lines.values(), *sigma_labels.values(), *sigma_texts.values(),
            conclusion_text
        )))
        
        # Show final message with reduced font size
        final_message = Text(
            "Statistical significance helps scientists\ndistinguish real discoveries from random chance",
            font="Arial", color=BLUE_C, font_size=30,
            line_spacing=1.5
        )
        final_message.move_to(ORIGIN)
        
        self.play(Write(final_message))
        self.wait(3)
        self.play(FadeOut(final_message))


if __name__ == "__main__":
    # You can configure rendering settings here if needed
    config.background_color = "#1E1E1E"  # Match the scene background
    config.frame_width = 1920 / 100  # HD width
    config.frame_height = 1080 / 100  # HD height
    config.frame_rate = 30  # Standard frame rate
    config.pixel_width = 1920  # HD resolution
    config.pixel_height = 1080  # HD resolution
    
    # Render the scene
    scene = StatisticalSignificance()
    scene.render()