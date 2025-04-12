压力毯数据设置阈值去除空采基线噪声的方法:

1. 将压力图转直方图；
2. 寻找直方图中两侧边界；
3. 从压力值大的边界开始向前扫描，压力值依次叠加；
4. 计算叠加压力值与压力值总和的比例；
5. 比例90-99%，根据收敛情况，选择特定比例下的压力值作为阈值， 低于阈值的压力值设置为0，高于阈值的压力值保持不变。

When the test subject is lying on the pressure-sensing mattress, the proposed system can detect the pressure distribution on each part of the mattressand display the pressure distribution image of the test subject.
However, even if there is no subject on the mattress, the pressure sensor on the mattress might return a nonzero value of the pressure due to various factors, which is called noise interference; hence, the system needs to filter out such noise [1].

[1] Kau L J, Wang M Y, Zhou H. Pressure-sensor-based sleep status and quality evaluation system[J]. IEEE Sensors Journal, 2023, 23(9): 9739-9754.
[2] https://github.com/JonesChau/Sleep-Parameter
