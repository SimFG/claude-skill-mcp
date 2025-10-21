import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.image as mpimg
from PIL import Image, ImageDraw, ImageFilter
import random

def create_stellar_river():
    # 创建高分辨率画布
    fig, ax = plt.subplots(figsize=(16, 12), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 75)
    ax.axis('off')
    
    # 设置背景 - 深邃的宇宙背景
    background_colors = ['#000814', '#001d3d', '#000000', '#0a0a23']
    for i, color in enumerate(background_colors):
        alpha = 0.3 if i > 0 else 1.0
        rect = plt.Rectangle((0, 0), 100, 75, facecolor=color, alpha=alpha, zorder=-10)
        ax.add_patch(rect)
    
    # 创建星河主体 - 流动的星云
    def create_nebula_stream():
        # 主星河流动路径
        x = np.linspace(0, 100, 500)
        y_base = 37.5 + 15 * np.sin(x * 0.08) + 8 * np.sin(x * 0.15)
        
        # 添加随机扰动创造自然流动感
        for i in range(len(x)):
            if i % 10 == 0:
                y_base[i] += random.uniform(-3, 3)
        
        # 星河核心 - 明亮的恒星带
        for i in range(len(x)-1):
            if i % 3 == 0:
                width = random.uniform(0.5, 2.5)
                brightness = random.uniform(0.6, 1.0)
                
                # 使用渐变色彩表现星河的温度变化
                colors = ['#ffd60a', '#f77f00', '#d62828', '#003049', '#669bbc']
                color = random.choice(colors)
                
                ax.plot(x[i:i+2], y_base[i:i+2], color=color, linewidth=width, 
                       alpha=brightness, zorder=5)
                
                # 添加光晕效果
                for halo_size in [0.1, 0.2]:
                    ax.plot(x[i:i+2], y_base[i:i+2], color=color, 
                           linewidth=width + halo_size, alpha=brightness * 0.3, zorder=4)
    
    create_nebula_stream()
    
    # 添加星云团块
    def add_nebula_clusters():
        cluster_centers = [(20, 45), (45, 30), (70, 50), (85, 35), (30, 60)]
        
        for center_x, center_y in cluster_centers:
            # 每个星云团块包含多个层次
            for layer in range(3):
                num_stars = random.randint(15, 30)
                radius_base = random.uniform(3, 8)
                
                for _ in range(num_stars):
                    angle = random.uniform(0, 2*np.pi)
                    distance = random.uniform(0, radius_base)
                    
                    x_pos = center_x + distance * np.cos(angle)
                    y_pos = center_y + distance * np.sin(angle)
                    
                    # 确保星星在画布范围内
                    if 0 <= x_pos <= 100 and 0 <= y_pos <= 75:
                        size = random.uniform(0.1, 0.8)
                        alpha = random.uniform(0.4, 0.9)
                        
                        # 星云色彩 - 从蓝紫色到橙红色
                        nebula_colors = ['#4cc9f0', '#4361ee', '#3a0ca3', '#7209b7', '#f72585', '#f77f00']
                        color = random.choice(nebula_colors)
                        
                        star = Circle((x_pos, y_pos), size, facecolor=color, alpha=alpha, zorder=3)
                        ax.add_patch(star)
                        
                        # 添加星星的光晕
                        for halo_factor in [2, 4]:
                            halo = Circle((x_pos, y_pos), size * halo_factor, 
                                        facecolor=color, alpha=alpha * 0.2 / halo_factor, zorder=2)
                            ax.add_patch(halo)
    
    add_nebula_clusters()
    
    # 添加遥远的背景恒星
    def add_background_stars():
        num_background_stars = 800
        
        for _ in range(num_background_stars):
            x_pos = random.uniform(0, 100)
            y_pos = random.uniform(0, 75)
            size = random.uniform(0.02, 0.15)
            alpha = random.uniform(0.1, 0.6)
            
            # 背景恒星多为冷色调
            bg_colors = ['#ffffff', '#e0e0e0', '#b8b8b8', '#87ceeb', '#add8e6']
            color = random.choice(bg_colors)
            
            star = Circle((x_pos, y_pos), size, facecolor=color, alpha=alpha, zorder=1)
            ax.add_patch(star)
    
    add_background_stars()
    
    # 添加星际尘埃和气体
    def add_interstellar_medium():
        # 使用渐变矩形模拟星际尘埃带
        dust_bands = [
            {'x': 10, 'y': 20, 'width': 30, 'height': 3, 'color': '#2c1810', 'alpha': 0.2},
            {'x': 50, 'y': 55, 'width': 25, 'height': 2, 'color': '#1a1a2e', 'alpha': 0.15},
            {'x': 75, 'y': 25, 'width': 20, 'height': 4, 'color': '#16213e', 'alpha': 0.18}
        ]
        
        for band in dust_bands:
            rect = plt.Rectangle((band['x'], band['y']), band['width'], band['height'],
                               facecolor=band['color'], alpha=band['alpha'], zorder=0)
            ax.add_patch(rect)
    
    add_interstellar_medium()
    
    # 添加亮星（焦点恒星）
    def add_bright_stars():
        bright_star_positions = [(25, 40), (60, 35), (80, 45), (15, 55)]
        
        for x_pos, y_pos in bright_star_positions:
            # 主恒星
            main_star = Circle((x_pos, y_pos), 0.4, facecolor='#ffffff', alpha=1.0, zorder=10)
            ax.add_patch(main_star)
            
            # 多层光晕
            for i, (size, alpha) in enumerate([(1.0, 0.8), (2.0, 0.4), (3.5, 0.2)]):
                halo = Circle((x_pos, y_pos), size, facecolor='#ffd60a', alpha=alpha, zorder=9-i)
                ax.add_patch(halo)
            
            # 星芒效果
            spike_length = 5
            for angle in [0, 45, 90, 135]:
                rad_angle = np.radians(angle)
                dx = spike_length * np.cos(rad_angle)
                dy = spike_length * np.sin(rad_angle)
                
                ax.plot([x_pos - dx, x_pos + dx], [y_pos - dy, y_pos + dy], 
                       color='#ffffff', linewidth=0.5, alpha=0.7, zorder=8)
    
    add_bright_stars()
    
    # 添加色彩平衡和深度
    def add_color_gradients():
        # 顶部蓝色渐变 - 表示深空
        for i in range(20):
            alpha = 0.02 * (20 - i) / 20
            rect = plt.Rectangle((0, 75 - i), 100, 1, facecolor='#1e3a8a', alpha=alpha, zorder=-5)
            ax.add_patch(rect)
        
        # 底部紫色渐变 - 表示星云边缘
        for i in range(15):
            alpha = 0.015 * (15 - i) / 15
            rect = plt.Rectangle((0, i), 100, 1, facecolor='#7c3aed', alpha=alpha, zorder=-5)
            ax.add_patch(rect)
    
    add_color_gradients()
    
    plt.tight_layout()
    return fig, ax

# 创建星河图像
fig, ax = create_stellar_river()
plt.savefig('stellar-river.png', dpi=300, bbox_inches='tight', 
            facecolor='black', edgecolor='none')
plt.close()

print("星河主题图片已创建完成！")