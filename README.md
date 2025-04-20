# Statistical Significance Visualization

A Manim animation that visually explains the concept of statistical significance (sigma levels) in scientific observations.

## Overview

This project uses the mathematical animation library [Manim](https://www.manim.community/) to create an educational animation about statistical significance. The animation explains what sigma (σ) values mean in scientific contexts, how they relate to confidence levels, and why different scientific fields require different sigma thresholds for accepting new discoveries.


## Content

The animation covers:

1. **Introduction** - A brief overview of statistical significance
2. **Normal Distribution** - Explanation of the normal distribution curve and what it represents
3. **Sigma Levels** - Detailed visualization of different confidence levels:
   - 1σ (68%): 1-in-3 chance of random fluctuation
   - 2σ (95%): 1-in-20 chance of random fluctuation
   - 3σ (99.7%): 1-in-370 chance of random fluctuation
   - 5σ (99.9999%): 1-in-3.5 million chance of random fluctuation
4. **Real-World Examples** - How different scientific disciplines apply various sigma thresholds
5. **Conclusion** - The practical importance of higher sigma values for extraordinary scientific claims

## Requirements

- Python 3.7+ (3.8+ recommended)
- Manim library (community edition)
- NumPy
- SciPy
- FFmpeg
- LaTeX distribution (like TeX Live or MiKTeX)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/statistical-significance.git
cd statistical-significance
```

2. Install the required Python packages:
```bash
pip install manim numpy scipy
```

3. Install system dependencies:

**Linux (Ubuntu/Debian):**
```bash
apt update && apt install -y ffmpeg texlive texlive-latex-extra texlive-fonts-recommended texlive-science
```

**macOS:**
```bash
brew install ffmpeg mactex
```

**Windows:**
- Install [MiKTeX](https://miktex.org/download)
- Install [FFmpeg](https://ffmpeg.org/download.html)

## Usage

### Command Line

To render the animation:

```bash
manim -pqh statistical_significance.py StatisticalSignificance
```

Parameters:
- `-p`: Preview the animation once it's done rendering
- `-q`: Quality (h for high, m for medium, l for low)
- `-r`: Resolution (e.g., `-r 1920,1080` for 1080p)

### Google Colab

This animation can also be rendered in Google Colab. Use the following code:

```python
!pip install manim numpy scipy
!apt update && apt install -y ffmpeg texlive texlive-latex-extra texlive-fonts-recommended texlive-science

%%manim -p -r 1920,1080 -v WARNING StatisticalSignificance
# [Insert the entire script here]
```

## Customization

You can customize various aspects of the animation:

- Modify the colors in the `sigma_colors` dictionary
- Adjust the text content in the `confidence_text` and `descriptions` dictionaries
- Change the scientific fields and standards in the real-world examples section

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The [Manim Community](https://www.manim.community/) for developing this amazing animation engine
- 3Blue1Brown (Grant Sanderson) for creating the original Manim library and inspiring mathematical animations
