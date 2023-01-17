from manimlib import *


class PythagoreanTree(Scene):
    def __init__(self, **kwargs):
        super(PythagoreanTree, self).__init__(**kwargs)
        # 深度
        self.level = 7
        # 所有方块的动画
        self.blocks_anim = [[] for _ in range(self.level)]

        # 可根据需要设置多个颜色,按照不同的level上色即可
        self.color = RED_B
        self.opacity = 0.7

        self.alpha = np.arccos(0.8)
        self.beta = PI / 2 - self.alpha

        # 第一个方块
        self.trunk = Square(fill_color=self.color, fill_opacity=self.opacity).shift(2.5 * DOWN)
        self.blocks_anim[0].append(FadeIn(self.trunk, shift=UP))

    def branch(self, block: Square, level):
        """
        为一个block构造树枝
        """
        # 父方块的锚点
        block_points = block.get_points()

        # 左右两个树枝
        lbranch, rbranch = block.copy(), block.copy()
        # 缩放
        lbranch.scale(0.8, about_point=block_points[3])
        rbranch.scale(0.6, about_point=block_points[0])
        # 平移
        lbranch.shift(0.8 * (block_points[3] - block_points[5]))
        rbranch.shift(0.6 * (block_points[11] - block_points[9]))
        # 旋转
        lbranch.rotate(angle=self.alpha, about_point=block_points[3])
        rbranch.rotate(angle=-self.beta, about_point=block_points[0])

        self.blocks_anim[level + 1].extend((ReplacementTransform(block.copy(), lbranch),
                                            ReplacementTransform(block.copy(), rbranch)))
        return lbranch, rbranch

    def grow(self, block: Square, level):
        """
        生成勾股树

        勾股树可看作一颗完全二叉树,因此采用递归来构造
        """
        # 到达叶子节点所在层级(level最低为0,最高为self.level-1)时停止
        if level == self.level - 1:
            return
        # 构造出左右两个树枝
        lbranch, rbranch = self.branch(block, level)
        # 在左树枝上生成一颗更小的勾股树
        self.grow(lbranch, level + 1)
        # 右树枝同理
        self.grow(rbranch, level + 1)

    def construct(self):
        self.grow(self.trunk, 0)

        for anims in self.blocks_anim:
            self.play(*anims)